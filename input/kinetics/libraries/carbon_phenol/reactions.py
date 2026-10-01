#!/usr/bin/env python
# encoding: utf-8

name = "carbon_phenol"
shortDesc = u"Consolidated phenolic-carbon pyrolysis library: novolac net-VE surrogate rows, net condensation water release, and o-QM/cresol/xylenol secondary cracking (COLIBRIv5 + da Silva 2007)."
longDesc = u"""
Consolidated library for phenolic (novolac / phenol-formaldehyde) carbon
chemistry on the RMG polymer branch. It merges and RETIRES the former
novolac_net_VE_surrogate library (its two rows are carried here VERBATIM as
entries 1-2): any deck whose reactionLibraries still names
'novolac_net_VE_surrogate' must switch to 'carbon_phenol'.

Contents, by provenance class:
  * Entries 1-2 - net first-order VE surrogate rows for novolac
    methylene-bridge volatile release (phenol / o-cresol split), Petrocelli &
    Klein 1984 (DOI 10.1021/ma00132a008). Lumped (net measured, model-compound
    analog). Moved unchanged from novolac_net_VE_surrogate.
  * Entry 3 - net condensation water-release VE row (novolac ->
    cyclic-ether daughter + H2O), ESTIMATED apparent kinetics bounded by the
    Torres-Herrador isoconversional stage-I band (DOI 10.2514/1.J059423).
    This is the polymer-side booking of phenolic OH + OH condensation; the
    elementary gas-phase truth lives in the Aryl_Ether_Condensation family.
  * Entries 4-5 - o-quinone-methide decomposition: the Dorrestijn 1997
    MEASURED rate for the parent o-QM (the choice COLIBRIv5 also makes; the
    da Silva & Bozzelli 2007 theory recommendation, DOI 10.1021/jp073335c, is
    retained in entry 4's longDesc as the cross-check defining the channel's
    ~25x uncertainty band), and the same measured rate transferred to
    methyl-o-QM by analogy, again following COLIBRIv5.
  * Entries 6-10 - cresol/xylenol secondary cracking rows taken from the
    COLIBRIv5 mechanism SI (Meziane, Delort, Bounaceur, Carstensen,
    Battin-Leclerc, Herbinet, Prog. React. Kinet. Mech. 51 (2026) e003,
    DOI 10.48130/prkm-0025-0027, CC BY 4.0; CHEMKIN SI file, default units
    cal/mol; underlying G4/CBS-QB3 calculations from that work plus
    Carstensen & Dean IJCK 44 (2012) 75-89 and Zhu & Bozzelli 2003/NIST).

SUPERSESSION: entries 4 and 8 supersede the project-local phenolic_pyrolysis
library rows R7 (oQM <=> benzene + CO, Ea = 42.0 kcal/mol, ~25 kcal/mol BELOW
the measured value) and R6 (oHO_Bz_rad <=> oQM + H, Ea = 24.0 kcal/mol,
~33 kcal/mol below the G4 value). Those two rows have been REMOVED from
phenolic_pyrolysis on this branch (they carry pointer notes), so co-loading
the two libraries is safe again; if an older phenolic_pyrolysis revision is
in play, remove R6/R7 there first.

Deliberate omission: the o-cresol O-H bond fission itself is NOT booked here.
The only COLIBRIv5 row for it is a 1-atm PLOG slice of the phenol analogy
(A = 6.58e38, n = -6.88), which is pressure-specific and the weakest
provenance in the candidate set; RMG's R_Recombination family generates the
reaction natively. The clean xylenol analog (entry 9) IS booked because its
source rate (Zhu & Bozzelli 2003) is a simple Arrhenius expression.

ACTIVATION SCOPE of entries 1-3: these net VE surrogate rows are valid ONLY
in decks that declare the matching novolac polymer pool and run the polymer
conduit; they are INVALID as ordinary gas-phase chemistry. Their reactant
(novolac_trimer_proxy) exists only in such decks, so in any other deck they
are inert by construction (a library reaction never activates unless its
reactants enter the model) -- but a deck that deliberately initializes the
C24H26O3 proxy as a gas species would wrongly animate them. Entry 3
additionally requires reactors at or below ~700 K (see its validity caveat).

COUPLING: entries 1-3 fire only while the committed novolac_trimer_proxy
graph remains isomorphic (strict=False) to the consuming deck's stitched pool
proxy; deck monomer/stitching revisions require revisiting this dictionary.
"""

