#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["db", "doublebond"], products=["four_ring"], ownReverse=False)

reverse = "Four_Ring_Cleavage_Cd"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '-1', '*4'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*4'],
])

entry(
    index = 1,
    label = "db",
    group = "OR{db_2H, db_HNd, db_HDe, db_Nd2, db_NdDe, db_De2}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "doublebond",
    group = "OR{mb_db, mb_CO, mb_OC, mb_CCO, mb_COC}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "db_2H",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "db_2H_2H",
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "db_2H_monosub",
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "db_2H_HNd",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "db_2H_HDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "db_2H_disub",
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "db_2H_Nd2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "db_2H_NdDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "db_2H_De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "db_HNd",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    R!H    0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "db_HNd_monosub",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    R!H    0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "db_HNd_HNd",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "db_HNd_HDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "db_HNd_disub",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    R!H    0 {2,S}
6    R!H    0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "db_HNd_Nd2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "db_HNd_NdDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "db_HNd_De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "db_HDe",
    group = "OR{db_HDe_HDe, db_HDe_disub}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "db_HDe_HDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "db_HDe_disub",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    R!H           0 {2,S}
6    R!H           0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "db_HDe_Nd2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "db_HDe_NdDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "db_HDe_De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "db_Nd2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    R!H    0 {2,S}
6    R!H    0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "db_Nd2_Nd2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "db_Nd2_NdDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "db_Nd2_De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "db_NdDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    R!H           0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "db_NdDe_NdDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "db_NdDe_De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "db_De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "mb_db",
    group = 
"""
1 *3 Cd 0 {2,D}
2 *4 Cd 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "mb_db_2H",
    group = 
"""
1 *3 Cd 0 {2,D} {3,S} {4,S}
2 *4 Cd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "mb_db_2H_2H",
    group = 
"""
1 *3 Cd 0 {2,D} {3,S} {4,S}
2 *4 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "mb_db_2H_monosub",
    group = 
"""
1 *3 Cd  0 {2,D} {3,S} {4,S}
2 *4 Cd  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    H   0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "mb_db_2H_HNd",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "mb_db_2H_HDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "mb_db_2H_disub",
    group = 
"""
1 *3 Cd  0 {2,D} {3,S} {4,S}
2 *4 Cd  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    R!H 0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "mb_db_2H_Nd2",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "mb_db_2H_NdDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "mb_db_2H_De2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "mb_db_HNd",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "mb_db_HNd_2H",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    H      0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "mb_db_HNd_monosub",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    R!H    0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "mb_db_HNd_HNd",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "mb_db_HNd_HDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "mb_db_HNd_disub",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    R!H    0 {2,S}
6    R!H    0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "mb_db_HNd_Nd2",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "mb_db_HNd_NdDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "mb_db_HNd_De2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "mb_db_HDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "mb_db_HDe_2H",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "mb_db_HDe_monosub",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    R!H           0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "mb_db_HDe_HNd",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "mb_db_HDe_HDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "mb_db_HDe_disub",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    R!H           0 {2,S}
6    R!H           0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "mb_db_HDe_Nd2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "mb_db_HDe_NdDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "mb_db_HDe_De2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "mb_db_Nd2",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "mb_db_Nd2_2H",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    H      0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "mb_db_Nd2_monosub",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    R!H    0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "mb_db_Nd2_HNd",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "mb_db_Nd2_HDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "mb_db_Nd2_disub",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    R!H    0 {2,S}
6    R!H    0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "mb_db_Nd2_Nd2",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "mb_db_Nd2_NdDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "mb_db_Nd2_De2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "mb_db_NdDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "mb_db_NdDe_2H",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "mb_db_NdDe_monosub",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    R!H           0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "mb_db_NdDe_HNd",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "mb_db_NdDe_HDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "mb_db_NdDe_disub",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    R!H           0 {2,S}
6    R!H           0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "mb_db_NdDe_Nd2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "mb_db_NdDe_NdDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "mb_db_NdDe_De2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "mb_db_De2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "mb_db_De2_2H",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "mb_db_De2_monosub",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    R!H           0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "mb_db_De2_HNd",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "mb_db_De2_HDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "mb_db_De2_disub",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    R!H           0 {2,S}
6    R!H           0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "mb_db_De2_Nd2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "mb_db_De2_NdDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "mb_db_De2_De2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cd            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "mb_CO",
    group = 
"""
1 *3 CO 0 {2,D}
2 *4 Od 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "mb_CO_2H",
    group = 
"""
1 *3 CO 0 {2,D} {3,S} {4,S}
2 *4 Od 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "mb_CO_HNd",
    group = 
"""
1 *3 CO     0 {2,D} {3,S} {4,S}
2 *4 Od     0 {1,D}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "mb_CO_HDe",
    group = 
"""
1 *3 CO            0 {2,D} {3,S} {4,S}
2 *4 Od            0 {1,D}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "mb_CO_Nd2",
    group = 
"""
1 *3 CO     0 {2,D} {3,S} {4,S}
2 *4 Od     0 {1,D}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "mb_CO_NdDe",
    group = 
"""
1 *3 CO            0 {2,D} {3,S} {4,S}
2 *4 Od            0 {1,D}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "mb_CO_De2",
    group = 
"""
1 *3 CO            0 {2,D} {3,S} {4,S}
2 *4 Od            0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "mb_OC",
    group = 
"""
1 *3 Od 0 {2,D}
2 *4 CO 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "mb_OC_2H",
    group = 
"""
1 *3 Od 0 {2,D}
2 *4 CO 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "mb_OC_HNd",
    group = 
"""
1 *3 Od     0 {2,D}
2 *4 CO     0 {1,D} {3,S} {4,S}
3    H      0 {2,S}
4    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "mb_OC_HDe",
    group = 
"""
1 *3 Od            0 {2,D}
2 *4 CO            0 {1,D} {3,S} {4,S}
3    H             0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "mb_OC_Nd2",
    group = 
"""
1 *3 Od     0 {2,D}
2 *4 CO     0 {1,D} {3,S} {4,S}
3    {Cs,O} 0 {2,S}
4    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "mb_OC_NdDe",
    group = 
"""
1 *3 Od            0 {2,D}
2 *4 CO            0 {1,D} {3,S} {4,S}
3    {Cs,O}        0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "mb_OC_De2",
    group = 
"""
1 *3 Od            0 {2,D}
2 *4 CO            0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO} 0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "mb_CCO",
    group = 
"""
1 *3 Cd  0 {2,D}
2 *4 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "mb_CCO_2H",
    group = 
"""
1 *3 Cd  0 {2,D} {3,S} {4,S}
2 *4 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    Od  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "mb_CCO_HNd",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cdd    0 {1,D} {5,D}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    Od     0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "mb_CCO_HDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cdd           0 {1,D} {5,D}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "mb_CCO_Nd2",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cdd    0 {1,D} {5,D}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    Od     0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "mb_CCO_NdDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cdd           0 {1,D} {5,D}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "mb_CCO_De2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cdd           0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "mb_COC",
    group = 
"""
1 *3 Cdd 0 {2,D} {3,D}
2 *4 Cd  0 {1,D}
3    Od  0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "mb_COC_2H",
    group = 
"""
1 *3 Cdd 0 {2,D} {5,D}
2 *4 Cd  0 {1,D} {3,S} {4,S}
3    H   0 {2,S}
4    H   0 {2,S}
5    Od  0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "mb_COC_HNd",
    group = 
"""
1 *3 Cdd    0 {2,D} {5,D}
2 *4 Cd     0 {1,D} {3,S} {4,S}
3    H      0 {2,S}
4    {Cs,O} 0 {2,S}
5    Od     0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "mb_COC_HDe",
    group = 
"""
1 *3 Cdd           0 {2,D} {5,D}
2 *4 Cd            0 {1,D} {3,S} {4,S}
3    H             0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    Od            0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "mb_COC_Nd2",
    group = 
"""
1 *3 Cdd    0 {2,D} {5,D}
2 *4 Cd     0 {1,D} {3,S} {4,S}
3    {Cs,O} 0 {2,S}
4    {Cs,O} 0 {2,S}
5    Od     0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "mb_COC_NdDe",
    group = 
"""
1 *3 Cdd           0 {2,D} {5,D}
2 *4 Cd            0 {1,D} {3,S} {4,S}
3    {Cs,O}        0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    Od            0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "mb_COC_De2",
    group = 
"""
1 *3 Cdd           0 {2,D} {5,D}
2 *4 Cd            0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO} 0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    Od            0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
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
    L2: mb_db
        L3: mb_db_2H
            L4: mb_db_2H_2H
            L4: mb_db_2H_monosub
                L5: mb_db_2H_HNd
                L5: mb_db_2H_HDe
            L4: mb_db_2H_disub
                L5: mb_db_2H_Nd2
                L5: mb_db_2H_NdDe
                L5: mb_db_2H_De2
        L3: mb_db_HNd
            L4: mb_db_HNd_2H
            L4: mb_db_HNd_monosub
                L5: mb_db_HNd_HNd
                L5: mb_db_HNd_HDe
            L4: mb_db_HNd_disub
                L5: mb_db_HNd_Nd2
                L5: mb_db_HNd_NdDe
                L5: mb_db_HNd_De2
        L3: mb_db_HDe
            L4: mb_db_HDe_2H
            L4: mb_db_HDe_monosub
                L5: mb_db_HDe_HNd
                L5: mb_db_HDe_HDe
            L4: mb_db_HDe_disub
                L5: mb_db_HDe_Nd2
                L5: mb_db_HDe_NdDe
                L5: mb_db_HDe_De2
        L3: mb_db_Nd2
            L4: mb_db_Nd2_2H
            L4: mb_db_Nd2_monosub
                L5: mb_db_Nd2_HNd
                L5: mb_db_Nd2_HDe
            L4: mb_db_Nd2_disub
                L5: mb_db_Nd2_Nd2
                L5: mb_db_Nd2_NdDe
                L5: mb_db_Nd2_De2
        L3: mb_db_NdDe
            L4: mb_db_NdDe_2H
            L4: mb_db_NdDe_monosub
                L5: mb_db_NdDe_HNd
                L5: mb_db_NdDe_HDe
            L4: mb_db_NdDe_disub
                L5: mb_db_NdDe_Nd2
                L5: mb_db_NdDe_NdDe
                L5: mb_db_NdDe_De2
        L3: mb_db_De2
            L4: mb_db_De2_2H
            L4: mb_db_De2_monosub
                L5: mb_db_De2_HNd
                L5: mb_db_De2_HDe
            L4: mb_db_De2_disub
                L5: mb_db_De2_Nd2
                L5: mb_db_De2_NdDe
                L5: mb_db_De2_De2
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
"""
)

