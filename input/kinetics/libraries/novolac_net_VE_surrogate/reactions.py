#!/usr/bin/env python
# encoding: utf-8

name = "novolac_net_VE_surrogate"
shortDesc = u"Net first-order surrogate for novolac methylene-bridge volatile release, split 0.5 phenol + 0.5 o-cresol (benchmark closure, 823-873 K)."
longDesc = u"""
Dedicated NET-SURROGATE library for the novolac (phenol-formaldehyde,
ortho-cresol repeat unit) polymer-pool benchmark deck. It is NOT a reaction
family and NOT part of any recommended set: load it explicitly via
reactionLibraries in a deck that declares the matching novolac polymer pool
(monomer C8H8O, monomer MW 120.148 g/mol; stitched baseline trimer proxy
C24H26O3, SMILES Cc1cc(O)cc(Cc2c(O)cc(C)cc2Cc2c(C)cc(C)cc2O)c1).

TWO rows carry the round-88 "carbon-volatile net-surrogate" channel as a
1:1 BRANCHED pair (the round-88 single collapsed o-cresol row split per the
source's own measured branching): one aromatic volatile released per
methylene-bridge scission event, ejected as
  * phenol (C6H6O, MW 94.111)  -- the benzene-analog branch, or
  * o-cresol (C7H8O, MW 108.14) -- the toluene-analog branch,
each row at HALF the total A-factor (A = 2.5e12 s^-1 each, Ea unchanged),
so the SUMMED bridge-disappearance event rate is exactly the source's
single net rate k = 5.0e12*exp(-66000 cal/mol / RT) s^-1. Under the RMG
polymer branch's concerted-loss evidence gate each row books its heavy
co-product into its own channel-keyed feature pool -- novolac_lossC6H6O
(cumulative chain-mass defect 94.111 g/mol per event) and
novolac_lossC7H8O (108.138 g/mol per event) -- instead of leaking it as an
ordinary gas-phase species; both gas MWs are below the monomer MW 120.148
and pass the DP-preservation cap. The graph-natural toluene-analog ejection
(xylenol, 122.16 g/mol > monomer MW) remains gate-refused, correctly: a
single event cannot eject more than one monomer mass.

Rate and branching provenance: Petrocelli & Klein 1984, Macromolecules
17(2):161-169, DOI 10.1021/ma00132a008 -- Table II net diphenylmethane
(DPM) disappearance rate (log A = 12.7 s^-1, E* = 66.0 kcal/mol, measured
at 550/600 C), and Fig 6 measured ~1:1 benzene:toluene product ratio,
mapped to phenol:cresol via the authors' own benzene->phenol /
toluene->cresol correspondence for the hydroxylated bridge substrate.
NOT elementary; benchmark-closure surrogate only, valid ~823-873 K.

The heavy daughter graphs (C18H20O2 for the phenol row, C17H18O2 for the
cresol row) are bookkeeping-only: under the concerted-loss feature gate
they are absorbed into the {pool}_lossC6H6O / {pool}_lossC7H8O feature
pools and never realized as ordinary gas-phase species; they must never be
interpreted as mechanistic o-quinone-methide(-ethylidene) intermediate
claims.

COUPLING: these entries fire only while the committed novolac_trimer_proxy
graph remains isomorphic (strict=False) to the consuming deck's stitched
pool proxy; deck monomer/stitching revisions require revisiting this
dictionary.
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
