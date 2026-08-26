#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for I-129: the lithium cation's enthalpy of formation in LithiumPrimaryThermo.

The report is ``docs/i129-lithium-cation-enthalpy.md``. This file is the executable half
of it. Every number the report quotes that can be re-derived is re-derived here, so a
later change that moves one fails a test rather than silently contradicting a document.

The defect, in one line: the shipped ``[Lip]`` sat 375.363 kJ/mol above ``[Li]`` where
lithium's ionisation energy is 520.221, and the entropy of the same pair was exactly
R ln 2 - enthalpy wrong, entropy right. The enthalpy has been replaced from NIST-JANAF
table Li-006.

Five groups:

1. **The corrected value against its source**, by the two independent conversion routes
   that carry JANAF's electron convention into this database's ion convention.
2. **The relationship that was wrong**, now asserted rather than assumed - including the
   1.73 kJ/mol residual that was deliberately left standing rather than tuned away.
3. **The diagnosis, as executable claims.** The correction chain is charge-blind; the
   BAC cannot reach a monatomic species; no lithium atom energy ships at any level of
   theory. Each of these is a load-bearing step in the argument that the original number
   could not have come from a lithium cation calculation, so each is measured here
   rather than asserted in prose.
3. **What did not change** - the other 131 entries, and the entropy and heat capacity of
   ``[Lip]`` itself.
4. **The regeneration hazard**, because the failure mode this correction introduces is
   that someone re-runs ARC and silently reverts it. The library header has to keep
   saying so.

Run with the runtime pinned::

    cd /home/alon/Code/RMG-database-i129-lithium-cation
    PYTHONPATH=/home/alon/Code/RMG-Py-i123-integration \\
        python -m pytest test/test_lithium_cation_enthalpy.py -q

