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

entry(
    index = 12,
    label = "trimer_rad33 => C17arylA + vinylxylenol_a",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.2e12, 's^-1'),
        n = 0,
        Ea = (23.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"BEP: novolak trimer bridge alpha-benzylic radical beta-scission",
    longDesc = u"""
    Provenance: BEP estimate. Bridge beta-scission of the trimer alpha-benzylic
    radical C27H31O3(33), ejecting a vinyl-substituted ring (volatile C10H12O,
    MW=148) and leaving an aryl sigma radical co-fragment. Rate from
    Stein/Robaugh 1982 bibenzyl beta-scission (JACS 104, 6567, Ea=26.6 kcal/mol,
    A=10^12.5 s^-1) with a -3.6 kcal/mol BEP correction for the ortho-OH
    substituent (DR2/S2.md, 4/4 sources). Mirrors training entries 5005-5006 in
    R_Addition_MultipleBond. This seed-library entry bypasses the rate-rule
    structural matching that failed to propose the reaction in v1-v6 (the
    two-ring-substituent trimer radical never matched the template leaf node);
    it is the MVP enabler for first fragmentation of the C27 trimer backbone.
    Will be superseded by Direct/QM rates from ARC R2/R4 when available.

    Marked irreversible (=>) 2026-07-11 for the poly_102 regeneration: the
    reverse direction (aryl sigma-radical re-addition across the melt/gas
    reference-state boundary) carries an unpaired reference-state term
    (U ~ 12 decades; RMG-Py HEAD thermo reference-state tripwire,
    rmgpy/solver/polymer.pyx). The BEP forward rate is the only defensible
    direction; reverse recombination of an ejected volatile with a melt aryl
    radical is negligible at pyrolysis temperatures.
        Uncertainty factor: x10.
    """,
)

entry(
    index = 13,
    label = "trimer_rad38 => dmHOphenyl + C19vinyl",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.2e12, 's^-1'),
        n = 0,
        Ea = (23.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"BEP: novolak trimer bridge alpha-benzylic radical beta-scission",
    longDesc = u"""
    Provenance: BEP estimate. Bridge beta-scission of the trimer alpha-benzylic
    radical C27H31O3(38), ejecting a vinyl-substituted ring (volatile C8H9O,
    MW=121) and leaving an aryl sigma radical co-fragment. Rate from
    Stein/Robaugh 1982 bibenzyl beta-scission (JACS 104, 6567, Ea=26.6 kcal/mol,
    A=10^12.5 s^-1) with a -3.6 kcal/mol BEP correction for the ortho-OH
    substituent (DR2/S2.md, 4/4 sources). Mirrors training entries 5005-5006 in
    R_Addition_MultipleBond. This seed-library entry bypasses the rate-rule
    structural matching that failed to propose the reaction in v1-v6 (the
    two-ring-substituent trimer radical never matched the template leaf node);
    it is the MVP enabler for first fragmentation of the C27 trimer backbone.
    Will be superseded by Direct/QM rates from ARC R2/R4 when available.

    Marked irreversible (=>) 2026-07-11 for the poly_102 regeneration: the
    reverse direction (aryl sigma-radical re-addition across the melt/gas
    reference-state boundary) carries an unpaired reference-state term
    (U ~ 12 decades; RMG-Py HEAD thermo reference-state tripwire,
    rmgpy/solver/polymer.pyx). The BEP forward rate is the only defensible
    direction; reverse recombination of an ejected volatile with a melt aryl
    radical is negligible at pyrolysis temperatures.
        Uncertainty factor: x10.
    """,
)

entry(
    index = 14,
    label = "trimer_rad44 => vinylxylenol_b + C17arylB",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.2e12, 's^-1'),
        n = 0,
        Ea = (23.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"BEP: novolak trimer bridge alpha-benzylic radical beta-scission",
    longDesc = u"""
    Provenance: BEP estimate. Bridge beta-scission of the trimer alpha-benzylic
    radical C27H31O3(44), ejecting a vinyl-substituted ring (volatile C10H12O,
    MW=148) and leaving an aryl sigma radical co-fragment. Rate from
    Stein/Robaugh 1982 bibenzyl beta-scission (JACS 104, 6567, Ea=26.6 kcal/mol,
    A=10^12.5 s^-1) with a -3.6 kcal/mol BEP correction for the ortho-OH
    substituent (DR2/S2.md, 4/4 sources). Mirrors training entries 5005-5006 in
    R_Addition_MultipleBond. This seed-library entry bypasses the rate-rule
    structural matching that failed to propose the reaction in v1-v6 (the
    two-ring-substituent trimer radical never matched the template leaf node);
    it is the MVP enabler for first fragmentation of the C27 trimer backbone.
    Will be superseded by Direct/QM rates from ARC R2/R4 when available.

    Marked irreversible (=>) 2026-07-11 for the poly_102 regeneration: the
    reverse direction (aryl sigma-radical re-addition across the melt/gas
    reference-state boundary) carries an unpaired reference-state term
    (U ~ 12 decades; RMG-Py HEAD thermo reference-state tripwire,
    rmgpy/solver/polymer.pyx). The BEP forward rate is the only defensible
    direction; reverse recombination of an ejected volatile with a melt aryl
    radical is negligible at pyrolysis temperatures.
        Uncertainty factor: x10.
    """,
)

