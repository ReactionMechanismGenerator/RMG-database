# I-129 — The lithium cation's enthalpy: diagnosis and correction

**Branch** `i129-lithium-cation-enthalpy` · **Base** `2d7123b08` · **2026-08-26**

Evidence labels: **[R]** code (file:line) · **[D]** database (file, entry) · **[M]** measured
(command and output shown) · **[L]** literature (full citation, specific table) · **[I]** inference
with its basis · **UNKNOWN** with what would settle it.

---

## 0. Summary

The shipped `[Lip]` entry was 144.86 kJ/mol below where lithium's ionisation energy puts it. The
cause is now established, and it is not any of the correction-scheme candidates:

> Arkane's atom-energy correction is keyed on **element counts alone**, so it is bit-identical for a
> cation and its neutral and **cancels exactly** in a cation-minus-neutral gap **[R][M]**. The
> Petersson BAC is **zero** for a bond-less species, of either charge **[M]**. Twenty neutrals in
> the same library — including LiH, LiF, LiCl and LiOH against NIST-JANAF — land within 2.5 kJ/mol,
> so the lithium atom-energy reference and the whole correction chain are sound **[M][L]**.
> Because the corrections cancel, the two stored numbers *are* a computed ionisation energy, and it
> is **3.890 eV**. No electronic-structure calculation produces that: reaching it would require the
> same run's neutral lithium to sit **25.9 kJ/mol above the Hartree–Fock limit** while that same
> neutral reproduces JANAF to 1.73 kJ/mol **[I][M]**. **The two energies did not come from one
> consistent calculation of this species pair. The stored number is not a lithium cation energy.**

It could not be recomputed, because the run's lithium atom energies were supplied to Arkane at run
time through `atomEnergies` and never committed: **0 of 67** levels of theory in
`input/quantum_corrections/data.py` carry a lithium atom energy **[M][D]**. So the entry was
replaced from **NIST-JANAF table Li-006** — E0 673.325, ΔfH°(298.15) 679.522 kJ/mol, ion
convention, by two independent conversion routes agreeing to 0.000 kJ/mol **[L][M]**.

Only `a6` (both NASA polynomials) and `E0` changed. Entropy and heat capacity are bit-identical to
ARC's at every temperature checked; 131 of the library's 132 entries are untouched **[M]**.

---

## 1. Reproduction from the shipped entry — Verifier 1, 2

```bash
cd /home/alon/Code/RMG-database-i129-lithium-cation
conda activate rmg_env
export PYTHONPATH=/home/alon/Code/RMG-Py-i123-integration:$PYTHONPATH
python probe1.py > >(tee probe1.stdout.log) 2> >(tee probe1.stderr.log >&2)
```

Probe sources: `probes/common.py`, `probes/probe1.py` (scratchpad; reproduced in
`test/test_lithium_cation_enthalpy.py`, which asserts every number below).

Every probe prints and asserts its own resolution, because a run against the wrong database or the
wrong runtime is a meaningless green — which has happened on this campaign:

```
python   : /home/alon/anaconda3/envs/rmg_env/bin/python
rmgpy    : /home/alon/Code/RMG-Py-i123-integration/rmgpy/__init__.py
PIN-BEFORE database.directory : /home/alon/Code/RMG-database/input      <- the default is WRONG
PIN-AFTER  database.directory : /home/alon/Code/RMG-database-i129-lithium-cation/input
thermo libraries loaded : 78 (files on disk: 78)
```

**The discrepancy, from the shipped entry [M]:**

```
H(298,[Li] ) =     157.5723 kJ/mol     E0([Li] ) =     151.3750 kJ/mol
H(298,[Lip]) =     532.9358 kJ/mol     E0([Lip]) =     526.7380 kJ/mol
H(298,[Lip]) - H(298,[Li]) =   375.3635 kJ/mol   (E0 route: 375.3630)
IE(Li), NIST ASD           =   520.2214 kJ/mol   (5.391714996 eV)
DISCREPANCY                =  -144.8579 kJ/mol = -1.5013 eV
ratio |discrepancy| / 5/2RT(298.15) = 23.4x
```

Matches the dispatch to the last printed digit.

**The asymmetry — enthalpy wrong, entropy right [M]:**