``test/conftest.py`` pins ``database.directory`` to this worktree before collection; the
fixtures below assert that pin rather than trusting it.
"""

import math
import os
import subprocess
import tempfile

import numpy as np
import pytest

from rmgpy import settings
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.molecule import Molecule
from rmgpy.species import Species

import arkane.encorr.data as aedata
from arkane.encorr.corr import get_atom_correction, get_bac
from arkane.exceptions import AtomEnergyCorrectionError
from arkane.modelchem import LevelOfTheory

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,
                                             'input'))
REPO_ROOT = os.path.dirname(THIS_DATABASE)
LIBRARY_DIR = os.path.join(THIS_DATABASE, 'thermo', 'libraries')
LIBRARY = 'LithiumPrimaryThermo'
LIBRARY_FILE = os.path.join(LIBRARY_DIR, LIBRARY + '.py')

#: The branch tip immediately before this ticket's edit, used as the negative control.
BASE_COMMIT = '2d7123b08'

R = 8.31446261815324
T0 = 298.15
#: kJ/mol per eV, CODATA.
EV = 96.48533212331
#: kJ/mol per Hartree, CODATA 2018.
HARTREE = 2625.4996394799

# --- the source, quoted so a test can check the file against it -------------------
#: NIST-JANAF Fourth Edition, table Li-006 "Lithium, Ion (Li+)", Li1+(g).
#: Electron convention, in which the released electron carries 5/2 R T.
JANAF_LIP_H0 = 677.947                             # kJ/mol, T = 0 row
JANAF_LIP_H298_ELECTRON_CONVENTION = 685.719       # kJ/mol, T = 298.15 row
JANAF_LIP_S298 = 133.017                           # J/(mol*K)
JANAF_LIP_CP298 = 20.786                           # J/(mol*K)
#: NIST-JANAF Li-001 "Lithium (Li)", Li1(ref): H(298.15) - H(0) of the element.
JANAF_LI_CR_DH_298_0 = 4.622                       # kJ/mol
#: NIST-JANAF Li-005 "Lithium (Li)", Li1(g): the neutral gas-phase atom.
JANAF_LI_G_H0 = 157.725                            # kJ/mol
JANAF_LI_G_H298 = 159.30                           # kJ/mol
#: 5/2 R T at 298.15 K, which is what JANAF prices a monatomic gas' and the electron's
#: thermal increment at.
DH_298_0_MONATOMIC = 6.197                         # kJ/mol

#: NIST Atomic Spectra Database ver. 5.12, doi:10.18434/T4W30F, Li I.
IE_LI_EV = 5.391714996

#: What is now in the file.
ENTERED_E0 = 673.325                               # kJ/mol, convention-free at 0 K
ENTERED_H298 = 679.522                             # kJ/mol, ion convention
#: What ARC wrote, and this ticket replaced.
ORIGINAL_E0 = 526.738                              # kJ/mol
ORIGINAL_H298 = 532.936                            # kJ/mol
#: The defect, as I-127 measured and pinned it.
ORIGINAL_RISE_OVER_NEUTRAL = 375.363               # kJ/mol
ORIGINAL_DISCREPANCY = -144.858                    # kJ/mol

#: exact non-relativistic total energies, infinite nuclear mass, in Hartree.
#: Li+ 1s(2) 1S: Drake's high-precision variational result. Li 1s(2)2s 2S: Puchalski &
#: Pachucki. E(Li) at the numerical Hartree-Fock limit.
E_EXACT_LIP = -7.2799134
E_EXACT_LI = -7.4780603
E_HF_LIMIT_LI = -7.4327269

LI = 'multiplicity 2\n1 Li u1 p0 c0\n'
LIP = '1 Li u0 p0 c+1\n'


def _species(adjacency_list, label=''):
    return Species(label=label,
                   molecule=[Molecule().from_adjacency_list(adjacency_list)])


@pytest.fixture(scope='module')
def pinned():
    """Assert the pin rather than trusting it. A run against another checkout would
    otherwise produce a green that means nothing, which has happened on this campaign."""
    assert settings['database.directory'] == THIS_DATABASE, (
        f"database.directory is {settings['database.directory']!r}, not this worktree")
    return THIS_DATABASE


@pytest.fixture(scope='module')
def thermo_db(pinned):
    db = ThermoDatabase()
    db.load_libraries(LIBRARY_DIR)
    on_disk = [f for f in os.listdir(LIBRARY_DIR) if f.endswith('.py')]
    assert len(db.libraries) == len(on_disk), (
        'a library failed to load; a sweep over a short dict is a silent green')
    return db


@pytest.fixture(scope='module')
def library(thermo_db):
    return thermo_db.libraries[LIBRARY]


@pytest.fixture(scope='module')
def cation(library):
    return library.entries['[Lip]'].data


@pytest.fixture(scope='module')
def neutral(library):
    return library.entries['[Li]'].data


@pytest.fixture(scope='module')
def original_library(pinned):
    """LithiumPrimaryThermo as it stood at ``BASE_COMMIT``, loaded from git.

    A negative control written from remembered numbers tests the memory. This one tests
    the edit.
    """
    src = subprocess.run(
        ['git', '-C', REPO_ROOT, 'show',
         f'{BASE_COMMIT}:input/thermo/libraries/{LIBRARY}.py'],
        capture_output=True, text=True, check=True).stdout
    tmpdir = tempfile.mkdtemp()
    with open(os.path.join(tmpdir, LIBRARY + '.py'), 'w') as f:
        f.write(src)
    db = ThermoDatabase()
    db.load_libraries(tmpdir, libraries=[LIBRARY])
    return db.libraries[LIBRARY]


# =====================================================================================
# 1. the corrected value against its source
# =====================================================================================

def test_the_source_table_is_electron_convention_by_its_own_arithmetic():
    """Before converting a number out of JANAF, establish which convention it is in from
    the table's own columns rather than from the front matter.

    Li(cr) -> Li+(g) + e-. Between 0 K and 298.15 K the products gain the cation's
    thermal increment and, IF the electron is priced, the electron's; the reactant loses
    the crystal's. JANAF's own two rows differ by exactly the priced version.
    """
    published = JANAF_LIP_H298_ELECTRON_CONVENTION - JANAF_LIP_H0
    electron_convention = (DH_298_0_MONATOMIC          # the cation
                           + DH_298_0_MONATOMIC        # the electron, priced
                           - JANAF_LI_CR_DH_298_0)     # the element reference state
    ion_convention = DH_298_0_MONATOMIC - JANAF_LI_CR_DH_298_0
    assert published == pytest.approx(electron_convention, abs=0.001)
    assert abs(published - ion_convention) == pytest.approx(DH_298_0_MONATOMIC,
                                                            abs=0.001)


def test_the_entered_enthalpy_is_the_ion_convention_value_by_two_routes(cation):
    """The conversion, by two routes that do not share an intermediate. If they disagree
    the transcription is wrong, and the disagreement says by how much.
    """
    # route 1: through E0 at 0 K, where the two conventions coincide
    e0 = JANAF_LIP_H0 - JANAF_LI_CR_DH_298_0
    route_1 = e0 + DH_298_0_MONATOMIC
    # route 2: straight off the 298.15 K row, subtracting the priced electron
    route_2 = JANAF_LIP_H298_ELECTRON_CONVENTION - DH_298_0_MONATOMIC

    assert route_1 == pytest.approx(route_2, abs=0.001), (
        f'the two conversion routes disagree by {abs(route_1 - route_2):.4f} kJ/mol')
    assert e0 == pytest.approx(ENTERED_E0, abs=0.001)
    assert route_1 == pytest.approx(ENTERED_H298, abs=0.001)

    assert cation.E0.value_si / 1000.0 == pytest.approx(ENTERED_E0, abs=0.001)
    assert cation.get_enthalpy(T0) / 1000.0 == pytest.approx(ENTERED_H298, abs=0.001)


def test_the_entered_value_is_not_the_electron_convention_one(cation):
    """The failure this database is most exposed to: entering JANAF's published number
    unconverted. It is 6.197 kJ/mol away, small enough to look like rounding."""
    entered = cation.get_enthalpy(T0) / 1000.0
    assert entered != pytest.approx(JANAF_LIP_H298_ELECTRON_CONVENTION, abs=1.0)
    assert JANAF_LIP_H298_ELECTRON_CONVENTION - entered == pytest.approx(
        DH_298_0_MONATOMIC, abs=0.001)


def test_the_nasa_polynomial_carries_the_enthalpy_the_e0_field_claims(cation):
    """``E0`` and the polynomials are two places the same number lives. RMG reads the
    polynomial; a reader reads ``E0``. They have to agree, in both temperature ranges."""
    for poly in cation.polynomials:
        assert poly.c0 == 2.5                    # monatomic, and unchanged
        assert poly.c5 * R / 1000.0 == pytest.approx(ENTERED_E0, abs=0.001)
    assert cation.E0.value_si / 1000.0 == pytest.approx(
        cation.polynomials[0].c5 * R / 1000.0, abs=0.001)


@pytest.mark.parametrize('T', [300.0, 500.0, 1000.0, 2000.0, 3000.0])
def test_the_entry_stays_five_halves_R_across_the_whole_range(cation, T):
    """Li+ is 1s(2) 1S, a closed shell with no low-lying electronic states, so JANAF
    tabulates a flat 5/2 R to 6000 K. This ticket did not touch Cp; the test is here so
    that a future edit to the enthalpy cannot quietly deform the polynomial."""
    assert cation.get_heat_capacity(T) == pytest.approx(2.5 * R, abs=0.001)
    assert cation.get_heat_capacity(T) == pytest.approx(JANAF_LIP_CP298, abs=0.001)


# =====================================================================================
# 2. the relationship that was wrong
# =====================================================================================

def test_the_cation_now_rises_over_the_neutral_by_the_ionisation_energy(cation, neutral):
    """The headline. And the residual, which is the point of the whole exercise.

    521.950, not 520.221. The 1.729 kJ/mol excess is NOT slop: the cation came from JANAF
    absolutely while the neutral is still ARC's, and ARC's neutral is 1.73 kJ/mol below
    JANAF Li-005. Forcing the rise to equal the ionisation energy exactly would mean
    back-solving the cation from the target - the one thing this ticket was told not to
    do - so the residual is left visible and accounted for instead.
    """
    rise = (cation.get_enthalpy(T0) - neutral.get_enthalpy(T0)) / 1000.0
    ie = IE_LI_EV * EV
    assert ie == pytest.approx(520.221, abs=0.001)

    residual = rise - ie
    assert residual == pytest.approx(1.729, abs=0.01)
    assert abs(residual) < 4.184, 'residual is no longer within chemical accuracy'

    # and it is accounted for: it IS the shipped neutral's own error against JANAF
    neutral_error = neutral.get_enthalpy(T0) / 1000.0 - JANAF_LI_G_H298
    assert neutral_error == pytest.approx(-residual, abs=0.02)


def test_the_corrected_value_was_not_back_solved_from_the_ionisation_energy(cation,
                                                                           neutral):
    """The discriminating test. A value fitted to close against IE(Li) would put the
    cation at E0(neutral) + IE. The entered value is not that, and the gap is the
    neutral's own error - which is what a sourced number looks like and a fitted one
    does not."""
    fitted = neutral.E0.value_si / 1000.0 + IE_LI_EV * EV
    entered = cation.E0.value_si / 1000.0
    assert entered != pytest.approx(fitted, abs=0.5)
    assert entered - fitted == pytest.approx(1.729, abs=0.02)


def test_the_entropy_of_the_pair_is_the_degeneracy_ratio_and_was_not_touched(
        cation, neutral, original_library):
    """The entropy was never the defect: S(Li) - S(Li+) is R ln 2 exactly, the ratio of
    a 2S neutral's electronic degeneracy to a 1S cation's. This ticket corrected the
    enthalpy only, so the entropy must be bit-identical to ARC's."""
    gap = neutral.get_entropy(T0) - cation.get_entropy(T0)
    assert gap == pytest.approx(R * math.log(2.0), abs=0.001)

    was = original_library.entries['[Lip]'].data
    for T in (T0, 1000.0, 2500.0):
        assert cation.get_entropy(T) == was.get_entropy(T)