entry(
    index = 1,
    label = "novolac_trimer_proxy => C18H20O2_oQE_daughter + phenol",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.5e12, 's^-1'),
        n = 0,
        Ea = (66000, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (873, 'K'),
    ),
    shortDesc = u"Net novolac bridge-scission phenol-release surrogate, 0.5 branch of the Petrocelli & Klein 1984 Table II DPM rate (Fig 6 ~1:1 branching)",
    longDesc = u"""
    Phenol branch (benzene-analog) of the split net first-order surrogate
    for novolac methylene-bridge volatile release: one phenol-class
    aromatic volatile per bridge-scission event on this branch; A-factor
    is HALF the source's net rate (2.5e12 of 5.0e12 s^-1) so that this row
    plus the o-cresol row sum exactly to the total bridge-disappearance
    rate k from Petrocelli & Klein 1984 Table II (diphenylmethane analog,
    log A = 12.7 s^-1, E* = 66.0 kcal/mol, measured 550/600 C). The 1:1
    branch ratio is the source's Fig 6 measured ~1:1 benzene:toluene
    product split, mapped via the authors' benzene->phenol correspondence
    for the hydroxylated bridge. NOT elementary (E* well below the
    ~85 kcal/mol homolysis BDE); valid only as benchmark closure over the
    source condition envelope.

    Caveats: (1) unsubstituted-analog transfer -- the rate is the net
    disappearance rate of diphenylmethane (no OH, no ring methyls),
    applied to the methylated/hydroxylated novolac bridge substrate; ring
    substituents are expected to perturb both A and E* by amounts the
    source does not quantify. (2) 2-temperature fit -- A and E* derive
    from measurements at only two temperatures (550 and 600 C, 823/873 K),
    so the Arrhenius extrapolation outside 823-873 K is unconstrained.
    (3) branch-ratio transfer -- the ~1:1 split is measured for DPM
    benzene:toluene; its transfer to phenol:cresol on the substituted
    bridge inherits the same unquantified substituent uncertainty.

    Product shape: the heavy co-product C18H20O2 is the trimer proxy after
    phenol-analog loss of one terminal ring (ring + OH, H-capped), with
    the bridge CH2 retained on the daughter as an exocyclic terminus and
    the ejected ring's methyl bookkeeping-retained on that exocyclic
    carbon (o-quinone-ethylidene terminus); SMILES
    CC=C1C(=O)C=C(C)C=C1Cc1c(C)cc(C)cc1O. Element-balanced against the
    proxy (C24H26O3 - C6H6O = C18H20O2) so the polymer-branch
    concerted-loss evidence gate books it as the novolac_lossC6H6O feature
    daughter (defect +94.111 g/mol) rather than an ordinary gas species;
    the daughter graph is bookkeeping-only (the methyl placement is an
    accounting choice, not a mechanistic migration claim).
    Irreversible (=>): re-addition of an ejected volatile across the
    melt/gas reference-state boundary is not defensible for a net
    surrogate.
    Provenance class: Lumped (net measured rate, model-compound analog).
    Uncertainty factor: x10.
    """,
)

