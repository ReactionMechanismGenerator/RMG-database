#!/usr/bin/env python
# encoding: utf-8

name = "Quarternary Ammonium Nucleophilic Substitution - SN2"
shortDesc = u""
longDesc = u"""
This family describes reactions on a singlet PES of the sort:

RCH2(N+)R3 + OH- -> RCH2OH + NR3 

OH attacks a carbon next to QA , where a QA group and are eliminated as NR3.

atom labeling:
*1 - C the carbon 
*2 - N adjacent to C *1
*3 - O 
"""

template(reactants=["RCH2(N+)R3","(O-)H"], products=["RCH2OH", "NR3"], ownReverse=False)

reversible = True

reactantNum = 2

productNum = 2

allowChargedSpecies = True


recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['LOSE_PAIR', '*3', '1'],
    ['GAIN_PAIR', '*2', '1'],
   
])

entry(
    index = 0,
    label="RCH2(N+)R3",
    group=
"""
1 *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 *2 N u0 p0 c+1 {1,S} {3,S} {4,S} {5,S}
3    R u0 p0 c0 {2,S}
4    R u0 p0 c0 {2,S}
5    R u0 p0 c0 {2,S}
6    R u0 p0 c0 {1,S}
7    H u0 p0 c0 {1,S}
8    H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

entry(
    index = 1,
    label = "(O-)H",
    group =
"""
1 *3 O u0 p3 c-1 {2,S} 
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "RCH2OH",
    group =
"""
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 O u0 p2 c0 {1,S} {3,S} 
3    H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    R u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "NR3",
    group =
"""
1 *2 N u0 p1 c0 {2,S} {3,S} {4,S}
2    R u0 p0 c0 {1,S}
3    R u0 p0 c0 {1,S}
4    R u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label="C6H5-CH2-(N+)(CH3)3", #TMBA
    group=
"""
1 *2 N u0 p0 c+1 {2,S} {7,S} {8,S} {9,S}
2 *1 C u0 p0 c0 {1,S} {3,S} {4,B} {6,B}
3    H u0 p0 c0 {2,S}
4    C u0 p0 c0 {2,B} {5,B} {10,S}
5    C u0 p0 c0 {4,B} {6,B} {11,S}
6    C u0 p0 c0 {2,B} {5,B} {12,S}
7    C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
8    C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
9    C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
10   H u0 p0 c0 {4,S}
11   H u0 p0 c0 {5,S}
12   H u0 p0 c0 {6,S}
13   H u0 p0 c0 {7,S}
14   H u0 p0 c0 {7,S}
15   H u0 p0 c0 {7,S}
16   H u0 p0 c0 {8,S}
17   H u0 p0 c0 {8,S}
18   H u0 p0 c0 {8,S}
19   H u0 p0 c0 {9,S}
20   H u0 p0 c0 {9,S}
21   H u0 p0 c0 {9,S}
""",
    kinetics=None,
)

entry(
    index = 5,
    label="C6H5-CH2-(N+)R2-CH3", 
    group=
"""
1 *2 N u0 p0 c+1 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    R u0 p0 c0 {1,S}
4    R u0 p0 c0 {1,S}
5    C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {5,S}
10   H u0 p0 c0 {5,S}
11   H u0 p0 c0 {5,S}
12   C u0 p0 c0 {13,B} {14,B} {15,S}
13   C u0 p0 c0 {12,B} {16,B} {17,S}
14   C u0 p0 c0 {12,B} {18,B} {19,S}
15   H u0 p0 c0 {12,S}
16   C u0 p0 c0 {13,B} {20,B} {21,S}
17   H u0 p0 c0 {13,S}
18   C u0 p0 c0 {14,B} {22,B} {23,S}
19   H u0 p0 c0 {14,S}
20   C u0 p0 c0 {16,B} {22,B} {24,S}
21   H u0 p0 c0 {16,S}
22   C u0 p0 c0 {18,B} {20,B} {25,S}
23   H u0 p0 c0 {18,S}
24   H u0 p0 c0 {20,S}
25   H u0 p0 c0 {22,S}
""",
    kinetics=None,
)

entry(
    index = 6,
    label="R-CH2-(N+)R2-CH3", 
    group=
"""
1 *2 N  u0 p0 c+1 {2,S} {5,S} {6,S} {7,S}
2 *1 C  u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3    R  u0 p0 c0 {2,S}
4    H  u0 p0 c0 {2,S}
5    R  u0 p0 c0 {1,S}
6    R  u0 p0 c0 {1,S}
7    C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
8    H  u0 p0 c0 {2,S}
9    H  u0 p0 c0 {7,S}
10   H  u0 p0 c0 {7,S}
11   H  u0 p0 c0 {7,S}
""",
    kinetics=None,
)

entry(
    index = 7,
    label="C6H5-CH2-(N+)(CH2CH3)3", 
    group=
"""
1 *2 N  u0 p0 c+1 {2,S} {7,S} {11,S} {15,S}
2 *1 C  u0 p0 c0 {1,S} {3,S} {4,B} {6,B}
3    C  u0 p0 c0 {2,S} {8,B} {9,B}
4    C  u0 p0 c0 {2,B} {5,B} {10,S}
5    C  u0 p0 c0 {4,B} {6,B} {12,S}
6    C  u0 p0 c0 {2,B} {5,B} {13,S}
7    C  u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
8    C  u0 p0 c0 {3,B} {9,B} {14,S}
9    C  u0 p0 c0 {3,B} {8,B} {15,S}
10   H  u0 p0 c0 {4,S}
11   C  u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
12   H  u0 p0 c0 {5,S}
13   H  u0 p0 c0 {6,S}
14   H  u0 p0 c0 {8,S}
15   C  u0 p0 c0 {1,S} {9,S} {22,S} {23,S}
16   H  u0 p0 c0 {7,S}
17   H  u0 p0 c0 {7,S}
18   C  u0 p0 c0 {7,S} {24,S} {25,S} {26,S}
19   H  u0 p0 c0 {11,S}
20   H  u0 p0 c0 {11,S}
21   H  u0 p0 c0 {11,S}
22   H  u0 p0 c0 {15,S}
23   H  u0 p0 c0 {15,S}
24   C  u0 p0 c0 {18,S} {27,S} {28,S} {29,S}
25   H  u0 p0 c0 {18,S}
26   H  u0 p0 c0 {18,S}
27   H  u0 p0 c0 {24,S}
28   H  u0 p0 c0 {24,S}
29   H  u0 p0 c0 {24,S}
""",
    kinetics=None,
)



tree(
"""
L1: R-CH2-(N+)R2-CH3
    L2: C6H5-CH2-(N+)R2-CH3
        L3: C6H5-CH2-(N+)(CH3)3
        L3: C6H5-CH2-(N+)(CH2CH3)3
"""
)