def test_the_retained_entropy_differs_from_janaf_by_far_less_than_the_defect(cation):
    """Honesty about what was left alone. The retained ARC entropy is 0.118 J/(mol*K)
    below JANAF Li-006, consistent with a 1 atm rather than 1 bar standard state
    (R ln 1.01325 = 0.109). That is 49x smaller than R ln 2 and 3 orders below the
    enthalpy defect, which is why it was out of scope - stated, not hidden."""
    delta = JANAF_LIP_S298 - cation.get_entropy(T0)
    assert delta == pytest.approx(0.118, abs=0.01)
    assert delta < R * math.log(2.0) / 10.0
    assert delta == pytest.approx(R * math.log(1.01325), abs=0.02)


# =====================================================================================
# 3. the diagnosis, as executable claims
# =====================================================================================

LOT = LevelOfTheory(method='ccsd(t)f12', basis='ccpvdzf12', software='molpro')


def test_the_atom_energy_correction_is_blind_to_charge():
    """Load-bearing step 1 of the diagnosis. Arkane's atom correction is keyed on element
    counts alone, so it is identical for a cation and its neutral and cancels exactly in
    a cation-minus-neutral gap. It therefore CANNOT be where a charge-specific error
    lives - which is what forces the defect down into the electronic energy.

    Nitrogen, because N ships an atom energy at this level and lithium does not.
    """
    neutral_n = Molecule().from_adjacency_list('multiplicity 4\n1 N u3 p1 c0\n')
    cation_n = Molecule().from_adjacency_list('multiplicity 3\n1 N u2 p1 c+1\n')
    assert neutral_n.get_net_charge() == 0
    assert cation_n.get_net_charge() == 1
    assert neutral_n.get_element_count() == cation_n.get_element_count() == {'N': 1}

    corr_neutral = get_atom_correction(LOT, neutral_n.get_element_count())
    corr_cation = get_atom_correction(LOT, cation_n.get_element_count())
    assert corr_cation == corr_neutral


