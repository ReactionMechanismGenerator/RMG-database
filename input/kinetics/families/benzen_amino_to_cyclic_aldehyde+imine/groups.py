#!/usr/bin/env python
# encoding: utf-8

name = "benzen_amino_to_cyclic_aldehyde+imine/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of benzen amine groups:
C1(OH)=CC=C(C(OH)CN(H)(R2)C=C1 + H2O <=> C1(OH(H)C(H)C=C(C=O)C=C1 + CNR2 + H2O

atom labels:

C1[*7](OH)=C[*8]C=C(C[*1](O[*2]H[*3])C[*4]N[*5](H[*6])(R2)C=C1 + <=> C1[*7](OH(H[*3])C[*8](H[*6])C=C(C[*1]=O[*2])C=C1 + C[*4]N[*5]R2 
ignoring H2O on both sides for simplicity
(training reactions do include H2O in the calculation, rates divided by 18 ml/mol)
"""

template(reactants=["benzen_amino"], products=["cyclic_aldehyde", "imine"], ownReverse=False)

reverse = "aldehyde+imine_to_amino"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*3'],
    ['BREAK_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*5', 1, '*6'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*4', 1, '*5'],
    ['CHANGE_BOND', '*7', -1, '*8'],
    ['FORM_BOND', '*8', 1, '*6'], 
    ['FORM_BOND', '*7', 1, '*3'],  
])

entry(
    index=0,
    label="benzen_amino",
    group=
"""
1     R ux px cx {2,S} 
2  *5 N u0 p1 c0 {1,S} {3,S} {13,S}
3  *4 C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {16,S}
5  *2 O u0 p2 c0 {4,S} {17,S}
6     C u0 p0 c0 {4,S} {7,S} {12,D}
7     C u0 p0 c0 {6,S} {8,D} {18,S}
8     C u0 p0 c0 {7,D} {9,S} {19,S}
9  *7 C u0 p0 c0 {8,S} {10,S} {11,D}
10    O u0 p2 c0 {9,S} {20,S}
11 *8 C u0 p0 c0 {9,D} {12,S} {21,S}
12    C u0 p0 c0 {6,D} {11,S} {22,S}
13 *6 H u0 p0 c0 {2,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17 *3 H u0 p0 c0 {5,S}
18    H u0 p0 c0 {7,S}
19    H u0 p0 c0 {8,S}
20    H u0 p0 c0 {10,S}
21    H u0 p0 c0 {11,S}
22    H u0 p0 c0 {12,S}
""",
    kinetics=None,
)


tree(
"""
L1: benzen_amino

"""
)
