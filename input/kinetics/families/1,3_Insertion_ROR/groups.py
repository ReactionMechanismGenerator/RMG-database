#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_ROR/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["doublebond", "R_OR"], products=["R_doublebond_OR"], ownReverse=False)

reverse = "1,2_Elimination_ROR"

recipe(actions=[
    ['BREAK_BOND', '*3', 'S', '*4'],
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*4'],
])

entry(
    index = 1,
    label = "doublebond",
    group = "OR{Cd_Cdd, Cdd_Cd, Cd_Cd, Sd_Cd, N3d_N3d, N3d_Cd}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "R_OR",
    group = "OR{H_OR, R_OH}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Cd_Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D}
2 *2 Cdd U0 {1,D} {3,D}
3    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "cco_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {4,S} {5,S}
2 *2 Cdd U0 {1,D} {3,D}
3    Od  U0 {2,D}
4    H   U0 {1,S}
5    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "cco_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd       U0 {2,D} {4,S} {5,S}
2 *2 Cdd      U0 {1,D} {3,D}
3    Od       U0 {2,D}
4    H        U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "cco_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd               U0 {2,D} {4,S} {5,S}
2 *2 Cdd              U0 {1,D} {3,D}
3    Od               U0 {2,D}
4    H                U0 {1,S}
5    {Cd,Ct,Cb,CO,CS} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "cco_Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd       U0 {2,D} {4,S} {5,S}
2 *2 Cdd      U0 {1,D} {3,D}
3    Od       U0 {2,D}
4    {Cs,O,S} U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "cco_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd               U0 {2,D} {4,S} {5,S}
2 *2 Cdd              U0 {1,D} {3,D}
3    Od               U0 {2,D}
4    {Cs,O,S}         U0 {1,S}
5    {Cd,Ct,Cb,CO,CS} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "cco_De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd               U0 {2,D} {4,S} {5,S}
2 *2 Cdd              U0 {1,D} {3,D}
3    Od               U0 {2,D}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cd,Ct,Cb,CO,CS} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Cdd_Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D}
3    Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Cdd_Cd_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    H   U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "Cdd_Cd_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd      U0 {2,D} {3,D}
2 *2 Cd       U0 {1,D} {4,S} {5,S}
3    Od       U0 {1,D}
4    H        U0 {2,S}
5    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "Cdd_Cd_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd              U0 {2,D} {3,D}
2 *2 Cd               U0 {1,D} {4,S} {5,S}
3    Od               U0 {1,D}
4    H                U0 {2,S}
5    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "Cdd_Cd_Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd      U0 {2,D} {3,D}
2 *2 Cd       U0 {1,D} {4,S} {5,S}
3    Od       U0 {1,D}
4    {Cs,O,S} U0 {2,S}
5    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "Cdd_Cd_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd              U0 {2,D} {3,D}
2 *2 Cd               U0 {1,D} {4,S} {5,S}
3    Od               U0 {1,D}
4    {Cs,O,S}         U0 {2,S}
5    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "Cdd_Cd_De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd              U0 {2,D} {3,D}
2 *2 Cd               U0 {1,D} {4,S} {5,S}
3    Od               U0 {1,D}
4    {Cd,Ct,Cb,CO,CS} U0 {2,S}
5    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "Cd_Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    R  U0 {1,S}
4    R  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "Cd/unsub_Cd/unsub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "Cd/unsub_Cd/monosub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cd  U0 {1,D} {5,S} {6,S}
3    H   U0 {1,S}
4    H   U0 {1,S}
5    H   U0 {2,S}
6    R!H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "Cd/H2_Cd/H/Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    H        U0 {1,S}
5    H        U0 {2,S}
6    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "Cd/H2_Cd/H/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    H                U0 {1,S}
5    H                U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "Cd/monosub_Cd/unsub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cd  U0 {1,D} {5,S} {6,S}
3    H   U0 {1,S}
4    R!H U0 {1,S}
5    H   U0 {2,S}
6    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "Cd/H/Nd_Cd/H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    H        U0 {2,S}
6    H        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Cd/H/De_Cd/H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    H                U0 {2,S}
6    H                U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "Cd/unsub_Cd/disub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cd  U0 {1,D} {5,S} {6,S}
3    H   U0 {1,S}
4    H   U0 {1,S}
5    R!H U0 {2,S}
6    R!H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "Cd/H2_Cd/Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    H        U0 {1,S}
5    {Cs,O,S} U0 {2,S}
6    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "Cd/H2_Cd/Nd/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    H                U0 {1,S}
5    {Cs,O,S}         U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "Cd/H2_Cd/De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    H                U0 {1,S}
5    {Cd,Ct,Cb,CO,CS} U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "Cd/disub_Cd/unsub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cd  U0 {1,D} {5,S} {6,S}
3    R!H U0 {1,S}
4    R!H U0 {1,S}
5    H   U0 {2,S}
6    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "Cd/Nd2_Cd/H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    {Cs,O,S} U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    H        U0 {2,S}
6    H        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "Cd/NdDe_Cd/H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    H                U0 {2,S}
6    H                U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "Cd/De2_Cd/H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    H                U0 {2,S}
6    H                U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "Cd/monosub_Cd/monosub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cd  U0 {1,D} {5,S} {6,S}
3    H   U0 {1,S}
4    R!H U0 {1,S}
5    H   U0 {2,S}
6    R!H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "Cd/H/Nd_Cd/H/Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    H        U0 {2,S}
6    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "Cd/H/Nd_Cd/H/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    {Cs,O,S}         U0 {1,S}
5    H                U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "Cd/H/S_Cd/H/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2 *2 C  U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    S  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "Thiophene3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2 *2 C  U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    S  U0 {1,S} {7,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {4,S} {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "Cd/H/De_Cd/H/Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    H                U0 {2,S}
6    {Cs,O,S}         U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "Cd/H/Cd_Cd/H/S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2 *2 C  U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    Cd U0 {1,S}
5    H  U0 {2,S}
6    S  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "Thiophene2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2 *2 C  U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    Cd U0 {1,S} {7,D}
5    H  U0 {2,S}
6    S  U0 {2,S} {7,S}
7    C  U0 {4,D} {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "Cd/H/De_Cd/H/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    H                U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "Cd/monosub_Cd/disub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cd  U0 {1,D} {5,S} {6,S}
3    H   U0 {1,S}
4    R!H U0 {1,S}
5    R!H U0 {2,S}
6    R!H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "Cd/H/Nd_Cd/Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    {Cs,O,S} U0 {2,S}
6    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "Cd/H/Nd_Cd/Nd/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    {Cs,O,S}         U0 {1,S}
5    {Cs,O,S}         U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "Cd/H/Nd_Cd/De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    {Cs,O,S}         U0 {1,S}
5    {Cd,Ct,Cb,CO,CS} U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "Cd/H/De_Cd/Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cs,O,S}         U0 {2,S}
6    {Cs,O,S}         U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "Cd/H/De_Cd/Nd/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cs,O,S}         U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "Cd/H/De_Cd/De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    H                U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cd,Ct,Cb,CO,CS} U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "Cd/disub_Cd/monosub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cd  U0 {1,D} {5,S} {6,S}
3    R!H U0 {1,S}
4    R!H U0 {1,S}
5    H   U0 {2,S}
6    R!H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "Cd/Nd2_Cd/H/Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    {Cs,O,S} U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    H        U0 {2,S}
6    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "Cd/Nd2_Cd/H/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         U0 {1,S}
4    {Cs,O,S}         U0 {1,S}
5    H                U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "Cd/De2_Cd/H/Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    H                U0 {2,S}
6    {Cs,O,S}         U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "Cd/De2_Cd/H/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    H                U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "Cd/Nd/De_Cd/H/Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    H                U0 {2,S}
6    {Cs,O,S}         U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "Cd/Nd/De_Cd/H/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    H                U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "Cd/disub_Cd/disub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cd  U0 {1,D} {5,S} {6,S}
3    R!H U0 {1,S}
4    R!H U0 {1,S}
5    R!H U0 {2,S}
6    R!H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "Cd/Nd2_Cd/Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    {Cs,O,S} U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    {Cs,O,S} U0 {2,S}
6    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "Cd/Nd2_Cd/Nd/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         U0 {1,S}
4    {Cs,O,S}         U0 {1,S}
5    {Cs,O,S}         U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "Cd/Nd2_Cd/De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         U0 {1,S}
4    {Cs,O,S}         U0 {1,S}
5    {Cd,Ct,Cb,CO,CS} U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "Cd/Nd/De_Cd/Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cs,O,S}         U0 {2,S}
6    {Cs,O,S}         U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "Cd/Nd/De_Cd/Nd/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cs,O,S}         U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "Cd/Nd/De_Cd/De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cd,Ct,Cb,CO,CS} U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "Cd/De2_Cd/Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cs,O,S}         U0 {2,S}
6    {Cs,O,S}         U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "Cd/De2_Cd/Nd/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cs,O,S}         U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "Cd/De2_Cd/De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2 *2 C                U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
5    {Cd,Ct,Cb,CO,CS} U0 {2,S}
6    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "Sd_Cd",
    group = "OR{Sd_Cds, Sd_Cdd}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "Sd_Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,D}
