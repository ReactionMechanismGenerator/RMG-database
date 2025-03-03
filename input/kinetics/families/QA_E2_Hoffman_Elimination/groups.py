#!/usr/bin/env python
# encoding: utf-8

name = "Quarternary Ammonium Hofmann elimination E2"
shortDesc = u""
longDesc = u"""
This family describes reactions on a singlet PES of the sort:

R-CHR-CR2-NR3 + OH -> CR2=CR2 + NR3 + H2O

OH attacks a proton on the second carbon next to QA ,  QA group and water are eliminated as NR3 and H2O.

atom labeling:
*1 - C the carbon connected to proton H 2*
*2 - H the eliminated proton connected to 1*
*3 - C adjacent to C *1 
*4 - N quarternary ammonium N connected to C 2*
*5 - O on the OH
"""

template(reactants=["R-CHR-CR2-NR3","OH"], products=["CR2=CR2", "NR3","H2O"], ownReverse=False)

reversible = True

reactantNum = 2

productNum = 3

allowChargedSpecies = True


recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*5'],
    ['LOSE_PAIR', '*5', '1'],
    ['GAIN_PAIR', '*4', '1'],
    ['CHANGE_BOND', '*1', 1, '*3'],
])

entry(
    index = 0,
    label="R-CHR-CR2-NR3",
    group=
"""
1 *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
4 *4 N u0 p0 c+1 {3,S} {9,S} {10,S} {11,S}
5    R u0 p0 c0 {1,S}
6    R u0 p0 c0 {1,S}
7    R u0 p0 c0 {3,S}
8    R u0 p0 c0 {3,S}
9    R u0 p0 c0 {4,S}
10   R u0 p0 c0 {4,S}
11   R u0 p0 c0 {4,S}
""",
    kinetics=None,
)

entry(
    index = 1,
    label = "OH",
    group =
"""
1 *5 O u0 p3 c-1 {2,S} 
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "CR2=CR2",
    group =
"""
1 *1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u0 p0 c0 {1,D} {3,S} {4,S}
3    R u0 p0 c0 {2,S}
4    R u0 p0 c0 {2,S}
5    R u0 p0 c0 {1,S}
6    R u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "H2O",
    group =
"""
1 *5 O u0 p2 c0 {2,S} {3,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "NR3",
    group =
"""
1 *4 N u0 p1 c0 {2,S} {3,S} {4,S}
2    R u0 p0 c0 {1,S}
3    R u0 p0 c0 {1,S}
4    R u0 p0 c0 {1,S}
""",
    kinetics = None,
)



