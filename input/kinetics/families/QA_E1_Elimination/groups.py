#!/usr/bin/env python
# encoding: utf-8

name = "Quarternary Ammonium E1 elimination"
shortDesc = u""
longDesc = u"""
This family describes reactions on a singlet PES of the sort:

R-CHR-CR2-(N+)R2-CH3 + OH -> CR2=CR2 + NR2-CH3 + H2O

The QA group leaves, forming a carbocation (transition state), then a proton is removed to create a double bond

atom labeling:
*1 - N of the QA
*2 - C adjacent to N *1
*3 - C adjacent to C *2
*4 - H proton on C *2 (secondary carbon)
*5 - O of the OH
"""

template(reactants=["R-CHR-CR2-NR2-CH3"], products=["CR2CR2", "NR2-CH3","H2O"], ownReverse=True)

reversible = True

reactantNum = 2

productNum = 3

allowChargedSpecies = True


recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*4', 1, '*5'],
    ['LOSE_PAIR', '*5', '1'],
    ['GAIN_PAIR', '*1', '1'],
    ['CHANGE_BOND', '*2', 1, '*3'],
   
])

entry(
    index = 0,
    label="R-CHR-CR2-NR2-CH3",
    group=
"""
1 *3 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *4 H u0 p0 c0 {1,S}
3 *2 C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4 *1 N u0 p0 c+1 {3,S} {9,S} {10,S} {11,S}
5    R u0 p0 c0 {1,S}
6    R u0 p0 c0 {1,S}
7    R u0 p0 c0 {3,S}
8    R u0 p0 c0 {3,S}
9    R u0 p0 c0 {4,S}
10   R u0 p0 c0 {4,S}
11   C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
12   H u0 p0 c0 {11,S}
13   H u0 p0 c0 {11,S}
14   H u0 p0 c0 {11,S}
15 *5 O u0 p3 c-1 {16,S} 
16    H u0 p0 c0 {15,S}
""",
    kinetics=None,
)


entry(
    index = 1,
    label = "CR2CR2",
    group =
"""
1 *2 C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u0 p0 c0 {1,D} {5,S} {6,S}
3    R u0 p0 c0 {1,S}
4    R u0 p0 c0 {1,S}
5    R u0 p0 c0 {2,S}
6    R u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "NR2-CH3",
    group =
"""
1 *1 N u0 p1 c0 {2,S} {3,S} {4,S}
2    R u0 p0 c0 {1,S}
3    R u0 p0 c0 {1,S}
4    C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5    H u0 p0 c0 {4,S}
6    H u0 p0 c0 {4,S}
7    H u0 p0 c0 {4,S}

""",
    kinetics = None,
)

entry(
    index = 3,
    label = "H2O",
    group =
"""
1 *5 O u0 p2 c0 {2,S} {3,S}
2 *4 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)


tree(
"""
L1: R-CHR-CR2-NR2-CH3

"""
)
