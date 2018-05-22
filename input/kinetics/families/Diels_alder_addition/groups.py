#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["{ene,yne}", "diene_out"], products=["Six_Ring"], ownReverse=False)

reverse = "Retro_Diels_Alder_Addition"

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*3', -1, '*4'],
    ['CHANGE_BOND', '*4', 1, '*5'],
    ['CHANGE_BOND', '*5', -1, '*6'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*6'],
])

entry(
    index = 1,
    label = "diene_out",
    group = """
1 *3 Cd u0 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "diene_in",
    group = 
"""
1 *4 [Cd,S4d,S6d,N3d,N5dc] u0 {2,S}
2 *5 [Cd,S4d,S6d,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "{ene,yne}",
    group = "OR{ene,yne}",
    kinetics = None,
)

entry(
    index = 3,
    label = "ene",
    group = 
"""
1 *1 [Cd,Cdd,CO,CS,O2d,S2d,S4d,S6d,N3d,N5dc] u0 {2,D}
2 *2 [Cd,CO,CS,O2d,S2d,S4d,S6d,N3d,N5dc]     u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "allene",
    group = 
"""
1 *1 Cdd u0 {2,D}
2 *2 Cd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "allene_unsub",
    group = 
"""
1 *1 Cdd u0 {2,D}
2 *2 Cd u0 {1,D} {3,S} {4,S}
3 H u0 {2,S}
4 H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "allene_monosub",
    group = 
"""
1 *1 Cdd u0 {2,D}
2 *2 Cd u0 {1,D} {3,S} {4,S}
3 R!H u0 {2,S}
4 H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "allene_disub",
    group = 
"""
1 *1 Cdd u0 {2,D}
2 *2 Cd u0 {1,D} {3,S} {4,S}
3 R!H u0 {2,S}
4 R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "yne",
    group = 
"""
1 *1 [Ct,S4t,S6t,S6td,S6tt,N3t,N5tc] u0 {2,T}
2 *2 [Ct,S4t,S6t,S6td,S6tt,N3t,N5tc] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "yne_unsub_unsub",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3 H u0 {1,S}
4 H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "yne_unsub_monosub",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3 H u0 {1,S}
4 R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "yne_monosub_monosub",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3 R!H u0 {1,S}
4 R!H u0 {2,S}
""",
    kinetics = None,
)


entry(
    index = 4,
    label = "diene_5ring_out",
    group = 
"""
1 *3 Cd u0 {2,D} {5,S} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {6,S} {7,S}
5 *7 R  u0 {1,S}
6 *8 C  u0 {1,S} {4,S}
7 *9 R  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "diene_5ring_H_H_out",
    group = 
"""
1 *3 Cd u0 {2,D} {5,S} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {6,S} {7,S}
5 *7 H  u0 {1,S}
6 *8 C  u0 {1,S} {4,S}
7 *9 H  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "diene_5ring_H_Nd_out",
    group = 
"""
1 *3 Cd       u0 {2,D} {5,S} {6,S}
2 *4 Cd       u0 {1,D} {3,S}
3 *5 Cd       u0 {2,S} {4,D}
4 *6 Cd       u0 {3,D} {6,S} {7,S}
5 *7 H        u0 {1,S}
6 *8 C        u0 {1,S} {4,S}
7 *9 [Cs,O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "diene_5ring_Nd_Nd_out",
    group = 
"""
1 *3 Cd       u0 {2,D} {5,S} {6,S}
2 *4 Cd       u0 {1,D} {3,S}
3 *5 Cd       u0 {2,S} {4,D}
4 *6 Cd       u0 {3,D} {6,S} {7,S}
5 *7 [Cs,O,S] u0 {1,S}
6 *8 C        u0 {1,S} {4,S}
7 *9 [Cs,O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "diene_unsub_unsub_out",
    group = 
"""
1 *3 Cd u0 {2,D} {5,S} {6,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {7,S} {8,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {4,S}
8    H  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "diene_unsub_monosub_out",
    group = 
"""
1 *3 Cd  u0 {2,D} {5,S} {6,S}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 Cd  u0 {2,S} {4,D}
4 *6 Cd  u0 {3,D} {7,S} {8,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {4,S}
8    R!H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "diene_unsub_monosubNd_out",
    group = 
"""
1 *3 Cd       u0 {2,D} {5,S} {6,S}
2 *4 Cd       u0 {1,D} {3,S}
3 *5 Cd       u0 {2,S} {4,D}
4 *6 Cd       u0 {3,D} {7,S} {8,S}
5    H        u0 {1,S}
6    H        u0 {1,S}
7    H        u0 {4,S}
8    [Cs,O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "diene_unsub_monosubDe_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6    H                u0 {1,S}
7    H                u0 {4,S}
8    [Cd,Ct,Cb,CO,CS] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "diene_unsub_disub_out",
    group = 
"""
1 *3 Cd  u0 {2,D} {5,S} {6,S}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 Cd  u0 {2,S} {4,D}
4 *6 Cd  u0 {3,D} {7,S} {8,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    R!H u0 {4,S}
8    R!H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "diene_unsub_disubNd2_out",
    group = 
"""
1 *3 Cd       u0 {2,D} {5,S} {6,S}
2 *4 Cd       u0 {1,D} {3,S}
3 *5 Cd       u0 {2,S} {4,D}
4 *6 Cd       u0 {3,D} {7,S} {8,S}
5    H        u0 {1,S}
6    H        u0 {1,S}
7    [Cs,O,S] u0 {4,S}
8    [Cs,O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "diene_unsub_disubNdDe_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6    H                u0 {1,S}
7    [Cs,O,S]         u0 {4,S}
8    [Cd,Ct,Cb,CO,CS] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "diene_unsub_disubDe2_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6    H                u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {4,S}
8    [Cd,Ct,Cb,CO,CS] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "diene_monosub_monosub_out",
    group = 
"""
1 *3 Cd  u0 {2,D} {5,S} {6,S}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 Cd  u0 {2,S} {4,D}
4 *6 Cd  u0 {3,D} {7,S} {8,S}
5    H   u0 {1,S}
6 *7 R!H u0 {1,S}
7 *8 R!H u0 {4,S}
8    H   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "diene_monosubNd_monosubNd_out",
    group = 
"""
1 *3 Cd       u0 {2,D} {5,S} {6,S}
2 *4 Cd       u0 {1,D} {3,S}
3 *5 Cd       u0 {2,S} {4,D}
4 *6 Cd       u0 {3,D} {7,S} {8,S}
5    H        u0 {1,S}
6 *7 [Cs,O,S] u0 {1,S}
7 *8 [Cs,O,S] u0 {4,S}
8    H        u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "diene_monosubNd_monosubDe_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6 *7 [Cs,O,S]         u0 {1,S}
7 *8 [Cd,Ct,Cb,CO,CS] u0 {4,S}
8    H                u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "diene_monosubDe_monosubDe_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6 *7 [Cd,Ct,Cb,CO,CS] u0 {1,S}
7 *8 [Cd,Ct,Cb,CO,CS] u0 {4,S}
8    H                u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "diene_monosub_disub_out",
    group = 
"""
1 *3 Cd  u0 {2,D} {5,S} {6,S}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 Cd  u0 {2,S} {4,D}
4 *6 Cd  u0 {3,D} {7,S} {8,S}
5    H   u0 {1,S}
6 *7 R!H u0 {1,S}
7 *8 R!H u0 {4,S}
8 *9 R!H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "diene_monosubNd_disubNd2_out",
    group = 
"""
1 *3 Cd       u0 {2,D} {5,S} {6,S}
2 *4 Cd       u0 {1,D} {3,S}
3 *5 Cd       u0 {2,S} {4,D}
4 *6 Cd       u0 {3,D} {7,S} {8,S}
5    H        u0 {1,S}
6 *7 [Cs,O,S] u0 {1,S}
7 *8 [Cs,O,S] u0 {4,S}
8 *9 [Cs,O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "diene_monosubNd_disubNdDe_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6 *7 [Cs,O,S]         u0 {1,S}
7 *8 [Cs,O,S]         u0 {4,S}
8 *9 [Cd,Ct,Cb,CO,CS] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "diene_monosubNd_disubDe2_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6 *7 [Cs,O,S]         u0 {1,S}
7 *8 [Cd,Ct,Cb,CO,CS] u0 {4,S}
8 *9 [Cd,Ct,Cb,CO,CS] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "diene_monosubDe_disubNd2_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6 *7 [Cd,Ct,Cb,CO,CS] u0 {1,S}
7 *8 [Cs,O,S]         u0 {4,S}
8 *9 [Cs,O,S]         u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "diene_monosubDe_disubNdDe_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6 *7 [Cd,Ct,Cb,CO,CS] u0 {1,S}
7 *8 [Cs,O,S]         u0 {4,S}
8 *9 [Cd,Ct,Cb,CO,CS] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "diene_monosubDe_disubDe2_out",
    group = 
"""
1 *3 Cd               u0 {2,D} {5,S} {6,S}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {7,S} {8,S}
5    H                u0 {1,S}
6 *7 [Cd,Ct,Cb,CO,CS] u0 {1,S}
7 *8 [Cd,Ct,Cb,CO,CS] u0 {4,S}
8 *9 [Cd,Ct,Cb,CO,CS] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "diene_disub_disub_out",
    group = 
"""
1 *3  Cd  u0 {2,D} {5,S} {6,S}
2 *4  Cd  u0 {1,D} {3,S}
3 *5  Cd  u0 {2,S} {4,D}
4 *6  Cd  u0 {3,D} {7,S} {8,S}
5 *7  R!H u0 {1,S}
6 *8  R!H u0 {1,S}
7 *9  R!H u0 {4,S}
8 *10 R!H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "diene_disubNd2_disubNd2_out",
    group = 
"""
1 *3  Cd       u0 {2,D} {5,S} {6,S}
2 *4  Cd       u0 {1,D} {3,S}
3 *5  Cd       u0 {2,S} {4,D}
4 *6  Cd       u0 {3,D} {7,S} {8,S}
5 *7  [Cs,O,S] u0 {1,S}
6 *8  [Cs,O,S] u0 {1,S}
7 *9  [Cs,O,S] u0 {4,S}
8 *10 [Cs,O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "diene_disubNd2_disubDe_out",
    group = 
"""
1 *3  Cd               u0 {2,D} {5,S} {6,S}
2 *4  Cd               u0 {1,D} {3,S}
3 *5  Cd               u0 {2,S} {4,D}
4 *6  Cd               u0 {3,D} {7,S} {8,S}
5 *7  [Cs,O,S]         u0 {1,S}
6 *8  [Cs,O,S]         u0 {1,S}
7 *9  R!H              u0 {4,S}
8 *10 [Cd,Ct,Cb,CO,CS] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "diene_disubDe_disubDe_out",
    group = 
"""
1 *3  Cd               u0 {2,D} {5,S} {6,S}
2 *4  Cd               u0 {1,D} {3,S}
3 *5  Cd               u0 {2,S} {4,D}
4 *6  Cd               u0 {3,D} {7,S} {8,S}
5 *7  R!H              u0 {1,S}
6 *8  [Cd,Ct,Cb,CO,CS] u0 {1,S}
7 *9  R!H              u0 {4,S}
8 *10 [Cd,Ct,Cb,CO,CS] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "diene_in_2H",
    group = 
"""
1 *4 Cd u0 {2,S} {3,S}
2 *5 Cd u0 {1,S} {4,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "diene_in_HNd",
    group = 
"""
1 *4 Cd       u0 {2,S} {3,S}
2 *5 Cd       u0 {1,S} {4,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "diene_in_HDe",
    group = 
"""
1 *4 Cd               u0 {2,S} {3,S}
2 *5 Cd               u0 {1,S} {4,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "diene_in_NdH",
    group = 
"""
1 *4 Cd       u0 {2,S} {3,S}
2 *5 Cd       u0 {1,S} {4,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "diene_in_DeH",
    group = 
"""
1 *4 Cd               u0 {2,S} {3,S}
2 *5 Cd               u0 {1,S} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "diene_in_Nd2",
    group = 
"""
1 *4 Cd       u0 {2,S} {3,S}
2 *5 Cd       u0 {1,S} {4,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "diene_in_NdDe",
    group = 
"""
1 *4 Cd               u0 {2,S} {3,S}
2 *5 Cd               u0 {1,S} {4,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "diene_in_DeNd",
    group = 
"""
1 *4 Cd               u0 {2,S} {3,S}
2 *5 Cd               u0 {1,S} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "diene_in_De2",
    group = 
"""
1 *4 Cd               u0 {2,S} {3,S}
2 *5 Cd               u0 {1,S} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "ene_unsub_unsub",
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
    index = 37,
    label = "ene_unsub_monosub",
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
    index = 38,
    label = "ene_2H_HNd",
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
    index = 39,
    label = "ene_2H_HDe",
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
    index = 40,
    label = "ene_monosub_unsub",
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
    index = 41,
    label = "ene_HNd_2H",
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
    index = 42,
    label = "ene_HDe_2H",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "ene_monosub_monosub",
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
    index = 44,
    label = "ene_HNd_HNd",
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
    index = 45,
    label = "ene_HNd_HDe",
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
    index = 46,
    label = "ene_HDe_HNd",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "ene_HDe_HDe",
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
    index = 48,
    label = "ene_unsub_disub",
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
    index = 49,
    label = "ene_2H_Nd2",
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
    index = 50,
    label = "ene_2H_NdDe",
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
    index = 51,
    label = "ene_2H_De2",
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
    index = 52,
    label = "ene_disub_unsub",
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
    index = 53,
    label = "ene_Nd2_2H",
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
    index = 54,
    label = "ene_NdDe_2H",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "ene_De2_2H",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "ene_monosub_disub",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    R!H u0 {1,S}
4    H   u0 {1,S}
5    R!H u0 {2,S}
6    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "ene_HNd_Nd2",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {1,S}
5    [Cs,O,S] u0 {2,S}
6    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "ene_HNd_NdDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    H                u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "ene_HNd_De2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "ene_HDe_Nd2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "ene_HDe_NdDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "ene_HDe_De2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "ene_disub_monosub",
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
    index = 64,
    label = "ene_Nd2_HNd",
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
    index = 65,
    label = "ene_Nd2_HDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    H                u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "ene_NdDe_HNd",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "ene_NdDe_HDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "ene_De2_HNd",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "ene_De2_HDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "ene_disub_disub",
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
    index = 71,
    label = "ene_Nd2_Nd2",
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
    index = 72,
    label = "ene_Nd2_NdDe",
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
    index = 73,
    label = "ene_Nd2_De2",
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
    index = 74,
    label = "ene_NdDe_Nd2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "ene_NdDe_NdDe",
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
    index = 76,
    label = "ene_NdDe_De2",
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
    index = 77,
    label = "ene_De2_Nd2",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "ene_De2_NdDe",
    group = 
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "ene_De2_De2",
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

tree(
"""
L1: diene_out
    L2: diene_5ring_out
        L3: diene_5ring_H_H_out
        L3: diene_5ring_H_Nd_out
        L3: diene_5ring_Nd_Nd_out
    L2: diene_unsub_unsub_out
    L2: diene_unsub_monosub_out
        L3: diene_unsub_monosubNd_out
        L3: diene_unsub_monosubDe_out
    L2: diene_unsub_disub_out
        L3: diene_unsub_disubNd2_out
        L3: diene_unsub_disubNdDe_out
        L3: diene_unsub_disubDe2_out
    L2: diene_monosub_monosub_out
        L3: diene_monosubNd_monosubNd_out
        L3: diene_monosubNd_monosubDe_out
        L3: diene_monosubDe_monosubDe_out
    L2: diene_monosub_disub_out
        L3: diene_monosubNd_disubNd2_out
        L3: diene_monosubNd_disubNdDe_out
        L3: diene_monosubNd_disubDe2_out
        L3: diene_monosubDe_disubNd2_out
        L3: diene_monosubDe_disubNdDe_out
        L3: diene_monosubDe_disubDe2_out
    L2: diene_disub_disub_out
        L3: diene_disubNd2_disubNd2_out
        L3: diene_disubNd2_disubDe_out
        L3: diene_disubDe_disubDe_out
L1: diene_in
    L2: diene_in_2H
    L2: diene_in_HNd
    L2: diene_in_HDe
    L2: diene_in_NdH
    L2: diene_in_DeH
    L2: diene_in_Nd2
    L2: diene_in_NdDe
    L2: diene_in_DeNd
    L2: diene_in_De2
L1: {ene,yne}
   L2: ene
       L3: ene_unsub_unsub
       L3: ene_unsub_monosub
          L4: ene_2H_HNd
          L4: ene_2H_HDe
       L3: ene_monosub_unsub
             L4: ene_HNd_2H
             L4: ene_HDe_2H
       L3: ene_monosub_monosub
             L4: ene_HNd_HNd
             L4: ene_HNd_HDe
             L4: ene_HDe_HNd
             L4: ene_HDe_HDe
       L3: ene_unsub_disub
             L4: ene_2H_Nd2
             L4: ene_2H_NdDe
             L4: ene_2H_De2
       L3: ene_disub_unsub
             L4: ene_Nd2_2H
             L4: ene_NdDe_2H
             L4: ene_De2_2H
       L3: ene_monosub_disub
             L4: ene_HNd_Nd2
             L4: ene_HNd_NdDe
             L4: ene_HNd_De2
             L4: ene_HDe_Nd2
             L4: ene_HDe_NdDe
             L4: ene_HDe_De2
       L3: ene_disub_monosub
             L4: ene_Nd2_HNd
             L4: ene_Nd2_HDe
             L4: ene_NdDe_HNd
             L4: ene_NdDe_HDe
             L4: ene_De2_HNd
             L4: ene_De2_HDe
       L3: ene_disub_disub
             L4: ene_Nd2_Nd2
             L4: ene_Nd2_NdDe
             L4: ene_Nd2_De2
             L4: ene_NdDe_Nd2
             L4: ene_NdDe_NdDe
             L4: ene_NdDe_De2
             L4: ene_De2_Nd2
             L4: ene_De2_NdDe
             L4: ene_De2_De2
        L3: allene
             L4: allene_unsub
             L4: allene_monosub
             L4: allene_disub
    L2: yne
        L3: yne_unsub_unsub
        L3: yne_unsub_monosub
        L3: yne_monosub_monosub
"""
)

forbidden(
    label = "threeMemberedRing_2342",
    group = 
"""
1 *3 Cd u0 {2,D}
2 *4 Cd u0 {1,D} {3,S} {4,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {2,S} {3,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "threeMemberedRing_3213",
    group = 
"""
1 *3 Cd u0 {2,D} {3,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {1,S} {2,S} {4,D}
4 *6 Cd u0 {3,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "allene_avoid_doublecounting",
    group = 
"""
1 *2 Cdd u0
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "benzene_diene_partial1",
    group = 
"""
1 *3 Cd u0 {2,D} {6,S} 
2 *4 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S} 
5    Cd ux {4,S} {6,D}
6    Cd ux {5,D} {1,S} 
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "benzene_diene_partial2",
    group = 
"""
1 *5 Cd u0 {2,D} {6,S} 
2 *6 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S} 
5    Cd ux {4,S} {6,D}
6    Cd ux {5,D} {1,S} 
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "benzene_diene1",
    group = 
"""
1 *3 Cd u0 {2,D} {6,S} 
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {5,S} 
5    Cd ux {4,S} {6,D}
6    Cd ux {5,D} {1,S} 
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "benzene_diene2",
    group = 
"""
1 *3 Cd u0 {2,D} {6,S} 
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {5,S} 
5 *8 Cd ux {4,S} {6,D}
6 *7 Cd ux {5,D} {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "benzene_monoSub1",
    group = 
"""
1 *3 Cd u0 {2,D} {6,S} {7,S}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {5,S} {8,S}
5 *7 Cd ux {4,S} {6,D}
6 *8 Cd ux {5,D} {1,S} 
7 H u0 {1,S}
8 *9 R  ux {4,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "benzene_monoSub2",
    group = 
"""
1 *3 Cd u0 {2,D}, {5,S}, {6,S}
2 *4 Cd u0 {1,D}, {3,S}
3 *5 Cd u0 {2,S}, {4,D}
4 *6 Cd u0 {3,D}, {7,S}, {8,S}
5 H u0 {1,S}
6 *7 Cd ux {1,S} {8,D}
7 *8 R ux {4,S}
8 *9 Cd ux {4,S} {6,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "benzene_twoSub1",
    group = 
"""
1 *3 Cd u0 {2,D}, {5,S}, {6,S}
2 *4 Cd u0 {1,D}, {3,S}
3 *5 Cd u0 {2,S}, {4,D}
4 *6 Cd u0 {3,D}, {7,S}, {8,S}
5 H u0 {1,S}
6 *7 Cd ux {1,S} {8,D}
7 *8 R ux {4,S}
8 *9 Cd ux {4,S} {6,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "benzene_twoSub2",
    group = 
"""
1 *3 Cd u0 {2,D}, {5,S}, {6,S}
2 *4 Cd u0 {1,D}, {3,S}
3 *5 Cd u0 {2,S}, {4,D}
4 *6 Cd u0 {3,D}, {7,S}, {8,S}
5 H u0 {1,S}
6 *7 Cd ux {1,S} {8,D}
7 *8 R ux {4,S}
8 *9 Cd ux {4,S} {6,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)


forbidden(
    label = "benzene_ene",
    group = 
"""
1 *1 Cd u0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S}
5    Cd ux {4,S} {6,D}
6    Cd ux {5,D} {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label= 'benzyl_isomer1',
    group=
"""
1 C 0 {2,D}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D}
4 C 0 {3,D} {5,S}
5 C 1 {4,S} {6,S}
6 C 0 {5,S} {7,D}
7 C 0 {2,S} {6,D}
"""
    )

forbidden(
    label= 'benzyl_isomer2',
    group=
"""
1 C 0 {2,D}
2 C 0 {1,D} {3,S} {7,S}
3 C 1 {2,S} {4,S}
4 C 0 {3,S} {5,D}
5 C 0 {4,D} {6,S}
6 C 0 {5,S} {7,D}
7 C 0 {2,S} {6,D}
"""
    )