# ==============================================================================
# v9 additions (2026-05-27) — make the char-competition + peak fix canonical.
# See ~/runs/RMG/poly_101/v9_report.md. NOTE: the v8 "second beta-scission" of
# the aryl sigma-radicals (C17arylA/B) was found MECHANISTICALLY INVALID (an aryl
# ring-carbon radical cannot beta-scission its own bridge) and is deliberately
# NOT included; the valid multi-step route (cap -> benzylic H-abs -> beta-scis)
# is seeded instead (entries 19-24).
# ==============================================================================

# ------------------------------------------------------------------------------
# Stage I — facile initiation: applied at the SPLICE step, not seeded.
# The physical bridge homolysis (proxy -> C9H11O + C18H21O2) is degenerate under
# kineticsFamilies=['polymers'] -- RMG cannot generate sinks for the benzyl
# products, which then consume all proxy and short-circuit the cascade (residue
# 100% C18H21O2, char chemistry inactive). The lumped initiation
# (proxy => trimer_rad33 + H, Ea=62.9, the C-C-homolysis rate) is injected in
# splice_yaml.py instead -- it directly produces the propagating radical that has
# the seeded beta-scission sink. See ~/runs/RMG/poly_101/v9_report.md.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Stage III — char formation (dehydrogenative cross-linking of aryl radicals)
# ------------------------------------------------------------------------------
# 0-D-robust char route: the literal 2 Ar. -> biaryl recombination (R24) is
# radical-radical and ~1000x suppressed at the reactor's gas-phase concentrations,
# so char is represented as the *unimolecular* dehydrogenative cross-linking /
# aromatization of the reactive aryl sigma-radicals (report R24/R26): the radical
# aromatizes into the char network (stilbene-type vinylene-bridge lump), releasing
# H. This is the competitor that fixes the v8 overshoot. Uncertainty factor: x10.

entry(
    index = 16,
    label = "C17arylA <=> char_C17 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A = (1.0e12, 's^-1'), n = 0.0, Ea = (12.0, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R16: aryl-radical dehydrogenative cross-linking -> char (C17arylA)",
    longDesc = u"""
    Provenance: Lumped/Analogy (report R24/R26 aryl cross-linking + aromatization).
    Unimolecular surrogate for condensed-phase aryl-radical cross-linking, robust to
    the 0-D gas-phase dilution that suppresses the literal bimolecular recombination.
    char_C17 = stilbene-type vinylene-bridge lump (non-volatile). Competes with the
    volatilize branch (entries 19-22). Uncertainty factor: x10.
    """,
)

entry(
    index = 17,
    label = "C17arylB <=> char_C17 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A = (1.0e12, 's^-1'), n = 0.0, Ea = (12.0, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R17: aryl-radical dehydrogenative cross-linking -> char (C17arylB)",
    longDesc = u"""
    Provenance: Lumped/Analogy (report R24/R26). As R16; C17arylB is the OH-position
    isomer of C17arylA and cross-links to the same char_C17 lump. Uncertainty x10.
    """,
)

entry(
    index = 18,
    label = "C19rad <=> char_C19 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A = (1.0e12, 's^-1'), n = 0.0, Ea = (12.0, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R18: aryl/benzylic-radical dehydrogenative cross-linking -> char (C19)",
    longDesc = u"""
    Provenance: Lumped/Analogy (report R24/R26). Cross-linking of the activated C19
    benzylic radical to char_C19; competes with its beta-scission (entry 24).
    Uncertainty x10.
    """,
)

# ------------------------------------------------------------------------------
# Stage II — volatilize branch (VALID multi-step competitor to char)
# ------------------------------------------------------------------------------
# The aryl sigma-radical cannot beta-scission its own bridge directly; the valid
# route is: cap the aryl radical -> benzylic H-abstraction at the remaining bridge
# -> beta-scission of the benzylic radical. Reuses existing volatiles (C7H7O_cresyl,
# vinylxylenol_a/_b, dmHOphenyl).

