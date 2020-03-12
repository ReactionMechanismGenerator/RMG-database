#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/groups"
shortDesc = ""
longDesc = """
The reaction site *3 should be a triplet, otherwise it will react via the 1+2_Cycloaddition family instead.
"""

template(reactants=["R_R", "YJ"], products=["RJ_R_Y"], ownReverse=False)

reverse = "Beta_Scission"
reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 0,
    label = "R_R",
    group = 
"""
1 *1 R!H u0 {2,[D,T,B]}
2 *2 R!H u0 {1,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "YJ",
    group = "OR{HJ, Y_1centerquadrad, Y_1centertrirad, Y_1centerbirad, CJ, OJ, SJ, NJ}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Cb_Cb",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B}
2 *2 [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Cb-R!H_Cb",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *2 [Cb,Cbf] u0 {1,B}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Cb-R!H_Cb-R!H",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,B} {5,[S,B]}
2 *2 [Cb,Cbf] u0 {1,B} {4,B} {6,[S,B]}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {2,B}
5    R!H      u0 {1,[S,B]}
6    R!H      u0 {2,[S,B]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Cb-indane_Cb-indane",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,[S,B]} {6,B}
2 *2 Cb       u0 {1,B} {4,[S,B]} {7,B}
3    C        u0 {1,[S,B]} {5,[S,D,T]}
4    C        u0 {2,[S,B]} {5,[S,D,T]}
5    C        u0 {3,[S,D,T]} {4,[S,D,T]}
6    [Cb,Cbf] u0 {1,B}
7    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Cb-indeneDe_Cb-indeneNde",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,S} {6,B}
2 *2 Cb       u0 {1,B} {4,S} {7,B}
3    Cd       u0 {1,S} {5,D}
4    C        u0 {2,S} {5,S}
5    Cd       u0 {3,D} {4,S}
6    [Cb,Cbf] u0 {1,B}
7    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Cb-indeneNde_Cb-indene_De",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,S} {6,B}
2 *1 Cb       u0 {1,B} {4,S} {7,B}
3    Cd       u0 {1,S} {5,D}
4    C        u0 {2,S} {5,S}
5    Cd       u0 {3,D} {4,S}
6    [Cb,Cbf] u0 {1,B}
7    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Cb-benzofuranNde_Cb-benzofuranDe",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,S} {6,B}
2 *2 Cb       u0 {1,B} {4,S} {7,B}
3    O        u0 {1,S} {5,S}
4    C        u0 {2,S} {5,D}
5    C        u0 {3,S} {4,D}
6    [Cb,Cbf] u0 {1,B}
7    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Cb-tetralin_Cb-tetralin",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {7,B}
2 *2 [Cb,Cbf] u0 {1,B} {4,[S,B]} {8,B}
3    C        u0 {1,[S,B]} {5,[S,D,B]}
4    C        u0 {2,[S,B]} {6,[S,D,B]}
5    C        u0 {3,[S,D,B]} {6,[S,D,B]}
6    C        u0 {4,[S,D,B]} {5,[S,D,B]}
7    [Cb,Cbf] u0 {1,B}
8    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Cb-naphthalene_Cb-naphthalene",
    group = 
"""
1 *1 Cbf      u0 {2,B} {3,B} {7,B}
2 *2 Cbf      u0 {1,B} {4,B} {8,B}
3    [Cb,Cbf] u0 {1,B} {5,B}
4    [Cb,Cbf] u0 {2,B} {6,B}
5    [Cb,Cbf] u0 {3,B} {6,B}
6    [Cb,Cbf] u0 {4,B} {5,B}
7    [Cb,Cbf] u0 {1,B}
8    [Cb,Cbf] u0 {2,B}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Cb-R!H_Cbf-R!H",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,B} {5,[S,B]}
2 *2 Cbf      u0 {1,B} {4,B} {6,[S,B]}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {2,B}
5    R!H      u0 {1,[S,B]}
6    R!H      u0 {2,[S,B]}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Cb-R!/H_or_Val7/Cb-/H_or_Val7/",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *2 [Cb,Cbf] u0 {1,B} {5,S}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
5    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Cb-R!H_Cb-H",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *2 [Cb,Cbf] u0 {1,B} {5,S}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Cb-C-cyclic_Cb-H",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {6,B}
2    [Cb,Cbf] u0 {1,B} {5,[S,B]}
3    C        u0 {1,[S,B]} {4,[S,D,T,B]}
4    C        u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
5    C        u0 {2,[S,B]} {7,[S,D,T,B]}
6 *2 Cb       u0 {1,B} {8,S}
7    C        u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
8    H        u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Cbf-Cb-cyclic_Cb-H",
    group = 
"""
1 *1 Cbf      u0 {2,B} {3,B} {6,B}
2    Cbf      u0 {1,B} {5,B}
3    [Cb,Cbf] u0 {1,B} {4,B}
4    [Cb,Cbf] u0 {3,B} {7,B}
5    [Cb,Cbf] u0 {2,B} {7,B}
6 *2 Cb       u0 {1,B} {8,S}
7    [Cb,Cbf] u0 {4,B} {5,B}
8    H        u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Cb-Cd_Cb-H",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S} {4,B}
2 *2 Cb u0 {1,B} {5,S}
3    Cd u0 {1,S}
4    Cb u0 {1,B}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Cb-Cs_Cb-H",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S} {4,B}
2 *2 Cb u0 {1,B} {5,S}
3    Cs u0 {1,S}
4    Cb u0 {1,B}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Cb-R!H_Cb-H-F",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *2 [Cb,Cbf] u0 {1,B} {5,S}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
5    F1s      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Cb-C-cyclic_Cb-H-F",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {6,B}
2    [Cb,Cbf] u0 {1,B} {5,[S,B]}
3    C        u0 {1,[S,B]} {4,[S,D,T,B]}
4    C        u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
5    C        u0 {2,[S,B]} {7,[S,D,T,B]}
6 *2 Cb       u0 {1,B} {8,S}
7    C        u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
8    F1s      u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Cbf-Cb-cyclic_Cb-H-F",
    group = 
"""
1 *1 Cbf      u0 {2,B} {3,B} {6,B}
2    Cbf      u0 {1,B} {5,B}
3    [Cb,Cbf] u0 {1,B} {4,B}
4    [Cb,Cbf] u0 {3,B} {7,B}
5    [Cb,Cbf] u0 {2,B} {7,B}
6 *2 Cb       u0 {1,B} {8,S}
7    [Cb,Cbf] u0 {4,B} {5,B}
8    F1s      u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Cb-Cd_Cb-H-F",
    group = 
"""
1 *1 Cb  u0 {2,B} {3,S} {4,B}
2 *2 Cb  u0 {1,B} {5,S}
3    Cd  u0 {1,S}
4    Cb  u0 {1,B}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Cb-Cs_Cb-H-F",
    group = 
"""
1 *1 Cb  u0 {2,B} {3,S} {4,B}
2 *2 Cb  u0 {1,B} {5,S}
3    Cs  u0 {1,S}
4    Cb  u0 {1,B}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Cb-R!H_Cb-H-Cl",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *2 [Cb,Cbf] u0 {1,B} {5,S}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
5    Cl1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Cb-C-cyclic_Cb-H-Cl",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {6,B}
2    [Cb,Cbf] u0 {1,B} {5,[S,B]}
3    C        u0 {1,[S,B]} {4,[S,D,T,B]}
4    C        u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
5    C        u0 {2,[S,B]} {7,[S,D,T,B]}
6 *2 Cb       u0 {1,B} {8,S}
7    C        u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
8    Cl1s     u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Cbf-Cb-cyclic_Cb-H-Cl",
    group = 
"""
1 *1 Cbf      u0 {2,B} {3,B} {6,B}
2    Cbf      u0 {1,B} {5,B}
3    [Cb,Cbf] u0 {1,B} {4,B}
4    [Cb,Cbf] u0 {3,B} {7,B}
5    [Cb,Cbf] u0 {2,B} {7,B}
6 *2 Cb       u0 {1,B} {8,S}
7    [Cb,Cbf] u0 {4,B} {5,B}
8    Cl1s     u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "Cb-Cd_Cb-H-Cl",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S} {4,B}
2 *2 Cb   u0 {1,B} {5,S}
3    Cd   u0 {1,S}
4    Cb   u0 {1,B}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Cb-Cs_Cb-H-Cl",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S} {4,B}
2 *2 Cb   u0 {1,B} {5,S}
3    Cs   u0 {1,S}
4    Cb   u0 {1,B}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Cb-R!H_Cb-H-Br",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *2 [Cb,Cbf] u0 {1,B} {5,S}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
5    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Cb-C-cyclic_Cb-H-Br",
    group = 
"""
1 *1 [Cb,Cbf] u0 {2,B} {3,[S,B]} {6,B}
2    [Cb,Cbf] u0 {1,B} {5,[S,B]}
3    C        u0 {1,[S,B]} {4,[S,D,T,B]}
4    C        u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
5    C        u0 {2,[S,B]} {7,[S,D,T,B]}
6 *2 Cb       u0 {1,B} {8,S}
7    C        u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
8    Br1s     u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Cbf-Cb-cyclic_Cb-H-Br",
    group = 
"""
1 *1 Cbf      u0 {2,B} {3,B} {6,B}
2    Cbf      u0 {1,B} {5,B}
3    [Cb,Cbf] u0 {1,B} {4,B}
4    [Cb,Cbf] u0 {3,B} {7,B}
5    [Cb,Cbf] u0 {2,B} {7,B}
6 *2 Cb       u0 {1,B} {8,S}
7    [Cb,Cbf] u0 {4,B} {5,B}
8    Br1s     u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Cb-Cd_Cb-H-Br",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S} {4,B}
2 *2 Cb   u0 {1,B} {5,S}
3    Cd   u0 {1,S}
4    Cb   u0 {1,B}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Cb-Cs_Cb-H-Br",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S} {4,B}
2 *2 Cb   u0 {1,B} {5,S}
3    Cs   u0 {1,S}
4    Cb   u0 {1,B}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Cb-/H_or_Val7/Cb",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 [Cb,Cbf] u0 {1,B}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Cb-H_Cb",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 [Cb,Cbf] u0 {1,B}
3    H        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Cb-H_Cb-R!H",
    group = 
"""
1 *2 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "Cb-H_Cb-indeneNde",
    group = 
"""
1 *2 Cb u0 {2,B} {3,S} {6,B}
2    Cb u0 {1,B} {4,S}
3    C  u0 {1,S} {5,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {3,S} {4,D}
6 *1 Cb u0 {1,B} {7,S}
7    H  u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "Cb-H_Cbf-Cb",
    group = 
"""
1 *2 Cbf      u0 {2,B} {3,B} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {1,B}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Cb-H-Ortho_Cb-C",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,S} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    C        u0 {1,S}
4    [Cb,Cbf] u0 {1,B}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "Cb-H-Ortho_Cb-C-fused",
    group = 
"""
1 *2 Cb  u0 {2,B} {3,S} {4,B}
2 *1 Cb  u0 {1,B} {5,S}
3    C   u0 {1,S}
4    Cbf u0 {1,B}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "Cb-H_Cb-H",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Cb-H-Meta_Cb-H",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    H        u0 {1,S}
5    R!H      u0 {3,S}
6    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Cb-H-Para_Cb-H",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    H        u0 {1,S}
6    H        u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "Cb-H-Para_Cb-H-fused",
    group = 
"""
1     Cbf u0 {2,B} {3,B} {9,B}
2  *1 Cb  u0 {1,B} {4,B} {7,S}
3     Cbf u0 {1,B} {5,B} {8,B}
4  *2 Cb  u0 {2,B} {6,B} {11,S}
5     Cb  u0 {3,B} {6,B} {10,S}
6     Cb  u0 {4,B} {5,B}
7     H   u0 {2,S}
8     Cb  u0 {3,B}
9     Cb  u0 {1,B}
10    R!H u0 {5,S}
11    H   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Cb-H_Cb-H_o_ketene",
    group = 
"""
1 *1 Cb  u0 {2,B} {4,B} {6,S}
2    Cb  u0 {1,B} {3,S}
3    Cd  u0 {2,S} {5,D}
4 *2 Cb  u0 {1,B} {7,S}
5    Cdd u0 {3,D} {8,D}
6    H   u0 {1,S}
7    H   u0 {4,S}
8    O   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Cb-H_Cb-CbfH",
    group = 
"""
1 *2 Cb  u0 {2,B} {3,S} {4,B}
2 *1 Cb  u0 {1,B} {5,S}
3    H   u0 {1,S}
4    Cbf u0 {1,B}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Cb-H_Cb-H-HF",
    group = 
"""
1 *1 Cb  u0 {2,B} {3,S}
2 *2 Cb  u0 {1,B} {4,S}
3    H   u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Cb-H_Cb-H_o_ketene-HF",
    group = 
"""
1 *1 Cb  u0 {2,B} {4,B} {6,S}
2    Cb  u0 {1,B} {3,S}
3    Cd  u0 {2,S} {5,D}
4 *2 Cb  u0 {1,B} {7,S}
5    Cdd u0 {3,D} {8,D}
6    H   u0 {1,S}
7    F1s u0 {4,S}
8    O   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Cb-H_Cb-CbfH-HF",
    group = 
"""
1 *2 Cb  u0 {2,B} {3,S} {4,B}
2 *1 Cb  u0 {1,B} {5,S}
3    F1s u0 {1,S}
4    Cbf u0 {1,B}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Cb-H_Cb-H-HCl",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S}
2 *2 Cb   u0 {1,B} {4,S}
3    H    u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Cb-H_Cb-H_o_ketene-HCl",
    group = 
"""
1 *1 Cb   u0 {2,B} {4,B} {6,S}
2    Cb   u0 {1,B} {3,S}
3    Cd   u0 {2,S} {5,D}
4 *2 Cb   u0 {1,B} {7,S}
5    Cdd  u0 {3,D} {8,D}
6    H    u0 {1,S}
7    Cl1s u0 {4,S}
8    O    u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Cb-H_Cb-CbfH-HCl",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {4,B}
2 *1 Cb   u0 {1,B} {5,S}
3    Cl1s u0 {1,S}
4    Cbf  u0 {1,B}
5    H    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Cb-H_Cb-H-HBr",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S}
2 *2 Cb   u0 {1,B} {4,S}
3    H    u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Cb-H_Cb-H_o_ketene-HBr",
    group = 
"""
1 *1 Cb   u0 {2,B} {4,B} {6,S}
2    Cb   u0 {1,B} {3,S}
3    Cd   u0 {2,S} {5,D}
4 *2 Cb   u0 {1,B} {7,S}
5    Cdd  u0 {3,D} {8,D}
6    H    u0 {1,S}
7    Br1s u0 {4,S}
8    O    u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Cb-H_Cb-CbfH-HBr",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {4,B}
2 *1 Cb   u0 {1,B} {5,S}
3    Br1s u0 {1,S}
4    Cbf  u0 {1,B}
5    H    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Cb-H_Cb-F",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 [Cb,Cbf] u0 {1,B}
3    F1s      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Cb-H_Cb-R!H-F",
    group = 
"""
1 *2 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
5    F1s      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Cb-H_Cb-indeneNde-F",
    group = 
"""
1 *2 Cb  u0 {2,B} {3,S} {6,B}
2    Cb  u0 {1,B} {4,S}
3    C   u0 {1,S} {5,S}
4    Cd  u0 {2,S} {5,D}
5    Cd  u0 {3,S} {4,D}
6 *1 Cb  u0 {1,B} {7,S}
7    F1s u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Cb-H_Cbf-Cb-F",
    group = 
"""
1 *2 Cbf      u0 {2,B} {3,B} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {1,B}
5    F1s      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Cb-H-Ortho_Cb-C-F",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,S} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    C        u0 {1,S}
4    [Cb,Cbf] u0 {1,B}
5    F1s      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Cb-H-Ortho_Cb-C-fused-F",
    group = 
"""
1 *2 Cb  u0 {2,B} {3,S} {4,B}
2 *1 Cb  u0 {1,B} {5,S}
3    C   u0 {1,S}
4    Cbf u0 {1,B}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cb-H_Cb-H-FF",
    group = 
"""
1 *1 Cb  u0 {2,B} {3,S}
2 *2 Cb  u0 {1,B} {4,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Cb-H-Meta_Cb-H-FF",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    F1s      u0 {1,S}
5    R!H      u0 {3,S}
6    F1s      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Cb-H-Para_Cb-H-FF",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    F1s      u0 {1,S}
6    F1s      u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Cb-H-Para_Cb-H-fused-FF",
    group = 
"""
1     Cbf u0 {2,B} {3,B} {9,B}
2  *1 Cb  u0 {1,B} {4,B} {7,S}
3     Cbf u0 {1,B} {5,B} {8,B}
4  *2 Cb  u0 {2,B} {6,B} {11,S}
5     Cb  u0 {3,B} {6,B} {10,S}
6     Cb  u0 {4,B} {5,B}
7     F1s u0 {2,S}
8     Cb  u0 {3,B}
9     Cb  u0 {1,B}
10    R!H u0 {5,S}
11    F1s u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Cb-H_Cb-H_o_ketene-FF",
    group = 
"""
1 *1 Cb  u0 {2,B} {4,B} {6,S}
2    Cb  u0 {1,B} {3,S}
3    Cd  u0 {2,S} {5,D}
4 *2 Cb  u0 {1,B} {7,S}
5    Cdd u0 {3,D} {8,D}
6    F1s u0 {1,S}
7    F1s u0 {4,S}
8    O   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Cb-H_Cb-CbfH-FF",
    group = 
"""
1 *2 Cb  u0 {2,B} {3,S} {4,B}
2 *1 Cb  u0 {1,B} {5,S}
3    F1s u0 {1,S}
4    Cbf u0 {1,B}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Cb-H_Cb-H-FCl",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S}
2 *2 Cb   u0 {1,B} {4,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Cb-H_Cb-H_o_ketene-FCl",
    group = 
"""
1 *1 Cb   u0 {2,B} {4,B} {6,S}
2    Cb   u0 {1,B} {3,S}
3    Cd   u0 {2,S} {5,D}
4 *2 Cb   u0 {1,B} {7,S}
5    Cdd  u0 {3,D} {8,D}
6    F1s  u0 {1,S}
7    Cl1s u0 {4,S}
8    O    u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Cb-H_Cb-CbfH-FCl",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {4,B}
2 *1 Cb   u0 {1,B} {5,S}
3    Cl1s u0 {1,S}
4    Cbf  u0 {1,B}
5    F1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Cb-H_Cb-H-FBr",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S}
2 *2 Cb   u0 {1,B} {4,S}
3    F1s  u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Cb-H_Cb-H_o_ketene-FBr",
    group = 
"""
1 *1 Cb   u0 {2,B} {4,B} {6,S}
2    Cb   u0 {1,B} {3,S}
3    Cd   u0 {2,S} {5,D}
4 *2 Cb   u0 {1,B} {7,S}
5    Cdd  u0 {3,D} {8,D}
6    F1s  u0 {1,S}
7    Br1s u0 {4,S}
8    O    u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Cb-H_Cb-CbfH-FBr",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {4,B}
2 *1 Cb   u0 {1,B} {5,S}
3    Br1s u0 {1,S}
4    Cbf  u0 {1,B}
5    F1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Cb-H-Meta_Cb-H-HF",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    H        u0 {1,S}
5    R!H      u0 {3,S}
6    F1s      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Cb-H-Para_Cb-H-HF",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    H        u0 {1,S}
6    F1s      u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Cb-H-Para_Cb-H-fused-HF",
    group = 
"""
1     Cbf u0 {2,B} {3,B} {9,B}
2  *1 Cb  u0 {1,B} {4,B} {7,S}
3     Cbf u0 {1,B} {5,B} {8,B}
4  *2 Cb  u0 {2,B} {6,B} {11,S}
5     Cb  u0 {3,B} {6,B} {10,S}
6     Cb  u0 {4,B} {5,B}
7     F1s u0 {2,S}
8     Cb  u0 {3,B}
9     Cb  u0 {1,B}
10    R!H u0 {5,S}
11    H   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Cb-H_Cb-Cl",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 [Cb,Cbf] u0 {1,B}
3    Cl1s     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Cb-H_Cb-R!H-Cl",
    group = 
"""
1 *2 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
5    Cl1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Cb-H_Cb-indeneNde-Cl",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {6,B}
2    Cb   u0 {1,B} {4,S}
3    C    u0 {1,S} {5,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6 *1 Cb   u0 {1,B} {7,S}
7    Cl1s u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Cb-H_Cbf-Cb-Cl",
    group = 
"""
1 *2 Cbf      u0 {2,B} {3,B} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {1,B}
5    Cl1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Cb-H-Ortho_Cb-C-Cl",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,S} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    C        u0 {1,S}
4    [Cb,Cbf] u0 {1,B}
5    Cl1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Cb-H-Ortho_Cb-C-fused-Cl",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {4,B}
2 *1 Cb   u0 {1,B} {5,S}
3    C    u0 {1,S}
4    Cbf  u0 {1,B}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Cb-H_Cb-H-ClCl",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S}
2 *2 Cb   u0 {1,B} {4,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Cb-H-Meta_Cb-H-ClCl",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    Cl1s     u0 {1,S}
5    R!H      u0 {3,S}
6    Cl1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Cb-H-Para_Cb-H-ClCl",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    Cl1s     u0 {1,S}
6    Cl1s     u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Cb-H-Para_Cb-H-fused-ClCl",
    group = 
"""
1     Cbf  u0 {2,B} {3,B} {9,B}
2  *1 Cb   u0 {1,B} {4,B} {7,S}
3     Cbf  u0 {1,B} {5,B} {8,B}
4  *2 Cb   u0 {2,B} {6,B} {11,S}
5     Cb   u0 {3,B} {6,B} {10,S}
6     Cb   u0 {4,B} {5,B}
7     Cl1s u0 {2,S}
8     Cb   u0 {3,B}
9     Cb   u0 {1,B}
10    R!H  u0 {5,S}
11    Cl1s u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Cb-H_Cb-H_o_ketene-ClCl",
    group = 
"""
1 *1 Cb   u0 {2,B} {4,B} {6,S}
2    Cb   u0 {1,B} {3,S}
3    Cd   u0 {2,S} {5,D}
4 *2 Cb   u0 {1,B} {7,S}
5    Cdd  u0 {3,D} {8,D}
6    Cl1s u0 {1,S}
7    Cl1s u0 {4,S}
8    O    u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Cb-H_Cb-CbfH-ClCl",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {4,B}
2 *1 Cb   u0 {1,B} {5,S}
3    Cl1s u0 {1,S}
4    Cbf  u0 {1,B}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Cb-H_Cb-H-ClBr",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S}
2 *2 Cb   u0 {1,B} {4,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Cb-H_Cb-H_o_ketene-ClBr",
    group = 
"""
1 *1 Cb   u0 {2,B} {4,B} {6,S}
2    Cb   u0 {1,B} {3,S}
3    Cd   u0 {2,S} {5,D}
4 *2 Cb   u0 {1,B} {7,S}
5    Cdd  u0 {3,D} {8,D}
6    Cl1s u0 {1,S}
7    Br1s u0 {4,S}
8    O    u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "Cb-H_Cb-CbfH-ClBr",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {4,B}
2 *1 Cb   u0 {1,B} {5,S}
3    Br1s u0 {1,S}
4    Cbf  u0 {1,B}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "Cb-H-Meta_Cb-H-HCl",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    H        u0 {1,S}
5    R!H      u0 {3,S}
6    Cl1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "Cb-H-Meta_Cb-H-FCl",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    F1s      u0 {1,S}
5    R!H      u0 {3,S}
6    Cl1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "Cb-H-Para_Cb-H-HCl",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    H        u0 {1,S}
6    Cl1s     u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "Cb-H-Para_Cb-H-fused-HCl",
    group = 
"""
1     Cbf  u0 {2,B} {3,B} {9,B}
2  *1 Cb   u0 {1,B} {4,B} {7,S}
3     Cbf  u0 {1,B} {5,B} {8,B}
4  *2 Cb   u0 {2,B} {6,B} {11,S}
5     Cb   u0 {3,B} {6,B} {10,S}
6     Cb   u0 {4,B} {5,B}
7     Cl1s u0 {2,S}
8     Cb   u0 {3,B}
9     Cb   u0 {1,B}
10    R!H  u0 {5,S}
11    H    u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "Cb-H-Para_Cb-H-FCl",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    F1s      u0 {1,S}
6    Cl1s     u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "Cb-H-Para_Cb-H-fused-FCl",
    group = 
"""
1     Cbf  u0 {2,B} {3,B} {9,B}
2  *1 Cb   u0 {1,B} {4,B} {7,S}
3     Cbf  u0 {1,B} {5,B} {8,B}
4  *2 Cb   u0 {2,B} {6,B} {11,S}
5     Cb   u0 {3,B} {6,B} {10,S}
6     Cb   u0 {4,B} {5,B}
7     Cl1s u0 {2,S}
8     Cb   u0 {3,B}
9     Cb   u0 {1,B}
10    R!H  u0 {5,S}
11    F1s  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Cb-H_Cb-Br",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,S}
2 *2 [Cb,Cbf] u0 {1,B}
3    Br1s     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Cb-H_Cb-R!H-Br",
    group = 
"""
1 *2 [Cb,Cbf] u0 {2,B} {3,[S,B]} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    R!H      u0 {1,[S,B]}
4    [Cb,Cbf] u0 {1,B}
5    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "Cb-H_Cb-indeneNde-Br",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {6,B}
2    Cb   u0 {1,B} {4,S}
3    C    u0 {1,S} {5,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6 *1 Cb   u0 {1,B} {7,S}
7    Br1s u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "Cb-H_Cbf-Cb-Br",
    group = 
"""
1 *2 Cbf      u0 {2,B} {3,B} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    [Cb,Cbf] u0 {1,B}
4    [Cb,Cbf] u0 {1,B}
5    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "Cb-H-Ortho_Cb-C-Br",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,S} {4,B}
2 *1 Cb       u0 {1,B} {5,S}
3    C        u0 {1,S}
4    [Cb,Cbf] u0 {1,B}
5    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "Cb-H-Ortho_Cb-C-fused-Br",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {4,B}
2 *1 Cb   u0 {1,B} {5,S}
3    C    u0 {1,S}
4    Cbf  u0 {1,B}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Cb-H_Cb-H-BrBr",
    group = 
"""
1 *1 Cb   u0 {2,B} {3,S}
2 *2 Cb   u0 {1,B} {4,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Cb-H-Meta_Cb-H-BrBr",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    Br1s     u0 {1,S}
5    R!H      u0 {3,S}
6    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "Cb-H-Para_Cb-H-BrBr",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    Br1s     u0 {1,S}
6    Br1s     u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "Cb-H-Para_Cb-H-fused-BrBr",
    group = 
"""
1     Cbf  u0 {2,B} {3,B} {9,B}
2  *1 Cb   u0 {1,B} {4,B} {7,S}
3     Cbf  u0 {1,B} {5,B} {8,B}
4  *2 Cb   u0 {2,B} {6,B} {11,S}
5     Cb   u0 {3,B} {6,B} {10,S}
6     Cb   u0 {4,B} {5,B}
7     Br1s u0 {2,S}
8     Cb   u0 {3,B}
9     Cb   u0 {1,B}
10    R!H  u0 {5,S}
11    Br1s u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Cb-H_Cb-H_o_ketene-BrBr",
    group = 
"""
1 *1 Cb   u0 {2,B} {4,B} {6,S}
2    Cb   u0 {1,B} {3,S}
3    Cd   u0 {2,S} {5,D}
4 *2 Cb   u0 {1,B} {7,S}
5    Cdd  u0 {3,D} {8,D}
6    Br1s u0 {1,S}
7    Br1s u0 {4,S}
8    O    u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "Cb-H_Cb-CbfH-BrBr",
    group = 
"""
1 *2 Cb   u0 {2,B} {3,S} {4,B}
2 *1 Cb   u0 {1,B} {5,S}
3    Br1s u0 {1,S}
4    Cbf  u0 {1,B}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "Cb-H-Meta_Cb-H-HBr",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    H        u0 {1,S}
5    R!H      u0 {3,S}
6    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "Cb-H-Meta_Cb-H-FBr",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    F1s      u0 {1,S}
5    R!H      u0 {3,S}
6    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Cb-H-Meta_Cb-H-ClBr",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2 *1 Cb       u0 {1,B} {6,S}
3    [Cb,Cbf] u0 {1,B} {5,S}
4    Cl1s     u0 {1,S}
5    R!H      u0 {3,S}
6    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "Cb-H-Para_Cb-H-HBr",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    H        u0 {1,S}
6    Br1s     u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "Cb-H-Para_Cb-H-fused-HBr",
    group = 
"""
1     Cbf  u0 {2,B} {3,B} {9,B}
2  *1 Cb   u0 {1,B} {4,B} {7,S}
3     Cbf  u0 {1,B} {5,B} {8,B}
4  *2 Cb   u0 {2,B} {6,B} {11,S}
5     Cb   u0 {3,B} {6,B} {10,S}
6     Cb   u0 {4,B} {5,B}
7     Br1s u0 {2,S}
8     Cb   u0 {3,B}
9     Cb   u0 {1,B}
10    R!H  u0 {5,S}
11    H    u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "Cb-H-Para_Cb-H-FBr",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    F1s      u0 {1,S}
6    Br1s     u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "Cb-H-Para_Cb-H-fused-FBr",
    group = 
"""
1     Cbf  u0 {2,B} {3,B} {9,B}
2  *1 Cb   u0 {1,B} {4,B} {7,S}
3     Cbf  u0 {1,B} {5,B} {8,B}
4  *2 Cb   u0 {2,B} {6,B} {11,S}
5     Cb   u0 {3,B} {6,B} {10,S}
6     Cb   u0 {4,B} {5,B}
7     Br1s u0 {2,S}
8     Cb   u0 {3,B}
9     Cb   u0 {1,B}
10    R!H  u0 {5,S}
11    F1s  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "Cb-H-Para_Cb-H-ClBr",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {5,S}
2    [Cb,Cbf] u0 {1,B} {4,B}
3 *1 Cb       u0 {1,B} {6,S}
4    [Cb,Cbf] u0 {2,B} {7,S}
5    Cl1s     u0 {1,S}
6    Br1s     u0 {3,S}
7    R!H      u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "Cb-H-Para_Cb-H-fused-ClBr",
    group = 
"""
1     Cbf  u0 {2,B} {3,B} {9,B}
2  *1 Cb   u0 {1,B} {4,B} {7,S}
3     Cbf  u0 {1,B} {5,B} {8,B}
4  *2 Cb   u0 {2,B} {6,B} {11,S}
5     Cb   u0 {3,B} {6,B} {10,S}
6     Cb   u0 {4,B} {5,B}
7     Br1s u0 {2,S}
8     Cb   u0 {3,B}
9     Cb   u0 {1,B}
10    R!H  u0 {5,S}
11    Cl1s u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "Cd_R",
    group = 
"""
1 *1 C   u0 {2,D}
2 *2 R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Cdd_Od",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "CO2",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "Ck_O",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "C=S_O",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    S   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "Cdd_Od-N3d",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "CO_O",
    group = 
"""
1 *1 CO  u0 {2,D}
2 *2 O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "CO-/H_or_Val7/H_or_Val7/O",
    group = 
"""
1 *1 CO       u0 {2,D} {3,S} {4,S}
2 *2 O2d      u0 {1,D}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "CO-HH_O",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "CO-HH_O-HF",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "CO-HH_O-HCl",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "CO-HH_O-HBr",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "CO-HH_O-FF",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "CO-HH_O-FCl",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "CO-HH_O-FBr",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "CO-HH_O-ClCl",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "CO-HH_O-ClBr",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "CO-HH_O-BrBr",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "CO-Nd/H_or_Val7/O",
    group = 
"""
1 *1 CO           u0 {2,D} {3,S} {4,S}
2 *2 O2d          u0 {1,D}
3    [H,Val7]     u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "CO-NdH_O",
    group = 
"""
1 *1 CO           u0 {2,D} {3,S} {4,S}
2 *2 O2d          u0 {1,D}
3    H            u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "CO-CsH_O",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "CO-NdH_O-F",
    group = 
"""
1 *1 CO           u0 {2,D} {3,S} {4,S}
2 *2 O2d          u0 {1,D}
3    F1s          u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "CO-CsH_O-F",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "CO-NdH_O-Cl",
    group = 
"""
1 *1 CO           u0 {2,D} {3,S} {4,S}
2 *2 O2d          u0 {1,D}
3    Cl1s         u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "CO-CsH_O-Cl",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "CO-NdH_O-Br",
    group = 
"""
1 *1 CO           u0 {2,D} {3,S} {4,S}
2 *2 O2d          u0 {1,D}
3    Br1s         u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "CO-CsH_O-Br",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "CO-De/H_or_Val7/O",
    group = 
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    [H,Val7]                  u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "CO-DeH_O",
    group = 
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "CO-CdH_O",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
4    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "CO-CtH_O",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "CO-DeH_O-F",
    group = 
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    F1s                       u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "CO-CdH_O-F",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    F1s u0 {1,S}
4    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "CO-CtH_O-F",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    F1s u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "CO-DeH_O-Cl",
    group = 
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    Cl1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "CO-CdH_O-Cl",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    Cl1s u0 {1,S}
4    Cd   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "CO-CtH_O-Cl",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "CO-DeH_O-Br",
    group = 
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    Br1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "CO-CdH_O-Br",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    Br1s u0 {1,S}
4    Cd   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "CO-CtH_O-Br",
    group = 
"""
1 *1 CO   u0 {2,D} {3,S} {4,S}
2 *2 O2d  u0 {1,D}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "CO-NdNd_O",
    group = 
"""
1 *1 CO           u0 {2,D} {3,S} {4,S}
2 *2 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "CO-CsCs_O",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "CO-DeNd_O",
    group = 
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    [Cs,O2s,S2s]              u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "CO-CdCs_O",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "CO-CtCs_O",
    group = 
"""
1 *1 CO  u0 {2,D} {3,S} {4,S}
2 *2 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "CO-DeDe_O",
    group = 
"""
1 *1 CO                        u0 {2,D} {3,S} {4,S}
2 *2 O2d                       u0 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Cdd_Sd",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 S2d u0 p2 {1,D}
3    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "Cdd-Sd_Sd",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 S2d u0 p2 {1,D}
3    S2d u0 p2 {1,D}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Cds_Cdd",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    R   ux {1,S}
4    R   ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Cds_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    R   ux {1,S}
4    R   ux {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "Cds-/H_or_Val7/H_or_Val7/Ca",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cdd      u0 {1,D} {5,D}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    C        u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "Cds-HH_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "Cds-HH_Ca-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "Cds-HH_Ca-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "Cds-HH_Ca-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "Cds-HH_Ca-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "Cds-HH_Ca-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "Cds-HH_Ca-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "Cds-HH_Ca-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "Cds-HH_Ca-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "Cds-HH_Ca-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "Cds-Cs/H_or_Val7/Ca",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cdd      u0 {1,D} {5,D}
3    [H,Val7] u0 {1,S}
4    Cs       u0 {1,S}
5    C        u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "Cds-CsH_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "Cds-CsH_Ca-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "Cds-CsH_Ca-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "Cds-CsH_Ca-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Cds-CsCs_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Cds-OneDe/H_or_Val7/Ca",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    [H,Val7]                  u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Cds-OneDeH_Ca",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "Cds-CtH_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Cds-CbH_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "Cds-COH_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "Cds-CdH_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    H   u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "Cds-C=SH_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "Cds-OneDeH_Ca-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    F1s                       u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "Cds-CtH_Ca-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "Cds-CbH_Ca-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "Cds-COH_Ca-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "Cds-CdH_Ca-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    F1s u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "Cds-C=SH_Ca-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "Cds-OneDeH_Ca-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    Cl1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "Cds-CtH_Ca-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "Cds-CbH_Ca-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Cb   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "Cds-COH_Ca-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    CO   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "Cds-CdH_Ca-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cd   u0 {1,S} {6,D}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "Cds-C=SH_Ca-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    CS   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "Cds-OneDeH_Ca-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    Br1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "Cds-CtH_Ca-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "Cds-CbH_Ca-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "Cds-COH_Ca-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "Cds-CdH_Ca-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cd   u0 {1,S} {6,D}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "Cds-C=SH_Ca-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    CS   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "Cds-OneDeCs_Ca",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    Cs                        u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "Cds-CtCs_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "Cds-CbCs_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "Cds-COCs_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "Cds-CdCs_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "Cds-C=SCs_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "Cds-TwoDe_Ca",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "Cds-CtCt_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "Cds-CtCb_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "Cds-CtCO_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "Cds-CbCb_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "Cds-CbCO_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "Cds-COCO_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "Cds-CdCt_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "Cds-CdCb_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "Cds-CdCO_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "Cds-CtC=S_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "Cds-CbC=S_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "Cds-COC=S_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "Cds-CdCd_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    C   u0 {2,D}
6    C   u0 {3,D}
7    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "Cds-CdC=S_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 231,
    label = "Cds-C=SC=S_Ca",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "Cds_Ck",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    R   ux {1,S}
4    R   ux {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "Cds-/H_or_Val7/H_or_Val7/Ck",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cdd      u0 {1,D} {5,D}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    O2d      u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "Cds-HH_Ck",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "Cds-HH_Ck-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "Cds-HH_Ck-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "Cds-HH_Ck-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 238,
    label = "Cds-HH_Ck-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "Cds-HH_Ck-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "Cds-HH_Ck-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "Cds-HH_Ck-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "Cds-HH_Ck-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "Cds-HH_Ck-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "Cds-Cs/H_or_Val7/Ck",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cdd      u0 {1,D} {5,D}
3    [H,Val7] u0 {1,S}
4    Cs       u0 {1,S}
5    O2d      u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "Cds-CsH_Ck",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "Cds-CsH_Ck-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "Cds-CsH_Ck-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "Cds-CsH_Ck-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "Cds-CsCs_Ck",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "Cds-OneDe/H_or_Val7/Ck",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    [H,Val7]                  u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "Cds-OneDeH_Ck",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "Cds-OneDeH_Ck-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    F1s                       u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "Cds-OneDeH_Ck-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    Cl1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "Cds-OneDeH_Ck-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    Br1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "Cds-OneDeCs_Ck",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    Cs                        u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "Cds-TwoDe_Ck",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "Cdd_Cds",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "Ca_Cds",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 259,
    label = "Ca_Cds-/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S} {4,S}
2 *1 Cdd      u0 {1,D} {5,D}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    C        u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "Ca_Cds-HH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "Ca-Cdd_Cds-HH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    Cdd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "Ca_Cds-HH-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "Ca-Cdd_Cds-HH-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    Cdd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "Ca_Cds-HH-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "Ca-Cdd_Cds-HH-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cdd  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "Ca_Cds-HH-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "Ca-Cdd_Cds-HH-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Cdd  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "Ca_Cds-HH-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "Ca-Cdd_Cds-HH-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    Cdd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "Ca_Cds-HH-FCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "Ca-Cdd_Cds-HH-FCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cdd  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "Ca_Cds-HH-FBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "Ca-Cdd_Cds-HH-FBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Cdd  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "Ca_Cds-HH-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "Ca-Cdd_Cds-HH-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cdd  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "Ca_Cds-HH-ClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "Ca-Cdd_Cds-HH-ClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cdd  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 278,
    label = "Ca_Cds-HH-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "Ca-Cdd_Cds-HH-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cdd  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "Ca_Cds-Cs/H_or_Val7/",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S} {4,S}
2 *1 Cdd      u0 {1,D} {5,D}
3    Cs       u0 {1,S}
4    [H,Val7] u0 {1,S}
5    C        u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "Ca_Cds-CsH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "Ca_Cds-CsH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "Ca_Cds-CsH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 284,
    label = "Ca_Cds-CsH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "Ca_Cds-CsCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 286,
    label = "Ca_Cds-OneDe/H_or_Val7/",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [H,Val7]                  u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "Ca_Cds-OneDeH",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "Ca_Cds-CtH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "Ca_Cds-CbH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "Ca_Cds-COH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "Ca_Cds-CdH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    H   u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "Ca_Cds-C=SH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "Ca_Cds-OneDeH-F",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    F1s                       u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "Ca_Cds-CtH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "Ca_Cds-CbH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "Ca_Cds-COH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "Ca_Cds-CdH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    F1s u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "Ca_Cds-C=SH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "Ca_Cds-OneDeH-Cl",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cl1s                      u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "Ca_Cds-CtH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "Ca_Cds-CbH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "Ca_Cds-COH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    CO   u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "Ca_Cds-CdH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cd   u0 {1,S} {6,D}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "Ca_Cds-C=SH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    CS   u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "Ca_Cds-OneDeH-Br",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Br1s                      u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "Ca_Cds-CtH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "Ca_Cds-CbH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "Ca_Cds-COH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    CO   u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "Ca_Cds-CdH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cd   u0 {1,S} {6,D}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "Ca_Cds-C=SH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    CS   u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "Ca_Cds-OneDeCs",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "Ca_Cds-CtCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "Ca_Cds-CbCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "Ca_Cds-COCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "Ca_Cds-CdCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "Ca_Cds-C=SCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "Ca_Cds-TwoDe",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    C                         u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "Ca_Cds-CtCt",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "Ca_Cds-CtCb",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "Ca_Cds-CtCO",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "Ca_Cds-CbCb",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "Ca_Cds-CbCO",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "Ca_Cds-COCO",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "Ca_Cds-CdCt",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "Ca_Cds-CdCb",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "Ca_Cds-CdCO",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "Ca_Cds-CtC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "Ca_Cds-CbC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "Ca_Cds-COC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "Ca_Cds-CdCd",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    C   u0 {2,D}
6    C   u0 {3,D}
7    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "Ca_Cds-CdCdCdCdCd_cycle",
    group = 
"""
1 *2 Cd  u0 {2,S} {3,S} {5,D}
2    Cd  u0 {1,S} {4,S} {8,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {2,S} {7,D}
5 *1 Cdd u0 {1,D} {9,D}
6    Cd  u0 {3,D} {7,S}
7    Cd  u0 {4,D} {6,S}
8    C   u0 {2,D}
9    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "Ca_Cds-CdC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "Ca_Cds-C=SC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "Ck_Cds",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "Ck_Cds-/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S} {4,S}
2 *1 Cdd      u0 {1,D} {5,D}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    O2d      u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "Ck_Cds-HH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "Ck_Cds-HH-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "Ck_Cds-HH-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "Ck_Cds-HH-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "Ck_Cds-HH-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "Ck_Cds-HH-FCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "Ck_Cds-HH-FBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "Ck_Cds-HH-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "Ck_Cds-HH-ClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "Ck_Cds-HH-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "Ck_Cds-Cs/H_or_Val7/",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S} {4,S}
2 *1 Cdd      u0 {1,D} {5,D}
3    Cs       u0 {1,S}
4    [H,Val7] u0 {1,S}
5    O2d      u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "Ck_Cds-CsH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "Ck_Cds-CsH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "Ck_Cds-CsH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "Ck_Cds-CsH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "Ck_Cds-CsCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "Ck_Cds-OneDe/H_or_Val7/",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [H,Val7]                  u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "Ck_Cds-OneDeH",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "Ck_Cds-CtH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "Ck_Cds-CbH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 356,
    label = "Ck_Cds-COH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    H   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 357,
    label = "Ck_Cds-CdH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    H   u0 {1,S}
5    O2d u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 358,
    label = "Ck_Cds-C=SH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    H   u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 359,
    label = "Ck_Cds-OneDeH-F",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    F1s                       u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 360,
    label = "Ck_Cds-CtH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 361,
    label = "Ck_Cds-CbH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 362,
    label = "Ck_Cds-COH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 363,
    label = "Ck_Cds-CdH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 364,
    label = "Ck_Cds-C=SH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 365,
    label = "Ck_Cds-OneDeH-Cl",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cl1s                      u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 366,
    label = "Ck_Cds-CtH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 367,
    label = "Ck_Cds-CbH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 368,
    label = "Ck_Cds-COH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    CO   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 369,
    label = "Ck_Cds-CdH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cd   u0 {1,S} {6,D}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
6    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 370,
    label = "Ck_Cds-C=SH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    CS   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 371,
    label = "Ck_Cds-OneDeH-Br",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Br1s                      u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 372,
    label = "Ck_Cds-CtH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 373,
    label = "Ck_Cds-CbH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 374,
    label = "Ck_Cds-COH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    CO   u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 375,
    label = "Ck_Cds-CdH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    Cd   u0 {1,S} {6,D}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
6    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 376,
    label = "Ck_Cds-C=SH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cdd  u0 {1,D} {5,D}
3    CS   u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 377,
    label = "Ck_Cds-OneDeCs",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 378,
    label = "Ck_Cds-CtCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 379,
    label = "Ck_Cds-CbCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 380,
    label = "Ck_Cds-COCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 381,
    label = "Ck_Cds-CdCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 382,
    label = "Ck_Cds-C=SCs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    Cs  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 383,
    label = "Ck_Cds-TwoDe",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 Cdd                       u0 {1,D} {5,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    O2d                       u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 384,
    label = "Ck_Cds-CtCt",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 385,
    label = "Ck_Cds-CtCb",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    Cb  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 386,
    label = "Ck_Cds-CtCO",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    CO  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 387,
    label = "Ck_Cds-CbCb",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    Cb  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 388,
    label = "Ck_Cds-CbCO",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    CO  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 389,
    label = "Ck_Cds-COCO",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    CO  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 390,
    label = "Ck_Cds-CdCt",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Ct  u0 {1,S}
5    O2d u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 391,
    label = "Ck_Cds-CdCb",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cb  u0 {1,S}
5    O2d u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 392,
    label = "Ck_Cds-CdCO",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S}
5    O2d u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 393,
    label = "Ck_Cds-CtC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Ct  u0 {1,S}
4    CS  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 394,
    label = "Ck_Cds-CbC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cb  u0 {1,S}
4    CS  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 395,
    label = "Ck_Cds-COC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CO  u0 {1,S}
4    CS  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 396,
    label = "Ck_Cds-CdCd",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    O2d u0 {2,D}
6    C   u0 {3,D}
7    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 397,
    label = "Ck_Cds-CdC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S}
5    O2d u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 398,
    label = "Ck_Cds-C=SC=S",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cdd u0 {1,D} {5,D}
3    CS  u0 {1,S}
4    CS  u0 {1,S}
5    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 399,
    label = "Cdd_Cdd",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    R!H u0 {1,D}
4    R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 400,
    label = "Ca_Ca",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    C   u0 {1,D}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 401,
    label = "Ca-Cb_Ca-Cb_cyc6",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    Cd  u0 {1,D} {5,S}
4    Cd  u0 {2,D} {6,S}
5    Cb  u0 {3,S} {6,B}
6    Cb  u0 {4,S} {5,B}
""",
    kinetics = None,
)

entry(
    index = 402,
    label = "Ck_Ck",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    O2d u0 {1,D}
4    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 403,
    label = "Ca_Ck",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    C   u0 {1,D}
4    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 404,
    label = "Ck_Ca",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D} {4,D}
3    O2d u0 {1,D}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 405,
    label = "Cds_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    R   ux {1,S}
4    R   ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 406,
    label = "Cds-/H_or_Val7/H_or_Val7/Sd",
    group = 
"""
1 *1 CS       u0 {2,D} {3,S} {4,S}
2 *2 S2d      u0 p2 {1,D}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 407,
    label = "Cds-HH_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 408,
    label = "Cds-HH_Sd-HF",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 409,
    label = "Cds-HH_Sd-HCl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 410,
    label = "Cds-HH_Sd-HBr",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 411,
    label = "Cds-HH_Sd-FF",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 412,
    label = "Cds-HH_Sd-FCl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 413,
    label = "Cds-HH_Sd-FBr",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 414,
    label = "Cds-HH_Sd-ClCl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 415,
    label = "Cds-HH_Sd-ClBr",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 416,
    label = "Cds-HH_Sd-BrBr",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 417,
    label = "Cds-Cs/H_or_Val7/Sd",
    group = 
"""
1 *1 CS       u0 {2,D} {3,S} {4,S}
2 *2 S2d      u0 p2 {1,D}
3    Cs       u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 418,
    label = "Cds-CsH_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 419,
    label = "Cds-CsH_Sd-F",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 420,
    label = "Cds-CsH_Sd-Cl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 421,
    label = "Cds-CsH_Sd-Br",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 422,
    label = "Cds-CsCs_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 423,
    label = "Cds-Os/H_or_Val7/Sd",
    group = 
"""
1 *1 CS       u0 {2,D} {3,S} {4,S}
2 *2 S2d      u0 p2 {1,D}
3    O2s      u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 424,
    label = "Cds-OsH_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 425,
    label = "Cds-OsH_Sd-F",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 426,
    label = "Cds-OsH_Sd-Cl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    O2s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 427,
    label = "Cds-OsH_Sd-Br",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    O2s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 428,
    label = "Cds-OsCs_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 429,
    label = "Cds-Ss/H_or_Val7/Sd",
    group = 
"""
1 *1 CS       u0 {2,D} {3,S} {4,S}
2 *2 S2d      u0 p2 {1,D}
3    S2s      u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 430,
    label = "Cds-SsH_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    S2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 431,
    label = "Cds-SsH_Sd-F",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    S2s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 432,
    label = "Cds-SsH_Sd-Cl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    S2s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 433,
    label = "Cds-SsH_Sd-Br",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    S2s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 434,
    label = "Cds-SsCs_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    S2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 435,
    label = "Cds-OneDe/H_or_Val7/Sd",
    group = 
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [H,Val7]                  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 436,
    label = "Cds-OneDeH_Sd",
    group = 
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 437,
    label = "Cds-CtH_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 438,
    label = "Cds-CbH_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 439,
    label = "Cds-COH_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 440,
    label = "Cds-CdH_Sd",
    group = 
"""
1 *1 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *2 S2d u0 p2 {1,D}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 441,
    label = "Cds-C=SH_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 442,
    label = "Cds-OneDeH_Sd-F",
    group = 
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    F1s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 443,
    label = "Cds-CtH_Sd-F",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 444,
    label = "Cds-CbH_Sd-F",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 445,
    label = "Cds-COH_Sd-F",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 446,
    label = "Cds-CdH_Sd-F",
    group = 
"""
1 *1 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *2 S2d u0 p2 {1,D}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 447,
    label = "Cds-C=SH_Sd-F",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 448,
    label = "Cds-OneDeH_Sd-Cl",
    group = 
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cl1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 449,
    label = "Cds-CtH_Sd-Cl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 450,
    label = "Cds-CbH_Sd-Cl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 451,
    label = "Cds-COH_Sd-Cl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    CO   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 452,
    label = "Cds-CdH_Sd-Cl",
    group = 
"""
1 *1 CS   u0 {2,S} {3,D} {4,S}
2    Cd   u0 {1,S} {5,D}
3 *2 S2d  u0 p2 {1,D}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 453,
    label = "Cds-C=SH_Sd-Cl",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    CS   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 454,
    label = "Cds-OneDeH_Sd-Br",
    group = 
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Br1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 455,
    label = "Cds-CtH_Sd-Br",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 456,
    label = "Cds-CbH_Sd-Br",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 457,
    label = "Cds-COH_Sd-Br",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    CO   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 458,
    label = "Cds-CdH_Sd-Br",
    group = 
"""
1 *1 CS   u0 {2,S} {3,D} {4,S}
2    Cd   u0 {1,S} {5,D}
3 *2 S2d  u0 p2 {1,D}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 459,
    label = "Cds-C=SH_Sd-Br",
    group = 
"""
1 *1 CS   u0 {2,D} {3,S} {4,S}
2 *2 S2d  u0 p2 {1,D}
3    CS   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 460,
    label = "Cds-OneDeCs_Sd",
    group = 
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 461,
    label = "Cds-CtCs_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 462,
    label = "Cds-CbCs_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 463,
    label = "Cds-COCs_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 464,
    label = "Cds-CdCs_Sd",
    group = 
"""
1 *1 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *2 S2d u0 p2 {1,D}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 465,
    label = "Cds-C=SCs_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 466,
    label = "Cds-TwoDe_Sd",
    group = 
"""
1 *1 CS                        u0 {2,D} {3,S} {4,S}
2 *2 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 467,
    label = "Cds-CtCt_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 468,
    label = "Cds-CtCb_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 469,
    label = "Cds-CtCO_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 470,
    label = "Cds-CbCb_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 471,
    label = "Cds-CbCO_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 472,
    label = "Cds-COCO_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 473,
    label = "Cds-CdCt_Sd",
    group = 
"""
1 *1 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *2 S2d u0 p2 {1,D}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 474,
    label = "Cds-CdCb_Sd",
    group = 
"""
1 *1 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *2 S2d u0 p2 {1,D}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 475,
    label = "Cds-CdCO_Sd",
    group = 
"""
1 *1 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *2 S2d u0 p2 {1,D}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 476,
    label = "Cds-CtC=S_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 477,
    label = "Cds-CbC=S_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 478,
    label = "Cds-COC=S_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 479,
    label = "Cds-CdCd_Sd",
    group = 
"""
1 *1 CS  u0 {2,S} {3,S} {4,D}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4 *2 S2d u0 p2 {1,D}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 480,
    label = "Cds-CdC=S_Sd",
    group = 
"""
1 *1 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *2 S2d u0 p2 {1,D}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 481,
    label = "Cds-C=SC=S_Sd",
    group = 
"""
1 *1 CS  u0 {2,D} {3,S} {4,S}
2 *2 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 482,
    label = "Cds_Nd",
    group = 
"""
1 *1 Cd u0 {2,D}
2 *2 N  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 483,
    label = "Cds_N3d",
    group = 
"""
1 *1 Cd  u0 {2,D}
2 *2 N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 484,
    label = "Cds-/H_or_Val7/H_or_Val7/N3d",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 N3d      u0 {1,D}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 485,
    label = "Cds-HH_N3d",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 N3d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 486,
    label = "Cds-HH_N3d-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 N3d u0 {1,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 487,
    label = "Cds-HH_N3d-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 N3d  u0 {1,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 488,
    label = "Cds-HH_N3d-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 N3d  u0 {1,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 489,
    label = "Cds-HH_N3d-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 N3d u0 {1,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 490,
    label = "Cds-HH_N3d-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 N3d  u0 {1,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 491,
    label = "Cds-HH_N3d-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 N3d  u0 {1,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 492,
    label = "Cds-HH_N3d-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 N3d  u0 {1,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 493,
    label = "Cds-HH_N3d-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 N3d  u0 {1,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 494,
    label = "Cds-HH_N3d-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 N3d  u0 {1,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 495,
    label = "Cds-NonDe/H_or_Val7/N3d",
    group = 
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 N3d                   u0 {1,D}
3    [H,Val7]              u0 {1,S}
4    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 496,
    label = "Cds-NonDeH_N3d",
    group = 
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 N3d                   u0 {1,D}
3    H                     u0 {1,S}
4    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 497,
    label = "Cds-NonDeH_N3d-F",
    group = 
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 N3d                   u0 {1,D}
3    F1s                   u0 {1,S}
4    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 498,
    label = "Cds-NonDeH_N3d-Cl",
    group = 
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 N3d                   u0 {1,D}
3    Cl1s                  u0 {1,S}
4    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 499,
    label = "Cds-NonDeH_N3d-Br",
    group = 
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 N3d                   u0 {1,D}
3    Br1s                  u0 {1,S}
4    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 500,
    label = "Cds-NonDe2_N3d",
    group = 
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 N3d                   u0 {1,D}
3    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
4    [Cs,O2s,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 501,
    label = "Cds_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    R  ux {1,S}
4    R  ux {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 502,
    label = "Cds-/H_or_Val7/H_or_Val7/Cds",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R        u0 {2,S}
6    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 503,
    label = "Cds-HH_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 504,
    label = "Cds-HH_Cds-HH",
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
    index = 505,
    label = "Cds-HH_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 506,
    label = "Cds-HH_Cds-Cs\O2s/H",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 507,
    label = "Cds-HH_Cds-Cs\H3/H",
    group = 
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cd u0 {1,S} {3,D} {7,S}
3 *1 Cd u0 {2,D} {8,S} {9,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 508,
    label = "Cds-HH_Cds-CsCs",
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
    index = 509,
    label = "Cds-HH_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 510,
    label = "Cds-HH_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 511,
    label = "Cds-HH_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 512,
    label = "Cds-HH_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 513,
    label = "Cds-HH_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 514,
    label = "Cds-HH_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 515,
    label = "Cds-HH_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 516,
    label = "Cds-HH_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 517,
    label = "Cds-HH_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 518,
    label = "Cds-HH_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 519,
    label = "Cds-HH_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 520,
    label = "Cds-HH_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 521,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {5,S}
2 *1 Cd u0 {1,D} {6,S} {7,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {8,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    Cb u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 522,
    label = "Cds-HH_Cds-CdH",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 523,
    label = "Cds-HH_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 524,
    label = "Cds-HH_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 525,
    label = "Cds-HH_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 526,
    label = "Cds-HH_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 527,
    label = "Cds-HH_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 528,
    label = "Cds-HH_Cds-CdCs",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 529,
    label = "Cds-HH_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 530,
    label = "Cds-HH_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 531,
    label = "Cds-HH_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 532,
    label = "Cds-HH_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 533,
    label = "Cds-HH_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 534,
    label = "Cds-HH_Cds-CdOs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 535,
    label = "Cds-HH_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 536,
    label = "Cds-HH_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 537,
    label = "Cds-HH_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 538,
    label = "Cds-HH_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 539,
    label = "Cds-HH_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 540,
    label = "Cds-HH_Cds-CdSs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 541,
    label = "Cds-HH_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 542,
    label = "Cds-HH_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 543,
    label = "Cds-HH_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 544,
    label = "Cds-HH_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 545,
    label = "Cds-HH_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 546,
    label = "Cds-HH_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 547,
    label = "Cds-HH_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 548,
    label = "Cds-HH_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 549,
    label = "Cds-HH_Cds-CdCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 550,
    label = "Cds-HH_Cds-CdCb",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 551,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {7,S} {8,S}
3    Cd u0 {1,S} {5,D}
4    Cb u0 {1,S} {6,B}
5    Cd u0 {3,D} {6,S}
6    Cb u0 {4,B} {5,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 552,
    label = "Cds-HH_Cds-CdCO",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 553,
    label = "Cds-HH_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 554,
    label = "Cds-HH_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 555,
    label = "Cds-HH_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 556,
    label = "Cds-HH_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 557,
    label = "Cds-HH_Cds-CdCd_cyc",
    group = 
"""
1  *2 Cd u0 {2,D} {3,S} {4,S}
2  *1 Cd u0 {1,D} {11,S} {12,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {7,S}
6     Cd u0 {4,D} {10,S}
7     Cd u0 {5,S} {8,D}
8     Cd u0 {7,D} {9,S}
9     Cd u0 {8,S} {10,D}
10    Cd u0 {6,S} {9,D}
11    H  u0 {2,S}
12    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 558,
    label = "Cds-HH_Cds-CdC=S",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 559,
    label = "Cds-HH_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 560,
    label = "Cds-HH_Cds-CtH-HHBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 561,
    label = "Cds-HH_Cds-CbH-HHBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 562,
    label = "Cds-HH_Cds-COH-HHBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 563,
    label = "Cds-HH_Cds-C=SH-HHBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 564,
    label = "Cds-HH_Cds-CtH-HHF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 565,
    label = "Cds-HH_Cds-CbH-HHF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 566,
    label = "Cds-HH_Cds-COH-HHF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 567,
    label = "Cds-HH_Cds-C=SH-HHF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 568,
    label = "Cds-HH_Cds-CtH-HHCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 569,
    label = "Cds-HH_Cds-CbH-HHCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 570,
    label = "Cds-HH_Cds-COH-HHCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 571,
    label = "Cds-HH_Cds-C=SH-HHCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 572,
    label = "Cds-HH_Cds-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 573,
    label = "Cds-HH_Cds-CtH-HFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 574,
    label = "Cds-HH_Cds-CbH-HFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 575,
    label = "Cds-HH_Cds-COH-HFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 576,
    label = "Cds-HH_Cds-C=SH-HFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 577,
    label = "Cds-HH_Cds-CtH-HFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 578,
    label = "Cds-HH_Cds-CbH-HFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 579,
    label = "Cds-HH_Cds-COH-HFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 580,
    label = "Cds-HH_Cds-C=SH-HFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 581,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {7,S} {8,S}
3    Cd  u0 {1,S} {5,D}
4    Cb  u0 {1,S} {6,B}
5    Cd  u0 {3,D} {6,S}
6    Cb  u0 {4,B} {5,S}
7    H   u0 {2,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 582,
    label = "Cds-HH_Cds-OneDeCs-HF",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    F1s                       u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 583,
    label = "Cds-HH_Cds-CtCs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 584,
    label = "Cds-HH_Cds-CbCs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 585,
    label = "Cds-HH_Cds-COCs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 586,
    label = "Cds-HH_Cds-CdCs-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 587,
    label = "Cds-HH_Cds-C=SCs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 588,
    label = "Cds-HH_Cds-OneDeOs-HF",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    F1s                       u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 589,
    label = "Cds-HH_Cds-CtOs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 590,
    label = "Cds-HH_Cds-CbOs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 591,
    label = "Cds-HH_Cds-COOs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 592,
    label = "Cds-HH_Cds-CdOs-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 593,
    label = "Cds-HH_Cds-C=SOs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 594,
    label = "Cds-HH_Cds-OneDeSs-HF",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    F1s                       u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 595,
    label = "Cds-HH_Cds-CtSs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 596,
    label = "Cds-HH_Cds-CbSs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 597,
    label = "Cds-HH_Cds-COSs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 598,
    label = "Cds-HH_Cds-CdSs-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 599,
    label = "Cds-HH_Cds-C=SSs-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 600,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-HHF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 {1,D} {6,S} {7,S}
3    Cd  u0 {1,S} {4,D}
4    Cd  u0 {3,D} {8,S}
5    H   u0 {1,S}
6    H   u0 {2,S}
7    F1s u0 {2,S}
8    Cb  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 601,
    label = "Cds-HH_Cds-CdH-HHF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 602,
    label = "Cds-HH_Cds-CdCd_cyc-HF",
    group = 
"""
1  *2 Cd  u0 {2,D} {3,S} {4,S}
2  *1 Cd  u0 {1,D} {11,S} {12,S}
3     Cd  u0 {1,S} {5,D}
4     Cd  u0 {1,S} {6,D}
5     Cd  u0 {3,D} {7,S}
6     Cd  u0 {4,D} {10,S}
7     Cd  u0 {5,S} {8,D}
8     Cd  u0 {7,D} {9,S}
9     Cd  u0 {8,S} {10,D}
10    Cd  u0 {6,S} {9,D}
11    H   u0 {2,S}
12    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 603,
    label = "Cds-HH_Cds-CtH-HFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 604,
    label = "Cds-HH_Cds-CbH-HFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 605,
    label = "Cds-HH_Cds-COH-HFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 606,
    label = "Cds-HH_Cds-C=SH-HFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 607,
    label = "Cds-HH_Cds-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 608,
    label = "Cds-HH_Cds-CtH-HClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 609,
    label = "Cds-HH_Cds-CbH-HClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 610,
    label = "Cds-HH_Cds-COH-HClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 611,
    label = "Cds-HH_Cds-C=SH-HClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 612,
    label = "Cds-HH_Cds-CtH-HClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 613,
    label = "Cds-HH_Cds-CbH-HClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 614,
    label = "Cds-HH_Cds-COH-HClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 615,
    label = "Cds-HH_Cds-C=SH-HClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 616,
    label = "Cds-HH_Cds-CdCd_cyc-HCl",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {4,S}
2  *1 Cd   u0 {1,D} {11,S} {12,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {7,S}
6     Cd   u0 {4,D} {10,S}
7     Cd   u0 {5,S} {8,D}
8     Cd   u0 {7,D} {9,S}
9     Cd   u0 {8,S} {10,D}
10    Cd   u0 {6,S} {9,D}
11    H    u0 {2,S}
12    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 617,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {7,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {1,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    H    u0 {2,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 618,
    label = "Cds-HH_Cds-OneDeCs-HCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    Cl1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 619,
    label = "Cds-HH_Cds-CtCs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 620,
    label = "Cds-HH_Cds-CbCs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 621,
    label = "Cds-HH_Cds-COCs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 622,
    label = "Cds-HH_Cds-CdCs-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 623,
    label = "Cds-HH_Cds-C=SCs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 624,
    label = "Cds-HH_Cds-OneDeOs-HCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    Cl1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 625,
    label = "Cds-HH_Cds-CtOs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 626,
    label = "Cds-HH_Cds-CbOs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 627,
    label = "Cds-HH_Cds-COOs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 628,
    label = "Cds-HH_Cds-CdOs-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 629,
    label = "Cds-HH_Cds-C=SOs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 630,
    label = "Cds-HH_Cds-OneDeSs-HCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    Cl1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 631,
    label = "Cds-HH_Cds-CtSs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 632,
    label = "Cds-HH_Cds-CbSs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 633,
    label = "Cds-HH_Cds-COSs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 634,
    label = "Cds-HH_Cds-CdSs-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 635,
    label = "Cds-HH_Cds-C=SSs-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 636,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-HHCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    H    u0 {2,S}
7    Cl1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 637,
    label = "Cds-HH_Cds-CdH-HHCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 638,
    label = "Cds-HH_Cds-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 639,
    label = "Cds-HH_Cds-OneDeCs-HBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    Br1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 640,
    label = "Cds-HH_Cds-CtCs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 641,
    label = "Cds-HH_Cds-CbCs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 642,
    label = "Cds-HH_Cds-COCs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 643,
    label = "Cds-HH_Cds-CdCs-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 644,
    label = "Cds-HH_Cds-C=SCs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 645,
    label = "Cds-HH_Cds-OneDeOs-HBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    Br1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 646,
    label = "Cds-HH_Cds-CtOs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 647,
    label = "Cds-HH_Cds-CbOs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 648,
    label = "Cds-HH_Cds-COOs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 649,
    label = "Cds-HH_Cds-CdOs-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 650,
    label = "Cds-HH_Cds-C=SOs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 651,
    label = "Cds-HH_Cds-OneDeSs-HBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    H                         u0 {1,S}
4    Br1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 652,
    label = "Cds-HH_Cds-CtSs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 653,
    label = "Cds-HH_Cds-CbSs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 654,
    label = "Cds-HH_Cds-COSs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 655,
    label = "Cds-HH_Cds-CdSs-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 656,
    label = "Cds-HH_Cds-C=SSs-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 657,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-HHBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    H    u0 {2,S}
7    Br1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 658,
    label = "Cds-HH_Cds-CdH-HHBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 659,
    label = "Cds-HH_Cds-CtH-HBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 660,
    label = "Cds-HH_Cds-CbH-HBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 661,
    label = "Cds-HH_Cds-COH-HBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 662,
    label = "Cds-HH_Cds-C=SH-HBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 663,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {7,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {1,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    H    u0 {2,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 664,
    label = "Cds-HH_Cds-CdCd_cyc-HBr",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {4,S}
2  *1 Cd   u0 {1,D} {11,S} {12,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {7,S}
6     Cd   u0 {4,D} {10,S}
7     Cd   u0 {5,S} {8,D}
8     Cd   u0 {7,D} {9,S}
9     Cd   u0 {8,S} {10,D}
10    Cd   u0 {6,S} {9,D}
11    H    u0 {2,S}
12    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 665,
    label = "Cds-HH_Cds-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 666,
    label = "Cds-HH_Cds-CtH-FFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 667,
    label = "Cds-HH_Cds-CbH-FFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 668,
    label = "Cds-HH_Cds-COH-FFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 669,
    label = "Cds-HH_Cds-C=SH-FFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 670,
    label = "Cds-HH_Cds-CtH-FFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 671,
    label = "Cds-HH_Cds-CbH-FFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 672,
    label = "Cds-HH_Cds-COH-FFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 673,
    label = "Cds-HH_Cds-C=SH-FFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 674,
    label = "Cds-HH_Cds-OneDeCs-FF",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    F1s                       u0 {1,S}
4    F1s                       u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 675,
    label = "Cds-HH_Cds-CtCs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 676,
    label = "Cds-HH_Cds-CbCs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 677,
    label = "Cds-HH_Cds-COCs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 678,
    label = "Cds-HH_Cds-CdCs-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 679,
    label = "Cds-HH_Cds-C=SCs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 680,
    label = "Cds-HH_Cds-OneDeOs-FF",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    F1s                       u0 {1,S}
4    F1s                       u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 681,
    label = "Cds-HH_Cds-CtOs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 682,
    label = "Cds-HH_Cds-CbOs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 683,
    label = "Cds-HH_Cds-COOs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 684,
    label = "Cds-HH_Cds-CdOs-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 685,
    label = "Cds-HH_Cds-C=SOs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 686,
    label = "Cds-HH_Cds-OneDeSs-FF",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    F1s                       u0 {1,S}
4    F1s                       u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 687,
    label = "Cds-HH_Cds-CtSs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 688,
    label = "Cds-HH_Cds-CbSs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 689,
    label = "Cds-HH_Cds-COSs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 690,
    label = "Cds-HH_Cds-CdSs-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 691,
    label = "Cds-HH_Cds-C=SSs-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 692,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-HFF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 {1,D} {6,S} {7,S}
3    Cd  u0 {1,S} {4,D}
4    Cd  u0 {3,D} {8,S}
5    H   u0 {1,S}
6    F1s u0 {2,S}
7    F1s u0 {2,S}
8    Cb  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 693,
    label = "Cds-HH_Cds-CdH-HFF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 694,
    label = "Cds-HH_Cds-Cs\O2s/H-FFF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 695,
    label = "Cds-HH_Cds-Cs\H3/H-HHHFFF",
    group = 
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {1,S} {3,D} {7,S}
3 *1 Cd  u0 {2,D} {8,S} {9,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    F1s u0 {2,S}
8    F1s u0 {3,S}
9    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 696,
    label = "Cds-HH_Cds-Cs\H3/H-HHFFFF",
    group = 
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {1,S} {3,D} {7,S}
3 *1 Cd  u0 {2,D} {8,S} {9,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
8    F1s u0 {3,S}
9    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 697,
    label = "Cds-HH_Cds-Cs\H3/H-HFFFFF",
    group = 
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {1,S} {3,D} {7,S}
3 *1 Cd  u0 {2,D} {8,S} {9,S}
4    H   u0 {1,S}
5    F1s u0 {1,S}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
8    F1s u0 {3,S}
9    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 698,
    label = "Cds-HH_Cds-Cs\H3/H-FFFFFF",
    group = 
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {1,S} {3,D} {7,S}
3 *1 Cd  u0 {2,D} {8,S} {9,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
8    F1s u0 {3,S}
9    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 699,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {7,S} {8,S}
3    Cd  u0 {1,S} {5,D}
4    Cb  u0 {1,S} {6,B}
5    Cd  u0 {3,D} {6,S}
6    Cb  u0 {4,B} {5,S}
7    F1s u0 {2,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 700,
    label = "Cds-HH_Cds-CdCd_cyc-FF",
    group = 
"""
1  *2 Cd  u0 {2,D} {3,S} {4,S}
2  *1 Cd  u0 {1,D} {11,S} {12,S}
3     Cd  u0 {1,S} {5,D}
4     Cd  u0 {1,S} {6,D}
5     Cd  u0 {3,D} {7,S}
6     Cd  u0 {4,D} {10,S}
7     Cd  u0 {5,S} {8,D}
8     Cd  u0 {7,D} {9,S}
9     Cd  u0 {8,S} {10,D}
10    Cd  u0 {6,S} {9,D}
11    F1s u0 {2,S}
12    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 701,
    label = "Cds-HH_Cds-CtH-FFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 702,
    label = "Cds-HH_Cds-CbH-FFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 703,
    label = "Cds-HH_Cds-COH-FFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 704,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-FFF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 {1,D} {6,S} {7,S}
3    Cd  u0 {1,S} {4,D}
4    Cd  u0 {3,D} {8,S}
5    F1s u0 {1,S}
6    F1s u0 {2,S}
7    F1s u0 {2,S}
8    Cb  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 705,
    label = "Cds-HH_Cds-CdH-FFF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 706,
    label = "Cds-HH_Cds-C=SH-FFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 707,
    label = "Cds-HH_Cds-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 708,
    label = "Cds-HH_Cds-OneDeCs-FCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    F1s                       u0 {1,S}
4    Cl1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 709,
    label = "Cds-HH_Cds-CtCs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 710,
    label = "Cds-HH_Cds-CbCs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 711,
    label = "Cds-HH_Cds-COCs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 712,
    label = "Cds-HH_Cds-CdCs-FCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 713,
    label = "Cds-HH_Cds-C=SCs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 714,
    label = "Cds-HH_Cds-OneDeOs-FCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    F1s                       u0 {1,S}
4    Cl1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 715,
    label = "Cds-HH_Cds-CtOs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 716,
    label = "Cds-HH_Cds-CbOs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 717,
    label = "Cds-HH_Cds-COOs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 718,
    label = "Cds-HH_Cds-CdOs-FCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 719,
    label = "Cds-HH_Cds-C=SOs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 720,
    label = "Cds-HH_Cds-OneDeSs-FCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    F1s                       u0 {1,S}
4    Cl1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 721,
    label = "Cds-HH_Cds-CtSs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 722,
    label = "Cds-HH_Cds-CbSs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 723,
    label = "Cds-HH_Cds-COSs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 724,
    label = "Cds-HH_Cds-CdSs-FCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 725,
    label = "Cds-HH_Cds-C=SSs-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 726,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-HFCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    F1s  u0 {2,S}
7    Cl1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 727,
    label = "Cds-HH_Cds-CdH-HFCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 728,
    label = "Cds-HH_Cds-CtH-FClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 729,
    label = "Cds-HH_Cds-CbH-FClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 730,
    label = "Cds-HH_Cds-COH-FClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 731,
    label = "Cds-HH_Cds-C=SH-FClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 732,
    label = "Cds-HH_Cds-CdCd_cyc-FCl",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {4,S}
2  *1 Cd   u0 {1,D} {11,S} {12,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {7,S}
6     Cd   u0 {4,D} {10,S}
7     Cd   u0 {5,S} {8,D}
8     Cd   u0 {7,D} {9,S}
9     Cd   u0 {8,S} {10,D}
10    Cd   u0 {6,S} {9,D}
11    F1s  u0 {2,S}
12    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 733,
    label = "Cds-HH_Cds-CtH-FClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 734,
    label = "Cds-HH_Cds-CbH-FClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 735,
    label = "Cds-HH_Cds-COH-FClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 736,
    label = "Cds-HH_Cds-C=SH-FClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 737,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle-FCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {7,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {1,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    F1s  u0 {2,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 738,
    label = "Cds-HH_Cds-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 739,
    label = "Cds-HH_Cds-CtH-FBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 740,
    label = "Cds-HH_Cds-CbH-FBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 741,
    label = "Cds-HH_Cds-COH-FBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 742,
    label = "Cds-HH_Cds-C=SH-FBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 743,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle-FBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {7,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {1,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    F1s  u0 {2,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 744,
    label = "Cds-HH_Cds-CdCd_cyc-FBr",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {4,S}
2  *1 Cd   u0 {1,D} {11,S} {12,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {7,S}
6     Cd   u0 {4,D} {10,S}
7     Cd   u0 {5,S} {8,D}
8     Cd   u0 {7,D} {9,S}
9     Cd   u0 {8,S} {10,D}
10    Cd   u0 {6,S} {9,D}
11    F1s  u0 {2,S}
12    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 745,
    label = "Cds-HH_Cds-OneDeCs-FBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    F1s                       u0 {1,S}
4    Br1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 746,
    label = "Cds-HH_Cds-CtCs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 747,
    label = "Cds-HH_Cds-CbCs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 748,
    label = "Cds-HH_Cds-COCs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 749,
    label = "Cds-HH_Cds-CdCs-FBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 750,
    label = "Cds-HH_Cds-C=SCs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 751,
    label = "Cds-HH_Cds-OneDeOs-FBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    F1s                       u0 {1,S}
4    Br1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 752,
    label = "Cds-HH_Cds-CtOs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 753,
    label = "Cds-HH_Cds-CbOs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 754,
    label = "Cds-HH_Cds-COOs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 755,
    label = "Cds-HH_Cds-CdOs-FBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 756,
    label = "Cds-HH_Cds-C=SOs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 757,
    label = "Cds-HH_Cds-OneDeSs-FBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    F1s                       u0 {1,S}
4    Br1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 758,
    label = "Cds-HH_Cds-CtSs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 759,
    label = "Cds-HH_Cds-CbSs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 760,
    label = "Cds-HH_Cds-COSs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 761,
    label = "Cds-HH_Cds-CdSs-FBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 762,
    label = "Cds-HH_Cds-C=SSs-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 763,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-HFBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    F1s  u0 {2,S}
7    Br1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 764,
    label = "Cds-HH_Cds-CdH-HFBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 765,
    label = "Cds-HH_Cds-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 766,
    label = "Cds-HH_Cds-CtH-ClClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 767,
    label = "Cds-HH_Cds-CbH-ClClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 768,
    label = "Cds-HH_Cds-COH-ClClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 769,
    label = "Cds-HH_Cds-C=SH-ClClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 770,
    label = "Cds-HH_Cds-CtH-ClClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 771,
    label = "Cds-HH_Cds-CbH-ClClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 772,
    label = "Cds-HH_Cds-COH-ClClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 773,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-ClClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    Cl1s u0 {1,S}
6    Cl1s u0 {2,S}
7    Cl1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 774,
    label = "Cds-HH_Cds-CdH-ClClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 775,
    label = "Cds-HH_Cds-C=SH-ClClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 776,
    label = "Cds-HH_Cds-CdCd_cyc-ClCl",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {4,S}
2  *1 Cd   u0 {1,D} {11,S} {12,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {7,S}
6     Cd   u0 {4,D} {10,S}
7     Cd   u0 {5,S} {8,D}
8     Cd   u0 {7,D} {9,S}
9     Cd   u0 {8,S} {10,D}
10    Cd   u0 {6,S} {9,D}
11    Cl1s u0 {2,S}
12    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 777,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {7,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {1,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    Cl1s u0 {2,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 778,
    label = "Cds-HH_Cds-OneDeCs-ClCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cl1s                      u0 {1,S}
4    Cl1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 779,
    label = "Cds-HH_Cds-CtCs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 780,
    label = "Cds-HH_Cds-CbCs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 781,
    label = "Cds-HH_Cds-COCs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 782,
    label = "Cds-HH_Cds-CdCs-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 783,
    label = "Cds-HH_Cds-C=SCs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 784,
    label = "Cds-HH_Cds-OneDeOs-ClCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cl1s                      u0 {1,S}
4    Cl1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 785,
    label = "Cds-HH_Cds-CtOs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 786,
    label = "Cds-HH_Cds-CbOs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 787,
    label = "Cds-HH_Cds-COOs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 788,
    label = "Cds-HH_Cds-CdOs-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 789,
    label = "Cds-HH_Cds-C=SOs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 790,
    label = "Cds-HH_Cds-OneDeSs-ClCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cl1s                      u0 {1,S}
4    Cl1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 791,
    label = "Cds-HH_Cds-CtSs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 792,
    label = "Cds-HH_Cds-CbSs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 793,
    label = "Cds-HH_Cds-COSs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 794,
    label = "Cds-HH_Cds-CdSs-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 795,
    label = "Cds-HH_Cds-C=SSs-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 796,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-HClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    Cl1s u0 {2,S}
7    Cl1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 797,
    label = "Cds-HH_Cds-CdH-HClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 798,
    label = "Cds-HH_Cds-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 799,
    label = "Cds-HH_Cds-CtH-ClBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 800,
    label = "Cds-HH_Cds-CbH-ClBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 801,
    label = "Cds-HH_Cds-COH-ClBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 802,
    label = "Cds-HH_Cds-C=SH-ClBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 803,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle-ClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {7,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {1,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    Cl1s u0 {2,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 804,
    label = "Cds-HH_Cds-CdCd_cyc-ClBr",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {4,S}
2  *1 Cd   u0 {1,D} {11,S} {12,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {7,S}
6     Cd   u0 {4,D} {10,S}
7     Cd   u0 {5,S} {8,D}
8     Cd   u0 {7,D} {9,S}
9     Cd   u0 {8,S} {10,D}
10    Cd   u0 {6,S} {9,D}
11    Cl1s u0 {2,S}
12    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 805,
    label = "Cds-HH_Cds-OneDeCs-ClBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cl1s                      u0 {1,S}
4    Br1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 806,
    label = "Cds-HH_Cds-CtCs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 807,
    label = "Cds-HH_Cds-CbCs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 808,
    label = "Cds-HH_Cds-COCs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 809,
    label = "Cds-HH_Cds-CdCs-ClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 810,
    label = "Cds-HH_Cds-C=SCs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 811,
    label = "Cds-HH_Cds-OneDeOs-ClBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cl1s                      u0 {1,S}
4    Br1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 812,
    label = "Cds-HH_Cds-CtOs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 813,
    label = "Cds-HH_Cds-CbOs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 814,
    label = "Cds-HH_Cds-COOs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 815,
    label = "Cds-HH_Cds-CdOs-ClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 816,
    label = "Cds-HH_Cds-C=SOs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 817,
    label = "Cds-HH_Cds-OneDeSs-ClBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cl1s                      u0 {1,S}
4    Br1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 818,
    label = "Cds-HH_Cds-CtSs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 819,
    label = "Cds-HH_Cds-CbSs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 820,
    label = "Cds-HH_Cds-COSs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 821,
    label = "Cds-HH_Cds-CdSs-ClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 822,
    label = "Cds-HH_Cds-C=SSs-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 823,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-HClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    Cl1s u0 {2,S}
7    Br1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 824,
    label = "Cds-HH_Cds-CdH-HClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 825,
    label = "Cds-HH_Cds-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 826,
    label = "Cds-HH_Cds-CtH-BrBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 827,
    label = "Cds-HH_Cds-CbH-BrBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 828,
    label = "Cds-HH_Cds-COH-BrBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 829,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-BrBrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    Br1s u0 {1,S}
6    Br1s u0 {2,S}
7    Br1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 830,
    label = "Cds-HH_Cds-CdH-BrBrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 831,
    label = "Cds-HH_Cds-C=SH-BrBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 832,
    label = "Cds-HH_Cds-OneDeCs-BrBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Br1s                      u0 {1,S}
4    Br1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 833,
    label = "Cds-HH_Cds-CtCs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 834,
    label = "Cds-HH_Cds-CbCs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 835,
    label = "Cds-HH_Cds-COCs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 836,
    label = "Cds-HH_Cds-CdCs-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 837,
    label = "Cds-HH_Cds-C=SCs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 838,
    label = "Cds-HH_Cds-OneDeOs-BrBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Br1s                      u0 {1,S}
4    Br1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 839,
    label = "Cds-HH_Cds-CtOs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 840,
    label = "Cds-HH_Cds-CbOs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 841,
    label = "Cds-HH_Cds-COOs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 842,
    label = "Cds-HH_Cds-CdOs-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 843,
    label = "Cds-HH_Cds-C=SOs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 844,
    label = "Cds-HH_Cds-OneDeSs-BrBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Br1s                      u0 {1,S}
4    Br1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 845,
    label = "Cds-HH_Cds-CtSs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 846,
    label = "Cds-HH_Cds-CbSs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 847,
    label = "Cds-HH_Cds-COSs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 848,
    label = "Cds-HH_Cds-CdSs-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 849,
    label = "Cds-HH_Cds-C=SSs-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 850,
    label = "Cds-HH_Cds-(Cd-Cd-Cb)H-HBrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    Br1s u0 {2,S}
7    Br1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 851,
    label = "Cds-HH_Cds-CdH-HBrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 852,
    label = "Cds-HH_Cds-CdCbCbCdCdCd_cycle-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {7,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {1,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    Br1s u0 {2,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 853,
    label = "Cds-HH_Cds-CdCd_cyc-BrBr",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {4,S}
2  *1 Cd   u0 {1,D} {11,S} {12,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {7,S}
6     Cd   u0 {4,D} {10,S}
7     Cd   u0 {5,S} {8,D}
8     Cd   u0 {7,D} {9,S}
9     Cd   u0 {8,S} {10,D}
10    Cd   u0 {6,S} {9,D}
11    Br1s u0 {2,S}
12    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 854,
    label = "Cds-Cs/H_or_Val7/Cds",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    Cs       u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R        u0 {2,S}
6    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 855,
    label = "Cds-CsH_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 856,
    label = "Cds-CsH_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 857,
    label = "Cds-Cs\O2s/H_Cds-HH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {2,S}
6    H   u0 {2,S}
7    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 858,
    label = "Cds-CsH_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 859,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {7,S}
2 *2 Cd u0 {1,D} {4,S} {8,S}
3    Cs u0 {1,S} {6,S}
4    Cs u0 {2,S} {5,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    H  u0 {1,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 860,
    label = "Cds-CsH_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 861,
    label = "Cds-CsH_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 862,
    label = "Cds-CsH_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 863,
    label = "Cds-CsH_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 864,
    label = "Cds-CsH_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 865,
    label = "Cds-CsH_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 866,
    label = "Cds-CsH_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 867,
    label = "Cds-CsH_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 868,
    label = "Cds-CsH_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 869,
    label = "Cds-CsH_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 870,
    label = "Cds-CsH_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 871,
    label = "Cds-CsH_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 872,
    label = "Cds-CsH_Cds-CbH-indene",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {6,S}
2 *2 Cd u0 {1,D} {4,S} {7,S}
3    Cs u0 {1,S} {5,S}
4    Cb u0 {2,S} {5,B}
5    Cb u0 {3,S} {4,B}
6    H  u0 {1,S}
7    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 873,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {7,S}
2 *2 Cd u0 {1,D} {4,S} {8,S}
3    Cs u0 {1,S} {6,S}
4    Cb u0 {2,S} {5,B}
5    Cb u0 {4,B} {6,S}
6    Cs u0 {3,S} {5,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 874,
    label = "Cds-CsH_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 875,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H",
    group = 
"""
1  *2 Cd u0 {2,D} {3,S} {7,S}
2  *1 Cd u0 {1,D} {8,S} {9,S}
3     Cd u0 {1,S} {4,D}
4     Cd u0 {3,D} {5,S}
5     Cd u0 {4,S} {6,D}
6     Cd u0 {5,D} {10,S}
7     H  u0 {1,S}
8     Cs u0 {2,S}
9     H  u0 {2,S}
10    Cd u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 876,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd)H",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {5,S}
2 *1 Cd u0 {1,D} {6,S} {7,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {8,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    H  u0 {2,S}
8    Cd u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 877,
    label = "Cds-CsH_Cds-Cd(Cd)H",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    Cd u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 878,
    label = "Cds-CsH_Cds-CdH",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 879,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {6,S}
2 *2 Cd u0 {1,D} {4,S} {7,S}
3    Cs u0 {1,S} {5,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {3,S} {4,D}
6    H  u0 {1,S}
7    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 880,
    label = "Cds-CsH_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 881,
    label = "Cds-CsH_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 882,
    label = "Cds-CsH_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 883,
    label = "Cds-CsH_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 884,
    label = "Cds-CsH_Cds-CbCs-dihydronaphthalene",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {7,S}
2 *2 Cd u0 {1,D} {4,S} {8,S}
3    Cs u0 {1,S} {6,S}
4    Cb u0 {2,S} {5,B}
5    Cb u0 {4,B} {6,S}
6    Cs u0 {3,S} {5,S}
7    H  u0 {1,S}
8    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 885,
    label = "Cds-CsH_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 886,
    label = "Cds-CsH_Cds-CdCs",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 887,
    label = "Cds-CsH_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 888,
    label = "Cds-CsH_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 889,
    label = "Cds-CsH_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 890,
    label = "Cds-CsH_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 891,
    label = "Cds-CsH_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 892,
    label = "Cds-CsH_Cds-CdOs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Cs  u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 893,
    label = "Cds-CsH_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 894,
    label = "Cds-CsH_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 895,
    label = "Cds-CsH_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 896,
    label = "Cds-CsH_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 897,
    label = "Cds-CsH_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 898,
    label = "Cds-CsH_Cds-CdSs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Cs  u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 899,
    label = "Cds-CsH_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 900,
    label = "Cds-CsH_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 901,
    label = "Cds-CsH_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 902,
    label = "Cds-CsH_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 903,
    label = "Cds-CsH_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 904,
    label = "Cds-CsH_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 905,
    label = "Cds-CsH_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 906,
    label = "Cds-CsH_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 907,
    label = "Cds-CsH_Cds-CdCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 908,
    label = "Cds-CsH_Cds-CdCb",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 909,
    label = "Cds-CsH_Cds-CdCO",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 910,
    label = "Cds-CsH_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 911,
    label = "Cds-CsH_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 912,
    label = "Cds-CsH_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 913,
    label = "Cds-CsH_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 914,
    label = "Cds-CsH_Cds-CdC=S",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 915,
    label = "Cds-CsH_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 916,
    label = "Cds-Cs\O2s/H_Cds-HH-HHCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    H    u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 917,
    label = "Cds-Cs\O2s/H_Cds-HH-HHBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    H    u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 918,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {7,S}
2 *2 Cd  u0 {1,D} {4,S} {8,S}
3    Cs  u0 {1,S} {6,S}
4    Cs  u0 {2,S} {5,S}
5    Cd  u0 {4,S} {6,D}
6    Cd  u0 {3,S} {5,D}
7    H   u0 {1,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 919,
    label = "Cds-Cs\O2s/H_Cds-HH-HFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    H    u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 920,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cs   u0 {2,S} {5,S}
5    Cd   u0 {4,S} {6,D}
6    Cd   u0 {3,S} {5,D}
7    H    u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 921,
    label = "Cds-Cs\O2s/H_Cds-HH-HFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 922,
    label = "Cds-Cs\O2s/H_Cds-HH-HFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    H    u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 923,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cs   u0 {2,S} {5,S}
5    Cd   u0 {4,S} {6,D}
6    Cd   u0 {3,S} {5,D}
7    H    u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 924,
    label = "Cds-Cs\O2s/H_Cds-HH-HClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 925,
    label = "Cds-Cs\O2s/H_Cds-HH-HClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 926,
    label = "Cds-Cs\O2s/H_Cds-HH-HBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 927,
    label = "Cds-CsH_Cds-CtH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 928,
    label = "Cds-CsH_Cds-CbH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 929,
    label = "Cds-CsH_Cds-CbH-indene-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    H    u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 930,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {4,B} {6,S}
6    Cs   u0 {3,S} {5,S}
7    H    u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 931,
    label = "Cds-CsH_Cds-COH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 932,
    label = "Cds-CsH_Cds-C=SH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 933,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    H    u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 934,
    label = "Cds-Cs\O2s/H_Cds-HH-HHF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S}
4    H   u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
7    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 935,
    label = "Cds-CsH_Cds-CtH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 936,
    label = "Cds-CsH_Cds-CbH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 937,
    label = "Cds-CsH_Cds-CbH-indene-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    H    u0 {1,S}
7    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 938,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {4,B} {6,S}
6    Cs   u0 {3,S} {5,S}
7    H    u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 939,
    label = "Cds-CsH_Cds-COH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 940,
    label = "Cds-CsH_Cds-C=SH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 941,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    H    u0 {1,S}
7    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 942,
    label = "Cds-CsH_Cds-CtH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 943,
    label = "Cds-CsH_Cds-CbH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 944,
    label = "Cds-CsH_Cds-CbH-indene-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cs  u0 {1,S} {5,S}
4    Cb  u0 {2,S} {5,B}
5    Cb  u0 {3,S} {4,B}
6    H   u0 {1,S}
7    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 945,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {7,S}
2 *2 Cd  u0 {1,D} {4,S} {8,S}
3    Cs  u0 {1,S} {6,S}
4    Cb  u0 {2,S} {5,B}
5    Cb  u0 {4,B} {6,S}
6    Cs  u0 {3,S} {5,S}
7    H   u0 {1,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 946,
    label = "Cds-CsH_Cds-COH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 947,
    label = "Cds-CsH_Cds-C=SH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 948,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cs  u0 {1,S} {5,S}
4    Cd  u0 {2,S} {5,D}
5    Cd  u0 {3,S} {4,D}
6    H   u0 {1,S}
7    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 949,
    label = "Cds-CsH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 950,
    label = "Cds-CsH_Cds-OneDeCs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    F1s                       u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 951,
    label = "Cds-CsH_Cds-CtCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 952,
    label = "Cds-CsH_Cds-CbCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 953,
    label = "Cds-CsH_Cds-CbCs-dihydronaphthalene-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {7,S}
2 *2 Cd  u0 {1,D} {4,S} {8,S}
3    Cs  u0 {1,S} {6,S}
4    Cb  u0 {2,S} {5,B}
5    Cb  u0 {4,B} {6,S}
6    Cs  u0 {3,S} {5,S}
7    F1s u0 {1,S}
8    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 954,
    label = "Cds-CsH_Cds-COCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 955,
    label = "Cds-CsH_Cds-CdCs-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 956,
    label = "Cds-CsH_Cds-C=SCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 957,
    label = "Cds-CsH_Cds-OneDeOs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    F1s                       u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 958,
    label = "Cds-CsH_Cds-CtOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 959,
    label = "Cds-CsH_Cds-CbOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 960,
    label = "Cds-CsH_Cds-COOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 961,
    label = "Cds-CsH_Cds-CdOs-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 962,
    label = "Cds-CsH_Cds-C=SOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 963,
    label = "Cds-CsH_Cds-OneDeSs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    F1s                       u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 964,
    label = "Cds-CsH_Cds-CtSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 965,
    label = "Cds-CsH_Cds-CbSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 966,
    label = "Cds-CsH_Cds-COSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 967,
    label = "Cds-CsH_Cds-CdSs-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 968,
    label = "Cds-CsH_Cds-C=SSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 969,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-HF",
    group = 
"""
1  *2 Cd  u0 {2,D} {3,S} {7,S}
2  *1 Cd  u0 {1,D} {8,S} {9,S}
3     Cd  u0 {1,S} {4,D}
4     Cd  u0 {3,D} {5,S}
5     Cd  u0 {4,S} {6,D}
6     Cd  u0 {5,D} {10,S}
7     H   u0 {1,S}
8     Cs  u0 {2,S}
9     F1s u0 {2,S}
10    Cd  u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 970,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd)H-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 {1,D} {6,S} {7,S}
3    Cd  u0 {1,S} {4,D}
4    Cd  u0 {3,D} {8,S}
5    H   u0 {1,S}
6    Cs  u0 {2,S}
7    F1s u0 {2,S}
8    Cd  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 971,
    label = "Cds-CsH_Cds-Cd(Cd)H-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,S}
4    H   u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    Cd  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 972,
    label = "Cds-CsH_Cds-CdH-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 973,
    label = "Cds-CsH_Cds-CtH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 974,
    label = "Cds-CsH_Cds-CbH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 975,
    label = "Cds-CsH_Cds-CbH-indene-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cs  u0 {1,S} {5,S}
4    Cb  u0 {2,S} {5,B}
5    Cb  u0 {3,S} {4,B}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 976,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {7,S}
2 *2 Cd  u0 {1,D} {4,S} {8,S}
3    Cs  u0 {1,S} {6,S}
4    Cb  u0 {2,S} {5,B}
5    Cb  u0 {4,B} {6,S}
6    Cs  u0 {3,S} {5,S}
7    F1s u0 {1,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 977,
    label = "Cds-CsH_Cds-COH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 978,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-FF",
    group = 
"""
1  *2 Cd  u0 {2,D} {3,S} {7,S}
2  *1 Cd  u0 {1,D} {8,S} {9,S}
3     Cd  u0 {1,S} {4,D}
4     Cd  u0 {3,D} {5,S}
5     Cd  u0 {4,S} {6,D}
6     Cd  u0 {5,D} {10,S}
7     F1s u0 {1,S}
8     Cs  u0 {2,S}
9     F1s u0 {2,S}
10    Cd  u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 979,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd)H-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 {1,D} {6,S} {7,S}
3    Cd  u0 {1,S} {4,D}
4    Cd  u0 {3,D} {8,S}
5    F1s u0 {1,S}
6    Cs  u0 {2,S}
7    F1s u0 {2,S}
8    Cd  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 980,
    label = "Cds-CsH_Cds-Cd(Cd)H-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    Cd  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 981,
    label = "Cds-CsH_Cds-CdH-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 982,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cs  u0 {1,S} {5,S}
4    Cd  u0 {2,S} {5,D}
5    Cd  u0 {3,S} {4,D}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 983,
    label = "Cds-CsH_Cds-C=SH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 984,
    label = "Cds-Cs\O2s/H_Cds-HH-FClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 985,
    label = "Cds-Cs\O2s/H_Cds-HH-FBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 986,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {7,S}
2 *2 Cd  u0 {1,D} {4,S} {8,S}
3    Cs  u0 {1,S} {6,S}
4    Cs  u0 {2,S} {5,S}
5    Cd  u0 {4,S} {6,D}
6    Cd  u0 {3,S} {5,D}
7    F1s u0 {1,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 987,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cs   u0 {2,S} {5,S}
5    Cd   u0 {4,S} {6,D}
6    Cd   u0 {3,S} {5,D}
7    F1s  u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 988,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cs   u0 {2,S} {5,S}
5    Cd   u0 {4,S} {6,D}
6    Cd   u0 {3,S} {5,D}
7    F1s  u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 989,
    label = "Cds-CsH_Cds-CtH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 990,
    label = "Cds-CsH_Cds-CbH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 991,
    label = "Cds-CsH_Cds-CbH-indene-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    F1s  u0 {1,S}
7    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 992,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {4,B} {6,S}
6    Cs   u0 {3,S} {5,S}
7    F1s  u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 993,
    label = "Cds-CsH_Cds-COH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 994,
    label = "Cds-CsH_Cds-C=SH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 995,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    F1s  u0 {1,S}
7    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 996,
    label = "Cds-Cs\O2s/H_Cds-HH-FClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 997,
    label = "Cds-Cs\O2s/H_Cds-HH-FFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S} {7,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    O2s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 998,
    label = "Cds-Cs\O2s/H_Cds-HH-FFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    F1s  u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 999,
    label = "Cds-Cs\O2s/H_Cds-HH-FFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    F1s  u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1000,
    label = "Cds-CsH_Cds-CtH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1001,
    label = "Cds-CsH_Cds-CbH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1002,
    label = "Cds-CsH_Cds-CbH-indene-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    F1s  u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1003,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {4,B} {6,S}
6    Cs   u0 {3,S} {5,S}
7    F1s  u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1004,
    label = "Cds-CsH_Cds-COH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1005,
    label = "Cds-CsH_Cds-C=SH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1006,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    F1s  u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1007,
    label = "Cds-CsH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1008,
    label = "Cds-CsH_Cds-OneDeCs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cl1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1009,
    label = "Cds-CsH_Cds-CtCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1010,
    label = "Cds-CsH_Cds-CbCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1011,
    label = "Cds-CsH_Cds-CbCs-dihydronaphthalene-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {4,B} {6,S}
6    Cs   u0 {3,S} {5,S}
7    Cl1s u0 {1,S}
8    Cs   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1012,
    label = "Cds-CsH_Cds-COCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1013,
    label = "Cds-CsH_Cds-CdCs-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1014,
    label = "Cds-CsH_Cds-C=SCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1015,
    label = "Cds-CsH_Cds-OneDeOs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cl1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1016,
    label = "Cds-CsH_Cds-CtOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1017,
    label = "Cds-CsH_Cds-CbOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1018,
    label = "Cds-CsH_Cds-COOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1019,
    label = "Cds-CsH_Cds-CdOs-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1020,
    label = "Cds-CsH_Cds-C=SOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1021,
    label = "Cds-CsH_Cds-OneDeSs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cl1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1022,
    label = "Cds-CsH_Cds-CtSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1023,
    label = "Cds-CsH_Cds-CbSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1024,
    label = "Cds-CsH_Cds-COSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1025,
    label = "Cds-CsH_Cds-CdSs-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1026,
    label = "Cds-CsH_Cds-C=SSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1027,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-HCl",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {7,S}
2  *1 Cd   u0 {1,D} {8,S} {9,S}
3     Cd   u0 {1,S} {4,D}
4     Cd   u0 {3,D} {5,S}
5     Cd   u0 {4,S} {6,D}
6     Cd   u0 {5,D} {10,S}
7     H    u0 {1,S}
8     Cs   u0 {2,S}
9     Cl1s u0 {2,S}
10    Cd   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 1028,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd)H-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    Cs   u0 {2,S}
7    Cl1s u0 {2,S}
8    Cd   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1029,
    label = "Cds-CsH_Cds-Cd(Cd)H-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,S}
4    H    u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    Cd   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1030,
    label = "Cds-CsH_Cds-CdH-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1031,
    label = "Cds-Cs\O2s/H_Cds-HH-ClBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1032,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cs   u0 {2,S} {5,S}
5    Cd   u0 {4,S} {6,D}
6    Cd   u0 {3,S} {5,D}
7    Cl1s u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1033,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cs   u0 {2,S} {5,S}
5    Cd   u0 {4,S} {6,D}
6    Cd   u0 {3,S} {5,D}
7    Cl1s u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1034,
    label = "Cds-CsH_Cds-CtH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1035,
    label = "Cds-CsH_Cds-CbH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1036,
    label = "Cds-CsH_Cds-CbH-indene-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    Cl1s u0 {1,S}
7    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1037,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {4,B} {6,S}
6    Cs   u0 {3,S} {5,S}
7    Cl1s u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1038,
    label = "Cds-CsH_Cds-COH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1039,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-ClCl",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {7,S}
2  *1 Cd   u0 {1,D} {8,S} {9,S}
3     Cd   u0 {1,S} {4,D}
4     Cd   u0 {3,D} {5,S}
5     Cd   u0 {4,S} {6,D}
6     Cd   u0 {5,D} {10,S}
7     Cl1s u0 {1,S}
8     Cs   u0 {2,S}
9     Cl1s u0 {2,S}
10    Cd   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 1040,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd)H-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    Cl1s u0 {1,S}
6    Cs   u0 {2,S}
7    Cl1s u0 {2,S}
8    Cd   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1041,
    label = "Cds-CsH_Cds-Cd(Cd)H-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    Cd   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1042,
    label = "Cds-CsH_Cds-CdH-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1043,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    Cl1s u0 {1,S}
7    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1044,
    label = "Cds-CsH_Cds-C=SH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1045,
    label = "Cds-CsH_Cds-CtH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1046,
    label = "Cds-CsH_Cds-CbH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1047,
    label = "Cds-CsH_Cds-CbH-indene-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    Cl1s u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1048,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {4,B} {6,S}
6    Cs   u0 {3,S} {5,S}
7    Cl1s u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1049,
    label = "Cds-CsH_Cds-COH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1050,
    label = "Cds-CsH_Cds-C=SH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1051,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    Cl1s u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1052,
    label = "Cds-Cs\O2s/H_Cds-HH-ClClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1053,
    label = "Cds-Cs\O2s/H_Cds-HH-ClClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1054,
    label = "Cds-CsH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1055,
    label = "Cds-CsH_Cds-CtH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1056,
    label = "Cds-CsH_Cds-CbH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1057,
    label = "Cds-CsH_Cds-CbH-indene-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1058,
    label = "Cds-CsH_Cds-CbH-dihydronaphthalene-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {4,B} {6,S}
6    Cs   u0 {3,S} {5,S}
7    Br1s u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1059,
    label = "Cds-CsH_Cds-COH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1060,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-BrBr",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {7,S}
2  *1 Cd   u0 {1,D} {8,S} {9,S}
3     Cd   u0 {1,S} {4,D}
4     Cd   u0 {3,D} {5,S}
5     Cd   u0 {4,S} {6,D}
6     Cd   u0 {5,D} {10,S}
7     Br1s u0 {1,S}
8     Cs   u0 {2,S}
9     Br1s u0 {2,S}
10    Cd   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 1061,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd)H-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    Br1s u0 {1,S}
6    Cs   u0 {2,S}
7    Br1s u0 {2,S}
8    Cd   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1062,
    label = "Cds-CsH_Cds-Cd(Cd)H-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    Cd   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1063,
    label = "Cds-CsH_Cds-CdH-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1064,
    label = "Cds-CsH_Cds-(CdsH-Cds)_cyc5-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cs   u0 {1,S} {5,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1065,
    label = "Cds-CsH_Cds-C=SH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1066,
    label = "Cds-Cs\O2s/H_Cds-HH-BrBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S} {7,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    O2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1067,
    label = "Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cs   u0 {2,S} {5,S}
5    Cd   u0 {4,S} {6,D}
6    Cd   u0 {3,S} {5,D}
7    Br1s u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1068,
    label = "Cds-CsH_Cds-OneDeCs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Br1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1069,
    label = "Cds-CsH_Cds-CtCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1070,
    label = "Cds-CsH_Cds-CbCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1071,
    label = "Cds-CsH_Cds-CbCs-dihydronaphthalene-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cs   u0 {1,S} {6,S}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {4,B} {6,S}
6    Cs   u0 {3,S} {5,S}
7    Br1s u0 {1,S}
8    Cs   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1072,
    label = "Cds-CsH_Cds-COCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1073,
    label = "Cds-CsH_Cds-CdCs-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1074,
    label = "Cds-CsH_Cds-C=SCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1075,
    label = "Cds-CsH_Cds-OneDeOs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Br1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1076,
    label = "Cds-CsH_Cds-CtOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1077,
    label = "Cds-CsH_Cds-CbOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1078,
    label = "Cds-CsH_Cds-COOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1079,
    label = "Cds-CsH_Cds-CdOs-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1080,
    label = "Cds-CsH_Cds-C=SOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1081,
    label = "Cds-CsH_Cds-OneDeSs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Br1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1082,
    label = "Cds-CsH_Cds-CtSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1083,
    label = "Cds-CsH_Cds-CbSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1084,
    label = "Cds-CsH_Cds-COSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1085,
    label = "Cds-CsH_Cds-CdSs-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1086,
    label = "Cds-CsH_Cds-C=SSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1087,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-HBr",
    group = 
"""
1  *2 Cd   u0 {2,D} {3,S} {7,S}
2  *1 Cd   u0 {1,D} {8,S} {9,S}
3     Cd   u0 {1,S} {4,D}
4     Cd   u0 {3,D} {5,S}
5     Cd   u0 {4,S} {6,D}
6     Cd   u0 {5,D} {10,S}
7     H    u0 {1,S}
8     Cs   u0 {2,S}
9     Br1s u0 {2,S}
10    Cd   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 1088,
    label = "Cds-CsH_Cds-(Cd-Cd-Cd)H-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    Cs   u0 {2,S}
7    Br1s u0 {2,S}
8    Cd   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1089,
    label = "Cds-CsH_Cds-Cd(Cd)H-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,S}
4    H    u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    Cd   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1090,
    label = "Cds-CsH_Cds-CdH-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1091,
    label = "Cds-CsCs_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1092,
    label = "Cds-CsCs_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1093,
    label = "Cds-CsCs_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1094,
    label = "Cds-CsCs_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1095,
    label = "Cds-CsCs_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1096,
    label = "Cds-CsCs_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1097,
    label = "Cds-CsCs_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1098,
    label = "Cds-CsCs_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1099,
    label = "Cds-CsCs_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1100,
    label = "Cds-CsCs_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1101,
    label = "Cds-CsCs_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1102,
    label = "Cds-CsCs_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1103,
    label = "Cds-CsCs_Cds-CdCs",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1104,
    label = "Cds-CsCs_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1105,
    label = "Cds-CsCs_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1106,
    label = "Cds-CsCs_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1107,
    label = "Cds-CsCs_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1108,
    label = "Cds-CsCs_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1109,
    label = "Cds-CsCs_Cds-CdOs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1110,
    label = "Cds-CsCs_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1111,
    label = "Cds-CsCs_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1112,
    label = "Cds-CsCs_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1113,
    label = "Cds-CsCs_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1114,
    label = "Cds-CsCs_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1115,
    label = "Cds-CsCs_Cds-CdSs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1116,
    label = "Cds-CsCs_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1117,
    label = "Cds-CsCs_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1118,
    label = "Cds-CsCs_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1119,
    label = "Cds-CsCs_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1120,
    label = "Cds-CsCs_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1121,
    label = "Cds-CsCs_Cds-CdH",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1122,
    label = "Cds-CsCs_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1123,
    label = "Cds-CsCs_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1124,
    label = "Cds-CsCs_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1125,
    label = "Cds-CsCs_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1126,
    label = "Cds-CsCs_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1127,
    label = "Cds-CsCs_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1128,
    label = "Cds-CsCs_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1129,
    label = "Cds-CsCs_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1130,
    label = "Cds-CsCs_Cds-CdCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1131,
    label = "Cds-CsCs_Cds-CdCb",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1132,
    label = "Cds-CsCs_Cds-CdCO",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1133,
    label = "Cds-CsCs_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1134,
    label = "Cds-CsCs_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1135,
    label = "Cds-CsCs_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1136,
    label = "Cds-CsCs_Cds-(Cd-Cd-Cd)Cd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {5,S}
2 *1 Cd u0 {1,D} {6,S} {7,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {8,S}
5    Cd u0 {1,S}
6    Cs u0 {2,S}
7    Cs u0 {2,S}
8    Cd u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1137,
    label = "Cds-CsCs_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1138,
    label = "Cds-CsCs_Cds-CdC=S",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1139,
    label = "Cds-CsCs_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1140,
    label = "Cds-CsCs_Cds-CtH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1141,
    label = "Cds-CsCs_Cds-CbH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1142,
    label = "Cds-CsCs_Cds-COH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1143,
    label = "Cds-CsCs_Cds-CdH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cs   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1144,
    label = "Cds-CsCs_Cds-C=SH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1145,
    label = "Cds-CsCs_Cds-CtH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1146,
    label = "Cds-CsCs_Cds-CbH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1147,
    label = "Cds-CsCs_Cds-COH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1148,
    label = "Cds-CsCs_Cds-CdH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1149,
    label = "Cds-CsCs_Cds-C=SH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1150,
    label = "Cds-CsCs_Cds-CtH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1151,
    label = "Cds-CsCs_Cds-CbH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1152,
    label = "Cds-CsCs_Cds-COH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1153,
    label = "Cds-CsCs_Cds-CdH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cs   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1154,
    label = "Cds-CsCs_Cds-C=SH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1155,
    label = "Cds-CsCs_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1156,
    label = "Cds-CsCs_Cds-SsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1157,
    label = "Cds-CsCs_Cds-SsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    S2s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1158,
    label = "Cds-CsCs_Cds-SsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    S2s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1159,
    label = "Cds-CsCs_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1160,
    label = "Cds-CsCs_Cds-CsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1161,
    label = "Cds-CsCs_Cds-CsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1162,
    label = "Cds-CsCs_Cds-CsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1163,
    label = "Cds-CsCs_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1164,
    label = "Cds-CsCs_Cds-OsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1165,
    label = "Cds-CsCs_Cds-OsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    O2s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1166,
    label = "Cds-CsCs_Cds-OsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    O2s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1167,
    label = "Cds-CsCs_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1168,
    label = "Cds-CsCs_Cds-HH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1169,
    label = "Cds-CsCs_Cds-HH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1170,
    label = "Cds-CsCs_Cds-HH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1171,
    label = "Cds-CsCs_Cds-HH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1172,
    label = "Cds-CsCs_Cds-HH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1173,
    label = "Cds-CsCs_Cds-HH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1174,
    label = "Cds-CsCs_Cds-HH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1175,
    label = "Cds-CsCs_Cds-HH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1176,
    label = "Cds-CsCs_Cds-HH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1177,
    label = "Cds-Ss/H_or_Val7/Cds",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    S2s      u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R        u0 {2,S}
6    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1178,
    label = "Cds-SsH_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    S2s u0 {1,S}
4    H   u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1179,
    label = "Cds-SsH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    S2s u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1180,
    label = "Cds-SsH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    S2s  u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1181,
    label = "Cds-SsH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    S2s  u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1182,
    label = "Cds-SsCs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    S2s u0 {1,S}
4    Cs  u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1183,
    label = "Cds-SsSs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1184,
    label = "Cds-N3s/H_or_Val7/Cds",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    N3s      u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R        u0 {2,S}
6    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1185,
    label = "Cds-N3sH_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    N3s u0 {1,S}
4    H   u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1186,
    label = "Cds-N3sH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    N3s u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1187,
    label = "Cds-N3sH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    N3s  u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1188,
    label = "Cds-N3sH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    N3s  u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1189,
    label = "Cds-Os/H_or_Val7/Cds",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    O2s      u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R        u0 {2,S}
6    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1190,
    label = "Cds-OsH_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    H   u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1191,
    label = "Cds-OsH_Cds-CsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    H   u0 {1,S}
5    Cs  u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1192,
    label = "Cds-OsH_Cds-CsH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    H   u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1193,
    label = "Cds-OsH_Cds-CsH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O2s  u0 {1,S}
4    H    u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1194,
    label = "Cds-OsH_Cds-CsH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O2s  u0 {1,S}
4    H    u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1195,
    label = "Cds-OsH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1196,
    label = "Cds-OsH_Cds-CsH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1197,
    label = "Cds-OsH_Cds-CsH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O2s  u0 {1,S}
4    F1s  u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1198,
    label = "Cds-OsH_Cds-CsH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O2s  u0 {1,S}
4    F1s  u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1199,
    label = "Cds-OsH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O2s  u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1200,
    label = "Cds-OsH_Cds-CsH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O2s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1201,
    label = "Cds-OsH_Cds-CsH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O2s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1202,
    label = "Cds-OsH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O2s  u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1203,
    label = "Cds-OsH_Cds-CsH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O2s  u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1204,
    label = "Cds-OsCs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    Cs  u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1205,
    label = "Cds-OsOs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1206,
    label = "Cds-OsSs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O2s u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1207,
    label = "Cds-OneDe_Cds",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [H,Cs,O2s,S2s]            u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1208,
    label = "Cds-OneDeCs_Cds",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1209,
    label = "Cds-CtCs_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1210,
    label = "Cds-CtCs_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1211,
    label = "Cds-CtCs_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1212,
    label = "Cds-CtCs_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1213,
    label = "Cds-CtCs_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1214,
    label = "Cds-CtCs_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1215,
    label = "Cds-CtCs_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1216,
    label = "Cds-CtCs_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1217,
    label = "Cds-CtCs_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1218,
    label = "Cds-CtCs_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1219,
    label = "Cds-CtCs_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1220,
    label = "Cds-CtCs_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1221,
    label = "Cds-CtCs_Cds-CdCs",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1222,
    label = "Cds-CtCs_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1223,
    label = "Cds-CtCs_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1224,
    label = "Cds-CtCs_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1225,
    label = "Cds-CtCs_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1226,
    label = "Cds-CtCs_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1227,
    label = "Cds-CtCs_Cds-CdOs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Ct  u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1228,
    label = "Cds-CtCs_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1229,
    label = "Cds-CtCs_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1230,
    label = "Cds-CtCs_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1231,
    label = "Cds-CtCs_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1232,
    label = "Cds-CtCs_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1233,
    label = "Cds-CtCs_Cds-CdSs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Ct  u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1234,
    label = "Cds-CtCs_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1235,
    label = "Cds-CtCs_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1236,
    label = "Cds-CtCs_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1237,
    label = "Cds-CtCs_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1238,
    label = "Cds-CtCs_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1239,
    label = "Cds-CtCs_Cds-CdH",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1240,
    label = "Cds-CtCs_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1241,
    label = "Cds-CtCs_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1242,
    label = "Cds-CtCs_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1243,
    label = "Cds-CtCs_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1244,
    label = "Cds-CtCs_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1245,
    label = "Cds-CtCs_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1246,
    label = "Cds-CtCs_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1247,
    label = "Cds-CtCs_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1248,
    label = "Cds-CtCs_Cds-CdCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1249,
    label = "Cds-CtCs_Cds-CdCb",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1250,
    label = "Cds-CtCs_Cds-CdCO",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1251,
    label = "Cds-CtCs_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1252,
    label = "Cds-CtCs_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1253,
    label = "Cds-CtCs_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1254,
    label = "Cds-CtCs_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1255,
    label = "Cds-CtCs_Cds-CdC=S",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Ct u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1256,
    label = "Cds-CtCs_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1257,
    label = "Cds-CtCs_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1258,
    label = "Cds-CtCs_Cds-SsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1259,
    label = "Cds-CtCs_Cds-SsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    S2s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1260,
    label = "Cds-CtCs_Cds-SsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    S2s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1261,
    label = "Cds-CtCs_Cds-CtH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1262,
    label = "Cds-CtCs_Cds-CbH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1263,
    label = "Cds-CtCs_Cds-COH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1264,
    label = "Cds-CtCs_Cds-CdH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Ct  u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1265,
    label = "Cds-CtCs_Cds-C=SH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1266,
    label = "Cds-CtCs_Cds-CtH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1267,
    label = "Cds-CtCs_Cds-CbH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1268,
    label = "Cds-CtCs_Cds-COH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1269,
    label = "Cds-CtCs_Cds-CdH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Ct   u0 {2,S}
6    Cs   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1270,
    label = "Cds-CtCs_Cds-C=SH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1271,
    label = "Cds-CtCs_Cds-CtH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1272,
    label = "Cds-CtCs_Cds-CbH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1273,
    label = "Cds-CtCs_Cds-COH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1274,
    label = "Cds-CtCs_Cds-CdH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Ct   u0 {2,S}
6    Cs   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1275,
    label = "Cds-CtCs_Cds-C=SH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1276,
    label = "Cds-CtCs_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1277,
    label = "Cds-CtCs_Cds-HH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1278,
    label = "Cds-CtCs_Cds-HH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1279,
    label = "Cds-CtCs_Cds-HH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1280,
    label = "Cds-CtCs_Cds-HH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1281,
    label = "Cds-CtCs_Cds-HH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1282,
    label = "Cds-CtCs_Cds-HH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1283,
    label = "Cds-CtCs_Cds-HH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1284,
    label = "Cds-CtCs_Cds-HH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1285,
    label = "Cds-CtCs_Cds-HH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1286,
    label = "Cds-CtCs_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1287,
    label = "Cds-CtCs_Cds-CsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1288,
    label = "Cds-CtCs_Cds-CsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1289,
    label = "Cds-CtCs_Cds-CsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1290,
    label = "Cds-CtCs_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1291,
    label = "Cds-CtCs_Cds-OsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1292,
    label = "Cds-CtCs_Cds-OsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    O2s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1293,
    label = "Cds-CtCs_Cds-OsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
5    O2s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1294,
    label = "Cds-CbCs_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1295,
    label = "Cds-CbCs_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1296,
    label = "Cds-CbCs_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1297,
    label = "Cds-CbCs_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1298,
    label = "Cds-CbCs_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1299,
    label = "Cds-CbCs_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1300,
    label = "Cds-CbCs_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1301,
    label = "Cds-CbCs_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1302,
    label = "Cds-CbCs_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1303,
    label = "Cds-CbCs_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1304,
    label = "Cds-CbCs_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1305,
    label = "Cds-CbCs_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1306,
    label = "Cds-CbCs_Cds-CdCs",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1307,
    label = "Cds-CbCs_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1308,
    label = "Cds-CbCs_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1309,
    label = "Cds-CbCs_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1310,
    label = "Cds-CbCs_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1311,
    label = "Cds-CbCs_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1312,
    label = "Cds-CbCs_Cds-CdOs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Cb  u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1313,
    label = "Cds-CbCs_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1314,
    label = "Cds-CbCs_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1315,
    label = "Cds-CbCs_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1316,
    label = "Cds-CbCs_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1317,
    label = "Cds-CbCs_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1318,
    label = "Cds-CbCs_Cds-CdSs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Cb  u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1319,
    label = "Cds-CbCs_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1320,
    label = "Cds-CbCs_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1321,
    label = "Cds-CbCs_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1322,
    label = "Cds-CbCs_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1323,
    label = "Cds-CbCs_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1324,
    label = "Cds-CbCs_Cds-CdH",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1325,
    label = "Cds-CbCs_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1326,
    label = "Cds-CbCs_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cs                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1327,
    label = "Cds-CbCs_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1328,
    label = "Cds-CbCs_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1329,
    label = "Cds-CbCs_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1330,
    label = "Cds-CbCs_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1331,
    label = "Cds-CbCs_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1332,
    label = "Cds-CbCs_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1333,
    label = "Cds-CbCs_Cds-CdCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1334,
    label = "Cds-CbCs_Cds-CdCb",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1335,
    label = "Cds-CbCs_Cds-CdCO",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1336,
    label = "Cds-CbCs_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1337,
    label = "Cds-CbCs_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1338,
    label = "Cds-CbCs_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1339,
    label = "Cds-CbCs_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1340,
    label = "Cds-CbCs_Cds-CdC=S",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Cb u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1341,
    label = "Cds-CbCs_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1342,
    label = "Cds-CbCs_Cds-CtH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1343,
    label = "Cds-CbCs_Cds-CbH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1344,
    label = "Cds-CbCs_Cds-COH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1345,
    label = "Cds-CbCs_Cds-CdH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Cb  u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1346,
    label = "Cds-CbCs_Cds-C=SH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1347,
    label = "Cds-CbCs_Cds-CtH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1348,
    label = "Cds-CbCs_Cds-CbH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1349,
    label = "Cds-CbCs_Cds-COH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1350,
    label = "Cds-CbCs_Cds-CdH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cb   u0 {2,S}
6    Cs   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1351,
    label = "Cds-CbCs_Cds-C=SH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1352,
    label = "Cds-CbCs_Cds-CtH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1353,
    label = "Cds-CbCs_Cds-CbH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1354,
    label = "Cds-CbCs_Cds-COH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1355,
    label = "Cds-CbCs_Cds-CdH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Cb   u0 {2,S}
6    Cs   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1356,
    label = "Cds-CbCs_Cds-C=SH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1357,
    label = "Cds-CbCs_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1358,
    label = "Cds-CbCs_Cds-CsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1359,
    label = "Cds-CbCs_Cds-CsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1360,
    label = "Cds-CbCs_Cds-CsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1361,
    label = "Cds-CbCs_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1362,
    label = "Cds-CbCs_Cds-OsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1363,
    label = "Cds-CbCs_Cds-OsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    O2s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1364,
    label = "Cds-CbCs_Cds-OsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    O2s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1365,
    label = "Cds-CbCs_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1366,
    label = "Cds-CbCs_Cds-SsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1367,
    label = "Cds-CbCs_Cds-SsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    S2s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1368,
    label = "Cds-CbCs_Cds-SsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    S2s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1369,
    label = "Cds-CbCs_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1370,
    label = "Cds-CbCs_Cds-HH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1371,
    label = "Cds-CbCs_Cds-HH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1372,
    label = "Cds-CbCs_Cds-HH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1373,
    label = "Cds-CbCs_Cds-HH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1374,
    label = "Cds-CbCs_Cds-HH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1375,
    label = "Cds-CbCs_Cds-HH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1376,
    label = "Cds-CbCs_Cds-HH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1377,
    label = "Cds-CbCs_Cds-HH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1378,
    label = "Cds-CbCs_Cds-HH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1379,
    label = "Cds-COCs_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1380,
    label = "Cds-CdCs_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1381,
    label = "Cds-CdCs_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1382,
    label = "Cds-CdCs_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1383,
    label = "Cds-CdCs_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1384,
    label = "Cds-CdCs_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1385,
    label = "Cds-CdCs_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1386,
    label = "Cds-CdCs_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1387,
    label = "Cds-CdCs_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    R                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1388,
    label = "Cds-CdCs_Cds-OneDe/H_or_Val7/",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    [H,Val7]                  u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1389,
    label = "Cds-CdCs_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1390,
    label = "Cds-CdCs_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1391,
    label = "Cds-CdCs_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1392,
    label = "Cds-CdCs_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1393,
    label = "Cds-CdCs_Cds-(Cd-Cd-Cd)H",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {7,S}
2 *1 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {5,D}
4    Cd u0 {2,S} {8,D}
5    Cd u0 {3,D} {9,S}
6    Cs u0 {2,S}
7    H  u0 {1,S}
8    C  u0 {4,D}
9    Cd u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1394,
    label = "Cds-CdCs_Cds-CdH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1395,
    label = "Cds-CdCs_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1396,
    label = "Cds-CdCs_Cds-OneDeH-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    F1s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1397,
    label = "Cds-CdCs_Cds-CtH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1398,
    label = "Cds-CdCs_Cds-CbH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1399,
    label = "Cds-CdCs_Cds-COH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1400,
    label = "Cds-CdCs_Cds-(Cd-Cd-Cd)H-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {7,S}
2 *1 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {5,D}
4    Cd  u0 {2,S} {8,D}
5    Cd  u0 {3,D} {9,S}
6    Cs  u0 {2,S}
7    F1s u0 {1,S}
8    C   u0 {4,D}
9    Cd  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1401,
    label = "Cds-CdCs_Cds-CdH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    Cs  u0 {1,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1402,
    label = "Cds-CdCs_Cds-C=SH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1403,
    label = "Cds-CdCs_Cds-OneDeH-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    Cl1s                      u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1404,
    label = "Cds-CdCs_Cds-CtH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1405,
    label = "Cds-CdCs_Cds-CbH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1406,
    label = "Cds-CdCs_Cds-COH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1407,
    label = "Cds-CdCs_Cds-(Cd-Cd-Cd)H-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {7,S}
2 *1 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {5,D}
4    Cd   u0 {2,S} {8,D}
5    Cd   u0 {3,D} {9,S}
6    Cs   u0 {2,S}
7    Cl1s u0 {1,S}
8    C    u0 {4,D}
9    Cd   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1408,
    label = "Cds-CdCs_Cds-CdH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Cs   u0 {1,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1409,
    label = "Cds-CdCs_Cds-C=SH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1410,
    label = "Cds-CdCs_Cds-OneDeH-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    Br1s                      u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1411,
    label = "Cds-CdCs_Cds-CtH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1412,
    label = "Cds-CdCs_Cds-CbH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1413,
    label = "Cds-CdCs_Cds-COH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1414,
    label = "Cds-CdCs_Cds-(Cd-Cd-Cd)H-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {7,S}
2 *1 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {5,D}
4    Cd   u0 {2,S} {8,D}
5    Cd   u0 {3,D} {9,S}
6    Cs   u0 {2,S}
7    Br1s u0 {1,S}
8    C    u0 {4,D}
9    Cd   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1415,
    label = "Cds-CdCs_Cds-CdH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Cs   u0 {1,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1416,
    label = "Cds-CdCs_Cds-C=SH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1417,
    label = "Cds-CdCs_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1418,
    label = "Cds-CdCs_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1419,
    label = "Cds-CdCs_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1420,
    label = "Cds-CdCs_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1421,
    label = "Cds-CdCs_Cds-CdCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1422,
    label = "Cds-CdCs_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1423,
    label = "Cds-CdCs_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1424,
    label = "Cds-CdCs_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1425,
    label = "Cds-CdCs_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1426,
    label = "Cds-CdCs_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1427,
    label = "Cds-CdCs_Cds-CdOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    Cs  u0 {1,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1428,
    label = "Cds-CdCs_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1429,
    label = "Cds-CdCs_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1430,
    label = "Cds-CdCs_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1431,
    label = "Cds-CdCs_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1432,
    label = "Cds-CdCs_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1433,
    label = "Cds-CdCs_Cds-CdSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    Cs  u0 {1,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1434,
    label = "Cds-CdCs_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1435,
    label = "Cds-CdCs_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cs                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1436,
    label = "Cds-CdCs_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1437,
    label = "Cds-CdCs_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1438,
    label = "Cds-CdCs_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1439,
    label = "Cds-CdCs_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1440,
    label = "Cds-CdCs_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1441,
    label = "Cds-CdCs_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1442,
    label = "Cds-CdCs_Cds-CdCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1443,
    label = "Cds-CdCs_Cds-CdCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1444,
    label = "Cds-CdCs_Cds-CdCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1445,
    label = "Cds-CdCs_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1446,
    label = "Cds-CdCs_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1447,
    label = "Cds-CdCs_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1448,
    label = "Cds-CdCs_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {8,D}
4    Cd u0 {1,S} {9,D}
5    Cd u0 {2,S} {7,D}
6    Cs u0 {2,S}
7    C  u0 {5,D}
8    C  u0 {3,D}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1449,
    label = "Cds-CdCs_Cds-CdC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1450,
    label = "Cds-CdCs_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1451,
    label = "Cds-CdCs_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1452,
    label = "Cds-CdCs_Cds-CsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1453,
    label = "Cds-CdCs_Cds-CsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1454,
    label = "Cds-CdCs_Cds-CsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1455,
    label = "Cds-CdCs_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1456,
    label = "Cds-CdCs_Cds-OsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    O2s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1457,
    label = "Cds-CdCs_Cds-OsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    O2s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1458,
    label = "Cds-CdCs_Cds-OsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    O2s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1459,
    label = "Cds-CdCs_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1460,
    label = "Cds-CdCs_Cds-SsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    S2s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1461,
    label = "Cds-CdCs_Cds-SsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    S2s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1462,
    label = "Cds-CdCs_Cds-SsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    S2s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1463,
    label = "Cds-CdCs_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1464,
    label = "Cds-CdCs_Cds-HH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1465,
    label = "Cds-CdCs_Cds-HH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1466,
    label = "Cds-CdCs_Cds-HH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1467,
    label = "Cds-CdCs_Cds-HH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1468,
    label = "Cds-CdCs_Cds-HH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1469,
    label = "Cds-CdCs_Cds-HH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1470,
    label = "Cds-CdCs_Cds-HH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1471,
    label = "Cds-CdCs_Cds-HH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1472,
    label = "Cds-CdCs_Cds-HH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1473,
    label = "Cds-C=SCs_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1474,
    label = "Cds-OneDeSs_Cds",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    S2s                       u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1475,
    label = "Cds-CtSs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1476,
    label = "Cds-CbSs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1477,
    label = "Cds-COSs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CO  u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1478,
    label = "Cds-CdSs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1479,
    label = "Cds-C=SSs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CS  u0 {1,S}
4    S2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1480,
    label = "Cds-OneDeOs_Cds",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    O2s                       u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1481,
    label = "Cds-CtOs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1482,
    label = "Cds-CbOs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1483,
    label = "Cds-COOs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CO  u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1484,
    label = "Cds-CdOs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1485,
    label = "Cds-C=SOs_Cds",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CS  u0 {1,S}
4    O2s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1486,
    label = "Cds-OneDeH_Cds",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1487,
    label = "Cds-CtH_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1488,
    label = "Cds-CtH_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1489,
    label = "Cds-CtH_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1490,
    label = "Cds-CtH_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1491,
    label = "Cds-CtH_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1492,
    label = "Cds-CtH_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1493,
    label = "Cds-CtH_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1494,
    label = "Cds-CtH_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1495,
    label = "Cds-CtH_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1496,
    label = "Cds-CtH_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1497,
    label = "Cds-CtH_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1498,
    label = "Cds-CtH_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1499,
    label = "Cds-CtH_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1500,
    label = "Cds-CtH_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1501,
    label = "Cds-CtH_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1502,
    label = "Cds-CtH_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1503,
    label = "Cds-CtH_Cds-CdH",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1504,
    label = "Cds-CtH_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1505,
    label = "Cds-CtH_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1506,
    label = "Cds-CtH_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1507,
    label = "Cds-CtH_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1508,
    label = "Cds-CtH_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1509,
    label = "Cds-CtH_Cds-CdCs",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1510,
    label = "Cds-CtH_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1511,
    label = "Cds-CtH_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1512,
    label = "Cds-CtH_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1513,
    label = "Cds-CtH_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1514,
    label = "Cds-CtH_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1515,
    label = "Cds-CtH_Cds-CdOs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Ct  u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1516,
    label = "Cds-CtH_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1517,
    label = "Cds-CtH_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1518,
    label = "Cds-CtH_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1519,
    label = "Cds-CtH_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1520,
    label = "Cds-CtH_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1521,
    label = "Cds-CtH_Cds-CdSs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Ct  u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1522,
    label = "Cds-CtH_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1523,
    label = "Cds-CtH_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1524,
    label = "Cds-CtH_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1525,
    label = "Cds-CtH_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1526,
    label = "Cds-CtH_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1527,
    label = "Cds-CtH_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1528,
    label = "Cds-CtH_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1529,
    label = "Cds-CtH_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1530,
    label = "Cds-CtH_Cds-CdCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1531,
    label = "Cds-CtH_Cds-CdCb",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1532,
    label = "Cds-CtH_Cds-CdCO",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1533,
    label = "Cds-CtH_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1534,
    label = "Cds-CtH_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1535,
    label = "Cds-CtH_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1536,
    label = "Cds-CtH_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1537,
    label = "Cds-CtH_Cds-CdC=S",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Ct u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1538,
    label = "Cds-CtH_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1539,
    label = "Cds-CtH_Cds-CtH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1540,
    label = "Cds-CtH_Cds-CbH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1541,
    label = "Cds-CtH_Cds-COH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1542,
    label = "Cds-CtH_Cds-C=SH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1543,
    label = "Cds-CtH_Cds-CtH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1544,
    label = "Cds-CtH_Cds-CbH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1545,
    label = "Cds-CtH_Cds-COH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1546,
    label = "Cds-CtH_Cds-C=SH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1547,
    label = "Cds-CtH_Cds-CtH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1548,
    label = "Cds-CtH_Cds-CbH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1549,
    label = "Cds-CtH_Cds-COH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1550,
    label = "Cds-CtH_Cds-C=SH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1551,
    label = "Cds-CbH_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1552,
    label = "Cds-CbH_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1553,
    label = "Cds-CbH_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1554,
    label = "Cds-CbH_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1555,
    label = "Cds-CbH_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1556,
    label = "Cds-CbH_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1557,
    label = "Cds-CbH_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1558,
    label = "Cds-CbH_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1559,
    label = "Cds-CbH_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1560,
    label = "Cds-CbH_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1561,
    label = "Cds-CbH_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1562,
    label = "Cds-CbH_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1563,
    label = "Cds-CbH_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1564,
    label = "Cds-CbH_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1565,
    label = "Cds-CbH_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1566,
    label = "Cds-CbH_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1567,
    label = "Cds-CbH_Cds-CdH",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1568,
    label = "Cds-CbH_Cds-Cd(CdCb)H",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {5,S}
2 *1 Cd u0 {1,D} {6,S} {7,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {8,S}
5    H  u0 {1,S}
6    Cb u0 {2,S}
7    H  u0 {2,S}
8    Cb u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 1569,
    label = "Cds-CbH_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1570,
    label = "Cds-CbH_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1571,
    label = "Cds-CbH_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1572,
    label = "Cds-CbH_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1573,
    label = "Cds-CbH_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1574,
    label = "Cds-CbH_Cds-CdCs",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1575,
    label = "Cds-CbH_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1576,
    label = "Cds-CbH_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1577,
    label = "Cds-CbH_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1578,
    label = "Cds-CbH_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1579,
    label = "Cds-CbH_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1580,
    label = "Cds-CbH_Cds-CdOs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Cb  u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1581,
    label = "Cds-CbH_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1582,
    label = "Cds-CbH_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1583,
    label = "Cds-CbH_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1584,
    label = "Cds-CbH_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1585,
    label = "Cds-CbH_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1586,
    label = "Cds-CbH_Cds-CdSs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Cb  u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1587,
    label = "Cds-CbH_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1588,
    label = "Cds-CbH_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1589,
    label = "Cds-CbH_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1590,
    label = "Cds-CbH_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1591,
    label = "Cds-CbH_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1592,
    label = "Cds-CbH_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1593,
    label = "Cds-CbH_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1594,
    label = "Cds-CbH_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1595,
    label = "Cds-CbH_Cds-CdCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1596,
    label = "Cds-CbH_Cds-CdCb",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1597,
    label = "Cds-CbH_Cds-CdCO",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1598,
    label = "Cds-CbH_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1599,
    label = "Cds-CbH_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1600,
    label = "Cds-CbH_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1601,
    label = "Cds-CbH_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1602,
    label = "Cds-CbH_Cds-CdC=S",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Cb u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1603,
    label = "Cds-CbH_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1604,
    label = "Cds-CbH_Cds-CtH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1605,
    label = "Cds-CbH_Cds-CbH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1606,
    label = "Cds-CbH_Cds-COH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1607,
    label = "Cds-CbH_Cds-C=SH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1608,
    label = "Cds-CbH_Cds-CtH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1609,
    label = "Cds-CbH_Cds-CbH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1610,
    label = "Cds-CbH_Cds-COH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1611,
    label = "Cds-CbH_Cds-C=SH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1612,
    label = "Cds-CbH_Cds-CtH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1613,
    label = "Cds-CbH_Cds-CbH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1614,
    label = "Cds-CbH_Cds-COH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1615,
    label = "Cds-CbH_Cds-C=SH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1616,
    label = "Cds-COH_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1617,
    label = "Cds-CdH_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1618,
    label = "Cds-CdH_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1619,
    label = "Cds-CdH_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1620,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {7,S}
2 *2 Cd u0 {1,D} {4,S} {8,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {2,S} {6,S}
5    Cd u0 {3,D} {6,S}
6    Cs u0 {4,S} {5,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1621,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {6,S}
2 *2 Cd u0 {1,D} {4,S} {7,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {2,S} {5,S}
5    C  u0 {3,D} {4,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1622,
    label = "Cds-CdH_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1623,
    label = "Cds-CdH_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1624,
    label = "Cds-CdH_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1625,
    label = "Cds-CdH_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1626,
    label = "Cds-CdH_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1627,
    label = "Cds-CdH_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1628,
    label = "Cds-CdH_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1629,
    label = "Cds-CdH_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1630,
    label = "Cds-CdH_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    R                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1631,
    label = "Cds-CdH_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1632,
    label = "Cds-CdH_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1633,
    label = "Cds-CdH_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1634,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {7,S}
2 *2 Cd u0 {1,D} {4,S} {8,S}
3    Cd u0 {1,S} {5,D}
4    Cb u0 {2,S} {6,B}
5    Cd u0 {3,D} {6,S}
6    Cb u0 {4,B} {5,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1635,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {6,S}
2 *2 Cd u0 {1,D} {4,S} {7,S}
3    Cd u0 {1,S} {5,S} {8,D}
4    Cb u0 {2,S} {5,B}
5    Cb u0 {3,S} {4,B}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1636,
    label = "Cds-CdH_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1637,
    label = "Cds-CdH_Cds-CdH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1638,
    label = "Cds-CdH_Cds-CdH_cyc5_1",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {6,S}
2 *1 Cd u0 {1,D} {4,S} {7,S}
3    Cd u0 {1,S} {5,S} {8,D}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {3,S} {4,D}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1639,
    label = "Cds-CdH_Cds-CdH_cyc5_2",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {6,S}
2 *2 Cd u0 {1,D} {4,S} {7,S}
3    Cd u0 {1,S} {5,S} {8,D}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {3,S} {4,D}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1640,
    label = "Cds-CdH_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1641,
    label = "Cds-CdH_Cds-OneDeH-HF",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    F1s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1642,
    label = "Cds-CdH_Cds-CtH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1643,
    label = "Cds-CdH_Cds-CbH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1644,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {7,S}
2 *2 Cd  u0 {1,D} {4,S} {8,S}
3    Cd  u0 {1,S} {5,D}
4    Cb  u0 {2,S} {6,B}
5    Cd  u0 {3,D} {6,S}
6    Cb  u0 {4,B} {5,S}
7    H   u0 {1,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1645,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cd  u0 {1,S} {5,S} {8,D}
4    Cb  u0 {2,S} {5,B}
5    Cb  u0 {3,S} {4,B}
6    H   u0 {1,S}
7    F1s u0 {2,S}
8    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1646,
    label = "Cds-CdH_Cds-COH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1647,
    label = "Cds-CdH_Cds-CdH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    H   u0 {1,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1648,
    label = "Cds-CdH_Cds-CdH_cyc5_2-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cd  u0 {1,S} {5,S} {8,D}
4    Cd  u0 {2,S} {5,D}
5    Cd  u0 {3,S} {4,D}
6    H   u0 {1,S}
7    F1s u0 {2,S}
8    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1649,
    label = "Cds-CdH_Cds-C=SH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1650,
    label = "Cds-CdH_Cds-OneDeH-HCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    Cl1s                      u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1651,
    label = "Cds-CdH_Cds-CtH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1652,
    label = "Cds-CdH_Cds-CbH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1653,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {2,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    H    u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1654,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    H    u0 {1,S}
7    Cl1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1655,
    label = "Cds-CdH_Cds-COH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1656,
    label = "Cds-CdH_Cds-CdH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    H    u0 {1,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1657,
    label = "Cds-CdH_Cds-CdH_cyc5_2-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    H    u0 {1,S}
7    Cl1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1658,
    label = "Cds-CdH_Cds-C=SH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1659,
    label = "Cds-CdH_Cds-OneDeH-HBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    Br1s                      u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1660,
    label = "Cds-CdH_Cds-CtH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1661,
    label = "Cds-CdH_Cds-CbH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1662,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {2,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    H    u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1663,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    H    u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1664,
    label = "Cds-CdH_Cds-COH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1665,
    label = "Cds-CdH_Cds-CdH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    H    u0 {1,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1666,
    label = "Cds-CdH_Cds-CdH_cyc5_2-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    H    u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1667,
    label = "Cds-CdH_Cds-C=SH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1668,
    label = "Cds-CdH_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1669,
    label = "Cds-CdH_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1670,
    label = "Cds-CdH_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1671,
    label = "Cds-CdH_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1672,
    label = "Cds-CdH_Cds-CdCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1673,
    label = "Cds-CdH_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1674,
    label = "Cds-CdH_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1675,
    label = "Cds-CdH_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1676,
    label = "Cds-CdH_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1677,
    label = "Cds-CdH_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1678,
    label = "Cds-CdH_Cds-CdOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    H   u0 {1,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1679,
    label = "Cds-CdH_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1680,
    label = "Cds-CdH_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1681,
    label = "Cds-CdH_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1682,
    label = "Cds-CdH_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1683,
    label = "Cds-CdH_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1684,
    label = "Cds-CdH_Cds-CdSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    H   u0 {1,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1685,
    label = "Cds-CdH_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1686,
    label = "Cds-CdH_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    H                         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1687,
    label = "Cds-CdH_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1688,
    label = "Cds-CdH_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1689,
    label = "Cds-CdH_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1690,
    label = "Cds-CdH_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1691,
    label = "Cds-CdH_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1692,
    label = "Cds-CdH_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1693,
    label = "Cds-CdH_Cds-CdCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1694,
    label = "Cds-CdH_Cds-CdCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1695,
    label = "Cds-CdH_Cds-CdCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1696,
    label = "Cds-CdH_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1697,
    label = "Cds-CdH_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1698,
    label = "Cds-CdH_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1699,
    label = "Cds-CdH_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {8,D}
4    Cd u0 {1,S} {9,D}
5    Cd u0 {2,S} {7,D}
6    H  u0 {2,S}
7    C  u0 {5,D}
8    C  u0 {3,D}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1700,
    label = "Cds-CdH_Cds-CdCd_cyc6",
    group = 
"""
1  *2 Cd u0 {2,S} {3,D} {4,S}
2     Cd u0 {1,S} {5,S} {10,D}
3  *1 Cd u0 {1,D} {8,S} {9,S}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {2,S} {7,D}
6     Cd u0 {4,D} {7,S}
7     Cd u0 {5,D} {6,S}
8     Cd u0 {3,S} {11,D}
9     H  u0 {3,S}
10    C  u0 {2,D}
11    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 1701,
    label = "Cds-CdH_Cds-CdCd_cyc6_cyc5",
    group = 
"""
1  *2 Cd u0 {2,S} {3,D} {6,S}
2     Cd u0 {1,S} {5,D} {7,S}
3  *1 Cd u0 {1,D} {4,S} {10,S}
4     Cd u0 {3,S} {5,S} {11,D}
5     C  u0 {2,D} {4,S}
6     Cd u0 {1,S} {8,D}
7     Cd u0 {2,S} {9,D}
8     Cd u0 {6,D} {9,S}
9     Cd u0 {7,D} {8,S}
10    H  u0 {3,S}
11    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1702,
    label = "Cds-CdH_Cds-CdC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    H  u0 {1,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1703,
    label = "Cds-CdH_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1704,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {7,S}
2 *2 Cd  u0 {1,D} {4,S} {8,S}
3    Cd  u0 {1,S} {5,D}
4    Cs  u0 {2,S} {6,S}
5    Cd  u0 {3,D} {6,S}
6    Cs  u0 {4,S} {5,S}
7    H   u0 {1,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1705,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cd  u0 {1,S} {5,D}
4    Cs  u0 {2,S} {5,S}
5    C   u0 {3,D} {4,S}
6    H   u0 {1,S}
7    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1706,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {6,S}
5    Cd   u0 {3,D} {6,S}
6    Cs   u0 {4,S} {5,S}
7    H    u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1707,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {5,S}
5    C    u0 {3,D} {4,S}
6    H    u0 {1,S}
7    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1708,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {6,S}
5    Cd   u0 {3,D} {6,S}
6    Cs   u0 {4,S} {5,S}
7    H    u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1709,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {5,S}
5    C    u0 {3,D} {4,S}
6    H    u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1710,
    label = "Cds-C=SH_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1711,
    label = "Cds-TwoDe_Cds",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1712,
    label = "Cds-CtCt_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1713,
    label = "Cds-CtCt_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1714,
    label = "Cds-CtCt_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1715,
    label = "Cds-CtCt_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1716,
    label = "Cds-CtCt_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1717,
    label = "Cds-CtCt_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1718,
    label = "Cds-CtCt_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1719,
    label = "Cds-CtCt_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1720,
    label = "Cds-CtCt_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1721,
    label = "Cds-CtCt_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1722,
    label = "Cds-CtCt_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1723,
    label = "Cds-CtCt_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1724,
    label = "Cds-CtCt_Cds-CdCs",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1725,
    label = "Cds-CtCt_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1726,
    label = "Cds-CtCt_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1727,
    label = "Cds-CtCt_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1728,
    label = "Cds-CtCt_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1729,
    label = "Cds-CtCt_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1730,
    label = "Cds-CtCt_Cds-CdOs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Ct  u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1731,
    label = "Cds-CtCt_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1732,
    label = "Cds-CtCt_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1733,
    label = "Cds-CtCt_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1734,
    label = "Cds-CtCt_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1735,
    label = "Cds-CtCt_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1736,
    label = "Cds-CtCt_Cds-CdSs",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Ct  u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1737,
    label = "Cds-CtCt_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1738,
    label = "Cds-CtCt_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1739,
    label = "Cds-CtCt_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1740,
    label = "Cds-CtCt_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1741,
    label = "Cds-CtCt_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1742,
    label = "Cds-CtCt_Cds-CdH",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    H  u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1743,
    label = "Cds-CtCt_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1744,
    label = "Cds-CtCt_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Ct                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1745,
    label = "Cds-CtCt_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1746,
    label = "Cds-CtCt_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1747,
    label = "Cds-CtCt_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1748,
    label = "Cds-CtCt_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1749,
    label = "Cds-CtCt_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1750,
    label = "Cds-CtCt_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1751,
    label = "Cds-CtCt_Cds-CdCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1752,
    label = "Cds-CtCt_Cds-CdCb",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1753,
    label = "Cds-CtCt_Cds-CdCO",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1754,
    label = "Cds-CtCt_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1755,
    label = "Cds-CtCt_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1756,
    label = "Cds-CtCt_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1757,
    label = "Cds-CtCt_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1758,
    label = "Cds-CtCt_Cds-CdC=S",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1759,
    label = "Cds-CtCt_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1760,
    label = "Cds-CtCt_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1761,
    label = "Cds-CtCt_Cds-HH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1762,
    label = "Cds-CtCt_Cds-HH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1763,
    label = "Cds-CtCt_Cds-HH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1764,
    label = "Cds-CtCt_Cds-HH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1765,
    label = "Cds-CtCt_Cds-HH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1766,
    label = "Cds-CtCt_Cds-HH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1767,
    label = "Cds-CtCt_Cds-HH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1768,
    label = "Cds-CtCt_Cds-HH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1769,
    label = "Cds-CtCt_Cds-HH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1770,
    label = "Cds-CtCt_Cds-CtH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1771,
    label = "Cds-CtCt_Cds-CbH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1772,
    label = "Cds-CtCt_Cds-COH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1773,
    label = "Cds-CtCt_Cds-CdH-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Ct   u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1774,
    label = "Cds-CtCt_Cds-C=SH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1775,
    label = "Cds-CtCt_Cds-CtH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1776,
    label = "Cds-CtCt_Cds-CbH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1777,
    label = "Cds-CtCt_Cds-COH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1778,
    label = "Cds-CtCt_Cds-CdH-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Ct   u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1779,
    label = "Cds-CtCt_Cds-C=SH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1780,
    label = "Cds-CtCt_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1781,
    label = "Cds-CtCt_Cds-CsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1782,
    label = "Cds-CtCt_Cds-CsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1783,
    label = "Cds-CtCt_Cds-CsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1784,
    label = "Cds-CtCt_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1785,
    label = "Cds-CtCt_Cds-OsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1786,
    label = "Cds-CtCt_Cds-OsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    O2s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1787,
    label = "Cds-CtCt_Cds-OsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    O2s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1788,
    label = "Cds-CtCt_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1789,
    label = "Cds-CtCt_Cds-SsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1790,
    label = "Cds-CtCt_Cds-SsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    S2s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1791,
    label = "Cds-CtCt_Cds-SsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Ct   u0 {1,S}
5    S2s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1792,
    label = "Cds-CtCt_Cds-CtH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1793,
    label = "Cds-CtCt_Cds-CbH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1794,
    label = "Cds-CtCt_Cds-COH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1795,
    label = "Cds-CtCt_Cds-CdH-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Ct  u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1796,
    label = "Cds-CtCt_Cds-C=SH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1797,
    label = "Cds-CtCb_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1798,
    label = "Cds-CtCO_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    CO u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1799,
    label = "Cds-CbCb_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1800,
    label = "Cds-CbCO_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    CO u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1801,
    label = "Cds-COCO_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CO u0 {1,S}
4    CO u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1802,
    label = "Cds-CdCt_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1803,
    label = "Cds-CdCt_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1804,
    label = "Cds-CdCt_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1805,
    label = "Cds-CdCt_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1806,
    label = "Cds-CdCt_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1807,
    label = "Cds-CdCt_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1808,
    label = "Cds-CdCt_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1809,
    label = "Cds-CdCt_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1810,
    label = "Cds-CdCt_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1811,
    label = "Cds-CdCt_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1812,
    label = "Cds-CdCt_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1813,
    label = "Cds-CdCt_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1814,
    label = "Cds-CdCt_Cds-CdCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1815,
    label = "Cds-CdCt_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1816,
    label = "Cds-CdCt_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1817,
    label = "Cds-CdCt_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1818,
    label = "Cds-CdCt_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1819,
    label = "Cds-CdCt_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1820,
    label = "Cds-CdCt_Cds-CdOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    Ct  u0 {1,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1821,
    label = "Cds-CdCt_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1822,
    label = "Cds-CdCt_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1823,
    label = "Cds-CdCt_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1824,
    label = "Cds-CdCt_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1825,
    label = "Cds-CdCt_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1826,
    label = "Cds-CdCt_Cds-CdSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    Ct  u0 {1,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1827,
    label = "Cds-CdCt_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1828,
    label = "Cds-CdCt_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1829,
    label = "Cds-CdCt_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1830,
    label = "Cds-CdCt_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1831,
    label = "Cds-CdCt_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1832,
    label = "Cds-CdCt_Cds-CdH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1833,
    label = "Cds-CdCt_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1834,
    label = "Cds-CdCt_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Ct                        u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1835,
    label = "Cds-CdCt_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1836,
    label = "Cds-CdCt_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1837,
    label = "Cds-CdCt_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1838,
    label = "Cds-CdCt_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1839,
    label = "Cds-CdCt_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1840,
    label = "Cds-CdCt_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    CO u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1841,
    label = "Cds-CdCt_Cds-CdCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1842,
    label = "Cds-CdCt_Cds-CdCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1843,
    label = "Cds-CdCt_Cds-CdCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1844,
    label = "Cds-CdCt_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Ct u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1845,
    label = "Cds-CdCt_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cb u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1846,
    label = "Cds-CdCt_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    CO u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1847,
    label = "Cds-CdCt_Cds-CdCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2 *1 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {8,D}
4    Cd u0 {1,S} {9,D}
5    Cd u0 {2,S} {7,D}
6    Ct u0 {2,S}
7    C  u0 {5,D}
8    C  u0 {3,D}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1848,
    label = "Cds-CdCt_Cds-CdC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {5,S}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {2,S} {8,D}
5    Ct u0 {1,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1849,
    label = "Cds-CdCt_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    CS u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1850,
    label = "Cds-CdCt_Cds-CtH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1851,
    label = "Cds-CdCt_Cds-CbH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1852,
    label = "Cds-CdCt_Cds-COH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1853,
    label = "Cds-CdCt_Cds-CdH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    Ct  u0 {1,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1854,
    label = "Cds-CdCt_Cds-C=SH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1855,
    label = "Cds-CdCt_Cds-CtH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1856,
    label = "Cds-CdCt_Cds-CbH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1857,
    label = "Cds-CdCt_Cds-COH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1858,
    label = "Cds-CdCt_Cds-CdH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Ct   u0 {1,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1859,
    label = "Cds-CdCt_Cds-C=SH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1860,
    label = "Cds-CdCt_Cds-CtH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1861,
    label = "Cds-CdCt_Cds-CbH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1862,
    label = "Cds-CdCt_Cds-COH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1863,
    label = "Cds-CdCt_Cds-CdH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Ct   u0 {1,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1864,
    label = "Cds-CdCt_Cds-C=SH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1865,
    label = "Cds-CdCt_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1866,
    label = "Cds-CdCt_Cds-CsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1867,
    label = "Cds-CdCt_Cds-CsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1868,
    label = "Cds-CdCt_Cds-CsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1869,
    label = "Cds-CdCt_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1870,
    label = "Cds-CdCt_Cds-OsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    O2s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1871,
    label = "Cds-CdCt_Cds-OsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    O2s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1872,
    label = "Cds-CdCt_Cds-OsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    O2s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1873,
    label = "Cds-CdCt_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1874,
    label = "Cds-CdCt_Cds-SsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    S2s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1875,
    label = "Cds-CdCt_Cds-SsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    S2s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1876,
    label = "Cds-CdCt_Cds-SsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    S2s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1877,
    label = "Cds-CdCt_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Ct u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1878,
    label = "Cds-CdCt_Cds-HH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1879,
    label = "Cds-CdCt_Cds-HH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1880,
    label = "Cds-CdCt_Cds-HH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1881,
    label = "Cds-CdCt_Cds-HH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Ct  u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1882,
    label = "Cds-CdCt_Cds-HH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1883,
    label = "Cds-CdCt_Cds-HH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1884,
    label = "Cds-CdCt_Cds-HH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1885,
    label = "Cds-CdCt_Cds-HH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1886,
    label = "Cds-CdCt_Cds-HH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Ct   u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1887,
    label = "Cds-CdCb_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cb u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1888,
    label = "Cds-CdCO_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CO u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1889,
    label = "Cds-CtC=S_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Ct u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1890,
    label = "Cds-CbC=S_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cb u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1891,
    label = "Cds-COC=S_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CO u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1892,
    label = "Cds-CdCd_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1893,
    label = "Cds-CdCd_Cds-CsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1894,
    label = "Cds-CdCd_Cds-OsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1895,
    label = "Cds-CdCd_Cds-OsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1896,
    label = "Cds-CdCd_Cds-SsCs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1897,
    label = "Cds-CdCd_Cds-SsOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1898,
    label = "Cds-CdCd_Cds-SsSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1899,
    label = "Cds-CdCd_Cds-OneDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    [H,Cs,O2s,S2s]            u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1900,
    label = "Cds-CdCd_Cds-OneDeCs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1901,
    label = "Cds-CdCd_Cds-CtCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1902,
    label = "Cds-CdCd_Cds-CbCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1903,
    label = "Cds-CdCd_Cds-COCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1904,
    label = "Cds-CdCd_Cds-CdCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    Cs u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1905,
    label = "Cds-CdCd_Cds-C=SCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1906,
    label = "Cds-CdCd_Cds-OneDeOs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1907,
    label = "Cds-CdCd_Cds-CtOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1908,
    label = "Cds-CdCd_Cds-CbOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1909,
    label = "Cds-CdCd_Cds-COOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1910,
    label = "Cds-CdCd_Cds-CdOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {2,S} {9,D}
6    O2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
9    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1911,
    label = "Cds-CdCd_Cds-C=SOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1912,
    label = "Cds-CdCd_Cds-OneDeSs",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1913,
    label = "Cds-CdCd_Cds-CtSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1914,
    label = "Cds-CdCd_Cds-CbSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1915,
    label = "Cds-CdCd_Cds-COSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1916,
    label = "Cds-CdCd_Cds-CdSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {2,S} {9,D}
6    S2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
9    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1917,
    label = "Cds-CdCd_Cds-C=SSs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1918,
    label = "Cds-CdCd_Cds-OneDeH",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    H                         u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1919,
    label = "Cds-CdCd_Cds-CtH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1920,
    label = "Cds-CdCd_Cds-CbH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1921,
    label = "Cds-CdCd_Cds-COH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1922,
    label = "Cds-CdCd_Cds-CdH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1923,
    label = "Cds-CdCd_Cds-C=SH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1924,
    label = "Cds-CdCd_Cds-TwoDe",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cd                        u0 {1,S} {8,D}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
8    C                         u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1925,
    label = "Cds-CdCd_Cds-CtCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1926,
    label = "Cds-CdCd_Cds-CtCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1927,
    label = "Cds-CdCd_Cds-CtCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1928,
    label = "Cds-CdCd_Cds-CbCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1929,
    label = "Cds-CdCd_Cds-CbCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1930,
    label = "Cds-CdCd_Cds-COCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    CO u0 {2,S}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1931,
    label = "Cds-CdCd_Cds-CdCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    Ct u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1932,
    label = "Cds-CdCd_Cds-CdCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    Cb u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1933,
    label = "Cds-CdCd_Cds-CdCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    CO u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1934,
    label = "Cds-CdCd_Cds-CtC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Ct u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1935,
    label = "Cds-CdCd_Cds-CbC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cb u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1936,
    label = "Cds-CdCd_Cds-COC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    CO u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1937,
    label = "Cds-CdCd_Cds-CdCd",
    group = 
"""
1  *1 Cd u0 {2,D} {3,S} {4,S}
2  *2 Cd u0 {1,D} {5,S} {6,S}
3     Cd u0 {1,S} {7,D}
4     Cd u0 {1,S} {8,D}
5     Cd u0 {2,S} {9,D}
6     Cd u0 {2,S} {10,D}
7     C  u0 {3,D}
8     C  u0 {4,D}
9     C  u0 {5,D}
10    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 1938,
    label = "Cds-CdCd_Cds-CdC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {9,D}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
9    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1939,
    label = "Cds-CdCd_Cds-C=SC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    CS u0 {2,S}
6    CS u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1940,
    label = "Cds-CdCd_Cds-CtH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1941,
    label = "Cds-CdCd_Cds-CbH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1942,
    label = "Cds-CdCd_Cds-COH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1943,
    label = "Cds-CdCd_Cds-CdH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {2,S} {9,D}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
9    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1944,
    label = "Cds-CdCd_Cds-C=SH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1945,
    label = "Cds-CdCd_Cds-CtH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1946,
    label = "Cds-CdCd_Cds-CbH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1947,
    label = "Cds-CdCd_Cds-COH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1948,
    label = "Cds-CdCd_Cds-CdH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cd   u0 {2,S} {9,D}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
9    C    u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1949,
    label = "Cds-CdCd_Cds-C=SH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1950,
    label = "Cds-CdCd_Cds-CtH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1951,
    label = "Cds-CdCd_Cds-CbH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1952,
    label = "Cds-CdCd_Cds-COH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1953,
    label = "Cds-CdCd_Cds-CdH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cd   u0 {2,S} {9,D}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
9    C    u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 1954,
    label = "Cds-CdCd_Cds-C=SH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1955,
    label = "Cds-CdCd_Cds-SsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1956,
    label = "Cds-CdCd_Cds-SsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    S2s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1957,
    label = "Cds-CdCd_Cds-SsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    S2s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1958,
    label = "Cds-CdCd_Cds-SsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    S2s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1959,
    label = "Cds-CdCd_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1960,
    label = "Cds-CdCd_Cds-HH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    H   u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1961,
    label = "Cds-CdCd_Cds-HH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1962,
    label = "Cds-CdCd_Cds-HH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1963,
    label = "Cds-CdCd_Cds-HH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1964,
    label = "Cds-CdCd_Cds-HH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1965,
    label = "Cds-CdCd_Cds-HH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1966,
    label = "Cds-CdCd_Cds-HH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1967,
    label = "Cds-CdCd_Cds-HH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1968,
    label = "Cds-CdCd_Cds-HH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1969,
    label = "Cds-CdCd_Cds-OsH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    H   u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1970,
    label = "Cds-CdCd_Cds-OsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    O2s u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1971,
    label = "Cds-CdCd_Cds-OsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    O2s  u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1972,
    label = "Cds-CdCd_Cds-OsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    O2s  u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1973,
    label = "Cds-CdCd_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {8,D}
5    Cs u0 {2,S}
6    H  u0 {2,S}
7    C  u0 {3,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1974,
    label = "Cds-CdCd_Cds-CsH-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1975,
    label = "Cds-CdCd_Cds-CsH-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1976,
    label = "Cds-CdCd_Cds-CsH-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {1,S} {8,D}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 1977,
    label = "Cds-CdC=S_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1978,
    label = "Cds-C=SC=S_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    CS u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1979,
    label = "Cds-OJ/H_or_Val7/Cds",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    O        u1 {1,S}
4    [H,Val7] u0 {1,S}
5    R        u0 {2,S}
6    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1980,
    label = "Cds-OJH_Cds",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    O  u1 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1981,
    label = "Cds-OJH_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    O  u1 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1982,
    label = "Cds-OJH_Cds-CsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    O  u1 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1983,
    label = "Cds-OJH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O   u1 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1984,
    label = "Cds-OJH_Cds-HH-FFF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O   u1 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1985,
    label = "Cds-OJH_Cds-HH-FFCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    F1s  u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1986,
    label = "Cds-OJH_Cds-HH-FFBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    F1s  u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1987,
    label = "Cds-OJH_Cds-HH-FClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1988,
    label = "Cds-OJH_Cds-HH-FClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1989,
    label = "Cds-OJH_Cds-HH-FBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1990,
    label = "Cds-OJH_Cds-CsH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O   u1 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1991,
    label = "Cds-OJH_Cds-CsH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    F1s  u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1992,
    label = "Cds-OJH_Cds-CsH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    F1s  u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1993,
    label = "Cds-OJH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1994,
    label = "Cds-OJH_Cds-HH-ClClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1995,
    label = "Cds-OJH_Cds-HH-ClClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1996,
    label = "Cds-OJH_Cds-HH-ClBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1997,
    label = "Cds-OJH_Cds-CsH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1998,
    label = "Cds-OJH_Cds-CsH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1999,
    label = "Cds-OJH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2000,
    label = "Cds-OJH_Cds-HH-BrBrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2001,
    label = "Cds-OJH_Cds-CsH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2002,
    label = "Cds-OJNonDe_Cds",
    group = 
"""
1 *1 Cd                    u0 {2,D} {3,S} {4,S}
2 *2 Cd                    u0 {1,D} {5,S} {6,S}
3    O                     u1 {1,S}
4    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
5    R                     u0 {2,S}
6    R                     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2003,
    label = "Cds-OJCs_Cds-/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    O        u1 {1,S}
4    Cs       u0 {1,S}
5    [H,Val7] u0 {2,S}
6    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2004,
    label = "Cds-OJCs_Cds-HH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    O  u1 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2005,
    label = "Cds-OJCs_Cds-HH-HF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O   u1 {1,S}
4    Cs  u0 {1,S}
5    H   u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2006,
    label = "Cds-OJCs_Cds-HH-HCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2007,
    label = "Cds-OJCs_Cds-HH-HBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cs   u0 {1,S}
5    H    u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2008,
    label = "Cds-OJCs_Cds-HH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    O   u1 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2009,
    label = "Cds-OJCs_Cds-HH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2010,
    label = "Cds-OJCs_Cds-HH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cs   u0 {1,S}
5    F1s  u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2011,
    label = "Cds-OJCs_Cds-HH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2012,
    label = "Cds-OJCs_Cds-HH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2013,
    label = "Cds-OJCs_Cds-HH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    O    u1 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2014,
    label = "Cds-OJDe_Cds",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    O                         u1 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2015,
    label = "Cds-OneDeH_Cds-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    F1s                       u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2016,
    label = "Cds-CtH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2017,
    label = "Cds-CtH_Cds-CtH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2018,
    label = "Cds-CtH_Cds-CbH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2019,
    label = "Cds-CtH_Cds-COH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2020,
    label = "Cds-CtH_Cds-C=SH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2021,
    label = "Cds-CtH_Cds-CtH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2022,
    label = "Cds-CtH_Cds-CbH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2023,
    label = "Cds-CtH_Cds-COH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2024,
    label = "Cds-CtH_Cds-CdH-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Ct  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2025,
    label = "Cds-CtH_Cds-C=SH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2026,
    label = "Cds-CtH_Cds-OneDeCs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    F1s                       u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2027,
    label = "Cds-CtH_Cds-CtCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2028,
    label = "Cds-CtH_Cds-CbCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2029,
    label = "Cds-CtH_Cds-COCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2030,
    label = "Cds-CtH_Cds-CdCs-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    Ct  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2031,
    label = "Cds-CtH_Cds-C=SCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2032,
    label = "Cds-CtH_Cds-OneDeOs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    F1s                       u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2033,
    label = "Cds-CtH_Cds-CtOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2034,
    label = "Cds-CtH_Cds-CbOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2035,
    label = "Cds-CtH_Cds-COOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2036,
    label = "Cds-CtH_Cds-CdOs-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Ct  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2037,
    label = "Cds-CtH_Cds-C=SOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2038,
    label = "Cds-CtH_Cds-OneDeSs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    F1s                       u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2039,
    label = "Cds-CtH_Cds-CtSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2040,
    label = "Cds-CtH_Cds-CbSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2041,
    label = "Cds-CtH_Cds-COSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2042,
    label = "Cds-CtH_Cds-CdSs-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Ct  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2043,
    label = "Cds-CtH_Cds-C=SSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2044,
    label = "Cds-CtH_Cds-CdH-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    Ct  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2045,
    label = "Cds-CtH_Cds-CtH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2046,
    label = "Cds-CtH_Cds-CbH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2047,
    label = "Cds-CtH_Cds-COH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2048,
    label = "Cds-CtH_Cds-C=SH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2049,
    label = "Cds-CbH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2050,
    label = "Cds-CbH_Cds-CtH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2051,
    label = "Cds-CbH_Cds-CbH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2052,
    label = "Cds-CbH_Cds-COH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2053,
    label = "Cds-CbH_Cds-C=SH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2054,
    label = "Cds-CbH_Cds-CtH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2055,
    label = "Cds-CbH_Cds-CbH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2056,
    label = "Cds-CbH_Cds-COH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2057,
    label = "Cds-CbH_Cds-C=SH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2058,
    label = "Cds-CbH_Cds-CtH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2059,
    label = "Cds-CbH_Cds-CbH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2060,
    label = "Cds-CbH_Cds-COH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2061,
    label = "Cds-CbH_Cds-CdH-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Cb  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2062,
    label = "Cds-CbH_Cds-Cd(CdCb)H-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 {1,D} {6,S} {7,S}
3    Cd  u0 {1,S} {4,D}
4    Cd  u0 {3,D} {8,S}
5    F1s u0 {1,S}
6    Cb  u0 {2,S}
7    F1s u0 {2,S}
8    Cb  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2063,
    label = "Cds-CbH_Cds-C=SH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2064,
    label = "Cds-CbH_Cds-OneDeCs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    F1s                       u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2065,
    label = "Cds-CbH_Cds-CtCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2066,
    label = "Cds-CbH_Cds-CbCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2067,
    label = "Cds-CbH_Cds-COCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2068,
    label = "Cds-CbH_Cds-CdCs-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cs  u0 {1,S}
5    Cb  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2069,
    label = "Cds-CbH_Cds-C=SCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2070,
    label = "Cds-CbH_Cds-OneDeOs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    F1s                       u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2071,
    label = "Cds-CbH_Cds-CtOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2072,
    label = "Cds-CbH_Cds-CbOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2073,
    label = "Cds-CbH_Cds-COOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2074,
    label = "Cds-CbH_Cds-CdOs-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    O2s u0 {1,S}
5    Cb  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2075,
    label = "Cds-CbH_Cds-C=SOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2076,
    label = "Cds-CbH_Cds-OneDeSs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    F1s                       u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2077,
    label = "Cds-CbH_Cds-CtSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2078,
    label = "Cds-CbH_Cds-CbSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2079,
    label = "Cds-CbH_Cds-COSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2080,
    label = "Cds-CbH_Cds-CdSs-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    S2s u0 {1,S}
5    Cb  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2081,
    label = "Cds-CbH_Cds-C=SSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2082,
    label = "Cds-CbH_Cds-CdH-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    H   u0 {1,S}
5    Cb  u0 {2,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2083,
    label = "Cds-CbH_Cds-Cd(CdCb)H-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 {1,D} {6,S} {7,S}
3    Cd  u0 {1,S} {4,D}
4    Cd  u0 {3,D} {8,S}
5    H   u0 {1,S}
6    Cb  u0 {2,S}
7    F1s u0 {2,S}
8    Cb  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2084,
    label = "Cds-COH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CO  u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2085,
    label = "Cds-CdH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2086,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {6,S}
5    Cd   u0 {3,D} {6,S}
6    Cs   u0 {4,S} {5,S}
7    F1s  u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2087,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {5,S}
5    C    u0 {3,D} {4,S}
6    F1s  u0 {1,S}
7    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2088,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {7,S}
2 *2 Cd  u0 {1,D} {4,S} {8,S}
3    Cd  u0 {1,S} {5,D}
4    Cs  u0 {2,S} {6,S}
5    Cd  u0 {3,D} {6,S}
6    Cs  u0 {4,S} {5,S}
7    F1s u0 {1,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2089,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cd  u0 {1,S} {5,D}
4    Cs  u0 {2,S} {5,S}
5    C   u0 {3,D} {4,S}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2090,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {6,S}
5    Cd   u0 {3,D} {6,S}
6    Cs   u0 {4,S} {5,S}
7    F1s  u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2091,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {5,S}
5    C    u0 {3,D} {4,S}
6    F1s  u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2092,
    label = "Cds-CdH_Cds-OneDeH-FF",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    F1s                       u0 {1,S}
5    F1s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2093,
    label = "Cds-CdH_Cds-CtH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2094,
    label = "Cds-CdH_Cds-CbH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2095,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {7,S}
2 *2 Cd  u0 {1,D} {4,S} {8,S}
3    Cd  u0 {1,S} {5,D}
4    Cb  u0 {2,S} {6,B}
5    Cd  u0 {3,D} {6,S}
6    Cb  u0 {4,B} {5,S}
7    F1s u0 {1,S}
8    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2096,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cd  u0 {1,S} {5,S} {8,D}
4    Cb  u0 {2,S} {5,B}
5    Cb  u0 {3,S} {4,B}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
8    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2097,
    label = "Cds-CdH_Cds-COH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2098,
    label = "Cds-CdH_Cds-CdH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    F1s u0 {1,S}
6    F1s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2099,
    label = "Cds-CdH_Cds-CdH_cyc5_1-FF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {6,S}
2 *1 Cd  u0 {1,D} {4,S} {7,S}
3    Cd  u0 {1,S} {5,S} {8,D}
4    Cd  u0 {2,S} {5,D}
5    Cd  u0 {3,S} {4,D}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
8    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2100,
    label = "Cds-CdH_Cds-CdH_cyc5_2-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {6,S}
2 *2 Cd  u0 {1,D} {4,S} {7,S}
3    Cd  u0 {1,S} {5,S} {8,D}
4    Cd  u0 {2,S} {5,D}
5    Cd  u0 {3,S} {4,D}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
8    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2101,
    label = "Cds-CdH_Cds-C=SH-FF",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2102,
    label = "Cds-CdH_Cds-OneDeH-FCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    F1s                       u0 {1,S}
5    Cl1s                      u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2103,
    label = "Cds-CdH_Cds-CtH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2104,
    label = "Cds-CdH_Cds-CbH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2105,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {2,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    F1s  u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2106,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    F1s  u0 {1,S}
7    Cl1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2107,
    label = "Cds-CdH_Cds-COH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2108,
    label = "Cds-CdH_Cds-CdH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    F1s  u0 {1,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2109,
    label = "Cds-CdH_Cds-CdH_cyc5_2-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    F1s  u0 {1,S}
7    Cl1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2110,
    label = "Cds-CdH_Cds-C=SH-FCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2111,
    label = "Cds-CdH_Cds-OneDeH-FBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    F1s                       u0 {1,S}
5    Br1s                      u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2112,
    label = "Cds-CdH_Cds-CtH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2113,
    label = "Cds-CdH_Cds-CbH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2114,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {2,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    F1s  u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2115,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    F1s  u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2116,
    label = "Cds-CdH_Cds-COH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2117,
    label = "Cds-CdH_Cds-CdH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    F1s  u0 {1,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2118,
    label = "Cds-CdH_Cds-CdH_cyc5_2-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    F1s  u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2119,
    label = "Cds-CdH_Cds-C=SH-FBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2120,
    label = "Cds-CdH_Cds-OneDeCs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    F1s                       u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2121,
    label = "Cds-CdH_Cds-CtCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2122,
    label = "Cds-CdH_Cds-CbCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2123,
    label = "Cds-CdH_Cds-COCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2124,
    label = "Cds-CdH_Cds-CdCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    F1s u0 {1,S}
6    Cs  u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2125,
    label = "Cds-CdH_Cds-C=SCs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2126,
    label = "Cds-CdH_Cds-OneDeOs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    F1s                       u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2127,
    label = "Cds-CdH_Cds-CtOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2128,
    label = "Cds-CdH_Cds-CbOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2129,
    label = "Cds-CdH_Cds-COOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2130,
    label = "Cds-CdH_Cds-CdOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    F1s u0 {1,S}
6    O2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2131,
    label = "Cds-CdH_Cds-C=SOs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    O2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2132,
    label = "Cds-CdH_Cds-OneDeSs-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    F1s                       u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2133,
    label = "Cds-CdH_Cds-CtSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Ct  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2134,
    label = "Cds-CdH_Cds-CbSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    Cb  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2135,
    label = "Cds-CdH_Cds-COSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CO  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2136,
    label = "Cds-CdH_Cds-CdSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {2,S} {8,D}
5    F1s u0 {1,S}
6    S2s u0 {2,S}
7    C   u0 {3,D}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2137,
    label = "Cds-CdH_Cds-C=SSs-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    Cd  u0 {1,S} {7,D}
4    F1s u0 {1,S}
5    S2s u0 {2,S}
6    CS  u0 {2,S}
7    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2138,
    label = "Cds-CdH_Cds-TwoDe-F",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    F1s                       u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2139,
    label = "Cds-CdH_Cds-CdCd_cyc6-F",
    group = 
"""
1  *2 Cd  u0 {2,S} {3,D} {4,S}
2     Cd  u0 {1,S} {5,S} {10,D}
3  *1 Cd  u0 {1,D} {8,S} {9,S}
4     Cd  u0 {1,S} {6,D}
5     Cd  u0 {2,S} {7,D}
6     Cd  u0 {4,D} {7,S}
7     Cd  u0 {5,D} {6,S}
8     Cd  u0 {3,S} {11,D}
9     F1s u0 {3,S}
10    C   u0 {2,D}
11    C   u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 2140,
    label = "Cds-CdH_Cds-CdCd_cyc6_cyc5-F",
    group = 
"""
1  *2 Cd  u0 {2,S} {3,D} {6,S}
2     Cd  u0 {1,S} {5,D} {7,S}
3  *1 Cd  u0 {1,D} {4,S} {10,S}
4     Cd  u0 {3,S} {5,S} {11,D}
5     C   u0 {2,D} {4,S}
6     Cd  u0 {1,S} {8,D}
7     Cd  u0 {2,S} {9,D}
8     Cd  u0 {6,D} {9,S}
9     Cd  u0 {7,D} {8,S}
10    F1s u0 {3,S}
11    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2141,
    label = "Cds-CdH_Cds-CdH_cyc5_1-HF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {6,S}
2 *1 Cd  u0 {1,D} {4,S} {7,S}
3    Cd  u0 {1,S} {5,S} {8,D}
4    Cd  u0 {2,S} {5,D}
5    Cd  u0 {3,S} {4,D}
6    H   u0 {1,S}
7    F1s u0 {2,S}
8    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2142,
    label = "Cds-C=SH_Cds-F",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    CS  u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
6    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2143,
    label = "Cds-OneDeH_Cds-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cl1s                      u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2144,
    label = "Cds-CtH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2145,
    label = "Cds-CtH_Cds-CtH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2146,
    label = "Cds-CtH_Cds-CbH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2147,
    label = "Cds-CtH_Cds-COH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2148,
    label = "Cds-CtH_Cds-CdH-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Ct   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2149,
    label = "Cds-CtH_Cds-C=SH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2150,
    label = "Cds-CtH_Cds-CtH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2151,
    label = "Cds-CtH_Cds-CbH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2152,
    label = "Cds-CtH_Cds-COH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2153,
    label = "Cds-CtH_Cds-C=SH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2154,
    label = "Cds-CtH_Cds-OneDeCs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cl1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2155,
    label = "Cds-CtH_Cds-CtCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2156,
    label = "Cds-CtH_Cds-CbCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2157,
    label = "Cds-CtH_Cds-COCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2158,
    label = "Cds-CtH_Cds-CdCs-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Ct   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2159,
    label = "Cds-CtH_Cds-C=SCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2160,
    label = "Cds-CtH_Cds-OneDeOs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cl1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2161,
    label = "Cds-CtH_Cds-CtOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2162,
    label = "Cds-CtH_Cds-CbOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2163,
    label = "Cds-CtH_Cds-COOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2164,
    label = "Cds-CtH_Cds-CdOs-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    Ct   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2165,
    label = "Cds-CtH_Cds-C=SOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2166,
    label = "Cds-CtH_Cds-OneDeSs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Cl1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2167,
    label = "Cds-CtH_Cds-CtSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2168,
    label = "Cds-CtH_Cds-CbSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2169,
    label = "Cds-CtH_Cds-COSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2170,
    label = "Cds-CtH_Cds-CdSs-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    Ct   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2171,
    label = "Cds-CtH_Cds-C=SSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2172,
    label = "Cds-CtH_Cds-CdH-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Ct   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2173,
    label = "Cds-CbH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2174,
    label = "Cds-CbH_Cds-OneDeCs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cl1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2175,
    label = "Cds-CbH_Cds-CtCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2176,
    label = "Cds-CbH_Cds-CbCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2177,
    label = "Cds-CbH_Cds-COCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2178,
    label = "Cds-CbH_Cds-CdCs-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cb   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2179,
    label = "Cds-CbH_Cds-C=SCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2180,
    label = "Cds-CbH_Cds-OneDeOs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cl1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2181,
    label = "Cds-CbH_Cds-CtOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2182,
    label = "Cds-CbH_Cds-CbOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2183,
    label = "Cds-CbH_Cds-COOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2184,
    label = "Cds-CbH_Cds-CdOs-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    Cb   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2185,
    label = "Cds-CbH_Cds-C=SOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2186,
    label = "Cds-CbH_Cds-OneDeSs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Cl1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2187,
    label = "Cds-CbH_Cds-CtSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2188,
    label = "Cds-CbH_Cds-CbSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2189,
    label = "Cds-CbH_Cds-COSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2190,
    label = "Cds-CbH_Cds-CdSs-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    Cb   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2191,
    label = "Cds-CbH_Cds-C=SSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2192,
    label = "Cds-CbH_Cds-CdH-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cb   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2193,
    label = "Cds-CbH_Cds-Cd(CdCb)H-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    Cb   u0 {2,S}
7    Cl1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2194,
    label = "Cds-CbH_Cds-CtH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2195,
    label = "Cds-CbH_Cds-CbH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2196,
    label = "Cds-CbH_Cds-COH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2197,
    label = "Cds-CbH_Cds-CdH-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cb   u0 {2,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2198,
    label = "Cds-CbH_Cds-Cd(CdCb)H-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    Cl1s u0 {1,S}
6    Cb   u0 {2,S}
7    Cl1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2199,
    label = "Cds-CbH_Cds-C=SH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2200,
    label = "Cds-CbH_Cds-CtH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2201,
    label = "Cds-CbH_Cds-CbH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2202,
    label = "Cds-CbH_Cds-COH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2203,
    label = "Cds-CbH_Cds-C=SH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2204,
    label = "Cds-CbH_Cds-Cd(CdCb)H-FCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    F1s  u0 {1,S}
6    Cb   u0 {2,S}
7    Cl1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2205,
    label = "Cds-COH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    CO   u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2206,
    label = "Cds-CdH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2207,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {6,S}
5    Cd   u0 {3,D} {6,S}
6    Cs   u0 {4,S} {5,S}
7    Cl1s u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2208,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {5,S}
5    C    u0 {3,D} {4,S}
6    Cl1s u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2209,
    label = "Cds-CdH_Cds-OneDeH-ClCl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cl1s                      u0 {1,S}
5    Cl1s                      u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2210,
    label = "Cds-CdH_Cds-CtH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2211,
    label = "Cds-CdH_Cds-CbH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2212,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {2,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    Cl1s u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2213,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    Cl1s u0 {1,S}
7    Cl1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2214,
    label = "Cds-CdH_Cds-COH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2215,
    label = "Cds-CdH_Cds-CdH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Cl1s u0 {1,S}
6    Cl1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2216,
    label = "Cds-CdH_Cds-CdH_cyc5_1-ClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {6,S}
2 *1 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    Cl1s u0 {1,S}
7    Cl1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2217,
    label = "Cds-CdH_Cds-CdH_cyc5_2-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    Cl1s u0 {1,S}
7    Cl1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2218,
    label = "Cds-CdH_Cds-C=SH-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2219,
    label = "Cds-CdH_Cds-OneDeH-ClBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cl1s                      u0 {1,S}
5    Br1s                      u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2220,
    label = "Cds-CdH_Cds-CtH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2221,
    label = "Cds-CdH_Cds-CbH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2222,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {2,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    Cl1s u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2223,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    Cl1s u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2224,
    label = "Cds-CdH_Cds-COH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2225,
    label = "Cds-CdH_Cds-CdH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Cl1s u0 {1,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2226,
    label = "Cds-CdH_Cds-CdH_cyc5_2-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    Cl1s u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2227,
    label = "Cds-CdH_Cds-C=SH-ClBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2228,
    label = "Cds-CdH_Cds-OneDeCs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cl1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2229,
    label = "Cds-CdH_Cds-CtCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2230,
    label = "Cds-CdH_Cds-CbCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2231,
    label = "Cds-CdH_Cds-COCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2232,
    label = "Cds-CdH_Cds-CdCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Cl1s u0 {1,S}
6    Cs   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2233,
    label = "Cds-CdH_Cds-C=SCs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2234,
    label = "Cds-CdH_Cds-OneDeOs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cl1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2235,
    label = "Cds-CdH_Cds-CtOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2236,
    label = "Cds-CdH_Cds-CbOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2237,
    label = "Cds-CdH_Cds-COOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2238,
    label = "Cds-CdH_Cds-CdOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Cl1s u0 {1,S}
6    O2s  u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2239,
    label = "Cds-CdH_Cds-C=SOs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2240,
    label = "Cds-CdH_Cds-OneDeSs-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cl1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2241,
    label = "Cds-CdH_Cds-CtSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2242,
    label = "Cds-CdH_Cds-CbSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2243,
    label = "Cds-CdH_Cds-COSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2244,
    label = "Cds-CdH_Cds-CdSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Cl1s u0 {1,S}
6    S2s  u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2245,
    label = "Cds-CdH_Cds-C=SSs-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cl1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2246,
    label = "Cds-CdH_Cds-TwoDe-Cl",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Cl1s                      u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2247,
    label = "Cds-CdH_Cds-CdCd_cyc6-Cl",
    group = 
"""
1  *2 Cd   u0 {2,S} {3,D} {4,S}
2     Cd   u0 {1,S} {5,S} {10,D}
3  *1 Cd   u0 {1,D} {8,S} {9,S}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {2,S} {7,D}
6     Cd   u0 {4,D} {7,S}
7     Cd   u0 {5,D} {6,S}
8     Cd   u0 {3,S} {11,D}
9     Cl1s u0 {3,S}
10    C    u0 {2,D}
11    C    u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 2248,
    label = "Cds-CdH_Cds-CdCd_cyc6_cyc5-Cl",
    group = 
"""
1  *2 Cd   u0 {2,S} {3,D} {6,S}
2     Cd   u0 {1,S} {5,D} {7,S}
3  *1 Cd   u0 {1,D} {4,S} {10,S}
4     Cd   u0 {3,S} {5,S} {11,D}
5     C    u0 {2,D} {4,S}
6     Cd   u0 {1,S} {8,D}
7     Cd   u0 {2,S} {9,D}
8     Cd   u0 {6,D} {9,S}
9     Cd   u0 {7,D} {8,S}
10    Cl1s u0 {3,S}
11    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2249,
    label = "Cds-CdH_Cds-CdH_cyc5_1-HCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {6,S}
2 *1 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    H    u0 {1,S}
7    Cl1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2250,
    label = "Cds-CdH_Cds-CdH_cyc5_1-FCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {6,S}
2 *1 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    F1s  u0 {1,S}
7    Cl1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2251,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {6,S}
5    Cd   u0 {3,D} {6,S}
6    Cs   u0 {4,S} {5,S}
7    Cl1s u0 {1,S}
8    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2252,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5-ClCl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {5,S}
5    C    u0 {3,D} {4,S}
6    Cl1s u0 {1,S}
7    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2253,
    label = "Cds-C=SH_Cds-Cl",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    CS   u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2254,
    label = "Cds-OneDeH_Cds-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Br1s                      u0 {1,S}
5    R                         u0 {2,S}
6    R                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2255,
    label = "Cds-CtH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2256,
    label = "Cds-CtH_Cds-CtH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2257,
    label = "Cds-CtH_Cds-CbH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2258,
    label = "Cds-CtH_Cds-COH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2259,
    label = "Cds-CtH_Cds-CdH-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Ct   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2260,
    label = "Cds-CtH_Cds-C=SH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2261,
    label = "Cds-CtH_Cds-OneDeCs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Br1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2262,
    label = "Cds-CtH_Cds-CtCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2263,
    label = "Cds-CtH_Cds-CbCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2264,
    label = "Cds-CtH_Cds-COCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2265,
    label = "Cds-CtH_Cds-CdCs-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Ct   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2266,
    label = "Cds-CtH_Cds-C=SCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2267,
    label = "Cds-CtH_Cds-OneDeOs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Br1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2268,
    label = "Cds-CtH_Cds-CtOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2269,
    label = "Cds-CtH_Cds-CbOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2270,
    label = "Cds-CtH_Cds-COOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2271,
    label = "Cds-CtH_Cds-CdOs-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    Ct   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2272,
    label = "Cds-CtH_Cds-C=SOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2273,
    label = "Cds-CtH_Cds-OneDeSs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Ct                        u0 {1,S}
4    Br1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2274,
    label = "Cds-CtH_Cds-CtSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2275,
    label = "Cds-CtH_Cds-CbSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2276,
    label = "Cds-CtH_Cds-COSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2277,
    label = "Cds-CtH_Cds-CdSs-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    Ct   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2278,
    label = "Cds-CtH_Cds-C=SSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2279,
    label = "Cds-CtH_Cds-CdH-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Ct   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2280,
    label = "Cds-CbH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2281,
    label = "Cds-CbH_Cds-OneDeCs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Br1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2282,
    label = "Cds-CbH_Cds-CtCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2283,
    label = "Cds-CbH_Cds-CbCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2284,
    label = "Cds-CbH_Cds-COCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2285,
    label = "Cds-CbH_Cds-CdCs-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cs   u0 {1,S}
5    Cb   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2286,
    label = "Cds-CbH_Cds-C=SCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2287,
    label = "Cds-CbH_Cds-OneDeOs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Br1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2288,
    label = "Cds-CbH_Cds-CtOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2289,
    label = "Cds-CbH_Cds-CbOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2290,
    label = "Cds-CbH_Cds-COOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2291,
    label = "Cds-CbH_Cds-CdOs-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    O2s  u0 {1,S}
5    Cb   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2292,
    label = "Cds-CbH_Cds-C=SOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2293,
    label = "Cds-CbH_Cds-OneDeSs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cb                        u0 {1,S}
4    Br1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2294,
    label = "Cds-CbH_Cds-CtSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2295,
    label = "Cds-CbH_Cds-CbSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2296,
    label = "Cds-CbH_Cds-COSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2297,
    label = "Cds-CbH_Cds-CdSs-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    S2s  u0 {1,S}
5    Cb   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2298,
    label = "Cds-CbH_Cds-C=SSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2299,
    label = "Cds-CbH_Cds-CdH-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    H    u0 {1,S}
5    Cb   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2300,
    label = "Cds-CbH_Cds-Cd(CdCb)H-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    H    u0 {1,S}
6    Cb   u0 {2,S}
7    Br1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2301,
    label = "Cds-CbH_Cds-CtH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2302,
    label = "Cds-CbH_Cds-CbH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2303,
    label = "Cds-CbH_Cds-COH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2304,
    label = "Cds-CbH_Cds-CdH-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Cb   u0 {2,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2305,
    label = "Cds-CbH_Cds-Cd(CdCb)H-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    Br1s u0 {1,S}
6    Cb   u0 {2,S}
7    Br1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2306,
    label = "Cds-CbH_Cds-C=SH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2307,
    label = "Cds-CbH_Cds-Cd(CdCb)H-FBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    F1s  u0 {1,S}
6    Cb   u0 {2,S}
7    Br1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2308,
    label = "Cds-CbH_Cds-Cd(CdCb)H-ClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 {1,D} {6,S} {7,S}
3    Cd   u0 {1,S} {4,D}
4    Cd   u0 {3,D} {8,S}
5    Cl1s u0 {1,S}
6    Cb   u0 {2,S}
7    Br1s u0 {2,S}
8    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2309,
    label = "Cds-COH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    CO   u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2310,
    label = "Cds-CdH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2311,
    label = "Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {6,S}
5    Cd   u0 {3,D} {6,S}
6    Cs   u0 {4,S} {5,S}
7    Br1s u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2312,
    label = "Cds-CdH_Cds-(CsH-Cds)_cyc5-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,D}
4    Cs   u0 {2,S} {5,S}
5    C    u0 {3,D} {4,S}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2313,
    label = "Cds-CdH_Cds-OneDeH-BrBr",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Br1s                      u0 {1,S}
5    Br1s                      u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2314,
    label = "Cds-CdH_Cds-CtH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2315,
    label = "Cds-CdH_Cds-CbH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2316,
    label = "Cds(CdCb)-CdH_Cds-CbH_cycle-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {7,S}
2 *2 Cd   u0 {1,D} {4,S} {8,S}
3    Cd   u0 {1,S} {5,D}
4    Cb   u0 {2,S} {6,B}
5    Cd   u0 {3,D} {6,S}
6    Cb   u0 {4,B} {5,S}
7    Br1s u0 {1,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2317,
    label = "Cds-CdH_Cds-Cb(Cb)H_cycle-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cb   u0 {2,S} {5,B}
5    Cb   u0 {3,S} {4,B}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2318,
    label = "Cds-CdH_Cds-COH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2319,
    label = "Cds-CdH_Cds-CdH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Br1s u0 {1,S}
6    Br1s u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2320,
    label = "Cds-CdH_Cds-CdH_cyc5_1-BrBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {6,S}
2 *1 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2321,
    label = "Cds-CdH_Cds-CdH_cyc5_2-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {6,S}
2 *2 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2322,
    label = "Cds-CdH_Cds-C=SH-BrBr",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2323,
    label = "Cds-CdH_Cds-OneDeCs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Br1s                      u0 {1,S}
5    Cs                        u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2324,
    label = "Cds-CdH_Cds-CtCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2325,
    label = "Cds-CdH_Cds-CbCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2326,
    label = "Cds-CdH_Cds-COCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2327,
    label = "Cds-CdH_Cds-CdCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Br1s u0 {1,S}
6    Cs   u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2328,
    label = "Cds-CdH_Cds-C=SCs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2329,
    label = "Cds-CdH_Cds-OneDeOs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Br1s                      u0 {1,S}
5    O2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2330,
    label = "Cds-CdH_Cds-CtOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2331,
    label = "Cds-CdH_Cds-CbOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2332,
    label = "Cds-CdH_Cds-COOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2333,
    label = "Cds-CdH_Cds-CdOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Br1s u0 {1,S}
6    O2s  u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2334,
    label = "Cds-CdH_Cds-C=SOs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    O2s  u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2335,
    label = "Cds-CdH_Cds-OneDeSs-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Br1s                      u0 {1,S}
5    S2s                       u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2336,
    label = "Cds-CdH_Cds-CtSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Ct   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2337,
    label = "Cds-CdH_Cds-CbSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    Cb   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2338,
    label = "Cds-CdH_Cds-COSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CO   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2339,
    label = "Cds-CdH_Cds-CdSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Cd   u0 {2,S} {8,D}
5    Br1s u0 {1,S}
6    S2s  u0 {2,S}
7    C    u0 {3,D}
8    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2340,
    label = "Cds-CdH_Cds-C=SSs-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    Cd   u0 {1,S} {7,D}
4    Br1s u0 {1,S}
5    S2s  u0 {2,S}
6    CS   u0 {2,S}
7    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2341,
    label = "Cds-CdH_Cds-TwoDe-Br",
    group = 
"""
1 *1 Cd                        u0 {2,D} {3,S} {4,S}
2 *2 Cd                        u0 {1,D} {5,S} {6,S}
3    Cd                        u0 {1,S} {7,D}
4    Br1s                      u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
7    C                         u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2342,
    label = "Cds-CdH_Cds-CdCd_cyc6-Br",
    group = 
"""
1  *2 Cd   u0 {2,S} {3,D} {4,S}
2     Cd   u0 {1,S} {5,S} {10,D}
3  *1 Cd   u0 {1,D} {8,S} {9,S}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {2,S} {7,D}
6     Cd   u0 {4,D} {7,S}
7     Cd   u0 {5,D} {6,S}
8     Cd   u0 {3,S} {11,D}
9     Br1s u0 {3,S}
10    C    u0 {2,D}
11    C    u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 2343,
    label = "Cds-CdH_Cds-CdCd_cyc6_cyc5-Br",
    group = 
"""
1  *2 Cd   u0 {2,S} {3,D} {6,S}
2     Cd   u0 {1,S} {5,D} {7,S}
3  *1 Cd   u0 {1,D} {4,S} {10,S}
4     Cd   u0 {3,S} {5,S} {11,D}
5     C    u0 {2,D} {4,S}
6     Cd   u0 {1,S} {8,D}
7     Cd   u0 {2,S} {9,D}
8     Cd   u0 {6,D} {9,S}
9     Cd   u0 {7,D} {8,S}
10    Br1s u0 {3,S}
11    C    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2344,
    label = "Cds-CdH_Cds-CdH_cyc5_1-HBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {6,S}
2 *1 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    H    u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2345,
    label = "Cds-CdH_Cds-CdH_cyc5_1-FBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {6,S}
2 *1 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    F1s  u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2346,
    label = "Cds-CdH_Cds-CdH_cyc5_1-ClBr",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {6,S}
2 *1 Cd   u0 {1,D} {4,S} {7,S}
3    Cd   u0 {1,S} {5,S} {8,D}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {3,S} {4,D}
6    Cl1s u0 {1,S}
7    Br1s u0 {2,S}
8    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2347,
    label = "Cds-C=SH_Cds-Br",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S} {6,S}
3    CS   u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
6    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2348,
    label = "Ct_R",
    group = 
"""
1 *1 Ct  u0 {2,T}
2 *2 R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2349,
    label = "Ct_Ct",
    group = 
"""
1 *1 Ct u0 {2,T}
2 *2 Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2350,
    label = "Ct-/H_or_Val7/Ct-/H_or_Val7/",
    group = 
"""
1 *1 Ct       u0 {2,T} {3,S}
2 *2 Ct       u0 {1,T} {4,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2351,
    label = "Ct-H_Ct-H",
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
    index = 2352,
    label = "Ct-H_Ct-H-HF",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    H   u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2353,
    label = "Ct-H_Ct-H-HCl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    H    u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2354,
    label = "Ct-H_Ct-H-HBr",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    H    u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2355,
    label = "Ct-H_Ct-H-FF",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2356,
    label = "Ct-H_Ct-H-FCl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2357,
    label = "Ct-H_Ct-H-FBr",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    F1s  u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2358,
    label = "Ct-H_Ct-H-ClCl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2359,
    label = "Ct-H_Ct-H-ClBr",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2360,
    label = "Ct-H_Ct-H-BrBr",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2361,
    label = "Ct-/H_or_Val7/Ct-Cs",
    group = 
"""
1 *1 Ct       u0 {2,T} {3,S}
2 *2 Ct       u0 {1,T} {4,S}
3    [H,Val7] u0 {1,S}
4    Cs       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2362,
    label = "Ct-H_Ct-Cs",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2363,
    label = "Ct-H_Ct-Cs-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    F1s u0 {1,S}
4    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2364,
    label = "Ct-H_Ct-Cs-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cl1s u0 {1,S}
4    Cs   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2365,
    label = "Ct-H_Ct-Cs-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Br1s u0 {1,S}
4    Cs   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2366,
    label = "Ct-Cs_Ct-/H_or_Val7/",
    group = 
"""
1 *1 Ct       u0 {2,T} {3,S}
2 *2 Ct       u0 {1,T} {4,S}
3    Cs       u0 {1,S}
4    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2367,
    label = "Ct-Cs_Ct-H",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2368,
    label = "Ct-Cs_Ct-H-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    Cs  u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2369,
    label = "Ct-Cs_Ct-H-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2370,
    label = "Ct-Cs_Ct-H-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cs   u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2371,
    label = "Ct-Cs_Ct-Cs",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2372,
    label = "Ct-/H_or_Val7/Ct-De",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [H,Val7]                  u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2373,
    label = "Ct-H_Ct-De",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2374,
    label = "Ct-H_Ct-Ct",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2375,
    label = "Ct-H_Ct-Cb",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2376,
    label = "Ct-H_Ct-CO",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2377,
    label = "Ct-H_Ct-Cd",
    group = 
"""
1 *2 Ct u0 {2,T} {3,S}
2 *1 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    H  u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2378,
    label = "Ct-H_Ct-Cd-C-Cb",
    group = 
"""
1 *2 Ct u0 {2,S} {3,T}
2    Cd u0 {1,S} {4,D}
3 *1 Ct u0 {1,T} {5,S}
4    C  u0 {2,D} {6,S}
5    H  u0 {3,S}
6    Cb u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2379,
    label = "Ct-H_Ct-C=S",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    H  u0 {1,S}
4    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2380,
    label = "Ct-H_Ct-De-F",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    F1s                       u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2381,
    label = "Ct-H_Ct-Ct-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    F1s u0 {1,S}
4    Ct  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2382,
    label = "Ct-H_Ct-Cb-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    F1s u0 {1,S}
4    Cb  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2383,
    label = "Ct-H_Ct-CO-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    F1s u0 {1,S}
4    CO  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2384,
    label = "Ct-H_Ct-Cd-F",
    group = 
"""
1 *2 Ct  u0 {2,T} {3,S}
2 *1 Ct  u0 {1,T} {4,S}
3    Cd  u0 {1,S} {5,D}
4    F1s u0 {2,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2385,
    label = "Ct-H_Ct-Cd-C-Cb-F",
    group = 
"""
1 *2 Ct  u0 {2,S} {3,T}
2    Cd  u0 {1,S} {4,D}
3 *1 Ct  u0 {1,T} {5,S}
4    C   u0 {2,D} {6,S}
5    F1s u0 {3,S}
6    Cb  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2386,
    label = "Ct-H_Ct-C=S-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    F1s u0 {1,S}
4    CS  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2387,
    label = "Ct-H_Ct-De-Cl",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    Cl1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2388,
    label = "Ct-H_Ct-Ct-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cl1s u0 {1,S}
4    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2389,
    label = "Ct-H_Ct-Cb-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cl1s u0 {1,S}
4    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2390,
    label = "Ct-H_Ct-CO-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cl1s u0 {1,S}
4    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2391,
    label = "Ct-H_Ct-Cd-Cl",
    group = 
"""
1 *2 Ct   u0 {2,T} {3,S}
2 *1 Ct   u0 {1,T} {4,S}
3    Cd   u0 {1,S} {5,D}
4    Cl1s u0 {2,S}
5    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2392,
    label = "Ct-H_Ct-Cd-C-Cb-Cl",
    group = 
"""
1 *2 Ct   u0 {2,S} {3,T}
2    Cd   u0 {1,S} {4,D}
3 *1 Ct   u0 {1,T} {5,S}
4    C    u0 {2,D} {6,S}
5    Cl1s u0 {3,S}
6    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2393,
    label = "Ct-H_Ct-C=S-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cl1s u0 {1,S}
4    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2394,
    label = "Ct-H_Ct-De-Br",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    Br1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2395,
    label = "Ct-H_Ct-Ct-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Br1s u0 {1,S}
4    Ct   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2396,
    label = "Ct-H_Ct-Cb-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Br1s u0 {1,S}
4    Cb   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2397,
    label = "Ct-H_Ct-CO-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Br1s u0 {1,S}
4    CO   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2398,
    label = "Ct-H_Ct-Cd-Br",
    group = 
"""
1 *2 Ct   u0 {2,T} {3,S}
2 *1 Ct   u0 {1,T} {4,S}
3    Cd   u0 {1,S} {5,D}
4    Br1s u0 {2,S}
5    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2399,
    label = "Ct-H_Ct-Cd-C-Cb-Br",
    group = 
"""
1 *2 Ct   u0 {2,S} {3,T}
2    Cd   u0 {1,S} {4,D}
3 *1 Ct   u0 {1,T} {5,S}
4    C    u0 {2,D} {6,S}
5    Br1s u0 {3,S}
6    Cb   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2400,
    label = "Ct-H_Ct-C=S-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Br1s u0 {1,S}
4    CS   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2401,
    label = "Ct-Cs_Ct-De",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    Cs                        u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2402,
    label = "Ct-Cs_Ct-Ct",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2403,
    label = "Ct-Cs_Ct-Cb",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2404,
    label = "Ct-Cs_Ct-CO",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2405,
    label = "Ct-Cs_Ct-Cd",
    group = 
"""
1 *2 Ct u0 {2,T} {3,S}
2 *1 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2406,
    label = "Ct-Cs_Ct-C=S",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cs u0 {1,S}
4    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2407,
    label = "Ct-De_Ct-/H_or_Val7/",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [H,Val7]                  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2408,
    label = "Ct-De_Ct-H",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2409,
    label = "Ct-Cb_Ct-H",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cb u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2410,
    label = "Ct-CO_Ct-H",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    CO u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2411,
    label = "Ct-Cd_Ct-H",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    H  u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2412,
    label = "Ct-Ct_Ct-H",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Ct u0 {1,S} {5,T}
4    H  u0 {2,S}
5    Ct u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 2413,
    label = "Ct-C=S_Ct-H",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    CS u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2414,
    label = "Ct-De_Ct-H-F",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    F1s                       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2415,
    label = "Ct-Cb_Ct-H-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    Cb  u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2416,
    label = "Ct-CO_Ct-H-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    CO  u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2417,
    label = "Ct-Cd_Ct-H-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    Cd  u0 {1,S} {5,D}
4    F1s u0 {2,S}
5    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2418,
    label = "Ct-Ct_Ct-H-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    Ct  u0 {1,S} {5,T}
4    F1s u0 {2,S}
5    Ct  u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 2419,
    label = "Ct-C=S_Ct-H-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 Ct  u0 {1,T} {4,S}
3    CS  u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2420,
    label = "Ct-De_Ct-H-Cl",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cl1s                      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2421,
    label = "Ct-Cb_Ct-H-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cb   u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2422,
    label = "Ct-CO_Ct-H-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    CO   u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2423,
    label = "Ct-Cd_Ct-H-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cd   u0 {1,S} {5,D}
4    Cl1s u0 {2,S}
5    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2424,
    label = "Ct-Ct_Ct-H-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Ct   u0 {1,S} {5,T}
4    Cl1s u0 {2,S}
5    Ct   u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 2425,
    label = "Ct-C=S_Ct-H-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    CS   u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2426,
    label = "Ct-De_Ct-H-Br",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Br1s                      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2427,
    label = "Ct-Cb_Ct-H-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cb   u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2428,
    label = "Ct-CO_Ct-H-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    CO   u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2429,
    label = "Ct-Cd_Ct-H-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Cd   u0 {1,S} {5,D}
4    Br1s u0 {2,S}
5    C    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2430,
    label = "Ct-Ct_Ct-H-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    Ct   u0 {1,S} {5,T}
4    Br1s u0 {2,S}
5    Ct   u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 2431,
    label = "Ct-C=S_Ct-H-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 Ct   u0 {1,T} {4,S}
3    CS   u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2432,
    label = "Ct-De_Ct-Cs",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2433,
    label = "Ct-Cb_Ct-Cs",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cb u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2434,
    label = "Ct-CO_Ct-Cs",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    CO u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2435,
    label = "Ct-Cd_Ct-Cs",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2436,
    label = "Ct-Ct_Ct-Cs",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Ct u0 {1,S} {5,T}
4    Cs u0 {2,S}
5    C  u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 2437,
    label = "Ct-CS_Ct-Cs",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    CS u0 {1,S}
4    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2438,
    label = "Ct-De_Ct-De",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2439,
    label = "Ct-Ct_Ct-Ct",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Ct u0 {1,S}
4    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2440,
    label = "Ct-Cd_Ct-Ct",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Ct u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2441,
    label = "Ct-Ct_Ct-Cd",
    group = 
"""
1 *2 Ct u0 {2,T} {3,S}
2 *1 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Ct u0 {2,S}
5    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2442,
    label = "Ct-Cd_Ct-Cd",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cd u0 {2,S} {6,D}
5    C  u0 {3,D}
6    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 2443,
    label = "Ct-Cd_Ct-Cd_cyc6",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cd u0 {2,S} {6,D}
5    Cd u0 {3,D} {6,S}
6    Cd u0 {4,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 2444,
    label = "Ct-De_Ct-Cb",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 Ct                        u0 {1,T} {4,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cb                        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2445,
    label = "Ct-Cd_Ct-Cb",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S}
4    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2446,
    label = "Ct-CdCdCb_Ct-Cb_cyc6",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cb u0 {2,S} {6,B}
5    Cd u0 {3,D} {6,S}
6    Cb u0 {4,B} {5,S}
""",
    kinetics = None,
)

entry(
    index = 2447,
    label = "Ct-Cb_Ct-Cd",
    group = 
"""
1 *1 Ct u0 {2,T} {4,S}
2 *2 Ct u0 {1,T} {3,S}
3    Cd u0 {2,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2448,
    label = "Ct-Cb_Ct-CdCdCb_cyc6",
    group = 
"""
1 *2 Ct u0 {2,T} {3,S}
2 *1 Ct u0 {1,T} {4,S}
3    Cd u0 {1,S} {5,D}
4    Cb u0 {2,S} {6,B}
5    Cd u0 {3,D} {6,S}
6    Cb u0 {4,B} {5,S}
""",
    kinetics = None,
)

entry(
    index = 2449,
    label = "Ct-Cb_Ct-CdCb_cyc5",
    group = 
"""
1 *1 Ct u0 {2,T} {4,S}
2 *2 Ct u0 {1,T} {3,S}
3    Cd u0 {2,S} {5,S}
4    Cb u0 {1,S} {5,B}
5    Cb u0 {3,S} {4,B}
""",
    kinetics = None,
)

entry(
    index = 2450,
    label = "Ct-O_Ct",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T}
3    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2451,
    label = "Ct-O_Ct-Cb",
    group = 
"""
1 *1 Ct u0 {2,T} {3,S}
2 *2 Ct u0 {1,T} {4,S}
3    O  u0 {1,S}
4    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2452,
    label = "Ct_Nt",
    group = 
"""
1 *1 Ct         u0 {2,T}
2 *2 [N3t,N5tc] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2453,
    label = "Ct_N3t",
    group = 
"""
1 *1 Ct  u0 {2,T}
2 *2 N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2454,
    label = "Ct-/H_or_Val7/N3t",
    group = 
"""
1 *1 Ct       u0 {2,T} {3,S}
2 *2 N3t      u0 {1,T}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2455,
    label = "Ct-H_N3t",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 N3t u0 {1,T}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2456,
    label = "Ct-H_N3t-F",
    group = 
"""
1 *1 Ct  u0 {2,T} {3,S}
2 *2 N3t u0 {1,T}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2457,
    label = "Ct-H_N3t-Cl",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 N3t  u0 {1,T}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2458,
    label = "Ct-H_N3t-Br",
    group = 
"""
1 *1 Ct   u0 {2,T} {3,S}
2 *2 N3t  u0 {1,T}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2459,
    label = "Ct-NonDe_N3t",
    group = 
"""
1 *1 Ct                    u0 {2,T} {3,S}
2 *2 N3t                   u0 {1,T}
3    [Cs,N3s,N5sc,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2460,
    label = "Ct-OneDe_N3t",
    group = 
"""
1 *1 Ct                        u0 {2,T} {3,S}
2 *2 N3t                       u0 {1,T}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2461,
    label = "Ct_N5t",
    group = 
"""
1 *1 Ct   u0 {2,T}
2 *2 N5tc u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2462,
    label = "Od_R",
    group = 
"""
1 *1 O2d u0 {2,D}
2 *2 R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2463,
    label = "Od_CO",
    group = 
"""
1 *2 C   u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2464,
    label = "Od_CO-/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *2 CO       u0 {2,D} {3,S} {4,S}
2 *1 O2d      u0 {1,D}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2465,
    label = "Od_CO-HH",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2466,
    label = "Od_CO-HH-HF",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2467,
    label = "Od_CO-HH-HCl",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2468,
    label = "Od_CO-HH-HBr",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2469,
    label = "Od_CO-HH-FF",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2470,
    label = "Od_CO-HH-FCl",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2471,
    label = "Od_CO-HH-FBr",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2472,
    label = "Od_CO-HH-ClCl",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2473,
    label = "Od_CO-HH-ClBr",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2474,
    label = "Od_CO-HH-BrBr",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2475,
    label = "Od_CO-Nd/H_or_Val7/",
    group = 
"""
1 *2 CO           u0 {2,D} {3,S} {4,S}
2 *1 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    [H,Val7]     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2476,
    label = "Od_CO-NdH",
    group = 
"""
1 *2 CO           u0 {2,D} {3,S} {4,S}
2 *1 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    H            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2477,
    label = "Od_CO-CsH",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2478,
    label = "Od_CO-NdH-F",
    group = 
"""
1 *2 CO           u0 {2,D} {3,S} {4,S}
2 *1 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    F1s          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2479,
    label = "Od_CO-CsH-F",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2480,
    label = "Od_CO-NdH-Cl",
    group = 
"""
1 *2 CO           u0 {2,D} {3,S} {4,S}
2 *1 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    Cl1s         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2481,
    label = "Od_CO-CsH-Cl",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2482,
    label = "Od_CO-NdH-Br",
    group = 
"""
1 *2 CO           u0 {2,D} {3,S} {4,S}
2 *1 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    Br1s         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2483,
    label = "Od_CO-CsH-Br",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2484,
    label = "Od_CO-NdNd",
    group = 
"""
1 *2 CO           u0 {2,D} {3,S} {4,S}
2 *1 O2d          u0 {1,D}
3    [Cs,O2s,S2s] u0 {1,S}
4    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2485,
    label = "Od_CO-CsCs",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2486,
    label = "Od_CO-De/H_or_Val7/",
    group = 
"""
1 *2 CO               u0 {2,D} {3,S} {4,S}
2 *1 O2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [H,Val7]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2487,
    label = "Od_CO-DeH",
    group = 
"""
1 *2 CO               u0 {2,D} {3,S} {4,S}
2 *1 O2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2488,
    label = "Od_CO-CdH",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cd  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2489,
    label = "Od_CO-CtH",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2490,
    label = "Od_CO-DeH-F",
    group = 
"""
1 *2 CO               u0 {2,D} {3,S} {4,S}
2 *1 O2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    F1s              u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2491,
    label = "Od_CO-CdH-F",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cd  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2492,
    label = "Od_CO-CtH-F",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2493,
    label = "Od_CO-DeH-Cl",
    group = 
"""
1 *2 CO               u0 {2,D} {3,S} {4,S}
2 *1 O2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cl1s             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2494,
    label = "Od_CO-CdH-Cl",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    Cd   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2495,
    label = "Od_CO-CtH-Cl",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2496,
    label = "Od_CO-DeH-Br",
    group = 
"""
1 *2 CO               u0 {2,D} {3,S} {4,S}
2 *1 O2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Br1s             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2497,
    label = "Od_CO-CdH-Br",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    Cd   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2498,
    label = "Od_CO-CtH-Br",
    group = 
"""
1 *2 CO   u0 {2,D} {3,S} {4,S}
2 *1 O2d  u0 {1,D}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2499,
    label = "Od_CO-DeNd",
    group = 
"""
1 *2 CO               u0 {2,D} {3,S} {4,S}
2 *1 O2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O2s,S2s]     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2500,
    label = "Od_CO-CdCs",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Cd  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2501,
    label = "Od_CO-CtCs",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S} {4,S}
2 *1 O2d u0 {1,D}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2502,
    label = "Od_Cdd",
    group = 
"""
1 *2 C   u0 {2,D} {3,D}
2 *1 O2d u0 {1,D}
3    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2503,
    label = "Od_Cdd-O2d",
    group = 
"""
1 *2 C   u0 {2,D} {3,D}
2 *1 O2d u0 {1,D}
3    O   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2504,
    label = "Od_Nd",
    group = 
"""
1 *1 O2d u0 {2,D}
2 *2 N   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2505,
    label = "Od_N3d",
    group = 
"""
1 *1 O2d u0 {2,D}
2 *2 N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2506,
    label = "Od_N5dc",
    group = 
"""
1 *1 O2d  u0 {2,D}
2 *2 N5dc u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2507,
    label = "Nd_R",
    group = "OR{N1dc_R, N3d_R}",
    kinetics = None,
)

entry(
    index = 2508,
    label = "N1dc_R",
    group = 
"""
1 *1 N1dc u0 p2 {2,D}
2 *2 R!H  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2509,
    label = "N3d_R",
    group = 
"""
1 *1 N3d u0 {2,D}
2 *2 R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2510,
    label = "N3d_Cd",
    group = 
"""
1 *1 N3d      u0 {2,D}
2 *2 [Cd,Cdd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2511,
    label = "N3d_Cds",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2512,
    label = "N3d-/H_or_Val7/Cds",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S} {4,S}
2 *1 N3d      u0 {1,D} {5,S}
3    R        u0 {1,S}
4    R        u0 {1,S}
5    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2513,
    label = "N3d-H_Cds",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2514,
    label = "N3d-H_Cds-HH",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2515,
    label = "N3d-H_Cds-NonDeH",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    H                     u0 {1,S}
5    H                     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2516,
    label = "N3d-H_Cds-NonDe2",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
5    H                     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2517,
    label = "N3d-H_Cds-F",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2518,
    label = "N3d-H_Cds-HH-HHF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2519,
    label = "N3d-H_Cds-HH-HFF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2520,
    label = "N3d-H_Cds-HH-FFF",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2521,
    label = "N3d-H_Cds-NonDeH-HF",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    H                     u0 {1,S}
5    F1s                   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2522,
    label = "N3d-H_Cds-NonDeH-FF",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    F1s                   u0 {1,S}
5    F1s                   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2523,
    label = "N3d-H_Cds-NonDe2-F",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
5    F1s                   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2524,
    label = "N3d-H_Cds-Cl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 N3d  u0 {1,D} {5,S}
3    R    u0 {1,S}
4    R    u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2525,
    label = "N3d-H_Cds-HH-HHCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 N3d  u0 {1,D} {5,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2526,
    label = "N3d-H_Cds-HH-HFCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 N3d  u0 {1,D} {5,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2527,
    label = "N3d-H_Cds-HH-HClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 N3d  u0 {1,D} {5,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2528,
    label = "N3d-H_Cds-HH-FFCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 N3d  u0 {1,D} {5,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2529,
    label = "N3d-H_Cds-HH-FClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 N3d  u0 {1,D} {5,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2530,
    label = "N3d-H_Cds-HH-ClClCl",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 N3d  u0 {1,D} {5,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2531,
    label = "N3d-H_Cds-NonDeH-HCl",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    H                     u0 {1,S}
5    Cl1s                  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2532,
    label = "N3d-H_Cds-NonDeH-FCl",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    F1s                   u0 {1,S}
5    Cl1s                  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2533,
    label = "N3d-H_Cds-NonDeH-ClCl",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    Cl1s                  u0 {1,S}
5    Cl1s                  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2534,
    label = "N3d-H_Cds-NonDe2-Cl",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
4    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
5    Cl1s                  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2535,
    label = "N3d-H_Cds-Br",
    group = 
"""
1 *2 Cd   u0 {2,D} {3,S} {4,S}
2 *1 N3d  u0 {1,D} {5,S}
3    R    u0 {1,S}
4    R    u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2536,
    label = "N3d-NonDe_Cds",
    group = 
"""
1 *2 Cd                    u0 {2,D} {3,S} {4,S}
2 *1 N3d                   u0 {1,D} {5,S}
3    R!H                   u0 {1,S}
4    R!H                   u0 {1,S}
5    [Cs,N3s,N5sc,O2s,S2s] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2537,
    label = "N3d-OneDe_Cds",
    group = 
"""
1 *2 Cd                        u0 {2,D} {3,S} {4,S}
2 *1 N3d                       u0 {1,D} {5,S}
3    R!H                       u0 {1,S}
4    R!H                       u0 {1,S}
5    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2538,
    label = "N3d_Cdd",
    group = 
"""
1 *1 N3d u0 {2,D}
2 *2 Cdd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2539,
    label = "N3d_Od",
    group = 
"""
1 *1 N3d u0 {2,D}
2 *2 O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2540,
    label = "N3d-/H_or_Val7/Od",
    group = 
"""
1 *1 N3d      u0 {2,D} {3,S}
2 *2 O2d      u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2541,
    label = "N3d-H_Od",
    group = 
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 O2d u0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2542,
    label = "N3d-H_Od-F",
    group = 
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 O2d u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2543,
    label = "N3d-H_Od-Cl",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 O2d  u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2544,
    label = "N3d-H_Od-Br",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 O2d  u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2545,
    label = "N3d-NonDe_Od",
    group = 
"""
1 *1 N3d              u0 {2,D} {3,S}
2 *2 O2d              u0 {1,D}
3    [Cs,N3s,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2546,
    label = "N3d-OneDe_Od",
    group = 
"""
1 *1 N3d                       u0 {2,D} {3,S}
2 *2 O2d                       u0 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2547,
    label = "N3d_Nd",
    group = 
"""
1 *1 N3d u0 {2,D}
2 *2 N   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2548,
    label = "N3d_N3d",
    group = 
"""
1 *1 N3d u0 {2,D}
2 *2 N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2549,
    label = "N3d-/H_or_Val7/N3d",
    group = 
"""
1 *1 N3d      u0 {2,D} {3,S}
2 *2 N3d      u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2550,
    label = "N3d-H_N3d",
    group = 
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 N3d u0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2551,
    label = "N3d-H_N3d-H",
    group = 
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 N3d u0 {1,D} {4,S}
3    H   u0 {1,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2552,
    label = "N3d-H_N3d-H-HF",
    group = 
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 N3d u0 {1,D} {4,S}
3    H   u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2553,
    label = "N3d-H_N3d-H-HCl",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 N3d  u0 {1,D} {4,S}
3    H    u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2554,
    label = "N3d-H_N3d-H-HBr",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 N3d  u0 {1,D} {4,S}
3    H    u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2555,
    label = "N3d-H_N3d-NonDe",
    group = 
"""
1 *1 N3d              u0 {2,D} {3,S}
2 *2 N3d              u0 {1,D} {4,S}
3    H                u0 {1,S}
4    [Cs,N3s,O2s,S2s] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2556,
    label = "N3d-H_N3d-OneDe",
    group = 
"""
1 *1 N3d                       u0 {2,D} {3,S}
2 *2 N3d                       u0 {1,D} {4,S}
3    H                         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2557,
    label = "N3d-H_N3d-F",
    group = 
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 N3d u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2558,
    label = "N3d-H_N3d-H-FF",
    group = 
"""
1 *1 N3d u0 {2,D} {3,S}
2 *2 N3d u0 {1,D} {4,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2559,
    label = "N3d-H_N3d-H-FCl",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 N3d  u0 {1,D} {4,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2560,
    label = "N3d-H_N3d-H-FBr",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 N3d  u0 {1,D} {4,S}
3    F1s  u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2561,
    label = "N3d-H_N3d-NonDe-F",
    group = 
"""
1 *1 N3d              u0 {2,D} {3,S}
2 *2 N3d              u0 {1,D} {4,S}
3    F1s              u0 {1,S}
4    [Cs,N3s,O2s,S2s] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2562,
    label = "N3d-H_N3d-OneDe-F",
    group = 
"""
1 *1 N3d                       u0 {2,D} {3,S}
2 *2 N3d                       u0 {1,D} {4,S}
3    F1s                       u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2563,
    label = "N3d-H_N3d-Cl",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 N3d  u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2564,
    label = "N3d-H_N3d-H-ClCl",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 N3d  u0 {1,D} {4,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2565,
    label = "N3d-H_N3d-H-ClBr",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 N3d  u0 {1,D} {4,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2566,
    label = "N3d-H_N3d-NonDe-Cl",
    group = 
"""
1 *1 N3d              u0 {2,D} {3,S}
2 *2 N3d              u0 {1,D} {4,S}
3    Cl1s             u0 {1,S}
4    [Cs,N3s,O2s,S2s] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2567,
    label = "N3d-H_N3d-OneDe-Cl",
    group = 
"""
1 *1 N3d                       u0 {2,D} {3,S}
2 *2 N3d                       u0 {1,D} {4,S}
3    Cl1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2568,
    label = "N3d-H_N3d-Br",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 N3d  u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2569,
    label = "N3d-H_N3d-H-BrBr",
    group = 
"""
1 *1 N3d  u0 {2,D} {3,S}
2 *2 N3d  u0 {1,D} {4,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2570,
    label = "N3d-H_N3d-NonDe-Br",
    group = 
"""
1 *1 N3d              u0 {2,D} {3,S}
2 *2 N3d              u0 {1,D} {4,S}
3    Br1s             u0 {1,S}
4    [Cs,N3s,O2s,S2s] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2571,
    label = "N3d-H_N3d-OneDe-Br",
    group = 
"""
1 *1 N3d                       u0 {2,D} {3,S}
2 *2 N3d                       u0 {1,D} {4,S}
3    Br1s                      u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2572,
    label = "N3d-NonDe_N3d",
    group = 
"""
1 *1 N3d              u0 {2,D} {3,S}
2 *2 N3d              u0 {1,D}
3    [Cs,N3s,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2573,
    label = "N3d-OneDe_N3d",
    group = 
"""
1 *1 N3d                       u0 {2,D} {3,S}
2 *2 N3d                       u0 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2574,
    label = "N3d_N5dc",
    group = 
"""
1 *1 N3d         u0 {2,D}
2 *2 [N5dc,N5tc] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2575,
    label = "Nt_R",
    group = "OR{N3t_R, N5t_R}",
    kinetics = None,
)

entry(
    index = 2576,
    label = "N3t_R",
    group = 
"""
1 *1 N3t u0 {2,T}
2 *2 R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2577,
    label = "N3t_Ct",
    group = 
"""
1 *1 N3t u0 {2,T}
2 *2 Ct  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2578,
    label = "N3t_Ct-/H_or_Val7/",
    group = 
"""
1 *2 Ct       u0 {2,T} {3,S}
2 *1 N3t      u0 {1,T}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2579,
    label = "N3t_Ct-H",
    group = 
"""
1 *2 Ct  u0 {2,T} {3,S}
2 *1 N3t u0 {1,T}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2580,
    label = "N3t_Ct-H-F",
    group = 
"""
1 *2 Ct  u0 {2,T} {3,S}
2 *1 N3t u0 {1,T}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2581,
    label = "N3t_Ct-H-Cl",
    group = 
"""
1 *2 Ct   u0 {2,T} {3,S}
2 *1 N3t  u0 {1,T}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2582,
    label = "N3t_Ct-H-Br",
    group = 
"""
1 *2 Ct   u0 {2,T} {3,S}
2 *1 N3t  u0 {1,T}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2583,
    label = "N3t_Ct-NonDe",
    group = 
"""
1 *2 Ct                    u0 {2,T} {3,S}
2 *1 N3t                   u0 {1,T}
3    [Cs,N3s,N5sc,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2584,
    label = "N3t_Ct-OneDe",
    group = 
"""
1 *2 Ct                        u0 {2,T} {3,S}
2 *1 N3t                       u0 {1,T}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2585,
    label = "N3t_N3t",
    group = 
"""
1 *1 N3t u0 {2,T}
2 *2 N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2586,
    label = "N5t_R",
    group = 
"""
1 *1 N5tc u0 {2,T}
2 *2 R!H  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2587,
    label = "Sd_R",
    group = 
"""
1 *1 S   u0 {2,D}
2 *2 R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2588,
    label = "Sd_Cdd",
    group = 
"""
1 *2 Cdd u0 {2,D} {3,D}
2 *1 S2d u0 p2 {1,D}
3    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2589,
    label = "Sd_Cdd-S2d",
    group = 
"""
1 *2 Cdd u0 {2,D} {3,D}
2 *1 S2d u0 p2 {1,D}
3    S2d u0 p2 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2590,
    label = "Sd_Cd",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2591,
    label = "Sd_Cds-/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *2 CS       u0 {2,D} {3,S} {4,S}
2 *1 S2d      u0 p2 {1,D}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2592,
    label = "Sd_Cds-HH",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2593,
    label = "Sd_Cds-HH-HF",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2594,
    label = "Sd_Cds-HH-HCl",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2595,
    label = "Sd_Cds-HH-HBr",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2596,
    label = "Sd_Cds-HH-FF",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2597,
    label = "Sd_Cds-HH-FCl",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2598,
    label = "Sd_Cds-HH-FBr",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2599,
    label = "Sd_Cds-HH-ClCl",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2600,
    label = "Sd_Cds-HH-ClBr",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2601,
    label = "Sd_Cds-HH-BrBr",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2602,
    label = "Sd_Cds-Cs/H_or_Val7/",
    group = 
"""
1 *2 CS       u0 {2,D} {3,S} {4,S}
2 *1 S2d      u0 p2 {1,D}
3    Cs       u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2603,
    label = "Sd_Cds-CsH",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2604,
    label = "Sd_Cds-CsH-F",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2605,
    label = "Sd_Cds-CsH-Cl",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2606,
    label = "Sd_Cds-CsH-Br",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2607,
    label = "Sd_Cds-Os/H_or_Val7/",
    group = 
"""
1 *2 CS       u0 {2,D} {3,S} {4,S}
2 *1 S2d      u0 p2 {1,D}
3    O2s      u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2608,
    label = "Sd_Cds-OsH",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2609,
    label = "Sd_Cds-OsH-F",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2610,
    label = "Sd_Cds-OsH-Cl",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    O2s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2611,
    label = "Sd_Cds-OsH-Br",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    O2s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2612,
    label = "Sd_Cds-OsCs",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    O2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2613,
    label = "Sd_Cds-CsCs",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2614,
    label = "Sd_Cds-OneDe/H_or_Val7/",
    group = 
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [H,Val7]                  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2615,
    label = "Sd_Cds-OneDeH",
    group = 
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2616,
    label = "Sd_Cds-CtH",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2617,
    label = "Sd_Cds-CbH",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2618,
    label = "Sd_Cds-COH",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2619,
    label = "Sd_Cds-CdH",
    group = 
"""
1 *2 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *1 S2d u0 p2 {1,D}
4    H   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2620,
    label = "Sd_Cds-C=SH",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2621,
    label = "Sd_Cds-OneDeH-F",
    group = 
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    F1s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2622,
    label = "Sd_Cds-CtH-F",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2623,
    label = "Sd_Cds-CbH-F",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2624,
    label = "Sd_Cds-COH-F",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2625,
    label = "Sd_Cds-CdH-F",
    group = 
"""
1 *2 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *1 S2d u0 p2 {1,D}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2626,
    label = "Sd_Cds-C=SH-F",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2627,
    label = "Sd_Cds-OneDeH-Cl",
    group = 
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cl1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2628,
    label = "Sd_Cds-CtH-Cl",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    Ct   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2629,
    label = "Sd_Cds-CbH-Cl",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    Cb   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2630,
    label = "Sd_Cds-COH-Cl",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    CO   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2631,
    label = "Sd_Cds-CdH-Cl",
    group = 
"""
1 *2 CS   u0 {2,S} {3,D} {4,S}
2    Cd   u0 {1,S} {5,D}
3 *1 S2d  u0 p2 {1,D}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2632,
    label = "Sd_Cds-C=SH-Cl",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    CS   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2633,
    label = "Sd_Cds-OneDeH-Br",
    group = 
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Br1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2634,
    label = "Sd_Cds-CtH-Br",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    Ct   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2635,
    label = "Sd_Cds-CbH-Br",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    Cb   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2636,
    label = "Sd_Cds-COH-Br",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    CO   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2637,
    label = "Sd_Cds-CdH-Br",
    group = 
"""
1 *2 CS   u0 {2,S} {3,D} {4,S}
2    Cd   u0 {1,S} {5,D}
3 *1 S2d  u0 p2 {1,D}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2638,
    label = "Sd_Cds-C=SH-Br",
    group = 
"""
1 *2 CS   u0 {2,D} {3,S} {4,S}
2 *1 S2d  u0 p2 {1,D}
3    CS   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2639,
    label = "Sd_Cds-OneDeCs",
    group = 
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2640,
    label = "Sd_Cds-CtCs",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2641,
    label = "Sd_Cds-CbCs",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2642,
    label = "Sd_Cds-COCs",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2643,
    label = "Sd_Cds-CdCs",
    group = 
"""
1 *2 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *1 S2d u0 p2 {1,D}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2644,
    label = "Sd_Cds-C=SCs",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2645,
    label = "Sd_Cds-TwoDe",
    group = 
"""
1 *2 CS                        u0 {2,D} {3,S} {4,S}
2 *1 S2d                       u0 p2 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2646,
    label = "Sd_Cds-CtCt",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2647,
    label = "Sd_Cds-CtCb",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2648,
    label = "Sd_Cds-CtCO",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2649,
    label = "Sd_Cds-CbCb",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2650,
    label = "Sd_Cds-CbCO",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2651,
    label = "Sd_Cds-COCO",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2652,
    label = "Sd_Cds-CdCt",
    group = 
"""
1 *2 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *1 S2d u0 p2 {1,D}
4    Ct  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2653,
    label = "Sd_Cds-CdCb",
    group = 
"""
1 *2 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *1 S2d u0 p2 {1,D}
4    Cb  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2654,
    label = "Sd_Cds-CdCO",
    group = 
"""
1 *2 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *1 S2d u0 p2 {1,D}
4    CO  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2655,
    label = "Sd_Cds-CtC=S",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Ct  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2656,
    label = "Sd_Cds-CbC=S",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    Cb  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2657,
    label = "Sd_Cds-COC=S",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CO  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2658,
    label = "Sd_Cds-CdCd",
    group = 
"""
1 *2 CS  u0 {2,S} {3,S} {4,D}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4 *1 S2d u0 p2 {1,D}
5    C   u0 {2,D}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2659,
    label = "Sd_Cds-CdC=S",
    group = 
"""
1 *2 CS  u0 {2,S} {3,D} {4,S}
2    Cd  u0 {1,S} {5,D}
3 *1 S2d u0 p2 {1,D}
4    CS  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2660,
    label = "Sd_Cds-C=SC=S",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S} {4,S}
2 *1 S2d u0 p2 {1,D}
3    CS  u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2661,
    label = "HJ",
    group = 
"""
1 *3 H u1
""",
    kinetics = None,
)

entry(
    index = 2662,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet}",
    kinetics = None,
)

entry(
    index = 2663,
    label = "C_quintet",
    group = 
"""
1 *3 C u4 p0
""",
    kinetics = None,
)

entry(
    index = 2664,
    label = "C_triplet",
    group = 
"""
1 *3 C u2 p1
""",
    kinetics = None,
)

entry(
    index = 2665,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, C/H_or_Val7/quartet, C/H_or_Val7/doublet}",
    kinetics = None,
)

entry(
    index = 2666,
    label = "N_atom_quartet",
    group = 
"""
1 *3 N u3 p1
""",
    kinetics = None,
)

entry(
    index = 2667,
    label = "N_atom_doublet",
    group = 
"""
1 *3 N u1 p2
""",
    kinetics = None,
)

entry(
    index = 2668,
    label = "C/H_or_Val7/quartet",
    group = 
"""
1 *3 Cs       u3 p0 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2669,
    label = "CH_quartet",
    group = 
"""
1 *3 Cs u3 p0 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2670,
    label = "CH_quartet-F",
    group = 
"""
1 *3 Cs  u3 p0 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2671,
    label = "CH_quartet-Cl",
    group = 
"""
1 *3 Cs   u3 p0 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2672,
    label = "CH_quartet-Br",
    group = 
"""
1 *3 Cs   u3 p0 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2673,
    label = "C/H_or_Val7/doublet",
    group = 
"""
1 *3 C        u1 p1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2674,
    label = "CH_doublet",
    group = 
"""
1 *3 C u1 p1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2675,
    label = "CH_doublet-F",
    group = 
"""
1 *3 C   u1 p1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2676,
    label = "CH_doublet-Cl",
    group = 
"""
1 *3 C    u1 p1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2677,
    label = "CH_doublet-Br",
    group = 
"""
1 *3 C    u1 p1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2678,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 R!H u2
""",
    kinetics = None,
)

entry(
    index = 2679,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O u2
""",
    kinetics = None,
)

entry(
    index = 2680,
    label = "SJJ",
    group = 
"""
1 *3 S u2
""",
    kinetics = None,
)

entry(
    index = 2681,
    label = "C/H_or_Val7/2_triplet",
    group = 
"""
1 *3 C        u2 {2,S} {3,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2682,
    label = "CH2_triplet",
    group = 
"""
1 *3 C u2 {2,S} {3,S}
2    H u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2683,
    label = "CH2_triplet-HF",
    group = 
"""
1 *3 C   u2 {2,S} {3,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2684,
    label = "CH2_triplet-HCl",
    group = 
"""
1 *3 C    u2 {2,S} {3,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2685,
    label = "CH2_triplet-HBr",
    group = 
"""
1 *3 C    u2 {2,S} {3,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2686,
    label = "CH2_triplet-FF",
    group = 
"""
1 *3 C   u2 {2,S} {3,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2687,
    label = "CH2_triplet-FCl",
    group = 
"""
1 *3 C    u2 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2688,
    label = "CH2_triplet-FBr",
    group = 
"""
1 *3 C    u2 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2689,
    label = "CH2_triplet-ClCl",
    group = 
"""
1 *3 C    u2 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2690,
    label = "CH2_triplet-ClBr",
    group = 
"""
1 *3 C    u2 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2691,
    label = "CH2_triplet-BrBr",
    group = 
"""
1 *3 C    u2 {2,S} {3,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2692,
    label = "CO_birad",
    group = 
"""
1 *3 C   u2 {2,D}
2    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2693,
    label = "N/H_or_Val7/triplet",
    group = 
"""
1 *3 N3s      u2 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2694,
    label = "NH_triplet",
    group = 
"""
1 *3 N3s u2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2695,
    label = "NH_triplet-F",
    group = 
"""
1 *3 N3s u2 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2696,
    label = "NH_triplet-Cl",
    group = 
"""
1 *3 N3s  u2 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2697,
    label = "NH_triplet-Br",
    group = 
"""
1 *3 N3s  u2 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2698,
    label = "CJ",
    group = 
"""
1 *3 C u1 p0
""",
    kinetics = None,
)

entry(
    index = 2699,
    label = "CbJ",
    group = 
"""
1 *3 Cb u1 p0
""",
    kinetics = None,
)

entry(
    index = 2700,
    label = "CtJ",
    group = 
"""
1 *3 Ct  u1 p0 {2,T}
2    R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2701,
    label = "CtJ_Ct",
    group = 
"""
1 *3 Ct u1 p0 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2702,
    label = "CtJ_N3t",
    group = 
"""
1 *3 Ct  u1 p0 {2,T}
2    N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2703,
    label = "C2b",
    group = 
"""
1 *3 C u1 p0 {2,T}
2    C u1 {1,T}
""",
    kinetics = None,
)

entry(
    index = 2704,
    label = "C=SJ",
    group = 
"""
1 *3 CS u1 p0 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2705,
    label = "C=SJ-/H_or_Val7/",
    group = 
"""
1 *3 CS       u1 p0 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2706,
    label = "C=SJ-H",
    group = 
"""
1 *3 CS u1 p0 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2707,
    label = "C=SJ-H-F",
    group = 
"""
1 *3 CS  u1 p0 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2708,
    label = "C=SJ-H-Cl",
    group = 
"""
1 *3 CS   u1 p0 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2709,
    label = "C=SJ-H-Br",
    group = 
"""
1 *3 CS   u1 p0 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2710,
    label = "C=SJ-Cs",
    group = 
"""
1 *3 CS u1 p0 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2711,
    label = "C=SJ-Ct",
    group = 
"""
1 *3 CS u1 p0 {2,S}
2    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2712,
    label = "C=SJ-Cb",
    group = 
"""
1 *3 CS u1 p0 {2,S}
2    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2713,
    label = "C=SJ-CO",
    group = 
"""
1 *3 CS u1 p0 {2,S}
2    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2714,
    label = "C=SJ-O2s",
    group = 
"""
1 *3 CS  u1 p0 {2,S}
2    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2715,
    label = "C=SJ-S2s",
    group = 
"""
1 *3 CS  u1 p0 {2,S}
2    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2716,
    label = "C=SJ-Cd",
    group = 
"""
1    Cd u0 {2,S} {3,D}
2 *3 CS u1 p0 {1,S}
3    C  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2717,
    label = "C=SJ-C=S",
    group = 
"""
1 *3 CS u1 p0 {2,S}
2    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2718,
    label = "CO_rad",
    group = 
"""
1 *3 C u1 p0 {2,D} {3,S}
2    O u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2719,
    label = "CO_pri_rad-H_or_Val7-1",
    group = 
"""
1 *3 C        u1 p0 {2,D} {3,S}
2    O        u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2720,
    label = "CO_pri_rad",
    group = 
"""
1 *3 C u1 p0 {2,D} {3,S}
2    O u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2721,
    label = "CO_pri_rad-F",
    group = 
"""
1 *3 C   u1 p0 {2,D} {3,S}
2    O   u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2722,
    label = "CO_pri_rad-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,D} {3,S}
2    O    u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2723,
    label = "CO_pri_rad-Br",
    group = 
"""
1 *3 C    u1 p0 {2,D} {3,S}
2    O    u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2724,
    label = "CO_sec_rad",
    group = 
"""
1 *3 C   u1 p0 {2,D} {3,S}
2    O   u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2725,
    label = "CO_rad/NonDe",
    group = 
"""
1 *3 C                     u1 p0 {2,D} {3,S}
2    O                     u0 {1,D}
3    [Cs,S2s,N3s,N5sc,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2726,
    label = "CO_rad/OneDe",
    group = 
"""
1 *3 C                         u1 p0 {2,D} {3,S}
2    O                         u0 {1,D}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2727,
    label = "CsJ",
    group = 
"""
1 *3 C u1 p0 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2728,
    label = "CsJ-/H_or_Val7/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *3 C        u1 p0 {2,S} {3,S} {4,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2729,
    label = "CsJ-HHH",
    group = 
"""
1 *3 C u1 p0 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2730,
    label = "CsJ-Cs/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *3 C        u1 p0 {2,S} {3,S} {4,S}
2    Cs       u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2731,
    label = "CsJ-CsHH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2732,
    label = "CsJ-CsHH-HF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cs  u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2733,
    label = "CsJ-CsHH-HCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cs   u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2734,
    label = "CsJ-CsHH-HBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cs   u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2735,
    label = "CsJ-CsHH-FF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cs  u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2736,
    label = "CsJ-CsHH-FCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cs   u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2737,
    label = "CsJ-CsHH-FBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cs   u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2738,
    label = "CsJ-CsHH-ClCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cs   u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2739,
    label = "CsJ-CsHH-ClBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cs   u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2740,
    label = "CsJ-CsHH-BrBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cs   u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2741,
    label = "CsJ-CsCs/H_or_Val7/",
    group = 
"""
1 *3 C        u1 p0 {2,S} {3,S} {4,S}
2    Cs       u0 {1,S}
3    Cs       u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2742,
    label = "CsJ-CsCsH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2743,
    label = "CsJ-CsCsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cs  u0 {1,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2744,
    label = "CsJ-CsCsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cs   u0 {1,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2745,
    label = "CsJ-CsCsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cs   u0 {1,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2746,
    label = "CsJ-CsCsCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2747,
    label = "CsJ-Os/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *3 C        u1 p0 {2,S} {3,S} {4,S}
2    O2s      u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2748,
    label = "CsJ-OsHH",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2749,
    label = "CsJ-OsHH-HF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2750,
    label = "CsJ-OsHH-HCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2751,
    label = "CsJ-OsHH-HBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2752,
    label = "CsJ-OsHH-FF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2753,
    label = "CsJ-OsHH-FCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2754,
    label = "CsJ-OsHH-FBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2755,
    label = "CsJ-OsHH-ClCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2756,
    label = "CsJ-OsHH-ClBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2757,
    label = "CsJ-OsHH-BrBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2758,
    label = "CsJ-OsCs/H_or_Val7/",
    group = 
"""
1 *3 C        u1 p0 {2,S} {3,S} {4,S}
2    O2s      u0 {1,S}
3    Cs       u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2759,
    label = "CsJ-OsCsH",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2760,
    label = "CsJ-OsCsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2761,
    label = "CsJ-OsCsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2762,
    label = "CsJ-OsCsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2763,
    label = "CsJ-OsCsCs",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2764,
    label = "CsJ-OsOs/H_or_Val7/",
    group = 
"""
1 *3 C        u1 p0 {2,S} {3,S} {4,S}
2    O2s      u0 {1,S}
3    O2s      u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2765,
    label = "CsJ-OsOsH",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2766,
    label = "CsJ-OsOsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2767,
    label = "CsJ-OsOsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    O2s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2768,
    label = "CsJ-OsOsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    O2s  u0 {1,S}
3    O2s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2769,
    label = "CsJ-OsOsCs",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2770,
    label = "CsJ-OsOsOs",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    O2s u0 {1,S}
3    O2s u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2771,
    label = "CsJ-Ss/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *3 C        u1 p0 {2,S} {3,S} {4,S}
2    S2s      u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2772,
    label = "CsJ-SsHH",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2773,
    label = "CsJ-SsHH-HF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2774,
    label = "CsJ-SsHH-HCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2775,
    label = "CsJ-SsHH-HBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2776,
    label = "CsJ-SsHH-FF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2777,
    label = "CsJ-SsHH-FCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2778,
    label = "CsJ-SsHH-FBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2779,
    label = "CsJ-SsHH-ClCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2780,
    label = "CsJ-SsHH-ClBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2781,
    label = "CsJ-SsHH-BrBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2782,
    label = "CsJ-SsCs/H_or_Val7/",
    group = 
"""
1 *3 C        u1 p0 {2,S} {3,S} {4,S}
2    S2s      u0 {1,S}
3    Cs       u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2783,
    label = "CsJ-SsCsH",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2784,
    label = "CsJ-SsCsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2785,
    label = "CsJ-SsCsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2786,
    label = "CsJ-SsCsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2787,
    label = "CsJ-SsCsCs",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2788,
    label = "CsJ-SsSs/H_or_Val7/",
    group = 
"""
1 *3 C        u1 p0 {2,S} {3,S} {4,S}
2    S2s      u0 {1,S}
3    S2s      u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2789,
    label = "CsJ-SsSsH",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2790,
    label = "CsJ-SsSsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2791,
    label = "CsJ-SsSsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    S2s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2792,
    label = "CsJ-SsSsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    S2s  u0 {1,S}
3    S2s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2793,
    label = "CsJ-SsSsCs",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2794,
    label = "CsJ-SsSsSs",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2795,
    label = "CsJ-Ns/H_or_Val7/H_or_Val7/",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    [H,Val7]   u0 {1,S}
3    [H,Val7]   u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2796,
    label = "CsJ-NsHH",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    H          u0 {1,S}
3    H          u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2797,
    label = "CsJ-NsHH-HF",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    H          u0 {1,S}
3    F1s        u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2798,
    label = "CsJ-NsHH-HCl",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    H          u0 {1,S}
3    Cl1s       u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2799,
    label = "CsJ-NsHH-HBr",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    H          u0 {1,S}
3    Br1s       u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2800,
    label = "CsJ-NsHH-FF",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    F1s        u0 {1,S}
3    F1s        u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2801,
    label = "CsJ-NsHH-FCl",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    F1s        u0 {1,S}
3    Cl1s       u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2802,
    label = "CsJ-NsHH-FBr",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    F1s        u0 {1,S}
3    Br1s       u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2803,
    label = "CsJ-NsHH-ClCl",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    Cl1s       u0 {1,S}
3    Cl1s       u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2804,
    label = "CsJ-NsHH-ClBr",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    Cl1s       u0 {1,S}
3    Br1s       u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2805,
    label = "CsJ-NsHH-BrBr",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    Br1s       u0 {1,S}
3    Br1s       u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2806,
    label = "CsJ-NsCs/H_or_Val7/",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    [H,Val7]   u0 {1,S}
3    [N3s,N5sc] u0 {1,S}
4    Cs         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2807,
    label = "CsJ-NsCsH",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    H          u0 {1,S}
3    [N3s,N5sc] u0 {1,S}
4    Cs         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2808,
    label = "CsJ-NsCsH-F",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    F1s        u0 {1,S}
3    [N3s,N5sc] u0 {1,S}
4    Cs         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2809,
    label = "CsJ-NsCsH-Cl",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    Cl1s       u0 {1,S}
3    [N3s,N5sc] u0 {1,S}
4    Cs         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2810,
    label = "CsJ-NsCsH-Br",
    group = 
"""
1 *3 C          u1 p0 {2,S} {3,S} {4,S}
2    Br1s       u0 {1,S}
3    [N3s,N5sc] u0 {1,S}
4    Cs         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2811,
    label = "CsJ-OneDe",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [H,Cs,O2s,S2s,N3s,N5sc]   u0 {1,S}
4    [H,Cs,O2s,S2s,N3s,N5sc]   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2812,
    label = "CsJ-OneDeCsCs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2813,
    label = "CsJ-CtCsCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2814,
    label = "CsJ-CbCsCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2815,
    label = "CsJ-COCsCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2816,
    label = "CsJ-CdCsCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2817,
    label = "CsJ-C=SCsCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2818,
    label = "CsJ-OneDeOsCs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    O2s                       u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2819,
    label = "CsJ-OneDeSsCs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    S2s                       u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2820,
    label = "CsJ-OneDeOsOs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    O2s                       u0 {1,S}
4    O2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2821,
    label = "CsJ-OneDeOsSs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    O2s                       u0 {1,S}
4    S2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2822,
    label = "CsJ-OneDeSsSs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    S2s                       u0 {1,S}
4    S2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2823,
    label = "CsJ-OneDeNsCs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
4    [N3s,N5sc]                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2824,
    label = "CsJ-OneDeHH",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    H                         u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2825,
    label = "CsJ-CtHH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2826,
    label = "CsJ-CbHH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2827,
    label = "CsJ-COHH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2828,
    label = "CsJ-CdHH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2829,
    label = "CsJ-(CdC)HH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2830,
    label = "CsJ-C=SHH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2831,
    label = "CsJ-OneDeCsH",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2832,
    label = "CsJ-CtCsH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2833,
    label = "CsJ-CbCsH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2834,
    label = "CsJ-COCsH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2835,
    label = "CsJ-CdCsH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2836,
    label = "CsJ-C=SCsH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2837,
    label = "CsJ-OneDeOsH",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    O2s                       u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2838,
    label = "CsJ-OneDeSsH",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    S2s                       u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2839,
    label = "CsJ-OneDeNsH",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    H                         u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [N3s,N5sc]                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2840,
    label = "CsJ-TwoDe",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [H,Cs,O2s,S2s]            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2841,
    label = "CsJ-TwoDeCs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2842,
    label = "CsJ-CtCtCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2843,
    label = "CsJ-CtCbCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2844,
    label = "CsJ-CtCOCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2845,
    label = "CsJ-CbCbCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2846,
    label = "CsJ-CbCOCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2847,
    label = "CsJ-COCOCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2848,
    label = "CsJ-CdCtCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2849,
    label = "CsJ-CdCbCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2850,
    label = "CsJ-CdCOCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2851,
    label = "CsJ-CtC=SCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2852,
    label = "CsJ-CbC=SCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2853,
    label = "CsJ-COC=SCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2854,
    label = "CsJ-CdCdCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2855,
    label = "CsJ-CdC=SCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2856,
    label = "CsJ-C=SC=SCs",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2857,
    label = "CsJ-TwoDeOs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    O2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2858,
    label = "CsJ-TwoDeSs",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    S2s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2859,
    label = "CsJ-TwoDeH",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2860,
    label = "CsJ-CtCtH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2861,
    label = "CsJ-CtCbH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2862,
    label = "CsJ-CtCOH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2863,
    label = "CsJ-CbCbH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2864,
    label = "CsJ-CbCOH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2865,
    label = "CsJ-COCOH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2866,
    label = "CsJ-CdCtH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2867,
    label = "CsJ-CdCbH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2868,
    label = "CsJ-CdCOH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2869,
    label = "CsJ-CtC=SH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2870,
    label = "CsJ-CbC=SH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2871,
    label = "CsJ-COC=SH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2872,
    label = "CsJ-CdCdH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2873,
    label = "CsJ-CdC=SH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2874,
    label = "CsJ-C=SC=SH",
    group = 
"""
1 *3 C  u1 p0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2875,
    label = "CsJ-ThreeDe",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2876,
    label = "CsJ-OneDeHH-HF",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    H                         u0 {1,S}
4    F1s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2877,
    label = "CsJ-CtHH-HF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Ct  u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2878,
    label = "CsJ-CbHH-HF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cb  u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2879,
    label = "CsJ-COHH-HF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    CO  u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2880,
    label = "CsJ-CdHH-HF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S} {5,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2881,
    label = "CsJ-(CdC)HH-HF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S} {5,D} {6,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2882,
    label = "CsJ-C=SHH-HF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    CS  u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2883,
    label = "CsJ-OneDeHH-HCl",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    H                         u0 {1,S}
4    Cl1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2884,
    label = "CsJ-CtHH-HCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Ct   u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2885,
    label = "CsJ-CbHH-HCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cb   u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2886,
    label = "CsJ-COHH-HCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CO   u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2887,
    label = "CsJ-CdHH-HCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2888,
    label = "CsJ-(CdC)HH-HCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D} {6,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2889,
    label = "CsJ-C=SHH-HCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CS   u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2890,
    label = "CsJ-OneDeHH-HBr",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    H                         u0 {1,S}
4    Br1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2891,
    label = "CsJ-CtHH-HBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Ct   u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2892,
    label = "CsJ-CbHH-HBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cb   u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2893,
    label = "CsJ-COHH-HBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CO   u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2894,
    label = "CsJ-CdHH-HBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2895,
    label = "CsJ-(CdC)HH-HBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D} {6,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2896,
    label = "CsJ-C=SHH-HBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CS   u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2897,
    label = "CsJ-OneDeHH-FF",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    F1s                       u0 {1,S}
4    F1s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2898,
    label = "CsJ-CtHH-FF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Ct  u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2899,
    label = "CsJ-CbHH-FF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cb  u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2900,
    label = "CsJ-COHH-FF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    CO  u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2901,
    label = "CsJ-CdHH-FF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S} {5,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2902,
    label = "CsJ-(CdC)HH-FF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S} {5,D} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
6    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2903,
    label = "CsJ-C=SHH-FF",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    CS  u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2904,
    label = "CsJ-OneDeHH-FCl",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    F1s                       u0 {1,S}
4    Cl1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2905,
    label = "CsJ-CtHH-FCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Ct   u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2906,
    label = "CsJ-CbHH-FCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cb   u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2907,
    label = "CsJ-COHH-FCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CO   u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2908,
    label = "CsJ-CdHH-FCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2909,
    label = "CsJ-(CdC)HH-FCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D} {6,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2910,
    label = "CsJ-C=SHH-FCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CS   u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2911,
    label = "CsJ-OneDeHH-FBr",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    F1s                       u0 {1,S}
4    Br1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2912,
    label = "CsJ-CtHH-FBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Ct   u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2913,
    label = "CsJ-CbHH-FBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cb   u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2914,
    label = "CsJ-COHH-FBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CO   u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2915,
    label = "CsJ-CdHH-FBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2916,
    label = "CsJ-(CdC)HH-FBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D} {6,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2917,
    label = "CsJ-C=SHH-FBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CS   u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2918,
    label = "CsJ-OneDeHH-ClCl",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cl1s                      u0 {1,S}
4    Cl1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2919,
    label = "CsJ-CtHH-ClCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Ct   u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2920,
    label = "CsJ-CbHH-ClCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cb   u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2921,
    label = "CsJ-COHH-ClCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CO   u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2922,
    label = "CsJ-CdHH-ClCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2923,
    label = "CsJ-(CdC)HH-ClCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2924,
    label = "CsJ-C=SHH-ClCl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CS   u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2925,
    label = "CsJ-OneDeHH-ClBr",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cl1s                      u0 {1,S}
4    Br1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2926,
    label = "CsJ-CtHH-ClBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Ct   u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2927,
    label = "CsJ-CbHH-ClBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cb   u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2928,
    label = "CsJ-COHH-ClBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CO   u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2929,
    label = "CsJ-CdHH-ClBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2930,
    label = "CsJ-(CdC)HH-ClBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D} {6,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2931,
    label = "CsJ-C=SHH-ClBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CS   u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2932,
    label = "CsJ-OneDeHH-BrBr",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Br1s                      u0 {1,S}
4    Br1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2933,
    label = "CsJ-CtHH-BrBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Ct   u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2934,
    label = "CsJ-CbHH-BrBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cb   u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2935,
    label = "CsJ-COHH-BrBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CO   u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2936,
    label = "CsJ-CdHH-BrBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2937,
    label = "CsJ-(CdC)HH-BrBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
6    C    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2938,
    label = "CsJ-C=SHH-BrBr",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CS   u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2939,
    label = "CsJ-OneDeCsH-F",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
4    F1s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2940,
    label = "CsJ-CtCsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Ct  u0 {1,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2941,
    label = "CsJ-CbCsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cb  u0 {1,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2942,
    label = "CsJ-COCsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    CO  u0 {1,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2943,
    label = "CsJ-CdCsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S} {5,D}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2944,
    label = "CsJ-C=SCsH-F",
    group = 
"""
1 *3 C   u1 p0 {2,S} {3,S} {4,S}
2    CS  u0 {1,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2945,
    label = "CsJ-OneDeCsH-Cl",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
4    Cl1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2946,
    label = "CsJ-CtCsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Ct   u0 {1,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2947,
    label = "CsJ-CbCsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cb   u0 {1,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2948,
    label = "CsJ-COCsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CO   u0 {1,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2949,
    label = "CsJ-CdCsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2950,
    label = "CsJ-C=SCsH-Cl",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CS   u0 {1,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2951,
    label = "CsJ-OneDeCsH-Br",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
4    Br1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2952,
    label = "CsJ-CtCsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Ct   u0 {1,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2953,
    label = "CsJ-CbCsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cb   u0 {1,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2954,
    label = "CsJ-COCsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CO   u0 {1,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2955,
    label = "CsJ-CdCsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2956,
    label = "CsJ-C=SCsH-Br",
    group = 
"""
1 *3 C    u1 p0 {2,S} {3,S} {4,S}
2    CS   u0 {1,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2957,
    label = "CsJ-TwoDeH-F",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    F1s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2958,
    label = "CsJ-TwoDeH-Cl",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Cl1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2959,
    label = "CsJ-TwoDeH-Br",
    group = 
"""
1 *3 C                         u1 p0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
4    Br1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2960,
    label = "CdsJ=Cdd",
    group = 
"""
1 *3 C   u1 p0 {2,D} {3,S}
2    C   u0 {1,D} {4,D}
3    R   u0 {1,S}
4    R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2961,
    label = "CdsJ",
    group = 
"""
1    C u0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 {1,D} {5,S}
3    R u0 {1,S}
4    R u0 {1,S}
5    R u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2962,
    label = "CdsJ-/H_or_Val7/",
    group = 
"""
1    C        u0 {2,D} {3,S} {4,S}
2 *3 C        u1 p0 {1,D} {5,S}
3    R        u0 {1,S}
4    R        u0 {1,S}
5    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2963,
    label = "CdsJ-H",
    group = 
"""
1    C u0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 {1,D} {5,S}
3    R u0 {1,S}
4    R u0 {1,S}
5    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2964,
    label = "CdsJ-(CdCb)H",
    group = 
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 p0 {1,D} {5,S}
3    Cb u0 {1,S}
4    R  u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2965,
    label = "CdsJ-H-F",
    group = 
"""
1    C   u0 {2,D} {3,S} {4,S}
2 *3 C   u1 p0 {1,D} {5,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2966,
    label = "CdsJ-(CdCb)H-F",
    group = 
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2 *3 Cd  u1 p0 {1,D} {5,S}
3    Cb  u0 {1,S}
4    R   u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2967,
    label = "CdsJ-H-Cl",
    group = 
"""
1    C    u0 {2,D} {3,S} {4,S}
2 *3 C    u1 p0 {1,D} {5,S}
3    R    u0 {1,S}
4    R    u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2968,
    label = "CdsJ-(CdCb)H-Cl",
    group = 
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 Cd   u1 p0 {1,D} {5,S}
3    Cb   u0 {1,S}
4    R    u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2969,
    label = "CdsJ-H-Br",
    group = 
"""
1    C    u0 {2,D} {3,S} {4,S}
2 *3 C    u1 p0 {1,D} {5,S}
3    R    u0 {1,S}
4    R    u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2970,
    label = "CdsJ-(CdCb)H-Br",
    group = 
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 Cd   u1 p0 {1,D} {5,S}
3    Cb   u0 {1,S}
4    R    u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2971,
    label = "CdsJ-Cs",
    group = 
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2972,
    label = "CdsJ-Ct",
    group = 
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2973,
    label = "CdsJ-Cb",
    group = 
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    Cb u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2974,
    label = "CdsJ-CO",
    group = 
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    CO u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2975,
    label = "CdsJ-O2s",
    group = 
"""
1    C   u0 {2,D} {3,S} {4,S}
2 *3 C   u1 p0 {1,D} {5,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
5    O2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2976,
    label = "CdsJ-S2s",
    group = 
"""
1    C   u0 {2,D} {3,S} {4,S}
2 *3 C   u1 p0 {1,D} {5,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
5    S2s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2977,
    label = "CdsJ-Cd",
    group = 
"""
1    C  u0 {2,D} {4,S} {5,S}
2 *3 C  u1 p0 {1,D} {3,S}
3    Cd u0 {2,S} {6,D}
4    R  u0 {1,S}
5    R  u0 {1,S}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2978,
    label = "CdsJ-C=S",
    group = 
"""
1    C  u0 {2,D} {3,S} {4,S}
2 *3 C  u1 p0 {1,D} {5,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    CS u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2979,
    label = "OJ",
    group = "OR{OJ_pri-H_or_Val7-1, OJ_sec, O2b}",
    kinetics = None,
)

entry(
    index = 2980,
    label = "OJ_pri-H_or_Val7-1",
    group = 
"""
1 *3 O        u1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2981,
    label = "OJ_pri",
    group = 
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2982,
    label = "OJ_pri-F",
    group = 
"""
1 *3 O   u1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2983,
    label = "OJ_pri-Cl",
    group = 
"""
1 *3 O    u1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2984,
    label = "OJ_pri-Br",
    group = 
"""
1 *3 O    u1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2985,
    label = "OJ_sec",
    group = 
"""
1 *3 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2986,
    label = "OJ-NonDe",
    group = 
"""
1 *3 O                     u1 {2,S}
2    [Cs,O2s,S2s,N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2987,
    label = "O_rad/NonDe",
    group = 
"""
1 *3 O            u1 {2,S}
2    [Cs,O2s,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2988,
    label = "OJ-Cs",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2989,
    label = "OJ-O2s",
    group = 
"""
1 *3 O   u1 {2,S}
2    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2990,
    label = "OJ-Ns",
    group = 
"""
1 *3 O          u1 {2,S}
2    [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2991,
    label = "OJ-OneDe",
    group = 
"""
1 *3 O                         u1 {2,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2992,
    label = "O_rad/OneDe",
    group = 
"""
1 *3 O                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2993,
    label = "OJ-OneDeN",
    group = 
"""
1 *3 O          u1 {2,S}
2    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2994,
    label = "OJ-NO",
    group = 
"""
1    [N3d,N5dc] u0 {2,S} {3,D}
2 *3 O          u1 {1,S}
3    O2d        u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2995,
    label = "O2b",
    group = 
"""
1 *3 O u1 {2,S}
2    O u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2996,
    label = "SJ",
    group = 
"""
1 *3 S u1
""",
    kinetics = None,
)

entry(
    index = 2997,
    label = "SsJ",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2998,
    label = "SsJ-/H_or_Val7/",
    group = 
"""
1 *3 S2s      u1 p2 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2999,
    label = "SsJ-H",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3000,
    label = "SsJ-H-F",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3001,
    label = "SsJ-H-Cl",
    group = 
"""
1 *3 S2s  u1 p2 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3002,
    label = "SsJ-H-Br",
    group = 
"""
1 *3 S2s  u1 p2 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3003,
    label = "SsJ-Cs",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3004,
    label = "SsJ-S2s",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    S2s u0 p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3005,
    label = "SsJ-OneDe",
    group = 
"""
1 *3 S2s                       u1 p2 {2,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3006,
    label = "SsJ-Ct",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3007,
    label = "SsJ-Cb",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3008,
    label = "SsJ-CO",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3009,
    label = "SsJ-Cd",
    group = 
"""
1    Cd  u0 {2,S} {3,D}
2 *3 S2s u1 p2 {1,S}
3    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 3010,
    label = "SsJ-C=S",
    group = 
"""
1 *3 S2s u1 p2 {2,S}
2    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3011,
    label = "NJ",
    group = 
"""
1 *3 N u1
""",
    kinetics = None,
)

entry(
    index = 3012,
    label = "N3J",
    group = 
"""
1 *3 [N3s,N3d] u1
""",
    kinetics = None,
)

entry(
    index = 3013,
    label = "N3sJ",
    group = 
"""
1 *3 N3s u1
""",
    kinetics = None,
)

entry(
    index = 3014,
    label = "N/H_or_Val7/2J",
    group = 
"""
1 *3 N3s      u1 {2,S} {3,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3015,
    label = "NH2J",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3016,
    label = "NH2J-HF",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3017,
    label = "NH2J-HCl",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3018,
    label = "NH2J-HBr",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3019,
    label = "NH2J-FF",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3020,
    label = "NH2J-FCl",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3021,
    label = "NH2J-FBr",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3022,
    label = "NH2J-ClCl",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3023,
    label = "NH2J-ClBr",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3024,
    label = "NH2J-BrBr",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3025,
    label = "N3sJ-NonDe/H_or_Val7/",
    group = 
"""
1 *3 N3s                   u1 {2,S} {3,S}
2    [O2s,S2s,N3s,N5sc,Cs] u0 {1,S}
3    [H,Val7]              u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3026,
    label = "N3sJ-NonDeH",
    group = 
"""
1 *3 N3s                   u1 {2,S} {3,S}
2    [O2s,S2s,N3s,N5sc,Cs] u0 {1,S}
3    H                     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3027,
    label = "N3sJ-CsH",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    Cs  u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3028,
    label = "N3sJ-OsH",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    O2s u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3029,
    label = "N3sJ-NsH",
    group = 
"""
1 *3 N3s        u1 {2,S} {3,S}
2    [N3s,N5sc] u0 {1,S}
3    H          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3030,
    label = "N3sJ-NonDeH-F",
    group = 
"""
1 *3 N3s                   u1 {2,S} {3,S}
2    [O2s,S2s,N3s,N5sc,Cs] u0 {1,S}
3    F1s                   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3031,
    label = "N3sJ-CsH-F",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    Cs  u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3032,
    label = "N3sJ-OsH-F",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    O2s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3033,
    label = "N3sJ-NsH-F",
    group = 
"""
1 *3 N3s        u1 {2,S} {3,S}
2    [N3s,N5sc] u0 {1,S}
3    F1s        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3034,
    label = "N3sJ-NonDeH-Cl",
    group = 
"""
1 *3 N3s                   u1 {2,S} {3,S}
2    [O2s,S2s,N3s,N5sc,Cs] u0 {1,S}
3    Cl1s                  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3035,
    label = "N3sJ-CsH-Cl",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Cs   u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3036,
    label = "N3sJ-OsH-Cl",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    O2s  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3037,
    label = "N3sJ-NsH-Cl",
    group = 
"""
1 *3 N3s        u1 {2,S} {3,S}
2    [N3s,N5sc] u0 {1,S}
3    Cl1s       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3038,
    label = "N3sJ-NonDeH-Br",
    group = 
"""
1 *3 N3s                   u1 {2,S} {3,S}
2    [O2s,S2s,N3s,N5sc,Cs] u0 {1,S}
3    Br1s                  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3039,
    label = "N3sJ-CsH-Br",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Cs   u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3040,
    label = "N3sJ-OsH-Br",
    group = 
"""
1 *3 N3s  u1 {2,S} {3,S}
2    O2s  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3041,
    label = "N3sJ-NsH-Br",
    group = 
"""
1 *3 N3s        u1 {2,S} {3,S}
2    [N3s,N5sc] u0 {1,S}
3    Br1s       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3042,
    label = "N3sJ-NonDe2",
    group = 
"""
1 *3 N3s                   u1 {2,S} {3,S}
2    [O2s,Cs,N3s,N5sc,S2s] u0 {1,S}
3    [O2s,Cs,N3s,N5sc,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3043,
    label = "N3sJ-OneDe/H_or_Val7/",
    group = 
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [H,Val7]                  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3044,
    label = "N3sJ-OneDeH",
    group = 
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    H                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3045,
    label = "N3sJ-OneDeH-F",
    group = 
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    F1s                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3046,
    label = "N3sJ-OneDeH-Cl",
    group = 
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cl1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3047,
    label = "N3sJ-OneDeH-Br",
    group = 
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Br1s                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3048,
    label = "N3sJ-OneDeCs",
    group = 
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    Cs                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3049,
    label = "N3sJ-TwoDe",
    group = 
"""
1 *3 N3s                       u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3050,
    label = "N3dJ",
    group = 
"""
1 *3 N3d u1
""",
    kinetics = None,
)

entry(
    index = 3051,
    label = "N3dJ_C",
    group = 
"""
1 *3 N3d u1 {2,D}
2    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 3052,
    label = "N3dJ_O",
    group = 
"""
1 *3 N3d u1 {2,D}
2    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 3053,
    label = "N3dJ_N",
    group = 
"""
1 *3 N3d u1 {2,D}
2    N   u0 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: R_R
    L2: Cb_Cb
        L3: Cb-R!H_Cb
            L4: Cb-R!H_Cb-R!H
                L5: Cb-indane_Cb-indane
                    L6: Cb-indeneDe_Cb-indeneNde
                    L6: Cb-indeneNde_Cb-indene_De
                L5: Cb-benzofuranNde_Cb-benzofuranDe
                L5: Cb-tetralin_Cb-tetralin
                    L6: Cb-naphthalene_Cb-naphthalene
                L5: Cb-R!H_Cbf-R!H
            L4: Cb-R!/H_or_Val7/Cb-/H_or_Val7/
                L5: Cb-R!H_Cb-H
                    L6: Cb-C-cyclic_Cb-H
                        L7: Cbf-Cb-cyclic_Cb-H
                    L6: Cb-Cd_Cb-H
                    L6: Cb-Cs_Cb-H
                L5: Cb-R!H_Cb-H-F
                    L6: Cb-C-cyclic_Cb-H-F
                        L7: Cbf-Cb-cyclic_Cb-H-F
                    L6: Cb-Cd_Cb-H-F
                    L6: Cb-Cs_Cb-H-F
                L5: Cb-R!H_Cb-H-Cl
                    L6: Cb-C-cyclic_Cb-H-Cl
                        L7: Cbf-Cb-cyclic_Cb-H-Cl
                    L6: Cb-Cd_Cb-H-Cl
                    L6: Cb-Cs_Cb-H-Cl
                L5: Cb-R!H_Cb-H-Br
                    L6: Cb-C-cyclic_Cb-H-Br
                        L7: Cbf-Cb-cyclic_Cb-H-Br
                    L6: Cb-Cd_Cb-H-Br
                    L6: Cb-Cs_Cb-H-Br
        L3: Cb-/H_or_Val7/Cb
            L4: Cb-H_Cb
                L5: Cb-H_Cb-R!H
                    L6: Cb-H_Cb-indeneNde
                    L6: Cb-H_Cbf-Cb
                    L6: Cb-H-Ortho_Cb-C
                        L7: Cb-H-Ortho_Cb-C-fused
                L5: Cb-H_Cb-H
                    L6: Cb-H-Meta_Cb-H
                    L6: Cb-H-Para_Cb-H
                        L7: Cb-H-Para_Cb-H-fused
                    L6: Cb-H_Cb-H_o_ketene
                    L6: Cb-H_Cb-CbfH
                L5: Cb-H_Cb-H-HF
                    L6: Cb-H_Cb-H_o_ketene-HF
                    L6: Cb-H_Cb-CbfH-HF
                L5: Cb-H_Cb-H-HCl
                    L6: Cb-H_Cb-H_o_ketene-HCl
                    L6: Cb-H_Cb-CbfH-HCl
                L5: Cb-H_Cb-H-HBr
                    L6: Cb-H_Cb-H_o_ketene-HBr
                    L6: Cb-H_Cb-CbfH-HBr
            L4: Cb-H_Cb-F
                L5: Cb-H_Cb-R!H-F
                    L6: Cb-H_Cb-indeneNde-F
                    L6: Cb-H_Cbf-Cb-F
                    L6: Cb-H-Ortho_Cb-C-F
                        L7: Cb-H-Ortho_Cb-C-fused-F
                L5: Cb-H_Cb-H-FF
                    L6: Cb-H-Meta_Cb-H-FF
                    L6: Cb-H-Para_Cb-H-FF
                        L7: Cb-H-Para_Cb-H-fused-FF
                    L6: Cb-H_Cb-H_o_ketene-FF
                    L6: Cb-H_Cb-CbfH-FF
                L5: Cb-H_Cb-H-FCl
                    L6: Cb-H_Cb-H_o_ketene-FCl
                    L6: Cb-H_Cb-CbfH-FCl
                L5: Cb-H_Cb-H-FBr
                    L6: Cb-H_Cb-H_o_ketene-FBr
                    L6: Cb-H_Cb-CbfH-FBr
                L5: Cb-H-Meta_Cb-H-HF
                L5: Cb-H-Para_Cb-H-HF
                    L6: Cb-H-Para_Cb-H-fused-HF
            L4: Cb-H_Cb-Cl
                L5: Cb-H_Cb-R!H-Cl
                    L6: Cb-H_Cb-indeneNde-Cl
                    L6: Cb-H_Cbf-Cb-Cl
                    L6: Cb-H-Ortho_Cb-C-Cl
                        L7: Cb-H-Ortho_Cb-C-fused-Cl
                L5: Cb-H_Cb-H-ClCl
                    L6: Cb-H-Meta_Cb-H-ClCl
                    L6: Cb-H-Para_Cb-H-ClCl
                        L7: Cb-H-Para_Cb-H-fused-ClCl
                    L6: Cb-H_Cb-H_o_ketene-ClCl
                    L6: Cb-H_Cb-CbfH-ClCl
                L5: Cb-H_Cb-H-ClBr
                    L6: Cb-H_Cb-H_o_ketene-ClBr
                    L6: Cb-H_Cb-CbfH-ClBr
                L5: Cb-H-Meta_Cb-H-HCl
                L5: Cb-H-Meta_Cb-H-FCl
                L5: Cb-H-Para_Cb-H-HCl
                    L6: Cb-H-Para_Cb-H-fused-HCl
                L5: Cb-H-Para_Cb-H-FCl
                    L6: Cb-H-Para_Cb-H-fused-FCl
            L4: Cb-H_Cb-Br
                L5: Cb-H_Cb-R!H-Br
                    L6: Cb-H_Cb-indeneNde-Br
                    L6: Cb-H_Cbf-Cb-Br
                    L6: Cb-H-Ortho_Cb-C-Br
                        L7: Cb-H-Ortho_Cb-C-fused-Br
                L5: Cb-H_Cb-H-BrBr
                    L6: Cb-H-Meta_Cb-H-BrBr
                    L6: Cb-H-Para_Cb-H-BrBr
                        L7: Cb-H-Para_Cb-H-fused-BrBr
                    L6: Cb-H_Cb-H_o_ketene-BrBr
                    L6: Cb-H_Cb-CbfH-BrBr
                L5: Cb-H-Meta_Cb-H-HBr
                L5: Cb-H-Meta_Cb-H-FBr
                L5: Cb-H-Meta_Cb-H-ClBr
                L5: Cb-H-Para_Cb-H-HBr
                    L6: Cb-H-Para_Cb-H-fused-HBr
                L5: Cb-H-Para_Cb-H-FBr
                    L6: Cb-H-Para_Cb-H-fused-FBr
                L5: Cb-H-Para_Cb-H-ClBr
                    L6: Cb-H-Para_Cb-H-fused-ClBr
    L2: Cd_R
        L3: Cdd_Od
            L4: CO2
            L4: Ck_O
            L4: C=S_O
            L4: Cdd_Od-N3d
        L3: CO_O
            L4: CO-/H_or_Val7/H_or_Val7/O
                L5: CO-HH_O
                L5: CO-HH_O-HF
                L5: CO-HH_O-HCl
                L5: CO-HH_O-HBr
                L5: CO-HH_O-FF
                L5: CO-HH_O-FCl
                L5: CO-HH_O-FBr
                L5: CO-HH_O-ClCl
                L5: CO-HH_O-ClBr
                L5: CO-HH_O-BrBr
            L4: CO-Nd/H_or_Val7/O
                L5: CO-NdH_O
                    L6: CO-CsH_O
                L5: CO-NdH_O-F
                    L6: CO-CsH_O-F
                L5: CO-NdH_O-Cl
                    L6: CO-CsH_O-Cl
                L5: CO-NdH_O-Br
                    L6: CO-CsH_O-Br
            L4: CO-De/H_or_Val7/O
                L5: CO-DeH_O
                    L6: CO-CdH_O
                    L6: CO-CtH_O
                L5: CO-DeH_O-F
                    L6: CO-CdH_O-F
                    L6: CO-CtH_O-F
                L5: CO-DeH_O-Cl
                    L6: CO-CdH_O-Cl
                    L6: CO-CtH_O-Cl
                L5: CO-DeH_O-Br
                    L6: CO-CdH_O-Br
                    L6: CO-CtH_O-Br
            L4: CO-NdNd_O
                L5: CO-CsCs_O
            L4: CO-DeNd_O
                L5: CO-CdCs_O
                L5: CO-CtCs_O
            L4: CO-DeDe_O
        L3: Cdd_Sd
            L4: Cdd-Sd_Sd
        L3: Cds_Cdd
            L4: Cds_Ca
                L5: Cds-/H_or_Val7/H_or_Val7/Ca
                    L6: Cds-HH_Ca
                    L6: Cds-HH_Ca-HF
                    L6: Cds-HH_Ca-HCl
                    L6: Cds-HH_Ca-HBr
                    L6: Cds-HH_Ca-FF
                    L6: Cds-HH_Ca-FCl
                    L6: Cds-HH_Ca-FBr
                    L6: Cds-HH_Ca-ClCl
                    L6: Cds-HH_Ca-ClBr
                    L6: Cds-HH_Ca-BrBr
                L5: Cds-Cs/H_or_Val7/Ca
                    L6: Cds-CsH_Ca
                    L6: Cds-CsH_Ca-F
                    L6: Cds-CsH_Ca-Cl
                    L6: Cds-CsH_Ca-Br
                L5: Cds-CsCs_Ca
                L5: Cds-OneDe/H_or_Val7/Ca
                    L6: Cds-OneDeH_Ca
                        L7: Cds-CtH_Ca
                        L7: Cds-CbH_Ca
                        L7: Cds-COH_Ca
                        L7: Cds-CdH_Ca
                        L7: Cds-C=SH_Ca
                    L6: Cds-OneDeH_Ca-F
                        L7: Cds-CtH_Ca-F
                        L7: Cds-CbH_Ca-F
                        L7: Cds-COH_Ca-F
                        L7: Cds-CdH_Ca-F
                        L7: Cds-C=SH_Ca-F
                    L6: Cds-OneDeH_Ca-Cl
                        L7: Cds-CtH_Ca-Cl
                        L7: Cds-CbH_Ca-Cl
                        L7: Cds-COH_Ca-Cl
                        L7: Cds-CdH_Ca-Cl
                        L7: Cds-C=SH_Ca-Cl
                    L6: Cds-OneDeH_Ca-Br
                        L7: Cds-CtH_Ca-Br
                        L7: Cds-CbH_Ca-Br
                        L7: Cds-COH_Ca-Br
                        L7: Cds-CdH_Ca-Br
                        L7: Cds-C=SH_Ca-Br
                L5: Cds-OneDeCs_Ca
                    L6: Cds-CtCs_Ca
                    L6: Cds-CbCs_Ca
                    L6: Cds-COCs_Ca
                    L6: Cds-CdCs_Ca
                    L6: Cds-C=SCs_Ca
                L5: Cds-TwoDe_Ca
                    L6: Cds-CtCt_Ca
                    L6: Cds-CtCb_Ca
                    L6: Cds-CtCO_Ca
                    L6: Cds-CbCb_Ca
                    L6: Cds-CbCO_Ca
                    L6: Cds-COCO_Ca
                    L6: Cds-CdCt_Ca
                    L6: Cds-CdCb_Ca
                    L6: Cds-CdCO_Ca
                    L6: Cds-CtC=S_Ca
                    L6: Cds-CbC=S_Ca
                    L6: Cds-COC=S_Ca
                    L6: Cds-CdCd_Ca
                    L6: Cds-CdC=S_Ca
                    L6: Cds-C=SC=S_Ca
            L4: Cds_Ck
                L5: Cds-/H_or_Val7/H_or_Val7/Ck
                    L6: Cds-HH_Ck
                    L6: Cds-HH_Ck-HF
                    L6: Cds-HH_Ck-HCl
                    L6: Cds-HH_Ck-HBr
                    L6: Cds-HH_Ck-FF
                    L6: Cds-HH_Ck-FCl
                    L6: Cds-HH_Ck-FBr
                    L6: Cds-HH_Ck-ClCl
                    L6: Cds-HH_Ck-ClBr
                    L6: Cds-HH_Ck-BrBr
                L5: Cds-Cs/H_or_Val7/Ck
                    L6: Cds-CsH_Ck
                    L6: Cds-CsH_Ck-F
                    L6: Cds-CsH_Ck-Cl
                    L6: Cds-CsH_Ck-Br
                L5: Cds-CsCs_Ck
                L5: Cds-OneDe/H_or_Val7/Ck
                    L6: Cds-OneDeH_Ck
                    L6: Cds-OneDeH_Ck-F
                    L6: Cds-OneDeH_Ck-Cl
                    L6: Cds-OneDeH_Ck-Br
                L5: Cds-OneDeCs_Ck
                L5: Cds-TwoDe_Ck
        L3: Cdd_Cds
            L4: Ca_Cds
                L5: Ca_Cds-/H_or_Val7/H_or_Val7/
                    L6: Ca_Cds-HH
                        L7: Ca-Cdd_Cds-HH
                    L6: Ca_Cds-HH-HF
                        L7: Ca-Cdd_Cds-HH-HF
                    L6: Ca_Cds-HH-HCl
                        L7: Ca-Cdd_Cds-HH-HCl
                    L6: Ca_Cds-HH-HBr
                        L7: Ca-Cdd_Cds-HH-HBr
                    L6: Ca_Cds-HH-FF
                        L7: Ca-Cdd_Cds-HH-FF
                    L6: Ca_Cds-HH-FCl
                        L7: Ca-Cdd_Cds-HH-FCl
                    L6: Ca_Cds-HH-FBr
                        L7: Ca-Cdd_Cds-HH-FBr
                    L6: Ca_Cds-HH-ClCl
                        L7: Ca-Cdd_Cds-HH-ClCl
                    L6: Ca_Cds-HH-ClBr
                        L7: Ca-Cdd_Cds-HH-ClBr
                    L6: Ca_Cds-HH-BrBr
                        L7: Ca-Cdd_Cds-HH-BrBr
                L5: Ca_Cds-Cs/H_or_Val7/
                    L6: Ca_Cds-CsH
                    L6: Ca_Cds-CsH-F
                    L6: Ca_Cds-CsH-Cl
                    L6: Ca_Cds-CsH-Br
                L5: Ca_Cds-CsCs
                L5: Ca_Cds-OneDe/H_or_Val7/
                    L6: Ca_Cds-OneDeH
                        L7: Ca_Cds-CtH
                        L7: Ca_Cds-CbH
                        L7: Ca_Cds-COH
                        L7: Ca_Cds-CdH
                        L7: Ca_Cds-C=SH
                    L6: Ca_Cds-OneDeH-F
                        L7: Ca_Cds-CtH-F
                        L7: Ca_Cds-CbH-F
                        L7: Ca_Cds-COH-F
                        L7: Ca_Cds-CdH-F
                        L7: Ca_Cds-C=SH-F
                    L6: Ca_Cds-OneDeH-Cl
                        L7: Ca_Cds-CtH-Cl
                        L7: Ca_Cds-CbH-Cl
                        L7: Ca_Cds-COH-Cl
                        L7: Ca_Cds-CdH-Cl
                        L7: Ca_Cds-C=SH-Cl
                    L6: Ca_Cds-OneDeH-Br
                        L7: Ca_Cds-CtH-Br
                        L7: Ca_Cds-CbH-Br
                        L7: Ca_Cds-COH-Br
                        L7: Ca_Cds-CdH-Br
                        L7: Ca_Cds-C=SH-Br
                L5: Ca_Cds-OneDeCs
                    L6: Ca_Cds-CtCs
                    L6: Ca_Cds-CbCs
                    L6: Ca_Cds-COCs
                    L6: Ca_Cds-CdCs
                    L6: Ca_Cds-C=SCs
                L5: Ca_Cds-TwoDe
                    L6: Ca_Cds-CtCt
                    L6: Ca_Cds-CtCb
                    L6: Ca_Cds-CtCO
                    L6: Ca_Cds-CbCb
                    L6: Ca_Cds-CbCO
                    L6: Ca_Cds-COCO
                    L6: Ca_Cds-CdCt
                    L6: Ca_Cds-CdCb
                    L6: Ca_Cds-CdCO
                    L6: Ca_Cds-CtC=S
                    L6: Ca_Cds-CbC=S
                    L6: Ca_Cds-COC=S
                    L6: Ca_Cds-CdCd
                        L7: Ca_Cds-CdCdCdCdCd_cycle
                    L6: Ca_Cds-CdC=S
                    L6: Ca_Cds-C=SC=S
            L4: Ck_Cds
                L5: Ck_Cds-/H_or_Val7/H_or_Val7/
                    L6: Ck_Cds-HH
                    L6: Ck_Cds-HH-HF
                    L6: Ck_Cds-HH-HCl
                    L6: Ck_Cds-HH-HBr
                    L6: Ck_Cds-HH-FF
                    L6: Ck_Cds-HH-FCl
                    L6: Ck_Cds-HH-FBr
                    L6: Ck_Cds-HH-ClCl
                    L6: Ck_Cds-HH-ClBr
                    L6: Ck_Cds-HH-BrBr
                L5: Ck_Cds-Cs/H_or_Val7/
                    L6: Ck_Cds-CsH
                    L6: Ck_Cds-CsH-F
                    L6: Ck_Cds-CsH-Cl
                    L6: Ck_Cds-CsH-Br
                L5: Ck_Cds-CsCs
                L5: Ck_Cds-OneDe/H_or_Val7/
                    L6: Ck_Cds-OneDeH
                        L7: Ck_Cds-CtH
                        L7: Ck_Cds-CbH
                        L7: Ck_Cds-COH
                        L7: Ck_Cds-CdH
                        L7: Ck_Cds-C=SH
                    L6: Ck_Cds-OneDeH-F
                        L7: Ck_Cds-CtH-F
                        L7: Ck_Cds-CbH-F
                        L7: Ck_Cds-COH-F
                        L7: Ck_Cds-CdH-F
                        L7: Ck_Cds-C=SH-F
                    L6: Ck_Cds-OneDeH-Cl
                        L7: Ck_Cds-CtH-Cl
                        L7: Ck_Cds-CbH-Cl
                        L7: Ck_Cds-COH-Cl
                        L7: Ck_Cds-CdH-Cl
                        L7: Ck_Cds-C=SH-Cl
                    L6: Ck_Cds-OneDeH-Br
                        L7: Ck_Cds-CtH-Br
                        L7: Ck_Cds-CbH-Br
                        L7: Ck_Cds-COH-Br
                        L7: Ck_Cds-CdH-Br
                        L7: Ck_Cds-C=SH-Br
                L5: Ck_Cds-OneDeCs
                    L6: Ck_Cds-CtCs
                    L6: Ck_Cds-CbCs
                    L6: Ck_Cds-COCs
                    L6: Ck_Cds-CdCs
                    L6: Ck_Cds-C=SCs
                L5: Ck_Cds-TwoDe
                    L6: Ck_Cds-CtCt
                    L6: Ck_Cds-CtCb
                    L6: Ck_Cds-CtCO
                    L6: Ck_Cds-CbCb
                    L6: Ck_Cds-CbCO
                    L6: Ck_Cds-COCO
                    L6: Ck_Cds-CdCt
                    L6: Ck_Cds-CdCb
                    L6: Ck_Cds-CdCO
                    L6: Ck_Cds-CtC=S
                    L6: Ck_Cds-CbC=S
                    L6: Ck_Cds-COC=S
                    L6: Ck_Cds-CdCd
                    L6: Ck_Cds-CdC=S
                    L6: Ck_Cds-C=SC=S
        L3: Cdd_Cdd
            L4: Ca_Ca
                L5: Ca-Cb_Ca-Cb_cyc6
            L4: Ck_Ck
            L4: Ca_Ck
            L4: Ck_Ca
        L3: Cds_Sd
            L4: Cds-/H_or_Val7/H_or_Val7/Sd
                L5: Cds-HH_Sd
                L5: Cds-HH_Sd-HF
                L5: Cds-HH_Sd-HCl
                L5: Cds-HH_Sd-HBr
                L5: Cds-HH_Sd-FF
                L5: Cds-HH_Sd-FCl
                L5: Cds-HH_Sd-FBr
                L5: Cds-HH_Sd-ClCl
                L5: Cds-HH_Sd-ClBr
                L5: Cds-HH_Sd-BrBr
            L4: Cds-Cs/H_or_Val7/Sd
                L5: Cds-CsH_Sd
                L5: Cds-CsH_Sd-F
                L5: Cds-CsH_Sd-Cl
                L5: Cds-CsH_Sd-Br
            L4: Cds-CsCs_Sd
            L4: Cds-Os/H_or_Val7/Sd
                L5: Cds-OsH_Sd
                L5: Cds-OsH_Sd-F
                L5: Cds-OsH_Sd-Cl
                L5: Cds-OsH_Sd-Br
            L4: Cds-OsCs_Sd
            L4: Cds-Ss/H_or_Val7/Sd
                L5: Cds-SsH_Sd
                L5: Cds-SsH_Sd-F
                L5: Cds-SsH_Sd-Cl
                L5: Cds-SsH_Sd-Br
            L4: Cds-SsCs_Sd
            L4: Cds-OneDe/H_or_Val7/Sd
                L5: Cds-OneDeH_Sd
                    L6: Cds-CtH_Sd
                    L6: Cds-CbH_Sd
                    L6: Cds-COH_Sd
                    L6: Cds-CdH_Sd
                    L6: Cds-C=SH_Sd
                L5: Cds-OneDeH_Sd-F
                    L6: Cds-CtH_Sd-F
                    L6: Cds-CbH_Sd-F
                    L6: Cds-COH_Sd-F
                    L6: Cds-CdH_Sd-F
                    L6: Cds-C=SH_Sd-F
                L5: Cds-OneDeH_Sd-Cl
                    L6: Cds-CtH_Sd-Cl
                    L6: Cds-CbH_Sd-Cl
                    L6: Cds-COH_Sd-Cl
                    L6: Cds-CdH_Sd-Cl
                    L6: Cds-C=SH_Sd-Cl
                L5: Cds-OneDeH_Sd-Br
                    L6: Cds-CtH_Sd-Br
                    L6: Cds-CbH_Sd-Br
                    L6: Cds-COH_Sd-Br
                    L6: Cds-CdH_Sd-Br
                    L6: Cds-C=SH_Sd-Br
            L4: Cds-OneDeCs_Sd
                L5: Cds-CtCs_Sd
                L5: Cds-CbCs_Sd
                L5: Cds-COCs_Sd
                L5: Cds-CdCs_Sd
                L5: Cds-C=SCs_Sd
            L4: Cds-TwoDe_Sd
                L5: Cds-CtCt_Sd
                L5: Cds-CtCb_Sd
                L5: Cds-CtCO_Sd
                L5: Cds-CbCb_Sd
                L5: Cds-CbCO_Sd
                L5: Cds-COCO_Sd
                L5: Cds-CdCt_Sd
                L5: Cds-CdCb_Sd
                L5: Cds-CdCO_Sd
                L5: Cds-CtC=S_Sd
                L5: Cds-CbC=S_Sd
                L5: Cds-COC=S_Sd
                L5: Cds-CdCd_Sd
                L5: Cds-CdC=S_Sd
                L5: Cds-C=SC=S_Sd
        L3: Cds_Nd
            L4: Cds_N3d
                L5: Cds-/H_or_Val7/H_or_Val7/N3d
                    L6: Cds-HH_N3d
                    L6: Cds-HH_N3d-HF
                    L6: Cds-HH_N3d-HCl
                    L6: Cds-HH_N3d-HBr
                    L6: Cds-HH_N3d-FF
                    L6: Cds-HH_N3d-FCl
                    L6: Cds-HH_N3d-FBr
                    L6: Cds-HH_N3d-ClCl
                    L6: Cds-HH_N3d-ClBr
                    L6: Cds-HH_N3d-BrBr
                L5: Cds-NonDe/H_or_Val7/N3d
                    L6: Cds-NonDeH_N3d
                    L6: Cds-NonDeH_N3d-F
                    L6: Cds-NonDeH_N3d-Cl
                    L6: Cds-NonDeH_N3d-Br
                L5: Cds-NonDe2_N3d
        L3: Cds_Cds
            L4: Cds-/H_or_Val7/H_or_Val7/Cds
                L5: Cds-HH_Cds
                    L6: Cds-HH_Cds-HH
                    L6: Cds-HH_Cds-CsH
                        L7: Cds-HH_Cds-Cs\O2s/H
                        L7: Cds-HH_Cds-Cs\H3/H
                    L6: Cds-HH_Cds-CsCs
                    L6: Cds-HH_Cds-OsH
                    L6: Cds-HH_Cds-OsCs
                    L6: Cds-HH_Cds-OsOs
                    L6: Cds-HH_Cds-SsH
                    L6: Cds-HH_Cds-SsCs
                    L6: Cds-HH_Cds-SsOs
                    L6: Cds-HH_Cds-SsSs
                    L6: Cds-HH_Cds-OneDe
                        L7: Cds-HH_Cds-OneDeH
                            L8: Cds-HH_Cds-CtH
                            L8: Cds-HH_Cds-CbH
                            L8: Cds-HH_Cds-COH
                            L8: Cds-HH_Cds-(Cd-Cd-Cb)H
                            L8: Cds-HH_Cds-CdH
                            L8: Cds-HH_Cds-C=SH
                        L7: Cds-HH_Cds-OneDeCs
                            L8: Cds-HH_Cds-CtCs
                            L8: Cds-HH_Cds-CbCs
                            L8: Cds-HH_Cds-COCs
                            L8: Cds-HH_Cds-CdCs
                            L8: Cds-HH_Cds-C=SCs
                        L7: Cds-HH_Cds-OneDeOs
                            L8: Cds-HH_Cds-CtOs
                            L8: Cds-HH_Cds-CbOs
                            L8: Cds-HH_Cds-COOs
                            L8: Cds-HH_Cds-CdOs
                            L8: Cds-HH_Cds-C=SOs
                        L7: Cds-HH_Cds-OneDeSs
                            L8: Cds-HH_Cds-CtSs
                            L8: Cds-HH_Cds-CbSs
                            L8: Cds-HH_Cds-COSs
                            L8: Cds-HH_Cds-CdSs
                            L8: Cds-HH_Cds-C=SSs
                    L6: Cds-HH_Cds-TwoDe
                        L7: Cds-HH_Cds-CtCt
                        L7: Cds-HH_Cds-CtCb
                        L7: Cds-HH_Cds-CtCO
                        L7: Cds-HH_Cds-CbCb
                        L7: Cds-HH_Cds-CbCO
                        L7: Cds-HH_Cds-COCO
                        L7: Cds-HH_Cds-CdCt
                        L7: Cds-HH_Cds-CdCb
                            L8: Cds-HH_Cds-CdCbCbCdCdCd_cycle
                        L7: Cds-HH_Cds-CdCO
                        L7: Cds-HH_Cds-CtC=S
                        L7: Cds-HH_Cds-CbC=S
                        L7: Cds-HH_Cds-COC=S
                        L7: Cds-HH_Cds-CdCd
                            L8: Cds-HH_Cds-CdCd_cyc
                        L7: Cds-HH_Cds-CdC=S
                        L7: Cds-HH_Cds-C=SC=S
                    L6: Cds-HH_Cds-CtH-HHBr
                    L6: Cds-HH_Cds-CbH-HHBr
                    L6: Cds-HH_Cds-COH-HHBr
                    L6: Cds-HH_Cds-C=SH-HHBr
                    L6: Cds-HH_Cds-CtH-HHF
                    L6: Cds-HH_Cds-CbH-HHF
                    L6: Cds-HH_Cds-COH-HHF
                    L6: Cds-HH_Cds-C=SH-HHF
                    L6: Cds-HH_Cds-CtH-HHCl
                    L6: Cds-HH_Cds-CbH-HHCl
                    L6: Cds-HH_Cds-COH-HHCl
                    L6: Cds-HH_Cds-C=SH-HHCl
                L5: Cds-HH_Cds-HF
                    L6: Cds-HH_Cds-CtH-HFCl
                    L6: Cds-HH_Cds-CbH-HFCl
                    L6: Cds-HH_Cds-COH-HFCl
                    L6: Cds-HH_Cds-C=SH-HFCl
                    L6: Cds-HH_Cds-CtH-HFBr
                    L6: Cds-HH_Cds-CbH-HFBr
                    L6: Cds-HH_Cds-COH-HFBr
                    L6: Cds-HH_Cds-C=SH-HFBr
                    L6: Cds-HH_Cds-CdCbCbCdCdCd_cycle-HF
                    L6: Cds-HH_Cds-OneDeCs-HF
                        L7: Cds-HH_Cds-CtCs-HF
                        L7: Cds-HH_Cds-CbCs-HF
                        L7: Cds-HH_Cds-COCs-HF
                        L7: Cds-HH_Cds-CdCs-HF
                        L7: Cds-HH_Cds-C=SCs-HF
                    L6: Cds-HH_Cds-OneDeOs-HF
                        L7: Cds-HH_Cds-CtOs-HF
                        L7: Cds-HH_Cds-CbOs-HF
                        L7: Cds-HH_Cds-COOs-HF
                        L7: Cds-HH_Cds-CdOs-HF
                        L7: Cds-HH_Cds-C=SOs-HF
                    L6: Cds-HH_Cds-OneDeSs-HF
                        L7: Cds-HH_Cds-CtSs-HF
                        L7: Cds-HH_Cds-CbSs-HF
                        L7: Cds-HH_Cds-COSs-HF
                        L7: Cds-HH_Cds-CdSs-HF
                        L7: Cds-HH_Cds-C=SSs-HF
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-HHF
                    L6: Cds-HH_Cds-CdH-HHF
                    L6: Cds-HH_Cds-CdCd_cyc-HF
                    L6: Cds-HH_Cds-CtH-HFF
                    L6: Cds-HH_Cds-CbH-HFF
                    L6: Cds-HH_Cds-COH-HFF
                    L6: Cds-HH_Cds-C=SH-HFF
                L5: Cds-HH_Cds-HCl
                    L6: Cds-HH_Cds-CtH-HClCl
                    L6: Cds-HH_Cds-CbH-HClCl
                    L6: Cds-HH_Cds-COH-HClCl
                    L6: Cds-HH_Cds-C=SH-HClCl
                    L6: Cds-HH_Cds-CtH-HClBr
                    L6: Cds-HH_Cds-CbH-HClBr
                    L6: Cds-HH_Cds-COH-HClBr
                    L6: Cds-HH_Cds-C=SH-HClBr
                    L6: Cds-HH_Cds-CdCd_cyc-HCl
                    L6: Cds-HH_Cds-CdCbCbCdCdCd_cycle-HCl
                    L6: Cds-HH_Cds-OneDeCs-HCl
                        L7: Cds-HH_Cds-CtCs-HCl
                        L7: Cds-HH_Cds-CbCs-HCl
                        L7: Cds-HH_Cds-COCs-HCl
                        L7: Cds-HH_Cds-CdCs-HCl
                        L7: Cds-HH_Cds-C=SCs-HCl
                    L6: Cds-HH_Cds-OneDeOs-HCl
                        L7: Cds-HH_Cds-CtOs-HCl
                        L7: Cds-HH_Cds-CbOs-HCl
                        L7: Cds-HH_Cds-COOs-HCl
                        L7: Cds-HH_Cds-CdOs-HCl
                        L7: Cds-HH_Cds-C=SOs-HCl
                    L6: Cds-HH_Cds-OneDeSs-HCl
                        L7: Cds-HH_Cds-CtSs-HCl
                        L7: Cds-HH_Cds-CbSs-HCl
                        L7: Cds-HH_Cds-COSs-HCl
                        L7: Cds-HH_Cds-CdSs-HCl
                        L7: Cds-HH_Cds-C=SSs-HCl
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-HHCl
                    L6: Cds-HH_Cds-CdH-HHCl
                L5: Cds-HH_Cds-HBr
                    L6: Cds-HH_Cds-OneDeCs-HBr
                        L7: Cds-HH_Cds-CtCs-HBr
                        L7: Cds-HH_Cds-CbCs-HBr
                        L7: Cds-HH_Cds-COCs-HBr
                        L7: Cds-HH_Cds-CdCs-HBr
                        L7: Cds-HH_Cds-C=SCs-HBr
                    L6: Cds-HH_Cds-OneDeOs-HBr
                        L7: Cds-HH_Cds-CtOs-HBr
                        L7: Cds-HH_Cds-CbOs-HBr
                        L7: Cds-HH_Cds-COOs-HBr
                        L7: Cds-HH_Cds-CdOs-HBr
                        L7: Cds-HH_Cds-C=SOs-HBr
                    L6: Cds-HH_Cds-OneDeSs-HBr
                        L7: Cds-HH_Cds-CtSs-HBr
                        L7: Cds-HH_Cds-CbSs-HBr
                        L7: Cds-HH_Cds-COSs-HBr
                        L7: Cds-HH_Cds-CdSs-HBr
                        L7: Cds-HH_Cds-C=SSs-HBr
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-HHBr
                    L6: Cds-HH_Cds-CdH-HHBr
                    L6: Cds-HH_Cds-CtH-HBrBr
                    L6: Cds-HH_Cds-CbH-HBrBr
                    L6: Cds-HH_Cds-COH-HBrBr
                    L6: Cds-HH_Cds-C=SH-HBrBr
                    L6: Cds-HH_Cds-CdCbCbCdCdCd_cycle-HBr
                    L6: Cds-HH_Cds-CdCd_cyc-HBr
                L5: Cds-HH_Cds-FF
                    L6: Cds-HH_Cds-CtH-FFCl
                    L6: Cds-HH_Cds-CbH-FFCl
                    L6: Cds-HH_Cds-COH-FFCl
                    L6: Cds-HH_Cds-C=SH-FFCl
                    L6: Cds-HH_Cds-CtH-FFBr
                    L6: Cds-HH_Cds-CbH-FFBr
                    L6: Cds-HH_Cds-COH-FFBr
                    L6: Cds-HH_Cds-C=SH-FFBr
                    L6: Cds-HH_Cds-OneDeCs-FF
                        L7: Cds-HH_Cds-CtCs-FF
                        L7: Cds-HH_Cds-CbCs-FF
                        L7: Cds-HH_Cds-COCs-FF
                        L7: Cds-HH_Cds-CdCs-FF
                        L7: Cds-HH_Cds-C=SCs-FF
                    L6: Cds-HH_Cds-OneDeOs-FF
                        L7: Cds-HH_Cds-CtOs-FF
                        L7: Cds-HH_Cds-CbOs-FF
                        L7: Cds-HH_Cds-COOs-FF
                        L7: Cds-HH_Cds-CdOs-FF
                        L7: Cds-HH_Cds-C=SOs-FF
                    L6: Cds-HH_Cds-OneDeSs-FF
                        L7: Cds-HH_Cds-CtSs-FF
                        L7: Cds-HH_Cds-CbSs-FF
                        L7: Cds-HH_Cds-COSs-FF
                        L7: Cds-HH_Cds-CdSs-FF
                        L7: Cds-HH_Cds-C=SSs-FF
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-HFF
                    L6: Cds-HH_Cds-CdH-HFF
                    L6: Cds-HH_Cds-Cs\O2s/H-FFF
                    L6: Cds-HH_Cds-Cs\H3/H-HHHFFF
                    L6: Cds-HH_Cds-Cs\H3/H-HHFFFF
                    L6: Cds-HH_Cds-Cs\H3/H-HFFFFF
                    L6: Cds-HH_Cds-Cs\H3/H-FFFFFF
                    L6: Cds-HH_Cds-CdCbCbCdCdCd_cycle-FF
                    L6: Cds-HH_Cds-CdCd_cyc-FF
                    L6: Cds-HH_Cds-CtH-FFF
                    L6: Cds-HH_Cds-CbH-FFF
                    L6: Cds-HH_Cds-COH-FFF
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-FFF
                    L6: Cds-HH_Cds-CdH-FFF
                    L6: Cds-HH_Cds-C=SH-FFF
                L5: Cds-HH_Cds-FCl
                    L6: Cds-HH_Cds-OneDeCs-FCl
                        L7: Cds-HH_Cds-CtCs-FCl
                        L7: Cds-HH_Cds-CbCs-FCl
                        L7: Cds-HH_Cds-COCs-FCl
                        L7: Cds-HH_Cds-CdCs-FCl
                        L7: Cds-HH_Cds-C=SCs-FCl
                    L6: Cds-HH_Cds-OneDeOs-FCl
                        L7: Cds-HH_Cds-CtOs-FCl
                        L7: Cds-HH_Cds-CbOs-FCl
                        L7: Cds-HH_Cds-COOs-FCl
                        L7: Cds-HH_Cds-CdOs-FCl
                        L7: Cds-HH_Cds-C=SOs-FCl
                    L6: Cds-HH_Cds-OneDeSs-FCl
                        L7: Cds-HH_Cds-CtSs-FCl
                        L7: Cds-HH_Cds-CbSs-FCl
                        L7: Cds-HH_Cds-COSs-FCl
                        L7: Cds-HH_Cds-CdSs-FCl
                        L7: Cds-HH_Cds-C=SSs-FCl
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-HFCl
                    L6: Cds-HH_Cds-CdH-HFCl
                    L6: Cds-HH_Cds-CtH-FClCl
                    L6: Cds-HH_Cds-CbH-FClCl
                    L6: Cds-HH_Cds-COH-FClCl
                    L6: Cds-HH_Cds-C=SH-FClCl
                    L6: Cds-HH_Cds-CdCd_cyc-FCl
                    L6: Cds-HH_Cds-CtH-FClBr
                    L6: Cds-HH_Cds-CbH-FClBr
                    L6: Cds-HH_Cds-COH-FClBr
                    L6: Cds-HH_Cds-C=SH-FClBr
                    L6: Cds-HH_Cds-CdCbCbCdCdCd_cycle-FCl
                L5: Cds-HH_Cds-FBr
                    L6: Cds-HH_Cds-CtH-FBrBr
                    L6: Cds-HH_Cds-CbH-FBrBr
                    L6: Cds-HH_Cds-COH-FBrBr
                    L6: Cds-HH_Cds-C=SH-FBrBr
                    L6: Cds-HH_Cds-CdCbCbCdCdCd_cycle-FBr
                    L6: Cds-HH_Cds-CdCd_cyc-FBr
                    L6: Cds-HH_Cds-OneDeCs-FBr
                        L7: Cds-HH_Cds-CtCs-FBr
                        L7: Cds-HH_Cds-CbCs-FBr
                        L7: Cds-HH_Cds-COCs-FBr
                        L7: Cds-HH_Cds-CdCs-FBr
                        L7: Cds-HH_Cds-C=SCs-FBr
                    L6: Cds-HH_Cds-OneDeOs-FBr
                        L7: Cds-HH_Cds-CtOs-FBr
                        L7: Cds-HH_Cds-CbOs-FBr
                        L7: Cds-HH_Cds-COOs-FBr
                        L7: Cds-HH_Cds-CdOs-FBr
                        L7: Cds-HH_Cds-C=SOs-FBr
                    L6: Cds-HH_Cds-OneDeSs-FBr
                        L7: Cds-HH_Cds-CtSs-FBr
                        L7: Cds-HH_Cds-CbSs-FBr
                        L7: Cds-HH_Cds-COSs-FBr
                        L7: Cds-HH_Cds-CdSs-FBr
                        L7: Cds-HH_Cds-C=SSs-FBr
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-HFBr
                    L6: Cds-HH_Cds-CdH-HFBr
                L5: Cds-HH_Cds-ClCl
                    L6: Cds-HH_Cds-CtH-ClClBr
                    L6: Cds-HH_Cds-CbH-ClClBr
                    L6: Cds-HH_Cds-COH-ClClBr
                    L6: Cds-HH_Cds-C=SH-ClClBr
                    L6: Cds-HH_Cds-CtH-ClClCl
                    L6: Cds-HH_Cds-CbH-ClClCl
                    L6: Cds-HH_Cds-COH-ClClCl
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-ClClCl
                    L6: Cds-HH_Cds-CdH-ClClCl
                    L6: Cds-HH_Cds-C=SH-ClClCl
                    L6: Cds-HH_Cds-CdCd_cyc-ClCl
                    L6: Cds-HH_Cds-CdCbCbCdCdCd_cycle-ClCl
                    L6: Cds-HH_Cds-OneDeCs-ClCl
                        L7: Cds-HH_Cds-CtCs-ClCl
                        L7: Cds-HH_Cds-CbCs-ClCl
                        L7: Cds-HH_Cds-COCs-ClCl
                        L7: Cds-HH_Cds-CdCs-ClCl
                        L7: Cds-HH_Cds-C=SCs-ClCl
                    L6: Cds-HH_Cds-OneDeOs-ClCl
                        L7: Cds-HH_Cds-CtOs-ClCl
                        L7: Cds-HH_Cds-CbOs-ClCl
                        L7: Cds-HH_Cds-COOs-ClCl
                        L7: Cds-HH_Cds-CdOs-ClCl
                        L7: Cds-HH_Cds-C=SOs-ClCl
                    L6: Cds-HH_Cds-OneDeSs-ClCl
                        L7: Cds-HH_Cds-CtSs-ClCl
                        L7: Cds-HH_Cds-CbSs-ClCl
                        L7: Cds-HH_Cds-COSs-ClCl
                        L7: Cds-HH_Cds-CdSs-ClCl
                        L7: Cds-HH_Cds-C=SSs-ClCl
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-HClCl
                    L6: Cds-HH_Cds-CdH-HClCl
                L5: Cds-HH_Cds-ClBr
                    L6: Cds-HH_Cds-CtH-ClBrBr
                    L6: Cds-HH_Cds-CbH-ClBrBr
                    L6: Cds-HH_Cds-COH-ClBrBr
                    L6: Cds-HH_Cds-C=SH-ClBrBr
                    L6: Cds-HH_Cds-CdCbCbCdCdCd_cycle-ClBr
                    L6: Cds-HH_Cds-CdCd_cyc-ClBr
                    L6: Cds-HH_Cds-OneDeCs-ClBr
                        L7: Cds-HH_Cds-CtCs-ClBr
                        L7: Cds-HH_Cds-CbCs-ClBr
                        L7: Cds-HH_Cds-COCs-ClBr
                        L7: Cds-HH_Cds-CdCs-ClBr
                        L7: Cds-HH_Cds-C=SCs-ClBr
                    L6: Cds-HH_Cds-OneDeOs-ClBr
                        L7: Cds-HH_Cds-CtOs-ClBr
                        L7: Cds-HH_Cds-CbOs-ClBr
                        L7: Cds-HH_Cds-COOs-ClBr
                        L7: Cds-HH_Cds-CdOs-ClBr
                        L7: Cds-HH_Cds-C=SOs-ClBr
                    L6: Cds-HH_Cds-OneDeSs-ClBr
                        L7: Cds-HH_Cds-CtSs-ClBr
                        L7: Cds-HH_Cds-CbSs-ClBr
                        L7: Cds-HH_Cds-COSs-ClBr
                        L7: Cds-HH_Cds-CdSs-ClBr
                        L7: Cds-HH_Cds-C=SSs-ClBr
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-HClBr
                    L6: Cds-HH_Cds-CdH-HClBr
                L5: Cds-HH_Cds-BrBr
                    L6: Cds-HH_Cds-CtH-BrBrBr
                    L6: Cds-HH_Cds-CbH-BrBrBr
                    L6: Cds-HH_Cds-COH-BrBrBr
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-BrBrBr
                    L6: Cds-HH_Cds-CdH-BrBrBr
                    L6: Cds-HH_Cds-C=SH-BrBrBr
                    L6: Cds-HH_Cds-OneDeCs-BrBr
                        L7: Cds-HH_Cds-CtCs-BrBr
                        L7: Cds-HH_Cds-CbCs-BrBr
                        L7: Cds-HH_Cds-COCs-BrBr
                        L7: Cds-HH_Cds-CdCs-BrBr
                        L7: Cds-HH_Cds-C=SCs-BrBr
                    L6: Cds-HH_Cds-OneDeOs-BrBr
                        L7: Cds-HH_Cds-CtOs-BrBr
                        L7: Cds-HH_Cds-CbOs-BrBr
                        L7: Cds-HH_Cds-COOs-BrBr
                        L7: Cds-HH_Cds-CdOs-BrBr
                        L7: Cds-HH_Cds-C=SOs-BrBr
                    L6: Cds-HH_Cds-OneDeSs-BrBr
                        L7: Cds-HH_Cds-CtSs-BrBr
                        L7: Cds-HH_Cds-CbSs-BrBr
                        L7: Cds-HH_Cds-COSs-BrBr
                        L7: Cds-HH_Cds-CdSs-BrBr
                        L7: Cds-HH_Cds-C=SSs-BrBr
                    L6: Cds-HH_Cds-(Cd-Cd-Cb)H-HBrBr
                    L6: Cds-HH_Cds-CdH-HBrBr
                    L6: Cds-HH_Cds-CdCbCbCdCdCd_cycle-BrBr
                    L6: Cds-HH_Cds-CdCd_cyc-BrBr
            L4: Cds-Cs/H_or_Val7/Cds
                L5: Cds-CsH_Cds
                    L6: Cds-CsH_Cds-HH
                        L7: Cds-Cs\O2s/H_Cds-HH
                    L6: Cds-CsH_Cds-CsH
                        L7: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6
                    L6: Cds-CsH_Cds-CsCs
                    L6: Cds-CsH_Cds-OsH
                    L6: Cds-CsH_Cds-OsCs
                    L6: Cds-CsH_Cds-OsOs
                    L6: Cds-CsH_Cds-SsH
                    L6: Cds-CsH_Cds-SsCs
                    L6: Cds-CsH_Cds-SsOs
                    L6: Cds-CsH_Cds-SsSs
                    L6: Cds-CsH_Cds-OneDe
                        L7: Cds-CsH_Cds-OneDeH
                            L8: Cds-CsH_Cds-CtH
                            L8: Cds-CsH_Cds-CbH
                                L9: Cds-CsH_Cds-CbH-indene
                                L9: Cds-CsH_Cds-CbH-dihydronaphthalene
                            L8: Cds-CsH_Cds-COH
                            L8: Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H
                            L8: Cds-CsH_Cds-(Cd-Cd-Cd)H
                            L8: Cds-CsH_Cds-Cd(Cd)H
                            L8: Cds-CsH_Cds-CdH
                                L9: Cds-CsH_Cds-(CdsH-Cds)_cyc5
                            L8: Cds-CsH_Cds-C=SH
                        L7: Cds-CsH_Cds-OneDeCs
                            L8: Cds-CsH_Cds-CtCs
                            L8: Cds-CsH_Cds-CbCs
                                L9: Cds-CsH_Cds-CbCs-dihydronaphthalene
                            L8: Cds-CsH_Cds-COCs
                            L8: Cds-CsH_Cds-CdCs
                            L8: Cds-CsH_Cds-C=SCs
                        L7: Cds-CsH_Cds-OneDeOs
                            L8: Cds-CsH_Cds-CtOs
                            L8: Cds-CsH_Cds-CbOs
                            L8: Cds-CsH_Cds-COOs
                            L8: Cds-CsH_Cds-CdOs
                            L8: Cds-CsH_Cds-C=SOs
                        L7: Cds-CsH_Cds-OneDeSs
                            L8: Cds-CsH_Cds-CtSs
                            L8: Cds-CsH_Cds-CbSs
                            L8: Cds-CsH_Cds-COSs
                            L8: Cds-CsH_Cds-CdSs
                            L8: Cds-CsH_Cds-C=SSs
                    L6: Cds-CsH_Cds-TwoDe
                        L7: Cds-CsH_Cds-CtCt
                        L7: Cds-CsH_Cds-CtCb
                        L7: Cds-CsH_Cds-CtCO
                        L7: Cds-CsH_Cds-CbCb
                        L7: Cds-CsH_Cds-CbCO
                        L7: Cds-CsH_Cds-COCO
                        L7: Cds-CsH_Cds-CdCt
                        L7: Cds-CsH_Cds-CdCb
                        L7: Cds-CsH_Cds-CdCO
                        L7: Cds-CsH_Cds-CtC=S
                        L7: Cds-CsH_Cds-CbC=S
                        L7: Cds-CsH_Cds-COC=S
                        L7: Cds-CsH_Cds-CdCd
                        L7: Cds-CsH_Cds-CdC=S
                        L7: Cds-CsH_Cds-C=SC=S
                    L6: Cds-Cs\O2s/H_Cds-HH-HHCl
                    L6: Cds-Cs\O2s/H_Cds-HH-HHBr
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-HF
                    L6: Cds-Cs\O2s/H_Cds-HH-HFCl
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-HCl
                    L6: Cds-Cs\O2s/H_Cds-HH-HFF
                    L6: Cds-Cs\O2s/H_Cds-HH-HFBr
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-HBr
                    L6: Cds-Cs\O2s/H_Cds-HH-HClBr
                    L6: Cds-Cs\O2s/H_Cds-HH-HClCl
                    L6: Cds-Cs\O2s/H_Cds-HH-HBrBr
                    L6: Cds-CsH_Cds-CtH-HBr
                    L6: Cds-CsH_Cds-CbH-HBr
                        L7: Cds-CsH_Cds-CbH-indene-HBr
                        L7: Cds-CsH_Cds-CbH-dihydronaphthalene-HBr
                    L6: Cds-CsH_Cds-COH-HBr
                    L6: Cds-CsH_Cds-C=SH-HBr
                    L6: Cds-CsH_Cds-(CdsH-Cds)_cyc5-HBr
                    L6: Cds-Cs\O2s/H_Cds-HH-HHF
                    L6: Cds-CsH_Cds-CtH-HCl
                    L6: Cds-CsH_Cds-CbH-HCl
                        L7: Cds-CsH_Cds-CbH-indene-HCl
                        L7: Cds-CsH_Cds-CbH-dihydronaphthalene-HCl
                    L6: Cds-CsH_Cds-COH-HCl
                    L6: Cds-CsH_Cds-C=SH-HCl
                    L6: Cds-CsH_Cds-(CdsH-Cds)_cyc5-HCl
                    L6: Cds-CsH_Cds-CtH-HF
                    L6: Cds-CsH_Cds-CbH-HF
                        L7: Cds-CsH_Cds-CbH-indene-HF
                        L7: Cds-CsH_Cds-CbH-dihydronaphthalene-HF
                    L6: Cds-CsH_Cds-COH-HF
                    L6: Cds-CsH_Cds-C=SH-HF
                    L6: Cds-CsH_Cds-(CdsH-Cds)_cyc5-HF
                L5: Cds-CsH_Cds-F
                    L6: Cds-CsH_Cds-OneDeCs-F
                        L7: Cds-CsH_Cds-CtCs-F
                        L7: Cds-CsH_Cds-CbCs-F
                            L8: Cds-CsH_Cds-CbCs-dihydronaphthalene-F
                        L7: Cds-CsH_Cds-COCs-F
                        L7: Cds-CsH_Cds-CdCs-F
                        L7: Cds-CsH_Cds-C=SCs-F
                    L6: Cds-CsH_Cds-OneDeOs-F
                        L7: Cds-CsH_Cds-CtOs-F
                        L7: Cds-CsH_Cds-CbOs-F
                        L7: Cds-CsH_Cds-COOs-F
                        L7: Cds-CsH_Cds-CdOs-F
                        L7: Cds-CsH_Cds-C=SOs-F
                    L6: Cds-CsH_Cds-OneDeSs-F
                        L7: Cds-CsH_Cds-CtSs-F
                        L7: Cds-CsH_Cds-CbSs-F
                        L7: Cds-CsH_Cds-COSs-F
                        L7: Cds-CsH_Cds-CdSs-F
                        L7: Cds-CsH_Cds-C=SSs-F
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-HF
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd)H-HF
                    L6: Cds-CsH_Cds-Cd(Cd)H-HF
                    L6: Cds-CsH_Cds-CdH-HF
                    L6: Cds-CsH_Cds-CtH-FF
                    L6: Cds-CsH_Cds-CbH-FF
                        L7: Cds-CsH_Cds-CbH-indene-FF
                        L7: Cds-CsH_Cds-CbH-dihydronaphthalene-FF
                    L6: Cds-CsH_Cds-COH-FF
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-FF
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd)H-FF
                    L6: Cds-CsH_Cds-Cd(Cd)H-FF
                    L6: Cds-CsH_Cds-CdH-FF
                        L7: Cds-CsH_Cds-(CdsH-Cds)_cyc5-FF
                    L6: Cds-CsH_Cds-C=SH-FF
                    L6: Cds-Cs\O2s/H_Cds-HH-FClBr
                    L6: Cds-Cs\O2s/H_Cds-HH-FBrBr
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-FF
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-FCl
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-FBr
                    L6: Cds-CsH_Cds-CtH-FCl
                    L6: Cds-CsH_Cds-CbH-FCl
                        L7: Cds-CsH_Cds-CbH-indene-FCl
                        L7: Cds-CsH_Cds-CbH-dihydronaphthalene-FCl
                    L6: Cds-CsH_Cds-COH-FCl
                    L6: Cds-CsH_Cds-C=SH-FCl
                    L6: Cds-CsH_Cds-(CdsH-Cds)_cyc5-FCl
                    L6: Cds-Cs\O2s/H_Cds-HH-FClCl
                    L6: Cds-Cs\O2s/H_Cds-HH-FFF
                    L6: Cds-Cs\O2s/H_Cds-HH-FFBr
                    L6: Cds-Cs\O2s/H_Cds-HH-FFCl
                    L6: Cds-CsH_Cds-CtH-FBr
                    L6: Cds-CsH_Cds-CbH-FBr
                        L7: Cds-CsH_Cds-CbH-indene-FBr
                        L7: Cds-CsH_Cds-CbH-dihydronaphthalene-FBr
                    L6: Cds-CsH_Cds-COH-FBr
                    L6: Cds-CsH_Cds-C=SH-FBr
                    L6: Cds-CsH_Cds-(CdsH-Cds)_cyc5-FBr
                L5: Cds-CsH_Cds-Cl
                    L6: Cds-CsH_Cds-OneDeCs-Cl
                        L7: Cds-CsH_Cds-CtCs-Cl
                        L7: Cds-CsH_Cds-CbCs-Cl
                            L8: Cds-CsH_Cds-CbCs-dihydronaphthalene-Cl
                        L7: Cds-CsH_Cds-COCs-Cl
                        L7: Cds-CsH_Cds-CdCs-Cl
                        L7: Cds-CsH_Cds-C=SCs-Cl
                    L6: Cds-CsH_Cds-OneDeOs-Cl
                        L7: Cds-CsH_Cds-CtOs-Cl
                        L7: Cds-CsH_Cds-CbOs-Cl
                        L7: Cds-CsH_Cds-COOs-Cl
                        L7: Cds-CsH_Cds-CdOs-Cl
                        L7: Cds-CsH_Cds-C=SOs-Cl
                    L6: Cds-CsH_Cds-OneDeSs-Cl
                        L7: Cds-CsH_Cds-CtSs-Cl
                        L7: Cds-CsH_Cds-CbSs-Cl
                        L7: Cds-CsH_Cds-COSs-Cl
                        L7: Cds-CsH_Cds-CdSs-Cl
                        L7: Cds-CsH_Cds-C=SSs-Cl
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-HCl
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd)H-HCl
                    L6: Cds-CsH_Cds-Cd(Cd)H-HCl
                    L6: Cds-CsH_Cds-CdH-HCl
                    L6: Cds-Cs\O2s/H_Cds-HH-ClBrBr
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-ClCl
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-ClBr
                    L6: Cds-CsH_Cds-CtH-ClCl
                    L6: Cds-CsH_Cds-CbH-ClCl
                        L7: Cds-CsH_Cds-CbH-indene-ClCl
                        L7: Cds-CsH_Cds-CbH-dihydronaphthalene-ClCl
                    L6: Cds-CsH_Cds-COH-ClCl
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-ClCl
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd)H-ClCl
                    L6: Cds-CsH_Cds-Cd(Cd)H-ClCl
                    L6: Cds-CsH_Cds-CdH-ClCl
                        L7: Cds-CsH_Cds-(CdsH-Cds)_cyc5-ClCl
                    L6: Cds-CsH_Cds-C=SH-ClCl
                    L6: Cds-CsH_Cds-CtH-ClBr
                    L6: Cds-CsH_Cds-CbH-ClBr
                        L7: Cds-CsH_Cds-CbH-indene-ClBr
                        L7: Cds-CsH_Cds-CbH-dihydronaphthalene-ClBr
                    L6: Cds-CsH_Cds-COH-ClBr
                    L6: Cds-CsH_Cds-C=SH-ClBr
                    L6: Cds-CsH_Cds-(CdsH-Cds)_cyc5-ClBr
                    L6: Cds-Cs\O2s/H_Cds-HH-ClClCl
                    L6: Cds-Cs\O2s/H_Cds-HH-ClClBr
                L5: Cds-CsH_Cds-Br
                    L6: Cds-CsH_Cds-CtH-BrBr
                    L6: Cds-CsH_Cds-CbH-BrBr
                        L7: Cds-CsH_Cds-CbH-indene-BrBr
                        L7: Cds-CsH_Cds-CbH-dihydronaphthalene-BrBr
                    L6: Cds-CsH_Cds-COH-BrBr
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-BrBr
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd)H-BrBr
                    L6: Cds-CsH_Cds-Cd(Cd)H-BrBr
                    L6: Cds-CsH_Cds-CdH-BrBr
                        L7: Cds-CsH_Cds-(CdsH-Cds)_cyc5-BrBr
                    L6: Cds-CsH_Cds-C=SH-BrBr
                    L6: Cds-Cs\O2s/H_Cds-HH-BrBrBr
                    L6: Cds-CsH_Cds-(CsH-Cds-Cds)_cyc6-BrBr
                    L6: Cds-CsH_Cds-OneDeCs-Br
                        L7: Cds-CsH_Cds-CtCs-Br
                        L7: Cds-CsH_Cds-CbCs-Br
                            L8: Cds-CsH_Cds-CbCs-dihydronaphthalene-Br
                        L7: Cds-CsH_Cds-COCs-Br
                        L7: Cds-CsH_Cds-CdCs-Br
                        L7: Cds-CsH_Cds-C=SCs-Br
                    L6: Cds-CsH_Cds-OneDeOs-Br
                        L7: Cds-CsH_Cds-CtOs-Br
                        L7: Cds-CsH_Cds-CbOs-Br
                        L7: Cds-CsH_Cds-COOs-Br
                        L7: Cds-CsH_Cds-CdOs-Br
                        L7: Cds-CsH_Cds-C=SOs-Br
                    L6: Cds-CsH_Cds-OneDeSs-Br
                        L7: Cds-CsH_Cds-CtSs-Br
                        L7: Cds-CsH_Cds-CbSs-Br
                        L7: Cds-CsH_Cds-COSs-Br
                        L7: Cds-CsH_Cds-CdSs-Br
                        L7: Cds-CsH_Cds-C=SSs-Br
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd-Cd-Cd)H-HBr
                    L6: Cds-CsH_Cds-(Cd-Cd-Cd)H-HBr
                    L6: Cds-CsH_Cds-Cd(Cd)H-HBr
                    L6: Cds-CsH_Cds-CdH-HBr
            L4: Cds-CsCs_Cds
                L5: Cds-CsCs_Cds-CsCs
                L5: Cds-CsCs_Cds-OsCs
                L5: Cds-CsCs_Cds-OsOs
                L5: Cds-CsCs_Cds-SsCs
                L5: Cds-CsCs_Cds-SsOs
                L5: Cds-CsCs_Cds-SsSs
                L5: Cds-CsCs_Cds-OneDe
                    L6: Cds-CsCs_Cds-OneDeCs
                        L7: Cds-CsCs_Cds-CtCs
                        L7: Cds-CsCs_Cds-CbCs
                        L7: Cds-CsCs_Cds-COCs
                        L7: Cds-CsCs_Cds-CdCs
                        L7: Cds-CsCs_Cds-C=SCs
                    L6: Cds-CsCs_Cds-OneDeOs
                        L7: Cds-CsCs_Cds-CtOs
                        L7: Cds-CsCs_Cds-CbOs
                        L7: Cds-CsCs_Cds-COOs
                        L7: Cds-CsCs_Cds-CdOs
                        L7: Cds-CsCs_Cds-C=SOs
                    L6: Cds-CsCs_Cds-OneDeSs
                        L7: Cds-CsCs_Cds-CtSs
                        L7: Cds-CsCs_Cds-CbSs
                        L7: Cds-CsCs_Cds-COSs
                        L7: Cds-CsCs_Cds-CdSs
                        L7: Cds-CsCs_Cds-C=SSs
                    L6: Cds-CsCs_Cds-OneDeH
                        L7: Cds-CsCs_Cds-CtH
                        L7: Cds-CsCs_Cds-CbH
                        L7: Cds-CsCs_Cds-COH
                        L7: Cds-CsCs_Cds-CdH
                        L7: Cds-CsCs_Cds-C=SH
                L5: Cds-CsCs_Cds-TwoDe
                    L6: Cds-CsCs_Cds-CtCt
                    L6: Cds-CsCs_Cds-CtCb
                    L6: Cds-CsCs_Cds-CtCO
                    L6: Cds-CsCs_Cds-CbCb
                    L6: Cds-CsCs_Cds-CbCO
                    L6: Cds-CsCs_Cds-COCO
                    L6: Cds-CsCs_Cds-CdCt
                    L6: Cds-CsCs_Cds-CdCb
                    L6: Cds-CsCs_Cds-CdCO
                    L6: Cds-CsCs_Cds-CtC=S
                    L6: Cds-CsCs_Cds-CbC=S
                    L6: Cds-CsCs_Cds-COC=S
                    L6: Cds-CsCs_Cds-(Cd-Cd-Cd)Cd
                    L6: Cds-CsCs_Cds-CdCd
                    L6: Cds-CsCs_Cds-CdC=S
                    L6: Cds-CsCs_Cds-C=SC=S
                L5: Cds-CsCs_Cds-CtH-Br
                L5: Cds-CsCs_Cds-CbH-Br
                L5: Cds-CsCs_Cds-COH-Br
                L5: Cds-CsCs_Cds-CdH-Br
                L5: Cds-CsCs_Cds-C=SH-Br
                L5: Cds-CsCs_Cds-CtH-F
                L5: Cds-CsCs_Cds-CbH-F
                L5: Cds-CsCs_Cds-COH-F
                L5: Cds-CsCs_Cds-CdH-F
                L5: Cds-CsCs_Cds-C=SH-F
                L5: Cds-CsCs_Cds-CtH-Cl
                L5: Cds-CsCs_Cds-CbH-Cl
                L5: Cds-CsCs_Cds-COH-Cl
                L5: Cds-CsCs_Cds-CdH-Cl
                L5: Cds-CsCs_Cds-C=SH-Cl
                L5: Cds-CsCs_Cds-SsH
                L5: Cds-CsCs_Cds-SsH-F
                L5: Cds-CsCs_Cds-SsH-Cl
                L5: Cds-CsCs_Cds-SsH-Br
                L5: Cds-CsCs_Cds-CsH
                L5: Cds-CsCs_Cds-CsH-F
                L5: Cds-CsCs_Cds-CsH-Cl
                L5: Cds-CsCs_Cds-CsH-Br
                L5: Cds-CsCs_Cds-OsH
                L5: Cds-CsCs_Cds-OsH-F
                L5: Cds-CsCs_Cds-OsH-Cl
                L5: Cds-CsCs_Cds-OsH-Br
                L5: Cds-CsCs_Cds-HH
                L5: Cds-CsCs_Cds-HH-HF
                L5: Cds-CsCs_Cds-HH-HCl
                L5: Cds-CsCs_Cds-HH-HBr
                L5: Cds-CsCs_Cds-HH-FF
                L5: Cds-CsCs_Cds-HH-FCl
                L5: Cds-CsCs_Cds-HH-FBr
                L5: Cds-CsCs_Cds-HH-ClCl
                L5: Cds-CsCs_Cds-HH-ClBr
                L5: Cds-CsCs_Cds-HH-BrBr
            L4: Cds-Ss/H_or_Val7/Cds
                L5: Cds-SsH_Cds
                L5: Cds-SsH_Cds-F
                L5: Cds-SsH_Cds-Cl
                L5: Cds-SsH_Cds-Br
            L4: Cds-SsCs_Cds
            L4: Cds-SsSs_Cds
            L4: Cds-N3s/H_or_Val7/Cds
                L5: Cds-N3sH_Cds
                L5: Cds-N3sH_Cds-F
                L5: Cds-N3sH_Cds-Cl
                L5: Cds-N3sH_Cds-Br
            L4: Cds-Os/H_or_Val7/Cds
                L5: Cds-OsH_Cds
                    L6: Cds-OsH_Cds-CsH
                    L6: Cds-OsH_Cds-CsH-HF
                    L6: Cds-OsH_Cds-CsH-HCl
                    L6: Cds-OsH_Cds-CsH-HBr
                L5: Cds-OsH_Cds-F
                    L6: Cds-OsH_Cds-CsH-FF
                    L6: Cds-OsH_Cds-CsH-FCl
                    L6: Cds-OsH_Cds-CsH-FBr
                L5: Cds-OsH_Cds-Cl
                    L6: Cds-OsH_Cds-CsH-ClCl
                    L6: Cds-OsH_Cds-CsH-ClBr
                L5: Cds-OsH_Cds-Br
                    L6: Cds-OsH_Cds-CsH-BrBr
            L4: Cds-OsCs_Cds
            L4: Cds-OsOs_Cds
            L4: Cds-OsSs_Cds
            L4: Cds-OneDe_Cds
                L5: Cds-OneDeCs_Cds
                    L6: Cds-CtCs_Cds
                        L7: Cds-CtCs_Cds-CsCs
                        L7: Cds-CtCs_Cds-OsCs
                        L7: Cds-CtCs_Cds-OsOs
                        L7: Cds-CtCs_Cds-SsCs
                        L7: Cds-CtCs_Cds-SsOs
                        L7: Cds-CtCs_Cds-SsSs
                        L7: Cds-CtCs_Cds-OneDe
                            L8: Cds-CtCs_Cds-OneDeCs
                                L9: Cds-CtCs_Cds-CtCs
                                L9: Cds-CtCs_Cds-CbCs
                                L9: Cds-CtCs_Cds-COCs
                                L9: Cds-CtCs_Cds-CdCs
                                L9: Cds-CtCs_Cds-C=SCs
                            L8: Cds-CtCs_Cds-OneDeOs
                                L9: Cds-CtCs_Cds-CtOs
                                L9: Cds-CtCs_Cds-CbOs
                                L9: Cds-CtCs_Cds-COOs
                                L9: Cds-CtCs_Cds-CdOs
                                L9: Cds-CtCs_Cds-C=SOs
                            L8: Cds-CtCs_Cds-OneDeSs
                                L9: Cds-CtCs_Cds-CtSs
                                L9: Cds-CtCs_Cds-CbSs
                                L9: Cds-CtCs_Cds-COSs
                                L9: Cds-CtCs_Cds-CdSs
                                L9: Cds-CtCs_Cds-C=SSs
                            L8: Cds-CtCs_Cds-OneDeH
                                L9: Cds-CtCs_Cds-CtH
                                L9: Cds-CtCs_Cds-CbH
                                L9: Cds-CtCs_Cds-COH
                                L9: Cds-CtCs_Cds-CdH
                                L9: Cds-CtCs_Cds-C=SH
                        L7: Cds-CtCs_Cds-TwoDe
                            L8: Cds-CtCs_Cds-CtCt
                            L8: Cds-CtCs_Cds-CtCb
                            L8: Cds-CtCs_Cds-CtCO
                            L8: Cds-CtCs_Cds-CbCb
                            L8: Cds-CtCs_Cds-CbCO
                            L8: Cds-CtCs_Cds-COCO
                            L8: Cds-CtCs_Cds-CdCt
                            L8: Cds-CtCs_Cds-CdCb
                            L8: Cds-CtCs_Cds-CdCO
                            L8: Cds-CtCs_Cds-CtC=S
                            L8: Cds-CtCs_Cds-CbC=S
                            L8: Cds-CtCs_Cds-COC=S
                            L8: Cds-CtCs_Cds-CdCd
                            L8: Cds-CtCs_Cds-CdC=S
                            L8: Cds-CtCs_Cds-C=SC=S
                        L7: Cds-CtCs_Cds-SsH
                        L7: Cds-CtCs_Cds-SsH-F
                        L7: Cds-CtCs_Cds-SsH-Cl
                        L7: Cds-CtCs_Cds-SsH-Br
                        L7: Cds-CtCs_Cds-CtH-F
                        L7: Cds-CtCs_Cds-CbH-F
                        L7: Cds-CtCs_Cds-COH-F
                        L7: Cds-CtCs_Cds-CdH-F
                        L7: Cds-CtCs_Cds-C=SH-F
                        L7: Cds-CtCs_Cds-CtH-Cl
                        L7: Cds-CtCs_Cds-CbH-Cl
                        L7: Cds-CtCs_Cds-COH-Cl
                        L7: Cds-CtCs_Cds-CdH-Cl
                        L7: Cds-CtCs_Cds-C=SH-Cl
                        L7: Cds-CtCs_Cds-CtH-Br
                        L7: Cds-CtCs_Cds-CbH-Br
                        L7: Cds-CtCs_Cds-COH-Br
                        L7: Cds-CtCs_Cds-CdH-Br
                        L7: Cds-CtCs_Cds-C=SH-Br
                        L7: Cds-CtCs_Cds-HH
                        L7: Cds-CtCs_Cds-HH-HF
                        L7: Cds-CtCs_Cds-HH-HCl
                        L7: Cds-CtCs_Cds-HH-HBr
                        L7: Cds-CtCs_Cds-HH-FF
                        L7: Cds-CtCs_Cds-HH-FCl
                        L7: Cds-CtCs_Cds-HH-FBr
                        L7: Cds-CtCs_Cds-HH-ClCl
                        L7: Cds-CtCs_Cds-HH-ClBr
                        L7: Cds-CtCs_Cds-HH-BrBr
                        L7: Cds-CtCs_Cds-CsH
                        L7: Cds-CtCs_Cds-CsH-F
                        L7: Cds-CtCs_Cds-CsH-Cl
                        L7: Cds-CtCs_Cds-CsH-Br
                        L7: Cds-CtCs_Cds-OsH
                        L7: Cds-CtCs_Cds-OsH-F
                        L7: Cds-CtCs_Cds-OsH-Cl
                        L7: Cds-CtCs_Cds-OsH-Br
                    L6: Cds-CbCs_Cds
                        L7: Cds-CbCs_Cds-CsCs
                        L7: Cds-CbCs_Cds-OsCs
                        L7: Cds-CbCs_Cds-OsOs
                        L7: Cds-CbCs_Cds-SsCs
                        L7: Cds-CbCs_Cds-SsOs
                        L7: Cds-CbCs_Cds-SsSs
                        L7: Cds-CbCs_Cds-OneDe
                            L8: Cds-CbCs_Cds-OneDeCs
                                L9: Cds-CbCs_Cds-CtCs
                                L9: Cds-CbCs_Cds-CbCs
                                L9: Cds-CbCs_Cds-COCs
                                L9: Cds-CbCs_Cds-CdCs
                                L9: Cds-CbCs_Cds-C=SCs
                            L8: Cds-CbCs_Cds-OneDeOs
                                L9: Cds-CbCs_Cds-CtOs
                                L9: Cds-CbCs_Cds-CbOs
                                L9: Cds-CbCs_Cds-COOs
                                L9: Cds-CbCs_Cds-CdOs
                                L9: Cds-CbCs_Cds-C=SOs
                            L8: Cds-CbCs_Cds-OneDeSs
                                L9: Cds-CbCs_Cds-CtSs
                                L9: Cds-CbCs_Cds-CbSs
                                L9: Cds-CbCs_Cds-COSs
                                L9: Cds-CbCs_Cds-CdSs
                                L9: Cds-CbCs_Cds-C=SSs
                            L8: Cds-CbCs_Cds-OneDeH
                                L9: Cds-CbCs_Cds-CtH
                                L9: Cds-CbCs_Cds-CbH
                                L9: Cds-CbCs_Cds-COH
                                L9: Cds-CbCs_Cds-CdH
                                L9: Cds-CbCs_Cds-C=SH
                        L7: Cds-CbCs_Cds-TwoDe
                            L8: Cds-CbCs_Cds-CtCt
                            L8: Cds-CbCs_Cds-CtCb
                            L8: Cds-CbCs_Cds-CtCO
                            L8: Cds-CbCs_Cds-CbCb
                            L8: Cds-CbCs_Cds-CbCO
                            L8: Cds-CbCs_Cds-COCO
                            L8: Cds-CbCs_Cds-CdCt
                            L8: Cds-CbCs_Cds-CdCb
                            L8: Cds-CbCs_Cds-CdCO
                            L8: Cds-CbCs_Cds-CtC=S
                            L8: Cds-CbCs_Cds-CbC=S
                            L8: Cds-CbCs_Cds-COC=S
                            L8: Cds-CbCs_Cds-CdCd
                            L8: Cds-CbCs_Cds-CdC=S
                            L8: Cds-CbCs_Cds-C=SC=S
                        L7: Cds-CbCs_Cds-CtH-F
                        L7: Cds-CbCs_Cds-CbH-F
                        L7: Cds-CbCs_Cds-COH-F
                        L7: Cds-CbCs_Cds-CdH-F
                        L7: Cds-CbCs_Cds-C=SH-F
                        L7: Cds-CbCs_Cds-CtH-Cl
                        L7: Cds-CbCs_Cds-CbH-Cl
                        L7: Cds-CbCs_Cds-COH-Cl
                        L7: Cds-CbCs_Cds-CdH-Cl
                        L7: Cds-CbCs_Cds-C=SH-Cl
                        L7: Cds-CbCs_Cds-CtH-Br
                        L7: Cds-CbCs_Cds-CbH-Br
                        L7: Cds-CbCs_Cds-COH-Br
                        L7: Cds-CbCs_Cds-CdH-Br
                        L7: Cds-CbCs_Cds-C=SH-Br
                        L7: Cds-CbCs_Cds-CsH
                        L7: Cds-CbCs_Cds-CsH-F
                        L7: Cds-CbCs_Cds-CsH-Cl
                        L7: Cds-CbCs_Cds-CsH-Br
                        L7: Cds-CbCs_Cds-OsH
                        L7: Cds-CbCs_Cds-OsH-F
                        L7: Cds-CbCs_Cds-OsH-Cl
                        L7: Cds-CbCs_Cds-OsH-Br
                        L7: Cds-CbCs_Cds-SsH
                        L7: Cds-CbCs_Cds-SsH-F
                        L7: Cds-CbCs_Cds-SsH-Cl
                        L7: Cds-CbCs_Cds-SsH-Br
                        L7: Cds-CbCs_Cds-HH
                        L7: Cds-CbCs_Cds-HH-HF
                        L7: Cds-CbCs_Cds-HH-HCl
                        L7: Cds-CbCs_Cds-HH-HBr
                        L7: Cds-CbCs_Cds-HH-FF
                        L7: Cds-CbCs_Cds-HH-FCl
                        L7: Cds-CbCs_Cds-HH-FBr
                        L7: Cds-CbCs_Cds-HH-ClCl
                        L7: Cds-CbCs_Cds-HH-ClBr
                        L7: Cds-CbCs_Cds-HH-BrBr
                    L6: Cds-COCs_Cds
                    L6: Cds-CdCs_Cds
                        L7: Cds-CdCs_Cds-CsCs
                        L7: Cds-CdCs_Cds-OsCs
                        L7: Cds-CdCs_Cds-OsOs
                        L7: Cds-CdCs_Cds-SsCs
                        L7: Cds-CdCs_Cds-SsOs
                        L7: Cds-CdCs_Cds-SsSs
                        L7: Cds-CdCs_Cds-OneDe
                            L8: Cds-CdCs_Cds-OneDe/H_or_Val7/
                                L9: Cds-CdCs_Cds-OneDeH
                                    L10: Cds-CdCs_Cds-CtH
                                    L10: Cds-CdCs_Cds-CbH
                                    L10: Cds-CdCs_Cds-COH
                                    L10: Cds-CdCs_Cds-(Cd-Cd-Cd)H
                                    L10: Cds-CdCs_Cds-CdH
                                    L10: Cds-CdCs_Cds-C=SH
                                L9: Cds-CdCs_Cds-OneDeH-F
                                    L10: Cds-CdCs_Cds-CtH-F
                                    L10: Cds-CdCs_Cds-CbH-F
                                    L10: Cds-CdCs_Cds-COH-F
                                    L10: Cds-CdCs_Cds-(Cd-Cd-Cd)H-F
                                    L10: Cds-CdCs_Cds-CdH-F
                                    L10: Cds-CdCs_Cds-C=SH-F
                                L9: Cds-CdCs_Cds-OneDeH-Cl
                                    L10: Cds-CdCs_Cds-CtH-Cl
                                    L10: Cds-CdCs_Cds-CbH-Cl
                                    L10: Cds-CdCs_Cds-COH-Cl
                                    L10: Cds-CdCs_Cds-(Cd-Cd-Cd)H-Cl
                                    L10: Cds-CdCs_Cds-CdH-Cl
                                    L10: Cds-CdCs_Cds-C=SH-Cl
                                L9: Cds-CdCs_Cds-OneDeH-Br
                                    L10: Cds-CdCs_Cds-CtH-Br
                                    L10: Cds-CdCs_Cds-CbH-Br
                                    L10: Cds-CdCs_Cds-COH-Br
                                    L10: Cds-CdCs_Cds-(Cd-Cd-Cd)H-Br
                                    L10: Cds-CdCs_Cds-CdH-Br
                                    L10: Cds-CdCs_Cds-C=SH-Br
                            L8: Cds-CdCs_Cds-OneDeCs
                                L9: Cds-CdCs_Cds-CtCs
                                L9: Cds-CdCs_Cds-CbCs
                                L9: Cds-CdCs_Cds-COCs
                                L9: Cds-CdCs_Cds-CdCs
                                L9: Cds-CdCs_Cds-C=SCs
                            L8: Cds-CdCs_Cds-OneDeOs
                                L9: Cds-CdCs_Cds-CtOs
                                L9: Cds-CdCs_Cds-CbOs
                                L9: Cds-CdCs_Cds-COOs
                                L9: Cds-CdCs_Cds-CdOs
                                L9: Cds-CdCs_Cds-C=SOs
                            L8: Cds-CdCs_Cds-OneDeSs
                                L9: Cds-CdCs_Cds-CtSs
                                L9: Cds-CdCs_Cds-CbSs
                                L9: Cds-CdCs_Cds-COSs
                                L9: Cds-CdCs_Cds-CdSs
                                L9: Cds-CdCs_Cds-C=SSs
                            L8: Cds-CdCs_Cds-TwoDe
                                L9: Cds-CdCs_Cds-CtCt
                                L9: Cds-CdCs_Cds-CtCb
                                L9: Cds-CdCs_Cds-CtCO
                                L9: Cds-CdCs_Cds-CbCb
                                L9: Cds-CdCs_Cds-CbCO
                                L9: Cds-CdCs_Cds-COCO
                                L9: Cds-CdCs_Cds-CdCt
                                L9: Cds-CdCs_Cds-CdCb
                                L9: Cds-CdCs_Cds-CdCO
                                L9: Cds-CdCs_Cds-CtC=S
                                L9: Cds-CdCs_Cds-CbC=S
                                L9: Cds-CdCs_Cds-COC=S
                                L9: Cds-CdCs_Cds-CdCd
                                L9: Cds-CdCs_Cds-CdC=S
                                L9: Cds-CdCs_Cds-C=SC=S
                        L7: Cds-CdCs_Cds-CsH
                        L7: Cds-CdCs_Cds-CsH-F
                        L7: Cds-CdCs_Cds-CsH-Cl
                        L7: Cds-CdCs_Cds-CsH-Br
                        L7: Cds-CdCs_Cds-OsH
                        L7: Cds-CdCs_Cds-OsH-F
                        L7: Cds-CdCs_Cds-OsH-Cl
                        L7: Cds-CdCs_Cds-OsH-Br
                        L7: Cds-CdCs_Cds-SsH
                        L7: Cds-CdCs_Cds-SsH-F
                        L7: Cds-CdCs_Cds-SsH-Cl
                        L7: Cds-CdCs_Cds-SsH-Br
                        L7: Cds-CdCs_Cds-HH
                        L7: Cds-CdCs_Cds-HH-HF
                        L7: Cds-CdCs_Cds-HH-HCl
                        L7: Cds-CdCs_Cds-HH-HBr
                        L7: Cds-CdCs_Cds-HH-FF
                        L7: Cds-CdCs_Cds-HH-FCl
                        L7: Cds-CdCs_Cds-HH-FBr
                        L7: Cds-CdCs_Cds-HH-ClCl
                        L7: Cds-CdCs_Cds-HH-ClBr
                        L7: Cds-CdCs_Cds-HH-BrBr
                    L6: Cds-C=SCs_Cds
                L5: Cds-OneDeSs_Cds
                    L6: Cds-CtSs_Cds
                    L6: Cds-CbSs_Cds
                    L6: Cds-COSs_Cds
                    L6: Cds-CdSs_Cds
                    L6: Cds-C=SSs_Cds
                L5: Cds-OneDeOs_Cds
                    L6: Cds-CtOs_Cds
                    L6: Cds-CbOs_Cds
                    L6: Cds-COOs_Cds
                    L6: Cds-CdOs_Cds
                    L6: Cds-C=SOs_Cds
                L5: Cds-OneDeH_Cds
                    L6: Cds-CtH_Cds
                        L7: Cds-CtH_Cds-HH
                        L7: Cds-CtH_Cds-CsH
                        L7: Cds-CtH_Cds-CsCs
                        L7: Cds-CtH_Cds-OsH
                        L7: Cds-CtH_Cds-OsCs
                        L7: Cds-CtH_Cds-OsOs
                        L7: Cds-CtH_Cds-SsH
                        L7: Cds-CtH_Cds-SsCs
                        L7: Cds-CtH_Cds-SsOs
                        L7: Cds-CtH_Cds-SsSs
                        L7: Cds-CtH_Cds-OneDe
                            L8: Cds-CtH_Cds-OneDeH
                                L9: Cds-CtH_Cds-CtH
                                L9: Cds-CtH_Cds-CbH
                                L9: Cds-CtH_Cds-COH
                                L9: Cds-CtH_Cds-CdH
                                L9: Cds-CtH_Cds-C=SH
                            L8: Cds-CtH_Cds-OneDeCs
                                L9: Cds-CtH_Cds-CtCs
                                L9: Cds-CtH_Cds-CbCs
                                L9: Cds-CtH_Cds-COCs
                                L9: Cds-CtH_Cds-CdCs
                                L9: Cds-CtH_Cds-C=SCs
                            L8: Cds-CtH_Cds-OneDeOs
                                L9: Cds-CtH_Cds-CtOs
                                L9: Cds-CtH_Cds-CbOs
                                L9: Cds-CtH_Cds-COOs
                                L9: Cds-CtH_Cds-CdOs
                                L9: Cds-CtH_Cds-C=SOs
                            L8: Cds-CtH_Cds-OneDeSs
                                L9: Cds-CtH_Cds-CtSs
                                L9: Cds-CtH_Cds-CbSs
                                L9: Cds-CtH_Cds-COSs
                                L9: Cds-CtH_Cds-CdSs
                                L9: Cds-CtH_Cds-C=SSs
                        L7: Cds-CtH_Cds-TwoDe
                            L8: Cds-CtH_Cds-CtCt
                            L8: Cds-CtH_Cds-CtCb
                            L8: Cds-CtH_Cds-CtCO
                            L8: Cds-CtH_Cds-CbCb
                            L8: Cds-CtH_Cds-CbCO
                            L8: Cds-CtH_Cds-COCO
                            L8: Cds-CtH_Cds-CdCt
                            L8: Cds-CtH_Cds-CdCb
                            L8: Cds-CtH_Cds-CdCO
                            L8: Cds-CtH_Cds-CtC=S
                            L8: Cds-CtH_Cds-CbC=S
                            L8: Cds-CtH_Cds-COC=S
                            L8: Cds-CtH_Cds-CdCd
                            L8: Cds-CtH_Cds-CdC=S
                            L8: Cds-CtH_Cds-C=SC=S
                        L7: Cds-CtH_Cds-CtH-HF
                        L7: Cds-CtH_Cds-CbH-HF
                        L7: Cds-CtH_Cds-COH-HF
                        L7: Cds-CtH_Cds-C=SH-HF
                        L7: Cds-CtH_Cds-CtH-HBr
                        L7: Cds-CtH_Cds-CbH-HBr
                        L7: Cds-CtH_Cds-COH-HBr
                        L7: Cds-CtH_Cds-C=SH-HBr
                        L7: Cds-CtH_Cds-CtH-HCl
                        L7: Cds-CtH_Cds-CbH-HCl
                        L7: Cds-CtH_Cds-COH-HCl
                        L7: Cds-CtH_Cds-C=SH-HCl
                    L6: Cds-CbH_Cds
                        L7: Cds-CbH_Cds-HH
                        L7: Cds-CbH_Cds-CsH
                        L7: Cds-CbH_Cds-CsCs
                        L7: Cds-CbH_Cds-OsH
                        L7: Cds-CbH_Cds-OsCs
                        L7: Cds-CbH_Cds-OsOs
                        L7: Cds-CbH_Cds-SsH
                        L7: Cds-CbH_Cds-SsCs
                        L7: Cds-CbH_Cds-SsOs
                        L7: Cds-CbH_Cds-SsSs
                        L7: Cds-CbH_Cds-OneDe
                            L8: Cds-CbH_Cds-OneDeH
                                L9: Cds-CbH_Cds-CtH
                                L9: Cds-CbH_Cds-CbH
                                L9: Cds-CbH_Cds-COH
                                L9: Cds-CbH_Cds-CdH
                                    L10: Cds-CbH_Cds-Cd(CdCb)H
                                L9: Cds-CbH_Cds-C=SH
                            L8: Cds-CbH_Cds-OneDeCs
                                L9: Cds-CbH_Cds-CtCs
                                L9: Cds-CbH_Cds-CbCs
                                L9: Cds-CbH_Cds-COCs
                                L9: Cds-CbH_Cds-CdCs
                                L9: Cds-CbH_Cds-C=SCs
                            L8: Cds-CbH_Cds-OneDeOs
                                L9: Cds-CbH_Cds-CtOs
                                L9: Cds-CbH_Cds-CbOs
                                L9: Cds-CbH_Cds-COOs
                                L9: Cds-CbH_Cds-CdOs
                                L9: Cds-CbH_Cds-C=SOs
                            L8: Cds-CbH_Cds-OneDeSs
                                L9: Cds-CbH_Cds-CtSs
                                L9: Cds-CbH_Cds-CbSs
                                L9: Cds-CbH_Cds-COSs
                                L9: Cds-CbH_Cds-CdSs
                                L9: Cds-CbH_Cds-C=SSs
                        L7: Cds-CbH_Cds-TwoDe
                            L8: Cds-CbH_Cds-CtCt
                            L8: Cds-CbH_Cds-CtCb
                            L8: Cds-CbH_Cds-CtCO
                            L8: Cds-CbH_Cds-CbCb
                            L8: Cds-CbH_Cds-CbCO
                            L8: Cds-CbH_Cds-COCO
                            L8: Cds-CbH_Cds-CdCt
                            L8: Cds-CbH_Cds-CdCb
                            L8: Cds-CbH_Cds-CdCO
                            L8: Cds-CbH_Cds-CtC=S
                            L8: Cds-CbH_Cds-CbC=S
                            L8: Cds-CbH_Cds-COC=S
                            L8: Cds-CbH_Cds-CdCd
                            L8: Cds-CbH_Cds-CdC=S
                            L8: Cds-CbH_Cds-C=SC=S
                        L7: Cds-CbH_Cds-CtH-HCl
                        L7: Cds-CbH_Cds-CbH-HCl
                        L7: Cds-CbH_Cds-COH-HCl
                        L7: Cds-CbH_Cds-C=SH-HCl
                        L7: Cds-CbH_Cds-CtH-HBr
                        L7: Cds-CbH_Cds-CbH-HBr
                        L7: Cds-CbH_Cds-COH-HBr
                        L7: Cds-CbH_Cds-C=SH-HBr
                        L7: Cds-CbH_Cds-CtH-HF
                        L7: Cds-CbH_Cds-CbH-HF
                        L7: Cds-CbH_Cds-COH-HF
                        L7: Cds-CbH_Cds-C=SH-HF
                    L6: Cds-COH_Cds
                    L6: Cds-CdH_Cds
                        L7: Cds-CdH_Cds-HH
                        L7: Cds-CdH_Cds-CsH
                            L8: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6
                            L8: Cds-CdH_Cds-(CsH-Cds)_cyc5
                        L7: Cds-CdH_Cds-CsCs
                        L7: Cds-CdH_Cds-OsH
                        L7: Cds-CdH_Cds-OsCs
                        L7: Cds-CdH_Cds-OsOs
                        L7: Cds-CdH_Cds-SsH
                        L7: Cds-CdH_Cds-SsCs
                        L7: Cds-CdH_Cds-SsOs
                        L7: Cds-CdH_Cds-SsSs
                        L7: Cds-CdH_Cds-OneDe
                            L8: Cds-CdH_Cds-OneDeH
                                L9: Cds-CdH_Cds-CtH
                                L9: Cds-CdH_Cds-CbH
                                    L10: Cds(CdCb)-CdH_Cds-CbH_cycle
                                    L10: Cds-CdH_Cds-Cb(Cb)H_cycle
                                L9: Cds-CdH_Cds-COH
                                L9: Cds-CdH_Cds-CdH
                                    L10: Cds-CdH_Cds-CdH_cyc5_1
                                    L10: Cds-CdH_Cds-CdH_cyc5_2
                                L9: Cds-CdH_Cds-C=SH
                            L8: Cds-CdH_Cds-OneDeH-HF
                                L9: Cds-CdH_Cds-CtH-HF
                                L9: Cds-CdH_Cds-CbH-HF
                                    L10: Cds(CdCb)-CdH_Cds-CbH_cycle-HF
                                    L10: Cds-CdH_Cds-Cb(Cb)H_cycle-HF
                                L9: Cds-CdH_Cds-COH-HF
                                L9: Cds-CdH_Cds-CdH-HF
                                    L10: Cds-CdH_Cds-CdH_cyc5_2-HF
                                L9: Cds-CdH_Cds-C=SH-HF
                            L8: Cds-CdH_Cds-OneDeH-HCl
                                L9: Cds-CdH_Cds-CtH-HCl
                                L9: Cds-CdH_Cds-CbH-HCl
                                    L10: Cds(CdCb)-CdH_Cds-CbH_cycle-HCl
                                    L10: Cds-CdH_Cds-Cb(Cb)H_cycle-HCl
                                L9: Cds-CdH_Cds-COH-HCl
                                L9: Cds-CdH_Cds-CdH-HCl
                                    L10: Cds-CdH_Cds-CdH_cyc5_2-HCl
                                L9: Cds-CdH_Cds-C=SH-HCl
                            L8: Cds-CdH_Cds-OneDeH-HBr
                                L9: Cds-CdH_Cds-CtH-HBr
                                L9: Cds-CdH_Cds-CbH-HBr
                                    L10: Cds(CdCb)-CdH_Cds-CbH_cycle-HBr
                                    L10: Cds-CdH_Cds-Cb(Cb)H_cycle-HBr
                                L9: Cds-CdH_Cds-COH-HBr
                                L9: Cds-CdH_Cds-CdH-HBr
                                    L10: Cds-CdH_Cds-CdH_cyc5_2-HBr
                                L9: Cds-CdH_Cds-C=SH-HBr
                            L8: Cds-CdH_Cds-OneDeCs
                                L9: Cds-CdH_Cds-CtCs
                                L9: Cds-CdH_Cds-CbCs
                                L9: Cds-CdH_Cds-COCs
                                L9: Cds-CdH_Cds-CdCs
                                L9: Cds-CdH_Cds-C=SCs
                            L8: Cds-CdH_Cds-OneDeOs
                                L9: Cds-CdH_Cds-CtOs
                                L9: Cds-CdH_Cds-CbOs
                                L9: Cds-CdH_Cds-COOs
                                L9: Cds-CdH_Cds-CdOs
                                L9: Cds-CdH_Cds-C=SOs
                            L8: Cds-CdH_Cds-OneDeSs
                                L9: Cds-CdH_Cds-CtSs
                                L9: Cds-CdH_Cds-CbSs
                                L9: Cds-CdH_Cds-COSs
                                L9: Cds-CdH_Cds-CdSs
                                L9: Cds-CdH_Cds-C=SSs
                            L8: Cds-CdH_Cds-TwoDe
                                L9: Cds-CdH_Cds-CtCt
                                L9: Cds-CdH_Cds-CtCb
                                L9: Cds-CdH_Cds-CtCO
                                L9: Cds-CdH_Cds-CbCb
                                L9: Cds-CdH_Cds-CbCO
                                L9: Cds-CdH_Cds-COCO
                                L9: Cds-CdH_Cds-CdCt
                                L9: Cds-CdH_Cds-CdCb
                                L9: Cds-CdH_Cds-CdCO
                                L9: Cds-CdH_Cds-CtC=S
                                L9: Cds-CdH_Cds-CbC=S
                                L9: Cds-CdH_Cds-COC=S
                                L9: Cds-CdH_Cds-CdCd
                                    L10: Cds-CdH_Cds-CdCd_cyc6
                                        L11: Cds-CdH_Cds-CdCd_cyc6_cyc5
                                L9: Cds-CdH_Cds-CdC=S
                                L9: Cds-CdH_Cds-C=SC=S
                        L7: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-HF
                        L7: Cds-CdH_Cds-(CsH-Cds)_cyc5-HF
                        L7: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-HCl
                        L7: Cds-CdH_Cds-(CsH-Cds)_cyc5-HCl
                        L7: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-HBr
                        L7: Cds-CdH_Cds-(CsH-Cds)_cyc5-HBr
                    L6: Cds-C=SH_Cds
            L4: Cds-TwoDe_Cds
                L5: Cds-CtCt_Cds
                    L6: Cds-CtCt_Cds-CsCs
                    L6: Cds-CtCt_Cds-OsCs
                    L6: Cds-CtCt_Cds-OsOs
                    L6: Cds-CtCt_Cds-SsCs
                    L6: Cds-CtCt_Cds-SsOs
                    L6: Cds-CtCt_Cds-SsSs
                    L6: Cds-CtCt_Cds-OneDe
                        L7: Cds-CtCt_Cds-OneDeCs
                            L8: Cds-CtCt_Cds-CtCs
                            L8: Cds-CtCt_Cds-CbCs
                            L8: Cds-CtCt_Cds-COCs
                            L8: Cds-CtCt_Cds-CdCs
                            L8: Cds-CtCt_Cds-C=SCs
                        L7: Cds-CtCt_Cds-OneDeOs
                            L8: Cds-CtCt_Cds-CtOs
                            L8: Cds-CtCt_Cds-CbOs
                            L8: Cds-CtCt_Cds-COOs
                            L8: Cds-CtCt_Cds-CdOs
                            L8: Cds-CtCt_Cds-C=SOs
                        L7: Cds-CtCt_Cds-OneDeSs
                            L8: Cds-CtCt_Cds-CtSs
                            L8: Cds-CtCt_Cds-CbSs
                            L8: Cds-CtCt_Cds-COSs
                            L8: Cds-CtCt_Cds-CdSs
                            L8: Cds-CtCt_Cds-C=SSs
                        L7: Cds-CtCt_Cds-OneDeH
                            L8: Cds-CtCt_Cds-CtH
                            L8: Cds-CtCt_Cds-CbH
                            L8: Cds-CtCt_Cds-COH
                            L8: Cds-CtCt_Cds-CdH
                            L8: Cds-CtCt_Cds-C=SH
                    L6: Cds-CtCt_Cds-TwoDe
                        L7: Cds-CtCt_Cds-CtCt
                        L7: Cds-CtCt_Cds-CtCb
                        L7: Cds-CtCt_Cds-CtCO
                        L7: Cds-CtCt_Cds-CbCb
                        L7: Cds-CtCt_Cds-CbCO
                        L7: Cds-CtCt_Cds-COCO
                        L7: Cds-CtCt_Cds-CdCt
                        L7: Cds-CtCt_Cds-CdCb
                        L7: Cds-CtCt_Cds-CdCO
                        L7: Cds-CtCt_Cds-CtC=S
                        L7: Cds-CtCt_Cds-CbC=S
                        L7: Cds-CtCt_Cds-COC=S
                        L7: Cds-CtCt_Cds-CdCd
                        L7: Cds-CtCt_Cds-CdC=S
                        L7: Cds-CtCt_Cds-C=SC=S
                    L6: Cds-CtCt_Cds-HH
                    L6: Cds-CtCt_Cds-HH-HF
                    L6: Cds-CtCt_Cds-HH-HCl
                    L6: Cds-CtCt_Cds-HH-HBr
                    L6: Cds-CtCt_Cds-HH-FF
                    L6: Cds-CtCt_Cds-HH-FCl
                    L6: Cds-CtCt_Cds-HH-FBr
                    L6: Cds-CtCt_Cds-HH-ClCl
                    L6: Cds-CtCt_Cds-HH-ClBr
                    L6: Cds-CtCt_Cds-HH-BrBr
                    L6: Cds-CtCt_Cds-CtH-Cl
                    L6: Cds-CtCt_Cds-CbH-Cl
                    L6: Cds-CtCt_Cds-COH-Cl
                    L6: Cds-CtCt_Cds-CdH-Cl
                    L6: Cds-CtCt_Cds-C=SH-Cl
                    L6: Cds-CtCt_Cds-CtH-Br
                    L6: Cds-CtCt_Cds-CbH-Br
                    L6: Cds-CtCt_Cds-COH-Br
                    L6: Cds-CtCt_Cds-CdH-Br
                    L6: Cds-CtCt_Cds-C=SH-Br
                    L6: Cds-CtCt_Cds-CsH
                    L6: Cds-CtCt_Cds-CsH-F
                    L6: Cds-CtCt_Cds-CsH-Cl
                    L6: Cds-CtCt_Cds-CsH-Br
                    L6: Cds-CtCt_Cds-OsH
                    L6: Cds-CtCt_Cds-OsH-F
                    L6: Cds-CtCt_Cds-OsH-Cl
                    L6: Cds-CtCt_Cds-OsH-Br
                    L6: Cds-CtCt_Cds-SsH
                    L6: Cds-CtCt_Cds-SsH-F
                    L6: Cds-CtCt_Cds-SsH-Cl
                    L6: Cds-CtCt_Cds-SsH-Br
                    L6: Cds-CtCt_Cds-CtH-F
                    L6: Cds-CtCt_Cds-CbH-F
                    L6: Cds-CtCt_Cds-COH-F
                    L6: Cds-CtCt_Cds-CdH-F
                    L6: Cds-CtCt_Cds-C=SH-F
                L5: Cds-CtCb_Cds
                L5: Cds-CtCO_Cds
                L5: Cds-CbCb_Cds
                L5: Cds-CbCO_Cds
                L5: Cds-COCO_Cds
                L5: Cds-CdCt_Cds
                    L6: Cds-CdCt_Cds-CsCs
                    L6: Cds-CdCt_Cds-OsCs
                    L6: Cds-CdCt_Cds-OsOs
                    L6: Cds-CdCt_Cds-SsCs
                    L6: Cds-CdCt_Cds-SsOs
                    L6: Cds-CdCt_Cds-SsSs
                    L6: Cds-CdCt_Cds-OneDe
                        L7: Cds-CdCt_Cds-OneDeCs
                            L8: Cds-CdCt_Cds-CtCs
                            L8: Cds-CdCt_Cds-CbCs
                            L8: Cds-CdCt_Cds-COCs
                            L8: Cds-CdCt_Cds-CdCs
                            L8: Cds-CdCt_Cds-C=SCs
                        L7: Cds-CdCt_Cds-OneDeOs
                            L8: Cds-CdCt_Cds-CtOs
                            L8: Cds-CdCt_Cds-CbOs
                            L8: Cds-CdCt_Cds-COOs
                            L8: Cds-CdCt_Cds-CdOs
                            L8: Cds-CdCt_Cds-C=SOs
                        L7: Cds-CdCt_Cds-OneDeSs
                            L8: Cds-CdCt_Cds-CtSs
                            L8: Cds-CdCt_Cds-CbSs
                            L8: Cds-CdCt_Cds-COSs
                            L8: Cds-CdCt_Cds-CdSs
                            L8: Cds-CdCt_Cds-C=SSs
                        L7: Cds-CdCt_Cds-OneDeH
                            L8: Cds-CdCt_Cds-CtH
                            L8: Cds-CdCt_Cds-CbH
                            L8: Cds-CdCt_Cds-COH
                            L8: Cds-CdCt_Cds-CdH
                            L8: Cds-CdCt_Cds-C=SH
                    L6: Cds-CdCt_Cds-TwoDe
                        L7: Cds-CdCt_Cds-CtCt
                        L7: Cds-CdCt_Cds-CtCb
                        L7: Cds-CdCt_Cds-CtCO
                        L7: Cds-CdCt_Cds-CbCb
                        L7: Cds-CdCt_Cds-CbCO
                        L7: Cds-CdCt_Cds-COCO
                        L7: Cds-CdCt_Cds-CdCt
                        L7: Cds-CdCt_Cds-CdCb
                        L7: Cds-CdCt_Cds-CdCO
                        L7: Cds-CdCt_Cds-CtC=S
                        L7: Cds-CdCt_Cds-CbC=S
                        L7: Cds-CdCt_Cds-COC=S
                        L7: Cds-CdCt_Cds-CdCd
                        L7: Cds-CdCt_Cds-CdC=S
                        L7: Cds-CdCt_Cds-C=SC=S
                    L6: Cds-CdCt_Cds-CtH-F
                    L6: Cds-CdCt_Cds-CbH-F
                    L6: Cds-CdCt_Cds-COH-F
                    L6: Cds-CdCt_Cds-CdH-F
                    L6: Cds-CdCt_Cds-C=SH-F
                    L6: Cds-CdCt_Cds-CtH-Cl
                    L6: Cds-CdCt_Cds-CbH-Cl
                    L6: Cds-CdCt_Cds-COH-Cl
                    L6: Cds-CdCt_Cds-CdH-Cl
                    L6: Cds-CdCt_Cds-C=SH-Cl
                    L6: Cds-CdCt_Cds-CtH-Br
                    L6: Cds-CdCt_Cds-CbH-Br
                    L6: Cds-CdCt_Cds-COH-Br
                    L6: Cds-CdCt_Cds-CdH-Br
                    L6: Cds-CdCt_Cds-C=SH-Br
                    L6: Cds-CdCt_Cds-CsH
                    L6: Cds-CdCt_Cds-CsH-F
                    L6: Cds-CdCt_Cds-CsH-Cl
                    L6: Cds-CdCt_Cds-CsH-Br
                    L6: Cds-CdCt_Cds-OsH
                    L6: Cds-CdCt_Cds-OsH-F
                    L6: Cds-CdCt_Cds-OsH-Cl
                    L6: Cds-CdCt_Cds-OsH-Br
                    L6: Cds-CdCt_Cds-SsH
                    L6: Cds-CdCt_Cds-SsH-F
                    L6: Cds-CdCt_Cds-SsH-Cl
                    L6: Cds-CdCt_Cds-SsH-Br
                    L6: Cds-CdCt_Cds-HH
                    L6: Cds-CdCt_Cds-HH-HF
                    L6: Cds-CdCt_Cds-HH-HCl
                    L6: Cds-CdCt_Cds-HH-HBr
                    L6: Cds-CdCt_Cds-HH-FF
                    L6: Cds-CdCt_Cds-HH-FCl
                    L6: Cds-CdCt_Cds-HH-FBr
                    L6: Cds-CdCt_Cds-HH-ClCl
                    L6: Cds-CdCt_Cds-HH-ClBr
                    L6: Cds-CdCt_Cds-HH-BrBr
                L5: Cds-CdCb_Cds
                L5: Cds-CdCO_Cds
                L5: Cds-CtC=S_Cds
                L5: Cds-CbC=S_Cds
                L5: Cds-COC=S_Cds
                L5: Cds-CdCd_Cds
                    L6: Cds-CdCd_Cds-CsCs
                    L6: Cds-CdCd_Cds-OsCs
                    L6: Cds-CdCd_Cds-OsOs
                    L6: Cds-CdCd_Cds-SsCs
                    L6: Cds-CdCd_Cds-SsOs
                    L6: Cds-CdCd_Cds-SsSs
                    L6: Cds-CdCd_Cds-OneDe
                        L7: Cds-CdCd_Cds-OneDeCs
                            L8: Cds-CdCd_Cds-CtCs
                            L8: Cds-CdCd_Cds-CbCs
                            L8: Cds-CdCd_Cds-COCs
                            L8: Cds-CdCd_Cds-CdCs
                            L8: Cds-CdCd_Cds-C=SCs
                        L7: Cds-CdCd_Cds-OneDeOs
                            L8: Cds-CdCd_Cds-CtOs
                            L8: Cds-CdCd_Cds-CbOs
                            L8: Cds-CdCd_Cds-COOs
                            L8: Cds-CdCd_Cds-CdOs
                            L8: Cds-CdCd_Cds-C=SOs
                        L7: Cds-CdCd_Cds-OneDeSs
                            L8: Cds-CdCd_Cds-CtSs
                            L8: Cds-CdCd_Cds-CbSs
                            L8: Cds-CdCd_Cds-COSs
                            L8: Cds-CdCd_Cds-CdSs
                            L8: Cds-CdCd_Cds-C=SSs
                        L7: Cds-CdCd_Cds-OneDeH
                            L8: Cds-CdCd_Cds-CtH
                            L8: Cds-CdCd_Cds-CbH
                            L8: Cds-CdCd_Cds-COH
                            L8: Cds-CdCd_Cds-CdH
                            L8: Cds-CdCd_Cds-C=SH
                    L6: Cds-CdCd_Cds-TwoDe
                        L7: Cds-CdCd_Cds-CtCt
                        L7: Cds-CdCd_Cds-CtCb
                        L7: Cds-CdCd_Cds-CtCO
                        L7: Cds-CdCd_Cds-CbCb
                        L7: Cds-CdCd_Cds-CbCO
                        L7: Cds-CdCd_Cds-COCO
                        L7: Cds-CdCd_Cds-CdCt
                        L7: Cds-CdCd_Cds-CdCb
                        L7: Cds-CdCd_Cds-CdCO
                        L7: Cds-CdCd_Cds-CtC=S
                        L7: Cds-CdCd_Cds-CbC=S
                        L7: Cds-CdCd_Cds-COC=S
                        L7: Cds-CdCd_Cds-CdCd
                        L7: Cds-CdCd_Cds-CdC=S
                        L7: Cds-CdCd_Cds-C=SC=S
                    L6: Cds-CdCd_Cds-CtH-F
                    L6: Cds-CdCd_Cds-CbH-F
                    L6: Cds-CdCd_Cds-COH-F
                    L6: Cds-CdCd_Cds-CdH-F
                    L6: Cds-CdCd_Cds-C=SH-F
                    L6: Cds-CdCd_Cds-CtH-Cl
                    L6: Cds-CdCd_Cds-CbH-Cl
                    L6: Cds-CdCd_Cds-COH-Cl
                    L6: Cds-CdCd_Cds-CdH-Cl
                    L6: Cds-CdCd_Cds-C=SH-Cl
                    L6: Cds-CdCd_Cds-CtH-Br
                    L6: Cds-CdCd_Cds-CbH-Br
                    L6: Cds-CdCd_Cds-COH-Br
                    L6: Cds-CdCd_Cds-CdH-Br
                    L6: Cds-CdCd_Cds-C=SH-Br
                    L6: Cds-CdCd_Cds-SsH
                    L6: Cds-CdCd_Cds-SsH-F
                    L6: Cds-CdCd_Cds-SsH-Cl
                    L6: Cds-CdCd_Cds-SsH-Br
                    L6: Cds-CdCd_Cds-HH
                    L6: Cds-CdCd_Cds-HH-HF
                    L6: Cds-CdCd_Cds-HH-HCl
                    L6: Cds-CdCd_Cds-HH-HBr
                    L6: Cds-CdCd_Cds-HH-FF
                    L6: Cds-CdCd_Cds-HH-FCl
                    L6: Cds-CdCd_Cds-HH-FBr
                    L6: Cds-CdCd_Cds-HH-ClCl
                    L6: Cds-CdCd_Cds-HH-ClBr
                    L6: Cds-CdCd_Cds-HH-BrBr
                    L6: Cds-CdCd_Cds-OsH
                    L6: Cds-CdCd_Cds-OsH-F
                    L6: Cds-CdCd_Cds-OsH-Cl
                    L6: Cds-CdCd_Cds-OsH-Br
                    L6: Cds-CdCd_Cds-CsH
                    L6: Cds-CdCd_Cds-CsH-F
                    L6: Cds-CdCd_Cds-CsH-Cl
                    L6: Cds-CdCd_Cds-CsH-Br
                L5: Cds-CdC=S_Cds
                L5: Cds-C=SC=S_Cds
            L4: Cds-OJ/H_or_Val7/Cds
                L5: Cds-OJH_Cds
                    L6: Cds-OJH_Cds-HH
                    L6: Cds-OJH_Cds-CsH
                L5: Cds-OJH_Cds-F
                    L6: Cds-OJH_Cds-HH-FFF
                    L6: Cds-OJH_Cds-HH-FFCl
                    L6: Cds-OJH_Cds-HH-FFBr
                    L6: Cds-OJH_Cds-HH-FClCl
                    L6: Cds-OJH_Cds-HH-FClBr
                    L6: Cds-OJH_Cds-HH-FBrBr
                    L6: Cds-OJH_Cds-CsH-FF
                    L6: Cds-OJH_Cds-CsH-FCl
                    L6: Cds-OJH_Cds-CsH-FBr
                L5: Cds-OJH_Cds-Cl
                    L6: Cds-OJH_Cds-HH-ClClCl
                    L6: Cds-OJH_Cds-HH-ClClBr
                    L6: Cds-OJH_Cds-HH-ClBrBr
                    L6: Cds-OJH_Cds-CsH-ClCl
                    L6: Cds-OJH_Cds-CsH-ClBr
                L5: Cds-OJH_Cds-Br
                    L6: Cds-OJH_Cds-HH-BrBrBr
                    L6: Cds-OJH_Cds-CsH-BrBr
            L4: Cds-OJNonDe_Cds
                L5: Cds-OJCs_Cds-/H_or_Val7/H_or_Val7/
                    L6: Cds-OJCs_Cds-HH
                    L6: Cds-OJCs_Cds-HH-HF
                    L6: Cds-OJCs_Cds-HH-HCl
                    L6: Cds-OJCs_Cds-HH-HBr
                    L6: Cds-OJCs_Cds-HH-FF
                    L6: Cds-OJCs_Cds-HH-FCl
                    L6: Cds-OJCs_Cds-HH-FBr
                    L6: Cds-OJCs_Cds-HH-ClCl
                    L6: Cds-OJCs_Cds-HH-ClBr
                    L6: Cds-OJCs_Cds-HH-BrBr
            L4: Cds-OJDe_Cds
            L4: Cds-OneDeH_Cds-F
                L5: Cds-CtH_Cds-F
                    L6: Cds-CtH_Cds-CtH-FBr
                    L6: Cds-CtH_Cds-CbH-FBr
                    L6: Cds-CtH_Cds-COH-FBr
                    L6: Cds-CtH_Cds-C=SH-FBr
                    L6: Cds-CtH_Cds-CtH-FF
                    L6: Cds-CtH_Cds-CbH-FF
                    L6: Cds-CtH_Cds-COH-FF
                    L6: Cds-CtH_Cds-CdH-FF
                    L6: Cds-CtH_Cds-C=SH-FF
                    L6: Cds-CtH_Cds-OneDeCs-F
                        L7: Cds-CtH_Cds-CtCs-F
                        L7: Cds-CtH_Cds-CbCs-F
                        L7: Cds-CtH_Cds-COCs-F
                        L7: Cds-CtH_Cds-CdCs-F
                        L7: Cds-CtH_Cds-C=SCs-F
                    L6: Cds-CtH_Cds-OneDeOs-F
                        L7: Cds-CtH_Cds-CtOs-F
                        L7: Cds-CtH_Cds-CbOs-F
                        L7: Cds-CtH_Cds-COOs-F
                        L7: Cds-CtH_Cds-CdOs-F
                        L7: Cds-CtH_Cds-C=SOs-F
                    L6: Cds-CtH_Cds-OneDeSs-F
                        L7: Cds-CtH_Cds-CtSs-F
                        L7: Cds-CtH_Cds-CbSs-F
                        L7: Cds-CtH_Cds-COSs-F
                        L7: Cds-CtH_Cds-CdSs-F
                        L7: Cds-CtH_Cds-C=SSs-F
                    L6: Cds-CtH_Cds-CdH-HF
                    L6: Cds-CtH_Cds-CtH-FCl
                    L6: Cds-CtH_Cds-CbH-FCl
                    L6: Cds-CtH_Cds-COH-FCl
                    L6: Cds-CtH_Cds-C=SH-FCl
                L5: Cds-CbH_Cds-F
                    L6: Cds-CbH_Cds-CtH-FCl
                    L6: Cds-CbH_Cds-CbH-FCl
                    L6: Cds-CbH_Cds-COH-FCl
                    L6: Cds-CbH_Cds-C=SH-FCl
                    L6: Cds-CbH_Cds-CtH-FBr
                    L6: Cds-CbH_Cds-CbH-FBr
                    L6: Cds-CbH_Cds-COH-FBr
                    L6: Cds-CbH_Cds-C=SH-FBr
                    L6: Cds-CbH_Cds-CtH-FF
                    L6: Cds-CbH_Cds-CbH-FF
                    L6: Cds-CbH_Cds-COH-FF
                    L6: Cds-CbH_Cds-CdH-FF
                        L7: Cds-CbH_Cds-Cd(CdCb)H-FF
                    L6: Cds-CbH_Cds-C=SH-FF
                    L6: Cds-CbH_Cds-OneDeCs-F
                        L7: Cds-CbH_Cds-CtCs-F
                        L7: Cds-CbH_Cds-CbCs-F
                        L7: Cds-CbH_Cds-COCs-F
                        L7: Cds-CbH_Cds-CdCs-F
                        L7: Cds-CbH_Cds-C=SCs-F
                    L6: Cds-CbH_Cds-OneDeOs-F
                        L7: Cds-CbH_Cds-CtOs-F
                        L7: Cds-CbH_Cds-CbOs-F
                        L7: Cds-CbH_Cds-COOs-F
                        L7: Cds-CbH_Cds-CdOs-F
                        L7: Cds-CbH_Cds-C=SOs-F
                    L6: Cds-CbH_Cds-OneDeSs-F
                        L7: Cds-CbH_Cds-CtSs-F
                        L7: Cds-CbH_Cds-CbSs-F
                        L7: Cds-CbH_Cds-COSs-F
                        L7: Cds-CbH_Cds-CdSs-F
                        L7: Cds-CbH_Cds-C=SSs-F
                    L6: Cds-CbH_Cds-CdH-HF
                        L7: Cds-CbH_Cds-Cd(CdCb)H-HF
                L5: Cds-COH_Cds-F
                L5: Cds-CdH_Cds-F
                    L6: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-FCl
                    L6: Cds-CdH_Cds-(CsH-Cds)_cyc5-FCl
                    L6: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-FF
                    L6: Cds-CdH_Cds-(CsH-Cds)_cyc5-FF
                    L6: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-FBr
                    L6: Cds-CdH_Cds-(CsH-Cds)_cyc5-FBr
                    L6: Cds-CdH_Cds-OneDeH-FF
                        L7: Cds-CdH_Cds-CtH-FF
                        L7: Cds-CdH_Cds-CbH-FF
                            L8: Cds(CdCb)-CdH_Cds-CbH_cycle-FF
                            L8: Cds-CdH_Cds-Cb(Cb)H_cycle-FF
                        L7: Cds-CdH_Cds-COH-FF
                        L7: Cds-CdH_Cds-CdH-FF
                            L8: Cds-CdH_Cds-CdH_cyc5_1-FF
                            L8: Cds-CdH_Cds-CdH_cyc5_2-FF
                        L7: Cds-CdH_Cds-C=SH-FF
                    L6: Cds-CdH_Cds-OneDeH-FCl
                        L7: Cds-CdH_Cds-CtH-FCl
                        L7: Cds-CdH_Cds-CbH-FCl
                            L8: Cds(CdCb)-CdH_Cds-CbH_cycle-FCl
                            L8: Cds-CdH_Cds-Cb(Cb)H_cycle-FCl
                        L7: Cds-CdH_Cds-COH-FCl
                        L7: Cds-CdH_Cds-CdH-FCl
                            L8: Cds-CdH_Cds-CdH_cyc5_2-FCl
                        L7: Cds-CdH_Cds-C=SH-FCl
                    L6: Cds-CdH_Cds-OneDeH-FBr
                        L7: Cds-CdH_Cds-CtH-FBr
                        L7: Cds-CdH_Cds-CbH-FBr
                            L8: Cds(CdCb)-CdH_Cds-CbH_cycle-FBr
                            L8: Cds-CdH_Cds-Cb(Cb)H_cycle-FBr
                        L7: Cds-CdH_Cds-COH-FBr
                        L7: Cds-CdH_Cds-CdH-FBr
                            L8: Cds-CdH_Cds-CdH_cyc5_2-FBr
                        L7: Cds-CdH_Cds-C=SH-FBr
                    L6: Cds-CdH_Cds-OneDeCs-F
                        L7: Cds-CdH_Cds-CtCs-F
                        L7: Cds-CdH_Cds-CbCs-F
                        L7: Cds-CdH_Cds-COCs-F
                        L7: Cds-CdH_Cds-CdCs-F
                        L7: Cds-CdH_Cds-C=SCs-F
                    L6: Cds-CdH_Cds-OneDeOs-F
                        L7: Cds-CdH_Cds-CtOs-F
                        L7: Cds-CdH_Cds-CbOs-F
                        L7: Cds-CdH_Cds-COOs-F
                        L7: Cds-CdH_Cds-CdOs-F
                        L7: Cds-CdH_Cds-C=SOs-F
                    L6: Cds-CdH_Cds-OneDeSs-F
                        L7: Cds-CdH_Cds-CtSs-F
                        L7: Cds-CdH_Cds-CbSs-F
                        L7: Cds-CdH_Cds-COSs-F
                        L7: Cds-CdH_Cds-CdSs-F
                        L7: Cds-CdH_Cds-C=SSs-F
                    L6: Cds-CdH_Cds-TwoDe-F
                        L7: Cds-CdH_Cds-CdCd_cyc6-F
                            L8: Cds-CdH_Cds-CdCd_cyc6_cyc5-F
                    L6: Cds-CdH_Cds-CdH_cyc5_1-HF
                L5: Cds-C=SH_Cds-F
            L4: Cds-OneDeH_Cds-Cl
                L5: Cds-CtH_Cds-Cl
                    L6: Cds-CtH_Cds-CtH-ClCl
                    L6: Cds-CtH_Cds-CbH-ClCl
                    L6: Cds-CtH_Cds-COH-ClCl
                    L6: Cds-CtH_Cds-CdH-ClCl
                    L6: Cds-CtH_Cds-C=SH-ClCl
                    L6: Cds-CtH_Cds-CtH-ClBr
                    L6: Cds-CtH_Cds-CbH-ClBr
                    L6: Cds-CtH_Cds-COH-ClBr
                    L6: Cds-CtH_Cds-C=SH-ClBr
                    L6: Cds-CtH_Cds-OneDeCs-Cl
                        L7: Cds-CtH_Cds-CtCs-Cl
                        L7: Cds-CtH_Cds-CbCs-Cl
                        L7: Cds-CtH_Cds-COCs-Cl
                        L7: Cds-CtH_Cds-CdCs-Cl
                        L7: Cds-CtH_Cds-C=SCs-Cl
                    L6: Cds-CtH_Cds-OneDeOs-Cl
                        L7: Cds-CtH_Cds-CtOs-Cl
                        L7: Cds-CtH_Cds-CbOs-Cl
                        L7: Cds-CtH_Cds-COOs-Cl
                        L7: Cds-CtH_Cds-CdOs-Cl
                        L7: Cds-CtH_Cds-C=SOs-Cl
                    L6: Cds-CtH_Cds-OneDeSs-Cl
                        L7: Cds-CtH_Cds-CtSs-Cl
                        L7: Cds-CtH_Cds-CbSs-Cl
                        L7: Cds-CtH_Cds-COSs-Cl
                        L7: Cds-CtH_Cds-CdSs-Cl
                        L7: Cds-CtH_Cds-C=SSs-Cl
                    L6: Cds-CtH_Cds-CdH-HCl
                L5: Cds-CbH_Cds-Cl
                    L6: Cds-CbH_Cds-OneDeCs-Cl
                        L7: Cds-CbH_Cds-CtCs-Cl
                        L7: Cds-CbH_Cds-CbCs-Cl
                        L7: Cds-CbH_Cds-COCs-Cl
                        L7: Cds-CbH_Cds-CdCs-Cl
                        L7: Cds-CbH_Cds-C=SCs-Cl
                    L6: Cds-CbH_Cds-OneDeOs-Cl
                        L7: Cds-CbH_Cds-CtOs-Cl
                        L7: Cds-CbH_Cds-CbOs-Cl
                        L7: Cds-CbH_Cds-COOs-Cl
                        L7: Cds-CbH_Cds-CdOs-Cl
                        L7: Cds-CbH_Cds-C=SOs-Cl
                    L6: Cds-CbH_Cds-OneDeSs-Cl
                        L7: Cds-CbH_Cds-CtSs-Cl
                        L7: Cds-CbH_Cds-CbSs-Cl
                        L7: Cds-CbH_Cds-COSs-Cl
                        L7: Cds-CbH_Cds-CdSs-Cl
                        L7: Cds-CbH_Cds-C=SSs-Cl
                    L6: Cds-CbH_Cds-CdH-HCl
                        L7: Cds-CbH_Cds-Cd(CdCb)H-HCl
                    L6: Cds-CbH_Cds-CtH-ClCl
                    L6: Cds-CbH_Cds-CbH-ClCl
                    L6: Cds-CbH_Cds-COH-ClCl
                    L6: Cds-CbH_Cds-CdH-ClCl
                        L7: Cds-CbH_Cds-Cd(CdCb)H-ClCl
                    L6: Cds-CbH_Cds-C=SH-ClCl
                    L6: Cds-CbH_Cds-CtH-ClBr
                    L6: Cds-CbH_Cds-CbH-ClBr
                    L6: Cds-CbH_Cds-COH-ClBr
                    L6: Cds-CbH_Cds-C=SH-ClBr
                    L6: Cds-CbH_Cds-Cd(CdCb)H-FCl
                L5: Cds-COH_Cds-Cl
                L5: Cds-CdH_Cds-Cl
                    L6: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-ClBr
                    L6: Cds-CdH_Cds-(CsH-Cds)_cyc5-ClBr
                    L6: Cds-CdH_Cds-OneDeH-ClCl
                        L7: Cds-CdH_Cds-CtH-ClCl
                        L7: Cds-CdH_Cds-CbH-ClCl
                            L8: Cds(CdCb)-CdH_Cds-CbH_cycle-ClCl
                            L8: Cds-CdH_Cds-Cb(Cb)H_cycle-ClCl
                        L7: Cds-CdH_Cds-COH-ClCl
                        L7: Cds-CdH_Cds-CdH-ClCl
                            L8: Cds-CdH_Cds-CdH_cyc5_1-ClCl
                            L8: Cds-CdH_Cds-CdH_cyc5_2-ClCl
                        L7: Cds-CdH_Cds-C=SH-ClCl
                    L6: Cds-CdH_Cds-OneDeH-ClBr
                        L7: Cds-CdH_Cds-CtH-ClBr
                        L7: Cds-CdH_Cds-CbH-ClBr
                            L8: Cds(CdCb)-CdH_Cds-CbH_cycle-ClBr
                            L8: Cds-CdH_Cds-Cb(Cb)H_cycle-ClBr
                        L7: Cds-CdH_Cds-COH-ClBr
                        L7: Cds-CdH_Cds-CdH-ClBr
                            L8: Cds-CdH_Cds-CdH_cyc5_2-ClBr
                        L7: Cds-CdH_Cds-C=SH-ClBr
                    L6: Cds-CdH_Cds-OneDeCs-Cl
                        L7: Cds-CdH_Cds-CtCs-Cl
                        L7: Cds-CdH_Cds-CbCs-Cl
                        L7: Cds-CdH_Cds-COCs-Cl
                        L7: Cds-CdH_Cds-CdCs-Cl
                        L7: Cds-CdH_Cds-C=SCs-Cl
                    L6: Cds-CdH_Cds-OneDeOs-Cl
                        L7: Cds-CdH_Cds-CtOs-Cl
                        L7: Cds-CdH_Cds-CbOs-Cl
                        L7: Cds-CdH_Cds-COOs-Cl
                        L7: Cds-CdH_Cds-CdOs-Cl
                        L7: Cds-CdH_Cds-C=SOs-Cl
                    L6: Cds-CdH_Cds-OneDeSs-Cl
                        L7: Cds-CdH_Cds-CtSs-Cl
                        L7: Cds-CdH_Cds-CbSs-Cl
                        L7: Cds-CdH_Cds-COSs-Cl
                        L7: Cds-CdH_Cds-CdSs-Cl
                        L7: Cds-CdH_Cds-C=SSs-Cl
                    L6: Cds-CdH_Cds-TwoDe-Cl
                        L7: Cds-CdH_Cds-CdCd_cyc6-Cl
                            L8: Cds-CdH_Cds-CdCd_cyc6_cyc5-Cl
                    L6: Cds-CdH_Cds-CdH_cyc5_1-HCl
                    L6: Cds-CdH_Cds-CdH_cyc5_1-FCl
                    L6: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-ClCl
                    L6: Cds-CdH_Cds-(CsH-Cds)_cyc5-ClCl
                L5: Cds-C=SH_Cds-Cl
            L4: Cds-OneDeH_Cds-Br
                L5: Cds-CtH_Cds-Br
                    L6: Cds-CtH_Cds-CtH-BrBr
                    L6: Cds-CtH_Cds-CbH-BrBr
                    L6: Cds-CtH_Cds-COH-BrBr
                    L6: Cds-CtH_Cds-CdH-BrBr
                    L6: Cds-CtH_Cds-C=SH-BrBr
                    L6: Cds-CtH_Cds-OneDeCs-Br
                        L7: Cds-CtH_Cds-CtCs-Br
                        L7: Cds-CtH_Cds-CbCs-Br
                        L7: Cds-CtH_Cds-COCs-Br
                        L7: Cds-CtH_Cds-CdCs-Br
                        L7: Cds-CtH_Cds-C=SCs-Br
                    L6: Cds-CtH_Cds-OneDeOs-Br
                        L7: Cds-CtH_Cds-CtOs-Br
                        L7: Cds-CtH_Cds-CbOs-Br
                        L7: Cds-CtH_Cds-COOs-Br
                        L7: Cds-CtH_Cds-CdOs-Br
                        L7: Cds-CtH_Cds-C=SOs-Br
                    L6: Cds-CtH_Cds-OneDeSs-Br
                        L7: Cds-CtH_Cds-CtSs-Br
                        L7: Cds-CtH_Cds-CbSs-Br
                        L7: Cds-CtH_Cds-COSs-Br
                        L7: Cds-CtH_Cds-CdSs-Br
                        L7: Cds-CtH_Cds-C=SSs-Br
                    L6: Cds-CtH_Cds-CdH-HBr
                L5: Cds-CbH_Cds-Br
                    L6: Cds-CbH_Cds-OneDeCs-Br
                        L7: Cds-CbH_Cds-CtCs-Br
                        L7: Cds-CbH_Cds-CbCs-Br
                        L7: Cds-CbH_Cds-COCs-Br
                        L7: Cds-CbH_Cds-CdCs-Br
                        L7: Cds-CbH_Cds-C=SCs-Br
                    L6: Cds-CbH_Cds-OneDeOs-Br
                        L7: Cds-CbH_Cds-CtOs-Br
                        L7: Cds-CbH_Cds-CbOs-Br
                        L7: Cds-CbH_Cds-COOs-Br
                        L7: Cds-CbH_Cds-CdOs-Br
                        L7: Cds-CbH_Cds-C=SOs-Br
                    L6: Cds-CbH_Cds-OneDeSs-Br
                        L7: Cds-CbH_Cds-CtSs-Br
                        L7: Cds-CbH_Cds-CbSs-Br
                        L7: Cds-CbH_Cds-COSs-Br
                        L7: Cds-CbH_Cds-CdSs-Br
                        L7: Cds-CbH_Cds-C=SSs-Br
                    L6: Cds-CbH_Cds-CdH-HBr
                        L7: Cds-CbH_Cds-Cd(CdCb)H-HBr
                    L6: Cds-CbH_Cds-CtH-BrBr
                    L6: Cds-CbH_Cds-CbH-BrBr
                    L6: Cds-CbH_Cds-COH-BrBr
                    L6: Cds-CbH_Cds-CdH-BrBr
                        L7: Cds-CbH_Cds-Cd(CdCb)H-BrBr
                    L6: Cds-CbH_Cds-C=SH-BrBr
                    L6: Cds-CbH_Cds-Cd(CdCb)H-FBr
                    L6: Cds-CbH_Cds-Cd(CdCb)H-ClBr
                L5: Cds-COH_Cds-Br
                L5: Cds-CdH_Cds-Br
                    L6: Cds-CdH_Cds-(CsH-Cs-Cds)_cyc6-BrBr
                    L6: Cds-CdH_Cds-(CsH-Cds)_cyc5-BrBr
                    L6: Cds-CdH_Cds-OneDeH-BrBr
                        L7: Cds-CdH_Cds-CtH-BrBr
                        L7: Cds-CdH_Cds-CbH-BrBr
                            L8: Cds(CdCb)-CdH_Cds-CbH_cycle-BrBr
                            L8: Cds-CdH_Cds-Cb(Cb)H_cycle-BrBr
                        L7: Cds-CdH_Cds-COH-BrBr
                        L7: Cds-CdH_Cds-CdH-BrBr
                            L8: Cds-CdH_Cds-CdH_cyc5_1-BrBr
                            L8: Cds-CdH_Cds-CdH_cyc5_2-BrBr
                        L7: Cds-CdH_Cds-C=SH-BrBr
                    L6: Cds-CdH_Cds-OneDeCs-Br
                        L7: Cds-CdH_Cds-CtCs-Br
                        L7: Cds-CdH_Cds-CbCs-Br
                        L7: Cds-CdH_Cds-COCs-Br
                        L7: Cds-CdH_Cds-CdCs-Br
                        L7: Cds-CdH_Cds-C=SCs-Br
                    L6: Cds-CdH_Cds-OneDeOs-Br
                        L7: Cds-CdH_Cds-CtOs-Br
                        L7: Cds-CdH_Cds-CbOs-Br
                        L7: Cds-CdH_Cds-COOs-Br
                        L7: Cds-CdH_Cds-CdOs-Br
                        L7: Cds-CdH_Cds-C=SOs-Br
                    L6: Cds-CdH_Cds-OneDeSs-Br
                        L7: Cds-CdH_Cds-CtSs-Br
                        L7: Cds-CdH_Cds-CbSs-Br
                        L7: Cds-CdH_Cds-COSs-Br
                        L7: Cds-CdH_Cds-CdSs-Br
                        L7: Cds-CdH_Cds-C=SSs-Br
                    L6: Cds-CdH_Cds-TwoDe-Br
                        L7: Cds-CdH_Cds-CdCd_cyc6-Br
                            L8: Cds-CdH_Cds-CdCd_cyc6_cyc5-Br
                    L6: Cds-CdH_Cds-CdH_cyc5_1-HBr
                    L6: Cds-CdH_Cds-CdH_cyc5_1-FBr
                    L6: Cds-CdH_Cds-CdH_cyc5_1-ClBr
                L5: Cds-C=SH_Cds-Br
    L2: Ct_R
        L3: Ct_Ct
            L4: Ct-/H_or_Val7/Ct-/H_or_Val7/
                L5: Ct-H_Ct-H
                L5: Ct-H_Ct-H-HF
                L5: Ct-H_Ct-H-HCl
                L5: Ct-H_Ct-H-HBr
                L5: Ct-H_Ct-H-FF
                L5: Ct-H_Ct-H-FCl
                L5: Ct-H_Ct-H-FBr
                L5: Ct-H_Ct-H-ClCl
                L5: Ct-H_Ct-H-ClBr
                L5: Ct-H_Ct-H-BrBr
            L4: Ct-/H_or_Val7/Ct-Cs
                L5: Ct-H_Ct-Cs
                L5: Ct-H_Ct-Cs-F
                L5: Ct-H_Ct-Cs-Cl
                L5: Ct-H_Ct-Cs-Br
            L4: Ct-Cs_Ct-/H_or_Val7/
                L5: Ct-Cs_Ct-H
                L5: Ct-Cs_Ct-H-F
                L5: Ct-Cs_Ct-H-Cl
                L5: Ct-Cs_Ct-H-Br
            L4: Ct-Cs_Ct-Cs
            L4: Ct-/H_or_Val7/Ct-De
                L5: Ct-H_Ct-De
                    L6: Ct-H_Ct-Ct
                    L6: Ct-H_Ct-Cb
                    L6: Ct-H_Ct-CO
                    L6: Ct-H_Ct-Cd
                        L7: Ct-H_Ct-Cd-C-Cb
                    L6: Ct-H_Ct-C=S
                L5: Ct-H_Ct-De-F
                    L6: Ct-H_Ct-Ct-F
                    L6: Ct-H_Ct-Cb-F
                    L6: Ct-H_Ct-CO-F
                    L6: Ct-H_Ct-Cd-F
                        L7: Ct-H_Ct-Cd-C-Cb-F
                    L6: Ct-H_Ct-C=S-F
                L5: Ct-H_Ct-De-Cl
                    L6: Ct-H_Ct-Ct-Cl
                    L6: Ct-H_Ct-Cb-Cl
                    L6: Ct-H_Ct-CO-Cl
                    L6: Ct-H_Ct-Cd-Cl
                        L7: Ct-H_Ct-Cd-C-Cb-Cl
                    L6: Ct-H_Ct-C=S-Cl
                L5: Ct-H_Ct-De-Br
                    L6: Ct-H_Ct-Ct-Br
                    L6: Ct-H_Ct-Cb-Br
                    L6: Ct-H_Ct-CO-Br
                    L6: Ct-H_Ct-Cd-Br
                        L7: Ct-H_Ct-Cd-C-Cb-Br
                    L6: Ct-H_Ct-C=S-Br
            L4: Ct-Cs_Ct-De
                L5: Ct-Cs_Ct-Ct
                L5: Ct-Cs_Ct-Cb
                L5: Ct-Cs_Ct-CO
                L5: Ct-Cs_Ct-Cd
                L5: Ct-Cs_Ct-C=S
            L4: Ct-De_Ct-/H_or_Val7/
                L5: Ct-De_Ct-H
                    L6: Ct-Cb_Ct-H
                    L6: Ct-CO_Ct-H
                    L6: Ct-Cd_Ct-H
                    L6: Ct-Ct_Ct-H
                    L6: Ct-C=S_Ct-H
                L5: Ct-De_Ct-H-F
                    L6: Ct-Cb_Ct-H-F
                    L6: Ct-CO_Ct-H-F
                    L6: Ct-Cd_Ct-H-F
                    L6: Ct-Ct_Ct-H-F
                    L6: Ct-C=S_Ct-H-F
                L5: Ct-De_Ct-H-Cl
                    L6: Ct-Cb_Ct-H-Cl
                    L6: Ct-CO_Ct-H-Cl
                    L6: Ct-Cd_Ct-H-Cl
                    L6: Ct-Ct_Ct-H-Cl
                    L6: Ct-C=S_Ct-H-Cl
                L5: Ct-De_Ct-H-Br
                    L6: Ct-Cb_Ct-H-Br
                    L6: Ct-CO_Ct-H-Br
                    L6: Ct-Cd_Ct-H-Br
                    L6: Ct-Ct_Ct-H-Br
                    L6: Ct-C=S_Ct-H-Br
            L4: Ct-De_Ct-Cs
                L5: Ct-Cb_Ct-Cs
                L5: Ct-CO_Ct-Cs
                L5: Ct-Cd_Ct-Cs
                L5: Ct-Ct_Ct-Cs
                L5: Ct-CS_Ct-Cs
            L4: Ct-De_Ct-De
                L5: Ct-Ct_Ct-Ct
                L5: Ct-Cd_Ct-Ct
                L5: Ct-Ct_Ct-Cd
                L5: Ct-Cd_Ct-Cd
                    L6: Ct-Cd_Ct-Cd_cyc6
                L5: Ct-De_Ct-Cb
                    L6: Ct-Cd_Ct-Cb
                        L7: Ct-CdCdCb_Ct-Cb_cyc6
                L5: Ct-Cb_Ct-Cd
                    L6: Ct-Cb_Ct-CdCdCb_cyc6
                    L6: Ct-Cb_Ct-CdCb_cyc5
            L4: Ct-O_Ct
                L5: Ct-O_Ct-Cb
        L3: Ct_Nt
            L4: Ct_N3t
                L5: Ct-/H_or_Val7/N3t
                    L6: Ct-H_N3t
                    L6: Ct-H_N3t-F
                    L6: Ct-H_N3t-Cl
                    L6: Ct-H_N3t-Br
                L5: Ct-NonDe_N3t
                L5: Ct-OneDe_N3t
            L4: Ct_N5t
    L2: Od_R
        L3: Od_CO
            L4: Od_CO-/H_or_Val7/H_or_Val7/
                L5: Od_CO-HH
                L5: Od_CO-HH-HF
                L5: Od_CO-HH-HCl
                L5: Od_CO-HH-HBr
                L5: Od_CO-HH-FF
                L5: Od_CO-HH-FCl
                L5: Od_CO-HH-FBr
                L5: Od_CO-HH-ClCl
                L5: Od_CO-HH-ClBr
                L5: Od_CO-HH-BrBr
            L4: Od_CO-Nd/H_or_Val7/
                L5: Od_CO-NdH
                    L6: Od_CO-CsH
                L5: Od_CO-NdH-F
                    L6: Od_CO-CsH-F
                L5: Od_CO-NdH-Cl
                    L6: Od_CO-CsH-Cl
                L5: Od_CO-NdH-Br
                    L6: Od_CO-CsH-Br
            L4: Od_CO-NdNd
                L5: Od_CO-CsCs
            L4: Od_CO-De/H_or_Val7/
                L5: Od_CO-DeH
                    L6: Od_CO-CdH
                    L6: Od_CO-CtH
                L5: Od_CO-DeH-F
                    L6: Od_CO-CdH-F
                    L6: Od_CO-CtH-F
                L5: Od_CO-DeH-Cl
                    L6: Od_CO-CdH-Cl
                    L6: Od_CO-CtH-Cl
                L5: Od_CO-DeH-Br
                    L6: Od_CO-CdH-Br
                    L6: Od_CO-CtH-Br
            L4: Od_CO-DeNd
                L5: Od_CO-CdCs
                L5: Od_CO-CtCs
        L3: Od_Cdd
            L4: Od_Cdd-O2d
        L3: Od_Nd
            L4: Od_N3d
            L4: Od_N5dc
    L2: Nd_R
        L3: N1dc_R
        L3: N3d_R
            L4: N3d_Cd
                L5: N3d_Cds
                    L6: N3d-/H_or_Val7/Cds
                        L7: N3d-H_Cds
                            L8: N3d-H_Cds-HH
                            L8: N3d-H_Cds-NonDeH
                            L8: N3d-H_Cds-NonDe2
                        L7: N3d-H_Cds-F
                            L8: N3d-H_Cds-HH-HHF
                            L8: N3d-H_Cds-HH-HFF
                            L8: N3d-H_Cds-HH-FFF
                            L8: N3d-H_Cds-NonDeH-HF
                            L8: N3d-H_Cds-NonDeH-FF
                            L8: N3d-H_Cds-NonDe2-F
                        L7: N3d-H_Cds-Cl
                            L8: N3d-H_Cds-HH-HHCl
                            L8: N3d-H_Cds-HH-HFCl
                            L8: N3d-H_Cds-HH-HClCl
                            L8: N3d-H_Cds-HH-FFCl
                            L8: N3d-H_Cds-HH-FClCl
                            L8: N3d-H_Cds-HH-ClClCl
                            L8: N3d-H_Cds-NonDeH-HCl
                            L8: N3d-H_Cds-NonDeH-FCl
                            L8: N3d-H_Cds-NonDeH-ClCl
                            L8: N3d-H_Cds-NonDe2-Cl
                        L7: N3d-H_Cds-Br
                    L6: N3d-NonDe_Cds
                    L6: N3d-OneDe_Cds
                L5: N3d_Cdd
            L4: N3d_Od
                L5: N3d-/H_or_Val7/Od
                    L6: N3d-H_Od
                    L6: N3d-H_Od-F
                    L6: N3d-H_Od-Cl
                    L6: N3d-H_Od-Br
                L5: N3d-NonDe_Od
                L5: N3d-OneDe_Od
            L4: N3d_Nd
                L5: N3d_N3d
                    L6: N3d-/H_or_Val7/N3d
                        L7: N3d-H_N3d
                            L8: N3d-H_N3d-H
                            L8: N3d-H_N3d-H-HF
                            L8: N3d-H_N3d-H-HCl
                            L8: N3d-H_N3d-H-HBr
                            L8: N3d-H_N3d-NonDe
                            L8: N3d-H_N3d-OneDe
                        L7: N3d-H_N3d-F
                            L8: N3d-H_N3d-H-FF
                            L8: N3d-H_N3d-H-FCl
                            L8: N3d-H_N3d-H-FBr
                            L8: N3d-H_N3d-NonDe-F
                            L8: N3d-H_N3d-OneDe-F
                        L7: N3d-H_N3d-Cl
                            L8: N3d-H_N3d-H-ClCl
                            L8: N3d-H_N3d-H-ClBr
                            L8: N3d-H_N3d-NonDe-Cl
                            L8: N3d-H_N3d-OneDe-Cl
                        L7: N3d-H_N3d-Br
                            L8: N3d-H_N3d-H-BrBr
                            L8: N3d-H_N3d-NonDe-Br
                            L8: N3d-H_N3d-OneDe-Br
                    L6: N3d-NonDe_N3d
                    L6: N3d-OneDe_N3d
                L5: N3d_N5dc
    L2: Nt_R
        L3: N3t_R
            L4: N3t_Ct
                L5: N3t_Ct-/H_or_Val7/
                    L6: N3t_Ct-H
                    L6: N3t_Ct-H-F
                    L6: N3t_Ct-H-Cl
                    L6: N3t_Ct-H-Br
                L5: N3t_Ct-NonDe
                L5: N3t_Ct-OneDe
            L4: N3t_N3t
        L3: N5t_R
    L2: Sd_R
        L3: Sd_Cdd
            L4: Sd_Cdd-S2d
        L3: Sd_Cd
            L4: Sd_Cds-/H_or_Val7/H_or_Val7/
                L5: Sd_Cds-HH
                L5: Sd_Cds-HH-HF
                L5: Sd_Cds-HH-HCl
                L5: Sd_Cds-HH-HBr
                L5: Sd_Cds-HH-FF
                L5: Sd_Cds-HH-FCl
                L5: Sd_Cds-HH-FBr
                L5: Sd_Cds-HH-ClCl
                L5: Sd_Cds-HH-ClBr
                L5: Sd_Cds-HH-BrBr
            L4: Sd_Cds-Cs/H_or_Val7/
                L5: Sd_Cds-CsH
                L5: Sd_Cds-CsH-F
                L5: Sd_Cds-CsH-Cl
                L5: Sd_Cds-CsH-Br
            L4: Sd_Cds-Os/H_or_Val7/
                L5: Sd_Cds-OsH
                L5: Sd_Cds-OsH-F
                L5: Sd_Cds-OsH-Cl
                L5: Sd_Cds-OsH-Br
            L4: Sd_Cds-OsCs
            L4: Sd_Cds-CsCs
            L4: Sd_Cds-OneDe/H_or_Val7/
                L5: Sd_Cds-OneDeH
                    L6: Sd_Cds-CtH
                    L6: Sd_Cds-CbH
                    L6: Sd_Cds-COH
                    L6: Sd_Cds-CdH
                    L6: Sd_Cds-C=SH
                L5: Sd_Cds-OneDeH-F
                    L6: Sd_Cds-CtH-F
                    L6: Sd_Cds-CbH-F
                    L6: Sd_Cds-COH-F
                    L6: Sd_Cds-CdH-F
                    L6: Sd_Cds-C=SH-F
                L5: Sd_Cds-OneDeH-Cl
                    L6: Sd_Cds-CtH-Cl
                    L6: Sd_Cds-CbH-Cl
                    L6: Sd_Cds-COH-Cl
                    L6: Sd_Cds-CdH-Cl
                    L6: Sd_Cds-C=SH-Cl
                L5: Sd_Cds-OneDeH-Br
                    L6: Sd_Cds-CtH-Br
                    L6: Sd_Cds-CbH-Br
                    L6: Sd_Cds-COH-Br
                    L6: Sd_Cds-CdH-Br
                    L6: Sd_Cds-C=SH-Br
            L4: Sd_Cds-OneDeCs
                L5: Sd_Cds-CtCs
                L5: Sd_Cds-CbCs
                L5: Sd_Cds-COCs
                L5: Sd_Cds-CdCs
                L5: Sd_Cds-C=SCs
            L4: Sd_Cds-TwoDe
                L5: Sd_Cds-CtCt
                L5: Sd_Cds-CtCb
                L5: Sd_Cds-CtCO
                L5: Sd_Cds-CbCb
                L5: Sd_Cds-CbCO
                L5: Sd_Cds-COCO
                L5: Sd_Cds-CdCt
                L5: Sd_Cds-CdCb
                L5: Sd_Cds-CdCO
                L5: Sd_Cds-CtC=S
                L5: Sd_Cds-CbC=S
                L5: Sd_Cds-COC=S
                L5: Sd_Cds-CdCd
                L5: Sd_Cds-CdC=S
                L5: Sd_Cds-C=SC=S
L1: YJ
    L2: HJ
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
    L2: Y_1centertrirad
        L3: N_atom_quartet
        L3: N_atom_doublet
        L3: C/H_or_Val7/quartet
            L4: CH_quartet
            L4: CH_quartet-F
            L4: CH_quartet-Cl
            L4: CH_quartet-Br
        L3: C/H_or_Val7/doublet
            L4: CH_doublet
            L4: CH_doublet-F
            L4: CH_doublet-Cl
            L4: CH_doublet-Br
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: SJJ
        L3: C/H_or_Val7/2_triplet
            L4: CH2_triplet
            L4: CH2_triplet-HF
            L4: CH2_triplet-HCl
            L4: CH2_triplet-HBr
            L4: CH2_triplet-FF
            L4: CH2_triplet-FCl
            L4: CH2_triplet-FBr
            L4: CH2_triplet-ClCl
            L4: CH2_triplet-ClBr
            L4: CH2_triplet-BrBr
        L3: CO_birad
        L3: N/H_or_Val7/triplet
            L4: NH_triplet
            L4: NH_triplet-F
            L4: NH_triplet-Cl
            L4: NH_triplet-Br
    L2: CJ
        L3: CbJ
        L3: CtJ
            L4: CtJ_Ct
            L4: CtJ_N3t
        L3: C2b
        L3: C=SJ
            L4: C=SJ-/H_or_Val7/
                L5: C=SJ-H
                L5: C=SJ-H-F
                L5: C=SJ-H-Cl
                L5: C=SJ-H-Br
            L4: C=SJ-Cs
            L4: C=SJ-Ct
            L4: C=SJ-Cb
            L4: C=SJ-CO
            L4: C=SJ-O2s
            L4: C=SJ-S2s
            L4: C=SJ-Cd
            L4: C=SJ-C=S
        L3: CO_rad
            L4: CO_pri_rad-H_or_Val7-1
                L5: CO_pri_rad
                L5: CO_pri_rad-F
                L5: CO_pri_rad-Cl
                L5: CO_pri_rad-Br
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: CsJ
            L4: CsJ-/H_or_Val7/H_or_Val7/H_or_Val7/
                L5: CsJ-HHH
            L4: CsJ-Cs/H_or_Val7/H_or_Val7/
                L5: CsJ-CsHH
                L5: CsJ-CsHH-HF
                L5: CsJ-CsHH-HCl
                L5: CsJ-CsHH-HBr
                L5: CsJ-CsHH-FF
                L5: CsJ-CsHH-FCl
                L5: CsJ-CsHH-FBr
                L5: CsJ-CsHH-ClCl
                L5: CsJ-CsHH-ClBr
                L5: CsJ-CsHH-BrBr
            L4: CsJ-CsCs/H_or_Val7/
                L5: CsJ-CsCsH
                L5: CsJ-CsCsH-F
                L5: CsJ-CsCsH-Cl
                L5: CsJ-CsCsH-Br
            L4: CsJ-CsCsCs
            L4: CsJ-Os/H_or_Val7/H_or_Val7/
                L5: CsJ-OsHH
                L5: CsJ-OsHH-HF
                L5: CsJ-OsHH-HCl
                L5: CsJ-OsHH-HBr
                L5: CsJ-OsHH-FF
                L5: CsJ-OsHH-FCl
                L5: CsJ-OsHH-FBr
                L5: CsJ-OsHH-ClCl
                L5: CsJ-OsHH-ClBr
                L5: CsJ-OsHH-BrBr
            L4: CsJ-OsCs/H_or_Val7/
                L5: CsJ-OsCsH
                L5: CsJ-OsCsH-F
                L5: CsJ-OsCsH-Cl
                L5: CsJ-OsCsH-Br
            L4: CsJ-OsCsCs
            L4: CsJ-OsOs/H_or_Val7/
                L5: CsJ-OsOsH
                L5: CsJ-OsOsH-F
                L5: CsJ-OsOsH-Cl
                L5: CsJ-OsOsH-Br
            L4: CsJ-OsOsCs
            L4: CsJ-OsOsOs
            L4: CsJ-Ss/H_or_Val7/H_or_Val7/
                L5: CsJ-SsHH
                L5: CsJ-SsHH-HF
                L5: CsJ-SsHH-HCl
                L5: CsJ-SsHH-HBr
                L5: CsJ-SsHH-FF
                L5: CsJ-SsHH-FCl
                L5: CsJ-SsHH-FBr
                L5: CsJ-SsHH-ClCl
                L5: CsJ-SsHH-ClBr
                L5: CsJ-SsHH-BrBr
            L4: CsJ-SsCs/H_or_Val7/
                L5: CsJ-SsCsH
                L5: CsJ-SsCsH-F
                L5: CsJ-SsCsH-Cl
                L5: CsJ-SsCsH-Br
            L4: CsJ-SsCsCs
            L4: CsJ-SsSs/H_or_Val7/
                L5: CsJ-SsSsH
                L5: CsJ-SsSsH-F
                L5: CsJ-SsSsH-Cl
                L5: CsJ-SsSsH-Br
            L4: CsJ-SsSsCs
            L4: CsJ-SsSsSs
            L4: CsJ-Ns/H_or_Val7/H_or_Val7/
                L5: CsJ-NsHH
                L5: CsJ-NsHH-HF
                L5: CsJ-NsHH-HCl
                L5: CsJ-NsHH-HBr
                L5: CsJ-NsHH-FF
                L5: CsJ-NsHH-FCl
                L5: CsJ-NsHH-FBr
                L5: CsJ-NsHH-ClCl
                L5: CsJ-NsHH-ClBr
                L5: CsJ-NsHH-BrBr
            L4: CsJ-NsCs/H_or_Val7/
                L5: CsJ-NsCsH
                L5: CsJ-NsCsH-F
                L5: CsJ-NsCsH-Cl
                L5: CsJ-NsCsH-Br
            L4: CsJ-OneDe
                L5: CsJ-OneDeCsCs
                    L6: CsJ-CtCsCs
                    L6: CsJ-CbCsCs
                    L6: CsJ-COCsCs
                    L6: CsJ-CdCsCs
                    L6: CsJ-C=SCsCs
                L5: CsJ-OneDeOsCs
                L5: CsJ-OneDeSsCs
                L5: CsJ-OneDeOsOs
                L5: CsJ-OneDeOsSs
                L5: CsJ-OneDeSsSs
                L5: CsJ-OneDeNsCs
                L5: CsJ-OneDeHH
                    L6: CsJ-CtHH
                    L6: CsJ-CbHH
                    L6: CsJ-COHH
                    L6: CsJ-CdHH
                        L7: CsJ-(CdC)HH
                    L6: CsJ-C=SHH
                L5: CsJ-OneDeCsH
                    L6: CsJ-CtCsH
                    L6: CsJ-CbCsH
                    L6: CsJ-COCsH
                    L6: CsJ-CdCsH
                    L6: CsJ-C=SCsH
                L5: CsJ-OneDeOsH
                L5: CsJ-OneDeSsH
                L5: CsJ-OneDeNsH
            L4: CsJ-TwoDe
                L5: CsJ-TwoDeCs
                    L6: CsJ-CtCtCs
                    L6: CsJ-CtCbCs
                    L6: CsJ-CtCOCs
                    L6: CsJ-CbCbCs
                    L6: CsJ-CbCOCs
                    L6: CsJ-COCOCs
                    L6: CsJ-CdCtCs
                    L6: CsJ-CdCbCs
                    L6: CsJ-CdCOCs
                    L6: CsJ-CtC=SCs
                    L6: CsJ-CbC=SCs
                    L6: CsJ-COC=SCs
                    L6: CsJ-CdCdCs
                    L6: CsJ-CdC=SCs
                    L6: CsJ-C=SC=SCs
                L5: CsJ-TwoDeOs
                L5: CsJ-TwoDeSs
                L5: CsJ-TwoDeH
                    L6: CsJ-CtCtH
                    L6: CsJ-CtCbH
                    L6: CsJ-CtCOH
                    L6: CsJ-CbCbH
                    L6: CsJ-CbCOH
                    L6: CsJ-COCOH
                    L6: CsJ-CdCtH
                    L6: CsJ-CdCbH
                    L6: CsJ-CdCOH
                    L6: CsJ-CtC=SH
                    L6: CsJ-CbC=SH
                    L6: CsJ-COC=SH
                    L6: CsJ-CdCdH
                    L6: CsJ-CdC=SH
                    L6: CsJ-C=SC=SH
            L4: CsJ-ThreeDe
            L4: CsJ-OneDeHH-HF
                L5: CsJ-CtHH-HF
                L5: CsJ-CbHH-HF
                L5: CsJ-COHH-HF
                L5: CsJ-CdHH-HF
                    L6: CsJ-(CdC)HH-HF
                L5: CsJ-C=SHH-HF
            L4: CsJ-OneDeHH-HCl
                L5: CsJ-CtHH-HCl
                L5: CsJ-CbHH-HCl
                L5: CsJ-COHH-HCl
                L5: CsJ-CdHH-HCl
                    L6: CsJ-(CdC)HH-HCl
                L5: CsJ-C=SHH-HCl
            L4: CsJ-OneDeHH-HBr
                L5: CsJ-CtHH-HBr
                L5: CsJ-CbHH-HBr
                L5: CsJ-COHH-HBr
                L5: CsJ-CdHH-HBr
                    L6: CsJ-(CdC)HH-HBr
                L5: CsJ-C=SHH-HBr
            L4: CsJ-OneDeHH-FF
                L5: CsJ-CtHH-FF
                L5: CsJ-CbHH-FF
                L5: CsJ-COHH-FF
                L5: CsJ-CdHH-FF
                    L6: CsJ-(CdC)HH-FF
                L5: CsJ-C=SHH-FF
            L4: CsJ-OneDeHH-FCl
                L5: CsJ-CtHH-FCl
                L5: CsJ-CbHH-FCl
                L5: CsJ-COHH-FCl
                L5: CsJ-CdHH-FCl
                    L6: CsJ-(CdC)HH-FCl
                L5: CsJ-C=SHH-FCl
            L4: CsJ-OneDeHH-FBr
                L5: CsJ-CtHH-FBr
                L5: CsJ-CbHH-FBr
                L5: CsJ-COHH-FBr
                L5: CsJ-CdHH-FBr
                    L6: CsJ-(CdC)HH-FBr
                L5: CsJ-C=SHH-FBr
            L4: CsJ-OneDeHH-ClCl
                L5: CsJ-CtHH-ClCl
                L5: CsJ-CbHH-ClCl
                L5: CsJ-COHH-ClCl
                L5: CsJ-CdHH-ClCl
                    L6: CsJ-(CdC)HH-ClCl
                L5: CsJ-C=SHH-ClCl
            L4: CsJ-OneDeHH-ClBr
                L5: CsJ-CtHH-ClBr
                L5: CsJ-CbHH-ClBr
                L5: CsJ-COHH-ClBr
                L5: CsJ-CdHH-ClBr
                    L6: CsJ-(CdC)HH-ClBr
                L5: CsJ-C=SHH-ClBr
            L4: CsJ-OneDeHH-BrBr
                L5: CsJ-CtHH-BrBr
                L5: CsJ-CbHH-BrBr
                L5: CsJ-COHH-BrBr
                L5: CsJ-CdHH-BrBr
                    L6: CsJ-(CdC)HH-BrBr
                L5: CsJ-C=SHH-BrBr
            L4: CsJ-OneDeCsH-F
                L5: CsJ-CtCsH-F
                L5: CsJ-CbCsH-F
                L5: CsJ-COCsH-F
                L5: CsJ-CdCsH-F
                L5: CsJ-C=SCsH-F
            L4: CsJ-OneDeCsH-Cl
                L5: CsJ-CtCsH-Cl
                L5: CsJ-CbCsH-Cl
                L5: CsJ-COCsH-Cl
                L5: CsJ-CdCsH-Cl
                L5: CsJ-C=SCsH-Cl
            L4: CsJ-OneDeCsH-Br
                L5: CsJ-CtCsH-Br
                L5: CsJ-CbCsH-Br
                L5: CsJ-COCsH-Br
                L5: CsJ-CdCsH-Br
                L5: CsJ-C=SCsH-Br
            L4: CsJ-TwoDeH-F
            L4: CsJ-TwoDeH-Cl
            L4: CsJ-TwoDeH-Br
        L3: CdsJ=Cdd
        L3: CdsJ
            L4: CdsJ-/H_or_Val7/
                L5: CdsJ-H
                    L6: CdsJ-(CdCb)H
                L5: CdsJ-H-F
                    L6: CdsJ-(CdCb)H-F
                L5: CdsJ-H-Cl
                    L6: CdsJ-(CdCb)H-Cl
                L5: CdsJ-H-Br
                    L6: CdsJ-(CdCb)H-Br
            L4: CdsJ-Cs
            L4: CdsJ-Ct
            L4: CdsJ-Cb
            L4: CdsJ-CO
            L4: CdsJ-O2s
            L4: CdsJ-S2s
            L4: CdsJ-Cd
            L4: CdsJ-C=S
    L2: OJ
        L3: OJ_pri-H_or_Val7-1
            L4: OJ_pri
            L4: OJ_pri-F
            L4: OJ_pri-Cl
            L4: OJ_pri-Br
        L3: OJ_sec
            L4: OJ-NonDe
                L5: O_rad/NonDe
                    L6: OJ-Cs
                    L6: OJ-O2s
                L5: OJ-Ns
            L4: OJ-OneDe
                L5: O_rad/OneDe
                L5: OJ-OneDeN
                    L6: OJ-NO
        L3: O2b
    L2: SJ
        L3: SsJ
            L4: SsJ-/H_or_Val7/
                L5: SsJ-H
                L5: SsJ-H-F
                L5: SsJ-H-Cl
                L5: SsJ-H-Br
            L4: SsJ-Cs
            L4: SsJ-S2s
            L4: SsJ-OneDe
                L5: SsJ-Ct
                L5: SsJ-Cb
                L5: SsJ-CO
                L5: SsJ-Cd
                L5: SsJ-C=S
    L2: NJ
        L3: N3J
            L4: N3sJ
                L5: N/H_or_Val7/2J
                    L6: NH2J
                    L6: NH2J-HF
                    L6: NH2J-HCl
                    L6: NH2J-HBr
                    L6: NH2J-FF
                    L6: NH2J-FCl
                    L6: NH2J-FBr
                    L6: NH2J-ClCl
                    L6: NH2J-ClBr
                    L6: NH2J-BrBr
                L5: N3sJ-NonDe/H_or_Val7/
                    L6: N3sJ-NonDeH
                        L7: N3sJ-CsH
                        L7: N3sJ-OsH
                        L7: N3sJ-NsH
                    L6: N3sJ-NonDeH-F
                        L7: N3sJ-CsH-F
                        L7: N3sJ-OsH-F
                        L7: N3sJ-NsH-F
                    L6: N3sJ-NonDeH-Cl
                        L7: N3sJ-CsH-Cl
                        L7: N3sJ-OsH-Cl
                        L7: N3sJ-NsH-Cl
                    L6: N3sJ-NonDeH-Br
                        L7: N3sJ-CsH-Br
                        L7: N3sJ-OsH-Br
                        L7: N3sJ-NsH-Br
                L5: N3sJ-NonDe2
                L5: N3sJ-OneDe/H_or_Val7/
                    L6: N3sJ-OneDeH
                    L6: N3sJ-OneDeH-F
                    L6: N3sJ-OneDeH-Cl
                    L6: N3sJ-OneDeH-Br
                L5: N3sJ-OneDeCs
                L5: N3sJ-TwoDe
            L4: N3dJ
                L5: N3dJ_C
                L5: N3dJ_O
                L5: N3dJ_N
"""
)

forbidden(
    label = "O2d",
    group = 
"""
1 *1 O u0 {2,D}
2 *2 O u0 {1,D}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