def test_the_bond_additivity_correction_cannot_reach_a_monatomic_species():
    """Load-bearing step 2. The library header advertises p-type BACs; a species with no
    bonds receives none, of either charge. So the BAC cannot be the 144.86 kJ/mol
    either."""
    bac = get_bac(LOT, bonds={}, coords=np.array([[0.0, 0.0, 0.0]]), nums=[3],
                  bac_type='p', multiplicity=1)
    assert bac == 0.0


def test_no_lithium_atom_energy_ships_at_any_level_of_theory():
    """Load-bearing step 3, and the reason the original number could not be recomputed
    rather than replaced.

    Every lithium value in this library depends on an atom energy that was supplied to
    Arkane at run time through ``atomEnergies`` and never committed. Nothing in this
    repository can reproduce or audit any of them. If this test ever fails because
    somebody added one, that is good news and the library becomes regenerable - see the
    header warning in the library file.
    """
    with_li = [k for k, v in aedata.atom_energies.items() if 'Li' in v]
    assert with_li == [], (
        f'a lithium atom energy now ships at {with_li}; the regeneration warning in '
        f'{LIBRARY}.py should be revisited')
    assert len(aedata.atom_energies) > 50, 'the atom-energy table failed to load'

    with pytest.raises(AtomEnergyCorrectionError):
        get_atom_correction(LOT, {'Li': 1})

    # the enthalpy half of the correction does exist, and is what both charges receive
    assert (aedata.atom_hf['Li'] - aedata.atom_thermal['Li']) * 4.184 == pytest.approx(
        153.093, abs=0.001)