entry(
    index = 19,
    label = "H + C17arylA <=> C17arylA_H",
    degeneracy = 1,
    kinetics = Arrhenius(A = (1.0e14, 'cm^3/(mol*s)'), n = 0.0, Ea = (0.0, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R19: aryl sigma-radical + H recombination -> stable C17 arene (barrierless)",
    longDesc = u"""
    Provenance: Direct (barrierless aryl + H recombination). Caps the reactive aryl
    sigma-radical to the closed-shell C17 arene C17arylA_H, the precursor to the
    valid second-generation beta-scission. Uncertainty factor: x2.
    """,
)

entry(
    index = 20,
    label = "H + C17arylB <=> C17arylA_H",
    degeneracy = 1,
    kinetics = Arrhenius(A = (1.0e14, 'cm^3/(mol*s)'), n = 0.0, Ea = (0.0, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R20: aryl sigma-radical + H recombination (C17arylB, isomeric lump)",
    longDesc = u"""
    Provenance: Direct (barrierless). As R19; C17arylB caps to the same isomeric
    C17arylA_H lump. Uncertainty factor: x2.
    """,
)

entry(
    index = 21,
    label = "H + C17arylA_H <=> H2 + C17benzrad",
    degeneracy = 4,
    kinetics = Arrhenius(A = (1.20e14, 'cm^3/(mol*s)'), n = 0.0, Ea = (8.235, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R21: benzylic H-abstraction at the C17 bridge by H (toluene analog)",
    longDesc = u"""
    Provenance: Analogy. Same H + benzylic-CH2 rate as seed R2 (H + DPM). Activates
    the stable C17 arene to the bridge benzylic radical C17benzrad, which can then
    beta-scission. Degeneracy 4 (two CH2 groups x two H). Uncertainty factor: x5.
    """,
)

entry(
    index = 22,
    label = "C17benzrad <=> C7H7O_cresyl + vinylxylenol_b",
    degeneracy = 1,
    kinetics = Arrhenius(A = (3.2e12, 's^-1'), n = 0.0, Ea = (23.0, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R22: second-generation bridge beta-scission of the C17 benzylic radical",
    longDesc = u"""
    Provenance: BEP estimate (same as seed entries 12-14): Stein/Robaugh 1982
    bibenzyl beta-scission (Ea=26.6, A=10^12.5 s^-1) with -3.6 kcal/mol ortho-OH BEP
    correction (DR2/S2.md). The benzylic radical ejects a vinylxylenol (C10, volatile)
    leaving a cresyl aryl radical (C7H7O, volatile). This is the VALID realization of
    the v8 extent fix's net products. Uncertainty factor: x10.
    """,
)

entry(
    index = 23,
    label = "H + C19vinyl <=> H2 + C19rad",
    degeneracy = 4,
    kinetics = Arrhenius(A = (1.20e14, 'cm^3/(mol*s)'), n = 0.0, Ea = (8.235, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R23: benzylic H-abstraction activating the closed-shell C19 fragment",
    longDesc = u"""
    Provenance: Analogy (seed R2). C19vinyl is the closed-shell C19 first-cut fragment;
    H-abstraction at its remaining bridge gives the benzylic radical C19rad, opening its
    char-vs-volatilize competition. Degeneracy 4. Uncertainty factor: x5.
    """,
)

entry(
    index = 24,
    label = "C19rad <=> C9H9O + vinylxylenol_a",
    degeneracy = 1,
    kinetics = Arrhenius(A = (3.2e12, 's^-1'), n = 0.0, Ea = (23.0, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R24: second-generation bridge beta-scission of the C19 benzylic radical",
    longDesc = u"""
    Provenance: BEP estimate (as entries 12-14, 22). Ejects a vinylxylenol (C10,
    volatile) leaving a C9H9O aryl radical (volatile). Competes with C19 char (entry 18).
    Uncertainty factor: x10.
    """,
)

# ------------------------------------------------------------------------------
# Stage III — char maturation / carbonization (v10, 2026-05-27)
# ------------------------------------------------------------------------------
# The v9 char (char_C17/char_C19) was terminal -> the TGA was flat above the main
# peak. Real novolak char keeps losing mass at high T (Zone III: dehydrogenation,
# decarbonylation, ring-fusion -> H2, CO, CH4). These two lumped maturation steps
# give the second high-T DTG peak (~660-720 C) and pull the residue toward the
# literature 55+/-5 wt%. The matured lumps (char_mature17/_19) are more-condensed
# fused aromatics. Rate = the seed's own phenol decarbonylation (R9: A=1e12,
# Ea=60.8); the 2nd-peak position + extent EMERGE from it. See v9_report.md / v10.

entry(
    index = 25,
    label = "char_C17 <=> char_mature17 + CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A = (1.0e12, 's^-1'), n = 0.0, Ea = (60.8, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R25: Zone-III char maturation (decarbonylation + dehydrogenation), C17",
    longDesc = u"""
    Provenance: Analogy (seed R9, phenol -> CO + cpd: A=1e12, Ea=60.8 kcal/mol).
    Lumped high-T carbonization of the C17 char: a phenolic ring decarbonylates
    (-> CO) and the structure dehydrogenatively fuses (-> H2), leaving a more-
    condensed aromatic lump (char_mature17, C16H16O). Gives the second high-T DTG
    peak the v9 terminal-char model lacked. Uncertainty factor: x10.
    """,
)

entry(
    index = 26,
    label = "char_C19 <=> char_mature19 + CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A = (1.0e12, 's^-1'), n = 0.0, Ea = (60.8, 'kcal/mol'), T0 = (1, 'K')),
    shortDesc = u"R26: Zone-III char maturation (decarbonylation + demethanation), C19",
    longDesc = u"""
    Provenance: Analogy (seed R9). As R25 for the C19 char; releases CO + CH4
    (both classic Zone-III novolak gases) leaving char_mature19 (C17H16O).
    Uncertainty factor: x10.
    """,
)
