# Kinetics development status — phenolic-polymer TGA chemistry (phase 6)

Live status document. Branch: `polymer` (tip `543ee71a9` at last update). Maintained
continuously as development advances; every claim here must stay consistent with the
evidence of record, `CKMG ckmg/data/prereg/phase6_kinetics_evidence.md` (CKMG branch
`phase6-rmgdb-families`, commit `8121cfd8`), which was committed *before* any
implementation per the project's purity-sequencing protocol. Last updated: 2026-07-23.
Since the previous update the scope moved well past training-data-only: four new
kinetics families landed (`Ketoenol_Aromatic`, `Aryl_Decarbonylation`,
`Salicyl_Alcohol_Dehydration`, `Aryl_Ether_Condensation`; commits `c41c0ad05`,
`e573fc979`, `f13ebb251`, `b264286e9`) and were registered in the `polymers` set of
`families/recommended.py` (`2a932fc77`); the Class-D net-surrogate library was
retired and consolidated into `input/kinetics/libraries/carbon_phenol/` (`15ead55db`,
10 entries), which also absorbed the o-QM/cresol/xylenol cracking chemistry and
superseded `phenolic_pyrolysis` entries R6/R7 (`36f1168c0`); and R_Recombination
gained two manual ATG tree leafs for bridge-homolysis anchors (`543ee71a9`). The
bimolecular condensation/water-release path, previously BLOCKED, is now covered by a
dual-track design (see below). Short RMG polymer generation smoke runs confirm rows
from all six new sources appear in the generated novolac model.

## Model system of record

The model system of record is **TACOT novolac** (documented in the user report R1, Ref
`2023.1085.3.02`): a phenol–formaldehyde **novolac** — cresol subunits joined by methylene
crosslinks, with **no** hydroxymethyl (`-CH2OH`) groups. The faithful proxy SMILES is
`c1c(O)c(Cc2c(O)cc(C)cc2)c(C)cc1`. This constrains every family decision below: novolac
carbon ejection must originate in methylene-bridge (diarylmethane-link) chemistry, not in the
resole hydroxymethyl-dehydration route — which is why the o-quinone-methide dehydration
family adds generalizable value but produces no benchmark flux on this system.

## Where this work comes from

Phase 4 of the CKMG benchmarking effort established that the RMG-generated novolac
mechanism carried zero forward TGA flux — every pathway was gated on radicals that were
never produced, and the database contained no molecular initiation or small-molecule
elimination chemistry applicable to the phenolic repeat unit. The user's standing
acceptance bar for any model of record is that it be elementary-reaction-based,
RMG-generalizable, and never hard-coded, with rate coefficients that are genuinely
citable. Phase 6 therefore added literature-anchored kinetics to RMG-database itself.
Two adversarial design reviews (Codex rounds 76–77) cut the original five-work-package
plan down to what the literature could actually support at the time: training data for
existing families first, one genuinely new family designed against a then-paywalled
primary source, and an explicit refusal to invent kinetics for channels the literature
does not cover. Since then the scope has grown: four new families now exist (one of
them, `Salicyl_Alcohol_Dehydration`, is the family designed in phase 6), and the
condensation channel that was deferred on principle has been resolved by a
dual-track design rather than by inventing an Arrhenius fit.

## Implemented: training data for existing families

All entries below carry the full citation, the unit-conversion arithmetic, and the
provenance class in their `longDesc`, plus a pointer back to the evidence document.

### R_Recombination (methylene-bridge homolysis, entered in the dissociation direction)