3    R  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "Sd_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    R  U0 {2,S}
4    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "Sd_Cd/unsub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    H  U0 {2,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "Sd_Cd/monosub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd  U0 {2,D}
2 *2 Cd  U0 {1,D} {3,S} {4,S}
3    H   U0 {2,S}
4    R!H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "Sd_Cd/H/Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd       U0 {2,D}
2 *2 Cd       U0 {1,D} {3,S} {4,S}
3    H        U0 {2,S}
4    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "Sd_Cd/H/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd               U0 {2,D}
2 *2 Cd               U0 {1,D} {3,S} {4,S}
3    H                U0 {2,S}
4    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "Sd_Cd/H/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    H  U0 {2,S}
4    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "Sd_Cd/disub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd  U0 {2,D}
2 *2 Cd  U0 {1,D} {3,S} {4,S}
3    R!H U0 {2,S}
4    R!H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "Sd_Cd/Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd       U0 {2,D}
2 *2 Cd       U0 {1,D} {3,S} {4,S}
3    {Cs,O,S} U0 {2,S}
4    {Cs,O,S} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "Sd_Cd/Nd/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd               U0 {2,D}
2 *2 Cd               U0 {1,D} {3,S} {4,S}
3    {Cs,O,S}         U0 {2,S}
4    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "Sd_Cd/De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd               U0 {2,D}
2 *2 Cd               U0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO,CS} U0 {2,S}
4    {Cd,Ct,Cb,CO,CS} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "N3d_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D}
2 *2 N3d U0 {1,D} {3,D}
3    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "N3d_Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D}
2 *2 Cd  U0 {1,D} {3,D}
3    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "H_OR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H                   U0 {2,S}
2 *4 Os                  U0 {1,S} {3,S}
3    {H,Cs,Cd,Sis,Sid,N} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "H_OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H  U0 {2,S}
2 *4 Os U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "H_OCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H  U0 {2,S}
2 *4 Os U0 {1,S} {3,S}
3    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "H_OCmethyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H  U0 {2,S}
2 *4 Os U0 {1,S} {3,S}
3    Cs U0 {2,S} {4,S} {5,S} {6,S}
4    H  U0 {3,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "H_OCpri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H  U0 {2,S}
2 *4 Os U0 {1,S} {3,S}
3    Cs U0 {2,S} {4,S} {5,S} {6,S}
4    H  U0 {3,S}
5    H  U0 {3,S}
6    C  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "H_OCsec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H  U0 {2,S}
2 *4 Os U0 {1,S} {3,S}
3    Cs U0 {2,S} {4,S} {5,S} {6,S}
4    H  U0 {3,S}
5    C  U0 {3,S}
6    C  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "H_OCter",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H  U0 {2,S}
2 *4 Os U0 {1,S} {3,S}
3    Cs U0 {2,S} {4,S} {5,S} {6,S}
4    C  U0 {3,S}
5    C  U0 {3,S}
6    C  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "H_OCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H  U0 {2,S}
2 *4 Os U0 {1,S} {3,S}
3    Cd U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "H_OCdpri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H  U0 {2,S}
2 *4 Os U0 {1,S} {3,S}
3    Cd U0 {2,S} {4,D} {5,S}
4    Cd U0 {3,D}
5    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "H_OCdsec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H  U0 {2,S}
2 *4 Os U0 {1,S} {3,S}
3    Cd U0 {2,S} {4,D} {5,S}
4    Cd U0 {3,D}
5    C  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "R_OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {Cs,Cd,Sis,Sid,N} U0 {2,S}
2 *4 Os                U0 {1,S} {3,S}
3    H                 U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "Cd_OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U0 {2,D} {3,S} {4,S}
2    Cd U0 {1,D}
3 *4 Os U0 {1,S} {5,S}
4    R  U0 {1,S}
5    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "Cd_pri_OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U0 {2,D} {3,S} {4,S}
2    Cd U0 {1,D}
3 *4 Os U0 {1,S} {5,S}
4    H  U0 {1,S}
5    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "Cd_sec_OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd  U0 {2,D} {3,S} {4,S}
2    Cd  U0 {1,D}
3 *4 Os  U0 {1,S} {5,S}
4    R!H U0 {1,S}
5    H   U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "Cs_OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs     U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os     U0 {1,S} {6,S}
3    {Cs,H} U0 {1,S}
4    {Cs,H} U0 {1,S}
5    {Cs,H} U0 {1,S}
6    H      U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "CH3OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os U0 {1,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "C_pri_OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os U0 {1,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {1,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C_sec_OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os U0 {1,S} {6,S}
3    H  U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C_ter_OH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os U0 {1,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
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
            L4: Cd/H2_Cd/Nd/De
            L4: Cd/H2_Cd/De2
        L3: Cd/disub_Cd/unsub
            L4: Cd/Nd2_Cd/H2
            L4: Cd/NdDe_Cd/H2
            L4: Cd/De2_Cd/H2
        L3: Cd/monosub_Cd/monosub
            L4: Cd/H/Nd_Cd/H/Nd
            L4: Cd/H/Nd_Cd/H/De
                L5: Cd/H/S_Cd/H/Cd
                    L6: Thiophene3
            L4: Cd/H/De_Cd/H/Nd
                L5: Cd/H/Cd_Cd/H/S
                    L6: Thiophene2
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
    L2: Sd_Cd
        L3: Sd_Cdd
        L3: Sd_Cds
            L4: Sd_Cd/unsub
            L4: Sd_Cd/monosub
                L5: Sd_Cd/H/Nd
                L5: Sd_Cd/H/De
                    L6: Sd_Cd/H/Cb
            L4: Sd_Cd/disub
                L5: Sd_Cd/Nd2
                L5: Sd_Cd/Nd/De
                L5: Sd_Cd/De2
    L2: N3d_N3d
    L2: N3d_Cd
L1: R_OR
    L2: H_OR
        L3: H_OH
        L3: H_OCs
            L4: H_OCmethyl
            L4: H_OCpri
            L4: H_OCsec
            L4: H_OCter
        L3: H_OCd
            L4: H_OCdpri
            L4: H_OCdsec
    L2: R_OH
        L3: Cd_OH
            L4: Cd_pri_OH
            L4: Cd_sec_OH
        L3: Cs_OH
            L4: CH3OH
            L4: C_pri_OH
            L4: C_sec_OH
            L4: C_ter_OH
"""
)

