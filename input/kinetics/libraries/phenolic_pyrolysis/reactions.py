#!/usr/bin/env python
# encoding: utf-8

name = "phenolic_pyrolysis"
shortDesc = u"Seed mechanism for novolak phenol-formaldehyde pyrolysis under N2 (300-1275 K)."
longDesc = u"""
Seed kinetic library for bootstrapping RMG-Py runs on novolak phenol-formaldehyde
resin pyrolysis under inert (N2) atmosphere, 300-1275 K (≈ 25-1000 °C).

The library targets the chemistry gaps identified in a 2026-05-14 RMG run that
generated only 48 species / 377 reactions and showed essentially no volatile-
release pathway — see ~/Code/TA/PRD.md §7.4. The reactions below capture the
*backbone* of phenolic-resin pyrolysis: bridge initiation, benzylic H-abstraction,
β-scission via ortho-quinone-methide, ipso phenol release, phenoxyl decarbonylation,
and the termination/recombination channels that compete with volatile escape.

The 11 reactions are curated from three independent Deep-Research literature
surveys consolidated in `~/runs/RMG/poly_101/consolidated_novolak_pyrolysis_report.md`.
Each rate is tagged with its provenance:

  Direct  = measured for the stated molecule or a tight model compound
  QM      = high-level QM/TST/RRKM calculation
  Analogy = transferred from a related molecule (toluene, bibenzyl, ...)
  Lumped  = back-fit from TGA/global kinetics (not represented in this seed)

Where multiple sources disagree on a value, the consolidated report's recommended
choice was used. Uncertainty factors are stated in the longDesc per reaction and
are typically x3-x10. This is a *seed* — RMG is expected to extend it via
rate-rule estimation, and the polymer-pool moments handle the chain-length
distribution separately.

Source: ~/runs/RMG/poly_101/consolidated_novolak_pyrolysis_report.md (2026-05-14)
"""

# ------------------------------------------------------------------------------
# Stage I — initiation (bridge homolysis)
# ------------------------------------------------------------------------------