| Entry | Reaction | k(T) | Source | Provenance | RMG rank | Effect scope |
|---|---|---|---|---|---|---|
| 5002 (superseded in place) | bibenzyl ⇌ 2 benzyl | 1.78×10¹⁵ exp(−261.07 kJ/mol /RT) s⁻¹, 648–748 K | Stein, Robaugh, Alfieri & Miller, *J. Am. Chem. Soc.* 104 (1982) 6567 (VLPP-MS) | MEASURED; Müller-Markgraf & Troe, *J. Phys. Chem.* 92 (1988) 4899 (shock tube, 900–1500 K, A=7.94×10¹⁴, Ea=250.27 kJ/mol) recorded as the uncertainty band | 5 | Exact-match, plus two ATG tree leafs fit from this anchor (see below) |
| 5003 (reconciled) | ethylbenzene ⇌ benzyl + CH₃ | unchanged (A=1.26×10¹⁷ s⁻¹, Ea=81.3 kcal/mol, 1000–1800 K) | Brouwer, Müller-Markgraf & Troe 1983 (shock tube) | MEASURED (provenance line appended; values untouched) | 5 | Exact-match only |
| 5004 (new) | diphenylmethane ⇌ benzyl + phenyl | 2.0×10¹⁵ exp(−344.2 kJ/mol /RT) s⁻¹, ~1000–1250 K; degeneracy 2 with A as the total rate | Rossi, McMillen & Golden, *J. Phys. Chem.* 88 (1984) 5031, DOI 10.1021/j150665a048 | EVALUATED — thermochemical-kinetics extrapolation (the paper measures the C–H channel); NIST holds no measured C–C entry for diphenylmethane (confirmed negative, 2026-07-17) | 6 | Exact-match, plus two ATG tree leafs fit from this anchor (see below) |

The bibenzyl supersession replaced the previous Buchanan/Dunstan/Douglas/Poutsma 1986
entry, whose measurement was of *surface-immobilized* bibenzyl; the Stein 1982 gas-phase
VLPP determination is the appropriate training anchor for gas-phase generalization, and
the reasoning is recorded inside the entry. The review round endorsed losing the
Buchanan values from the machine-readable training set (they remain cited in the
`longDesc`), because duplicate exact entries distort both depository selection and any
future tree regeneration.

**R_Recombination ATG tree regeneration — done for the bridge nodes that matter (`543ee71a9`).**
The auto-generated-tree limitation described in earlier versions of this document (exact
isomorphic matches only via depository, fitted rate rules baked into the tree and not
updated at load time) is now addressed for the anchors that matter to the novolac bridge:
two manual ATG tree leafs were added — aryl+benzylic (child of node-128) and
benzylic+benzylic (child of node-167) — with A·Tⁿ rules (E0=0; the Blowers-Masel Ea clamps
to 0 for these exothermic recombinations) fit to the GAV-thermo-reversed training anchors
5004 (Rossi 1984, EVALUATED) and 5002 (Stein 1982, MEASURED) over their honest windows.
The implied dissociation reproduces the raw anchors within 5–13% in-window; the prior
generic node estimate (A ≈ 9.99×10¹²) sat roughly 9x low. A naive single-reaction
Blowers-Masel fit would have sat 3–4 orders low because both anchors carry Ea_diss below
dH_diss (falloff), making the exact reverse Ea negative — carried here by the Tⁿ term
instead. This is not a full tree regeneration (other, non-bridge nodes are untouched); it
is a targeted leaf addition scoped to the two node families the novolac and diphenylmethane
bridges actually hit.

### H_Abstraction (benzylic sites)