def test_the_original_number_implied_an_impossible_ionisation_energy(original_library):
    """The diagnosis itself, as arithmetic.

    Because the corrections cancel, the two ORIGINAL stored numbers implied a computed
    IE(Li) of 3.890 eV. For a variational wavefunction method E(Li+) cannot fall below
    the exact two-electron energy, so reaching that gap would require the same
    calculation's neutral lithium to sit ABOVE the Hartree-Fock limit - while that same
    neutral reproduces JANAF to 1.73 kJ/mol. The two energies cannot have come from one
    consistent calculation of this species pair.
    """
    was_cation = original_library.entries['[Lip]'].data
    was_neutral = original_library.entries['[Li]'].data
    rise = (was_cation.get_enthalpy(T0) - was_neutral.get_enthalpy(T0)) / 1000.0
    assert rise == pytest.approx(ORIGINAL_RISE_OVER_NEUTRAL, abs=0.01)

    implied_ie_hartree = rise / HARTREE
    assert implied_ie_hartree * HARTREE / EV == pytest.approx(3.890, abs=0.01)

    # what the neutral would have had to be for that gap to come from a real calculation
    needed_neutral = E_EXACT_LIP - implied_ie_hartree
    assert needed_neutral > E_HF_LIMIT_LI, (
        'the variational argument no longer holds; recheck the reference energies')
    assert (needed_neutral - E_HF_LIMIT_LI) * HARTREE == pytest.approx(25.85, abs=0.1)

    # and the exact energies do reproduce the spectroscopic ionisation energy, which is
    # what makes them usable as a bound
    assert (E_EXACT_LIP - E_EXACT_LI) * HARTREE / EV == pytest.approx(IE_LI_EV,
                                                                     abs=0.001)


def test_the_defect_was_far_larger_than_any_convention_choice(original_library):
    """Why it was never a reference-state question. 144.86 kJ/mol is 23x the entire
    6.197 kJ/mol difference between the electron and ion conventions."""
    was_cation = original_library.entries['[Lip]'].data
    was_neutral = original_library.entries['[Li]'].data
    discrepancy = ((was_cation.get_enthalpy(T0) - was_neutral.get_enthalpy(T0)) / 1000.0
                   - IE_LI_EV * EV)
    assert discrepancy == pytest.approx(ORIGINAL_DISCREPANCY, abs=0.01)
    assert abs(discrepancy) / DH_298_0_MONATOMIC == pytest.approx(23.4, abs=0.1)


# =====================================================================================
# 4. what did not change
# =====================================================================================

def test_exactly_one_entry_of_the_library_moved(library, original_library):
    """The negative control, against the pre-edit library from git rather than against
    numbers typed from memory."""
    assert len(library.entries) == len(original_library.entries) == 132

    moved = set()
    for label, now in library.entries.items():
        was = original_library.entries[label]
        for T in (T0, 1000.0, 2500.0):
            if (abs(now.data.get_enthalpy(T) - was.data.get_enthalpy(T)) > 1e-6
                    or abs(now.data.get_entropy(T) - was.data.get_entropy(T)) > 1e-9
                    or abs(now.data.get_heat_capacity(T)
                           - was.data.get_heat_capacity(T)) > 1e-9):
                moved.add(label)
    assert moved == {'[Lip]'}


