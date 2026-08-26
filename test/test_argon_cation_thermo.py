#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for ``PlasmaThermo``, the argon-cation thermochemistry entry, and for
the charged-species thermochemistry coverage this ticket measured around it.

The report is ``docs/i127-argon-cation-thermo.md``. This file is the executable half of
it: every number quoted there that can be re-derived is re-derived here, so a later
change that moves one fails a test rather than silently contradicting a document.

Four groups, in descending order of how much they would cost to be wrong about:

1. **The reference-state convention.** ``Ar+`` is entered under the ion convention -
   the electron priced at zero enthalpy at all temperatures - because that is what this
   database and this runtime do. NIST-JANAF publishes the electron-convention value and
   the two differ by 6.197 kJ/mol. A value entered under the wrong one is wrong by an
   amount no other test here would catch, so the determination and the conversion are
   both pinned, by two independent arithmetic routes that close to 0.002 kJ/mol.

2. **The sourced values themselves**, against the source and against argon's ionisation
   energy from an unrelated database.

3. **The whole path** - load, resolve, a finite equilibrium constant, reactor
   acceptance, and the argon ionisation reaction carried end to end. Each separately,
   because each can fail on its own.

4. **The coverage gap's shape**, and the two defects found while measuring it: the
   shipped ``[Lip]`` entry disagreed with lithium's ionisation energy by 145 kJ/mol, and
   group additivity answers for monatomic cations with numbers that put the cation
   *below* the neutral. The group-additivity one is still pinned as it is, not fixed.
   The ``[Lip]`` one was diagnosed and corrected by I-129, so its test here now asserts
   the corrected relationship instead of the defect; the full statement of that work is
   ``test/test_lithium_cation_enthalpy.py`` and ``docs/i129-lithium-cation-enthalpy.md``.

Run with the runtime pinned::

    cd /home/alon/Code/RMG-database-i127-argon-thermo
    PYTHONPATH=/home/alon/Code/RMG-Py-i123-integration \\
        python -m pytest test/test_argon_cation_thermo.py -q

