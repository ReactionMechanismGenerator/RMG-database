#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["RnCyclic"], ownReverse=False)

reverse = "Ring_Open_Endo_Cycli_Radical"
reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 0,
    label = "Rn",
    group = "OR{R3, R4, R5, R6plus}",
    kinetics = None,
)

entry(
    index = 1,
    label = "multiplebond_intra",
    group = 
"""
1 *2 R!H u0    {2,[D,T,B]}
2 *3 R!H u0 c0 {1,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "radadd_intra",
    group = 
"""
1 *1 R!H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R3",
    group = 
"""
1 *2 R!H u0 {2,[S,D,T,B]} {3,[D,T,B]}
2 *1 R!H u1 {1,[S,D,T,B]}
3 *3 R!H u0 c0 {1,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R3_cyclic",
    group = "OR{Rn0cx_beta, Rn1cx_alpha}",
    kinetics = None,
)

entry(
    index = 5,
    label = "Rn0cx_beta",
    group = "OR{Rn0c4_beta, Rn0c5_beta_short, Rn0c6_beta_short, Rn0c7_beta_short, Rn0c8_beta_short}",
    kinetics = None,
)

entry(
    index = 6,
    label = "Rn0c4_beta",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Rn0c5_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {3,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Rn0c6_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Rn0c6_beta_short_SBSS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,S}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D]}
3 *1 R!H u1 r1 {2,[S,D]} {6,S}
4    R!H ux r1 {1,S} {5,S}
5    R!H ux r1 {4,S} {6,B}
6    R!H ux r1 {3,S} {5,B}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Rn0c6_beta_short_SBSS_D",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {4,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D]}
3 *1 R!H u1 r1 {2,[S,D]} {6,S}
4    R!H ux r1 {1,S} {5,S}
5    R!H ux r1 {4,S} {6,B}
6    R!H ux r1 {3,S} {5,B}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Rn0c7_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Rn0c7_beta_short_SDSDS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,S}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {7,S}
4    R!H ux r1 {1,S} {5,D}
5    R!H ux r1 {4,D} {6,S}
6    R!H ux r1 {5,S} {7,D}
7    R!H ux r1 {3,S} {6,D}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Rn0c7_beta_short_SDSDS_D",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {4,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {7,S}
4    R!H ux r1 {1,S} {5,D}
5    R!H ux r1 {4,D} {6,S}
6    R!H ux r1 {5,S} {7,D}
7    R!H ux r1 {3,S} {6,D}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Rn0c8_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Rn1cx_alpha",
    group = "OR{Rn1c3_alpha_short, Rn1c4_alpha_short, Rn1c5_alpha_short, Rn1c6_alpha_short, Rn1c7_alpha_short, Rn1c8_alpha_short}",
    kinetics = None,
)

entry(
    index = 16,
    label = "Rn1c3_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Rn1c4_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Rn1c5_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Rn1c6_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {7,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Rn1c6ben_alpha_short",
    group = 
"""
1 *3 C   u0 c0 r1 {2,B} {4,B}
2 *2 C   u0 r1 {1,B} {3,S} {7,B}
3 *1 R!H u1 {2,S}
4    C   ux r1 {1,B} {5,B}
5    C   ux r1 {4,B} {6,B}
6    C   ux r1 {5,B} {7,B}
7    C   ux r1 {2,B} {6,B}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Rn1c7_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Rn1c8_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R3_linear",
    group = 
"""
1 *2 [Cd,Ct,CO,N,CS]       u0 {2,S} {3,[D,T]}
2 *1 R!H                   u1 {1,S}
3 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "R3_D",
    group = 
"""
1 *2 Cd       u0 {2,S} {3,D}
2 *1 R!H      u1 {1,S}
3 *3 [Cd,Cdd] u0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "R3_T",
    group = 
"""
1 *2 Ct  u0 {2,S} {3,T}
2 *1 R!H u1 {1,S}
3 *3 Ct  u0 c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R3_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 CO  u0 {1,S} {3,D}
3 *3 O2d u0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "R3_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 CS  u0 {1,S} {3,D}
3 *3 S2d u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "R4",
    group = 
"""
1 *4 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *2 R!H u0 {1,[S,D,T,B]} {4,[D,T,B]}
3 *1 R!H u1 {1,[S,D,T,B]}
4 *3 R!H u0 c0 {2,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "R4_cyclic",
    group = "OR{Rn0cx_gamma, Rn1cx_beta, Rn2cx_alpha, Rn0c5_beta_long, Rn1c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 30,
    label = "Rn0cx_gamma",
    group = "OR{Rn0c6_gamma, Rn0c7_gamma_short, Rn0c8_gamma_short}",
    kinetics = None,
)

entry(
    index = 31,
    label = "Rn0c6_gamma",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Rn0c7_gamma_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Rn0c7_gamma_short_SSDS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,S}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {7,S}
5    R!H ux r1 {1,S} {6,D}
6    R!H ux r1 {5,D} {7,S}
7    R!H ux r1 {4,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Rn0c7_gamma_short_SSDS_D",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {5,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {7,S}
5    R!H ux r1 {1,S} {6,D}
6    R!H ux r1 {5,D} {7,S}
7    R!H ux r1 {4,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Rn0c8_gamma_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "Rn1cx_beta",
    group = "OR{Rn1c4_beta, Rn1c5_beta_short, Rn1c6_beta_short, Rn1c7_beta_short, Rn1c8_beta_short}",
    kinetics = None,
)

entry(
    index = 37,
    label = "Rn1c4_beta",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Rn1c5_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "Rn1c6_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "Rn1c7_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Rn1c8_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Rn2cx_alpha",
    group = "OR{Rn2c3_alpha_short, Rn2c4_alpha_short, Rn2c5_alpha_short, Rn2c6_alpha_short, Rn2c7_alpha_short, Rn2c8_alpha_short}",
    kinetics = None,
)

entry(
    index = 43,
    label = "Rn2c3_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Rn2c4_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Rn2c5_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {7,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Rn2c6_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Rn2c7_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Rn2c8_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {10,[S,D,T,B]}
3  *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *1 R!H u1 r0 {3,[S,D,T,B]}
5     R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {2,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Rn0c5_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Rn1c3_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "R4_linear",
    group = 
"""
1 *4 R!H                   ux {2,S} {3,[S,D,T,B]}
2 *2 [Cd,Ct,CO,N,CS]       u0 {1,S} {4,[D,T]}
3 *1 R!H                   u1 {1,[S,D,T,B]}
4 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "R4_S",
    group = 
"""
1 *4 R!H                 u0 {2,S} {3,S}
2 *2 [Cd,Ct,CO,CS]       u0 {1,S} {4,[D,T]}
3 *1 R!H                 u1 {1,S}
4 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "R4_S_D",
    group = 
"""
1 *4 R!H      u0 {2,S} {3,S}
2 *2 Cd       u0 {1,S} {4,D}
3 *1 R!H      u1 {1,S}
4 *3 [Cd,Cdd] u0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "R4_Cs_RR_D",
    group = 
"""
1 *4 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd       u0 {1,S} {6,D}
3 *1 Cs       u1 {1,S}
4    R        u0 {1,S}
5    R        u0 {1,S}
6 *3 [Cd,Cdd] u0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "R4_Cs_HH_D",
    group = 
"""
1 *4 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd       u0 {1,S} {6,D}
3 *1 Cs       u1 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6 *3 [Cd,Cdd] u0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "R4_S_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 Ct  u0 {2,S} {4,T}
4 *3 Ct  u0 c0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "R4_S_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 CO  u0 {2,S} {4,D}
4 *3 O2d u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "R4_S_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 CS  u0 {2,S} {4,D}
4 *3 S2d u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "R4_D",
    group = 
"""
1 *1 Cd                  u1 {2,D}
2 *4 Cd                  u0 {1,D} {3,S}
3 *2 [Cd,Ct,CO,CS]       u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "R4_D_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "R4_D_T",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *2 Ct u0 {2,S} {4,T}
4 *3 Ct u0 c0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "R4_D_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *2 CO  u0 {2,S} {4,D}
4 *3 O2d u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "R4_D_CS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *2 CS  u0 {2,S} {4,D}
4 *3 S2d u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "R4_T",
    group = 
"""
1 *1 Ct                  u1 {2,T}
2 *4 Ct                  u0 {1,T} {3,S}
3 *2 [Cd,Ct,CO,CS]       u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "R4_T_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "R4_T_T",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T} {3,S}
3 *2 Ct u0 {2,S} {4,T}
4 *3 Ct u0 c0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "R4_T_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *2 CO  u0 {2,S} {4,D}
4 *3 O2d u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "R4_T_CS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *2 CS  u0 {2,S} {4,D}
4 *3 S2d u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "R5",
    group = 
"""
1 *5 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *4 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
3 *2 R!H u0 {1,[S,D,T,B]} {5,[D,T,B]}
4 *1 R!H u1 {2,[S,D,T,B]}
5 *3 R!H u0 c0 {3,[D,T,B]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
""",
)

entry(
    index = 70,
    label = "R5_cyclic",
    group = "OR{Rn0cx_delta, Rn1cx_gamma, Rn2cx_beta, Rn3cx_alpha, Rn0c6_beta_long, Rn1c4_alpha_long, Rn0c7_gamma_long, Rn1c5_beta_long, Rn2c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 71,
    label = "Rn0cx_delta",
    group = "OR{Rn0c8_delta, Rn0c10_delta_short}",
    kinetics = None,
)

entry(
    index = 72,
    label = "Rn0c8_delta",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Rn0c10_delta_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *1 R!H u1 r1 {4,[S,D,T,B]} {10,[S,D,T,B]}
6     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {5,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Rn0c10_delta_short_SSDSDS",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {6,S}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *1 R!H u1 r1 {4,[S,D,T,B]} {10,S}
6     R!H ux r1 {1,S} {7,D}
7     R!H ux r1 {6,D} {8,S}
8     R!H ux r1 {7,S} {9,D}
9     R!H ux r1 {8,D} {10,S}
10    R!H ux r1 {5,S} {9,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Rn0c10_delta_short_SSDSDS_D",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,D} {6,S}
2  *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *1 R!H u1 r1 {4,[S,D,T,B]} {10,S}
6     R!H ux r1 {1,S} {7,D}
7     R!H ux r1 {6,D} {8,S}
8     R!H ux r1 {7,S} {9,D}
9     R!H ux r1 {8,D} {10,S}
10    R!H ux r1 {5,S} {9,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Rn1cx_gamma",
    group = "OR{Rn1c6_gamma, Rn1c7_gamma_short, Rn1c8_gamma_short}",
    kinetics = None,
)

entry(
    index = 77,
    label = "Rn1c6_gamma",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Rn1c7_gamma_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {8,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Rn1c8_gamma_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {4,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Rn2cx_beta",
    group = "OR{Rn2c4_beta, Rn2c5_beta_short, Rn2c6_beta_short, Rn2c7_beta_short, Rn2c8_beta_short}",
    kinetics = None,
)

entry(
    index = 81,
    label = "Rn2c4_beta",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Rn2c5_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Rn2c5_beta_short_SS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,S} {7,[S,D,T,B]}
4 *4 R!H ux {3,S} {5,S}
5 *1 R!H u1 r0 {4,S}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Rn2c6_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Rn2c7_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Rn2c8_beta_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {10,[S,D,T,B]}
4  *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *1 R!H u1 r0 {4,[S,D,T,B]}
6     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {3,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Rn3cx_alpha",
    group = "OR{Rn3c3_alpha_short, Rn3c4_alpha_short, Rn3c5_alpha_short, Rn3c6_alpha_short, Rn3c7_alpha_short, Rn3c8_alpha_short}",
    kinetics = None,
)

entry(
    index = 88,
    label = "Rn3c3_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Rn3c4_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {7,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "Rn3c5_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "Rn3c6_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "Rn3c6ben_alpha_short",
    group = 
"""
1 *3 C   u0 c0 r1 {2,B} {6,B}
2 *2 C   u0 r1 {1,B} {3,[S,D,T,B]} {9,B}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    C   ux r1 {1,B} {7,B}
7    C   ux r1 {6,B} {8,B}
8    C   ux r1 {7,B} {9,B}
9    C   ux r1 {2,B} {8,B}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "Rn3c6ben_alpha_short_MSS",
    group = 
"""
1 *3 C   u0 c0 r1 {2,B} {6,B}
2 *2 C   u0 r1 {1,B} {3,S} {9,B}
3 *5 R!H ux {2,S} {4,S}
4 *4 R!H ux r0 {3,S} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    C   ux r1 {1,B} {7,B}
7    C   ux r1 {6,B} {8,B}
8    C   ux r1 {7,B} {9,B}
9    C   ux r1 {2,B} {8,B}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "Rn3c6ben_alpha_short_SDS",
    group = 
"""
1 *3 C   u0 c0 r1 {2,B} {6,B}
2 *2 C   u0 r1 {1,B} {3,S} {9,B}
3 *5 R!H ux {2,S} {4,D}
4 *4 R!H ux r0 {3,D} {5,S}
5 *1 R!H u1 r0 {4,S}
6    C   ux r1 {1,B} {7,B}
7    C   ux r1 {6,B} {8,B}
8    C   ux r1 {7,B} {9,B}
9    C   ux r1 {2,B} {8,B}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "Rn3c7_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {10,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *1 R!H u1 r0 {4,[S,D,T,B]}
6     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {2,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "Rn3c8_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {11,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *1 R!H u1 r0 {4,[S,D,T,B]}
6     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {2,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Rn0c6_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Rn0c6_beta_long_SS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,S}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {6,S}
6    R!H ux r1 {1,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "Rn0c6_beta_long_SS_D",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {6,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {6,S}
6    R!H ux r1 {1,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "Rn0c6_beta_long_SS_D_HH",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {6,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {6,S}
6    R!H ux r1 {1,S} {5,S} {7,S} {8,S}
7    H   u0 {6,S}
8    H   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "2-hydro-naphthalene",
    group = 
"""
1 *3 Cd u0 c0 r1 {2,D} {6,S}
2 *2 Cd u0 r1 {1,D} {3,S}
3 *5 Cb ux r1 {2,S} {4,B}
4 *4 Cb ux r1 {3,B} {5,S}
5 *1 C  u1 r1 {4,S} {6,S}
6    C  ux r1 {1,S} {5,S} {7,S} {8,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "Rn0c6_beta_long_SS_D_RH",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {6,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {6,S}
6    R!H ux r1 {1,S} {5,S} {7,S} {8,S}
7    R!H u0 {6,S}
8    H   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Rn0c6_beta_long_SS_D_RR",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {6,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {6,S}
6    R!H ux r1 {1,S} {5,S} {7,S} {8,S}
7    R!H u0 {6,S}
8    R!H u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Rn1c4_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "Rn0c7_gamma_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {7,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "Rn0c7_gamma_long_SSS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,S}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {7,S}
6    R!H ux r1 {1,S} {7,S}
7    R!H ux r1 {5,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Rn0c7_gamma_long_SSS_D",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {6,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {7,S}
6    R!H ux r1 {1,S} {7,S}
7    R!H ux r1 {5,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "Rn0c7_gamma_long_SDS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,S}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {7,S}
6    R!H ux r1 {1,S} {7,D}
7    R!H ux r1 {5,S} {6,D}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "Rn0c7_gamma_long_SDS_D",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {6,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {7,S}
6    R!H ux r1 {1,S} {7,D}
7    R!H ux r1 {5,S} {6,D}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "Rn1c5_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Rn2c3_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "R5_linear",
    group = 
"""
1 *5 R!H                   ux {2,[S,D,T,B]} {3,[S,D]}
2 *4 R!H                   ux {1,[S,D,T,B]} {4,[S,D,T,B]}
3 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {1,[S,D]} {5,[D,T]}
4 *1 R!H                   u1 {2,[S,D,T,B]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {3,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
""",
)

entry(
    index = 113,
    label = "R5_cyc5_beta",
    group = 
"""
1 *1 R!H                   u1 r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
2 *4 R!H                   ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H                   ux r1 {2,[S,D,T,B]} {4,[S,D]} {7,[S,D,T,B]}
4 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {3,[S,D]} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {4,[D,T]}
6    R!H                   ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H                   ux r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
""",
)

entry(
    index = 114,
    label = "R5_SS",
    group = 
"""
1 *5 R!H                   u0 {2,S} {3,S}
2 *4 R!H                   u0 {1,S} {4,S}
3 *2 [Cd,Ct,CO,N,CS]       u0 {1,S} {5,[D,T]}
4 *1 R!H                   u1 {2,S}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {3,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
""",
)

entry(
    index = 115,
    label = "R5_SS_D",
    group = 
"""
1 *5 R!H      u0 {2,S} {3,S}
2 *4 R!H      u0 {1,S} {4,S}
3 *2 Cd       u0 {1,S} {5,D}
4 *1 R!H      u1 {2,S}
5 *3 [Cd,Cdd] u0 c0 {3,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 116,
    label = "R5_CsCs_RR_D",
    group = 
"""
1 *5 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Cd       u0 {1,S} {9,D}
4    R        u0 {1,S}
5    R        u0 {1,S}
6 *1 Cs       u1 {2,S}
7    R        u0 {2,S}
8    R        u0 {2,S}
9 *3 [Cd,Cdd] u0 c0 {3,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 117,
    label = "R5_CsCs_RH_D",
    group = 
"""
1 *5 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Cd       u0 {1,S} {9,D}
4    R        u0 {1,S}
5    H        u0 {1,S}
6 *1 Cs       u1 {2,S}
7    R        u0 {2,S}
8    H        u0 {2,S}
9 *3 [Cd,Cdd] u0 c0 {3,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 118,
    label = "R5_CsCs_HH_D",
    group = 
"""
1 *5 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 Cd       u0 {1,S} {9,D}
4    H        u0 {1,S}
5    H        u0 {1,S}
6 *1 Cs       u1 {2,S}
7    H        u0 {2,S}
8    H        u0 {2,S}
9 *3 [Cd,Cdd] u0 c0 {3,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 119,
    label = "R5_SS_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 120,
    label = "R5_SS_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 121,
    label = "R5_SS_CS",
    group = 
"""
1 *5 R!H u0 {2,S} {3,S}
2 *4 R!H u0 {1,S} {4,S}
3 *2 CS  u0 {1,S} {5,D}
4 *1 R!H u1 {2,S}
5 *3 S2d u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Cs-R5_SS_CS",
    group = 
"""
1 *4 R!H u0 {2,S} {3,S}
2 *5 R!H u0 {1,S} {4,S}
3 *1 Cs  u1 {1,S} {6,S}
4 *2 CS  u0 {2,S} {5,D}
5 *3 S2d u0 c0 {4,D}
6    Cs  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "H2-R5_SS_CS",
    group = 
"""
1 *1 Cs  u1 {2,S} {5,S} {6,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 {3,S} {7,D}
5    H   u0 {1,S}
6    H   u0 {1,S}
7 *3 S2d u0 c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "R5_SM",
    group = 
"""
1 *5 [Cd,Ct,Cb]            u0 {2,[D,T,B]} {3,S}
2 *4 [Cd,Ct,Cb]            u0 {1,[D,T,B]} {4,S}
3 *2 [Cd,Ct,CO,N,CS]       u0 {1,S} {5,[D,T]}
4 *1 R!H                   u1 {2,S}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "R5_SD",
    group = 
"""
1 *5 Cd                    u0 {2,D} {3,S}
2 *4 Cd                    u0 {1,D} {4,S}
3 *2 [Cd,Ct,CO,N,CS]       u0 {1,S} {5,[D,T]}
4 *1 R!H                   u1 {2,S}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {3,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
""",
)

entry(
    index = 126,
    label = "R5_SD_D",
    group = 
"""
1 *5 Cd       u0 {2,D} {3,S}
2 *4 Cd       u0 {1,D} {4,S}
3 *2 Cd       u0 {1,S} {5,D}
4 *1 R!H      u1 {2,S}
5 *3 [Cd,Cdd] u0 c0 {3,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 127,
    label = "R5_SD_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 128,
    label = "R5_SD_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 129,
    label = "R5_SD_CS",
    group = 
"""
1 *5 Cd  u0 {2,D} {3,S}
2 *4 Cd  u0 {1,D} {4,S}
3 *2 CS  u0 {1,S} {5,D}
4 *1 R!H u1 {2,S}
5 *3 S2d u0 c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "R5_ST",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 Ct                    u0 {1,S} {3,T}
3 *5 Ct                    u0 {2,T} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
""",
)

entry(
    index = 131,
    label = "R5_ST_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 Ct       u0 {1,S} {3,T}
3 *5 Ct       u0 {2,T} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 132,
    label = "R5_ST_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 133,
    label = "R5_ST_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 134,
    label = "R5_ST_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 CS  u0 {3,S} {5,D}
5 *3 S2d u0 c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "R5_SB",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 Cb                    u0 {1,S} {3,B}
3 *5 Cb                    u0 {2,B} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "R5_MS",
    group = 
"""
1 *5 R!H                   u0 {2,S} {3,[S,D]}
2 *4 [Cd,Ct,Cb]            u0 {1,S} {4,[D,T,B]}
3 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {1,[S,D]} {5,[D,T]}
4 *1 [Cd,Ct,Cb]            u1 {2,[D,T,B]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "R5_DS",
    group = 
"""
1 *5 R!H                   u0 {2,S} {3,S}
2 *4 Cd                    u0 {1,S} {4,D}
3 *2 [Cd,Ct,CO,N,CS]       u0 {1,S} {5,[D,T]}
4 *1 Cd                    u1 {2,D}
5 *3 [Cd,Cdd,Ct,O2d,S2d,N] u0 c0 {3,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
""",
)

entry(
    index = 138,
    label = "R5_DS_D",
    group = 
"""
1 *5 R!H      u0 {2,S} {3,S}
2 *4 Cd       u0 {1,S} {4,D}
3 *2 Cd       u0 {1,S} {5,D}
4 *1 Cd       u1 {2,D}
5 *3 [Cd,Cdd] u0 c0 {3,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 139,
    label = "R5_DS_T",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 140,
    label = "R5_DS_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 141,
    label = "R5_DS_CS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 {3,S} {5,D}
5 *3 S2d u0 c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "R5_TS",
    group = 
"""
1 *1 Ct                    u1 {2,T}
2 *4 Ct                    u0 {1,T} {3,S}
3 *5 R!H                   u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
""",
)

entry(
    index = 143,
    label = "R5_TS_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 144,
    label = "R5_TS_T",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 145,
    label = "R5_TS_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 146,
    label = "R5_BS",
    group = 
"""
1 *1 Cb                    u1 {2,B}
2 *4 Cb                    u0 {1,B} {3,S}
3 *5 R!H                   u0 {2,S} {4,[S,D]}
4 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {3,[S,D]} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "R5_MM",
    group = 
"""
1 *1 [Cd,Cb]               u1 {2,[D,B]}
2 *4 [Cdd,Cbf]             u0 {1,[D,B]} {3,[D,B]}
3 *5 [Cd,Cb]               u0 {2,[D,B]} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "R6plus",
    group = "OR{R6, R7, R8, R9, R10, R11, R12, R13}",
    kinetics = None,
)

entry(
    index = 149,
    label = "R6",
    group = 
"""
1 *6 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *5 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
3 *4 R!H ux {1,[S,D,T,B]} {5,[S,D,T,B]}
4 *2 R!H u0 {2,[S,D,T,B]} {6,[D,T,B]}
5 *1 R!H u1 {3,[S,D,T,B]}
6 *3 R!H u0 c0 {4,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "R6_cyclic",
    group = "OR{Rn0cx_epsilon, Rn1cx_delta, Rn2cx_gamma, Rn3cx_beta, Rn4cx_alpha, Rn0c7_beta_long, Rn1c5_alpha_long, Rn0c8_gamma_long, Rn1c6_beta_long, Rn2c4_alpha_long, Rn1c7_gamma_long, Rn2c5_beta_long, Rn3c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 151,
    label = "Rn0cx_epsilon",
    group = "OR{Rn0c10_epsilon}",
    kinetics = None,
)

entry(
    index = 152,
    label = "Rn0c10_epsilon",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r1 {5,[S,D,T,B]} {10,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {6,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Rn0c10_epsilon_SDSDS",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {7,S}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r1 {5,[S,D,T,B]} {10,S}
7     R!H ux r1 {1,S} {8,D}
8     R!H ux r1 {7,D} {9,S}
9     R!H ux r1 {8,S} {10,D}
10    R!H ux r1 {6,S} {9,D}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "Rn0c10_epsilon_SDSDS_D",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,D} {7,S}
2  *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r1 {5,[S,D,T,B]} {10,S}
7     R!H ux r1 {1,S} {8,D}
8     R!H ux r1 {7,D} {9,S}
9     R!H ux r1 {8,S} {10,D}
10    R!H ux r1 {6,S} {9,D}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Rn1cx_delta",
    group = "OR{Rn1c8_delta}",
    kinetics = None,
)

entry(
    index = 156,
    label = "Rn1c8_delta",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {5,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Rn2cx_gamma",
    group = "OR{Rn2c6_gamma, Rn2c7_gamma_short, Rn2c8_gamma_short}",
    kinetics = None,
)

entry(
    index = 158,
    label = "Rn2c6_gamma",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {8,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "Rn2c7_gamma_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {4,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Rn2c8_gamma_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {10,[S,D,T,B]}
5  *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {4,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Rn3cx_beta",
    group = "OR{Rn3c4_beta, Rn3c5_beta_short, Rn3c6_beta_short, Rn3c7_beta_short, Rn3c8_beta_short}",
    kinetics = None,
)

entry(
    index = 162,
    label = "Rn3c4_beta",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "Rn3c5_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Rn3c6_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "Rn3c7_beta_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {10,[S,D,T,B]}
4  *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {3,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Rn3c8_beta_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {11,[S,D,T,B]}
4  *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {3,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Rn4cx_alpha",
    group = "OR{Rn4c3_alpha_short, Rn4c4_alpha_short, Rn4c5_alpha_short, Rn4c6_alpha_short, Rn4c7_alpha_short, Rn4c8_alpha_short}",
    kinetics = None,
)

entry(
    index = 168,
    label = "Rn4c3_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {7,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "Rn4c4_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "Rn4c5_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "Rn4c6_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {10,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {2,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "Rn4c6ben_alpha_short",
    group = 
"""
1  *3 C u0 c0 r1 {2,B} {7,B}
2  *2 C u0 r1 {1,B} {3,[S,D,T,B]} {10,B}
3  *5 C ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 C ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 C ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 C u1 r0 {5,[S,D,T,B]}
7     C ux r1 {1,B} {8,B}
8     C ux r1 {7,B} {9,B}
9     C ux r1 {8,B} {10,B}
10    C ux r1 {2,B} {9,B}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "Rn4c6ben_alpha_short_SDSS",
    group = 
"""
1  *3 C u0 c0 r1 {2,B} {7,B}
2  *2 C u0 r1 {1,B} {3,S} {10,B}
3  *5 C ux {2,S} {4,S}
4  *6 C ux r0 {3,S} {5,D}
5  *4 C ux r0 {4,D} {6,S}
6  *1 C u1 r0 {5,S}
7     C ux r1 {1,B} {8,B}
8     C ux r1 {7,B} {9,B}
9     C ux r1 {8,B} {10,B}
10    C ux r1 {2,B} {9,B}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "Rn4c6ben_alpha_short_DSDS",
    group = 
"""
1  *3 C u0 c0 r1 {2,B} {7,B}
2  *2 C u0 r1 {1,B} {3,S} {10,B}
3  *5 C ux {2,S} {4,D}
4  *6 C ux r0 {3,D} {5,S}
5  *4 C ux r0 {4,S} {6,D}
6  *1 C u1 r0 {5,D}
7     C ux r1 {1,B} {8,B}
8     C ux r1 {7,B} {9,B}
9     C ux r1 {8,B} {10,B}
10    C ux r1 {2,B} {9,B}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "Rn4c7_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {11,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {2,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "Rn4c8_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {12,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {10,[S,D,T,B]} {12,[S,D,T,B]}
12    R!H ux r1 {2,[S,D,T,B]} {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "Rn0c7_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "Rn0c7_beta_long_SS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,S}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r1 {5,[S,D,T,B]} {7,S}
7    R!H ux r1 {1,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "Rn0c7_beta_long_SS_D",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,D} {7,S}
2 *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r1 {5,[S,D,T,B]} {7,S}
7    R!H ux r1 {1,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "Rn1c5_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "Rn1c5_alpha_long_indene",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D]}
2 *2 R!H u0 r1 {1,[D,T]} {3,S}
3 *5 R!H ux r1 {2,S} {4,B}
4 *6 R!H ux r1 {3,B} {5,S}
5 *4 R!H ux r1 {1,[S,D]} {4,S} {6,[S,D]}
6 *1 R!H u1 {5,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "Rn0c8_gamma_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r1 {5,[S,D,T,B]} {8,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "Rn1c6_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Rn2c4_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Rn1c7_gamma_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Rn2c5_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "Rn2c5_beta_long_SS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,S} {7,[S,D,T,B]}
5 *4 R!H ux {4,S} {6,S}
6 *1 R!H u1 r0 {5,S}
7    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Rn3c3_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "R6_linear",
    group = 
"""
1 *6 R!H                   ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *5 R!H                   ux {1,[S,D,T,B]} {4,[S,D]}
3 *4 R!H                   ux {1,[S,D,T,B]} {5,[S,D,T,B]}
4 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {2,[S,D]} {6,[D,T]}
5 *1 R!H                   u1 {3,[S,D,T,B]}
6 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "R6_RSR",
    group = 
"""
1 *6 R!H                   u0 {2,[S,D,T,B]} {3,S}
2 *5 R!H                   u0 {1,[S,D,T,B]} {4,S}
3 *4 R!H                   u0 {1,S} {5,[S,D,T,B]}
4 *2 [Cd,Ct,CO,N,CS]       u0 {2,S} {6,[D,T]}
5 *1 R!H                   u1 {3,[S,D,T,B]}
6 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "R6_SSR",
    group = 
"""
1 *6 R!H                 u0 {2,[S,D,T,B]} {3,S}
2 *5 R!H                 u0 {1,[S,D,T,B]} {4,S}
3 *4 R!H                 u0 {1,S} {5,S}
4 *2 [Cd,Ct,CO,CS]       u0 {2,S} {6,[D,T]}
5 *1 R!H                 u1 {3,S}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "R6_SSS",
    group = 
"""
1 *6 R!H                 u0 {2,S} {3,S}
2 *5 R!H                 u0 {1,S} {4,S}
3 *4 R!H                 u0 {1,S} {5,S}
4 *2 [Cd,Ct,CO,CS]       u0 {2,S} {6,[D,T]}
5 *1 R!H                 u1 {3,S}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "R6_SSS_D",
    group = 
"""
1 *6 R!H      u0 {2,S} {3,S}
2 *5 R!H      u0 {1,S} {4,S}
3 *4 R!H      u0 {1,S} {5,S}
4 *2 Cd       u0 {2,S} {6,D}
5 *1 R!H      u1 {3,S}
6 *3 [Cd,Cdd] u0 c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "R6_CsCsCs_RR_D",
    group = 
"""
1  *6 Cs       u0 {2,S} {3,S} {5,S} {6,S}
2  *5 Cs       u0 {1,S} {4,S} {7,S} {8,S}
3  *4 Cs       u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Cd       u0 {2,S} {12,D}
5     R        u0 {1,S}
6     R        u0 {1,S}
7     R        u0 {2,S}
8     R        u0 {2,S}
9  *1 Cs       u1 {3,S}
10    R        u0 {3,S}
11    R        u0 {3,S}
12 *3 [Cd,Cdd] u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 6 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 195,
    label = "R6_CsCsCs_RH_D",
    group = 
"""
1  *6 Cs       u0 {2,S} {3,S} {5,S} {6,S}
2  *5 Cs       u0 {1,S} {4,S} {7,S} {8,S}
3  *4 Cs       u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Cd       u0 {2,S} {12,D}
5     R        u0 {1,S}
6     H        u0 {1,S}
7     R        u0 {2,S}
8     H        u0 {2,S}
9  *1 Cs       u1 {3,S}
10    R        u0 {3,S}
11    H        u0 {3,S}
12 *3 [Cd,Cdd] u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 6 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 196,
    label = "R6_CsCsCs_HH_D",
    group = 
"""
1  *6 Cs       u0 {2,S} {3,S} {5,S} {6,S}
2  *5 Cs       u0 {1,S} {4,S} {7,S} {8,S}
3  *4 Cs       u0 {1,S} {9,S} {10,S} {11,S}
4  *2 Cd       u0 {2,S} {12,D}
5     H        u0 {1,S}
6     H        u0 {1,S}
7     H        u0 {2,S}
8     H        u0 {2,S}
9  *1 Cs       u1 {3,S}
10    H        u0 {3,S}
11    H        u0 {3,S}
12 *3 [Cd,Cdd] u0 c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 6 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 197,
    label = "R6_SSS_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 {4,S} {6,T}
6 *3 Ct  u0 c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "R6_SSS_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 {4,S} {6,D}
6 *3 O2d u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "R6_SSM",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 R!H                 u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb]          u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]          u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "R6_SSM_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "R6_SSM_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "R6_SSM_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 O2d        u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "R6_SSM_CS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CS         u0 {4,S} {6,D}
6 *3 S2d        u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "R6_MSR",
    group = 
"""
1 *6 R!H                 u0 {2,[S,D,T,B]} {3,S}
2 *5 R!H                 u0 {1,[S,D,T,B]} {4,S}
3 *4 [Cd,Ct,Cb]          u0 {1,S} {5,[D,T,B]}
4 *2 [Cd,Ct,CO,CS]       u0 {2,S} {6,[D,T]}
5 *1 [Cd,Ct,Cb]          u1 {3,[D,T,B]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "R6_DSR",
    group = 
"""
1 *6 R!H                 u0 {2,[S,D,T,B]} {3,S}
2 *5 R!H                 u0 {1,[S,D,T,B]} {4,S}
3 *4 Cd                  u0 {1,S} {5,D}
4 *2 [Cd,Ct,CO,CS]       u0 {2,S} {6,[D,T]}
5 *1 Cd                  u1 {3,D}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "R6_DSS",
    group = 
"""
1 *6 R!H                 u0 {2,S} {3,S}
2 *5 R!H                 u0 {1,S} {4,S}
3 *4 Cd                  u0 {1,S} {5,D}
4 *2 [Cd,Ct,CO,CS]       u0 {2,S} {6,[D,T]}
5 *1 Cd                  u1 {3,D}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "R6_DSS_D",
    group = 
"""
1 *6 R!H      u0 {2,S} {3,S}
2 *5 R!H      u0 {1,S} {4,S}
3 *4 Cd       u0 {1,S} {5,D}
4 *2 Cd       u0 {2,S} {6,D}
5 *1 Cd       u1 {3,D}
6 *3 [Cd,Cdd] u0 c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "R6_DSS_T",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 {4,S} {6,T}
6 *3 Ct  u0 c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "R6_DSS_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 {4,S} {6,D}
6 *3 O2d u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "R6_DSM",
    group = 
"""
1 *1 Cd                  u1 {2,D}
2 *4 Cd                  u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb]          u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]          u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "R6_DSM_D",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "R6_DSB_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *6 Cb       u0 {2,S} {4,B}
4 *5 Cb       u0 {3,B} {5,S}
5 *2 Cd       u0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "R6_DSM_T",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "R6_DSB_T",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *6 Cb u0 {2,S} {4,B}
4 *5 Cb u0 {3,B} {5,S}
5 *2 Ct u0 {4,S} {6,T}
6 *3 Ct u0 c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "R6_DSM_CO",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 O2d        u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "R6_DSM_CS",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CS         u0 {4,S} {6,D}
6 *3 S2d        u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "R6_TSR",
    group = 
"""
1 *1 Ct                  u1 {2,T}
2 *4 Ct                  u0 {1,T} {3,S}
3 *6 R!H                 u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                 u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "R6_TSS",
    group = 
"""
1 *1 Ct                  u1 {2,T}
2 *4 Ct                  u0 {1,T} {3,S}
3 *6 R!H                 u0 {2,S} {4,S}
4 *5 R!H                 u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "R6_TSS_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "R6_TSS_T",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 {4,S} {6,T}
6 *3 Ct  u0 c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "R6_TSS_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 {4,S} {6,D}
6 *3 O2d u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "R6_TSS_CS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CS  u0 {4,S} {6,D}
6 *3 S2d u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "R6_TSM",
    group = 
"""
1 *1 Ct                  u1 {2,T}
2 *4 Ct                  u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb]          u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]          u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "R6_TSM_D",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "R6_TSM_T",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "R6_TSM_CO",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 O2d        u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "R6_TSM_CS",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CS         u0 {4,S} {6,D}
6 *3 S2d        u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "R6_MSR_D",
    group = 
"""
1 *1 [Cd,Ct,Cb]          u1 {2,[D,T,B]}
2 *4 [Cd,Ct,Cb]          u0 {1,[D,T,B]} {3,S}
3 *6 R!H                 u0 {2,S} {4,D}
4 *5 R!H                 u0 {3,D} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "R6_SMS",
    group = 
"""
1 *6 [Cd,Ct,Cb]            u0 {2,S} {3,[D,T,B]}
2 *5 R!H                   u0 {1,S} {4,[S,D]}
3 *4 [Cd,Ct,Cb]            u0 {1,[D,T,B]} {5,S}
4 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {2,[S,D]} {6,[D,T]}
5 *1 R!H                   u1 {3,S}
6 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "R6_SMS_D",
    group = 
"""
1 *6 [Cd,Ct,Cb] u0 {2,S} {3,[D,T,B]}
2 *5 R!H        u0 {1,S} {4,[S,D]}
3 *4 [Cd,Ct,Cb] u0 {1,[D,T,B]} {5,S}
4 *2 [Cd,Cdd]   u0 {2,[S,D]} {6,D}
5 *1 R!H        u1 {3,S}
6 *3 [Cd,Cdd]   u0 c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 231,
    label = "R6_SMS(M)S_D",
    group = 
"""
1 *5 R!H        u0 {2,S} {3,S} {5,[D,T,B]}
2 *6 [Cd,Ct,Cb] u0 {1,S} {4,[D,T,B]}
3 *2 Cd         u0 {1,S} {6,D}
4 *4 [Cd,Ct,Cb] u0 {2,[D,T,B]} {7,S}
5    R!H        u0 {1,[D,T,B]}
6 *3 [Cd,Cdd]   u0 c0 {3,D}
7 *1 R!H        u1 {4,S}
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "R6_SDS_D",
    group = 
"""
1 *6 Cd       u0 {2,S} {3,D}
2 *5 R!H      u0 {1,S} {4,[S,D]}
3 *4 Cd       u0 {1,D} {5,S}
4 *2 [Cd,Cdd] u0 {2,[S,D]} {6,D}
5 *1 R!H      u1 {3,S}
6 *3 [Cd,Cdd] u0 c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "R6_SBS_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,B}
3 *6 [Cd,Ct,Cb] u0 {2,B} {4,S}
4 *5 R!H        u0 {3,S} {5,[S,D]}
5 *2 [Cd,Cdd]   u0 {4,[S,D]} {6,D}
6 *3 [Cd,Cdd]   u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "R6_SMS_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "R6_SMS_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 O2d        u0 c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "R6_SMM",
    group = 
"""
1 *6 [Cdd,Cbf]       u0 {2,[D,B]} {3,[D,B]}
2 *5 [Cd,Cb]         u0 {1,[D,B]} {4,S}
3 *4 [Cd,Cb]         u0 {1,[D,B]} {5,S}
4 *2 [Cd,Ct,CO,CS]   u0 {2,S} {6,[D,T]}
5 *1 R!H             u1 {3,S}
6 *3 [Cd,Ct,O2d,S2d] u0 c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "R7",
    group = 
"""
1 *7 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *6 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
3 *5 R!H ux {1,[S,D,T,B]} {5,[S,D,T,B]}
4 *4 R!H ux {2,[S,D,T,B]} {6,[S,D,T,B]}
5 *2 R!H u0 {3,[S,D,T,B]} {7,[D,T,B]}
6 *1 R!H u1 {4,[S,D,T,B]}
7 *3 R!H u0 c0 {5,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 238,
    label = "R7_cyclic",
    group = "OR{Rn2cx_delta, Rn3cx_gamma, Rn4cx_beta, Rn5cx_alpha, Rn0c8_beta_long, Rn1c6_alpha_long, Rn1c7_beta_long, Rn2c5_alpha_long, Rn0c10_delta_long, Rn1c8_gamma_long, Rn2c6_beta_long, Rn3c4_alpha_long, Rn2c7_gamma_long, Rn3c5_beta_long, Rn4c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 239,
    label = "Rn2cx_delta",
    group = "OR{Rn2c8_delta}",
    kinetics = None,
)

entry(
    index = 240,
    label = "Rn2c8_delta",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {10,[S,D,T,B]}
6  *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {5,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "Rn3cx_gamma",
    group = "OR{Rn3c6_gamma, Rn3c7_gamma_short, Rn3c8_gamma_short}",
    kinetics = None,
)

entry(
    index = 242,
    label = "Rn3c6_gamma",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {4,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "Rn3c7_gamma_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {10,[S,D,T,B]}
5  *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {4,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "Rn3c8_gamma_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {11,[S,D,T,B]}
5  *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {4,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "Rn4cx_beta",
    group = "OR{Rn4c4_beta, Rn4c5_beta_short, Rn4c6_beta_short, Rn4c7_beta_short, Rn4c8_beta_short}",
    kinetics = None,
)

entry(
    index = 246,
    label = "Rn4c4_beta",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "Rn4c5_beta_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "Rn4c6_beta_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {10,[S,D,T,B]}
4  *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {3,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "Rn4c7_beta_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {11,[S,D,T,B]}
4  *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {3,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "Rn4c8_beta_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {12,[S,D,T,B]}
4  *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {10,[S,D,T,B]} {12,[S,D,T,B]}
12    R!H ux r1 {3,[S,D,T,B]} {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "Rn5cx_alpha",
    group = "OR{Rn5c3_alpha_short, Rn5c4_alpha_short, Rn5c5_alpha_short, Rn5c6_alpha_short, Rn5c7_alpha_short, Rn5c8_alpha_short}",
    kinetics = None,
)

entry(
    index = 252,
    label = "Rn5c3_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "Rn5c4_alpha_short",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "Rn5c5_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {10,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {2,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "Rn5c6_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {11,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {2,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "Rn5c7_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {12,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {10,[S,D,T,B]} {12,[S,D,T,B]}
12    R!H ux r1 {2,[S,D,T,B]} {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "Rn5c8_alpha_short",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {13,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {10,[S,D,T,B]} {12,[S,D,T,B]}
12    R!H ux r1 {11,[S,D,T,B]} {13,[S,D,T,B]}
13    R!H ux r1 {2,[S,D,T,B]} {12,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "Rn0c8_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 259,
    label = "Rn1c6_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "Rn1c6_alpha_long_loop",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {6,S}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r1 {4,[S,D,T,B]} {6,S}
6  *4 R!H ux r1 {1,S} {5,S} {7,S} {10,S}
7  *1 R!H u1 r1 {6,S} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {6,S} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "Rn1c7_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "Rn2c5_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "Rn2c5_alpha_long_SS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,S}
6 *4 R!H ux {5,S} {7,S}
7 *1 R!H u1 r0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "Rn2c5_alpha_long_DS",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,S}
6 *4 R!H ux {5,S} {7,D}
7 *1 R!H u1 r0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "Rn0c10_delta_long",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r1 {6,[S,D,T,B]} {10,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "Rn0c10_delta_long_SSDS",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {8,S}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r1 {6,[S,D,T,B]} {10,S}
8     R!H ux r1 {1,S} {9,D}
9     R!H ux r1 {8,D} {10,S}
10    R!H ux r1 {7,S} {9,S}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "Rn0c10_delta_long_SSDS_D",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,D} {8,S}
2  *2 R!H u0 r1 {1,D} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r1 {6,[S,D,T,B]} {10,S}
8     R!H ux r1 {1,S} {9,D}
9     R!H ux r1 {8,D} {10,S}
10    R!H ux r1 {7,S} {9,S}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "Rn1c8_gamma_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "Rn2c6_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "Rn3c4_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "Rn2c7_gamma_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {5,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "Rn3c5_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {8,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "Rn4c3_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "R7_linear",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H                   ux {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO,N,CS]       u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "R7_SDSD_D",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 R!H                   ux {1,S} {3,D}
3 *6 R!H                   ux {2,D} {4,S}
4 *7 R!H                   ux {3,S} {5,D}
5 *5 R!H                   ux {4,D} {6,S}
6 *2 [Cd,Ct,CO,N,CS]       u0 {5,S} {7,D}
7 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "R8",
    group = 
"""
1 *7 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *8 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
3 *6 R!H ux {1,[S,D,T,B]} {5,[S,D,T,B]}
4 *5 R!H ux {2,[S,D,T,B]} {6,[S,D,T,B]}
5 *4 R!H ux {3,[S,D,T,B]} {7,[S,D,T,B]}
6 *2 R!H u0 {4,[S,D,T,B]} {8,[D,T,B]}
7 *1 R!H u1 {5,[S,D,T,B]}
8 *3 R!H u0 c0 {6,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "R8_cyclic",
    group = "OR{Rn1c7_alpha_long, Rn1c8_beta_long, Rn2c6_alpha_long, Rn2c7_beta_long, Rn3c5_alpha_long, Rn2c8_gamma_long, Rn3c6_beta_long, Rn4c4_alpha_long, Rn3c7_gamma_long, Rn4c5_beta_long, Rn5c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 278,
    label = "Rn1c7_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "Rn1c8_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {9,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {9,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
9    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "Rn2c6_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "Rn2c7_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {9,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
9    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "Rn3c5_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "Rn2c8_gamma_long",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {9,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {10,[S,D,T,B]}
7  *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *1 R!H u1 r0 {7,[S,D,T,B]}
9     R!H ux r1 {1,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {6,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 284,
    label = "Rn3c6_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {9,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
6 *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
9    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "Rn4c4_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 286,
    label = "Rn3c7_gamma_long",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {9,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {10,[S,D,T,B]}
6  *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *1 R!H u1 r0 {7,[S,D,T,B]}
9     R!H ux r1 {1,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {5,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "Rn4c5_beta_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {9,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5 *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
9    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "Rn5c3_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "R8_linear",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H                   ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H                   ux {5,[S,D,T,B]} {7,S}
7 *2 [Cd,Ct,CO,N,CS]       u0 {6,S} {8,[D,T]}
8 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {7,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "R9",
    group = 
"""
1 *7 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
2 *8 R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *9 R!H ux {2,[S,D,T,B]} {5,[S,D,T,B]}
4 *6 R!H ux {1,[S,D,T,B]} {6,[S,D,T,B]}
5 *5 R!H ux {3,[S,D,T,B]} {7,[S,D,T,B]}
6 *4 R!H ux {4,[S,D,T,B]} {8,[S,D,T,B]}
7 *2 R!H u0 {5,[S,D,T,B]} {9,[D,T,B]}
8 *1 R!H u1 {6,[S,D,T,B]}
9 *3 R!H u0 c0 {7,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "R9_cyclic",
    group = "OR{Rn1c8_alpha_long, Rn2c7_alpha_long, Rn2c8_beta_long, Rn3c6_alpha_long, Rn3c7_beta_long, Rn3c8_gamma_long, Rn4c5_alpha_long, Rn4c6_beta_long, Rn5c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 292,
    label = "Rn1c8_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "Rn2c7_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "Rn2c8_beta_long",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {10,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *6 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {10,[S,D,T,B]}
8  *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
10    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "Rn3c6_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "Rn3c7_beta_long",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {10,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {10,[S,D,T,B]}
7  *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
10    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "Rn3c8_gamma_long",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {10,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {11,[S,D,T,B]}
7  *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
10    R!H ux r1 {1,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {6,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "Rn4c5_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "Rn4c6_beta_long",
    group = 
"""
1  *3 R!H u0 c0 r1 {2,[D,T]} {10,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {10,[S,D,T,B]}
6  *7 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *6 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
10    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "Rn5c4_alpha_long",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "R9_linear",
    group = 
"""
1 *7 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
2 *8 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *9 R!H                   ux {2,[S,D,T,B]} {5,[S,D,T,B]}
4 *6 R!H                   ux {1,[S,D,T,B]} {6,[S,D,T,B]}
5 *5 R!H                   ux {3,[S,D,T,B]} {7,S}
6 *4 R!H                   ux {4,[S,D,T,B]} {8,[S,D,T,B]}
7 *2 [Cd,Ct,CO,N,CS]       u0 {5,S} {9,[D,T]}
8 *1 R!H                   u1 {6,[S,D,T,B]}
9 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {7,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "R9_SSSSSD",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 R!H                   u0 {1,S} {3,S}
3 *6 R!H                   u0 {2,S} {4,S}
4 *7 R!H                   u0 {3,S} {5,S}
5 *8 R!H                   u0 {4,S} {6,S}
6 *9 R!H                   u0 {5,S} {7,D}
7 *5 R!H                   u0 {6,D} {8,S}
8 *2 [Cd,Ct,CO,N,CS]       u0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "R9_SDSSSD",
    group = 
"""
1 *7 R!H                   u0 {2,S} {4,S}
2 *8 R!H                   u0 {1,S} {3,S}
3 *9 R!H                   u0 {2,S} {5,D}
4 *6 R!H                   u0 {1,S} {6,D}
5 *5 R!H                   u0 {3,D} {7,S}
6 *4 R!H                   u0 {4,D} {8,S}
7 *2 [Cd,Ct,CO,N,CS]       u0 {5,S} {9,[D,T]}
8 *1 R!H                   u1 {6,S}
9 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {7,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "R10",
    group = 
"""
1  *7  R!H ux {2,[S,D,T,B]} {5,[S,D,T,B]}
2  *8  R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  *9  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux {3,[S,D,T,B]} {6,[S,D,T,B]}
5  *6  R!H ux {1,[S,D,T,B]} {7,[S,D,T,B]}
6  *5  R!H ux {4,[S,D,T,B]} {8,[S,D,T,B]}
7  *4  R!H ux {5,[S,D,T,B]} {9,[S,D,T,B]}
8  *2  R!H u0 {6,[S,D,T,B]} {10,[D,T,B]}
9  *1  R!H u1 {7,[S,D,T,B]}
10 *3  R!H u0 c0 {8,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "R10_cyclic",
    group = "OR{Rn2c8_alpha_long, Rn3c7_alpha_long, Rn3c8_beta_long, Rn4c6_alpha_long, Rn4c7_beta_long, Rn5c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 306,
    label = "Rn2c8_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "Rn3c7_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "Rn3c8_beta_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {11,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {11,[S,D,T,B]}
8  *6  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
11     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "Rn4c6_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "Rn4c6_alpha_long_SDSD",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {6,S}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,S}
6  *8  R!H ux r1 {1,S} {5,S} {7,D}
7  *7  R!H ux {6,D} {8,S}
8  *6  R!H ux r0 {7,S} {9,D}
9  *4  R!H ux r0 {8,D} {10,S}
10 *1  R!H u1 r0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "Rn4c7_beta_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {11,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {11,[S,D,T,B]}
7  *7  R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
11     R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "Rn5c5_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {5,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "R10_linear",
    group = 
"""
1  *1  R!H                   u1 {2,[S,D,T,B]}
2  *4  R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  *6  R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7  R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8  R!H                   ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H                   ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *10 R!H                   ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5  R!H                   ux {7,[S,D,T,B]} {9,S}
9  *2  [Cd,Ct,CO,N,CS]       u0 {8,S} {10,[D,T]}
10 *3  [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {9,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "R11",
    group = 
"""
1  *7  R!H ux {2,[S,D,T,B]} {6,[S,D,T,B]}
2  *8  R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  *9  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *11 R!H ux {4,[S,D,T,B]} {7,[S,D,T,B]}
6  *6  R!H ux {1,[S,D,T,B]} {8,[S,D,T,B]}
7  *5  R!H ux {5,[S,D,T,B]} {9,[S,D,T,B]}
8  *4  R!H ux {6,[S,D,T,B]} {10,[S,D,T,B]}
9  *2  R!H u0 {7,[S,D,T,B]} {11,[D,T,B]}
10 *1  R!H u1 {8,[S,D,T,B]}
11 *3  R!H u0 c0 {9,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "R11_cyclic",
    group = "OR{Rn3c8_alpha_long, Rn4c7_alpha_long, Rn4c8_beta_long, Rn5c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 316,
    label = "Rn3c8_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *11 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *10 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *7  R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "Rn4c7_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *11 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *10 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8  R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *7  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "Rn4c8_beta_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {12,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *11 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *10 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {12,[S,D,T,B]}
8  *7  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 r0 {10,[S,D,T,B]}
12     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "Rn5c6_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *11 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *10 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8  R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *7  R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "R11_linear",
    group = 
"""
1  *1  R!H                   u1 {2,[S,D,T,B]}
2  *4  R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  *6  R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7  R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8  R!H                   ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H                   ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *10 R!H                   ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *11 R!H                   ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *5  R!H                   ux {8,[S,D,T,B]} {10,S}
10 *2  [Cd,Ct,CO,N,CS]       u0 {9,S} {11,[D,T]}
11 *3  [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {10,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "R12",
    group = 
"""
1  *7  R!H ux {2,[S,D,T,B]} {7,[S,D,T,B]}
2  *8  R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  *9  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *11 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *12 R!H ux {5,[S,D,T,B]} {8,[S,D,T,B]}
7  *6  R!H ux {1,[S,D,T,B]} {9,[S,D,T,B]}
8  *5  R!H ux {6,[S,D,T,B]} {10,[S,D,T,B]}
9  *4  R!H ux {7,[S,D,T,B]} {11,[S,D,T,B]}
10 *2  R!H u0 {8,[S,D,T,B]} {12,[D,T,B]}
11 *1  R!H u1 {9,[S,D,T,B]}
12 *3  R!H u0 c0 {10,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "R12_cyclic",
    group = "OR{Rn4c8_alpha_long, Rn5c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 323,
    label = "Rn4c8_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *12 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *11 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *10 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *9  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *8  R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *7  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *6  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *4  R!H ux r0 {10,[S,D,T,B]} {12,[S,D,T,B]}
12 *1  R!H u1 r0 {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "Rn5c7_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *12 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *11 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *10 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *9  R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *8  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *7  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *6  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *4  R!H ux r0 {10,[S,D,T,B]} {12,[S,D,T,B]}
12 *1  R!H u1 r0 {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "R12_linear",
    group = 
"""
1  *1  R!H                   u1 {2,[S,D,T,B]}
2  *4  R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  *6  R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7  R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8  R!H                   ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H                   ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *10 R!H                   ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *11 R!H                   ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *12 R!H                   ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *5  R!H                   ux {9,[S,D,T,B]} {11,S}
11 *2  [Cd,Ct,CO,N,CS]       u0 {10,S} {12,[D,T]}
12 *3  [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {11,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "R13",
    group = 
"""
1  *7  R!H ux {2,[S,D,T,B]} {8,[S,D,T,B]}
2  *8  R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  *9  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *11 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *12 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *13 R!H ux {6,[S,D,T,B]} {9,[S,D,T,B]}
8  *6  R!H ux {1,[S,D,T,B]} {10,[S,D,T,B]}
9  *5  R!H ux {7,[S,D,T,B]} {11,[S,D,T,B]}
10 *4  R!H ux {8,[S,D,T,B]} {12,[S,D,T,B]}
11 *2  R!H u0 {9,[S,D,T,B]} {13,[D,T,B]}
12 *1  R!H u1 {10,[S,D,T,B]}
13 *3  R!H u0 c0 {11,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "R13_cyclic",
    group = "OR{Rn5c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 328,
    label = "Rn5c8_alpha_long",
    group = 
"""
1  *3  R!H u0 c0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *13 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *12 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *11 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *10 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *9  R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *8  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *7  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *6  R!H ux r0 {10,[S,D,T,B]} {12,[S,D,T,B]}
12 *4  R!H ux r0 {11,[S,D,T,B]} {13,[S,D,T,B]}
13 *1  R!H u1 r0 {12,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "R13_linear",
    group = 
"""
1  *1  R!H                   u1 {2,[S,D,T,B]}
2  *4  R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  *6  R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7  R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8  R!H                   ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H                   ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *10 R!H                   ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *11 R!H                   ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *12 R!H                   ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *13 R!H                   ux {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *5  R!H                   ux {10,[S,D,T,B]} {12,S}
12 *2  [Cd,Ct,CO,N,CS]       u0 {11,S} {13,[D,T]}
13 *3  [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {12,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "doublebond_intra",
    group = 
"""
1 *2 [Cd,Cdd] u0 {2,D}
2 *3 [Cd,Cdd] u0 c0 {1,D}
""",
    kinetics = None,
    longDesc = 
u"""
Note that nodes below this currently do not match allenic type Cdd atoms for *3,
so this is the most specific group that will match such a molecule.
""",
)

entry(
    index = 331,
    label = "doublebond_intra_CdCdd",
    group = 
"""
1 *2 Cdd u0 {2,D}
2 *3 Cd  u0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "doublebond_intra_pri",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 c0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "doublebond_intra_pri_2H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "doublebond_intra_pri_HNd",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "doublebond_intra_pri_HDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "doublebond_intra_pri_HCd",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S}
3    H  u0 {1,S}
4    Cd u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "doublebond_intra_pri_HCt",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "doublebond_intra_pri_NdNd",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "doublebond_intra_pri_NdDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "doublebond_intra_pri_NdCd",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    [Cs,O,S] u0 {1,S}
4    Cd       u0 {1,S}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "doublebond_intra_pri_NdCt",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    [Cs,O,S] u0 {1,S}
4    Ct       u0 {1,S}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "doublebond_intra_pri_DeDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "doublebond_intra_secNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "doublebond_intra_secNd_2H",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    H        u0 {1,S}
4    H        u0 {1,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "doublebond_intra_secNd_HNd",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "doublebond_intra_secNd_HDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "doublebond_intra_secNd_HCd",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    H        u0 {1,S}
4    Cd       u0 {1,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "doublebond_intra_secNd_HCt",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    H        u0 {1,S}
4    Ct       u0 {1,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "doublebond_intra_secNd_NdNd",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "doublebond_intra_secNd_NdDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "doublebond_intra_secNd_NdCd",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    [Cs,O,S] u0 {1,S}
4    Cd       u0 {1,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "doublebond_intra_secNd_NdCt",
    group = 
"""
1 *3 Cd       u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S}
3    [Cs,O,S] u0 {1,S}
4    Ct       u0 {1,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "doublebond_intra_secNd_DeDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "doublebond_intra_secDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "doublebond_intra_secDe_2H",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 356,
    label = "doublebond_intra_secDe_HNd",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    H                u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 357,
    label = "doublebond_intra_secDe_HDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 358,
    label = "doublebond_intra_secDe_HCd",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    H                u0 {1,S}
4    Cd               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 359,
    label = "doublebond_intra_secDe_HCt",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    H                u0 {1,S}
4    Ct               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 360,
    label = "doublebond_intra_secDe_NdNd",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 361,
    label = "doublebond_intra_secDe_NdDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 362,
    label = "doublebond_intra_secDe_NdCd",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    Cd               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 363,
    label = "doublebond_intra_secDe_NdCt",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    Ct               u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 364,
    label = "doublebond_intra_secDe_DeDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 365,
    label = "triplebond_intra",
    group = 
"""
1 *2 Ct u0 {2,T}
2 *3 Ct u0 c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 366,
    label = "triplebond_intra_H",
    group = 
"""
1 *3 Ct u0 c0 {2,T} {3,S}
2 *2 Ct u0 {1,T}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 367,
    label = "triplebond_intra_Nd",
    group = 
"""
1 *3 Ct       u0 c0 {2,T} {3,S}
2 *2 Ct       u0 {1,T}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 368,
    label = "triplebond_intra_De",
    group = 
"""
1 *3 Ct               u0 c0 {2,T} {3,S}
2 *2 Ct               u0 {1,T}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 369,
    label = "benzenebond_intra",
    group = 
"""
1 *2 [Cb,Cbf] u0 r1 {2,B}
2 *3 [Cb,Cbf] u0 c0 r1 {1,B}
""",
    kinetics = None,
)

entry(
    index = 370,
    label = "benzenebond_intra_CbCb",
    group = 
"""
1 *2 Cb u0 r1 {2,B}
2 *3 Cb u0 c0 r1 {1,B}
""",
    kinetics = None,
)

entry(
    index = 371,
    label = "benzenebond_intra_CbCbH",
    group = 
"""
1 *2 Cb u0 r1 {2,B}
2 *3 Cb u0 c0 r1 {1,B} {3,S}
3    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 372,
    label = "benzenebond_intra_CbCbf",
    group = 
"""
1 *2 Cb  u0 r1 {2,B}
2 *3 Cbf u0 c0 r1 {1,B}
""",
    kinetics = None,
)

entry(
    index = 373,
    label = "benzenebond_intra_CbfCb",
    group = 
"""
1 *2 Cbf u0 r1 {2,B}
2 *3 Cb  u0 c0 r1 {1,B}
""",
    kinetics = None,
)

entry(
    index = 374,
    label = "benzenebond_intra_CbfCbf",
    group = 
"""
1 *2 Cbf u0 r1 {2,B}
2 *3 Cbf u0 c0 r1 {1,B}
""",
    kinetics = None,
)

entry(
    index = 375,
    label = "carbonyl_intra",
    group = 
"""
1 *2 CO  u0 {2,D}
2 *3 O2d u0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 376,
    label = "carbonyl_intra_H",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S}
2 *3 O2d u0 c0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 377,
    label = "carbonyl_intra_Nd",
    group = 
"""
1 *2 CO       u0 {2,D} {3,S}
2 *3 O2d      u0 c0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 378,
    label = "carbonyl_intra_De",
    group = 
"""
1 *2 CO               u0 {2,D} {3,S}
2 *3 O2d              u0 c0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 379,
    label = "thiyl_intra",
    group = 
"""
1 *2 CS  u0 {2,D}
2 *3 S2d u0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 380,
    label = "thiyl_intra_H",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S}
2 *3 S2d u0 c0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 381,
    label = "thiyl_intra_Nd",
    group = 
"""
1 *2 CS       u0 {2,D} {3,S}
2 *3 S2d      u0 c0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 382,
    label = "thiyl_intra_De",
    group = 
"""
1 *2 CS               u0 {2,D} {3,S}
2 *3 S2d              u0 c0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 383,
    label = "radadd_intra_cs",
    group = 
"""
1 *1 Cs u1
""",
    kinetics = None,
)

entry(
    index = 384,
    label = "radadd_intra_cs2H",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 385,
    label = "radadd_intra_csHNd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    H        u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 386,
    label = "radadd_intra_csHDe",
    group = 
"""
1 *1 Cs               u1 {2,S} {3,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 387,
    label = "radadd_intra_csHCd",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 388,
    label = "radadd_intra_csH(CdCdCd)",
    group = 
"""
1    Cd u0 {2,S} {3,D}
2 *1 Cs u1 {1,S} {4,S}
3    Cd u0 {1,D} {5,S}
4    H  u0 {2,S}
5    Cd u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 389,
    label = "radadd_intra_csHCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 390,
    label = "radadd_intra_csHCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 391,
    label = "radadd_intra_csNdNd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 392,
    label = "radadd_intra_csNdDe",
    group = 
"""
1 *1 Cs               u1 {2,S} {3,S}
2    [Cs,O,S]         u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 393,
    label = "radadd_intra_csNdCd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    Cd       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 394,
    label = "radadd_intra_csNdCt",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    Ct       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 395,
    label = "radadd_intra_csDeDe",
    group = 
"""
1 *1 Cs               u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 396,
    label = "radadd_intra_O",
    group = 
"""
1 *1 O u1
""",
    kinetics = None,
)

entry(
    index = 397,
    label = "radadd_intra_S",
    group = 
"""
1 *1 S u1
""",
    kinetics = None,
)

entry(
    index = 398,
    label = "radadd_intra_Cb",
    group = 
"""
1 *1 Cb u1
""",
    kinetics = None,
)

entry(
    index = 399,
    label = "radadd_intra_cdsingle",
    group = 
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 400,
    label = "radadd_intra_cdsingleH",
    group = 
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 401,
    label = "radadd_intra_cdsingleNd",
    group = 
"""
1 *1 Cd       u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 402,
    label = "radadd_intra_cdsingleDe",
    group = 
"""
1 *1 Cd               u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 403,
    label = "radadd_intra_cdsingleDe_cb",
    group = 
"""
1 *1 Cd u1 {2,S}
2    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 404,
    label = "radadd_intra_cddouble",
    group = 
"""
1 *1 Cd u1 {2,D}
2    Cd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 405,
    label = "radadd_intra_CO",
    group = 
"""
1 *1 CO u1 {2,D}
2    O  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 406,
    label = "radadd_intra_Ct",
    group = 
"""
1 *1 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 407,
    label = "Rn2c6_alpha_short_O",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T]} {8,[S,D,T,B]}
3 *4 O   ux {2,[S,D,T]} {4,[S,D,T]}
4 *1 R!H u1 r0 {3,[S,D,T]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 408,
    label = "Rn2c6_alpha_short_C",
    group = 
"""
1 *3 R!H u0 c0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *4 C   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 409,
    label = "doublebond_intra_pri_HNd_Cs",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    H        u0 {2,S}
5    Cs       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 410,
    label = "doublebond_intra_pri_HNd_O",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    H        u0 {2,S}
5    O        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 411,
    label = "radadd_intra_csHCO",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    H        u0 {1,S}
3    CO       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 412,
    label = "doublebond_intra_pri_HCO",
    group = 
"""
1 *2 Cd        u0 {2,D} {3,S}
2 *3 Cd        u0 c0 {1,D} {4,S} {5,S}
3    H         u0 {1,S}
4    H         u0 {2,S}
5    CO        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 413,
    label = "radadd_intra_csHCs",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    H        u0 {1,S}
3    Cs       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 414,
    label = "radadd_intra_csHO",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    H        u0 {1,S}
3    O       u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: Rn
    L2: R3
        L3: R3_cyclic
            L4: Rn0cx_beta
                L5: Rn0c4_beta
                L5: Rn0c5_beta_short
                L5: Rn0c6_beta_short
                    L6: Rn0c6_beta_short_SBSS
                        L7: Rn0c6_beta_short_SBSS_D
                L5: Rn0c7_beta_short
                    L6: Rn0c7_beta_short_SDSDS
                        L7: Rn0c7_beta_short_SDSDS_D
                L5: Rn0c8_beta_short
            L4: Rn1cx_alpha
                L5: Rn1c3_alpha_short
                L5: Rn1c4_alpha_short
                L5: Rn1c5_alpha_short
                L5: Rn1c6_alpha_short
                    L6: Rn1c6ben_alpha_short
                L5: Rn1c7_alpha_short
                L5: Rn1c8_alpha_short
        L3: R3_linear
            L4: R3_D
            L4: R3_T
            L4: R3_CO
            L4: R3_CS
    L2: R4
        L3: R4_cyclic
            L4: Rn0cx_gamma
                L5: Rn0c6_gamma
                L5: Rn0c7_gamma_short
                    L6: Rn0c7_gamma_short_SSDS
                        L7: Rn0c7_gamma_short_SSDS_D
                L5: Rn0c8_gamma_short
            L4: Rn1cx_beta
                L5: Rn1c4_beta
                L5: Rn1c5_beta_short
                L5: Rn1c6_beta_short
                L5: Rn1c7_beta_short
                L5: Rn1c8_beta_short
            L4: Rn2cx_alpha
                L5: Rn2c3_alpha_short
                L5: Rn2c4_alpha_short
                L5: Rn2c5_alpha_short
                L5: Rn2c6_alpha_short
                    L6: Rn2c6_alpha_short_O
                    L6: Rn2c6_alpha_short_C
                L5: Rn2c7_alpha_short
                L5: Rn2c8_alpha_short
            L4: Rn0c5_beta_long
            L4: Rn1c3_alpha_long
        L3: R4_linear
            L4: R4_S
                L5: R4_S_D
                    L6: R4_Cs_RR_D
                        L7: R4_Cs_HH_D
                L5: R4_S_T
                L5: R4_S_CO
                L5: R4_S_CS
            L4: R4_D
                L5: R4_D_D
                L5: R4_D_T
                L5: R4_D_CO
                L5: R4_D_CS
            L4: R4_T
                L5: R4_T_D
                L5: R4_T_T
                L5: R4_T_CO
                L5: R4_T_CS
    L2: R5
        L3: R5_cyclic
            L4: Rn0cx_delta
                L5: Rn0c8_delta
                L5: Rn0c10_delta_short
                    L6: Rn0c10_delta_short_SSDSDS
                        L7: Rn0c10_delta_short_SSDSDS_D
            L4: Rn1cx_gamma
                L5: Rn1c6_gamma
                L5: Rn1c7_gamma_short
                L5: Rn1c8_gamma_short
            L4: Rn2cx_beta
                L5: Rn2c4_beta
                L5: Rn2c5_beta_short
                    L6: Rn2c5_beta_short_SS
                L5: Rn2c6_beta_short
                L5: Rn2c7_beta_short
                L5: Rn2c8_beta_short
            L4: Rn3cx_alpha
                L5: Rn3c3_alpha_short
                L5: Rn3c4_alpha_short
                L5: Rn3c5_alpha_short
                L5: Rn3c6_alpha_short
                    L6: Rn3c6ben_alpha_short
                        L7: Rn3c6ben_alpha_short_MSS
                        L7: Rn3c6ben_alpha_short_SDS
                L5: Rn3c7_alpha_short
                L5: Rn3c8_alpha_short
            L4: Rn0c6_beta_long
                L5: Rn0c6_beta_long_SS
                    L6: Rn0c6_beta_long_SS_D
                        L7: Rn0c6_beta_long_SS_D_HH
                            L8: 2-hydro-naphthalene
                        L7: Rn0c6_beta_long_SS_D_RH
                        L7: Rn0c6_beta_long_SS_D_RR
            L4: Rn1c4_alpha_long
            L4: Rn0c7_gamma_long
                L5: Rn0c7_gamma_long_SSS
                    L6: Rn0c7_gamma_long_SSS_D
                L5: Rn0c7_gamma_long_SDS
                    L6: Rn0c7_gamma_long_SDS_D
            L4: Rn1c5_beta_long
            L4: Rn2c3_alpha_long
        L3: R5_linear
            L4: R5_cyc5_beta
            L4: R5_SS
                L5: R5_SS_D
                    L6: R5_CsCs_RR_D
                        L7: R5_CsCs_RH_D
                            L8: R5_CsCs_HH_D
                L5: R5_SS_T
                L5: R5_SS_CO
                L5: R5_SS_CS
                    L6: Cs-R5_SS_CS
                    L6: H2-R5_SS_CS
            L4: R5_SM
                L5: R5_SD
                    L6: R5_SD_D
                    L6: R5_SD_T
                    L6: R5_SD_CO
                    L6: R5_SD_CS
                L5: R5_ST
                    L6: R5_ST_D
                    L6: R5_ST_T
                    L6: R5_ST_CO
                    L6: R5_ST_CS
                L5: R5_SB
            L4: R5_MS
                L5: R5_DS
                    L6: R5_DS_D
                    L6: R5_DS_T
                    L6: R5_DS_CO
                    L6: R5_DS_CS
                L5: R5_TS
                    L6: R5_TS_D
                    L6: R5_TS_T
                    L6: R5_TS_CO
                L5: R5_BS
            L4: R5_MM
    L2: R6plus
        L3: R6
            L4: R6_cyclic
                L5: Rn0cx_epsilon
                    L6: Rn0c10_epsilon
                        L7: Rn0c10_epsilon_SDSDS
                            L8: Rn0c10_epsilon_SDSDS_D
                L5: Rn1cx_delta
                    L6: Rn1c8_delta
                L5: Rn2cx_gamma
                    L6: Rn2c6_gamma
                    L6: Rn2c7_gamma_short
                    L6: Rn2c8_gamma_short
                L5: Rn3cx_beta
                    L6: Rn3c4_beta
                    L6: Rn3c5_beta_short
                    L6: Rn3c6_beta_short
                    L6: Rn3c7_beta_short
                    L6: Rn3c8_beta_short
                L5: Rn4cx_alpha
                    L6: Rn4c3_alpha_short
                    L6: Rn4c4_alpha_short
                    L6: Rn4c5_alpha_short
                    L6: Rn4c6_alpha_short
                        L7: Rn4c6ben_alpha_short
                            L8: Rn4c6ben_alpha_short_SDSS
                            L8: Rn4c6ben_alpha_short_DSDS
                    L6: Rn4c7_alpha_short
                    L6: Rn4c8_alpha_short
                L5: Rn0c7_beta_long
                    L6: Rn0c7_beta_long_SS
                        L7: Rn0c7_beta_long_SS_D
                L5: Rn1c5_alpha_long
                    L6: Rn1c5_alpha_long_indene
                L5: Rn0c8_gamma_long
                L5: Rn1c6_beta_long
                L5: Rn2c4_alpha_long
                L5: Rn1c7_gamma_long
                L5: Rn2c5_beta_long
                    L6: Rn2c5_beta_long_SS
                L5: Rn3c3_alpha_long
            L4: R6_linear
                L5: R6_RSR
                    L6: R6_SSR
                        L7: R6_SSS
                            L8: R6_SSS_D
                                L9: R6_CsCsCs_RR_D
                                    L10: R6_CsCsCs_RH_D
                                        L11: R6_CsCsCs_HH_D
                            L8: R6_SSS_T
                            L8: R6_SSS_CO
                        L7: R6_SSM
                            L8: R6_SSM_D
                            L8: R6_SSM_T
                            L8: R6_SSM_CO
                            L8: R6_SSM_CS
                    L6: R6_MSR
                        L7: R6_DSR
                            L8: R6_DSS
                                L9: R6_DSS_D
                                L9: R6_DSS_T
                                L9: R6_DSS_CO
                            L8: R6_DSM
                                L9: R6_DSM_D
                                    L10: R6_DSB_D
                                L9: R6_DSM_T
                                    L10: R6_DSB_T
                                L9: R6_DSM_CO
                                L9: R6_DSM_CS
                        L7: R6_TSR
                            L8: R6_TSS
                                L9: R6_TSS_D
                                L9: R6_TSS_T
                                L9: R6_TSS_CO
                                L9: R6_TSS_CS
                            L8: R6_TSM
                                L9: R6_TSM_D
                                L9: R6_TSM_T
                                L9: R6_TSM_CO
                                L9: R6_TSM_CS
                        L7: R6_MSR_D
                L5: R6_SMS
                    L6: R6_SMS_D
                        L7: R6_SMS(M)S_D
                        L7: R6_SDS_D
                        L7: R6_SBS_D
                    L6: R6_SMS_T
                    L6: R6_SMS_CO
                L5: R6_SMM
        L3: R7
            L4: R7_cyclic
                L5: Rn2cx_delta
                    L6: Rn2c8_delta
                L5: Rn3cx_gamma
                    L6: Rn3c6_gamma
                    L6: Rn3c7_gamma_short
                    L6: Rn3c8_gamma_short
                L5: Rn4cx_beta
                    L6: Rn4c4_beta
                    L6: Rn4c5_beta_short
                    L6: Rn4c6_beta_short
                    L6: Rn4c7_beta_short
                    L6: Rn4c8_beta_short
                L5: Rn5cx_alpha
                    L6: Rn5c3_alpha_short
                    L6: Rn5c4_alpha_short
                    L6: Rn5c5_alpha_short
                    L6: Rn5c6_alpha_short
                    L6: Rn5c7_alpha_short
                    L6: Rn5c8_alpha_short
                L5: Rn0c8_beta_long
                L5: Rn1c6_alpha_long
                    L6: Rn1c6_alpha_long_loop
                L5: Rn1c7_beta_long
                L5: Rn2c5_alpha_long
                    L6: Rn2c5_alpha_long_SS
                    L6: Rn2c5_alpha_long_DS
                L5: Rn0c10_delta_long
                    L6: Rn0c10_delta_long_SSDS
                        L7: Rn0c10_delta_long_SSDS_D
                L5: Rn1c8_gamma_long
                L5: Rn2c6_beta_long
                L5: Rn3c4_alpha_long
                L5: Rn2c7_gamma_long
                L5: Rn3c5_beta_long
                L5: Rn4c3_alpha_long
            L4: R7_linear
                L5: R7_SDSD_D
        L3: R8
            L4: R8_cyclic
                L5: Rn1c7_alpha_long
                L5: Rn1c8_beta_long
                L5: Rn2c6_alpha_long
                L5: Rn2c7_beta_long
                L5: Rn3c5_alpha_long
                L5: Rn2c8_gamma_long
                L5: Rn3c6_beta_long
                L5: Rn4c4_alpha_long
                L5: Rn3c7_gamma_long
                L5: Rn4c5_beta_long
                L5: Rn5c3_alpha_long
            L4: R8_linear
        L3: R9
            L4: R9_cyclic
                L5: Rn1c8_alpha_long
                L5: Rn2c7_alpha_long
                L5: Rn2c8_beta_long
                L5: Rn3c6_alpha_long
                L5: Rn3c7_beta_long
                L5: Rn3c8_gamma_long
                L5: Rn4c5_alpha_long
                L5: Rn4c6_beta_long
                L5: Rn5c4_alpha_long
            L4: R9_linear
                L5: R9_SSSSSD
                L5: R9_SDSSSD
        L3: R10
            L4: R10_cyclic
                L5: Rn2c8_alpha_long
                L5: Rn3c7_alpha_long
                L5: Rn3c8_beta_long
                L5: Rn4c6_alpha_long
                    L6: Rn4c6_alpha_long_SDSD
                L5: Rn4c7_beta_long
                L5: Rn5c5_alpha_long
            L4: R10_linear
        L3: R11
            L4: R11_cyclic
                L5: Rn3c8_alpha_long
                L5: Rn4c7_alpha_long
                L5: Rn4c8_beta_long
                L5: Rn5c6_alpha_long
            L4: R11_linear
        L3: R12
            L4: R12_cyclic
                L5: Rn4c8_alpha_long
                L5: Rn5c7_alpha_long
            L4: R12_linear
        L3: R13
            L4: R13_cyclic
                L5: Rn5c8_alpha_long
            L4: R13_linear
L1: multiplebond_intra
    L2: doublebond_intra
        L3: doublebond_intra_CdCdd
        L3: doublebond_intra_pri
            L4: doublebond_intra_pri_2H
            L4: doublebond_intra_pri_HNd
                L5: doublebond_intra_pri_HNd_Cs
                L5: doublebond_intra_pri_HNd_O
            L4: doublebond_intra_pri_HDe
                L5: doublebond_intra_pri_HCd
                L5: doublebond_intra_pri_HCt
                L5: doublebond_intra_pri_HCO
            L4: doublebond_intra_pri_NdNd
            L4: doublebond_intra_pri_NdDe
                L5: doublebond_intra_pri_NdCd
                L5: doublebond_intra_pri_NdCt
            L4: doublebond_intra_pri_DeDe
        L3: doublebond_intra_secNd
            L4: doublebond_intra_secNd_2H
            L4: doublebond_intra_secNd_HNd
            L4: doublebond_intra_secNd_HDe
                L5: doublebond_intra_secNd_HCd
                L5: doublebond_intra_secNd_HCt
            L4: doublebond_intra_secNd_NdNd
            L4: doublebond_intra_secNd_NdDe
                L5: doublebond_intra_secNd_NdCd
                L5: doublebond_intra_secNd_NdCt
            L4: doublebond_intra_secNd_DeDe
        L3: doublebond_intra_secDe
            L4: doublebond_intra_secDe_2H
            L4: doublebond_intra_secDe_HNd
            L4: doublebond_intra_secDe_HDe
                L5: doublebond_intra_secDe_HCd
                L5: doublebond_intra_secDe_HCt
            L4: doublebond_intra_secDe_NdNd
            L4: doublebond_intra_secDe_NdDe
                L5: doublebond_intra_secDe_NdCd
                L5: doublebond_intra_secDe_NdCt
            L4: doublebond_intra_secDe_DeDe
    L2: triplebond_intra
        L3: triplebond_intra_H
        L3: triplebond_intra_Nd
        L3: triplebond_intra_De
    L2: benzenebond_intra
        L3: benzenebond_intra_CbCb
            L4: benzenebond_intra_CbCbH
        L3: benzenebond_intra_CbCbf
        L3: benzenebond_intra_CbfCb
        L3: benzenebond_intra_CbfCbf
    L2: carbonyl_intra
        L3: carbonyl_intra_H
        L3: carbonyl_intra_Nd
        L3: carbonyl_intra_De
    L2: thiyl_intra
        L3: thiyl_intra_H
        L3: thiyl_intra_Nd
        L3: thiyl_intra_De
L1: radadd_intra
    L2: radadd_intra_cs
        L3: radadd_intra_cs2H
        L3: radadd_intra_csHNd
            L4: radadd_intra_csHCs
            L4: radadd_intra_csHO
        L3: radadd_intra_csHDe
            L4: radadd_intra_csHCd
                L5: radadd_intra_csH(CdCdCd)
            L4: radadd_intra_csHCt
            L4: radadd_intra_csHCb
            L4: radadd_intra_csHCO
        L3: radadd_intra_csNdNd
        L3: radadd_intra_csNdDe
            L4: radadd_intra_csNdCd
            L4: radadd_intra_csNdCt
        L3: radadd_intra_csDeDe
    L2: radadd_intra_O
    L2: radadd_intra_S
    L2: radadd_intra_Cb
    L2: radadd_intra_cdsingle
        L3: radadd_intra_cdsingleH
        L3: radadd_intra_cdsingleNd
        L3: radadd_intra_cdsingleDe
            L4: radadd_intra_cdsingleDe_cb
    L2: radadd_intra_cddouble
    L2: radadd_intra_CO
    L2: radadd_intra_Ct
"""
)

forbidden(
    label = "1_naphthyl_7_add_res1",
    group = 
"""
1     C u0 {2,[D,B]} {3,[S,B]} {4,[S,B]}
2     C u0 {1,[D,B]} {5,[S,B]} {6,[S,B]}
3     C u0 {1,[S,B]} {7,[D,B]}
4     C u0 {1,[S,B]} {9,[D,B]}
5     C u0 {2,[S,B]} {8,[D,B]}
6  *1 C u1 {2,[S,B]} {10,[D,B]}
7     C u0 {3,[D,B]} {8,[S,B]}
8  *3 C u0 {5,[D,B]} {7,[S,B]}
9     C u0 {4,[D,B]} {10,[S,B]}
10    C u0 {6,[D,B]} {9,[S,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 1.
""",
)

forbidden(
    label = "1_naphthyl_7_add_res2",
    group = 
"""
1     C u0 {2,S} {3,S} {4,D}
2     C u0 {1,S} {5,S} {6,D}
3     C u0 {1,S} {7,D}
4     C u0 {1,D} {9,S}
5  *2 C u0 {2,S} {8,D}
6  *1 C u1 {2,D} {10,S}
7     C u0 {3,D} {8,S}
8  *3 C u0 {5,D} {7,S}
9     C u0 {4,S} {10,D}
10    C u0 {6,S} {9,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 2.
""",
)

forbidden(
    label = "1_naphthyl_7_add_res3",
    group = 
"""
1     C u0 {2,S} {3,S} {4,D}
2     C u0 {1,S} {5,S} {6,D}
3     C u0 {1,S} {7,D}
4     C u0 {1,D} {9,S}
5  *1 C u1 {2,S} {8,D}
6     C u0 {2,D} {10,S}
7     C u0 {3,D} {8,S}
8     C u0 {5,D} {7,S}
9  *2 C u0 {4,S} {10,D}
10 *3 C u0 {6,S} {9,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 3.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD1_res1",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3    C u0 p0 c0 {1,D} {7,S}
4 *2 C u0 p0 c0 {2,S} {7,D}
5    C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,D} {8,S}
7 *3 C u0 p0 c0 {3,S} {4,D}
8 *1 C u1 p0 c0 {6,S} {9,S}
9    C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 5-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD1_res2",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S}
4    C u0 p0 c0 {2,D} {7,S}
5 *2 C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,S} {8,D}
7 *1 C u1 p0 c0 {3,S} {4,S}
8    C u0 p0 c0 {6,D} {9,S}
9 *3 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 5-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD2_res1",
    group = 
"""
1 *2 C u0 p0 c0 {2,S} {3,S} {5,D}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3 *1 C u1 p0 c0 {1,S} {7,S}
4    C u0 p0 c0 {2,S} {7,D}
5 *3 C u0 p0 c0 {1,D} {9,S}
6    C u0 p0 c0 {2,D} {8,S}
7    C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,S} {9,D}
9    C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 3-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD2_res2",
    group = 
"""
1 *2 C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3 *3 C u0 p0 c0 {1,D} {7,S}
4    C u0 p0 c0 {2,S} {7,D}
5 *1 C u1 p0 c0 {1,S} {9,S}
6    C u0 p0 c0 {2,D} {8,S}
7    C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,S} {9,D}
9    C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 3-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD2_res3",
    group = 
"""
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {4,S} {6,S}
3 *1 C u1 p0 c0 {1,S} {7,S}
4    C u0 p0 c0 {2,S} {7,D}
5 *3 C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,S} {8,D}
7    C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,D} {9,S}
9 *2 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 3-membered ring tricyclic.
Resonance form 3.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD3_res1",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {5,D}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 *3 C u0 p0 c0 {2,S} {7,D}
5    C u0 p0 c0 {1,D} {9,S}
6    C u0 p0 c0 {2,D} {8,S}
7 *2 C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,S} {9,D}
9    C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,4, and 3-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD3_res2",
    group = 
"""
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {4,S} {6,S}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 *3 C u0 p0 c0 {2,S} {7,D}
5    C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,S} {8,D}
7 *2 C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,D} {9,S}
9    C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,4, and 3-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD3_res3",
    group = 
"""
1    C u0 p0 c0 {2,B} {3,S} {5,B}
2    C u0 p0 c0 {1,B} {4,S} {6,B}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 *3 C u0 p0 c0 {2,S} {7,D}
5    C u0 p0 c0 {1,B} {9,B}
6    C u0 p0 c0 {2,B} {8,B}
7 *2 C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,B} {9,B}
9    C u0 p0 c0 {5,B} {8,B}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,4, and 3-membered ring tricyclic.
Resonance form3.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD4_res1",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3    C u0 p0 c0 {1,D} {7,S}
4 *2 C u0 p0 c0 {2,S} {7,D}
5 *1 C u1 p0 c0 {1,S} {9,S}
6    C u0 p0 c0 {2,D} {8,S}
7 *3 C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,S} {9,D}
9    C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 4-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD4_res2",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S}
4    C u0 p0 c0 {2,D} {7,S}
5 *3 C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,S} {8,D}
7 *1 C u1 p0 c0 {3,S} {4,S}
8    C u0 p0 c0 {6,D} {9,S}
9 *2 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 4-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD5_res1",
    group = 
"""
1    C u0 {2,S} {3,S} {6,D}
2    C u0 {1,S} {4,S} {5,D}
3    C u0 {1,S} {7,S}
4 *2 C u0 {2,S} {7,D}
5    C u0 {2,D} {8,S}
6    C u0 {1,D} {9,S}
7 *3 C u0 {3,S} {4,D}
8    C u0 {5,S} {9,D}
9 *1 C u1 {6,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from  ring-closing to form a highly strained tricyclic. Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD5_res2",
    group = 
"""
1    C u0 {2,B} {3,S} {6,B}
2    C u0 {1,B} {4,S} {5,B}
3    C u0 {1,S} {7,S}
4 *2 C u0 {2,S} {7,D}
5    C u0 {2,B} {8,B}
6    C u0 {1,B} {9,B}
7 *3 C u0 {3,S} {4,D}
8    C u0 {5,B} {9,B}
9 *1 C u1 {6,B} {8,B}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from  ring-closing to form a highly strained tricyclic. Resonance form 2.
""",
)

forbidden(
    label = "Rn0c6_beta_long_phenyl",
    group = 
"""
1 *1 C u1 {2,[D,B]} {6,[S,B]}
2    C u0 {1,[D,B]} {3,[S,B]}
3 *3 C u0 {2,[S,B]} {4,[D,B]}
4 *2 C u0 {3,[D,B]} {5,[S,B]}
5    C u0 {4,[S,B]} {6,[D,B]}
6    C u0 {1,[S,B]} {5,[D,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 3 and 5 membered ring.
""",
)

forbidden(
    label = "Rn0c6_beta_short_phenyl",
    group = 
"""
1 *1 C u1 {2,[S,B]} {6,[D,B]}
2 *2 C u0 {1,[S,B]} {3,[D,B]}
3 *3 C u0 {2,[D,B]} {4,[S,B]}
4    C u0 {3,[S,B]} {5,[D,B]}
5    C u0 {4,[D,B]} {6,[S,B]}
6    C u0 {1,[D,B]} {5,[S,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 3 and 5 membered ring.
""",
)

forbidden(
    label = "Rn0c6_gamma_phenyl",
    group = 
"""
1 *1 C u1 {2,[D,B]} {6,[S,B]}
2    C u0 {1,[D,B]} {3,[S,B]}
3 *2 C u0 {2,[S,B]} {4,[D,B]}
4 *3 C u0 {3,[D,B]} {5,[S,B]}
5    C u0 {4,[S,B]} {6,[D,B]}
6    C u0 {1,[S,B]} {5,[D,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 4 and 4 membered ring.
""",
)

forbidden(
    label = "Rn1c6_beta_long_phenyl",
    group = 
"""
1 *4 C u0 {2,[D,B]} {3,[S,B]} {7,S}
2    C u0 {1,[D,B]} {4,[S,B]}
3 *2 C u0 {1,[S,B]} {5,[D,B]}
4    C u0 {2,[S,B]} {6,[D,B]}
5 *3 C u0 {3,[D,B]} {6,[S,B]}
6    C u0 {4,[D,B]} {5,[S,B]}
7 *1 C u1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 1 carbon away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn1c6_beta_short_phenyl",
    group = 
"""
1 *4 C u0 {2,[D,B]} {3,[S,B]} {7,S}
2    C u0 {1,[D,B]} {4,[S,B]}
3 *2 C u0 {1,[S,B]} {5,[D,B]}
4    C u0 {2,[S,B]} {6,[D,B]}
5 *3 C u0 {3,[D,B]} {6,[S,B]}
6    C u0 {4,[D,B]} {5,[S,B]}
7 *1 C u1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 1 carbon away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn1c6_gamma_phenyl",
    group = 
"""
1 *4 C u0 {2,[D,B]} {3,[S,B]} {7,S}
2 *5 C u0 {1,[D,B]} {4,[S,B]}
3    C u0 {1,[S,B]} {5,[D,B]}
4 *2 C u0 {2,[S,B]} {6,[D,B]}
5    C u0 {3,[D,B]} {6,[S,B]}
6 *3 C u0 {4,[D,B]} {5,[S,B]}
7 *1 C u1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 1 carbon away from a phenyl side group from adding to the para-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn2c6_beta_long_phenyl",
    group = 
"""
1 *6 C u0 {2,[S,B]} {3,[D,B]} {6,S}
2 *7 C u0 {1,[S,B]} {4,[D,B]}
3    C u0 {1,[D,B]} {5,[S,B]}
4 *5 C u0 {2,[D,B]} {7,[S,B]}
5 *3 C u0 {3,[S,B]} {7,[D,B]}
6 *4 C u0 {1,S} {8,[S,D,T]}
7 *2 C u0 {4,[S,B]} {5,[D,B]}
8 *1 C u1 {6,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 2 carbons away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn2c6_beta_short_phenyl",
    group = 
"""
1 *5 C u0 {2,[D,B]} {3,[S,B]} {6,S}
2    C u0 {1,[D,B]} {4,[S,B]}
3 *2 C u0 {1,[S,B]} {5,[D,B]}
4    C u0 {2,[S,B]} {7,[D,B]}
5 *3 C u0 {3,[D,B]} {7,[S,B]}
6 *4 C u0 {1,S} {8,[S,D,T]}
7    C u0 {4,[D,B]} {5,[S,B]}
8 *1 C u1 {6,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 2 carbons away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn2c6_gamma_phenyl",
    group = 
"""
1 *6 C u0 {2,[D,B]} {3,[S,B]} {6,S}
2 *5 C u0 {1,[D,B]} {4,[S,B]}
3    C u0 {1,[S,B]} {5,[D,B]}
4 *2 C u0 {2,[S,B]} {7,[D,B]}
5    C u0 {3,[D,B]} {7,[S,B]}
6 *4 C u0 {1,S} {8,[S,D,T]}
7 *3 C u0 {4,[D,B]} {5,[S,B]}
8 *1 C u1 {6,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 2 carbons away from a phenyl side group from adding to the para-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn3c6_beta_long_phenyl",
    group = 
"""
1 *7 C u0 {2,[S,B]} {3,[D,B]} {4,S}
2 *8 C u0 {1,[S,B]} {5,[D,B]}
3    C u0 {1,[D,B]} {6,[S,B]}
4 *6 C u0 {1,S} {8,[S,D,T]}
5 *5 C u0 {2,[D,B]} {7,[S,B]}
6 *3 C u0 {3,[S,B]} {7,[D,B]}
7 *2 C u0 {5,[S,B]} {6,[D,B]}
8 *4 C u0 {4,[S,D,T]} {9,[S,D,T]}
9 *1 C u1 {8,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 3 carbons away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn3c6_beta_short_phenyl",
    group = 
"""
1 *5 C u0 {2,[D,B]} {3,[S,B]} {4,S}
2    C u0 {1,[D,B]} {5,[S,B]}
3 *2 C u0 {1,[S,B]} {6,[D,B]}
4 *6 C u0 {1,S} {8,[S,D,T]}
5    C u0 {2,[S,B]} {7,[D,B]}
6 *3 C u0 {3,[D,B]} {7,[S,B]}
7    C u0 {5,[D,B]} {6,[S,B]}
8 *4 C u0 {4,[S,D,T]} {9,[S,D,T]}
9 *1 C u1 {8,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 3 carbons away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn3c6_gamma_phenyl",
    group = 
"""
1 *7 C u0 {2,[S,B]} {3,[D,B]} {4,S}
2    C u0 {1,[S,B]} {5,[D,B]}
3 *5 C u0 {1,[D,B]} {6,[S,B]}
4 *6 C u0 {1,S} {8,[S,D,T]}
5    C u0 {2,[D,B]} {7,[S,B]}
6 *2 C u0 {3,[S,B]} {7,[D,B]}
7 *3 C u0 {5,[S,B]} {6,[D,B]}
8 *4 C u0 {4,[S,D,T]} {9,[S,D,T]}
9 *1 C u1 {8,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 3 carbons away from a phenyl side group from adding to the para-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "bond31",
    group = 
"""
1 *3 R!H u0 c0 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "bond31rad",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "product34_to_product57",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {3,S} {5,S}
3 *1 C u1 p0 c0 {1,S} {2,S}
4 *3 C u0 p0 c0 {1,S} {6,D}
5    C u0 p0 c0 {2,S} {7,D}
6 *2 C u0 p0 c0 {4,D} {7,S}
7    C u0 p0 c0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid product34 in vinylCPD_H library from ring closing to form a fused 6, 3, and 3-membered ring tricyclic.
""",
)

forbidden(
    label = "product45_to_product56",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,S}
3 *2 C u0 p0 c0 {1,S} {4,D}
4 *3 C u0 p0 c0 {2,S} {3,D}
5    C u0 p0 c0 {1,S} {7,D}
6 *1 C u1 p0 c0 {2,S} {7,S}
7    C u0 p0 c0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid product45 in vinylCPD_H library from ring closing to form a fused 5, 4, and 3-membered ring tricyclic.
""",
)

forbidden(
    label = "s2_3_6_diene_0_2_self_ring_close_1_res_1",
    group = 
"""
1    C u0 {2,S} {3,S} {4,[S,D]}
2    C u0 {1,S} {3,S} {5,[S,D]}
3 *1 C u1 {1,S} {2,S}
4    C u0 {1,[S,D]} {6,S}
5    C u0 {2,[S,D]} {7,S}
6 *3 C u0 {4,S} {7,D}
7 *2 C u0 {5,S} {6,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_3_6_diene_0_2 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 3-member ring to one of the far corners of the 6. Resonance form 1.
""",
)

forbidden(
    label = "s2_3_6_diene_0_2_self_ring_close_1_res_2",
    group = 
"""
1 *2 C u0 {2,S} {3,D} {4,S}
2    C u0 {1,S} {3,S} {5,S}
3 *3 C u0 {1,D} {2,S}
4    C u0 {1,S} {6,D}
5    C u0 {2,S} {7,S}
6    C u0 {4,D} {7,S}
7 *1 C u1 {5,S} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_3_6_diene_0_2 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 3-member ring to one of the far corners of the 6. Resonance form 2.
""",
)

forbidden(
    label = "s2_4_5_diene_1_5_self_ring_close_res1",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {5,D}
2    C u0 p0 c0 {1,S} {4,S} {6,S}
3 *3 C u0 p0 c0 {1,S} {4,D}
4 *2 C u0 p0 c0 {2,S} {3,D}
5    C u0 p0 c0 {1,D} {7,S}
6    C u0 p0 c0 {2,S} {7,S}
7 *1 C u1 p0 c0 {5,S} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_4_5_diene_1_5 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 5-member ring to the corner of the 4. Resonance form 1.
""",
)

forbidden(
    label = "s2_4_5_diene_1_5_self_ring_close_res2",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {5,D}
2    C u0 p0 c0 {1,S} {4,S} {6,S}
3 *2 C u0 p0 c0 {1,S} {4,D}
4 *3 C u0 p0 c0 {2,S} {3,D}
5    C u0 p0 c0 {1,D} {7,S}
6    C u0 p0 c0 {2,S} {7,S}
7 *1 C u1 p0 c0 {5,S} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_4_5_diene_1_5 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 5-member ring to the corner of the 4. Resonance form 2.
""",
)

forbidden(
    label = "s2_4_5_diene_1_5_self_ring_close_res3",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,S}
3    C u0 p0 c0 {1,D} {4,S}
4 *1 C u1 p0 c0 {2,S} {3,S}
5 *2 C u0 p0 c0 {1,S} {7,D}
6    C u0 p0 c0 {2,S} {7,S}
7 *3 C u0 p0 c0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_4_5_diene_1_5 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 5-member ring to the corner of the 4. Resonance form 3.
""",
)

