#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_RSR/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["doublebond", "R_SR"], products=["R_singlebond_SR"], ownReverse=False)

reverse = "1,2_Elimination_RSR"

recipe(actions=[
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "doublebond",
    group = "OR{Cd_Cdd, Cdd_Cd, Cd_Cd, Od_Cd, Sd_Cd}",
    kinetics = None,
)

entry(
    index = 2,
    label = "R_SR",
    group = "OR{H_SR, R_SH}",
    kinetics = None,
)

entry(
    index = 3,
    label = "Cd_Cdd",
    group = 
"""
1 *1 Cd  u0 {2,D}
2 *2 Cdd u0 {1,D} {3,D}
3    Od  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "cco_2H",
    group = 
"""
1 *1 Cd  u0 {2,D} {4,S} {5,S}
2 *2 Cdd u0 {1,D} {3,D}
3    Od  u0 {2,D}
4    H   u0 {1,S}
5    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "cco_HNd",
    group = 
"""
1 *1 Cd       u0 {2,D} {4,S} {5,S}
2 *2 Cdd      u0 {1,D} {3,D}
3    Od       u0 {2,D}
4    H        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "cco_HDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {4,S} {5,S}
2 *2 Cdd           u0 {1,D} {3,D}
3    Od            u0 {2,D}
4    H             u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "cco_Nd2",
    group = 
"""
1 *1 Cd       u0 {2,D} {4,S} {5,S}
2 *2 Cdd      u0 {1,D} {3,D}
3    Od       u0 {2,D}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "cco_NdDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {4,S} {5,S}
2 *2 Cdd           u0 {1,D} {3,D}
3    Od            u0 {2,D}
4    [Cs,O,S]      u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "cco_De2",
    group = 
"""
1 *1 Cd            u0 {2,D} {4,S} {5,S}
2 *2 Cdd           u0 {1,D} {3,D}
3    Od            u0 {2,D}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Cdd_Cd",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D}
3    Od  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Cdd_Cd_2H",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  u0 {1,D} {4,S} {5,S}
3    Od  u0 {1,D}
4    H   u0 {2,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Cdd_Cd_HNd",
    group = 
"""
1 *1 Cdd      u0 {2,D} {3,D}
2 *2 Cd       u0 {1,D} {4,S} {5,S}
3    Od       u0 {1,D}
4    H        u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Cdd_Cd_HDe",
    group = 
"""
1 *1 Cdd           u0 {2,D} {3,D}
2 *2 Cd            u0 {1,D} {4,S} {5,S}
3    Od            u0 {1,D}
4    H             u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Cdd_Cd_Nd2",
    group = 
"""
1 *1 Cdd      u0 {2,D} {3,D}
2 *2 Cd       u0 {1,D} {4,S} {5,S}
3    Od       u0 {1,D}
4    [Cs,O,S] u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Cdd_Cd_NdDe",
    group = 
"""
1 *1 Cdd           u0 {2,D} {3,D}
2 *2 Cd            u0 {1,D} {4,S} {5,S}
3    Od            u0 {1,D}
4    [Cs,O,S]      u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Cdd_Cd_De2",
    group = 
"""
1 *1 Cdd           u0 {2,D} {3,D}
2 *2 Cd            u0 {1,D} {4,S} {5,S}
3    Od            u0 {1,D}
4    [Cd,Ct,Cb,CO] u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Cd_Cd",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Cd/unsub_Cd/unsub",
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
    index = 19,
    label = "Cd/unsub_Cd/monosub",
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
    index = 20,
    label = "Cd/H2_Cd/H/Nd",
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
    index = 21,
    label = "Cd/H2_Cd/H/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    H             u0 {1,S}
5    H             u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Cd/monosub_Cd/unsub",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Cd/H/Nd_Cd/H2",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    H        u0 {2,S}
6    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Cd/H/De_Cd/H2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    H             u0 {2,S}
6    H             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Cd/unsub_Cd/disub",
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
    index = 26,
    label = "Cd/H2_Cd/Nd2",
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
    index = 27,
    label = "Cd/H2_Cd/Cs2",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Cd/H2_Cd/Nd/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    H             u0 {1,S}
5    [Cs,O,S]      u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Cd/H2_Cd/De2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    H             u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Cd/disub_Cd/unsub",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Cd/Nd2_Cd/H2",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    H        u0 {2,S}
6    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Cd/NdDe_Cd/H2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    H             u0 {2,S}
6    H             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Cd/De2_Cd/H2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    H             u0 {2,S}
6    H             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Cd/monosub_Cd/monosub",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
5    H   u0 {2,S}
6    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Cd/H/Nd_Cd/H/Nd",
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
    index = 36,
    label = "Cd/H/Nd_Cd/H/Os",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    H        u0 {2,S}
6    O        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "Cd/H/Nd_Cd/H/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
5    H             u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Cd/H/De_Cd/H/Nd",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    H             u0 {2,S}
6    [Cs,O,S]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "Cd/H/De_Cd/H/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    H             u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "Cd/monosub_Cd/disub",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {2,S}
6    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Cd/H/Nd_Cd/Nd2",
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
    index = 42,
    label = "Cd/H/Nd_Cd/Nd/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
5    [Cs,O,S]      u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "Cd/H/Nd_Cd/De2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Cd/H/De_Cd/Nd2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O,S]      u0 {2,S}
6    [Cs,O,S]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Cd/H/De_Cd/Nd/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O,S]      u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Cd/H/De_Cd/De2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Cd/disub_Cd/monosub",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
5    H   u0 {2,S}
6    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Cd/Nd2_Cd/H/Nd",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    H        u0 {2,S}
6    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Cd/Nd2_Cd/H/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
5    H             u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Cd/De2_Cd/H/Nd",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    H             u0 {2,S}
6    [Cs,O,S]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Cd/De2_Cd/H/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    H             u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Cd/Nd/De_Cd/H/Nd",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    H             u0 {2,S}
6    [Cs,O,S]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Cd/Nd/De_Cd/H/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    H             u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Cd/disub_Cd/disub",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {2,S}
6    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Cd/Nd2_Cd/Nd2",
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
    index = 56,
    label = "Cd/Nd2_Cd/Nd/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
5    [Cs,O,S]      u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Cd/Nd2_Cd/De2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Cd/Nd/De_Cd/Nd2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O,S]      u0 {2,S}
6    [Cs,O,S]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Cd/Nd/De_Cd/Nd/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O,S]      u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Cd/Nd/De_Cd/De2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cd/De2_Cd/Nd2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O,S]      u0 {2,S}
6    [Cs,O,S]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Cd/De2_Cd/Nd/De",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O,S]      u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Cd/De2_Cd/De2",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Od_Cd",
    group = "OR{Od_Cds, Od_Cdd}",
    kinetics = None,
)