entry(
    index = 2,
    label = "novolac_trimer_proxy => C17H18O2_oQM_daughter + o_cresol",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.5e12, 's^-1'),
        n = 0,
        Ea = (66000, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (873, 'K'),
    ),
    shortDesc = u"Net novolac bridge-scission cresol-release surrogate, 0.5 branch of the Petrocelli & Klein 1984 Table II DPM rate (Fig 6 ~1:1 branching)",
    longDesc = u"""
    o-Cresol branch (toluene-analog) of the split net first-order
    surrogate for novolac methylene-bridge volatile release: one
    cresol-class aromatic volatile per bridge-scission event on this
    branch (cresol/xylenol product isomers collapsed to o-cresol at
    MW 108.14); A-factor is HALF the source's net rate (2.5e12 of
    5.0e12 s^-1) so that this row plus the phenol row sum exactly to the
    total bridge-disappearance rate k from Petrocelli & Klein 1984
    Table II (diphenylmethane analog, log A = 12.7 s^-1,
    E* = 66.0 kcal/mol, measured 550/600 C). The 1:1 branch ratio is the
    source's Fig 6 measured ~1:1 benzene:toluene product split, mapped via
    the authors' toluene->cresol correspondence for the hydroxylated
    bridge. NOT elementary (E* well below the ~85 kcal/mol homolysis BDE);
    valid only as benchmark closure over the source condition envelope.

    Caveats: (1) unsubstituted-analog transfer -- the rate is the net
    disappearance rate of diphenylmethane (no OH, no ring methyls),
    applied to the methylated/hydroxylated novolac bridge substrate; ring
    substituents are expected to perturb both A and E* by amounts the
    source does not quantify. (2) 2-temperature fit -- A and E* derive
    from measurements at only two temperatures (550 and 600 C, 823/873 K),
    so the Arrhenius extrapolation outside 823-873 K is unconstrained.
    (3) branch-ratio transfer -- the ~1:1 split is measured for DPM
    benzene:toluene; its transfer to phenol:cresol on the substituted
    bridge inherits the same unquantified substituent uncertainty.

    Product shape: the heavy co-product C17H18O2 is the trimer proxy after
    benzene-analog loss of one terminal ring (ring + its ring-methyl + OH,
    H-capped), with the bridge CH2 retained on the daughter as an
    exocyclic methylene (o-quinone-methide terminus); SMILES
    C=C1C(=O)C=C(C)C=C1Cc1c(C)cc(C)cc1O. Element-balanced against the
    proxy (C24H26O3 - C7H8O = C17H18O2) so the polymer-branch
    concerted-loss evidence gate books it as the novolac_lossC7H8O feature
    daughter (defect +108.138 g/mol) rather than an ordinary gas species;
    the daughter graph is bookkeeping-only.
    Irreversible (=>): re-addition of an ejected volatile across the
    melt/gas reference-state boundary is not defensible for a net
    surrogate.
    Provenance class: Lumped (net measured rate, model-compound analog).
    Uncertainty factor: x10.
    """,
)