``test/conftest.py`` pins ``database.directory`` to this worktree before collection; the
fixtures below assert that pin rather than trusting it.
"""

import math
import os
import runpy
import shutil
import tempfile

import pytest

import rmgpy.data.rmg as rmg_data_module
from rmgpy import settings
from rmgpy import electron_placement
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.data.rmg import RMGDatabase
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.molecule import Molecule
from rmgpy.reaction import Reaction
from rmgpy.species import Species
from rmgpy.thermo.thermoengine import generate_thermo_data

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,
                                             'input'))
LIBRARY_DIR = os.path.join(THIS_DATABASE, 'thermo', 'libraries')
GROUP_DIR = os.path.join(THIS_DATABASE, 'thermo', 'groups')
KINETICS_LIBRARY_DIR = os.path.join(THIS_DATABASE, 'kinetics', 'libraries')

LIBRARY = 'PlasmaThermo'
IONISATION = 'PlasmaElectronImpactIonization'
DERIVATION_SCRIPT = os.path.join(os.path.dirname(THIS_DATABASE), 'docs', 'ar2p-thermo',
                                 'thermo_check.py')

R = 8.31446261815324
T0 = 298.15
#: kJ/mol per eV, CODATA.
EV = 96.48533212331

# --- the source, quoted so a test can check the file against it -------------------
#: NIST-JANAF Fourth Edition, table Ar-002 "Argon, Ion (Ar+)", T = 298.15 row.
#: Electron convention, in which the released electron carries 5/2 R T.
JANAF_ARP_H298_ELECTRON_CONVENTION = 1526.778      # kJ/mol
JANAF_ARP_S298 = 166.404                           # J/(mol*K)
JANAF_ARP_CP298 = 20.984                           # J/(mol*K)
JANAF_ARP_GF298 = 1517.077                         # kJ/mol
#: NIST-JANAF Ar-002, T = 0 row: delta-f H(0), and -(H - H(Tr)) = H(298.15) - H(0).
JANAF_ARP_H0 = 1520.573                            # kJ/mol
JANAF_ARP_DH_298_0 = 6.206                         # kJ/mol
#: NIST-JANAF Ar-001 "Argon (Ar)", the element reference state.
JANAF_AR_S298 = 154.845                            # J/(mol*K)
JANAF_AR_DH_298_0 = 6.197                          # kJ/mol
#: JANAF's electron, i.e. what the electron convention prices it at.
JANAF_ELECTRON_S298 = 20.979                       # J/(mol*K)

#: NIST Atomic Spectra Database ver. 5.12, doi:10.18434/T4W30F.
IE_AR_EV = 15.7596119
IE_LI_EV = 5.391714996

#: What is actually in the file.
ENTERED_H298 = 1520.581                            # kJ/mol, ion convention
AR2P_H298 = 1391.112                                # kJ/mol, derived ion convention
AR2P_S298 = 237.472                                 # J/(mol*K)
ENTERED_E0 = 1520.573                              # kJ/mol, convention-free at 0 K

AR = '1 Ar u0 p4 c0\n'
ARP = 'multiplicity 2\n1 Ar u1 p3 c+1\n'
LI = 'multiplicity 2\n1 Li u1 p0 c0\n'
LIP = '1 Li u0 p0 c+1\n'
ELECTRON = '1 e u0 p0 c-1\n'


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
    """Load thermo through RMG's process-global production path.

    PlasmaReactor's charged-thermo guard reads the same global database as the
    thermo engine. Save and restore it so this module stays order-independent.
    """
    previous = rmg_data_module.database
    rmg_data_module.database = None
    try:
        db = RMGDatabase()
        db.load_thermo(os.path.join(THIS_DATABASE, 'thermo'))
        yield db.thermo
    finally:
        rmg_data_module.database = previous


@pytest.fixture(scope='module')
def estimator_only(pinned):
    """The same database with every library unloaded, so any answer it gives is group
    additivity and HBI rather than a lookup."""
    db = ThermoDatabase()
    db.load_libraries(LIBRARY_DIR)
    db.unload_libraries()
    db.load_groups(GROUP_DIR)
    assert not db.libraries
    return db


@pytest.fixture(scope='module')
def entry(thermo_db):
    return thermo_db.libraries[LIBRARY].entries['[Arp]']


# =====================================================================================
# 1. The reference-state convention
# =====================================================================================

def test_every_electron_entry_in_this_database_prices_the_electron_at_zero(thermo_db):
    """The determination behind the whole entry, stated as a test.

    Three libraries carry an ``electron`` species. All three give it a NASA polynomial
    whose coefficients are identically zero, so H = S = Cp = 0 at every temperature.
    That is the ion convention (Bartmess 1994), and it is what fixes which of the two
    published Ar+ enthalpies may be entered here. If a library ever gives the electron
    real thermal functions, this fails and the Ar+ entry has to be revisited with it.
    """
    found = {}
    for name, library in thermo_db.libraries.items():
        for label, e in library.entries.items():
            if e.item is not None and e.item.is_electron():
                found[name] = e
    assert set(found) == {'electrocatThermo', 'electrocatLiThermo',
                          'computationalLithiumElectrode'}, sorted(found)
    for name, e in found.items():
        # 298-3000 K is the span those NASA polynomials declare; outside it they raise
        # rather than answer, which is itself a statement that they are placeholders.
        for T in (298.15, 500.0, 1000.0, 3000.0):
            assert e.data.get_enthalpy(T) == 0.0, (name, T)
            assert e.data.get_entropy(T) == 0.0, (name, T)
            assert e.data.get_heat_capacity(T) == 0.0, (name, T)


def test_the_runtime_adds_no_electron_term_to_a_charge_transfer_free_energy(thermo_db):
    """The second half of the determination, and the half that lives in RMG-Py.

    ``Reaction._get_free_energy_of_charge_transfer_reaction`` adds an electrochemical
    term only when ``potential != 0``, and every reactor calls it at zero. So an
    ionisation's dG is the same whether the electron is carried as metadata or as an
    explicit species - which is the ion convention expressed in code.
    """
    ar, arp = _species(AR, 'Ar'), _species(ARP, 'Ar+')
    electron = _species(ELECTRON, 'e-')
    for s in (ar, arp, electron):
        s.thermo = thermo_db.get_thermo_data(s)

    implicit = Reaction(reactants=[ar], products=[arp], electrons=+1, reversible=False)
    explicit = Reaction(reactants=[ar, electron],
                        products=[arp, electron, electron],
                        electrons=0, reversible=False)
    assert implicit.get_free_energy_of_reaction(T0) == pytest.approx(
        explicit.get_free_energy_of_reaction(T0), abs=1e-6)


def test_the_entered_enthalpy_is_the_ion_convention_value_by_two_routes(entry):
    """The one piece of arithmetic applied to any sourced number in this branch.

    Route 1 converts JANAF's 298.15 K electron-convention value by the electron's
    5/2 R T. Route 2 rebuilds it from JANAF's 0 K row, where the two conventions
    coincide. They close to 0.002 kJ/mol, which is what makes the conversion a
    transcription rather than a choice.
    """
    thermal_electron = 2.5 * R * T0 / 1000.0
    assert thermal_electron == pytest.approx(6.197, abs=0.001)

    route_1 = JANAF_ARP_H298_ELECTRON_CONVENTION - thermal_electron
    route_2 = JANAF_ARP_H0 + JANAF_ARP_DH_298_0 - JANAF_AR_DH_298_0
    assert route_1 == pytest.approx(route_2, abs=0.002)

    entered = entry.data.H298.value_si / 1000.0
    assert entered == pytest.approx(ENTERED_H298, abs=1e-6)
    assert entered == pytest.approx(route_1, abs=0.002)
    assert entered == pytest.approx(route_2, abs=0.002)

    # and it is NOT the electron-convention value, which is the mistake being avoided
    assert abs(entered - JANAF_ARP_H298_ELECTRON_CONVENTION) == pytest.approx(
        thermal_electron, abs=0.002)


def test_the_source_table_is_electron_convention_by_its_own_arithmetic():
    """Established from the table's numbers rather than from anybody's wording, because
    the two conventions' NAMES are inverted between sources and the arithmetic is not.

    The discriminator has to be the ENTHALPY. JANAF's own 298.15 K and 0 K
    enthalpies of formation differ by 6.205 kJ/mol, which is the electron's
    5/2 R T = 6.197 plus the 0.009 by which Ar+'s own enthalpy increment exceeds a bare
    monatomic gas's. Under the ion convention the same difference would be 0.009 alone.
    6.205 against 0.009 is not a close call.
    """
    difference = JANAF_ARP_H298_ELECTRON_CONVENTION - JANAF_ARP_H0
    assert difference == pytest.approx(6.205, abs=0.001)

    thermal_electron = 2.5 * R * T0 / 1000.0
    ion_own_increment = JANAF_ARP_DH_298_0 - JANAF_AR_DH_298_0
    assert ion_own_increment == pytest.approx(0.009, abs=0.001)
    # electron convention predicts the observed difference; ion convention does not
    assert difference == pytest.approx(thermal_electron + ion_own_increment, abs=0.002)
    assert abs(difference - ion_own_increment) > 6.0


def test_the_two_conventions_free_energies_coincide_near_room_temperature():
    """Why the free energy is NOT the discriminator, pinned so nobody tries to use it.

    Bartmess (J. Phys. Chem. 98 (1994) 6420, p. 6421) records Sharpe and Richardson's
    observation that at 297 K the electron's T*S numerically equals its H - H(0), so the
    two conventions give the same delta-G for an ionisation. That is a coincidence, not
    an identity, and it is also the reason the ion-convention value entered here gives
    an almost exactly right free energy of ionisation at room temperature: measured, RMG
    returns 1517.077 kJ/mol for Ar => Ar+ at 300 K against JANAF's own delta-f G(300) of
    1517.017 - 0.060 kJ/mol apart. The agreement decays away from 298 K, and that
    residue belongs to the electron's zero thermochemistry, not to this entry.
    """
    electron_convention = JANAF_ARP_H298_ELECTRON_CONVENTION - T0 * (
        JANAF_ARP_S298 + JANAF_ELECTRON_S298 - JANAF_AR_S298) / 1000.0
    ion_convention = ENTERED_H298 - T0 * (JANAF_ARP_S298 - JANAF_AR_S298) / 1000.0
    assert electron_convention == pytest.approx(JANAF_ARP_GF298, abs=0.002)
    assert ion_convention == pytest.approx(electron_convention, abs=0.1)


# =====================================================================================
# 2. The sourced values
# =====================================================================================

def test_the_entry_transcribes_the_janaf_table(entry):
    data = entry.data
    assert type(data).__name__ == 'ThermoData'
    assert data.S298.value_si == pytest.approx(JANAF_ARP_S298, abs=1e-6)
    assert data.get_heat_capacity(T0) == pytest.approx(JANAF_ARP_CP298, abs=1e-6)
    assert data.E0.value_si / 1000.0 == pytest.approx(ENTERED_E0, abs=1e-6)
    # the table stops at 6000 K and so does the entry
    assert data.Tmin.value_si == pytest.approx(T0, abs=1e-6)
    assert data.Tmax.value_si == pytest.approx(6000.0, abs=1e-6)


@pytest.mark.parametrize('T,janaf_s,janaf_dh', [
    (300.0, 166.533, 0.039),
    (500.0, 177.461, 4.325),
    (1000.0, 193.065, 15.606),
    (2000.0, 208.596, 37.960),
    (6000.0, 232.040, 122.994),
])
def test_the_entry_reproduces_the_janaf_columns_across_the_whole_range(entry, T,
                                                                      janaf_s,
                                                                      janaf_dh):
    """The 298.15 K point being right does not make the Cp grid right. This walks the
    table: entropy to 0.03 J/(mol*K) and the enthalpy increment to 0.04 kJ/mol at every
    decade from 300 K to the table's 6000 K ceiling. If the Cpdata grid is ever thinned
    or a value mistyped, this is what catches it."""
    assert entry.data.get_entropy(T) == pytest.approx(janaf_s, abs=0.03)
    increment = (entry.data.get_enthalpy(T) - entry.data.get_enthalpy(T0)) / 1000.0
    assert increment == pytest.approx(janaf_dh, abs=0.04)


def test_e0_reproduces_argons_ionisation_energy_from_an_unrelated_database(entry):
    """Corroboration, not a second measurement: JANAF's 0 K enthalpy of formation for
    Ar+ is argon's first ionisation energy, and NIST ASD measures that spectroscopically
    to eight figures. Agreement to 0.002 kJ/mol says the transcription is right."""
    assert entry.data.E0.value_si / 1000.0 == pytest.approx(IE_AR_EV * EV, abs=0.005)


def test_the_heat_capacity_is_not_five_halves_R_and_that_is_the_physics(entry):
    """Ar+ is 2P with a 2P(1/2) level 1431.6 cm^-1 above the 2P(3/2) ground level, so Cp
    carries a Schottky bump peaking near 1000 K. An entry with a flat monatomic Cp would
    be wrong by ~10% over 600-2000 K; this pins that the bump is present and where."""
    monatomic = 2.5 * R
    assert entry.data.get_heat_capacity(T0) > monatomic
    peak_T = max((300.0, 400.0, 600.0, 800.0, 1000.0, 1500.0, 2000.0, 4000.0, 6000.0),
                 key=entry.data.get_heat_capacity)
    assert peak_T == 1000.0
    assert entry.data.get_heat_capacity(1000.0) / monatomic == pytest.approx(1.096,
                                                                            abs=0.002)
    assert entry.data.get_heat_capacity(6000.0) == pytest.approx(monatomic, abs=0.2)


def test_the_entropy_is_the_neutrals_plus_the_electronic_degeneracy(entry):
    """S(Ar+) - S(Ar) is R ln 4 from the 2P(3/2) ground level's degeneracy, plus a small
    contribution from the 2P(1/2) level. Both are in the transcribed number; this is a
    check on the transcription that needs nothing but the two JANAF entropies."""
    difference = JANAF_ARP_S298 - JANAF_AR_S298
    assert difference == pytest.approx(R * math.log(4.0), abs=0.05)
    assert entry.data.S298.value_si - JANAF_AR_S298 == pytest.approx(difference,
                                                                    abs=1e-6)


def test_the_structure_is_the_gas_phase_ground_state(entry):
    molecule = entry.item
    assert len(molecule.atoms) == 1
    atom = molecule.atoms[0]
    assert atom.element.symbol == 'Ar'
    assert molecule.get_net_charge() == 1
    assert atom.radical_electrons == 1        # 3s2 3p5
    assert atom.lone_pairs == 3
    assert molecule.multiplicity == 2


def test_the_smiles_round_trip_still_corrupts_this_species(entry):
    """Recorded by ``docs/i120-argon-recombination.md`` and re-pinned here because this
    entry is the first thing in the database that would be silently mismatched by it:
    ``Ar+`` exports to ``[Ar+]``, which reads back as Ar2+. Adjacency lists are the only
    safe interchange form. If RMG-Py ever fixes this, the test fails and the warning in
    the library's longDesc can be retired."""
    smiles = entry.item.to_smiles()
    assert Molecule().from_smiles(smiles).get_net_charge() == 2


