#!/usr/bin/env python
# encoding: utf-8

name = "novolac_net_VE_surrogate"
shortDesc = u"Net first-order surrogate for novolac methylene-bridge cresol-class volatile release (benchmark closure, 823-873 K)."
longDesc = u"""
Dedicated single-channel NET-SURROGATE library for the novolac (phenol-
formaldehyde, ortho-cresol repeat unit) polymer-pool benchmark deck. It is
NOT a reaction family and NOT part of any recommended set: load it explicitly
via reactionLibraries in a deck that declares the matching novolac polymer
pool (monomer C8H8O, monomer MW 120.148 g/mol; stitched baseline trimer proxy
C24H26O3, SMILES Cc1cc(O)cc(Cc2c(O)cc(C)cc2Cc2c(C)cc(C)cc2O)c1).

The single row is the round-88 "carbon-volatile net-surrogate" channel:
one cresol-class aromatic volatile released per methylene-bridge scission
event, collapsed to o-cresol (C7H8O, MW 108.14), with the element-balanced
heavy co-product an o-quinone-methide-terminated dimer (C17H18O2). Under the
RMG polymer branch's concerted-loss evidence gate this row books the heavy
product into the channel-keyed feature pool novolac_lossC7H8O (cumulative
chain-mass defect 108.138 g/mol per event) instead of leaking it as an
ordinary gas-phase species; MW(o-cresol) = 108.14 < monomer MW 120.148
passes the DP-preservation cap. The graph-natural toluene-analog ejection
(xylenol, 122.16 g/mol > monomer MW) is gate-refused, correctly: a single
event cannot eject more than one monomer mass.

Rate provenance: Petrocelli & Klein 1984, Macromolecules 17(2):161-169,
DOI 10.1021/ma00132a008 -- Table II net diphenylmethane (DPM) disappearance
rate (log A = 12.7 s^-1, E* = 66.0 kcal/mol, measured at 550/600 C), with
Fig 6 ~1:1 benzene:toluene branching. NOT elementary; benchmark-closure
surrogate only, valid ~823-873 K.

The C17H18O2 daughter graph is bookkeeping-only: under the concerted-loss
feature gate it is absorbed into the {pool}_lossC7H8O feature pool and never
realized as an ordinary gas-phase species; it must never be interpreted as a
mechanistic o-quinone-methide intermediate claim.

COUPLING: this entry fires only while the committed novolac_trimer_proxy
graph remains isomorphic (strict=False) to the consuming deck's stitched
pool proxy; deck monomer/stitching revisions require revisiting this
dictionary.
"""

entry(
    index = 1,
    label = "novolac_trimer_proxy => C17H18O2_oQM_daughter + o_cresol",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.0e12, 's^-1'),
        n = 0,
        Ea = (66000, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (873, 'K'),
    ),
    shortDesc = u"Net novolac bridge-scission cresol-release surrogate (Petrocelli & Klein 1984 Table II DPM rate)",
    longDesc = u"""
    Net first-order surrogate for novolac methylene-bridge volatile release:
    one cresol-class aromatic volatile per bridge-scission event;
    cresol/xylenol product isomers collapsed to o-cresol at MW 108.14; total
    bridge-disappearance rate = k from Petrocelli & Klein 1984 Table II
    (diphenylmethane analog, log A = 12.7 s^-1, E* = 66.0 kcal/mol, measured
    550/600 C). NOT elementary (E* well below ~85 kcal/mol homolysis BDE);
    valid only as benchmark closure over the source condition envelope.

    Caveats: (1) unsubstituted-analog transfer -- the rate is the net
    disappearance rate of diphenylmethane (no OH, no ring methyls), applied
    to the methylated/hydroxylated novolac bridge substrate; ring
    substituents are expected to perturb both A and E* by amounts the source
    does not quantify. (2) 2-temperature fit -- A and E* derive from
    measurements at only two temperatures (550 and 600 C, 823/873 K), so the
    Arrhenius extrapolation outside 823-873 K is unconstrained.

    Product shape: the heavy co-product C17H18O2 is the trimer proxy after
    benzene-analog loss of one terminal ring (ring + its ring-methyl + OH,
    H-capped), with the bridge CH2 retained on the daughter as an exocyclic
    methylene (o-quinone-methide terminus); SMILES
    C=C1C(=O)C=C(C)C=C1Cc1c(C)cc(C)cc1O. Element-balanced against the proxy
    (C24H26O3 - C7H8O = C17H18O2) so the polymer-branch concerted-loss
    evidence gate books it as the novolac_lossC7H8O feature daughter
    (defect +108.138 g/mol) rather than an ordinary gas species.
    Irreversible (=>): re-addition of an ejected volatile across the
    melt/gas reference-state boundary is not defensible for a net surrogate.
    Provenance class: Lumped (net measured rate, model-compound analog).
    Uncertainty factor: x10.
    """,
)