entry(
    index = 3,
    label = "novolac_trimer_proxy => C24H24O2_cyclic_ether_daughter + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.0e5, 's^-1'),
        n = 0,
        Ea = (85, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (423, 'K'),
        Tmax = (673, 'K'),
    ),
    shortDesc = u"ESTIMATED net stage-I condensation water-release surrogate: intra-chain phenolic OH + OH -> cyclic aryl ether + H2O (apparent kinetics, Torres-Herrador stage-I band)",
    longDesc = u"""
    ESTIMATED (rank-10-equivalent) net apparent row booking the stage-I/II
    condensation water release of cured phenolics on the polymer pool:
    two phenolic OH groups on adjacent methylene-bridged units condense to
    a cyclic diaryl ether plus water (Trick & Saliba, Carbon 33 (1995)
    1509, stage-I water assignment; Jackson & Conley 1964 condensation
    chemistry). This is the POLYMER-SIDE booking of the chemistry whose
    elementary gas-phase truth is the Aryl_Ether_Condensation family: the
    bimolecular family applied to two polymer proxies would produce
    hexamer-scale products that bust the polymer-branch DP caps and
    conduit shapes and therefore contributes zero polymer flux; a net
    first-order VE row on the pool is the only booking that releases water
    from the condensed phase in the current method-of-moments framework.

    Kinetics are APPARENT, not elementary, and are an explicit ESTIMATE:
    A = 1.0e5 s^-1 with Ea = 85 kJ/mol sits inside the Torres-Herrador et
    al. isoconversional apparent band for stage-I phenolic-resin
    decomposition (81.6-93.5 kJ/mol, DOI 10.2514/1.J059423;
    transport-convolved condensed-phase values), giving k(500 K) ~ 1.3e-4
    s^-1, the scale of the observed stage-I DTG water-release peak. The
    intrinsic (elementary) barrier is far higher (ReaxFF water-formation
    barriers in crosslinked phenolics: 42-49 kcal/mol, DOI
    10.1016/j.polymer.2010.12.034); the low apparent value lumps site
    availability, chain mobility, and transport. Replacement path: an
    in-house ARC/Arkane CBS-QB3 elementary condensation rate combined with
    an explicit site-concentration model. Uncertainty factor: >= x30.

    VALIDITY ENFORCEMENT CAVEAT: RMG does not enforce Tmin/Tmax at
    simulation time. Extrapolated beyond 673 K this apparent fit reaches
    ~1 s^-1 at 900 K and would unphysically dominate pool mass loss; the
    real stage-I channel shuts down by RESERVOIR EXHAUSTION (the finite
    phenolic-OH pair inventory, a few wt% of resin mass as water), which
    the method-of-moments pool cannot express. This is structural, not
    parametric: ANY A/Ea pair inside the Torres-Herrador band anchored at
    the stage-I DTG scale extrapolates to the same order at 900 K. Decks
    whose reactors exceed ~700 K must either exclude this row or treat
    the high-temperature water flux as diagnostic only.

    Separation from the Aryl_Ether_Condensation family is structural, not
    advisory: the bimolecular family cannot deliver polymer-pool flux
    (its polymer-scale products bust the DP-preservation caps and conduit
    shapes and are refused, verified on this branch), and this row does
    not touch gas-phase phenols -- the two book disjoint OH inventories.

    Product shape: the daughter is the trimer proxy after loss of the
    central ring's OH (as water, taking one H from the chain-end phenol
    whose oxygen becomes the ether); SMILES
    Cc1cc(O)cc(Cc2c3cc(C)cc2Cc2c(C)cc(C)cc2O3)c1, element-balanced
    (C24H26O3 - H2O = C24H24O2). The lit-corroborated intra-chain
    condensation motif in novolac chars is XANTHENE
    (xanthene/dimethylxanthene in Py-GC-MS product slates, DOI
    10.1016/j.polymdegradstab.2012.04.016); on this proxy's substitution
    pattern neither OH pair is ortho-ortho across a shared methylene
    bridge, so every available ring closure is the homologous 7-membered
    dibenzoxepine-type ether ring, and that is what the daughter graph
    carries. The daughter graph is bookkeeping-only: under the
    concerted-loss evidence gate it is absorbed into the novolac_lossH2O
    feature pool (cumulative chain-mass defect 18.015 g/mol per event) and
    never realized as an ordinary gas-phase species. The ejected gas
    (H2O, MW 18.015 < monomer MW 120.148) passes the DP-preservation cap;
    eject_units = 18.015/120.148 ~ 0.1500.
    Irreversible (=>): rehydration across the melt/gas boundary is not
    defensible for a net surrogate.
    Provenance class: Estimated (apparent-band bounded).
    """,
)

