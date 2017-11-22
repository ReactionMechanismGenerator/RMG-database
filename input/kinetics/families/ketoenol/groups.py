#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/groups"
shortDesc = u""
longDesc = u"""
Sulfur was added to this family, and is treated the same as oxygen.
Ideally we would like to branch this into a new family "R=RSR <=> RRR=S"
once relevant kinetic data is available
"""

template(reactants=["R_ROSR"], products=["keton"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*4', 1, '*1'],
])

boundaryAtoms = ["*2", "*3"]

entry(
        index = 19,
        label = 'R1_doublebond',
        group = 
"""
1 *1 R!H u0
""",
    kinetics = None,
)

entry(
        index = 20,
        label = 'R2_doublebond',
        group = 
"""
1 *2 R!H u0
""",
    kinetics = None,
)

entry( 
        index = 21,
        label = 'R_O',
        group = 
"""
1 *4 R u0 
""",
    kinetics = None,
        )


entry(
    index = 500,
    label = "R_ROSR",
    group =
"""
1 *1 R!H     u0 {2,D}
2 *2 R!H     u0 {1,D} {3,S}
3 *3 [O,S2s] u0 {2,S} {4,S}
4 *4 R       u0 {3,S}
""",
    kinetics = None,
)


entry(
    index = 1,
    label = "R_ROR",
    group = 
"""
1 *1 R!H u0 {2,D}
2 *2 R!H u0 {1,D} {3,S}
3 *3 O   u0 {2,S} {4,S}
4 *4 R   u0 {3,S}
""",
    kinetics = None,
)


entry(
    index = 501,
    label = "R_RSR",
    group = 
"""
1 *1 R!H u0 {2,D}
2 *2 R!H u0 {1,D} {3,S}
3 *3 S2s u0 p2 c0 {2,S} {4,S}
4 *4 R   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "R_O_H",
    group = 
"""
1 *4 H u0
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R_O_R",
    group = 
"""
1 *4 R!H u0
""",
    kinetics = None,
    nodalDistance=10,
)

entry(
    index = 34,
    label = "R_O_C",
    group = 
"""
1 *4 C u0
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "R1_doublebond_CH2",
    group = 
"""
1 *1 C u0 {2,S} {3,S}
2    H u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "R1_doublebond_CHR",
    group = 
"""
1 *1 C   u0 {2,S} {3,S}
2    R!H u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R1_doublebond_S",
    group = 
"""
1 *1 S u0 
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "R1_doublebond_CHCH3",
    group = 
"""
1 *1 C u0 {2,S} {3,S}
2    C u0 {1,S} {4,S} {5,S} {6,S}
3    H u0 {1,S}
4    H u0 {2,S}
5    H u0 {2,S}
6    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "R2_doublebond_Cs",
    group = 
"""
1 *2 C u0 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "R2_doublebond_H",
    group = 
"""
1 *2 C u0 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "R2_doublebond_CH3",
    group = 
"""
1 *2 C u0 {2,S} 
2    Cs u0 {1,S} {3,S} {4,S} {5,S}
3    H u0 {2,S}
4    H u0 {2,S}
5    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "R2_doublebond_CsC",
    group = 
"""
1 *2 C u0 {2,S}
2    Cs u0 {1,S} {3,S}
3    C u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "R2_doublebond_CH2CH3",
    group = 
"""
1 *2 C u0 {2,S}
2    Cs u0 {1,S} {3,S} {4,S} {5,S}
3    Cs u0 {2,S} {6,S} {7,S} {8,S}
4    H u0 {2,S}
5    H u0 {2,S}
6    H u0 {3,S}
7    H u0 {3,S}
8    H u0 {3,S}
""",
    kinetics = None,
)

tree(
"""
L1: R_ROSR
    L2: R_ROR
    L2: R_RSR
L1: R1_doublebond
    L2: R1_doublebond_CHR
        L3: R1_doublebond_CHCH3
    L2: R1_doublebond_S
    L2: R1_doublebond_CH2
L1: R2_doublebond
    L2: R2_doublebond_Cs
        L3: R2_doublebond_CH3
        L3: R2_doublebond_CsC
            L4: R2_doublebond_CH2CH3
    L2: R2_doublebond_H
L1: R_O
    L2: R_O_H
    L2: R_O_R
        L3: R_O_C
"""
)

