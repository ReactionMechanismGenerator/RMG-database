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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "R_OR",
    group = "OR{H_OR, R_OH}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "Cd_Cdd",
    group = 
"""
1 *1 Cd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "cco_2H",
    group = 
"""
1 *1 Cd  0 {2,D} {4,S} {5,S}
2 *2 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
4    H   0 {1,S}
5    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "cco_HNd",
    group = 
"""
1 *1 Cd       0 {2,D} {4,S} {5,S}
2 *2 Cdd      0 {1,D} {3,D}
3    Od       0 {2,D}
4    H        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "cco_HDe",
    group = 
"""
1 *1 Cd               0 {2,D} {4,S} {5,S}
2 *2 Cdd              0 {1,D} {3,D}
3    Od               0 {2,D}
4    H                0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "cco_Nd2",
    group = 
"""
1 *1 Cd       0 {2,D} {4,S} {5,S}
2 *2 Cdd      0 {1,D} {3,D}
3    Od       0 {2,D}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "cco_NdDe",
    group = 
"""
1 *1 Cd               0 {2,D} {4,S} {5,S}
2 *2 Cdd              0 {1,D} {3,D}
3    Od               0 {2,D}
4    {Cs,O,S}         0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "cco_De2",
    group = 
"""
1 *1 Cd               0 {2,D} {4,S} {5,S}
2 *2 Cdd              0 {1,D} {3,D}
3    Od               0 {2,D}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "Cdd_Cd",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D}
3    Od  0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "Cdd_Cd_2H",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D} {4,S} {5,S}
3    Od  0 {1,D}
4    H   0 {2,S}
5    H   0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "Cdd_Cd_HNd",
    group = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    Od       0 {1,D}
4    H        0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "Cdd_Cd_HDe",
    group = 
"""
1 *1 Cdd              0 {2,D} {3,D}
2 *2 Cd               0 {1,D} {4,S} {5,S}
3    Od               0 {1,D}
4    H                0 {2,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "Cdd_Cd_Nd2",
    group = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    Od       0 {1,D}
4    {Cs,O,S} 0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "Cdd_Cd_NdDe",
    group = 
"""
1 *1 Cdd              0 {2,D} {3,D}
2 *2 Cd               0 {1,D} {4,S} {5,S}
3    Od               0 {1,D}
4    {Cs,O,S}         0 {2,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "Cdd_Cd_De2",
    group = 
"""
1 *1 Cdd              0 {2,D} {3,D}
2 *2 Cd               0 {1,D} {4,S} {5,S}
3    Od               0 {1,D}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "Cd_Cd",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    R  0 {1,S}
4    R  0 {1,S}
5    R  0 {2,S}
6    R  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "Cd/unsub_Cd/unsub",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "Cd/unsub_Cd/monosub",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cd  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    H   0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "Cd/H2_Cd/H/Nd",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "Cd/H2_Cd/H/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "Cd/monosub_Cd/unsub",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cd  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    H   0 {2,S}
6    H   0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "Cd/H/Nd_Cd/H2",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "Cd/H/De_Cd/H2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "Cd/unsub_Cd/disub",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cd  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    R!H 0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "Cd/H2_Cd/Nd2",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "Cd/H2_Cd/Nd/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "Cd/H2_Cd/De2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "Cd/disub_Cd/unsub",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cd  0 {1,D} {5,S} {6,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    H   0 {2,S}
6    H   0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "Cd/Nd2_Cd/H2",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "Cd/NdDe_Cd/H2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "Cd/De2_Cd/H2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "Cd/monosub_Cd/monosub",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cd  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    H   0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "Cd/H/Nd_Cd/H/Nd",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "Cd/H/Nd_Cd/H/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "Cd/H/S_Cd/H/Cd",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2 *2 C  0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    H  0 {2,S}
6    Cd 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "Thiophene3",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2 *2 C  0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    S  0 {1,S} {7,S}
5    H  0 {2,S}
6    Cd 0 {2,S} {7,D}
7    C  0 {4,S} {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "Cd/H/De_Cd/H/Nd",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "Cd/H/Cd_Cd/H/S",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2 *2 C  0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    H  0 {2,S}
6    S  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "Thiophene2",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2 *2 C  0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    Cd 0 {1,S} {7,D}
5    H  0 {2,S}
6    S  0 {2,S} {7,S}
7    C  0 {4,D} {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "Cd/H/De_Cd/H/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "Cd/monosub_Cd/disub",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cd  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "Cd/H/Nd_Cd/Nd2",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "Cd/H/Nd_Cd/Nd/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "Cd/H/Nd_Cd/De2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "Cd/H/De_Cd/Nd2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "Cd/H/De_Cd/Nd/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "Cd/H/De_Cd/De2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "Cd/disub_Cd/monosub",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cd  0 {1,D} {5,S} {6,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    H   0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "Cd/Nd2_Cd/H/Nd",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "Cd/Nd2_Cd/H/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "Cd/De2_Cd/H/Nd",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "Cd/De2_Cd/H/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "Cd/Nd/De_Cd/H/Nd",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "Cd/Nd/De_Cd/H/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "Cd/disub_Cd/disub",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cd  0 {1,D} {5,S} {6,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "Cd/Nd2_Cd/Nd2",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "Cd/Nd2_Cd/Nd/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "Cd/Nd2_Cd/De2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "Cd/Nd/De_Cd/Nd2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "Cd/Nd/De_Cd/Nd/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "Cd/Nd/De_Cd/De2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "Cd/De2_Cd/Nd2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "Cd/De2_Cd/Nd/De",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "Cd/De2_Cd/De2",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2 *2 C                0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "Sd_Cd",
    group = "OR{Sd_Cds, Sd_Cdd}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "Sd_Cdd",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,D}
3    R  0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "Sd_Cds",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    R  0 {2,S}
4    R  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "Sd_Cd/unsub",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "Sd_Cd/monosub",
    group = 
"""
1 *1 Sd  0 {2,D}
2 *2 Cd  0 {1,D} {3,S} {4,S}
3    H   0 {2,S}
4    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "Sd_Cd/H/Nd",
    group = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    H        0 {2,S}
4    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "Sd_Cd/H/De",
    group = 
"""
1 *1 Sd               0 {2,D}
2 *2 Cd               0 {1,D} {3,S} {4,S}
3    H                0 {2,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "Sd_Cd/H/Cb",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    Cb 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "Sd_Cd/disub",
    group = 
"""
1 *1 Sd  0 {2,D}
2 *2 Cd  0 {1,D} {3,S} {4,S}
3    R!H 0 {2,S}
4    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "Sd_Cd/Nd2",
    group = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    {Cs,O,S} 0 {2,S}
4    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "Sd_Cd/Nd/De",
    group = 
"""
1 *1 Sd               0 {2,D}
2 *2 Cd               0 {1,D} {3,S} {4,S}
3    {Cs,O,S}         0 {2,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "Sd_Cd/De2",
    group = 
"""
1 *1 Sd               0 {2,D}
2 *2 Cd               0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {2,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "H_OR",
    group = 
"""
1 *3 H                   0 {2,S}
2 *4 Os                  0 {1,S} {3,S}
3    {H,Cs,Cd,Sis,Sid,N} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "H_OH",
    group = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "H_OCs",
    group = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "H_OCmethyl",
    group = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "H_OCpri",
    group = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    C  0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "H_OCsec",
    group = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    C  0 {3,S}
6    C  0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "H_OCter",
    group = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {5,S} {6,S}
4    C  0 {3,S}
5    C  0 {3,S}
6    C  0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "H_OCd",
    group = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cd 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "H_OCdpri",
    group = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cd 0 {2,S} {4,D} {5,S}
4    Cd 0 {3,D}
5    H  0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "H_OCdsec",
    group = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cd 0 {2,S} {4,D} {5,S}
4    Cd 0 {3,D}
5    C  0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "R_OH",
    group = 
"""
1 *3 {Cs,Cd,Sis,Sid,N} 0 {2,S}
2 *4 Os                0 {1,S} {3,S}
3    H                 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "Cd_OH",
    group = 
"""
1 *3 Cd 0 {2,D} {3,S} {4,S}
2    Cd 0 {1,D}
3 *4 Os 0 {1,S} {5,S}
4    R  0 {1,S}
5    H  0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "Cd_pri_OH",
    group = 
"""
1 *3 Cd 0 {2,D} {3,S} {4,S}
2    Cd 0 {1,D}
3 *4 Os 0 {1,S} {5,S}
4    H  0 {1,S}
5    H  0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "Cd_sec_OH",
    group = 
"""
1 *3 Cd  0 {2,D} {3,S} {4,S}
2    Cd  0 {1,D}
3 *4 Os  0 {1,S} {5,S}
4    R!H 0 {1,S}
5    H   0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "Cs_OH",
    group = 
"""
1 *3 Cs     0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os     0 {1,S} {6,S}
3    {Cs,H} 0 {1,S}
4    {Cs,H} 0 {1,S}
5    {Cs,H} 0 {1,S}
6    H      0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "CH3OH",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os 0 {1,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    label = "C_pri_OH",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os 0 {1,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
6    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "C_sec_OH",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os 0 {1,S} {6,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
6    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    label = "C_ter_OH",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Os 0 {1,S} {6,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
6    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "N3d_N3d",
    group = 
"""
1 *1 N3d  0 {2,D}
2 *2 N3d 0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Dec 19 16:45:30 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 98,
    label = "N3d_Cd",
    group = 
"""
1 *1 N3d 0 {2,D}
2 *2 Cd  0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Dec 19 16:45:30 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
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