def test_argon_dimer_cation_entry_is_present(thermo_db):
    """The deliberately derived Ar2+ entry is present with its ruled values."""
    entry = thermo_db.libraries[LIBRARY].entries['[Ar2p]']
    assert entry.data.H298.value_si / 1000.0 == pytest.approx(AR2P_H298, abs=1e-9)
    assert entry.data.S298.value_si == pytest.approx(AR2P_S298, abs=1e-9)
    assert 'derived primary-read constants' in entry.short_desc
    assert 'DERIVED entry' in entry.long_desc


def test_ar2p_entry_reproduces_the_versioned_derivation(thermo_db):
    """The shipped rounded table stays tied to the versioned 53-level calculation.

    H(T)-H(0), S, and Cp are checked at all three reported temperatures. H at 298.15 K
    includes the ion-convention formation anchor; at higher temperatures the comparison
    uses H(T)-H(298.15), with a 0.010 kJ/mol allowance for integrating the table's
    three-decimal Cp values.
    """
    model = runpy.run_path(DERIVATION_SCRIPT)
    levels = model['signorell_merkt_levels']()
    entry = thermo_db.libraries[LIBRARY].entries['[Ar2p]']
    d0 = 10603.7
    cm_to_kj = 0.0119626565638786
    h0 = 1520.573 - d0 * cm_to_kj
    model_h0_increment = model['thermo'](T0, levels)[0]

    for temperature in (T0, 1000.0, 1500.0):
        h_increment, entropy, heat_capacity = model['thermo'](temperature, levels)
        # ThermoData's evaluator adds its interpolation reference offset at exactly
        # 298.15 K; compare the stored S298 there and evaluated S at the other points.
        entry_entropy = (entry.data.S298.value_si if temperature == T0
                         else entry.data.get_entropy(temperature))
        assert entry_entropy == pytest.approx(entropy, abs=0.001)
        assert entry.data.get_heat_capacity(temperature) == pytest.approx(
            heat_capacity, abs=0.001)
        if temperature == T0:
            derived_h = h0 + h_increment - 2 * 2.5 * R * temperature / 1000.0
            assert derived_h == pytest.approx(AR2P_H298, abs=0.001)
        else:
            entry_delta_h = ((entry.data.get_enthalpy(temperature)
                              - entry.data.get_enthalpy(T0)) / 1000.0)
            assert entry_delta_h == pytest.approx(
                h_increment - model_h0_increment, abs=0.010)


# =====================================================================================
# 3. The whole path
# =====================================================================================

def test_the_library_loads_alongside_every_other_thermo_library(thermo_db):
    on_disk = [f for f in os.listdir(LIBRARY_DIR) if f.endswith('.py')]
    assert len(thermo_db.libraries) == len(on_disk)
    assert LIBRARY in thermo_db.libraries
    # Ar2+ and O3- are derived from primary-read spectroscopic constants;
    # the other entries transcribe/reconcile published JANAF or NASA7 data.
    assert list(thermo_db.libraries[LIBRARY].entries) == [
        '[Arp]', '[Hep]', '[Nep]', '[Ar2p]', '[Op]', '[O2p]', '[Om]', '[O2m]', '[O3m]']


def test_the_species_resolves_to_this_library(thermo_db):
    data = thermo_db.get_thermo_data(_species(ARP, 'Ar+'))
    assert LIBRARY in data.comment
    # get_thermo_data round-trips through Wilhoit, which moves H298 by ~3 J/mol for
    # every species it returns; 0.01 kJ/mol is that artefact, not a data tolerance.
    assert data.get_enthalpy(T0) / 1000.0 == pytest.approx(ENTERED_H298, abs=0.01)


