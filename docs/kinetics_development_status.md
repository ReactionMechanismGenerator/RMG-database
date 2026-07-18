# Kinetics development status — phenolic-polymer TGA chemistry (phase 6)

Live status document. Branch: `phase6-phenolic-training` (worktree `RMG-database-phase6`,
base `polymer` @ `7cb91d10`). Maintained continuously as development advances; every claim
here must stay consistent with the evidence of record,
`CKMG ckmg/data/prereg/phase6_kinetics_evidence.md` (CKMG branch `phase6-rmgdb-families`,
commit `8121cfd8`), which was committed *before* any implementation per the project's
purity-sequencing protocol. Last updated: 2026-07-18 (carbon-ejection dev cycle:
round-86 mass-soundness verification of the volatile-ejection host and the generic-bridge-rate
finding added; the phase-6 training anchors landed earlier at amended commit `25c5e2f2`, and
the `phase6-phenolic-training` branch has since merged to `polymer`).

## Model system of record

The model system of record is **TACOT novolac** (documented in the user report R1, Ref
`2023.1085.3.02`): a phenol–formaldehyde **novolac** — cresol subunits joined by methylene
crosslinks, with **no** hydroxymethyl (`-CH2OH`) groups. The faithful proxy SMILES is
`c1c(O)c(Cc2c(O)cc(C)cc2)c(C)cc1`. This constrains every family decision below: novolac
carbon ejection must originate in methylene-bridge (diarylmethane-link) chemistry, not in the
resole hydroxymethyl-dehydration route — which is why the o-quinone-methide family below adds
generalizable value but produces no benchmark flux on this system.

## Where this work comes from

Phase 4 of the CKMG benchmarking effort established that the RMG-generated novolac
mechanism carries zero forward TGA flux — every pathway is gated on radicals that are
never produced, and the database contains no molecular initiation or small-molecule
elimination chemistry applicable to the phenolic repeat unit. The user's standing
acceptance bar for any model of record is that it be elementary-reaction-based,
RMG-generalizable, and never hard-coded, with rate coefficients that are genuinely
citable. Phase 6 therefore adds literature-anchored kinetics to RMG-database itself.
Two adversarial design reviews (Codex rounds 76–77) cut the original five-work-package
plan down to what the literature can actually support: training data for existing
families now, one genuinely new family parked on a paywalled primary source, and an
explicit refusal to invent kinetics for channels the literature does not cover.

## Implemented: training data for existing families

No new family has been created so far — everything landed to date is training data
(with provenance-classed citations) for families that already exist. All entries carry
the full citation, the unit-conversion arithmetic, and the provenance class in their
`longDesc`, plus a pointer back to the evidence document.

### R_Recombination (methylene-bridge homolysis, entered in the dissociation direction)

| Entry | Reaction | k(T) | Source | Provenance | RMG rank | Effect scope |
|---|---|---|---|---|---|---|
| 5002 (superseded in place) | bibenzyl ⇌ 2 benzyl | 1.78×10¹⁵ exp(−261.07 kJ/mol /RT) s⁻¹, 648–748 K | Stein, Robaugh, Alfieri & Miller, *J. Am. Chem. Soc.* 104 (1982) 6567 (VLPP-MS) | MEASURED; Müller-Markgraf & Troe, *J. Phys. Chem.* 92 (1988) 4899 (shock tube, 900–1500 K, A=7.94×10¹⁴, Ea=250.27 kJ/mol) recorded as the uncertainty band | 5 | Exact-match only (family is ATG, see caveats) |
| 5003 (reconciled) | ethylbenzene ⇌ benzyl + CH₃ | unchanged (A=1.26×10¹⁷ s⁻¹, Ea=81.3 kcal/mol, 1000–1800 K) | Brouwer, Müller-Markgraf & Troe 1983 (shock tube) | MEASURED (provenance line appended; values untouched) | 5 | Exact-match only |
| 5004 (new) | diphenylmethane ⇌ benzyl + phenyl | 2.0×10¹⁵ exp(−344.2 kJ/mol /RT) s⁻¹, ~1000–1250 K; degeneracy 2 with A as the total rate | Rossi, McMillen & Golden, *J. Phys. Chem.* 88 (1984) 5031, DOI 10.1021/j150665a048 | EVALUATED — thermochemical-kinetics extrapolation (the paper measures the C–H channel); NIST holds no measured C–C entry for diphenylmethane (confirmed negative, 2026-07-17) | 6 | Exact-match only |

