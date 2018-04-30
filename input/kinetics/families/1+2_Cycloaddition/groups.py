#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/groups"
shortDesc = u""
longDesc = u"""
Reaction site *3 should always be a singlet in this family.
"""

template(reactants=["multiplebond", "elec_def"], products=["cycle"], ownReverse=False)

reverse = "Three_Ring_Cleavage"

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['LOSE_PAIR', '*3', '1'],
])

entry(
    index = 1,
    label = "elec_def",
    group = "OR{carbene, me_carbene, dime_carbene, ph_carbene, o_atom_singlet, imidogen_singlet}",
    kinetics = None,
)

entry(
    index = 2,
    label = "multiplebond",
    group = "OR{mb_carbonyl, mb_db, mb_tb}",
    kinetics = None,
)

entry(
    index = 3,
    label = "o_atom_singlet",
    group = 
"""
1 *3 O u0 p3
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "carbene",
    group = 
"""
1 *3 C u0 p1 {2,S} {3,S}
2    H u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "me_carbene",
    group = 
"""
1 *3 C  u0 p1 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "ph_carbene",
    group = 
"""
1 *3 C  u0 p1 {2,S} {3,S}
2    Cb u0 {1,S} {4,B} {5,B}
3    H  u0 {1,S}
4    Cb u0 {2,B} {6,B}
5    Cb u0 {2,B} {7,B}
6    Cb u0 {4,B} {8,B}
7    Cb u0 {5,B} {8,B}
8    Cb u0 {6,B} {7,B}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "dime_carbene",
    group = 
"""
1 *3 C  u0 p1 {2,S} {3,S}
2    Cs u0 {1,S} {4,S} {5,S} {6,S}
3    Cs u0 {1,S} {7,S} {8,S} {9,S}
4    H  u0 {2,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    H  u0 {3,S}
8    H  u0 {3,S}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "imidogen_singlet",
    group = 
"""
1 *3 N1s u0 p2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "mb_carbonyl",
    group = 
"""
1 *1 [CO,Cdd,N] u0 {2,D}
2 *2 [O,N]      u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "mb_carbonyl_2H",
    group = 
"""
1 *1 CO u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "mb_carbonyl_HNd",
    group = 
"""
1 *1 CO     u0 {2,D} {3,S} {4,S}
2 *2 O      u0 {1,D}
3    H      u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "mb_carbonyl_HDe",
    group = 
"""
1 *1 CO            u0 {2,D} {3,S} {4,S}
2 *2 O             u0 {1,D}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "mb_carbonyl_NdNd",
    group = 
"""
1 *1 CO     u0 {2,D} {3,S} {4,S}
2 *2 O      u0 {1,D}
3    [Cs,O] u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "mb_carbonyl_NdDe",
    group = 
"""
1 *1 CO            u0 {2,D} {3,S} {4,S}
2 *2 O             u0 {1,D}
3    [Cs,O]        u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "mb_carbonyl_DeDe",
    group = 
"""
1 *1 CO            u0 {2,D} {3,S} {4,S}
2 *2 O             u0 {1,D}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "mb_db",
    group = 
"""
1 *1 [Cd,Cdd,N] u0 {2,D}
2 *2 [Cd,Cdd,N] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "mb_db_dbSub",
    group = 
"""
1 *1 Cdd      u0 {2,D} {3,D}
2 *2 Cd       u0 {1,D}
3    [Cd,Cdd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "mb_db_unsub",
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
    index = 18,
    label = "mb_db_monosub",
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
    index = 19,
    label = "mb_db_monosub_Nd",
    group = 
"""
1 *1 Cd     u0 {2,D} {3,S} {4,S}
2 *2 Cd     u0 {1,D} {5,S} {6,S}
3    H      u0 {1,S}
4    H      u0 {1,S}
5    H      u0 {2,S}
6    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "mb_db_monosub_De",
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
    index = 21,
    label = "mb_db_onecdisub",
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
    index = 22,
    label = "mb_db_onecdisub_Nd",
    group = 
"""
1 *1 Cd     u0 {2,D} {3,S} {4,S}
2 *2 Cd     u0 {1,D} {5,S} {6,S}
3    H      u0 {1,S}
4    H      u0 {1,S}
5    [Cs,O] u0 {2,S}
6    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "mb_db_onecdisub_oneDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    H             u0 {1,S}
5    [Cs,O]        u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "mb_db_onecdisub_twoDe",
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
    index = 25,
    label = "mb_db_twocdisub",
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
    index = 26,
    label = "mb_db_twocdisub_Nd",
    group = 
"""
1 *1 Cd     u0 {2,D} {3,S} {4,S}
2 *2 Cd     u0 {1,D} {5,S} {6,S}
3    H      u0 {1,S}
4    [Cs,O] u0 {1,S}
5    H      u0 {2,S}
6    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "mb_db_twocdisub_oneDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cs,O]        u0 {1,S}
5    H             u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "mb_db_twocdisub_twoDe",
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
    index = 29,
    label = "mb_db_trisub",
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
    index = 30,
    label = "mb_db_trisub_Nd",
    group = 
"""
1 *1 Cd     u0 {2,D} {3,S} {4,S}
2 *2 Cd     u0 {1,D} {5,S} {6,S}
3    H      u0 {1,S}
4    [Cs,O] u0 {1,S}
5    [Cs,O] u0 {2,S}
6    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "mb_db_trisub_oneMDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O]        u0 {2,S}
6    [Cs,O]        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "mb_db_trisub_oneDDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cs,O]        u0 {1,S}
5    [Cs,O]        u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "mb_db_trisub_onectwoDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cs,O]        u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "mb_db_trisub_twoctwoDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O]        u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "mb_db_trisub_threeDe",
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
    index = 36,
    label = "mb_db_tetrasub",
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
    index = 37,
    label = "mb_db_tetrasub_Nd",
    group = 
"""
1 *1 Cd     u0 {2,D} {3,S} {4,S}
2 *2 Cd     u0 {1,D} {5,S} {6,S}
3    [Cs,O] u0 {1,S}
4    [Cs,O] u0 {1,S}
5    [Cs,O] u0 {2,S}
6    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "mb_db_tetrasub_oneDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O]        u0 {1,S}
4    [Cs,O]        u0 {1,S}
5    [Cs,O]        u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "mb_db_tetrasub_onectwoDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O]        u0 {1,S}
4    [Cs,O]        u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "mb_db_tetrasub_twoctwoDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O]        u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O]        u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "mb_db_tetrasub_threeDe",
    group = 
"""
1 *1 Cd            u0 {2,D} {3,S} {4,S}
2 *2 Cd            u0 {1,D} {5,S} {6,S}
3    [Cs,O]        u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
6    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "mb_db_tetrasub_fourDe",
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
    index = 43,
    label = "mb_tb",
    group = 
"""
1 *1 [Ct,N] u0 {2,T}
2 *2 [Ct,N] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "mb_tb_unsub",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "mb_tb_monosub",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    R!H u0 {1,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "mb_tb_monosub_Nd",
    group = 
"""
1 *1 Ct      u0 {2,T} {3,S}
2 *2 Ct      u0 {1,T} {4,S}
3    [Cs,Os] u0 {1,S}
4    H       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "mb_tb_disub",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    R!H u0 {1,S}
4    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "mb_tb_disub_twoNd",
    group = 
"""
1 *1 Ct      u0 {2,T} {3,S}
2 *2 Ct      u0 {1,T} {4,S}
3    [Cs,Os] u0 {1,S}
4    [Cs,Os] u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: elec_def
    L2: o_atom_singlet
    L2: carbene
    L2: me_carbene
    L2: ph_carbene
    L2: dime_carbene
    L2: imidogen_singlet
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