def test_without_this_library_the_species_is_refused(estimator_only):
    """What the state of the world was before this branch, measured rather than
    remembered: no estimator in this database covers a monatomic argon cation."""
    with pytest.raises(Exception):
        estimator_only.get_thermo_data(_species(ARP, 'Ar+'))


@pytest.mark.parametrize('T', [300.0, 500.0, 1000.0, 2000.0, 6000.0])
def test_an_equilibrium_constant_involving_the_cation_is_finite(thermo_db, T):
    ar, arp = _species(AR, 'Ar'), _species(ARP, 'Ar+')
    for s in (ar, arp):
        s.thermo = thermo_db.get_thermo_data(s)
    reaction = Reaction(reactants=[ar], products=[arp], electrons=+1, reversible=False)
    assert reaction.is_balanced()
    Kc = reaction.get_equilibrium_constant(T)
    assert math.isfinite(Kc) and Kc > 0.0
    dG = reaction.get_free_energy_of_reaction(T) / 1000.0
    assert 1200.0 < dG < 1600.0          # of order the ionisation energy, as it must be


def test_the_runtime_refuses_to_reverse_that_equilibrium(thermo_db):
    """The Keq above is finite and it is NOT licence to build a reverse rate from it.
    The electron is priced at zero in that sum, so Keq describes a different reaction
    than the one being reversed, and RMG-Py says so by name. Pinned so a green
    'the equilibrium constant computes' is never read as more than it is."""
    ar, arp = _species(AR, 'Ar'), _species(ARP, 'Ar+')
    for s in (ar, arp):
        s.thermo = thermo_db.get_thermo_data(s)
    reaction = Reaction(reactants=[ar], products=[arp], electrons=+1, reversible=True)
    refusal = reaction.get_reverse_from_equilibrium_refusal()
    assert refusal is not None
    assert 'omits the electron entirely' in refusal


@pytest.fixture(scope='module')
def argon_ionisation(pinned):
    """The reaction this ticket unblocks, built in a SCRATCH copy of the shipped
    ionisation library under a temporary directory.

    Adding an argon rate to this database is an explicit non-goal of the ticket, and it
    is a different owner's call besides. What is demonstrated here is that the
    thermochemistry wall - the reason that library's own header gives for carrying one
    entry - is gone. The scratch library keeps the shipped library's NAME because
    ``FAMILY_ELECTRON_PLACEMENT`` is keyed on the label; nothing is written into the
    repository.
    """
    tmp = tempfile.mkdtemp(prefix='i127-scratch-kinetics-')
    try:
        libraries = os.path.join(tmp, 'libraries')
        os.makedirs(libraries)
        shutil.copytree(os.path.join(KINETICS_LIBRARY_DIR, IONISATION),
                        os.path.join(libraries, IONISATION))
        with open(os.path.join(libraries, IONISATION, 'dictionary.txt'), 'a') as fh:
            fh.write('\n[Ar]\n' + AR + '\n[Arp]\n' + ARP)
        with open(os.path.join(libraries, IONISATION, 'reactions.py'), 'a') as fh:
            fh.write('\nentry(\n'
                     '    index = 900,\n'
                     '    label = "[Ar] => [Arp]",\n'
                     '    degeneracy = 1,\n'
                     '    reversible = False,\n'
                     '    kinetics = VoronovEIArrhenius(Z=18, N=18),\n'
                     '    shortDesc = u"scratch only",\n'
                     ')\n')
        db = KineticsDatabase()
        db.load_libraries(libraries, libraries=[IONISATION])
        reactions = db.libraries[IONISATION].get_library_reactions()
        argon = [r for r in reactions
                 if any(a.element.symbol == 'Ar'
                        for a in r.reactants[0].molecule[0].atoms)]
        assert len(argon) == 1
        yield argon[0]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_the_argon_ionisation_reaction_loads_and_balances(argon_ionisation):
    assert type(argon_ionisation.kinetics).__name__ == 'VoronovEIArrhenius'
    assert argon_ionisation.electrons == +1
    assert argon_ionisation.is_balanced()


def test_the_argon_ionisation_reaction_resolves_its_electrons(argon_ionisation):
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    assert registry.get(argon_ionisation.family) == (1, 2)
    electron = _species(ELECTRON, 'e-')
    view = electron_placement.resolve_electron_placement(
        argon_ionisation,
        list(argon_ionisation.reactants) + list(argon_ionisation.products) + [electron])
    assert sum(1 for s in view.reactants if s.is_electron()) == 1
    assert sum(1 for s in view.products if s.is_electron()) == 2
    assert len(argon_ionisation.reactants) == 1       # canonical form not mutated


def test_the_plasma_reactor_accepts_the_argon_ionisation_reaction(thermo_db,
                                                                  argon_ionisation):
    from rmgpy.solver.plasma import PlasmaReactor

    ar = argon_ionisation.reactants[0]
    arp = argon_ionisation.products[0]
    electron = _species(ELECTRON, 'e-')
    for s in (ar, arp, electron):
        s.thermo = generate_thermo_data(s)
    assert LIBRARY in arp.thermo.comment

    Te = 23209.0            # 2 eV, inside the Voronov argon fit's 1 eV - 20 keV range
    reactor = PlasmaReactor(T=(1000, 'K'), P=(1, 'bar'), Te=(Te, 'K'),
                            initial_mole_fractions={ar: 1.0, arp: 1e-12,
                                                    electron: 1e-12},
                            termination=[])
    reactor.initialize_model(core_species=[ar, arp, electron],
                             core_reactions=[argon_ionisation],
                             edge_species=[], edge_reactions=[])
    assert len(reactor.kf) == 1
    expected = argon_ionisation.kinetics.get_rate_coefficient_electron_temp(Te)
    assert reactor.kf[0] == pytest.approx(expected, rel=1e-9)
    assert reactor.kf[0] > 0.0


# =====================================================================================
# 4. Coverage, and the two defects found while measuring it
# =====================================================================================

def test_the_only_gas_phase_cations_in_this_database_are_these_set(thermo_db):
    """The coverage audit's headline, as a set rather than a count. Beyond the two
    electrochemical reference species (``proton`` and ``Li_ion``, H298 = 0 by
    construction, not gas-phase thermochemistry at all) and ``[Lip]``/``H3O``, the free
    monatomic noble-gas cations with real gas-phase thermochemistry are the three this
    library carries: Ar+, He+, and Ne+; it also carries the deliberately derived
    diatomic Ar2+ entry, and sourced O+ and O2+ entries."""
    cations = {}
    for name, library in thermo_db.libraries.items():
        for label, e in library.entries.items():
            if e.item is None or e.item.get_net_charge() <= 0:
                continue
            cations.setdefault(label, set()).add(name)
    assert set(cations) == {'proton', 'H3O', 'Li_ion', '[Lip]', '[Arp]', '[Hep]',
                            '[Nep]', '[Ar2p]', '[Op]', '[O2p]'}, sorted(cations)
    assert cations['[Arp]'] == {LIBRARY}
    assert cations['[Hep]'] == {LIBRARY}
    assert cations['[Nep]'] == {LIBRARY}
    assert cations['[Ar2p]'] == {LIBRARY}
    assert cations['[Op]'] == {LIBRARY}
    assert cations['[O2p]'] == {LIBRARY}

    # the two electrochemical ones are zero by construction, not by measurement
    for label, expected_libraries in (('proton', {'electrocatThermo',
                                                  'electrocatLiThermo'}),
                                      ('Li_ion', {'computationalLithiumElectrode'})):
        assert cations[label] == expected_libraries
        for name in expected_libraries:
            data = thermo_db.libraries[name].entries[label].data
            assert abs(data.get_enthalpy(T0)) < 10.0      # J/mol