The bibenzyl supersession replaced the previous Buchanan/Dunstan/Douglas/Poutsma 1986
entry, whose measurement was of *surface-immobilized* bibenzyl; the Stein 1982 gas-phase
VLPP determination is the appropriate training anchor for gas-phase generalization, and
the reasoning is recorded inside the entry. The review round endorsed losing the
Buchanan values from the machine-readable training set (they remain cited in the
`longDesc`), because duplicate exact entries distort both depository selection and any
future tree regeneration.

### H_Abstraction (benzylic sites)

| Entry | Reaction | k(T) | Source | Provenance | RMG rank | Effect scope |
|---|---|---|---|---|---|---|
| 3117 (new) | toluene + H ⇌ H₂ + benzyl | 4.553×10¹⁰ (T/298 K)³·⁹⁸ exp(−14.2 kJ/mol /RT) cm³ mol⁻¹ s⁻¹, 700–1800 K (NIST T0=298 form preserved; normalized safely by RMG's `change_t0`) | NIST squib 2006OEH/DAV9867-9873 = Oehlschlaeger, Davidson & Hanson, *J. Phys. Chem. A* 110 (2006) 9867, DOI 10.1021/jp062567t (shock tube, benzyl UV absorption); cross-checked against the paper's own two-parameter fit (exact numeric match after unit conversion); Baulch et al. 1992/1994 evaluation recorded as the consistency band | MEASURED (review fit of shock-tube data) | 1 | Generalizable: folds into rate rules at load (family is not ATG); wins node `C/H3/Cb;H_rad` |
| 3118 (new) | toluene + CH₃ ⇌ CH₄ + benzyl | 2.511×10¹⁰ exp(−29.0 kJ/mol /RT) cm³ mol⁻¹ s⁻¹, 650–770 K | NIST squib 1989ZHA/AHO1541-1549 (Zhang & Ahonkhai); corroboration: 2018MER/AWA, the 1950–1970 classic band, and Li 2016 (theory) | MEASURED | 1 | Generalizable: wins node `C/H3/Cb;C_methyl` |

A useful audit byproduct: the toluene abstraction reactions already existed in training,
but only as Li et al. 2016 *theory* entries (G4; entries 182 and 267, rank 4). That also
resolved a provenance flag in the evidence document — NIST squib 2016LI/GUO3424-3432 is
that same theory paper, so it stays corroboration-only rather than a measured source.

## Implementation caveats (verified against the branch code, not assumed)

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

**Auto-generated-tree limitation (R_Recombination).** On this branch R_Recombination is
an auto-generated (ATG) family: training additions are consulted only for *exact
isomorphic matches* via the depository, while the fitted rate rules — which serve every
non-exact analog — are baked into the tree and are not updated at load time. The
benchmark novolac bridge is a hydroxylated diphenylmethane, a non-exact analog, so the
new homolysis anchors deliberately make **no claim of changing generated-mechanism
bridge rates**. Folding them into the fitted rules requires regenerating the ATG tree,
which is parked as a separate follow-up (it is heavier, riskier, and needs its own
verification round). This scope-of-effect statement is embedded in each R_Recombination
entry and in the commit message. H_Abstraction, by contrast, is not ATG: its training
entries become rate rules at load, so the measured anchors genuinely generalize to
benzylic analogs — at honestly-labeled ANALOGY tier for substituted bridges.

*Confirmed empirically (round-86, 2026-07-18).* On the novolac proxy the generated bridge
rows carry a **generic** R_Recombination pre-exponential A ≈ 9.99×10¹² — i.e. the cited
5002/5004 homolysis rates are not reaching the smoke-run bridge rows. They affect
exact-match depository retrieval only, which the non-exact hydroxylated-diphenylmethane
bridge never triggers; regenerating the ATG tree remains the only route to fold them into
the rates the generated mechanism actually uses.

**Polymer routing verdict: ROUTING-VETOED (smoke test, 2026-07-17).** The generation
smoke test (novolac single-methylene-bridge polymer + this database worktree, RMG
polymer branch @ bd3ef5ff5, run of record `~/runs/CKMG/phase6_smoke_2026.07.17/`)
settled the efficacy question empirically. The chemistry generates: H_Abstraction fires
on ring, benzylic and phenolic sites — with the new rank-1 anchor (entry 3117) confirmed
verbatim as the kinetics source in the annotated mechanism — and R_Recombination
produces the bridge C–C scission rows. But every one of the 352 reactions coupling a
chain-scale fragment to the polymer pool is refused conduit-deferred
(`would_admit=0`; refusal census classes r93-general and feature-radical,
`rmgpy/polymer.py:3506` and ~3700–3760), with zero moment-credit conduit admissions.
The only non-carbon gas observed is H₂ from live H-abstraction/volatile-ejection rows
(four non-refused `volatile_ejection/1` rows, seed-H-driven); conduit-mediated carbon
volatile flux is exactly zero. Conclusion: the conduit admission machinery is not a
disabled switch but incomplete by design — `CONDUIT_ADMISSION_ENABLED=False` is not a
deck option, the admission classifier only accepts a narrow forward one-gas-product
shape, feature-radical sightings block admission via a sticky ledger, and the live
admit arm has no solver dispatch yet (`rmgpy/polymer_conduit.py:730,816,830,1016`;
`rmgpy/solver/polymer.pyx:2570`). No elementary decomposition chemistry — however
well-anchored in the database — can produce carbon TGA flux on this branch until that
machinery is completed (a design decision for the polymer-branch owner), and separately
the ATG tree regeneration is needed for the bridge rate itself. Both are outside this
database branch's scope. Entries 3118/5002/5004 were not cited in the generated mechanism, and
5002/5004 could not be (exact-match-only on a non-exact bridge) — consistent with the
committed scope-of-effect statements.

## Candidate families to implement next — anchors and blockers

**Novolac carbon-volatile ejection (net closed-shell step; the load-bearing benchmark gap).**
This is the missing forward-flux step and the top pending candidate. The target is a *net*
closed-shell volatile-ejection
`novolac_chain → shorter_chain + {cresol C₇H₈O / phenol C₆H₆O / benzene / toluene / CO / CH₄}`,
hosted by RMG-Py's existing concerted-loss / `VOLATILE_EJECTION` machinery. The host is
mass-sound (verified round-86, 2026-07-18): the condensed mass drops by exactly MW(gas) per
event, with no double-count. **Status: BLOCKED — no fully-cited *net* novolac carbon-volatile
rate or yield is in hand.** The in-hand novolac-applicable sources (R_Recombination 5002/5004)
are homolysis-to-radicals, **not** a net closed-shell volatile with a cited product yield —
relabeling them as a net step would be fabrication and is out. The fully-cited net steps that
do exist — da Silva o-QM → benzene + CO (10.1021/jp073335c) and Pelucchi phenol → C₅H₆ + CO
(10.1039/c8re00198g) — are resole-only / monomer-scale and have **no novolac inlet**; neither
by itself produces a novolac net volatile step. **Unblock condition:** a cited
product-*specific* net rate (an Arrhenius A/Ea, or a conversion–time curve reducible to k(T))
plus the product branching for diphenylmethane / phenolic-diarylmethane pyrolysis to
closed-shell aromatics. **Best target:** Petrocelli & Klein, "Model reaction pathways in Kraft
lignin pyrolysis" (1984), which reports DPM → benzene / toluene / fluorene Arrhenius
parameters. **Secondary:** Buchanan & Britt / Poutsma / Savage diarylmethane-pyrolysis product
distributions — caveat: the surface-immobilized DPM work shows char / fluorene / PAH routes
dominating, which may argue for a *small or blocked* carbon step rather than unblocking a large
one.

*Provenance rule for when it lands.* The net step is a **calibrated net surrogate, explicitly
not elementary**. Its required provenance label is verbatim: "net first-order surrogate for
novolac diarylmethane-link volatile release, constructed from a model-compound bridge-cleavage
rate and an experimentally observed product branching fraction under specified pyrolysis
conditions; not elementary; valid only as a sensitivity/benchmark closure over that condition
envelope." A condition-transferability caveat is mandatory whenever the source conditions
(high-T/P, surface-immobilized, H-donor, catalyst, long-residence) differ from the TGA envelope.

**True elementary radical cascade (deferred, scope L — needs an RMG-Py method-of-moments
redesign).** The physically-honest alternative to the net surrogate — bridge homolysis → a
tracked condensed-scale gas radical → gas-phase β-scission → small volatile — is a **NO-GO** on
current RMG-Py without a large method-of-moments redesign: the moment solver holds no state for
a radical that has left the condensed pool, so the cascade would open a real mass-balance hole,
which the guards correctly refuse. Deferred with that reason recorded; it is not a
database-branch task.

**Phenolic dehydration to o-quinone methide (new family; the strongest *closed-shell* family candidate).**
Salicyl-alcohol-type units eliminate water to form o-quinone methide — the only genuinely
new family designed so far. Feasibility is settled: the recipe shape (closed-shell 1→2
with ring dearomatization) is proven machinery, and hosting it inside the existing
Retroene family is impossible (template proof: Retroene requires its H-accepting atom to
carry a reducible π bond, and the departing water oxygen is saturated). The kinetics
anchor is Dorrestijn, Epema, van Scheppingen & Mulder, *J. Chem. Soc., Perkin Trans. 2*
(1998) 1173–1178, DOI 10.1039/a800189h. **Blocker: the paper is fully closed-access —
no OA copy exists (verified via OpenAlex/Unpaywall), and citing-review routes were
cookie-walled; institutional retrieval of this PDF is the unlock.** Honest scope note:
this is resole chemistry — the TACOT benchmark novolac is methyl-capped with no
hydroxymethyl group, so the family adds generalizable value but no benchmark flux.

**o-Quinone-methide decomposition (CO channel).** Anchor: da Silva & Bozzelli,
*J. Phys. Chem. A* 111 (2007) 7987, DOI 10.1021/jp073335c. The overall rate expression
k = 2.64×10¹⁴ exp(−35 900 K/T) s⁻¹ (dominant channel via 2-hydroxyphenylcarbene →
tropone → benzene + CO) is confirmed from the PubMed abstract, but the channel-specific
Arrhenius triplets need the paywalled full text. Currently orphaned for the benchmark:
without the dehydration family there is no o-QM inlet.

**Bimolecular phenolic condensation (2 ArOH → Ar–O–Ar + H₂O).** The real stage-I water
channel for novolac and the largest benchmark gap. **No citable elementary rate
coefficient exists in any source we could reach** — this is the state of the literature,
not a retrieval failure. Deferred on principle: authoring it would require inventing
kinetics, which the acceptance bar forbids. Any future unlock would come from new
primary literature (e.g. a QM study of phenol condensation kinetics).

**R_Recombination ATG tree regeneration.** Not a new family but the step that would let
the new measured homolysis anchors influence substituted-bridge estimates. Needs its own
branch, reproducibility check of the tree-generation machinery on the polymer branch,
and a before/after rule diff review.

**Phenolic-substituted H-abstraction upgrade.** Pelucchi, Cavallotti, Cuoci, Faravelli,
Frassoldati & Ranzi, *React. Chem. Eng.* 4 (2019) 490–506, DOI 10.1039/c8re00198g, is
open access (CC BY-NC) but bot-blocked at both RSC and the Polimi repository mirror
(`hdl.handle.net/11311/1094679`); a manual pull would likely upgrade novolac-bridge
abstraction from ANALOGY-tier rule estimates to citable cresol/xylenol-specific values.

## Status ledger

| Item | State |
|---|---|
| Evidence of record committed before implementation | done (`8121cfd8`, CKMG side) |
| R_Recombination training anchors (exact-match scope) | done (`25c5e2f2`) |
| H_Abstraction measured anchors, rank-rubric verified | done (`25c5e2f2`) |
| Generation smoke test (polymer routing verdict) | done — ROUTING-VETOED (conduit admission disabled; see caveats) |
| WP5 constraints headroom (three blocks) | mooted — no admissible flux to protect until conduit admission lands (RMG-Py side) |
| Flux census + benchmark rerun (role='certification') | mooted by routing veto — would reproduce the known zero-flux result |
| `VOLATILE_EJECTION` host mass-soundness | verified round-86 (2026-07-18) — condensed mass drops by exactly MW(gas)/event, no double-count |
| Generated-bridge-rate delivery (5002/5004 → generated rows) | confirmed inert (round-86) — generated rows carry generic A ≈ 9.99×10¹²; needs ATG regen |
| Novolac carbon-volatile ejection (calibrated net surrogate) | BLOCKED — no cited *net* novolac rate/yield in hand; unblock = Petrocelli & Klein 1984 (DPM Arrhenius) PDF |
| True elementary radical cascade | deferred (scope L) — NO-GO without an RMG-Py method-of-moments redesign (mass-balance hole) |
| Dehydration/o-QM family | parked — paywalled primary (10.1039/a800189h) |
| o-QM decomposition training | parked — paywalled full text (10.1021/jp073335c) |
| Phenolic condensation | deferred — no citable elementary kinetics exist |
| ATG tree regeneration | parked — separate follow-up |
