#!/usr/bin/env python
# encoding: utf-8

name = "API_2+2_cycloaddition_CS/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["CS", "doublebond"], products=["four_ring"], ownReverse=False)

reverse = "Four_Ring_Cleavage_CS"

reversible = True

only_reverse = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*3', -1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 0,
    label = "CS",
    group = 
"""
1 *1 CS  u0 {2,D}
2 *2 S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "doublebond",
    group = "OR{mb_CO, mb_OC, mb_CS, mb_SC, mb_CCO, mb_COC}",
    kinetics = None,
)

entry(
    index = 2,
    label = "CS_2H",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "CS_HNd",
    group = 
"""
1 *1 CS       u0 {2,D} {3,S} {4,S}
2 *2 S2d      u0 {1,D}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "CS_HDe",
    group = 
"""
1 *1 CS               u0 {2,D} {3,S} {4,S}
2 *2 S2d              u0 {1,D}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CS_Nd2",
    group = 
"""
1 *1 CS       u0 {2,D} {3,S} {4,S}
2 *2 S2d      u0 {1,D}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "CS_NdDe",
    group = 
"""
1 *1 CS               u0 {2,D} {3,S} {4,S}
2 *2 S2d              u0 {1,D}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "CS_De2",
    group = 
"""
1 *1 CS               u0 {2,D} {3,S} {4,S}
2 *2 S2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CH2CHS",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 {1,D}
3    H   u0 {1,S}
4    C   u1 {1,S} {5,S} {6,S}
5    H   u0 {4,S}
6    H   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "mb_CO",
    group = 
"""
1 *3 CO  u0 {2,D}
2 *4 O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "mb_CO_2H",
    group = 
"""
1 *3 CO  u0 {2,D} {3,S} {4,S}
2 *4 O2d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "mb_CO_HNd",
    group = 
"""
1 *3 CO       u0 {2,D} {3,S} {4,S}
2 *4 O2d      u0 {1,D}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "mb_CO_HDe",
    group = 
"""
1 *3 CO               u0 {2,D} {3,S} {4,S}
2 *4 O2d              u0 {1,D}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "mb_CO_Nd2",
    group = 
"""
1 *3 CO       u0 {2,D} {3,S} {4,S}
2 *4 O2d      u0 {1,D}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "mb_CO_NdDe",
    group = 
"""
1 *3 CO               u0 {2,D} {3,S} {4,S}
2 *4 O2d              u0 {1,D}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "mb_CO_De2",
    group = 
"""
1 *3 CO               u0 {2,D} {3,S} {4,S}
2 *4 O2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "mb_OC",
    group = 
"""
1 *3 O2d u0 {2,D}
2 *4 CO  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "mb_OC_2H",
    group = 