def test_no_element_in_either_shipped_table_has_thermochemistry_above_charge_one(
        thermo_db):
    """The one clean arithmetic statement in the coverage audit. Both rate tables drive
    342 charge-stage transitions; thermochemistry exists for the +1 cation of two
    elements and for nothing at all above +1."""
    for library in thermo_db.libraries.values():
        for e in library.entries.values():
            if e.item is not None:
                assert e.item.get_net_charge() <= 1, e.label


def test_the_shipped_lithium_cation_now_agrees_with_lithiums_ionisation_energy(
        thermo_db):
    """This test was written by I-127 to pin a defect: ``[Lip]`` minus ``[Li]`` was
    375.36 kJ/mol where lithium's ionisation energy is 520.22, a 144.86 kJ/mol shortfall
    that no reference-state choice can explain. I-129 diagnosed it - the stored number is
    not a lithium cation energy at all - and replaced the enthalpy from NIST-JANAF
    Li-006. So the assertion is inverted rather than deleted: the relationship stays
    *asserted* rather than assumed, and this file keeps a claim about lithium that
    ``test_lithium_cation_enthalpy.py`` states in full.

    The tolerance is the one thing worth reading carefully. The rise is 521.95, not
    520.22, and the 1.73 kJ/mol residual is deliberate: the cation was transcribed from
    JANAF absolutely while the neutral is still ARC's, and ARC's neutral is itself
    1.73 kJ/mol below JANAF Li-005. A test that demanded exact closure would be
    demanding a number fitted to the ionisation energy, which is what I-129 was told not
    to produce. So the residual is bounded by chemical accuracy, not by zero.
    """
    library = thermo_db.libraries['LithiumPrimaryThermo']
    neutral = library.entries['[Li]'].data
    cation = library.entries['[Lip]'].data

    rise = (cation.get_enthalpy(T0) - neutral.get_enthalpy(T0)) / 1000.0
    expected = IE_LI_EV * EV
    assert expected == pytest.approx(520.221, abs=0.01)

    residual = rise - expected
    assert residual == pytest.approx(1.729, abs=0.01), (
        'the rise over the neutral is no longer the ionisation energy plus the known '
        f'residual; rise = {rise:.3f}, IE = {expected:.3f}')
    #: chemical accuracy, 1 kcal/mol - and far below the 144.86 kJ/mol the defect was
    assert abs(residual) < 4.184
    #: the residual is the shipped neutral's own error against NIST-JANAF Li-005, so it
    #: is accounted for rather than merely small
    janaf_li_h298 = 159.30
    assert neutral.get_enthalpy(T0) / 1000.0 - janaf_li_h298 == pytest.approx(
        -residual, abs=0.02)

    # the ENTROPY of the same pair was always right, and this ticket did not touch it:
    # S(Li+) is S(Li) minus R ln 2 exactly, the 2S/1S degeneracy ratio.
    s_gap = neutral.get_entropy(T0) - cation.get_entropy(T0)
    assert s_gap == pytest.approx(R * math.log(2.0), abs=0.002)


@pytest.mark.parametrize('symbol,cation,neutral,ie_ev', [
    ('N', 'multiplicity 3\n1 N u2 p1 c+1\n', 'multiplicity 4\n1 N u3 p1 c0\n', 14.53413),
    ('O', 'multiplicity 4\n1 O u3 p1 c+1\n', 'multiplicity 3\n1 O u2 p2 c0\n', 13.618055),
    ('Si', 'multiplicity 2\n1 Si u1 p1 c+1\n', 'multiplicity 3\n1 Si u2 p1 c0\n', 8.15168),
])
def test_group_additivity_answers_for_monatomic_cations_and_the_answer_is_wrong(
        estimator_only, symbol, cation, neutral, ie_ev):
    """The second defect, and the reason a library entry is the only honest way to give
    a cation thermochemistry here.

    Asked for a monatomic cation, group additivity does not refuse. It saturates the ion
    into a neutral-valence group descriptor - N+ is matched to ``group(N3s-CsCsCs)``, a
    trisubstituted amine - and returns a number. The number must exceed the neutral's by
    at least the element's ionisation energy. It does not; for N and Si it is *lower*
    than the neutral, so even the sign of ionisation is wrong.

    This is why the gap is a generation consequence rather than a list: nothing in this
    database can produce a charged species' thermochemistry except a library entry
    somebody wrote by hand.
    """
    got = estimator_only.get_thermo_data(_species(cation)).get_enthalpy(T0) / 1000.0
    base = estimator_only.get_thermo_data(_species(neutral)).get_enthalpy(T0) / 1000.0
    rise = got - base
    ionisation_energy = ie_ev * EV
    assert rise < ionisation_energy - 500.0, (
        f'{symbol}+ estimated {rise:+.1f} kJ/mol above {symbol}, '
        f'IE is {ionisation_energy:.1f} kJ/mol')


@pytest.mark.parametrize('symbol,adjacency_list', [
    ('He', 'multiplicity 2\n1 He u1 p0 c+1\n'),
    ('Ne', 'multiplicity 2\n1 Ne u1 p3 c+1\n'),
])
def test_the_other_noble_gas_cations_are_refused_by_the_estimator(estimator_only, symbol,
                                                                  adjacency_list):
    """The noble gases are the one place group additivity fails loudly instead of
    quietly, because no thermo group covers them. He+ and Ne+ now HAVE library entries
    (from the i186 ticket, verified in section 5 below), but the estimator with every
    library unloaded still refuses them - which is exactly what makes those entries
    load-bearing: nothing but the hand-written library entry can give a noble-gas cation
    thermochemistry here."""
    with pytest.raises(Exception):
        estimator_only.get_thermo_data(_species(adjacency_list))


@pytest.mark.parametrize('symbol,adjacency_list,error', [
    ('C', 'multiplicity 2\n1 C u1 p1 c+1\n', 'AtomTypeError'),
    ('F', 'multiplicity 3\n1 F u2 p2 c+1\n', 'AtomTypeError'),
    ('Al', '1 Al u0 p1 c+1\n', 'KeyError'),
])
def test_the_gate_before_thermochemistry_is_the_atom_type(symbol, adjacency_list, error):
    """Three of the elements ``voronov.yaml`` can ionise - C and Al on the ionisation
    side, F on the recombination side - still cannot have thermochemistry at all, for a
    reason that has nothing to do with data: RMG has no atom type that admits the element
    at charge +1, so the cation cannot be constructed for an entry to attach to. That gate
    lives in ``rmgpy/molecule/atomtype.py``, i.e. in RMG-Py, and is what makes this gap a
    generation consequence.

    Na, Mg, K and Ca were in this set until RMG-Py commit ``e918cafdd`` ("Give RMG alkali
    and alkaline-earth atom types") added their charged atom types; they now build, and are
    pinned as such by ``test_alkali_and_alkaline_earth_cations_now_build``. C, F and Al are
    what remain gated by the atom type."""
    with pytest.raises(Exception) as excinfo:
        Molecule().from_adjacency_list(adjacency_list)
    assert type(excinfo.value).__name__ == error


