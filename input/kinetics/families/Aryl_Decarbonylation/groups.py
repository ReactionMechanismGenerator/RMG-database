#!/usr/bin/env python
# encoding: utf-8

name = "Aryl_Decarbonylation/groups"
shortDesc = u""
longDesc = u"""
Decarbonylation (CO extrusion with ring contraction) of aryloxy-type radicals:
a cyclohexadienonyl radical -- the reactive keto resonance form of a phenoxy-type
radical -- contracts to a cyclopentadienyl-type radical while expelling CO, e.g.

    phenoxy (C6H5O.) <=> cyclopentadienyl (C5H5.) + CO

This is the dominant high-temperature CO-release channel of phenolic pyrolysis
and the primary source of the cyclopentadienyl radicals that seed PAH/char
growth (phenolic-polymer phase 6; DR2 items 5-6). No existing family performs a
six-to-five ring contraction with CO loss: R_Addition_COm (reverse) only breaks
the single acyl R-C(=O) bond and CO_Disproportionation is an abstraction.

The template is written on the LOCALIZED keto (cyclohexadienon-2-yl) resonance
form, not the aromatic Ar-O. form: RMG marks the keto resonance structures of
aryloxy radicals reactive=True (verified empirically on the polymer branch,
2026-07-22: Species('[O]c1ccccc1') carries O=C1[CH]C=CC=C1 with reactive=True),
so the family fires through them in ordinary reaction generation without any
aromatic-bond machinery.

The CO product is emitted as the neutral singlet-carbene structure (:C=O, C2d
atom type, same device as Cyclopentadiene_scission's carbene products); RMG's
resonance machinery relates it to the canonical [C-]#[O+] representation.

Atom labeling:
*1 - carbonyl carbon (departs as CO)
*2 - carbonyl oxygen
*3 - radical-bearing ortho ring carbon (attacks *4 to close the 5-ring;
     retains the radical in the cyclopentadienyl product)
*4 - other ortho ring carbon

The overall transformation is multi-step at the molecular level (bicyclic
acyl-radical intermediate); the family books the net elementary-equivalent step
with effective Arrhenius parameters from the training anchors, which is the
standard treatment of this channel in combustion mechanisms.
"""

template(reactants=["Root"], products=["cyclopentadienyl", "CO"], ownReverse=False)

reverse = "Cyclopentadienyl_CO_Addition"
reversible = True

reactantNum = 1

productNum = 2

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*3'],
    ['BREAK_BOND', '*1', 1, '*4'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['GAIN_PAIR', '*1', '1'],
])

entry(
    index = 0,
    label = "Root",
    group =
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3 *3 C   u1 {1,S} {5,S}
4 *4 Cd  u0 {1,S} {7,D}
5    Cd  u0 {3,S} {6,D}
6    Cd  u0 {5,D} {7,S}
7    Cd  u0 {6,S} {4,D}
""",
    kinetics = None,
)

tree(
"""
L1: Root
"""
)
