#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["multiplebond", "elec_def"], products=["cycle"], ownReverse=False)

reverse = "Three_Ring_Cleavage"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*3'],
    ['LOSE_RADICAL', '*3', '2'],
])

entry(
    index = 1,
    label = "elec_def",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "multiplebond",
    group = "OR{mb_carbonyl, mb_db, mb_tb}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "o_atom",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U2 L2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "imidogen",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s U2 {2,S}
2    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "carbene",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U2 {2,S} {3,S}
2    H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "me_carbene",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U2 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {2,S}
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
    index = 6,
    label = "ph_carbene",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U2 {2,S} {3,S}
2    Cb U0 {1,S} {4,B} {5,B}
3    H  U0 {1,S}
4    Cb U0 {2,B} {6,B}
5    Cb U0 {2,B} {7,B}
6    Cb U0 {4,B} {8,B}
7    Cb U0 {5,B} {8,B}
8    Cb U0 {6,B} {7,B}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "dime_carbene",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U2 {2,S} {3,S}
2    Cs U0 {1,S} {4,S} {5,S} {6,S}
3    Cs U0 {1,S} {7,S} {8,S} {9,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    H  U0 {3,S}
8    H  U0 {3,S}
9    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "mb_carbonyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cdd,N} U0 {2,D}
2 *2 {O,N}      U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "mb_carbonyl_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO U0 {2,D} {3,S} {4,S}
2 *2 O  U0 {1,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "mb_carbonyl_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO     U0 {2,D} {3,S} {4,S}
2 *2 O      U0 {1,D}
3    H      U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "mb_carbonyl_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO            U0 {2,D} {3,S} {4,S}
2 *2 O             U0 {1,D}
3    H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "mb_carbonyl_NdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO     U0 {2,D} {3,S} {4,S}
2 *2 O      U0 {1,D}
3    {Cs,O} U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "mb_carbonyl_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO            U0 {2,D} {3,S} {4,S}
2 *2 O             U0 {1,D}
3    {Cs,O}        U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "mb_carbonyl_DeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO            U0 {2,D} {3,S} {4,S}
2 *2 O             U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "mb_db",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cdd,N} U0 {2,D}
2 *2 {Cd,Cdd,N} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "mb_db_dbSub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd      U0 {2,D} {3,D}
2 *2 Cd       U0 {1,D}
3    {Cd,Cdd} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "mb_db_unsub",
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
    index = 18,
    label = "mb_db_monosub",
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
    index = 19,
    label = "mb_db_monosub_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd     U0 {2,D} {3,S} {4,S}
2 *2 Cd     U0 {1,D} {5,S} {6,S}
3    H      U0 {1,S}
4    H      U0 {1,S}
5    H      U0 {2,S}
6    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "mb_db_monosub_De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    H             U0 {1,S}
5    H             U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "mb_db_onecdisub",
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
    index = 22,
    label = "mb_db_onecdisub_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd     U0 {2,D} {3,S} {4,S}
2 *2 Cd     U0 {1,D} {5,S} {6,S}
3    H      U0 {1,S}
4    H      U0 {1,S}
5    {Cs,O} U0 {2,S}
6    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "mb_db_onecdisub_oneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    H             U0 {1,S}
5    {Cs,O}        U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "mb_db_onecdisub_twoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    H             U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "mb_db_twocdisub",
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
    index = 26,
    label = "mb_db_twocdisub_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd     U0 {2,D} {3,S} {4,S}
2 *2 Cd     U0 {1,D} {5,S} {6,S}
3    H      U0 {1,S}
4    {Cs,O} U0 {1,S}
5    H      U0 {2,S}
6    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "mb_db_twocdisub_oneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    {Cs,O}        U0 {1,S}
5    H             U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "mb_db_twocdisub_twoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    H             U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "mb_db_trisub",
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
    index = 30,
    label = "mb_db_trisub_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd     U0 {2,D} {3,S} {4,S}
2 *2 Cd     U0 {1,D} {5,S} {6,S}
3    H      U0 {1,S}
4    {Cs,O} U0 {1,S}
5    {Cs,O} U0 {2,S}
6    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "mb_db_trisub_oneMDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cs,O}        U0 {2,S}
6    {Cs,O}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "mb_db_trisub_oneDDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    {Cs,O}        U0 {1,S}
5    {Cs,O}        U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "mb_db_trisub_onectwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    {Cs,O}        U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "mb_db_trisub_twoctwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cs,O}        U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "mb_db_trisub_threeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "mb_db_tetrasub",
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
    index = 37,
    label = "mb_db_tetrasub_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd     U0 {2,D} {3,S} {4,S}
2 *2 Cd     U0 {1,D} {5,S} {6,S}
3    {Cs,O} U0 {1,S}
4    {Cs,O} U0 {1,S}
5    {Cs,O} U0 {2,S}
6    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "mb_db_tetrasub_oneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    {Cs,O}        U0 {1,S}
4    {Cs,O}        U0 {1,S}
5    {Cs,O}        U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "mb_db_tetrasub_onectwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    {Cs,O}        U0 {1,S}
4    {Cs,O}        U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "mb_db_tetrasub_twoctwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    {Cs,O}        U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cs,O}        U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "mb_db_tetrasub_threeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    {Cs,O}        U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "mb_db_tetrasub_fourDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U0 {2,D} {3,S} {4,S}
2 *2 Cd            U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
6    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "mb_tb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Ct,N} U0 {2,T}
2 *2 {Ct,N} U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "mb_tb_unsub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    H  U0 {1,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "mb_tb_monosub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U0 {2,T} {3,S}
2 *2 Ct  U0 {1,T} {4,S}
3    R!H U0 {1,S}
4    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "mb_tb_monosub_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct      U0 {2,T} {3,S}
2 *2 Ct      U0 {1,T} {4,S}
3    {Cs,Os} U0 {1,S}
4    H       U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "mb_tb_disub",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U0 {2,T} {3,S}
2 *2 Ct  U0 {1,T} {4,S}
3    R!H U0 {1,S}
4    R!H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "mb_tb_disub_twoNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct      U0 {2,T} {3,S}
2 *2 Ct      U0 {1,T} {4,S}
3    {Cs,Os} U0 {1,S}
4    {Cs,Os} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: elec_def
    L2: o_atom
    L2: imidogen
    L2: carbene
    L2: me_carbene
    L2: ph_carbene
    L2: dime_carbene
L1: multiplebond
    L2: mb_carbonyl
        L3: mb_carbonyl_2H
        L3: mb_carbonyl_HNd
        L3: mb_carbonyl_HDe
        L3: mb_carbonyl_NdNd
        L3: mb_carbonyl_NdDe
        L3: mb_carbonyl_DeDe
    L2: mb_db
        L3: mb_db_dbSub
        L3: mb_db_unsub
        L3: mb_db_monosub
            L4: mb_db_monosub_Nd
            L4: mb_db_monosub_De
        L3: mb_db_onecdisub
            L4: mb_db_onecdisub_Nd
            L4: mb_db_onecdisub_oneDe
            L4: mb_db_onecdisub_twoDe
        L3: mb_db_twocdisub
            L4: mb_db_twocdisub_Nd
            L4: mb_db_twocdisub_oneDe
            L4: mb_db_twocdisub_twoDe
        L3: mb_db_trisub
            L4: mb_db_trisub_Nd
            L4: mb_db_trisub_oneMDe
            L4: mb_db_trisub_oneDDe
            L4: mb_db_trisub_onectwoDe
            L4: mb_db_trisub_twoctwoDe
            L4: mb_db_trisub_threeDe
        L3: mb_db_tetrasub
            L4: mb_db_tetrasub_Nd
            L4: mb_db_tetrasub_oneDe
            L4: mb_db_tetrasub_onectwoDe
            L4: mb_db_tetrasub_twoctwoDe
            L4: mb_db_tetrasub_threeDe
            L4: mb_db_tetrasub_fourDe
    L2: mb_tb
        L3: mb_tb_unsub
        L3: mb_tb_monosub
            L4: mb_tb_monosub_Nd
        L3: mb_tb_disub
            L4: mb_tb_disub_twoNd
"""
)

forbidden(
    label = "carbene_triplet",
    multiplicity = [3],
    group = 
"""
1 *1 C U2 {2,S} {3,S}
2    H U0 {1,S}
3    H U0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