@pytest.mark.parametrize('symbol,adjacency_list,atomtype', [
    ('Na', '1 Na u0 p0 c+1\n', 'Na+'),
    ('Mg', 'multiplicity 2\n1 Mg u1 p0 c+1\n', 'Mg+'),
    ('K', '1 K u0 p0 c+1\n', 'K+'),
    ('Ca', 'multiplicity 2\n1 Ca u1 p0 c+1\n', 'Ca+'),
])
def test_alkali_and_alkaline_earth_cations_now_build(symbol, adjacency_list, atomtype):
    """The capability the atom-type gate above used to deny, now pinned so it cannot
    regress unnoticed.

    RMG-Py commit ``e918cafdd`` ("Give RMG alkali and alkaline-earth atom types", ported
    from branch 99) added Na, K, Mg and Ca with their charged forms because the carried
    ``PlasmaAlkali`` library and four plasma families otherwise fail to load with
    ``KeyError``. So each of these +1 cations now constructs to its own charged atom type
    rather than raising. This flipped four parametrizations of the gate test above from
    green to red; the truth it now asserts is that they build. Thermochemistry for them is
    a separate matter - a library entry still has to be authored - but the construction gate
    is gone, deliberately."""
    cation = Molecule().from_adjacency_list(adjacency_list)
    assert cation.get_net_charge() == 1
    assert cation.atoms[0].element.symbol == symbol
    assert cation.atoms[0].atomtype.label == atomtype


def test_argon_atom_type_resolves_to_a_specific_leaf_and_no_longer_parses_any_charge():
    """Argon perception moved twice, and this pin moved with it. Both the history and
    today's measured behaviour are on the record.

    **Round one (what this test was written for).** Argon's atom type used to declare no
    charge constraint at all. RMG-Py commit ``b52045138`` ("Narrow the placement
    declarations, and let noble gases be cations") gave He, Ne and Ar ``charge=[0, 1, 2]``
    so that ``GroupAtom.make_sample_molecule`` would stop refusing the noble-gas cations
    (Ar+, He+, He+2, Ne+) that are real species in the carried ``PlasmaAir`` library. That
    falsified the old assertion ``not ATOMTYPES['Ar'].charge``. The pin was then rewritten
    to assert ``charge == [0, 1, 2]`` *and* ``atomtype.label == 'Ar'``, on the reasoning
    that the envelope gated group-sample construction only, while ``from_adjacency_list``
    still returned the generic ``Ar`` without consulting charge features **because argon
    was in** ``nonSpecifics``. **That reasoning was correct when it was written**: with
    argon a ``nonSpecifics`` catch-all, ``get_atomtype`` genuinely did hand back ``Ar``
    for anything, which is why a nonsense Ar(4+) parsed exactly as readily as Ar+.

    **Round two (why it is red today, and what this pin now says).** Argon left
    ``nonSpecifics`` and grew specific leaves, and a later merge narrowed ``Ar0s``. Both
    halves of the old assertion are now false, and measurement (see
    ``docs/argon-perception-pins/logs/probe_stdout.log``) says:

      * ``nonSpecifics`` is now ``['He', 'Ne', 'e']`` - argon is **not** in it;
      * ``ATOMTYPES['Ar'].specific`` is ``['Ar0', 'Ar0s', 'Ar0e', 'Ar+', 'Ar++']``;
      * ``Ar+`` (``u1 p3 c+1``) perceives as the **specific leaf** ``Ar+``, not ``Ar``;
      * the nonsense Ar(4+) no longer parses **at all** - no leaf admits ``+4``, so
        ``from_adjacency_list`` raises ``AtomTypeError``.

    **Round three, which happened while I-226 was being written.** The leaf list above was
    first pinned as the four ``['Ar0', 'Ar0s', 'Ar+', 'Ar++']`` against engine
    ``fced5e836``. Within the hour, RMG-Py merged ``i222-metastable-argon-atomtype``
    (``311818121``), adding a fifth leaf ``Ar0e`` for metastable argon
    (``single=[0], lone_pairs=[3], charge=[0]``) - and **this pin caught it immediately**,
    which is the entire reason it asserts the list exactly rather than loosely. Nothing else
    in this file moved: ``Ar+``, ``Ar0``, the dimer and the Ar(4+) refusal were all
    unaffected. The list is deliberately still exact; a sixth leaf should fail here too.

    The generic ``Ar`` keeps ``charge=[0, 1, 2]``, so that half of the old pin survives
    verbatim. What died is the corollary the old docstring called uncomfortable: argon no
    longer parses any charge. That incoherence has been **resolved** in RMG-Py, in the
    direction the old docstring hoped for - the envelope and what parses now agree.

    This test PINS OBSERVED CURRENT BEHAVIOUR so it cannot regress silently; it does not
    bless that behaviour as intended. The open question it still does not settle is owned
    in RMG-Py: the ``Ar++`` leaf admits only ``lone_pairs=[3]`` (closed-shell), and so
    refuses the physical ``3P`` ground state of Ar(2+) (``u2 p2 c+2``). See the referral in
    ``docs/argon-perception-pins/report.md``."""
    from rmgpy.molecule.atomtype import ATOMTYPES
    from rmgpy.exceptions import AtomTypeError

    ground = Molecule().from_adjacency_list(ARP)

    # The generic Ar keeps the charge envelope b52045138 gave it ...
    assert ATOMTYPES['Ar'].charge == [0, 1, 2]
    # ... but argon is no longer a nonSpecifics catch-all, and has specific leaves.
    from rmgpy.molecule.atomtype import nonSpecifics
    assert 'Ar' not in nonSpecifics
    # Exact on purpose: this list gaining Ar0e is what this assertion caught mid-ticket.
    assert [t.label for t in ATOMTYPES['Ar'].specific] == [
        'Ar0', 'Ar0s', 'Ar0e', 'Ar+', 'Ar++']

    # Ar+ now resolves to its own leaf rather than the generic parent.
    assert ground.atoms[0].atomtype.label == 'Ar+'
    # and the neutral ground state resolves to its own leaf too
    assert Molecule().from_adjacency_list(AR).atoms[0].atomtype.label == 'Ar0'

    # The nonsense argon cation that used to parse "just as readily" is now refused
    # outright: no argon leaf admits +4. This is the assertion that inverted.
    with pytest.raises(AtomTypeError):
        Molecule().from_adjacency_list('multiplicity 5\n1 Ar u4 p0 c+4\n')


