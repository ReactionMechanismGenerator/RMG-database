#!/usr/bin/env python
# encoding: utf-8

name = "Quarternary Ammonium Nucleophilic Substitution - Demethylation"
shortDesc = u""
longDesc = u"""
This family describes reactions on a singlet PES of the sort:

R-CH2-NR2-CH3 + OH -> R-CH2-NR2 + CH3-OH 

OH attacks methyl group on QA , the methyl is eliminated as methanol.

atom labeling:
*1 - C the carbon on methyl
*2 - N adjacent to C *1
*3 - O from the nucleophile
"""

template(reactants=["R-CH2-NR2-CH3","OH"], products=["R-CH2-NR2", "CH3-OH"], ownReverse=False)

reversible = True

reactantNum = 2

productNum = 2

allowChargedSpecies = True


recipe(actions=[
    ['FORM_BOND', '*1', 1, '*3'],
    ['BREAK_BOND', '*1', 1, '*3'],
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
2    H uo p0 c0 {1,s}
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

group(
    index = 4,
    label="C6H5-CH2-(N+)(CH3)3)", #TMBA
    group=
"""
1 *2 N u0 p0 c+1 {2,S} {7,S} {8,S} {9,S}
2 *1 C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3    C u0 p0 c0 {2,S} {4,S} {12,D}
4    C u0 p0 c0 {3,S} {5,S} {13,D}
5    C u0 p0 c0 {4,S} {6,S} {14,D}
6    C u0 p0 c0 {5,S} {7,S} {15,D}
7    C u0 p0 c0 {1,S} {6,S} {16,D}
8    C u0 p0 c0 {1,S} {17,H} {18,H} {19,H}
9    C u0 p0 c0 {1,S} {20,H} {21,H} {22,H}
10   C u0 p0 c0 {2,S} {23,H} {24,H} {25,H}
11   C u0 p0 c0 {2,S} {26,H} {27,H} {28,H}
""",
    kinetics=None,
)

group(
    index = 5,
    label="C6H5-CH2-(N+)(CH2CH3)3", #TEBA
    group=
"""
1 *2 N u0 p0 c+1 {2,S} {8,S} {10,S} {12,S}
2 *1 C u0 p0 c0 {1,S} {3,S}
3    C u0 p0 c0 {2,S} {4,S} {7,S}
4    C u0 p0 c0 {3,S} {5,S}
5    C u0 p0 c0 {4,S} {6,S}
6    C u0 p0 c0 {5,S} {7,S}
7    C u0 p0 c0 {3,S} {6,S}
8    C u0 p0 c0 {1,S} {9,S}
9    C u0 p0 c0 {8,S}
10   C u0 p0 c0 {1,S} {11,S}
11   C u0 p0 c0 {10,S}
12   C u0 p0 c0 {1,S} {13,S}
13   C u0 p0 c0 {12,S}
""",
    kinetics=None,
)

tree(
"""
L1: R-CH2-NR2-CH3
    L2: C6H5-CH2-(N+)(CH3)3)
    L2: C6H5-CH2-(N+)(CH2CH3)3
"""
)