| Entry | Reaction | k(T) | Source | Provenance | RMG rank | Effect scope |
|---|---|---|---|---|---|---|
| 3117 (new) | toluene + H ⇌ H₂ + benzyl | 4.553×10¹⁰ (T/298 K)³·⁹⁸ exp(−14.2 kJ/mol /RT) cm³ mol⁻¹ s⁻¹, 700–1800 K (NIST T0=298 form preserved; normalized safely by RMG's `change_t0`) | NIST squib 2006OEH/DAV9867-9873 = Oehlschlaeger, Davidson & Hanson, *J. Phys. Chem. A* 110 (2006) 9867, DOI 10.1021/jp062567t (shock tube, benzyl UV absorption); cross-checked against the paper's own two-parameter fit (exact numeric match after unit conversion); Baulch et al. 1992/1994 evaluation recorded as the consistency band | MEASURED (review fit of shock-tube data) | 1 | Generalizable: folds into rate rules at load (family is not ATG); wins node `C/H3/Cb;H_rad` |
| 3118 (new) | toluene + CH₃ ⇌ CH₄ + benzyl | 2.511×10¹⁰ exp(−29.0 kJ/mol /RT) cm³ mol⁻¹ s⁻¹, 650–770 K | NIST squib 1989ZHA/AHO1541-1549 (Zhang & Ahonkhai); corroboration: 2018MER/AWA, the 1950–1970 classic band, and Li 2016 (theory) | MEASURED | 1 | Generalizable: wins node `C/H3/Cb;C_methyl` |

A useful audit byproduct: the toluene abstraction reactions already existed in training,
but only as Li et al. 2016 *theory* entries (G4; entries 182 and 267, rank 4). That also
resolved a provenance flag in the evidence document — NIST squib 2016LI/GUO3424-3432 is
that same theory paper, so it stays corroboration-only rather than a measured source.

**Rank shadowing, found and fixed.** The new measured entries were first committed at
rank 5 and were thereby inert: both exact depository selection and rate-rule selection
in RMG prefer the *lowest* rank, so the existing rank-4 theory entries kept winning.
The fix assigned rank 1 to entries 3117/3118, which is not a convenience choice: the
RMG rank rubric (`documentation/source/users/rmg/kinetics.rst` in RMG-Py, "Rank 1 |
Experiment/FCI") places experimental determinations above rank-4/5 theory, and the
in-family precedent (Tsang & Herron 1991 review-of-experiment entries 86–88, and the
Peng/Marshall experimental entry 70, all rank 1) matches. Verification after the fix:
exact retrieval for both reactions returns the new entries, and the derived rules win
their tree nodes against both the rank-4 theory rules and the rank-10 converted
group-additivity entries. The theory entries themselves were left untouched.

## Implemented: four new kinetics families

Four new reaction families were designed and landed under `input/kinetics/families/`,
all registered in the `polymers` set of `families/recommended.py` (`2a932fc77`) so they
participate in RMG generation for phenolic-polymer decks by default.

| Family | Commit | Chemistry |
|---|---|---|
| `Ketoenol_Aromatic` | `c41c0ad05` | Phenol ⇌ 2,4-cyclohexadienone (aromatic keto-enol tautomerization); the closed-shell entry point that lets a phenolic ring present a carbonyl for downstream chemistry without breaking aromaticity assumptions elsewhere in the tree. |
| `Aryl_Decarbonylation` | `e573fc979` | Aryloxy radical → cyclopentadienyl-type radical + CO (ring-contraction decarbonylation), generalizing the o-methylphenoxy / dimethylphenoxy → CO extrusion chemistry beyond the specific COLIBRIv5 analogy entries. |
| `Salicyl_Alcohol_Dehydration` | `f13ebb251` | Salicyl-alcohol-type unit → o-quinone methide + H₂O; the closed-shell 1→2 dehydration with ring dearomatization that could not be hosted inside Retroene (Retroene requires its H-accepting atom to carry a reducible π bond; the departing water oxygen here is saturated). This is the family designed in phase 6 against the Dorrestijn et al. 1998 anchor. |
| `Aryl_Ether_Condensation` | `b264286e9` | 2 ArOH ⇌ Ar–O–Ar + H₂O, the elementary gas-phase bimolecular phenolic condensation step. This is the family that resolves the condensation channel described as BLOCKED in earlier versions of this document (see "Condensation/water-release path" below). |

Each family carries its own template/groups/rules tree and training reactions per the
standard RMG-database layout; see the family directories for full detail. Their
`Aryl_Decarbonylation` product (CO) requires `maximumSingletCarbenes=1` in the RMG
input to generate without being silently vetoed — this is an RMG-Py behavior, not a
database defect (see "Verification" below).

## The `carbon_phenol` library (replaces `novolac_net_VE_surrogate`)

**`novolac_net_VE_surrogate` is RETIRED and its file has been deleted** (`15ead55db`);
decks that still reference that library name will fail loudly, by design — there is no
compatibility shim. `input/kinetics/libraries/carbon_phenol/` is the consolidated
replacement, holding 10 entries. It is still deliberately **not** a reaction family, **not**
training data, and **not** in any recommended set — it is loaded only by decks that
explicitly declare the matching novolac polymer pool (monomer C₈H₈O, monomer MW
120.148 g/mol; stitched trimer proxy C24H26O3).

**Historical development (round-88, 2026-07-18, and the 2026-07-21 branch-split
follow-up).** The library's original two rows (VE ejection: novolac trimer proxy →
phenol + `C18H20O2_oQE_daughter`, and → o-cresol + `C17H18O2_oQM_daughter`) came from
Petrocelli & Klein 1984, *Macromolecules* 17(2):161–169, DOI
[10.1021/ma00132a008](https://doi.org/10.1021/ma00132a008) — Table II net DPM
disappearance (A = 2.5×10¹² s⁻¹ per branch, half of the total 5.0×10¹² s⁻¹, Ea = 66.0
kcal/mol, valid 823–873 K), with the phenol/o-cresol split realizing Fig 6's ~1:1
benzene:toluene branching as two distinct gas products rather than one collapsed
channel. Both rows are exact, substrate-specific surrogates (unsubstituted-DPM-analog
rate transferred to the methylated/hydroxylated novolac bridge; 2-temperature fit,
550/600 °C only) — explicitly NOT elementary (E* = 66 kcal/mol, well below the ~85
kcal/mol methylene-bridge C–C homolysis BDE) and NOT generalizable; they must never seed
a rate rule. These two rows now live in `carbon_phenol` as entries 1 and 2, carrying the
same provenance and caveats forward verbatim.

**Current contents (`carbon_phenol`, 10 entries).**
- **Entries 1–2**: the VE ejection rows above (phenol / o-cresol branches, Petrocelli &
  Klein 1984).
- **Entry 3 (ESTIMATED)**: novolac trimer proxy → `C24H24O2_cyclic_ether_daughter` + H₂O
  — the polymer-side, condensed-phase apparent kinetics for stage-I/II condensation
  water release (A = 1.0×10⁵ s⁻¹, Ea = 85 kJ/mol, valid **≤673 K**). This is a rank-10
  equivalent ESTIMATE, anchored to the Torres-Herrador et al. isoconversional apparent
  band for stage-I phenolic-resin decomposition (81.6–93.5 kJ/mol, DOI
  10.2514/1.J059423), not a first-principles rate; the intrinsic elementary barrier is
  far higher (ReaxFF water-formation barriers in crosslinked phenolics: 42–49 kcal/mol,
  DOI 10.1016/j.polymer.2010.12.034). RMG does not enforce Tmin/Tmax at simulation
  time, so decks whose reactors exceed ~700 K must either exclude this row or treat its
  flux as diagnostic only (see "Open items" below). Replacement path: an in-house
  ARC/Arkane CBS-QB3 elementary condensation rate combined with an explicit
  site-concentration model.
- **Entries 4–10**: the o-QM/cresol/xylenol secondary-cracking chemistry, consolidated
  from COLIBRIv5 plus a directly-measured anchor. Notably, oQM ⇌ benzene + CO is booked
  at Ea = 67.16 kcal/mol (A = 6.31×10¹⁴ s⁻¹), the Dorrestijn et al. measured rate
  (~850–1050 K) adopted by COLIBRIv5 — this **supersedes** the now-removed
  `phenolic_pyrolysis` entries R6 (oHO_Bz_rad ⇌ oQM + H, Ea = 24.0 kcal/mol) and R7 (oQM
  ⇌ benzene + CO, Ea = 42.0 kcal/mol), both of which sat well below (~25–33 kcal/mol
  below) the measured value and were removed as superseded (`36f1168c0`). The remaining
  entries cover o-methylphenoxy → CO extrusion, o-hydroxybenzyl β-C–H scission to
  o-quinone methide (Ea = 57.1 kcal/mol), 2,5-dimethylphenol/phenoxy CO-extrusion
  analogies, and related COLIBRIv5 rows; each carries its citation and provenance class
  (Measured / Evaluated / Analogy) in its `longDesc`. `phenolic_pyrolysis` is no longer
  a standalone source for the o-QM pathway on this branch — co-load `carbon_phenol`.

## Condensation/water-release path — no longer blocked

Earlier versions of this document described bimolecular phenolic condensation
(2 ArOH → Ar–O–Ar + H₂O) as BLOCKED on an external citable elementary rate. It is
**no longer blocked**, resolved by a dual-track design rather than by inventing an
Arrhenius fit for the polymer pool directly:

- **`Aryl_Ether_Condensation`** (new family, `b264286e9`) carries the elementary
  gas-phase chemistry: 2 ArOH ⇌ Ar–O–Ar + H₂O with its own citable training reactions
  and rate rules, usable wherever RMG generates true bimolecular condensation between
  small aromatic species.
- **`carbon_phenol` entry 3** (ESTIMATED, see above) carries the condensed-phase
  *apparent* flux on the polymer conduit itself, because the bimolecular family applied
  to two polymer-pool proxies would produce hexamer-scale products that bust the
  polymer-branch DP-preservation caps and conduit shapes (refused, verified on this
  branch) — the elementary family cannot deliver polymer-pool flux, and this net
  first-order row is the only booking that releases water from the condensed phase in
  the current method-of-moments framework. The two tracks book disjoint OH inventories
  (gas-phase small-molecule chemistry vs. the intra-chain polymer pool) and are not
  double-counted against each other.

This resolves the channel without violating the acceptance bar against invented
kinetics: the elementary family is literature-anchored gas-phase chemistry, and the
polymer-pool row is honestly labeled ESTIMATED with its band and validity window
carried in `longDesc` (see "Open items" below for the outstanding replacement plan).

## Verification

Short RMG polymer generation smoke runs on branch `polymer` demonstrate that rows from
all six new kinetics sources (the four new families, the R_Recombination ATG refit, and
the `carbon_phenol` library) appear in the generated novolac model. One of them,
`Aryl_Decarbonylation`, requires `maximumSingletCarbenes=1` in the RMG input to generate
at all — without it, RMG-Py silently vetoes family-generated CO. This is an RMG-Py
issue (a non-resonance-aware carbene whitelist), not a defect in this database branch.

Two RMG-Py polymer-branch issues were found in the course of this verification and are
documented **out of scope** for this database branch (they are RMG-Py-side bugs, not
kinetics-data problems): a compiled-solver hang tied to exhausted pool moments, and the
silent CO carbene veto above (non-resonance-aware whitelist). Full detail on both,
including reproduction steps, is in `RMG_polymer_branch_modifications_report.md` (in
the project's DR2 literature folder).

## Candidate families and open items

**True elementary radical cascade (deferred, scope L — needs an RMG-Py method-of-moments
redesign).** The physically-honest alternative to the `carbon_phenol` net surrogate rows
— bridge homolysis → a tracked condensed-scale gas radical → gas-phase β-scission →
small volatile — is a **NO-GO** on current RMG-Py without a large method-of-moments
redesign: the moment solver holds no state for a radical that has left the condensed
pool, so the cascade would open a real mass-balance hole, which the guards correctly
refuse. Deferred with that reason recorded; it is not a database-branch task.

**`carbon_phenol` entry 3 CBS-QB3 replacement.** The estimated stage-I water-release row
is a rank-10-equivalent apparent-band estimate, not a first-principles rate. Planned
replacement: an in-house ARC/Arkane CBS-QB3 elementary condensation rate combined with
an explicit site-concentration model, to replace the Torres-Herrador-band ESTIMATE with
a citable elementary rate consistent with the `Aryl_Ether_Condensation` family's own
chemistry.

**`carbon_phenol` entry 3 >673 K policy question, still open.** RMG does not enforce
Tmin/Tmax at simulation time; extrapolated beyond 673 K the entry-3 apparent fit reaches
~1 s⁻¹ at 900 K and would unphysically dominate pool mass loss, because the real
stage-I channel shuts down by reservoir exhaustion (the finite phenolic-OH pair
inventory) which the method-of-moments pool cannot express. Whether decks whose
reactors exceed ~700 K should exclude this row outright, or treat its high-temperature
flux as diagnostic-only, has not been decided; this is structural (any A/Ea pair
anchored at the stage-I DTG scale extrapolates to the same order at 900 K), not
parametric, so it will not be fixed by refitting the same band.

**Phenolic dehydration to o-quinone methide — landed as `Salicyl_Alcohol_Dehydration`.**
Previously the only genuinely new family designed (kinetics anchor Dorrestijn, Epema,
van Scheppingen & Mulder, *J. Chem. Soc., Perkin Trans. 2* (1998) 1173–1178, DOI
10.1039/a800189h); see "Implemented: four new kinetics families" above. Scope note
carried forward: this is resole chemistry — the TACOT benchmark novolac is methyl-capped
with no hydroxymethyl group, so the family adds generalizable value but no benchmark
flux on the TACOT system itself.

**Phenolic-substituted H-abstraction upgrade.** Pelucchi, Cavallotti, Cuoci, Faravelli,
Frassoldati & Ranzi, *React. Chem. Eng.* 4 (2019) 490–506, DOI 10.1039/c8re00198g, is
open access (CC BY-NC) but bot-blocked at both RSC and the Polimi repository mirror
(`hdl.handle.net/11311/1094679`); a manual pull would likely upgrade novolac-bridge
abstraction from ANALOGY-tier rule estimates to citable cresol/xylenol-specific values.
Still outstanding.

**R_Recombination full ATG tree regeneration.** The two manual leafs landed in
`543ee71a9` are scoped to the aryl+benzylic and benzylic+benzylic bridge nodes that the
novolac and diphenylmethane anchors hit; a full tree regeneration (which would let the
measured anchors influence every other node) is heavier, riskier, and still parked as a
separate follow-up needing its own branch and before/after rule diff review.

## Status ledger

| Item | State |
|---|---|
| Evidence of record committed before implementation | done (`8121cfd8`, CKMG side) |
| R_Recombination training anchors (exact-match scope) | done (`25c5e2f2`) |
| R_Recombination ATG bridge-node leafs | done (`543ee71a9`) — reproduces 5002/5004 anchors within 5–13% in-window |
| H_Abstraction measured anchors, rank-rubric verified | done (`25c5e2f2`) |
| Four new kinetics families (`Ketoenol_Aromatic`, `Aryl_Decarbonylation`, `Salicyl_Alcohol_Dehydration`, `Aryl_Ether_Condensation`) | done (`c41c0ad05`, `e573fc979`, `f13ebb251`, `b264286e9`); registered in `polymers` set (`2a932fc77`) |
| `carbon_phenol` library (consolidated, replaces `novolac_net_VE_surrogate`) | done (`15ead55db`) — 10 entries: VE ejection (2), estimated condensation (1), o-QM/cresol/xylenol cracking (7) |
| `phenolic_pyrolysis` R6/R7 | removed as superseded (`36f1168c0`) |
| Condensation/water-release path | no longer BLOCKED — dual-track design (`Aryl_Ether_Condensation` + `carbon_phenol` entry 3) |
| Generation verification (six new sources) | done — short RMG polymer smoke runs show rows from all six sources; `Aryl_Decarbonylation` needs `maximumSingletCarbenes=1` |
| RMG-Py polymer-branch issues found (out of scope) | documented — compiled-solver hang (exhausted pool moments); silent CO carbene veto; full detail in `RMG_polymer_branch_modifications_report.md` |
| `carbon_phenol` entry 3 CBS-QB3 replacement | open — planned ARC/Arkane elementary rate + site-concentration model |
| `carbon_phenol` entry 3 >673 K policy question | open — undecided whether to exclude or treat as diagnostic-only above ~700 K |
| True elementary radical cascade | deferred (scope L) — NO-GO without an RMG-Py method-of-moments redesign (mass-balance hole) |
| Phenolic-substituted H-abstraction upgrade | open — source bot-blocked at both mirrors |
| R_Recombination full ATG tree regeneration | parked — separate follow-up beyond the bridge-node leafs already landed |
