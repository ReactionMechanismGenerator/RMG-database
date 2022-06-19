#!/usr/bin/env python
# encoding: utf-8

name = "benzen_amino_to_cyclic_aldehyde+imine/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of benzen amine groups:
C1(OH)=CC=C(C(OH)CN(H)(R2)C=C1 + H2O <=> C1(OH(H)C(H)C=C(C=O)C=C1 + CNR2 + H2O

atom labels:

C1[*7](OH)=C[*8]C=C(C[*1](O[*2]H[*3])C[*4]N[*5](H[*6])(R2)C=C1 + <=> C1[*7](OH)(H[*3])C[*8](H[*6])C=C(C[*1]=O[*2])C=C1 + C[*4]N[*5]R2 
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
    ['CHANGE_BOND', '*1', +1, '*2'],
    ['CHANGE_BOND', '*4', +1, '*5'],
    ['BREAK_BOND', '*7', 1, '*8'],
    ['BREAK_BOND', '*8', 1, '*12'],
    ['BREAK_BOND', '*12', 1, '*9'],
    ['BREAK_BOND', '*9', 1, '*10'],
    ['BREAK_BOND', '*10', 1, '*11'],
    ['BREAK_BOND', '*11', 1, '*7'],
    ['FORM_BOND', '*7', 1, '*8'],
    ['FORM_BOND', '*8', 1, '*12'],
    ['FORM_BOND', '*12', 1, '*9'],
    ['CHANGE_BOND', '*12', +1, '*9'],
    ['FORM_BOND', '*9', 1, '*10'],
    ['FORM_BOND', '*10', 1, '*11'],
    ['CHANGE_BOND', '*10', +1, '*11'],
    ['FORM_BOND', '*11', 1, '*7'],
    ['FORM_BOND', '*8', 1, '*6'], 
    ['FORM_BOND', '*7', 1, '*3'],
])

entry(
    index=0,
    label="benzen_amino",
    group=
"""
1      Cs       u0 {2,S} 
2  *5  N3s      u0 p1 {1,S} {3,S} {13,S}
3  *4  C        u0 {2,S} {4,S} {14,S} {15,S}
4  *1  C        u0 {3,S} {5,S} {6,S}
5  *2  O2s      u0 p2 {4,S} {16,S}
6  *9  Cb       u0 {4,S} {7,B} {12,B}
7  *10 Cb u0 {6,B} {8,B}
8  *11 Cb u0 {7,B} {9,B}
9  *7  Cb       u0 {8,B} {10,S} {11,B}
10     O2s      u0 p2 {9,S} {17,S}
11 *8  Cb       u0 {9,B} {12,B}
12 *12 Cb u0 {6,B} {11,B}
13 *6  H        u0 {2,S}
14     H        u0 {3,S}
15     H        u0 {3,S}
16 *3  H        u0 {5,S}
17     H        u0 {10,S}
""",
    kinetics=None,
)

#entry(
#    index=1,
#    label="adrenaline",
#    group=
#"""
#1  *5  N u0 p1 c0 {2,S} {13,S} {14,S}
#2  *4  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
#3  *1  C u0 p0 c0 {2,S} {4,S} {12,S} {17,S}
#4  *9  C u0 p0 c0 {3,S} {5,B} {9,B}
#5  *12 C u0 p0 c0 {4,B} {6,B} {18,S}
#6  *8 C u0 p0 c0 {5,B} {7,B} {11,S}
#7  *7  C u0 p0 c0 {6,B} {8,B} {10,S}
#8  *11 C u0 p0 c0 {7,B} {9,B} {19,S}
#9  *10 C u0 p0 c0 {4,B} {8,B} {20,S}
#10     O u0 p2 c0 {7,S} {21,S}
#11     O u0 p2 c0 {6,S} {22,S}
#12 *2  O u0 p2 c0 {3,S} {23,S}
#13     H u0 p0 c0 {1,S}
#14 *6  H u0 p0 c0 {1,S}
#15     H u0 p0 c0 {2,S}
#16     H u0 p0 c0 {2,S}
#17     H u0 p0 c0 {3,S}
#18     H u0 p0 c0 {5,S}
#19     H u0 p0 c0 {8,S}
#20     H u0 p0 c0 {9,S}
#21     H u0 p0 c0 {10,S}
#22     H u0 p0 c0 {11,S}
#23 *3  H u0 p0 c0 {12,S}
#
#""",
#    kinetics=None,
#)

tree(
"""
L1: benzen_amino

"""
)
