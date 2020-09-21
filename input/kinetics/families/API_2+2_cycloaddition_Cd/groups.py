#!/usr/bin/env python
# encoding: utf-8

name = "API_2+2_cycloaddition_Cd/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["db", "doublebond"], products=["four_ring"], ownReverse=False)

reverse = "Four_Ring_Cleavage_Cd"
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
    label = "db",
    group = "OR{db_2H, db_HNd, db_HDe, db_Nd2, db_NdDe, db_De2}",
    kinetics = None,
)

entry(
    index = 1,
    label = "doublebond",
    group = "OR{mb_CO, mb_OC, mb_CCO, mb_COC, mb_CS, mb_SC, mb_CCS, mb_CSC}",
    kinetics = None,
)

entry(
    index = 2,
    label = "db_2H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "db_2H_2H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "db_2H_monosub",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {2,S}
6    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "db_2H_HNd",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    H        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {2,S}
6    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "db_2H_HDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
5    H                u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "db_2H_disub",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    R!H u0 {2,S}
6    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "db_2H_Nd2",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    H        u0 {1,S}
4    H        u0 {1,S}
5    [Cs,O,S] u0 {2,S}
6    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "db_2H_NdDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "db_2H_De2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "db_HNd",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    R!H      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "db_HNd_monosub",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    H        u0 {2,S}
6    R!H      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "db_HNd_HNd",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    H        u0 {2,S}
6    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "db_HNd_HDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    H                u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "db_HNd_disub",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    R!H      u0 {2,S}
6    R!H      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "db_HNd_Nd2",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {2,S}
6    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "db_HNd_NdDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "db_HNd_De2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "db_HDe",
    group = "OR{db_HDe_HDe, db_HDe_disub}",
    kinetics = None,
)