entry(
    index = 4,
    label = "oQM => benzene + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.31e14, 's^-1'),
        n = 0,
        Ea = (67160, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (850, 'K'),
        Tmax = (1050, 'K'),
    ),
    shortDesc = u"o-Quinone methide unimolecular decomposition to benzene + CO, Dorrestijn 1997 measured rate (as adopted by COLIBRIv5)",
    longDesc = u"""
    Measured total unimolecular decomposition rate of o-quinone methide
    (6-methylene-2,4-cyclohexadien-1-one): k = 6.31e14 exp(-33,800 K / T)
    s^-1 (Ea = 67.16 kcal/mol), measured ~850-1050 K by Dorrestijn and
    Mulder (1997; reported in da Silva & Bozzelli 2007, DOI
    10.1021/jp073335c, and adopted verbatim by the COLIBRIv5 mechanism,
    SI L5633, O-OC6H4CH2=A1+CO). The measurement window overlaps the
    novolac TGA benchmark's high-temperature end, which is why the
    measured value is booked over the theory recommendation. The minor
    fulvene + CO channel (benzene:fulvene ~ 90:10 at 900-950 K per
    da Silva) is folded into this single benzene-channel row.

    Cross-check defining the uncertainty band: da Silva & Bozzelli 2007
    recommend from CBS-QB3/RRKM k = 2.64e14 exp(-35,900 K / T) s^-1 over
    800-2400 K (kiloKelvin exponent notation in the paper; 71.34
    kcal/mol), ~25x SLOWER at 900 K with the spread growing toward lower
    T. The measurement-vs-theory disagreement is inherited from the
    primary sources and is the channel's real uncertainty band.

    Booked irreversible: the rate is a measured NET decomposition over a
    multistep path (bicyclic intermediate); thermo-reversal of a net step
    is not meaningful, and benzene + CO re-addition is negligible at
    benchmark conditions.

    SUPERSEDES phenolic_pyrolysis R7 (same reaction, Ea = 42.0 kcal/mol,
    ~25 kcal/mol below this measurement; removed from that library on
    this branch).
    Provenance class: Measurement (via secondary reporting; primary
    Dorrestijn PDFs pending retrieval).
    """,
)