entry(
    index = 1,
    label = "bibenzyl <=> benzyl_rad + benzyl_rad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e15, 's^-1'),
        n = 0.0,
        Ea = (62.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R1: bibenzyl central C-C homolysis (analog for novolak bridge)",
    longDesc = u"""
    Provenance: Direct (model compound). Bibenzyl PhCH2-CH2Ph central C-C BDE
    62.9 kcal/mol, A = 10^15.3 s^-1. Used as analog initiation for benzylic
    C-C bonds in the novolak network. NOTE: the actual novolak bridge is the
    DPM-type Ph-CH2-Ph linkage (BDE ~100 kcal/mol, far less reactive at TGA
    temperatures); this entry represents the *minority* dibenzyl-type linkage
    population that may exist from imperfect cure or post-cure cross-linking.
    Uncertainty factor: x3.
    """,
)

# ------------------------------------------------------------------------------
# Stage II — H-abstraction at the bridge methylene (chain propagation)
# ------------------------------------------------------------------------------
# The bridge model is diphenylmethane (DPM, Ph-CH2-Ph). The actual novolak
# bridge is a hydroxylated diphenylmethane (2,2'-methylenebisphenol etc.); DPM
# is the simpler stand-in for which rate analogies are best-characterised.
# Uncertainty x5-x10 since direct novolak rates are unavailable.

entry(
    index = 2,
    label = "H + DPM <=> H2 + DPM_rad",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.20e14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (8.235, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R2: H abstraction at the bridge CH2 by H atom (toluene analog)",
    longDesc = u"""
    Provenance: Analogy. Transferred from H + toluene (Tsang & Hampson 1986
    type fit, validated 600-1100 K). The bridge benzylic C-H BDE in DPM is
    ~85 kcal/mol, ~3 kcal/mol weaker than toluene's primary benzylic; this
    rate slightly under-estimates abstraction in the resin. Degeneracy 2 for
    the two equivalent bridge H atoms. Uncertainty factor: x5.
    """,
)

entry(
    index = 3,
    label = "CH3 + DPM <=> CH4 + DPM_rad",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (9.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R3: H abstraction at the bridge CH2 by methyl (toluene analog)",
    longDesc = u"""
    Provenance: Analogy. Toluene + CH3 -> CH4 + benzyl (rate-rule fit). Major
    pathway for CH4 production in the TGA window. Degeneracy 2. Uncertainty
    factor: x5.
    """,
)

entry(
    index = 4,
    label = "phenoxyl + DPM <=> phenol + DPM_rad",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (13.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R4: H abstraction at the bridge CH2 by phenoxyl (rate-rule)",
    longDesc = u"""
    Provenance: Analogy / rate-rule estimate. Phenoxyl is the dominant
    chain-carrier in phenolic pyrolysis (high steady-state concentration once
    OH-bearing rings activate); abstracting benzylic H regenerates phenol
    closing the propagation loop. Direct rate not measured for either toluene
    or DPM; transferred from PhO + CH4 rate-rule with adjustment for the
    weaker benzylic C-H. DR-3 flagged as a major sensitivity. Uncertainty
    factor: x10.
    """,
)

# ------------------------------------------------------------------------------
# Stage II — β-scission via the ortho-quinone-methide pathway
# ------------------------------------------------------------------------------

entry(
    index = 5,
    label = "oHO_BzOH <=> oQM + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e15, 's^-1'),
        n = 0.0,
        Ea = (64.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R5: 2-hydroxybenzyl alcohol cyclodehydration (methylol defect route)",
    longDesc = u"""
    Provenance: Direct (model compound, VLPP-MS). 2-hydroxybenzyl alcohol
    (a methylol-bearing defect representative of incompletely-cured resin)
    eliminates water to form ortho-quinone methide. Important if the resin
    has residual -CH2OH groups; minor for fully cured novolak.
    Uncertainty factor: x3.
    """,
)

entry(
    index = 6,
    label = "oHO_Bz_rad <=> oQM + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e13, 's^-1'),
        n = 0.0,
        Ea = (24.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R6: β-scission of 2-hydroxybenzyl radical → o-QM + H",
    longDesc = u"""
    Provenance: QM/analogy. β-scission of the benzylic-radical hydroxybenzyl
    species produces ortho-quinone methide (oQM) and an H atom. Central
    pathway in DR-3 for the *condensed-radical → volatile* transition;
    feeds H back into the propagation loop. Uncertainty factor: x5.
    """,
)

entry(
    index = 7,
    label = "oQM <=> benzene + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e10, 's^-1'),
        n = 0.7,
        Ea = (42.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R7: o-quinone methide unimolecular decomposition → benzene + CO",
    longDesc = u"""
    Provenance: QM/QRRK (da Silva & Bozzelli line of work). Decarbonylation of
    o-QM produces benzene and CO. Primary source of CO in the TGA window.
    Uncertainty factor: x3.
    """,
)

# ------------------------------------------------------------------------------
# Stage II — ipso phenol release (the canonical novolak volatile-release route)
# ------------------------------------------------------------------------------

entry(
    index = 8,
    label = "H + BzPhOH <=> benzyl_rad + phenol",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (9.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R8: ipso displacement of benzyl from 2-benzylphenol → phenol",
    longDesc = u"""
    Provenance: Analogy / rate-rule (Pelucchi / Pratali Maffei phenolic
    rate rules). H attacks the phenolic ring ipso to the methylene bridge,
    expelling the benzyl group as a free radical and releasing the phenol
    moiety intact. This is the canonical mechanism for phenol release from
    novolak. The 2-benzylphenol substrate is the simplest model compound
    that captures both the bridge and the phenolic OH. Uncertainty factor: x10.
    """,
)

# ------------------------------------------------------------------------------
# Stage III — high-T secondary chemistry (phenol/phenoxyl decomposition)
# ------------------------------------------------------------------------------

entry(
    index = 9,
    label = "phenol <=> cpd + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e12, 's^-1'),
        n = 0.0,
        Ea = (60.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R9: phenol unimolecular decomposition → cyclopentadiene + CO",
    longDesc = u"""
    Provenance: Direct/QM literature compilation. Phenol decomposes to
    cyclopentadiene plus CO at high T (>1000 K). In the TGA window this is a
    minor secondary channel; included so phenol does not pile up unrealistically
    in gas-phase residence. Uncertainty factor: x3.
    """,
)

entry(
    index = 10,
    label = "phenoxyl <=> cpdyl + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.0e11, 's^-1'),
        n = 0.0,
        Ea = (43.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R10: phenoxyl decarbonylation → cyclopentadienyl + CO",
    longDesc = u"""
    Provenance: QM (AI-TST-ME / RRKM, model compound). Key high-T CO source
    once phenoxyl pool builds up. The rate parameters are a representative
    Arrhenius fit at ~1000 K to the full RRKM expression in the original
    source (the original is non-Arrhenius). Uncertainty factor: x3.
    """,
)

# ------------------------------------------------------------------------------
# Stage II — termination (radical recombination)
# ------------------------------------------------------------------------------

entry(
    index = 11,
    label = "H + benzyl_rad <=> toluene",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.0e13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"R11: H + benzyl radical recombination → toluene (barrierless)",
    longDesc = u"""
    Provenance: Direct (model compound). Barrierless radical recombination;
    competes with H atom propagation and dampens the benzyl radical pool.
    Uncertainty factor: x2.
    """,
)