entry(
    index = 20,
    label = "db_HDe_HDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "db_HDe_disub",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    R!H              u0 {2,S}
6    R!H              u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "db_HDe_Nd2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "db_HDe_NdDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "db_HDe_De2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "db_Nd2",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    R!H      u0 {2,S}
6    R!H      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "db_Nd2_Nd2",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {2,S}
6    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "db_Nd2_NdDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "db_Nd2_De2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "db_NdDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    R!H              u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "db_NdDe_NdDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "db_NdDe_De2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "db_De2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "mb_CO",
    group = 
"""
1 *3 CO  u0 {2,D}
2 *4 O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 89,
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
    index = 90,
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
    index = 91,
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
    index = 92,
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
    index = 93,
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
    index = 94,
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
    index = 95,
    label = "mb_OC",
    group = 
"""
1 *3 O2d u0 {2,D}
2 *4 CO  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "mb_OC_2H",
    group = 
"""
1 *4 CO  u0 {2,D} {3,S} {4,S}
2 *3 O2d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "mb_OC_HNd",
    group = 
"""
1 *4 CO       u0 {2,D} {3,S} {4,S}
2 *3 O2d      u0 {1,D}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 98,
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
    index = 99,
    label = "mb_OC_Nd2",
    group = 
"""
1 *4 CO       u0 {2,D} {3,S} {4,S}
2 *3 O2d      u0 {1,D}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 100,
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
    index = 101,
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
    index = 102,
    label = "mb_CCO",
    group = 
"""
1 *3 Cd  u0 {2,D}
2 *4 Cdd u0 {1,D} {3,D}
3    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "mb_CCO_2H",
    group = 
"""
1 *3 Cd  u0 {2,D} {3,S} {4,S}
2 *4 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "mb_CCO_HNd",
    group = 
"""
1 *3 Cd       u0 {2,D} {3,S} {4,S}
2 *4 Cdd      u0 {1,D} {5,D}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    O2d      u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "mb_CCO_HDe",
    group = 
"""
1 *3 Cd               u0 {2,D} {3,S} {4,S}
2 *4 Cdd              u0 {1,D} {5,D}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    O2d              u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "mb_CCO_Nd2",
    group = 
"""
1 *3 Cd       u0 {2,D} {3,S} {4,S}
2 *4 Cdd      u0 {1,D} {5,D}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    O2d      u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "mb_CCO_NdDe",
    group = 
"""
1 *3 Cd               u0 {2,D} {3,S} {4,S}
2 *4 Cdd              u0 {1,D} {5,D}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    O2d              u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "mb_CCO_De2",
    group = 
"""
1 *3 Cd               u0 {2,D} {3,S} {4,S}
2 *4 Cdd              u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    O2d              u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "mb_COC",
    group = 
"""
1 *3 Cdd u0 {2,D} {3,D}
2 *4 Cd  u0 {1,D}
3    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "mb_COC_2H",
    group = 
"""
1 *3 Cdd u0 {2,D} {5,D}
2 *4 Cd  u0 {1,D} {3,S} {4,S}
3    H   u0 {2,S}
4    H   u0 {2,S}
5    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "mb_COC_HNd",
    group = 
"""
1 *3 Cdd      u0 {2,D} {5,D}
2 *4 Cd       u0 {1,D} {3,S} {4,S}
3    H        u0 {2,S}
4    [Cs,O,S] u0 {2,S}
5    O2d      u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "mb_COC_HDe",
    group = 
"""
1 *3 Cdd              u0 {2,D} {5,D}
2 *4 Cd               u0 {1,D} {3,S} {4,S}
3    H                u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    O2d              u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "mb_COC_Nd2",
    group = 
"""
1 *3 Cdd      u0 {2,D} {5,D}
2 *4 Cd       u0 {1,D} {3,S} {4,S}
3    [Cs,O,S] u0 {2,S}
4    [Cs,O,S] u0 {2,S}
5    O2d      u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "mb_COC_NdDe",
    group = 
"""
1 *3 Cdd              u0 {2,D} {5,D}
2 *4 Cd               u0 {1,D} {3,S} {4,S}
3    [Cs,O,S]         u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    O2d              u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "mb_COC_De2",
    group = 
"""
1 *3 Cdd              u0 {2,D} {5,D}
2 *4 Cd               u0 {1,D} {3,S} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    O2d              u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "mb_CS",
    group = 
"""
1 *3 CS  u0 {2,D}
2 *4 S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 117,
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
    index = 118,
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
    index = 119,
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
    index = 120,
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
    index = 121,
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
    index = 122,
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
    index = 123,
    label = "mb_SC",
    group = 
"""
1 *3 S2d u0 {2,D}
2 *4 CS  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 124,
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
    index = 125,
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
    index = 126,
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
    index = 127,
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
    index = 128,
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
    index = 129,
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

entry(
    index = 130,
    label = "mb_CCS",
    group = 
"""
1 *3 Cd  u0 {2,D}
2 *4 Cdd u0 {1,D} {3,D}
3    S2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "mb_CCS_2H",
    group = 
"""
1 *3 Cd  u0 {2,D} {3,S} {4,S}
2 *4 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "mb_CCS_HNd",
    group = 
"""
1 *3 Cd       u0 {2,D} {3,S} {4,S}
2 *4 Cdd      u0 {1,D} {5,D}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    S2d      u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "mb_CCS_HDe",
    group = 
"""
1 *3 Cd               u0 {2,D} {3,S} {4,S}
2 *4 Cdd              u0 {1,D} {5,D}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    S2d              u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "mb_CCS_Nd2",
    group = 
"""
1 *3 Cd       u0 {2,D} {3,S} {4,S}
2 *4 Cdd      u0 {1,D} {5,D}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    S2d      u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "mb_CCS_NdDe",
    group = 
"""
1 *3 Cd               u0 {2,D} {3,S} {4,S}
2 *4 Cdd              u0 {1,D} {5,D}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    S2d              u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "mb_CCS_De2",
    group = 
"""
1 *3 Cd               u0 {2,D} {3,S} {4,S}
2 *4 Cdd              u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    S2d              u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "mb_CSC",
    group = 
"""
1 *3 Cdd u0 {2,D} {3,D}
2 *4 Cd  u0 {1,D}
3    S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "mb_CSC_2H",
    group = 
"""
1 *3 Cdd u0 {2,D} {5,D}
2 *4 Cd  u0 {1,D} {3,S} {4,S}
3    H   u0 {2,S}
4    H   u0 {2,S}
5    S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "mb_CSC_HNd",
    group = 
"""
1 *3 Cdd      u0 {2,D} {5,D}
2 *4 Cd       u0 {1,D} {3,S} {4,S}
3    H        u0 {2,S}
4    [Cs,O,S] u0 {2,S}
5    S2d      u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "mb_CSC_HDe",
    group = 
"""
1 *3 Cdd              u0 {2,D} {5,D}
2 *4 Cd               u0 {1,D} {3,S} {4,S}
3    H                u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    S2d              u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "mb_CSC_Nd2",
    group = 
"""
1 *3 Cdd      u0 {2,D} {5,D}
2 *4 Cd       u0 {1,D} {3,S} {4,S}
3    [Cs,O,S] u0 {2,S}
4    [Cs,O,S] u0 {2,S}
5    S2d      u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "mb_CSC_NdDe",
    group = 
"""
1 *3 Cdd              u0 {2,D} {5,D}
2 *4 Cd               u0 {1,D} {3,S} {4,S}
3    [Cs,O,S]         u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    S2d              u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "mb_CSC_De2",
    group = 
"""
1 *3 Cdd              u0 {2,D} {5,D}
2 *4 Cd               u0 {1,D} {3,S} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    S2d              u0 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: db
    L2: db_2H
        L3: db_2H_2H
        L3: db_2H_monosub
            L4: db_2H_HNd
            L4: db_2H_HDe
        L3: db_2H_disub
            L4: db_2H_Nd2
            L4: db_2H_NdDe
            L4: db_2H_De2
    L2: db_HNd
        L3: db_HNd_monosub
            L4: db_HNd_HNd
            L4: db_HNd_HDe
        L3: db_HNd_disub
            L4: db_HNd_Nd2
            L4: db_HNd_NdDe
            L4: db_HNd_De2
    L2: db_HDe
        L3: db_HDe_HDe
        L3: db_HDe_disub
            L4: db_HDe_Nd2
            L4: db_HDe_NdDe
            L4: db_HDe_De2
    L2: db_Nd2
        L3: db_Nd2_Nd2
        L3: db_Nd2_NdDe
        L3: db_Nd2_De2
    L2: db_NdDe
        L3: db_NdDe_NdDe
        L3: db_NdDe_De2
    L2: db_De2
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
    L2: mb_CCS
        L3: mb_CCS_2H
        L3: mb_CCS_HNd
        L3: mb_CCS_HDe
        L3: mb_CCS_Nd2
        L3: mb_CCS_NdDe
        L3: mb_CCS_De2
    L2: mb_CSC
        L3: mb_CSC_2H
        L3: mb_CSC_HNd
        L3: mb_CSC_HDe
        L3: mb_CSC_Nd2
        L3: mb_CSC_NdDe
        L3: mb_CSC_De2
"""
)

forbidden(
    label = "benzene_db",
    group = 
"""
1 *1 Cd u0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S}
5    Cd ux {4,S} {6,D}
6    Cd ux {1,S} {5,D}
""",
    shortDesc = u"""Benzene doublebond *1 *2""",
    longDesc = 
u"""
Banning the doublebond within Benzene from reacting in 2+2 cycloaddition.
""",
)

forbidden(
    label = "benzene_doublebond",
    group = 
"""
1 *3 Cd u0 {2,D} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S}
5    Cd ux {4,S} {6,D}
6    Cd ux {1,S} {5,D}
""",
    shortDesc = u"""Benzene doublebond *3 *4""",
    longDesc = 
u"""
Banning the doublebond within Benzene from reacting in 2+2 cycloaddition.
""",
)