entry(
    index = 5,
    label = "methyl_oQM => toluene + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.31e14, 's^-1'),
        n = 0,
        Ea = (67160, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"Methyl-o-quinone methide decomposition to toluene + CO, Dorrestijn-1997-analogy as adopted by COLIBRIv5",
    longDesc = u"""
    Unimolecular decomposition of methyl-o-quinone methide (the o-cresol /
    methylated-ring analog of o-QM; the terminus motif of methylated
    novolac bridge-scission daughters) to toluene + CO. Rate is the
    Dorrestijn & Mulder 1997 measured parent-o-QM rate transferred
    unchanged to the methylated ring, exactly as adopted by COLIBRIv5
    (SI L8648, XYLMETHIDE=A1CH3+CO, 6.31e14 exp(-67,160 cal/mol / RT);
    Meziane et al. 2026, DOI 10.48130/prkm-0025-0027). Identical to the
    parent rate booked in entry 4, so the parent/methyl pair is
    source-consistent; the measurement-vs-theory spread documented there
    applies here in full. Booked irreversible for the same net-step
    reason as entry 4.
    Provenance class: Analogy (measured parent-species rate).
    """,
)

entry(
    index = 6,
    label = "o_methylphenoxy => methylcyclopentadienyl + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(2.5e12, 's^-1'), n=0.48, Ea=(54400, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e12, 's^-1'), n=0.61, Ea=(53300, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"o-Methylphenoxy ring contraction + CO loss to methylcyclopentadienyl, COLIBRIv5 G4 (3 steps lumped, duplicate pair)",
    longDesc = u"""
    CO extrusion with ring contraction of the o-methylphenoxy radical (the
    o-cresol-derived phenoxy) to the methylcyclopentadienyl radical:
    G4 rate calculated in the COLIBRIv5 work itself, lumped over the
    3-step mechanism (SI L5906/L5909, declared DUPLICATE pair, booked here
    as a single MultiArrhenius; Meziane et al., Prog. React. Kinet. Mech.
    51 (2026) e003, DOI 10.48130/prkm-0025-0027, CHEMKIN default units
    cal/mol). Booked irreversible: the source rate is an effective
    multistep-lumped forward rate, and thermo-reversing a lumped step
    manufactures reverse chemistry through uncertain thermo.

    Interaction note: this is the methyl-substituted instance of the
    transformation the Aryl_Decarbonylation family estimates from its
    parent-phenoxy training anchor. RMG's existing-reaction check is
    expected to suppress the family-generated duplicate when this library
    is loaded, but that is a behavior to VERIFY in the generated model
    (part of the polymer-branch generation-run protocol), not a
    guarantee.
    Provenance class: Theory (G4, multistep-lumped).
    """,
)

entry(
    index = 7,
    label = "o_methylphenoxy <=> o_hydroxybenzyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.8e6, 's^-1'),
        n = 1.69,
        Ea = (31200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"o-Methylphenoxy <-> o-hydroxybenzyl H-shift isomerization, COLIBRIv5 G4",
    longDesc = u"""
    Intramolecular H-shift interconverting the o-methylphenoxy radical
    (O-centered) and the o-hydroxybenzyl radical (C-centered): the pivot
    that connects cresol O-H chemistry to the o-QM channel. G4 rate from
    the COLIBRIv5 work (SI L5912; Meziane et al. 2026, DOI
    10.48130/prkm-0025-0027, cal/mol units); the only such isomerization
    in that mechanism (no m-/p- analogs exist there).
    Provenance class: Theory (G4).
    """,
)

entry(
    index = 8,
    label = "o_hydroxybenzyl <=> oQM + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e11, 's^-1'),
        n = 0.95,
        Ea = (57100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"o-Hydroxybenzyl beta-C-H scission to o-quinone methide + H, COLIBRIv5 G4",
    longDesc = u"""
    Beta C-H scission of the o-hydroxybenzyl radical producing o-quinone
    methide plus an H atom -- the radical inlet to the o-QM pool. G4 rate
    from the COLIBRIv5 work (SI L5914; Meziane et al. 2026, DOI
    10.48130/prkm-0025-0027, cal/mol units).

    SUPERSEDES phenolic_pyrolysis R6 (same reaction, A = 1.3e13 s^-1,
    Ea = 24.0 kcal/mol -- ~33 kcal/mol below this G4 value, far below the
    channel endothermicity; removed from that library on this branch).
    Provenance class: Theory (G4).
    """,
)

entry(
    index = 9,
    label = "xylenol_25 <=> dimethylphenoxy_25 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.0e14, 's^-1'),
        n = 0,
        Ea = (87000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"2,5-Dimethylphenol O-H bond fission, Zhu & Bozzelli 2003 via COLIBRIv5",
    longDesc = u"""
    O-H bond fission of 2,5-dimethylphenol (COLIBRIv5's lumped xylenol
    representative, formed there from both xylene isomers) to the
    2,5-dimethylphenoxy radical plus H. Simple-Arrhenius rate credited to
    Zhu & Bozzelli 2003 / NIST in the COLIBRIv5 SI (L8889,
    HOCH3A1CH3=OCH3A1CH3+H; Meziane et al. 2026, DOI
    10.48130/prkm-0025-0027, cal/mol units).

    Isomer-lumping caveat: the graph-natural xylenol of novolac repeat
    units is the 3,5-/2,4-substitution type; this row carries the source's
    2,5-isomer verbatim and should be read as a xylenol-class rate. The
    corresponding o-CRESOL O-H fission is deliberately NOT booked in this
    library (the only COLIBRIv5 row for it is a 1-atm PLOG slice of the
    phenol analogy); RMG's R_Recombination family covers it.
    Provenance class: Literature rate (NIST-tabulated), via COLIBRIv5.
    """,
)

entry(
    index = 10,
    label = "dimethylphenoxy_25 => CO + dimethylcyclopentadienyl",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.5e14, 's^-1'),
        n = 0,
        Ea = (54800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"2,5-Dimethylphenoxy ring contraction + CO loss, Carstensen & Dean 2012 analogy via COLIBRIv5",
    longDesc = u"""
    CO extrusion with ring contraction of the 2,5-dimethylphenoxy radical
    to the dimethylcyclopentadienyl radical, by analogy to Carstensen &
    Dean, Int. J. Chem. Kinet. 44 (2012) 75-89, as adopted by COLIBRIv5
    (SI L11034, OCH3A1CH3=>CO+DMCPDR; Meziane et al. 2026, DOI
    10.48130/prkm-0025-0027, cal/mol units). Booked irreversible exactly
    as written in the source mechanism.
    Provenance class: Analogy (rate-rule transfer), via COLIBRIv5.
    """,
)
