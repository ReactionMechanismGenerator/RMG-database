#!/usr/bin/env python
# encoding: utf-8

name = "oxidation_of_phenols/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-oxidation of phenolic compounds:
HOC1=CC=CC=C1 <=> OC1=CC=CC=C1 + [H]
atom labels:
H[1*]_O[*2]_C1=CC=CC=C1 <=> [O][*2]_C1=CC=CC=C1 + H[*1]
"""

template(reactants=["phenol",], products=["r_phenol", "r_H"], ownReverse=False)

reverse = "Reduction_of_radical_phenol"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['GAIN_RADICAL', '*2','1'],
    ['GAIN_RADICAL', '*1','1'],

])

entry(
    index=0,
    label="phenol",
    group=
"""
1 *2 O u0 p2 c0 {2,S} {8,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {4,S} 
4    C u0 p0 c0 {3,S} {5,D} 
5    C u0 p0 c0 {4,D} {6,S} 
6    C u0 p0 c0 {5,S} {7,D} 
7    C u0 p0 c0 {2,S} {6,D} 
8 *1 H u0 p0 c0 {1,S}

""",
    kinetics=None,
)


entry(
    index=1,
    label="Epinephrine",
    group=
"""
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  N u0 p1 c0 {1,S} {3,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {20,S}
5  O u0 p2 c0 {4,S} {21,S}
6  C u0 p0 c0 {4,S} {7,S} {13,D}
7  C u0 p0 c0 {6,S} {8,D} {22,S}
8  C u0 p0 c0 {7,D} {9,S} {23,S}
9  C u0 p0 c0 {8,S} {10,S} {11,D}
10 O u0 p2 c0 {9,S} {24,S}
11 C u0 p0 c0 {9,D} {12,S} {13,S}
12 *2 O u0 p2 c0 {11,S} {25,S}
13 C u0 p0 c0 {6,D} {11,S} {26,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {10,S}
25 *1 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {13,S}


""",
    kinetics=None,
)


tree(
"""
L1: phenol
  L2: Epinephrine
"""
)