@pytest.mark.parametrize('T', [298.15, 1000.0, 2500.0])
def test_the_cation_moved_by_one_constant_offset_at_every_temperature(
        cation, original_library, T):
    """An enthalpy-only correction is a constant shift of ``a6``. If the shift varied
    with temperature, something other than ``a6`` had been touched."""
    was = original_library.entries['[Lip]'].data
    shift = (cation.get_enthalpy(T) - was.get_enthalpy(T)) / 1000.0
    assert shift == pytest.approx(ENTERED_E0 - ORIGINAL_E0, abs=0.001)
    assert shift == pytest.approx(146.587, abs=0.001)


def test_the_other_charged_species_in_the_database_were_not_touched(thermo_db):
    """The four charged entries that are not ``[Lip]``. ``[Arp]`` is I-127's sourced
    argon cation; the rest are electrochemical reference species that are zero by
    construction, not by measurement."""
    seen = {}
    for name, lib in thermo_db.libraries.items():
        for label, e in lib.entries.items():
            if e.item is not None and e.item.get_net_charge() != 0:
                seen.setdefault(label, set()).add(name)
    assert set(seen) == {'proton', 'H3O', 'Li_ion', '[Lip]', '[Arp]', 'electron'}

    arp = thermo_db.libraries['PlasmaCationThermo'].entries['[Arp]'].data
    assert arp.get_enthalpy(T0) / 1000.0 == pytest.approx(1520.581, abs=0.01)
    for name, label in (('computationalLithiumElectrode', 'Li_ion'),
                        ('electrocatThermo', 'proton'),
                        ('electrocatLiThermo', 'proton')):
        data = thermo_db.libraries[name].entries[label].data
        assert abs(data.get_enthalpy(T0)) < 10.0


def test_the_lithium_cation_is_still_the_species_it_is_filed_as(library):
    """A correction to a number must not have moved the structure it hangs on."""
    mol = library.entries['[Lip]'].item
    assert mol.to_adjacency_list() == LIP
    assert mol.get_net_charge() == 1
    assert mol.multiplicity == 1
    assert len(mol.atoms) == 1
    assert mol.atoms[0].element.symbol == 'Li'


def test_the_species_still_resolves_to_this_library(thermo_db):
    """End of the path, not just the entry: a Li+ species handed to the database comes
    back with the corrected number."""
    data = thermo_db.get_thermo_data(_species(LIP, 'Li+'))
    assert data.get_enthalpy(T0) / 1000.0 == pytest.approx(ENTERED_H298, abs=0.01)
    assert LIBRARY in data.comment or 'Thermo library' in data.comment


# =====================================================================================
# 5. the regeneration hazard
# =====================================================================================

def test_the_library_header_warns_that_regeneration_reverts_this_correction():
    """The one failure mode this correction introduces. LithiumPrimaryThermo is
    ARC-generated; a regeneration would silently restore a 1.5 eV error and nothing at
    the point of regeneration would fail. The warning is a deliverable, so it is pinned
    like one - if someone tidies the header away, this fails.
    """
    text = open(LIBRARY_FILE).read()
    header = text[:text.index('entry(')]
    for phrase in ('NO LONGER ENTIRELY THE PRODUCT',
                   'ONE ENTRY IS HAND-REPLACED',
                   'REGENERATING THIS LIBRARY FROM ARC WILL SILENTLY REVERT',
                   'Li-006',
                   'test/test_lithium_cation_enthalpy.py',
                   'docs/i129-lithium-cation-enthalpy.md'):
        assert phrase in header, f'the header no longer says: {phrase!r}'


def test_the_entry_itself_records_its_source_and_what_was_replaced(library):
    """The entry has to carry its own provenance, because a reader who greps for
    ``[Lip]`` never sees the header."""
    long_desc = library.entries['[Lip]'].long_desc
    for phrase in ('NIST-JANAF', 'Li-006', 'ENTHALPY REPLACED',
                   'ion convention', '677.947', '685.719'):
        assert phrase in long_desc, f'the entry no longer records: {phrase!r}'
    # and it must still carry ARC's original geometry block, which was not replaced
    assert 'External symmetry: 1, optical isomers: 1' in long_desc
