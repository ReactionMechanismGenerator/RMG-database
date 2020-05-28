#!/usr/bin/env python
# encoding: utf-8

name = "Fake_amine_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:
C-NH-R + [OH3+] <=> C-[NH2+]-R + H2O <=RDS=> C-[OH2+] + R-NH2 <=> C-OH + [H+] + R-NH2
overall taken as:
R1-NH-C(OOH)R2 + H2O <=> R1-NH2 + O=C-R2 + H2O2

atom labels:
R1-N(*1)H-C(*2)-[O(*3)O(*4)H(*5)]R2 + H(*6)O(*7)H <=> R1-N(*1)H-H(*5) + O(*3)=C(*2)-R2 + H(*6)O(*4)O(*7)H
"""

template(reactants=["NHCOOH", "H2O"], products=["aldehyde", "amine_product", "H2O2"], ownReverse=False)

reverse = "condensation"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['BREAK_BOND', '*6', 1, '*7'],
    ['FORM_BOND', '*1', 1, '*5'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*7', 1, '*4'],
    ['FORM_BOND', '*4', 1, '*6'],
])

entry(
    index = 0,
    label = "NHCOOH",
    group =
"""
1    R!H u0 p0 c0 {2,S}
2 *1 N   u0 p1 c0 {1,S} {3,S} {7,S}
3 *2 C   u0 p0 c0 {2,S} {4,S} {6,S}
4 *3 O   u0 p2 c0 {3,S} {5,S}
5 *4 O   u0 p2 c0 {4,S} {8,S}
6    R   u0 p0 c0 {3,S}
7    H   u0 p0 c0 {2,S}
8 *5 H   u0 p0 c0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "H2O",
    group =
"""
1 *7 O u0 p2 c0 {2,S} {3,S}
2 *6 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: NHCOOH
L1: H2O
"""
)