```
S(298,[Li] ) =   138.6620 J/(mol*K)
S(298,[Lip]) =   132.8988 J/(mol*K)
S([Li]) - S([Lip]) =   5.7632   R ln 2 =   5.7632   residual = +0.00002 J/(mol*K)
Cp(298) : [Li] 20.7862   [Lip] 20.7862   5/2 R = 20.7862
```

The entropy gap is `R ln 2` to **2 parts in 10⁵** — the electronic degeneracy of Li(²S) against
Li⁺(¹S), handled exactly right. The heat capacity is 5/2 R for both, correct for monatomics with no
low-lying electronic states. **The statistical mechanics is right and only the enthalpy is wrong**,
which is what makes this a defect rather than a different reference state.

---

## 2. What it was **not** — the ruled-out list, by measurement

The dispatch names six candidate causes. Five are eliminated by measurement, not argument.

### 2.1 An atom-energy correction applied to a cation as though it were neutral — RULED OUT

`get_atom_correction` iterates `atoms.items()`, a dict of **element symbol → count**; charge is
never read **[R]** `arkane/encorr/corr.py:128-149` (RMG-Py `i123-integration`). Measured on
nitrogen, because N ships an atom energy at this level and lithium does not **[M]**:

```
N  (neutral)  net charge +0   element count {'N': 1}   atom correction = 143617.000056 kJ/mol
N+ (cation)   net charge +1   element count {'N': 1}   atom correction = 143617.000056 kJ/mol
difference between the two = 0.0000000000e+00 J/mol
```

Bit-identical. **It cannot carry a charge-specific error, and it cancels exactly in a
cation-minus-neutral gap.** This is the step that forces the defect down into the electronic energy.

### 2.2 A bond-additivity correction — RULED OUT

The library header advertises p-type BACs. For a bond-less species **[M]**:

```
Petersson BAC for a bond-less (monatomic) species = 0.0000000000e+00 J/mol
```

Neither `[Li]` nor `[Lip]` can receive one.

### 2.3 A reference-state / electron-convention choice — RULED OUT

The entire difference between the electron and ion conventions is 5/2·R·T = 6.197 kJ/mol at
298.15 K. The defect is **23.4×** that **[M]**. One line of arithmetic kills it, which is why it was
the contract's Premise check.

### 2.4 Wrong spin multiplicity or electronic state — RULED OUT

Both would move the entropy. `S([Li]) − S([Lip]) = R ln 2` to 2e-5, and Cp is exactly 5/2 R for
both **[M]** — a doublet neutral and a singlet cation, correctly assigned. A wrong electronic state
on either species would also break the degeneracy ratio. It does not.

### 2.5 A structure that does not match the label — RULED OUT

`[Lip]`'s stored molecule is `1 Li u0 p0 c+1` — one lithium atom, net charge +1, multiplicity 1
**[D]** `input/thermo/libraries/LithiumPrimaryThermo.py`, entry 65. The SMILES round-trip corruption
recorded for monatomic ions on this campaign cannot produce this defect either: it would change the
multiplicity (which is right) or the element count (which drives the correction and cancels), and
if it had dropped or doubled the charge before the ESS job, the cation's energy would equal the
neutral's or exceed it by tens of eV. It is neither **[I]**, basis: the measured value sits
0.143 Ha above the neutral.

### 2.6 A unit or sign error at write time — RULED OUT, including one appealing coincidence

`E0` and both NASA polynomials agree with each other: `a6·R = 526.7384` against the stored
`E0 = 526.738` kJ/mol **[M]**. The entry is internally consistent, so nothing was mangled between
the polynomial and the `E0` field.

Recorded because it is exactly the kind of trap this campaign is exposed to: `144.8579 − 6.1974 =
138.6611`, and `S°(298,[Li]) = 138.6615 J/(mol·K)` — agreement to 3 parts in 10⁶, across a unit
change of 1000. **Rejected**: there is no code path that mixes an entropy into an enthalpy, the
"identity" requires reading J/(mol·K) as kJ/mol, and it does not generalise — argon's cation shows
no such relation. It is numerology, and it is written down here so nobody rediscovers it and
believes it **[I]**.

### 2.7 The value being correct for a *different* species — NOT FULLY RULED OUT