"""
1 *3 O2d u0 {2,D}
2 *4 CO  u0 {1,D} {3,S} {4,S}
3    H   u0 {2,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "mb_OC_HNd",
    group = 
"""
1 *3 O2d      u0 {2,D}
2 *4 CO       u0 {1,D} {3,S} {4,S}
3    H        u0 {2,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "mb_OC_HDe",
    group = 
"""
1 *3 O2d              u0 {2,D}
2 *4 CO               u0 {1,D} {3,S} {4,S}
3    H                u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "mb_OC_Nd2",
    group = 
"""
1 *3 O2d      u0 {2,D}
2 *4 CO       u0 {1,D} {3,S} {4,S}
3    [Cs,O,S] u0 {2,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "mb_OC_NdDe",
    group = 
"""
1 *3 O2d              u0 {2,D}
2 *4 CO               u0 {1,D} {3,S} {4,S}
3    [Cs,O,S]         u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "mb_OC_De2",
    group = 
"""
1 *3 O2d              u0 {2,D}
2 *4 CO               u0 {1,D} {3,S} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "mb_CCO",
    group = 
"""
1 *3 Cd        u0 {2,D}
2 *4 Cdd       u0 {1,D} {3,D}
3    [O2d,S2d] u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "mb_CCO_2H",
    group = 
"""
1 *3 Cd        u0 {2,D} {3,S} {4,S}
2 *4 Cdd       u0 {1,D} {5,D}
3    H         u0 {1,S}
4    H         u0 {1,S}
5    [O2d,S2d] u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "mb_CCO_HNd",
    group = 
"""
1 *3 Cd        u0 {2,D} {3,S} {4,S}
2 *4 Cdd       u0 {1,D} {5,D}
3    H         u0 {1,S}
4    [Cs,O,S]  u0 {1,S}
5    [O2d,S2d] u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "mb_CCO_HDe",
    group = 
"""
1 *3 Cd               u0 {2,D} {3,S} {4,S}
2 *4 Cdd              u0 {1,D} {5,D}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [O2d,S2d]        u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "mb_CCO_Nd2",
    group = 
"""
1 *3 Cd        u0 {2,D} {3,S} {4,S}
2 *4 Cdd       u0 {1,D} {5,D}
3    [Cs,O,S]  u0 {1,S}
4    [Cs,O,S]  u0 {1,S}
5    [O2d,S2d] u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "mb_CCO_NdDe",
    group = 
"""
1 *3 Cd               u0 {2,D} {3,S} {4,S}
2 *4 Cdd              u0 {1,D} {5,D}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [O2d,S2d]        u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "mb_CCO_De2",
    group = 
"""
1 *3 Cd               u0 {2,D} {3,S} {4,S}
2 *4 Cdd              u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [O2d,S2d]        u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "mb_COC",
    group = 
"""
1 *3 Cdd       u0 {2,D} {3,D}
2 *4 Cd        u0 {1,D}
3    [O2d,S2d] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "mb_COC_2H",
    group = 
"""
1 *3 Cdd       u0 {2,D} {5,D}
2 *4 Cd        u0 {1,D} {3,S} {4,S}
3    H         u0 {2,S}
4    H         u0 {2,S}
5    [O2d,S2d] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "mb_COC_HNd",
    group = 
"""
1 *3 Cdd       u0 {2,D} {5,D}
2 *4 Cd        u0 {1,D} {3,S} {4,S}
3    H         u0 {2,S}
4    [Cs,O,S]  u0 {2,S}
5    [O2d,S2d] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "mb_COC_HDe",
    group = 
"""
1 *3 Cdd              u0 {2,D} {5,D}
2 *4 Cd               u0 {1,D} {3,S} {4,S}
3    H                u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [O2d,S2d]        u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "mb_COC_Nd2",
    group = 
"""
1 *3 Cdd       u0 {2,D} {5,D}
2 *4 Cd        u0 {1,D} {3,S} {4,S}
3    [Cs,O,S]  u0 {2,S}
4    [Cs,O,S]  u0 {2,S}
5    [O2d,S2d] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "mb_COC_NdDe",
    group = 
"""
1 *3 Cdd              u0 {2,D} {5,D}
2 *4 Cd               u0 {1,D} {3,S} {4,S}
3    [Cs,O,S]         u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [O2d,S2d]        u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "mb_COC_De2",
    group = 
"""
1 *3 Cdd              u0 {2,D} {5,D}
2 *4 Cd               u0 {1,D} {3,S} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [O2d,S2d]        u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "mb_CS",
    group = 
"""
1 *3 CS  u0 {2,D}
2 *4 S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "mb_CS_2H",
    group = 
"""
1 *3 CS  u0 {2,D} {3,S} {4,S}
2 *4 S2d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "mb_CS_HNd",
    group = 
"""
1 *3 CS       u0 {2,D} {3,S} {4,S}
2 *4 S2d      u0 {1,D}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "mb_CS_HDe",
    group = 
"""
1 *3 CS               u0 {2,D} {3,S} {4,S}
2 *4 S2d              u0 {1,D}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "mb_CS_Nd2",
    group = 
"""
1 *3 CS       u0 {2,D} {3,S} {4,S}
2 *4 S2d      u0 {1,D}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "mb_CS_NdDe",
    group = 
"""
1 *3 CS               u0 {2,D} {3,S} {4,S}
2 *4 S2d              u0 {1,D}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "mb_CS_De2",
    group = 
"""
1 *3 CS               u0 {2,D} {3,S} {4,S}
2 *4 S2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "mb_SC",
    group = 
"""
1 *3 S2d u0 {2,D}
2 *4 CS  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "mb_SC_2H",
    group = 
"""
1 *3 S2d u0 {2,D}
2 *4 CS  u0 {1,D} {3,S} {4,S}
3    H   u0 {2,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "mb_SC_HNd",
    group = 
"""
1 *3 S2d      u0 {2,D}
2 *4 CS       u0 {1,D} {3,S} {4,S}
3    H        u0 {2,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "mb_SC_HDe",
    group = 
"""
1 *3 S2d              u0 {2,D}
2 *4 CS               u0 {1,D} {3,S} {4,S}
3    H                u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "mb_SC_Nd2",
    group = 
"""
1 *3 S2d      u0 {2,D}
2 *4 CS       u0 {1,D} {3,S} {4,S}
3    [Cs,O,S] u0 {2,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "mb_SC_NdDe",
    group = 
"""
1 *3 S2d              u0 {2,D}
2 *4 CS               u0 {1,D} {3,S} {4,S}
3    [Cs,O,S]         u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "mb_SC_De2",
    group = 
"""
1 *3 S2d              u0 {2,D}
2 *4 CS               u0 {1,D} {3,S} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: CS
    L2: CS_2H
    L2: CS_HNd
    L2: CS_HDe
    L2: CS_Nd2
    L2: CS_NdDe
    L2: CS_De2
    L2: CH2CHS
L1: doublebond
    L2: mb_CO
        L3: mb_CO_2H
        L3: mb_CO_HNd
        L3: mb_CO_HDe
        L3: mb_CO_Nd2
        L3: mb_CO_NdDe
        L3: mb_CO_De2
    L2: mb_OC
        L3: mb_OC_2H
        L3: mb_OC_HNd
        L3: mb_OC_HDe
        L3: mb_OC_Nd2
        L3: mb_OC_NdDe
        L3: mb_OC_De2
    L2: mb_CCO
        L3: mb_CCO_2H
        L3: mb_CCO_HNd
        L3: mb_CCO_HDe
        L3: mb_CCO_Nd2
        L3: mb_CCO_NdDe
        L3: mb_CCO_De2
    L2: mb_COC
        L3: mb_COC_2H
        L3: mb_COC_HNd
        L3: mb_COC_HDe
        L3: mb_COC_Nd2
        L3: mb_COC_NdDe
        L3: mb_COC_De2
    L2: mb_CS
        L3: mb_CS_2H
        L3: mb_CS_HNd
        L3: mb_CS_HDe
        L3: mb_CS_Nd2
        L3: mb_CS_NdDe
        L3: mb_CS_De2
    L2: mb_SC
        L3: mb_SC_2H
        L3: mb_SC_HNd
        L3: mb_SC_HDe
        L3: mb_SC_Nd2
        L3: mb_SC_NdDe
        L3: mb_SC_De2
"""
)