# =====================================================================================
# Negative control
# =====================================================================================

@pytest.mark.parametrize('label,adjacency_list,h298,s298,library', [
    ('Li', LI, 157.5723, 138.6620, 'LithiumPrimaryThermo'),
    # [Lip]'s enthalpy was 532.9358 when I-127 wrote this control; I-129 diagnosed that
    # number as not being a lithium cation energy at all and replaced it from NIST-JANAF
    # Li-006. The ENTROPY is unchanged, which is the part this control was really for:
    # I-127 added no lithium data, and I-129 touched no lithium entropy.
    ('Li+', LIP, 679.5225, 132.8988, 'LithiumPrimaryThermo'),
])
def test_the_lithium_channel_species_are_untouched(thermo_db, label, adjacency_list,
                                                   h298, s298, library):
    data = thermo_db.get_thermo_data(_species(adjacency_list, label))
    assert library in data.comment
    assert data.get_enthalpy(T0) / 1000.0 == pytest.approx(h298, abs=0.01)
    assert data.get_entropy(T0) == pytest.approx(s298, abs=0.02)


def test_neutral_argon_is_untouched(thermo_db):
    data = thermo_db.get_thermo_data(_species(AR, 'Ar'))
    assert LIBRARY not in data.comment
    assert abs(data.get_enthalpy(T0)) < 10.0          # J/mol; argon is a reference state
    assert data.get_entropy(T0) == pytest.approx(154.735, abs=0.2)


# =====================================================================================
# 5. The noble-gas cations He+ and Ne+ (i186 ticket)
# =====================================================================================
#
# Same class of free monatomic noble-gas cation as Ar+, same NIST-JANAF source family
# (He-002, Ne-002), same ion convention. Every number below is quoted from the JANAF
# table so a test can check the file against it, exactly as for Ar+ above.

HEP = 'multiplicity 2\n1 He u1 p0 c+1\n'
NEP = 'multiplicity 2\n1 Ne u1 p3 c+1\n'
HE = '1 He u0 p0 c0\n'
NE = '1 Ne u0 p3 c0\n'

#: NIST-JANAF He-002 "Helium, Ion (He+)".
JANAF_HEP_H298_EC = 2378.522    # kJ/mol, electron convention (298.15 K row)
JANAF_HEP_H0 = 2372.324         # kJ/mol, 0 K row = delta-f H(0)
JANAF_HEP_DH_298_0 = 6.197      # kJ/mol, -(H-H(Tr)) at T=0
JANAF_HEP_S298 = 131.913        # J/(mol*K)
JANAF_HEP_CP298 = 20.786        # J/(mol*K), flat 5/2 R (2S, hydrogen-like)
JANAF_HE_S298 = 126.152         # J/(mol*K), neutral He (He-001)
JANAF_HE_DH_298_0 = 6.197       # kJ/mol, neutral He
IE_HE_EV = 24.58738880          # NIST ASD

#: NIST-JANAF Ne-002 "Neon, Ion (Ne+)".
JANAF_NEP_H298_EC = 2086.966    # kJ/mol, electron convention (298.15 K row)
JANAF_NEP_H0 = 2080.662         # kJ/mol, 0 K row = delta-f H(0)
JANAF_NEP_DH_298_0 = 6.304      # kJ/mol, -(H-H(Tr)) at T=0 (>6.197 by the 2P fine structure)
JANAF_NEP_S298 = 158.307        # J/(mol*K)
JANAF_NEP_CP298 = 22.119        # J/(mol*K), 2P with a Schottky bump
JANAF_NE_S298 = 146.327         # J/(mol*K), neutral Ne (Ne-001)
JANAF_NE_DH_298_0 = 6.197       # kJ/mol, neutral Ne
IE_NE_EV = 21.564540            # NIST ASD

#: Entered ion-convention enthalpies (EC value minus the electron's 5/2 R T).
ENTERED_HEP_H298 = 2372.325
ENTERED_NEP_H298 = 2080.769


@pytest.fixture(scope='module')
def hep_entry(thermo_db):
    return thermo_db.libraries[LIBRARY].entries['[Hep]']


@pytest.fixture(scope='module')
def nep_entry(thermo_db):
    return thermo_db.libraries[LIBRARY].entries['[Nep]']


@pytest.mark.parametrize('adj,h298_ec,h0,dh,dh_neutral,entered', [
    (HEP, JANAF_HEP_H298_EC, JANAF_HEP_H0, JANAF_HEP_DH_298_0, JANAF_HE_DH_298_0,
     ENTERED_HEP_H298),
    (NEP, JANAF_NEP_H298_EC, JANAF_NEP_H0, JANAF_NEP_DH_298_0, JANAF_NE_DH_298_0,
     ENTERED_NEP_H298),
])
def test_noblegas_entered_enthalpy_is_ion_convention_by_two_routes(thermo_db, adj,
                                                                   h298_ec, h0, dh,
                                                                   dh_neutral, entered):
    """The one piece of arithmetic on any sourced number, for He+ and Ne+ as for Ar+.
    Route 1 converts JANAF's 298.15 K electron-convention value by the electron's 5/2 R T;
    route 2 rebuilds it from the 0 K row where the conventions coincide. They close to
    0.002 kJ/mol, and the entered value is neither the raw electron-convention value."""
    thermal_electron = 2.5 * R * T0 / 1000.0
    route_1 = h298_ec - thermal_electron
    route_2 = h0 + dh - dh_neutral
    assert route_1 == pytest.approx(route_2, abs=0.002)
    assert route_1 == pytest.approx(entered, abs=0.002)
    # get_thermo_data round-trips through Wilhoit (~0.003 kJ/mol); still nowhere near the
    # 6.197 kJ/mol convention gap.
    got = thermo_db.get_thermo_data(_species(adj)).get_enthalpy(T0) / 1000.0
    assert got == pytest.approx(entered, abs=0.01)
    assert abs(got - h298_ec) == pytest.approx(thermal_electron, abs=0.02)


@pytest.mark.parametrize('entry_fixture,s298,cp298,h0,tmax', [
    ('hep_entry', JANAF_HEP_S298, JANAF_HEP_CP298, JANAF_HEP_H0, 6000.0),
    ('nep_entry', JANAF_NEP_S298, JANAF_NEP_CP298, JANAF_NEP_H0, 6000.0),
])
def test_noblegas_entry_transcribes_the_janaf_table(request, entry_fixture, s298, cp298,
                                                    h0, tmax):
    entry = request.getfixturevalue(entry_fixture)
    data = entry.data
    assert type(data).__name__ == 'ThermoData'
    assert data.S298.value_si == pytest.approx(s298, abs=1e-6)
    assert data.get_heat_capacity(T0) == pytest.approx(cp298, abs=1e-6)
    assert data.E0.value_si / 1000.0 == pytest.approx(h0, abs=1e-6)
    assert data.Tmin.value_si == pytest.approx(T0, abs=1e-6)
    assert data.Tmax.value_si == pytest.approx(tmax, abs=1e-6)