See §7. The stored energy sits 0.143 Ha above neutral lithium, which is a tight constraint: whatever
it is, it is lithium-atom-like. It is **not** a solvated Li⁺ (solvation of Li⁺ in a carbonate is
≈ −5 eV, not −1.5 eV, and the library's 20 neutrals reproduce *gas-phase* experiment **[M]**), and
it matches no Li I level (3.890 eV falls between 3d at 3.8785 eV and 4s at 4.341 eV, missing 3d by
1.2 kJ/mol where everything else here closes to 0.01) **[L]** NIST ASD ver. 5.12, Li I.

---

## 3. What it **was** — the diagnosis — Verifier 3

### 3.1 The library's machinery is sound, measured against 20 independent references

If the correction chain or the lithium atom energy were wrong, every lithium species would move.
Measured against evaluated thermochemistry **[M][L]** (ATcT v1.122 / NIST-JANAF 4th ed. / NIST
Chemistry WebBook, per row):

| label | RMG ΔfH298 | reference | error | source |
|---|---:|---:|---:|---|
| `[H]` | 218.66 | 218.00 | +0.66 | ATcT/JANAF, H atom |
| `[CH3]` | 146.59 | 146.70 | −0.11 | ATcT, methyl |
| `C[CH2]` | 121.46 | 119.00 | +2.46 | ATcT, ethyl |
| `C` | −73.15 | −74.60 | +1.45 | ATcT, methane |
| `C=C` | 53.05 | 52.40 | +0.65 | ATcT, ethene |
| `O` | −240.75 | −241.83 | +1.08 | JANAF, water |
| `N` | −46.93 | −45.90 | −1.03 | JANAF, ammonia |
| `O=C` | −110.29 | −108.70 | −1.59 | ATcT, formaldehyde |
| `O=C=O` | −393.98 | −393.51 | −0.47 | JANAF, CO₂ |
| `CO` | −200.67 | −201.00 | +0.33 | WebBook, methanol |
| `CCO` | −234.04 | −234.80 | +0.76 | WebBook, ethanol |
| `COC` | −183.48 | −184.10 | +0.62 | WebBook, DME |
| `CF` | −235.34 | −234.30 | −1.04 | WebBook, CH₃F |
| `CCl` | −81.90 | −81.90 | −0.00 | WebBook, CH₃Cl |
| `CN` | −21.05 | −22.50 | +1.45 | WebBook, methylamine |
| **`[Li][H]`** | **140.62** | **140.60** | **+0.02** | **JANAF, LiH(g)** |
| **`[Li]F`** | **−340.78** | **−340.90** | **+0.12** | **JANAF, LiF(g)** |
| **`[Li]Cl`** | **−195.71** | **−195.60** | **−0.11** | **JANAF, LiCl(g)** |
| **`[Li]O`** | **−230.22** | **−229.00** | **−1.22** | **JANAF, LiOH(g)** |
| **`[Li]`** | **157.57** | **159.30** | **−1.73** | **JANAF Li-005, Li(g)** |

Four lithium compounds within 1.3 kJ/mol. **The lithium atom-energy reference is right, the BACs
are right, the neutral lithium atom is right to 1.73 kJ/mol.** Nothing systematic is available to
blame.

*(Incidental, out of scope: `[Li]O[Li]` (Li₂O(g)) reads −139.00 against JANAF's −166.5, a
+27.5 kJ/mol outlier — plausibly the harmonic approximation failing on a quasilinear molecule.
Reported, not touched: it is a neutral, and neutral lithium thermochemistry is a stated non-goal.)*

### 3.2 Therefore the stored cation energy is not a cation energy

Because the corrections cancel exactly (§2.1), the two stored numbers *are* the computed ionisation
energy **[M]**:

```
implied E_elec(Li+) - E_elec(Li) = 375.3630 kJ/mol = 0.142968 Ha = 3.8904 eV
NIST ASD IE(Li)                  = 520.2214 kJ/mol = 0.198142 Ha = 5.391715 eV
```

The bound that closes it **[I]**, basis: the variational principle plus three reference energies
**[L]** (exact non-relativistic, infinite nuclear mass: E(Li⁺) = −7.2799134 Ha, Drake's
high-precision two-electron result; E(Li) = −7.4780603 Ha, Puchalski & Pachucki; numerical
Hartree–Fock limit E(Li) = −7.4327269 Ha):

- CCSD is FCI for a two-electron system and (T) vanishes, so **any** wavefunction calculation of
  Li⁺ satisfies E(Li⁺) ≥ −7.2799134 Ha, in any basis, at any correlation level.
- To reach the implied gap of 0.142968 Ha, the same calculation's neutral must satisfy
  E(Li) ≥ −7.422882 Ha.
- That is **25.85 kJ/mol above the Hartree–Fock limit** for the lithium atom — a description of the
  neutral worse than Hartree–Fock in a minimal basis.
- But that same neutral reproduces JANAF Li-005 to 1.73 kJ/mol (§3.1).

Contradiction. **The two energies did not come from one consistent electronic-structure calculation
of this species pair.** The defect is upstream of the stored number, in the single-point energy the
cation was given, and it is not repairable by adjusting any correction.

This also rules out the level of theory as an explanation, independently of the dispatch's assertion
that it cannot be one: a *mixed* pair is required, so no single level — however poor — reproduces it.

### 3.3 Why it could not be recomputed rather than replaced

```
levels of theory carrying atom energies      : 67
levels of theory carrying a LITHIUM energy   : 0  []
get_atom_correction(ccsd(t)-f12/cc-pvdz-f12, Li) raises AtomEnergyCorrectionError:
  An energy correction for element "Li" is unavailable for
  LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12',software='molpro').
```

**[M][D]** `input/quantum_corrections/data.py`. The run that produced this library supplied its
lithium atom energies through Arkane's `atomEnergies` input keyword **[R]**
`arc/statmech/arkane.py:389`, and they were never committed. **Nothing in this repository can
reproduce, or audit, any lithium number in either lithium library.** That is a durable finding
independent of this ticket: it is why a fresh calculation would not have identified which input was
wrong, and it is recorded in the library header for whoever regenerates it.

`atom_hf['Li'] − atom_thermal['Li'] = 153.093 kJ/mol` is the enthalpy half of the correction, and
both charges receive it identically **[M]**.

---

## 4. The charged-species sweep — Verifier 4

Answered by enumerating **every net-charged entry in all 78 thermo libraries**, not by spot check
**[M]**:

| library | label | q | atoms | H298 kJ/mol | S298 |
|---|---|---:|---:|---:|---:|
| LithiumPrimaryThermo | `[Lip]` | +1 | 1 | *(this entry)* | 132.899 |
| PlasmaCationThermo | `[Arp]` | +1 | 1 | 1520.5841 | 166.415 |
| computationalLithiumElectrode | `electron` | −1 | 1 | 0.0000 | 0.000 |
| computationalLithiumElectrode | `Li_ion` | +1 | 1 | 0.0037 | 29.132 |
| electrocatLiThermo | `electron` | −1 | 1 | 0.0000 | 0.000 |
| electrocatLiThermo | `proton` | +1 | 1 | 0.0022 | 65.347 |
| electrocatLiThermo | `H3O` | +1 | 4 | −241.8154 | 253.995 |
| electrocatThermo | `electron` | −1 | 1 | 0.0000 | 0.000 |
| electrocatThermo | `proton` | +1 | 1 | 0.0022 | 65.347 |
| electrocatThermo | `H3O` | +1 | 4 | −241.8154 | 253.995 |

10 entries, 6 distinct labels. The ionisation test applied to every monatomic cation with a neutral
counterpart **[M]**:

```
LithiumPrimaryThermo/[Lip] (Li+)  rise = 375.363   IE = 520.221   defect = -144.858 kJ/mol
PlasmaCationThermo/[Arp]   (Ar+)  rise = 1520.584  IE = 1520.571  defect =   +0.013 kJ/mol
computationalLithiumElectrode/Li_ion  (Li+)  rise = -157.569  ... (zero by construction)
electrocat{,Li}Thermo/proton          (H+)   rise = -217.996  ... (zero by construction)
```

**The signature appears on no other charged species.** `[Arp]` — the entry the dispatch specifically
asked about — is correct to **0.013 kJ/mol**, so it does **not** carry the defect and was not
touched. The remaining three are electrocatalysis reference species, zero by construction under the
computational-hydrogen-electrode convention, not gas-phase thermochemistry at all.

**Honest limit on this result:** the database contains exactly **two** gas-phase cations, so "no
systematic cation defect" rests on n = 1 comparison. What the sweep establishes positively is that
no *other* shipped charged species inherits it, so a single-entry fix is the right shape of fix.

---

## 5. The correction — Verifier 5

### 5.1 Provenance

**[L]** NIST-JANAF Thermochemical Tables, Fourth Edition, table **Li-006**, "Lithium, Ion (Li⁺)",
Li1+(g), retrieved from `https://janaf.nist.gov/tables/Li-006.txt` on 2026-08-26:

| quantity | value | row |
|---|---:|---|
| ΔfH°(0 K) | 677.947 kJ/mol | T = 0 |
| ΔfH°(298.15 K) | 685.719 kJ/mol | T = 298.15 |
| S°(298.15 K) | 133.017 J/(mol·K) | T = 298.15 |
| Cp | 20.786 J/(mol·K), constant to 6000 K | all |

Supporting: **Li-001** "Lithium (Li)", Li1(ref): H(298.15) − H(0) = 4.622 kJ/mol. **Li-005**
"Lithium (Li)", Li1(g): ΔfH°(0) = 157.725 kJ/mol.

**The source's own convention, read off its own columns rather than its front matter [M]:**
685.719 − 677.947 = 7.772, and 6.197 (cation) + 6.197 (electron, priced) − 4.622 (Li crystal) =
7.772. Exactly the **electron convention**. This database prices the electron at **zero** — the ion
convention — so a conversion is required, and entering JANAF's published number unconverted would
be wrong by 6.197 kJ/mol, small enough to look like rounding.

### 5.2 The conversion, by two independent routes

```
route 1  E0        = 677.947 - 4.622 [H(298)-H(0) of Li(cr)]        = 673.325 kJ/mol
         H(298.15) = 673.325 + 6.197 [H(298)-H(0) of Li+(g)]        = 679.522 kJ/mol
route 2  H(298.15) = 685.719 - 6.197 [the priced electron, EC->IC]  = 679.522 kJ/mol
routes agree to 0.000 kJ/mol
```

Cross-check against a database with no connection to JANAF: 677.947 − 157.725 = **520.222** kJ/mol,
against NIST ASD's IE(Li) = 520.2214 **[L]** (ASD ver. 5.12, doi:10.18434/T4W30F, Li I).

`a6 = E0/R = 673325 / 8.314472 = 80982.29` → entered as **80982.3** in both polynomials, giving
E0 = 673.3251 and H(298.15) = 679.5225 kJ/mol.

### 5.3 The correction follows from the diagnosis, not from the target

This is the distinction the dispatch draws, so it is made testable rather than asserted.

A value *fitted* to close against the ionisation energy would sit at
`E0([Li]) + IE = 151.375 + 520.221 = 671.596`. The entered value is **673.325** — 1.729 kJ/mol
away. The rise over this library's own neutral is **521.950**, not 520.221.

**That 1.729 kJ/mol residual was deliberately left standing.** It is exactly the shipped neutral's
own error against JANAF Li-005 (−1.73 kJ/mol, §3.1): the cation now comes from JANAF absolutely
while the neutral is still ARC's. Forcing the pair to close exactly would have meant back-solving
the cation from the ionisation energy — the one thing this ticket was told not to produce. The
residual is the tell that the number was sourced, and
`test_the_corrected_value_was_not_back_solved_from_the_ionisation_energy` asserts precisely that.

Correcting the neutral too would remove the residual, and was **not** done: neutral lithium is a
stated non-goal, the diagnosis does not land there, and 1.73 kJ/mol is within the calculation's own
accuracy.

### 5.4 What was deliberately not changed

The retained ARC entropy, 132.899, is 0.118 J/(mol·K) below JANAF Li-006's 133.017 — consistent
with a 1 atm rather than 1 bar standard state (R ln 1.01325 = 0.109), and the *same* 0.118 offset
appears on the neutral. That is 49× smaller than R ln 2 and three orders below the enthalpy defect.
The dispatch forbids changing the entropy, and there is no reason to want to. Stated, not hidden.

### 5.5 The regeneration hazard — a deliverable, not a comment

`LithiumPrimaryThermo` is ARC-generated. **A regeneration silently reverts this fix**: the ARC run
terminates green, the library loads, RMG uses the number, and nothing at the point of regeneration
fails. The library `shortDesc` and a block at the very top of its `longDesc` now say so in the
loudest terms available — what was replaced, why the original was unrepairable (its lithium atom
energy matches none of the 67 shipped levels, so its inputs are gone), which test to run afterwards,
and that a regenerated `[Lip]` remains unauditable until a lithium atom energy is committed to
`input/quantum_corrections/data.py`. The entry's own `longDesc` carries the full diagnosis, because
a reader who greps for `[Lip]` never sees the header.
`test_the_library_header_warns_that_regeneration_reverts_this_correction` pins both, so tidying the
warning away fails a test.

---

## 6. Downstream effect — Verifier 7

`E0([Lip])` moved by **+146.587 kJ/mol**. ΔG moves by that × the cation's net stoichiometric
coefficient, so the direction differs between the plasma and battery sides. The electron
contributes nothing: the runtime sums free energies over the explicit species and prices the
electron at zero.

**Who resolves `[Lip]`, measured [M]:** two of the 35 shipped RMG-Py example decks load
`LithiumPrimaryThermo` — `examples/rmg/SEI_pure_EC/input.py` and `examples/rmg/SEI_pure_ACN/input.py`
— and both declare a `SMILES("[Li+]")` species of their own. `electrocatLiThermo` and
`LithiumSurface` are listed *ahead* of it but carry no lithium cation, so they cannot shadow the
entry: **LithiumPrimaryThermo is the first library either deck lists that carries one.** 38 shipped
reactions name `[Lip]`: 36 in `LithiumPrimaryChargedKinetics`, 1 in
`PlasmaElectronImpactIonization`, 1 in `PlasmaRadiativeRecombination`.

**Plasma side — `[Li] => [Lip]`, the ionisation channel (net `[Lip]` = +1) [M]:**

| T / K | ΔG before | ΔG after | Keq before | Keq after | after/before |
|---:|---:|---:|---:|---:|---:|
| 300 | 377.092 | 523.679 | 2.207e−66 | 6.626e−92 | **3.00e−26** |
| 500 | 378.245 | 524.832 | 3.061e−40 | 1.487e−55 | 4.86e−16 |
| 1000 | 381.126 | 527.713 | 1.237e−20 | 2.727e−28 | 2.20e−08 |
| 2000 | 386.890 | 533.477 | 7.865e−11 | 1.168e−14 | 1.48e−04 |
| 3000 | 392.653 | 539.240 | 1.457e−07 | 4.085e−10 | 2.80e−03 |

**Battery/SEI side — `[Lip] + O <=> [Li]O + [H]` (net `[Lip]` = −1) [M]:**

| T / K | ΔG before | ΔG after | Keq before | Keq after | after/before |
|---:|---:|---:|---:|---:|---:|
| 300 | −303.083 | −449.670 | 5.894e+52 | 1.963e+78 | **3.33e+25** |
| 500 | −302.917 | −449.504 | 4.415e+31 | 9.087e+46 | 2.06e+15 |
| 1000 | −304.347 | −450.934 | 7.891e+15 | 3.580e+23 | 4.54e+07 |
| 2000 | −310.057 | −456.644 | 1.252e+08 | 8.435e+11 | 6.74e+03 |
| 3000 | −316.003 | −462.590 | 3.177e+05 | 1.133e+08 | 3.57e+02 |

`[Lip] + CO <=> [Li]OC + [H]` gives the same ratios to five figures, as it must.

**The blast radius in one sentence, for a reader who was not here:** this correction moves every
lithium-cation equilibrium in the shipped SEI example decks by up to 25 orders of magnitude at room
temperature, in the direction of making Li⁺ *harder* to form and its consumption *more* favourable —
which is correct, because the old number made the lithium cation 146.6 kJ/mol too stable. **Whether
that is acceptable to land in a community library used for battery-electrolyte mechanisms is a
judgement for whoever reviews the merge, not for this ticket**, which is why the numbers are here
rather than the conclusion.

---

## 7. What could not be reached — Verifier 10

**UNKNOWN: which specific wrong input produced the number.** The diagnosis establishes *that* the
cation's electronic energy did not come from a consistent Li⁺ calculation, and that no correction,
convention, level of theory, basis, or state assignment can account for it. It does not establish
*which* of these produced it:

- a single-point path pointing at the wrong file when Arkane read `energy = Log(<sp_path>)` **[R]**
  `arc/statmech/arkane.py:111`;
- the cation's energy taken from the project's own **DFT** level (`wb97x-d3/def2-tzvp`) while the
  neutral's came from `ccsd(t)-f12/cc-pvdz-f12`. This is the **leading unexcluded candidate**,
  because it is the only class of number that can sit below the exact two-electron energy at all: a
  density-functional total energy is not variationally bounded, and the arithmetic is consistent
  with a neutral at the frozen-core F12 value (≈ the ROHF energy, since cc-pVDZ-F12 is a *valence*
  basis and Li has one valence electron) against a cation ≈0.010 Ha below exact, which is the
  ordinary total-energy error of a hybrid functional for a two-electron cation **[I]**;
- a hand-entered or restart-file `e_elect`;
- a value carried in from a different ARC project.

**What would settle it:** the original ARC project's `[Lip]` Molpro single-point output, or its
`restart.yml` / `e_elect_summary.yml`. Neither is in this repository or anywhere on this machine;
the library arrived as a single 6671-line commit, `240625189` (Matt Johnson, 2021-11-30, message
"add LithiumPrimaryThermo Library"), with no project data **[M]**. Failing that, one
`wb97x-d3/def2-tzvp` single-point on Li⁺ would confirm or kill the leading candidate in seconds —
**no quantum-chemistry package is installed in this environment** (`psi4`, `pyscf`, `ase`, `xtb` all
absent; `/usr/bin/orca` is the GNOME screen reader, not the QC program) **[M]**, and running new
calculations to produce a replacement value is a stated non-goal.

Note that this UNKNOWN does not weaken the correction: the replacement is sourced from JANAF, not
derived from any hypothesis about the original.

**Also not reached:** whether `[Li]O[Li]`'s +27.5 kJ/mol outlier (§3.1) is a second defect or a
harmonic-approximation failure. Neutral lithium thermochemistry is a non-goal; flagged for a
follow-on.

---

## 8. Negative control — Verifier 8

Compared against the pre-edit library taken from git at `2d7123b08`, rather than against numbers
typed from memory — a control written from recollection tests the recollection **[M]**:

```
pre-edit library loaded from 2d7123b08: 132 entries
post-edit library in the worktree     : 132 entries
entries whose H, S or Cp moved at 298.15 / 1000 / 2500 K: ['[Lip]']
    [Lip] T= 298.15  dH = +146.5866 kJ/mol  dS = +0.000e+00  dCp = +0.000e+00
    [Lip] T=1000.00  dH = +146.5866 kJ/mol  dS = +0.000e+00  dCp = +0.000e+00
    [Lip] T=2500.00  dH = +146.5866 kJ/mol  dS = +0.000e+00  dCp = +0.000e+00
```

**Exactly one entry of 132 changed.** Its entropy and heat capacity are bit-identical to ARC's at
every temperature checked, and its enthalpy moved by one constant offset at all of them — which is
what an `a6`-only edit must look like, and what a deformed polynomial would not.

Every other charged species in the database, unmoved **[M]**:

```
PlasmaCationThermo            [Arp]     H298 =    1520.5841   (I-127's sourced argon, untouched)
computationalLithiumElectrode Li_ion    H298 =       0.0037
electrocat{,Li}Thermo         proton    H298 =       0.0022
electrocat{,Li}Thermo         H3O       H298 =    -241.8154
all four electron entries               H298 =       0.0000
```

**Full suite:** `200 passed, 4 failed`. The four failures are **pre-existing and unrelated** —
`test_plasma_electron_attachment.py` asserts `source == 'rate rules'` where the pinned runtime's
`family.get_kinetics` returns a `KineticsDepository` object. Confirmed by reverting
`LithiumPrimaryThermo.py` to `2d7123b08` and re-running that file alone: **`4 failed, 41 passed`**,
identical set. They involve no thermo libraries at all (`kinetics_db.libraries == {}`). Not this
ticket's; flagged.

---

## 9. The pinning test — Verifier 6

I-127's `test_the_shipped_lithium_cation_disagrees_with_lithiums_ionisation_energy` passed *because*
the defect was present and failed by design on correction. It was **rewritten, not deleted**, to
`test_the_shipped_lithium_cation_now_agrees_with_lithiums_ionisation_energy`: the relationship stays
*asserted* rather than assumed, now against the ionisation energy plus the accounted-for
1.729 kJ/mol residual, with the residual independently tied to the neutral's own JANAF error so it
is explained rather than merely tolerated. Its sibling negative control
`test_the_lithium_channel_species_are_untouched` was updated for the enthalpy and keeps asserting
the **unchanged entropy**, which is what that control was really for. The argon module's docstring
was updated so it no longer claims the defect is unfixed.

`test/test_lithium_cation_enthalpy.py` (new, 27 tests) states the ticket in full: the source and its
convention by two routes, the corrected relationship and its residual, the not-back-solved
discriminator, **the diagnosis as executable claims** (charge-blindness, zero BAC, no lithium atom
energy, the variational contradiction), the negative control, and the regeneration warning.

```bash
$ python -m pytest test/test_lithium_cation_enthalpy.py -q
27 passed in 21.37s
```

**Shown to bite.** A suite that passes on first run proves nothing until it fails against what it
pins. With `LithiumPrimaryThermo.py` reverted to `2d7123b08`:

```
13 failed, 62 passed
FAILED test_lithium_cation_enthalpy.py::test_the_entered_enthalpy_is_the_ion_convention_value_by_two_routes
FAILED test_lithium_cation_enthalpy.py::test_the_cation_now_rises_over_the_neutral_by_the_ionisation_energy
FAILED test_lithium_cation_enthalpy.py::test_the_corrected_value_was_not_back_solved_from_the_ionisation_energy
FAILED test_lithium_cation_enthalpy.py::test_exactly_one_entry_of_the_library_moved
FAILED test_lithium_cation_enthalpy.py::test_the_library_header_warns_that_regeneration_reverts_this_correction
FAILED test_argon_cation_thermo.py::test_the_shipped_lithium_cation_now_agrees_with_lithiums_ionisation_energy
   ... 13 in total
```

---

## 10. The diff — Verifier 9

```
 input/thermo/libraries/LithiumPrimaryThermo.py | 93 +++++++++++++++++++++++--
 test/test_argon_cation_thermo.py               | 60 ++++++++++------
 test/test_lithium_cation_enthalpy.py           | (new, 27 tests)
 docs/i129-lithium-cation-enthalpy.md           | (new, this file)
 docs/contracts/i129-lithium-cation-enthalpy.md | (new)
```

The whole numerical change, in four lines:

```diff
-  NASAPolynomial(coeffs=[2.5,...,-1.11018e-23,63352,1.74004],  Tmin=(10,'K'),      Tmax=(794.005,'K')),
-  NASAPolynomial(coeffs=[2.5,...,-9.62112e-25,63352,1.74004],  Tmin=(794.005,'K'), Tmax=(3000,'K')),
-  E0 = (526.738,'kJ/mol'),
+  NASAPolynomial(coeffs=[2.5,...,-1.11018e-23,80982.3,1.74004], Tmin=(10,'K'),      Tmax=(794.005,'K')),
+  NASAPolynomial(coeffs=[2.5,...,-9.62112e-25,80982.3,1.74004], Tmin=(794.005,'K'), Tmax=(3000,'K')),
+  E0 = (673.325,'kJ/mol'),
```

Everything else in the 93 changed lines of the library is the two warning blocks and the entry's
provenance. `a1`–`a5`, `a7`, `Cp0`, `CpInf`, the temperature ranges, the molecule and the geometry
are untouched.

Writes are confined to this worktree; `/home/alon/Code/RMG-Py-i123-integration`,
`/home/alon/Code/ARC`, `/home/alon/Code/RMG-database` and `/home/alon/Code/RMG-database-plasma` were
read only. No merge, no push, no PR.
