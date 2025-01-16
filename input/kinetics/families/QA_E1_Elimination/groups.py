#!/usr/bin/env python
# encoding: utf-8

name = "Quarternary Ammonium E1 elimination"
shortDesc = u""
longDesc = u"""
This family describes reactions on a singlet PES of the sort:

R-CHR-CR2-NR2-CH3 + OH -> CR2=CR2 + NR2-CH3 + H2O

The QA group leaves, forming a carbocation (transition state), then a proton is removed to create a double bond

atom labeling:
*1 - N of the QA
*2 - C adjacent to N *1
*3 - C adjacent to C *2
*4 - H proton on C *2 (secondary carbon)
*5 - O of the OH
"""

template(reactants=["R-CHR-CR2-NR2-CH3","OH"], products=["CR2=CR2", "NR2-CH3","H2O"], ownReverse=False)

reversible = True

reactantNum = 2

productNum = 3

allowChargedSpecies = True


recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*4', 1, '*5'],
    ['CHANGE_BOND', '*2', 2, '*3'],
    ['LOSE_PAIR', '*3', '1'],
    ['GAIN_PAIR', '*2', '1'],
   
])

group(
    index = 0,
    label="R-CH2-NR2-CH3",
    group=
"""
1 *1 C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2 *2 N u0 p0 c+1 {1,S} {3,S} {7,S} {8,S}
3    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4    R u0 p0 c0 {3,S}
5    H u0 p0 c0 {3,S}
6    H u0 p0 c0 {3,S}
7    R u0 p0 c0 {2,S}
8    R u0 p0 c0 {2,S}
9    H u0 p0 c0 {1,S}
10   H u0 p0 c0 {1,S}
11   H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

entry(
    index = 1,
    label = "OH",
    group =
"""
1 *3 O u0 p3 c-1 {2,S} 
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "R-CH2-NR2",
    group =
"""
1 *2 N u0 p1 c0 {2,S} {3,S} {4,S} 
2    C u0 p0 c0 {1,S} {3,S} 
3    R u0 p0 c0 {1,S}
4    R u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    R u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "CH3-OH",
    group =
"""
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)


tree(
"""
L1: NNHNH2

"""
)