@pytest.mark.parametrize('entry_fixture,ie_ev', [
    ('hep_entry', IE_HE_EV),
    ('nep_entry', IE_NE_EV),
])
def test_noblegas_e0_reproduces_ionisation_energy(request, entry_fixture, ie_ev):
    """A monatomic cation's 0 K enthalpy of formation is the neutral's ionisation energy.
    NIST ASD measures it spectroscopically; agreement to 0.002 kJ/mol is what makes the
    transcription right. This is the free, independent check the ticket named."""
    entry = request.getfixturevalue(entry_fixture)
    assert entry.data.E0.value_si / 1000.0 == pytest.approx(ie_ev * EV, abs=0.005)


def test_helium_cation_entropy_is_the_neutrals_plus_r_ln_2(hep_entry):
    """He+ is 2S(1/2) hydrogen-like: S(He+) - S(He) is R ln 2 from the ground-level
    degeneracy, with NO fine-structure term (an S term has no orbital angular momentum).
    That is the whole entropy difference, unlike the 2P Ne+/Ar+ which add R ln 4."""
    difference = JANAF_HEP_S298 - JANAF_HE_S298
    assert difference == pytest.approx(R * math.log(2.0), abs=0.01)
    assert hep_entry.data.S298.value_si - JANAF_HE_S298 == pytest.approx(difference,
                                                                        abs=1e-6)


def test_neon_cation_entropy_is_the_neutrals_plus_r_ln_4_plus_fine_structure(nep_entry):
    """Ne+ is 2P(3/2) ground: S(Ne+) - S(Ne) is R ln 4 plus a small 2P(1/2) contribution,
    the same structure as Ar+."""
    difference = JANAF_NEP_S298 - JANAF_NE_S298
    assert difference == pytest.approx(R * math.log(4.0), abs=0.5)   # dominated by R ln 4
    assert difference > R * math.log(4.0)                            # + fine structure
    assert nep_entry.data.S298.value_si - JANAF_NE_S298 == pytest.approx(difference,
                                                                        abs=1e-6)


def test_helium_cation_heat_capacity_is_flat_five_halves_R(hep_entry):
    """The physics distinction from Ar+/Ne+: He+ has an S ground term, no low-lying
    fine-structure partner, so no Schottky bump. Cp is a flat 5/2 R across the whole
    table. A bump here would be a transcription error, not physics."""
    monatomic = 2.5 * R
    for T in (298.15, 400.0, 600.0, 1000.0, 2000.0, 4000.0, 6000.0):
        assert hep_entry.data.get_heat_capacity(T) == pytest.approx(monatomic, abs=0.01)


def test_neon_cation_heat_capacity_has_a_schottky_bump_peaking_near_500(nep_entry):
    """Ne+ is 2P with a 2P(1/2) level ~780 cm^-1 above the ground level - a smaller
    splitting than Ar+'s 1431.6 cm^-1, so the Schottky bump peaks near 500 K rather than
    1000 K. An entry with a flat Cp would be wrong by ~10% over 400-1500 K."""
    monatomic = 2.5 * R
    assert nep_entry.data.get_heat_capacity(T0) > monatomic
    peak_T = max((300.0, 400.0, 500.0, 600.0, 800.0, 1000.0, 1500.0, 2000.0),
                 key=nep_entry.data.get_heat_capacity)
    assert peak_T == 500.0
    assert nep_entry.data.get_heat_capacity(6000.0) == pytest.approx(monatomic, abs=0.1)


@pytest.mark.parametrize('entry_fixture,rows', [
    # (T, JANAF S, JANAF H-H(Tr)) from He-002
    ('hep_entry', [(300.0, 132.042, 0.038), (500.0, 142.660, 4.196),
                   (1000.0, 157.068, 14.589), (2000.0, 171.476, 35.375),
                   (6000.0, 194.311, 118.519)]),
    # from Ne-002
    ('nep_entry', [(300.0, 158.444, 0.041), (500.0, 169.967, 4.558),
                   (1000.0, 185.567, 15.788), (2000.0, 200.537, 37.340),
                   (6000.0, 223.591, 121.149)]),
])
def test_noblegas_reproduces_the_janaf_columns_across_the_whole_range(request,
                                                                     entry_fixture, rows):
    """Walk the table: entropy to 0.03 J/(mol*K) and the enthalpy increment to 0.06 kJ/mol
    at every decade to the 6000 K ceiling, so a thinned or mistyped Cp grid is caught. The
    enthalpy tolerance is looser than S because the increment is a Cp integral from 298 K
    to T reconstructed from a 13-point grid through a Wilhoit fit; at the 6000 K ceiling
    that spline integration drifts ~0.045 kJ/mol from JANAF's own quadrature (0.04 % of a
    121 kJ/mol increment) - a grid artefact, not a transcription error, since every Cpdata
    value is the JANAF value verbatim."""
    entry = request.getfixturevalue(entry_fixture)
    for T, janaf_s, janaf_dh in rows:
        assert entry.data.get_entropy(T) == pytest.approx(janaf_s, abs=0.03)
        increment = (entry.data.get_enthalpy(T) - entry.data.get_enthalpy(T0)) / 1000.0
        assert increment == pytest.approx(janaf_dh, abs=0.06)


@pytest.mark.parametrize('adj', [HEP, NEP])
def test_noblegas_cation_resolves_to_this_library(thermo_db, adj):
    data = thermo_db.get_thermo_data(_species(adj))
    assert LIBRARY in data.comment


@pytest.mark.parametrize('adj', [HEP, NEP])
def test_noblegas_cation_smiles_round_trip_still_corrupts(thermo_db, adj):
    """``to_smiles()`` writes ``[He+]``/``[Ne+]`` correctly (no phantom hydrogen), but the
    monatomic-ion SMILES ROUND TRIP reads that string back as charge +2 - the same
    from_smiles defect the Ar+ entry documents. Adjacency lists are the only safe
    interchange form. (Separately, the [HeH+]/[NeH+] that appears in group-additivity error
    messages is NOT this - it is GA's own radical-saturation reference, saturate_radicals
    turning He+ into helium hydride to find an HBI base; that is a misleading diagnostic,
    not a SMILES-writer bug.)"""
    entry = thermo_db.libraries[LIBRARY].entries[
        '[Hep]' if adj is HEP else '[Nep]']
    smiles = entry.item.to_smiles()
    assert Molecule().from_smiles(smiles).get_net_charge() == 2


def test_the_helium_dication_was_not_entered(thermo_db):
    """He2+ (He(2+), monatomic, +2) has no NIST-JANAF table - He-003 returns HTTP 404 -
    so there is no tabulated Cp(T)/S(T) to transcribe, and it was deliberately not entered,
    exactly as for the argon dication. If a defensible source is ever reached, this test
    is the place that says so."""
    for library in thermo_db.libraries.values():
        for e in library.entries.values():
            if e.item is None:
                continue
            if all(a.element.symbol == 'He' for a in e.item.atoms) and \
                    e.item.get_net_charge() >= 2:
                pytest.fail(f'unexpected helium dication entry {e.label!r}')