entry(
    index = 65,
    label = "Od_Cdd",
    group = 
"""
1 *1 Od  u0 {2,D}
2 *2 Cdd u0 {1,D} {3,D}
3    R!H   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Od_Cds",
    group = 
"""
1 *1 Od u0 {2,D}
2 *2 CO u0 {1,D} {3,S} {4,S}
3    R  u0 {2,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Od_Cd/unsub",
    group = 
"""
1 *1 Od u0 {2,D}
2 *2 CO u0 {1,D} {3,S} {4,S}
3    H  u0 {2,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Od_Cd/monosub",
    group = 
"""
1 *1 Od  u0 {2,D}
2 *2 CO  u0 {1,D} {3,S} {4,S}
3    H   u0 {2,S}
4    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Od_Cd/H/Nd",
    group = 
"""
1 *1 Od       u0 {2,D}
2 *2 CO       u0 {1,D} {3,S} {4,S}
3    H        u0 {2,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Od_Cd/H/Os",
    group = 
"""
1 *1 Od u0 {2,D}
2 *2 CO u0 {1,D} {3,S} {4,S}
3    H  u0 {2,S}
4    O  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Od_Cd/H/De",
    group = 
"""
1 *1 Od            u0 {2,D}
2 *2 CO            u0 {1,D} {3,S} {4,S}
3    H             u0 {2,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Od_Cd/H/Cd",
    group = 
"""
1 *1 Od u0 {2,D}
2 *2 CO u0 {1,D} {3,S} {4,S}
3    H  u0 {2,S}
4    Cd u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Od_Cd/H/Cb",
    group = 
"""
1 *1 Od u0 {2,D}
2 *2 CO u0 {1,D} {3,S} {4,S}
3    H  u0 {2,S}
4    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Od_Cd/disub",
    group = 
"""
1 *1 Od  u0 {2,D}
2 *2 CO  u0 {1,D} {3,S} {4,S}
3    R!H u0 {2,S}
4    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Od_Cd/Nd2",
    group = 
"""
1 *1 Od       u0 {2,D}
2 *2 CO       u0 {1,D} {3,S} {4,S}
3    [Cs,O,S] u0 {2,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Od_Cd/CsCs",
    group = 
"""
1 *1 Od u0 {2,D}
2 *2 CO u0 {1,D} {3,S} {4,S}
3    Cs u0 {2,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Od_Cd/CsOs",
    group = 
"""
1 *1 Od u0 {2,D}
2 *2 CO u0 {1,D} {3,S} {4,S}
3    Cs u0 {2,S}
4    O  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Od_Cd/Nd/De",
    group = 
"""
1 *1 Od            u0 {2,D}
2 *2 CO            u0 {1,D} {3,S} {4,S}
3    [Cs,O,S]      u0 {2,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Od_Cd/De2",
    group = 
"""
1 *1 Od            u0 {2,D}
2 *2 CO            u0 {1,D} {3,S} {4,S}
3    [Cd,Ct,Cb,CO] u0 {2,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Sd_Cd",
    group = "OR{Sd_Cds, Sd_Cdd}",
    kinetics = None,
)

entry(
    index = 78,
    label = "Sd_Cdd",
    group = 
"""
1 *1 S2d u0 {2,D}
2 *2 Cdd u0 {1,D} {3,D}
3    R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Sd_Cds",
    group = 
"""
1 *1 S2d u0 {2,D}
2 *2 CS u0 {1,D} {3,S} {4,S}
3    R  u0 {2,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Sd_Cd/unsub",
    group = 
"""
1 *1 S2d u0 {2,D}
2 *2 CS u0 {1,D} {3,S} {4,S}
3    H  u0 {2,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Sd_Cd/monosub",
    group = 
"""
1 *1 S2d u0 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    H   u0 {2,S}
4    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Sd_Cd/H/Nd",
    group = 
"""
1 *1 S2d      u0 {2,D}
2 *2 CS       u0 {1,D} {3,S} {4,S}
3    H        u0 {2,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Sd_Cd/H/De",
    group = 
"""
1 *1 S2d           u0 {2,D}
2 *2 CS            u0 {1,D} {3,S} {4,S}
3    H             u0 {2,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Sd_Cd/disub",
    group = 
"""
1 *1 S2d u0 {2,D}
2 *2 CS  u0 {1,D} {3,S} {4,S}
3    R!H u0 {2,S}
4    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Sd_Cd/Nd2",
    group = 
"""
1 *1 S2d      u0 {2,D}
2 *2 CS       u0 {1,D} {3,S} {4,S}
3    [Cs,O,S] u0 {2,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Sd_Cd/Nd/De",
    group = 
"""
1 *1 S2d           u0 {2,D}
2 *2 CS            u0 {1,D} {3,S} {4,S}
3    [Cs,O,S]      u0 {2,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Sd_Cd/De2",
    group = 
"""
1 *1 S2d           u0 {2,D}
2 *2 CS            u0 {1,D} {3,S} {4,S}
3    [Cd,Ct,Cb,CO] u0 {2,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "H_SR",
    group = 
"""
1 *3 H  u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "H_SH",
    group = 
"""
1 *3 H  u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "H_SCs",
    group = 
"""
1 *3 H  u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "H_SCs(HHH)",
    group = 
"""
1 *3 H  u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S} {5,S} {6,S}
4    H  u0 {3,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "H_SCs(CsHH)",
    group = 
"""
1 *3 H  u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S} {5,S} {6,S}
4    Cs u0 {3,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "H_SCs(CsCsH)",
    group = 
"""
1 *3 H  u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S} {5,S} {6,S}
4    Cs u0 {3,S}
5    Cs u0 {3,S}
6    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "H_SCs(CsCsCs)",
    group = 
"""
1 *3 H  u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S} {5,S} {6,S}
4    Cs u0 {3,S}
5    Cs u0 {3,S}
6    Cs u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "H_SCd",
    group = 
"""
1 *3 H  u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    Cd u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "R_SH",
    group = 
"""
1 *3 R!H u0 {2,S}
2 *4 S2s  u0 {1,S} {3,S}
3    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Cs_SH",
    group = 
"""
1 *3 Cs u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Cd_SH",
    group = 
"""
1 *3 Cd u0 {2,S}
2 *4 S2s u0 {1,S} {3,S}
3    H  u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: doublebond
    L2: Cd_Cdd
        L3: cco_2H
        L3: cco_HNd
        L3: cco_HDe
        L3: cco_Nd2
        L3: cco_NdDe
        L3: cco_De2
    L2: Cdd_Cd
        L3: Cdd_Cd_2H
        L3: Cdd_Cd_HNd
        L3: Cdd_Cd_HDe
        L3: Cdd_Cd_Nd2
        L3: Cdd_Cd_NdDe
        L3: Cdd_Cd_De2
    L2: Cd_Cd
        L3: Cd/unsub_Cd/unsub
        L3: Cd/unsub_Cd/monosub
            L4: Cd/H2_Cd/H/Nd
            L4: Cd/H2_Cd/H/De
        L3: Cd/monosub_Cd/unsub
            L4: Cd/H/Nd_Cd/H2
            L4: Cd/H/De_Cd/H2
        L3: Cd/unsub_Cd/disub
            L4: Cd/H2_Cd/Nd2
                L5: Cd/H2_Cd/Cs2
            L4: Cd/H2_Cd/Nd/De
            L4: Cd/H2_Cd/De2
        L3: Cd/disub_Cd/unsub
            L4: Cd/Nd2_Cd/H2
            L4: Cd/NdDe_Cd/H2
            L4: Cd/De2_Cd/H2
        L3: Cd/monosub_Cd/monosub
            L4: Cd/H/Nd_Cd/H/Nd
                L5: Cd/H/Nd_Cd/H/Os
            L4: Cd/H/Nd_Cd/H/De
            L4: Cd/H/De_Cd/H/Nd
            L4: Cd/H/De_Cd/H/De
        L3: Cd/monosub_Cd/disub
            L4: Cd/H/Nd_Cd/Nd2
            L4: Cd/H/Nd_Cd/Nd/De
            L4: Cd/H/Nd_Cd/De2
            L4: Cd/H/De_Cd/Nd2
            L4: Cd/H/De_Cd/Nd/De
            L4: Cd/H/De_Cd/De2
        L3: Cd/disub_Cd/monosub
            L4: Cd/Nd2_Cd/H/Nd
            L4: Cd/Nd2_Cd/H/De
            L4: Cd/De2_Cd/H/Nd
            L4: Cd/De2_Cd/H/De
            L4: Cd/Nd/De_Cd/H/Nd
            L4: Cd/Nd/De_Cd/H/De
        L3: Cd/disub_Cd/disub
            L4: Cd/Nd2_Cd/Nd2
            L4: Cd/Nd2_Cd/Nd/De
            L4: Cd/Nd2_Cd/De2
            L4: Cd/Nd/De_Cd/Nd2
            L4: Cd/Nd/De_Cd/Nd/De
            L4: Cd/Nd/De_Cd/De2
            L4: Cd/De2_Cd/Nd2
            L4: Cd/De2_Cd/Nd/De
            L4: Cd/De2_Cd/De2
    L2: Od_Cd
        L3: Od_Cdd
        L3: Od_Cds
            L4: Od_Cd/unsub
            L4: Od_Cd/monosub
                L5: Od_Cd/H/Nd
                    L6: Od_Cd/H/Os
                L5: Od_Cd/H/De
                    L6: Od_Cd/H/Cd
                    L6: Od_Cd/H/Cb
            L4: Od_Cd/disub
                L5: Od_Cd/Nd2
                    L6: Od_Cd/CsCs
                    L6: Od_Cd/CsOs
                L5: Od_Cd/Nd/De
                L5: Od_Cd/De2
    L2: Sd_Cd
        L3: Sd_Cdd
        L3: Sd_Cds
            L4: Sd_Cd/unsub
            L4: Sd_Cd/monosub
                L5: Sd_Cd/H/Nd
                L5: Sd_Cd/H/De
            L4: Sd_Cd/disub
                L5: Sd_Cd/Nd2
                L5: Sd_Cd/Nd/De
                L5: Sd_Cd/De2
L1: R_SR
    L2: H_SR
        L3: H_SH
        L3: H_SCs
            L4: H_SCs(HHH)
            L4: H_SCs(CsHH)
            L4: H_SCs(CsCsH)
            L4: H_SCs(CsCsCs)
        L3: H_SCd
    L2: R_SH
        L3: Cs_SH
        L3: Cd_SH
"""
)

