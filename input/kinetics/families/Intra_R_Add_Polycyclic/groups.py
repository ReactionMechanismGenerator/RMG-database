#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Polycyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn_cyclic"], products=["RnCycle"], ownReverse=False)

reverse = "Ring_Open_Poly_Cycli_Radical"

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*2', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 0,
    label = "Rn_cyclic",
    group = "OR{Rn0cx, Rn1cx, Rn2cx, Rn3cx, Rn4cx, Rn5cx}",
    kinetics = None,
)

entry(
    index = 1,
    label = "multiplebond_intra",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,N]        u0 r1 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 r1 {1,[D,T,B]}
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
    label = "Rn0cx",
    group = "OR{Rn0cx_beta, Rn0cx_gamma, Rn0cx_delta}",
    kinetics = None,
)

entry(
    index = 4,
    label = "Rn0cx_beta",
    group = "OR{Rn0c4_beta, Rn0c5_beta, Rn0c6_beta, Rn0c7_beta, Rn0c8_beta}",
    kinetics = None,
)

entry(
    index = 5,
    label = "Rn0c4_beta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Rn0c5_beta",
    group = "OR{Rn0c5_beta_short, Rn0c5_beta_long}",
    kinetics = None,
)

entry(
    index = 7,
    label = "Rn0c5_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {3,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Rn0c5_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Rn0c6_beta",
    group = "OR{Rn0c6_beta_short, Rn0c6_beta_long}",
    kinetics = None,
)

entry(
    index = 10,
    label = "Rn0c6_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Rn0c6_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Rn0c6_beta_long_SSSD",
    group =
"""
1 *3 C u0 r1 {2,D} {6,[S,D,T,B]}
2 *2 C u0 r1 {1,D} {3,S}
3 *5 C ux r1 {2,S} {4,S}
4 *4 C ux r1 {3,S} {5,S}
5 *1 C u1 r1 {4,S} {6,[S,D,T,B]}
6    C ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Rn0c6_beta_long_SDSD",
    group =
"""
1 *3 C u0 r1 {2,D} {6,[S,D,T,B]}
2 *2 C u0 r1 {1,D} {3,S}
3 *5 C ux r1 {2,S} {4,D}
4 *4 C ux r1 {3,D} {5,S}
5 *1 C u1 r1 {4,S} {6,[S,D,T,B]}
6    C ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Rn0c6_beta_long_SDSD_H",
    group =
"""
1 *3 C u0 r1 {2,D} {6,[S,D,T,B]}
2 *2 C u0 r1 {1,D} {3,S}
3 *5 C ux r1 {2,S} {4,D}
4 *4 C ux r1 {3,D} {5,S}
5 *1 C u1 r1 {4,S} {6,[S,D,T,B]}
6    C ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,S} {8,S}
7    H u0 r0 {6,S}
8    H u0 r0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Rn0c6_beta_long_SDSD_R1",
    group =
"""
1 *3 C   u0 r1 {2,D} {6,[S,D,T,B]}
2 *2 C   u0 r1 {1,D} {3,S}
3 *5 C   ux r1 {2,S} {4,D}
4 *4 C   ux r1 {3,D} {5,S}
5 *1 C   u1 r1 {4,S} {6,[S,D,T,B]}
6    C   ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,S} {8,S}
7    R!H u0 r0 {6,S}
8    H   u0 r0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Rn0c6_beta_long_SDSD_R2",
    group =
"""
1 *3 C   u0 r1 {2,D} {6,[S,D,T,B]}
2 *2 C   u0 r1 {1,D} {3,S}
3 *5 C   ux r1 {2,S} {4,D}
4 *4 C   ux r1 {3,D} {5,S}
5 *1 C   u1 r1 {4,S} {6,[S,D,T,B]}
6    C   ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,S} {8,S}
7    R!H u0 r0 {6,S}
8    R!H u0 r0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Rn0c7_beta",
    group = "OR{Rn0c7_beta_short, Rn0c7_beta_long}",
    kinetics = None,
)

entry(
    index = 13,
    label = "Rn0c7_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
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
    index = 14,
    label = "Rn0c7_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 15,
    label = "Rn0c8_beta",
    group = "OR{Rn0c8_beta_short, Rn0c8_beta_long}",
    kinetics = None,
)

entry(
    index = 16,
    label = "Rn0c8_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
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
    index = 17,
    label = "Rn0c8_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 18,
    label = "Rn0cx_gamma",
    group = "OR{Rn0c6_gamma, Rn0c7_gamma, Rn0c8_gamma}",
    kinetics = None,
)

entry(
    index = 19,
    label = "Rn0c6_gamma",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Rn0c7_gamma",
    group = "OR{Rn0c7_gamma_short, Rn0c7_gamma_long}",
    kinetics = None,
)

entry(
    index = 21,
    label = "Rn0c7_gamma_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
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
    index = 22,
    label = "Rn0c7_gamma_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 22,
    label = "Rn0c7_gamma_long_SDSD",
    group =
"""
1 *3 C u0 r1 {2,D} {6,[S,D,T,B]}
2 *2 C u0 r1 {1,D} {3,S}
3 *5 C ux r1 {2,S} {4,D}
4 *4 C ux r1 {3,D} {5,S}
5 *1 C u1 r1 {4,S} {7,[S,D,T,B]}
6    C ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    C ux r1 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Rn0c7_gamma_long_SDSD_R5",
    group =
"""
1  *3 C   u0 r1 {2,D} {6,[S,D,T,B]}
2  *2 C   u0 r1 {1,D} {3,S}
3  *5 C   ux r1 {2,S} {4,D}
4  *4 C   ux r1 {3,D} {5,S}
5  *1 C   u1 r1 {4,S} {7,[S,D,T,B]}
6     C   ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
7     C   ux r1 {5,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
8     R!H ux r1 {6,[S,D,T,B]} {10,[S,D,T,B]}
9     R!H ux r1 {7,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Rn0c8_gamma",
    group = "OR{Rn0c8_gamma_short, Rn0c8_gamma_long}",
    kinetics = None,
)

entry(
    index = 24,
    label = "Rn0c8_gamma_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
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
    index = 25,
    label = "Rn0c8_gamma_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 26,
    label = "Rn0cx_delta",
    group = "OR{Rn0c8_delta}",
    kinetics = None,
)

entry(
    index = 27,
    label = "Rn0c8_delta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 28,
    label = "Rn1cx",
    group = "OR{Rn1cx_alpha}",
    kinetics = None,
)

entry(
    index = 29,
    label = "Rn1cx_alpha",
    group = "OR{Rn1c3_alpha, Rn1c4_alpha, Rn1c5_alpha, Rn1c6_alpha, Rn1c7_alpha, Rn1c8_alpha}",
    kinetics = None,
)

entry(
    index = 30,
    label = "Rn1c3_alpha",
    group = "OR{Rn1c3_alpha_short, Rn1c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 31,
    label = "Rn1c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Rn1c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Rn1c4_alpha",
    group = "OR{Rn1c4_alpha_short, Rn1c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 34,
    label = "Rn1c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Rn1c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "Rn1c5_alpha",
    group = "OR{Rn1c5_alpha_short, Rn1c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 37,
    label = "Rn1c5_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Rn1c5_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Rn1c5_alpha_long_SSSDS",
    group =
"""
1 *3 C u0 r1 {2,D} {5,S}
2 *2 C u0 r1 {1,D} {3,S}
3 *5 C ux r1 {2,S} {4,S}
4 *6 C ux r1 {3,S} {5,S}
5 *4 C ux r1 {1,S} {4,S} {6,S}
6 *1 C u1 r0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Rn1c5_alpha_long_SDSDS",
    group =
"""
1 *3 C u0 r1 {2,D} {5,S}
2 *2 C u0 r1 {1,D} {3,S}
3 *5 C ux r1 {2,S} {4,D}
4 *6 C ux r1 {3,D} {5,S}
5 *4 C ux r1 {1,S} {4,S} {6,S}
6 *1 C u1 r0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Rn1c5_alpha_long_SDSDS_H",
    group =
"""
1 *3 C u0 r1 {2,D} {5,S}
2 *2 C u0 r1 {1,D} {3,S}
3 *5 C ux r1 {2,S} {4,D}
4 *6 C ux r1 {3,D} {5,S}
5 *4 C ux r1 {1,S} {4,S} {6,S} {7,S}
6 *1 C u1 r0 {5,S}
7    H u0 r0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Rn1c5_alpha_long_SDSDS_R",
    group =
"""
1 *3 C   u0 r1 {2,D} {5,S}
2 *2 C   u0 r1 {1,D} {3,S}
3 *5 C   ux r1 {2,S} {4,D}
4 *6 C   ux r1 {3,D} {5,S}
5 *4 C   ux r1 {1,S} {4,S} {6,S} {7,S}
6 *1 C   u1 r0 {5,S}
7    R!H u0 r0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "Rn1c6_alpha",
    group = "OR{Rn1c6_alpha_short, Rn1c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 40,
    label = "Rn1c6_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
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
    index = 41,
    label = "Rn1c6_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 42,
    label = "Rn1c7_alpha",
    group = "OR{Rn1c7_alpha_short, Rn1c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 43,
    label = "Rn1c7_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
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
    index = 44,
    label = "Rn1c7_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 45,
    label = "Rn1c8_alpha",
    group = "OR{Rn1c8_alpha_short, Rn1c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 46,
    label = "Rn1c8_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
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
    index = 47,
    label = "Rn1c8_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 48,
    label = "Rn2cx",
    group = "OR{Rn2cx_alpha, Rn2cx_beta}",
    kinetics = None,
)

entry(
    index = 49,
    label = "Rn2cx_alpha",
    group = "OR{Rn2c3_alpha, Rn2c4_alpha, Rn2c5_alpha, Rn2c6_alpha, Rn2c7_alpha, Rn2c8_alpha}",
    kinetics = None,
)

entry(
    index = 50,
    label = "Rn2c3_alpha",
    group = "OR{Rn2c3_alpha_short, Rn2c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 51,
    label = "Rn2c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Rn2c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Rn2c4_alpha",
    group = "OR{Rn2c4_alpha_short, Rn2c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 54,
    label = "Rn2c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Rn2c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Rn2c5_alpha",
    group = "OR{Rn2c5_alpha_short, Rn2c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 57,
    label = "Rn2c5_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
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
    index = 58,
    label = "Rn2c5_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
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
    index = 59,
    label = "Rn2c6_alpha",
    group = "OR{Rn2c6_alpha_short, Rn2c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 60,
    label = "Rn2c6_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
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
    index = 61,
    label = "Rn2c6_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 62,
    label = "Rn2c7_alpha",
    group = "OR{Rn2c7_alpha_short, Rn2c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 63,
    label = "Rn2c7_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
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
    index = 64,
    label = "Rn2c7_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 65,
    label = "Rn2c8_alpha",
    group = "OR{Rn2c8_alpha_short, Rn2c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 66,
    label = "Rn2c8_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
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
    index = 67,
    label = "Rn2c8_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 68,
    label = "Rn2cx_beta",
    group = "OR{Rn2c4_beta, Rn2c5_beta, Rn2c6_beta, Rn2c7_beta, Rn2c8_beta}",
    kinetics = None,
)

entry(
    index = 69,
    label = "Rn2c4_beta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Rn2c5_beta",
    group = "OR{Rn2c5_beta_short, Rn2c5_beta_long}",
    kinetics = None,
)

entry(
    index = 71,
    label = "Rn2c5_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 71,
    label = "Rn2c5_beta_short_SDSDS",
    group =
"""
1 *3 C u0 r1 {2,D} {6,S}
2 *2 C u0 r1 {1,D} {3,S}
3 *5 C ux r1 {2,S} {4,S} {7,S}
4 *4 C ux r0 {3,S} {5,S}
5 *1 C u1 r0 {4,S}
6    C ux r1 {1,S} {7,D}
7    C ux r1 {3,S} {6,D}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Rn2c5_beta_short_SDSSD",
    group =
"""
1 *3 C u0 r1 {2,D} {6,S}
2 *2 C u0 r1 {1,D} {3,S}
3 *5 C ux r1 {2,S} {4,S} {7,D}
4 *4 C ux r0 {3,S} {5,S}
5 *1 C u1 r0 {4,S}
6    C ux r1 {1,S} {7,S}
7    C ux r1 {3,D} {6,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Rn2c5_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 73,
    label = "Rn2c6_beta",
    group = "OR{Rn2c6_beta_short, Rn2c6_beta_long}",
    kinetics = None,
)

entry(
    index = 74,
    label = "Rn2c6_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
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
    index = 75,
    label = "Rn2c6_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 76,
    label = "Rn2c7_beta",
    group = "OR{Rn2c7_beta_short, Rn2c7_beta_long}",
    kinetics = None,
)

entry(
    index = 77,
    label = "Rn2c7_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 78,
    label = "Rn2c7_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {9,[S,D,T,B]}
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
    index = 79,
    label = "Rn2c8_beta",
    group = "OR{Rn2c8_beta_short, Rn2c8_beta_long}",
    kinetics = None,
)

entry(
    index = 80,
    label = "Rn2c8_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 81,
    label = "Rn2c8_beta_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {10,[S,D,T,B]}
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
    index = 82,
    label = "Rn3cx",
    group = "OR{Rn3cx_alpha, Rn3cx_beta, Rn3cx_gamma}",
    kinetics = None,
)

entry(
    index = 83,
    label = "Rn3cx_alpha",
    group = "OR{Rn3c3_alpha, Rn3c4_alpha, Rn3c5_alpha, Rn3c6_alpha, Rn3c7_alpha, Rn3c8_alpha}",
    kinetics = None,
)

entry(
    index = 84,
    label = "Rn3c3_alpha",
    group = "OR{Rn3c3_alpha_short, Rn3c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 85,
    label = "Rn3c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Rn3c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Rn3c4_alpha",
    group = "OR{Rn3c4_alpha_short, Rn3c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 88,
    label = "Rn3c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 89,
    label = "Rn3c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
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
    index = 90,
    label = "Rn3c5_alpha",
    group = "OR{Rn3c5_alpha_short, Rn3c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 91,
    label = "Rn3c5_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 92,
    label = "Rn3c5_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
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
    index = 93,
    label = "Rn3c6_alpha",
    group = "OR{Rn3c6_alpha_short, Rn3c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 94,
    label = "Rn3c6_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
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
    index = 95,
    label = "Rn3c6_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 96,
    label = "Rn3c7_alpha",
    group = "OR{Rn3c7_alpha_short, Rn3c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 97,
    label = "Rn3c7_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 98,
    label = "Rn3c7_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 99,
    label = "Rn3c8_alpha",
    group = "OR{Rn3c8_alpha_short, Rn3c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 100,
    label = "Rn3c8_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 101,
    label = "Rn3c8_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 102,
    label = "Rn3cx_beta",
    group = "OR{Rn3c4_beta, Rn3c5_beta, Rn3c6_beta, Rn3c7_beta, Rn3c8_beta}",
    kinetics = None,
)

entry(
    index = 103,
    label = "Rn3c4_beta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 104,
    label = "Rn3c5_beta",
    group = "OR{Rn3c5_beta_short, Rn3c5_beta_long}",
    kinetics = None,
)

entry(
    index = 105,
    label = "Rn3c5_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 106,
    label = "Rn3c5_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 107,
    label = "Rn3c6_beta",
    group = "OR{Rn3c6_beta_short, Rn3c6_beta_long}",
    kinetics = None,
)

entry(
    index = 108,
    label = "Rn3c6_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
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
    index = 109,
    label = "Rn3c6_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {9,[S,D,T,B]}
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
    index = 110,
    label = "Rn3c7_beta",
    group = "OR{Rn3c7_beta_short, Rn3c7_beta_long}",
    kinetics = None,
)

entry(
    index = 111,
    label = "Rn3c7_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 112,
    label = "Rn3c7_beta_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {10,[S,D,T,B]}
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
    index = 113,
    label = "Rn3c8_beta",
    group = "OR{Rn3c8_beta_short, Rn3c8_beta_long}",
    kinetics = None,
)

entry(
    index = 114,
    label = "Rn3c8_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 115,
    label = "Rn3c8_beta_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {11,[S,D,T,B]}
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
    index = 116,
    label = "Rn3cx_gamma",
    group = "OR{Rn3c6_gamma, Rn3c7_gamma, Rn3c8_gamma}",
    kinetics = None,
)

entry(
    index = 117,
    label = "Rn3c6_gamma",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 118,
    label = "Rn3c7_gamma",
    group = "OR{Rn3c7_gamma_short, Rn3c7_gamma_long}",
    kinetics = None,
)

entry(
    index = 119,
    label = "Rn3c7_gamma_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 120,
    label = "Rn3c7_gamma_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {9,[S,D,T,B]}
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
    index = 121,
    label = "Rn3c8_gamma",
    group = "OR{Rn3c8_gamma_short, Rn3c8_gamma_long}",
    kinetics = None,
)

entry(
    index = 122,
    label = "Rn3c8_gamma_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 123,
    label = "Rn3c8_gamma_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {10,[S,D,T,B]}
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
    index = 124,
    label = "Rn4cx",
    group = "OR{Rn4cx_alpha, Rn4cx_beta}",
    kinetics = None,
)

entry(
    index = 125,
    label = "Rn4cx_alpha",
    group = "OR{Rn4c3_alpha, Rn4c4_alpha, Rn4c5_alpha, Rn4c6_alpha, Rn4c7_alpha, Rn4c8_alpha}",
    kinetics = None,
)

entry(
    index = 126,
    label = "Rn4c3_alpha",
    group = "OR{Rn4c3_alpha_short, Rn4c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 127,
    label = "Rn4c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 128,
    label = "Rn4c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
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
    index = 129,
    label = "Rn4c4_alpha",
    group = "OR{Rn4c4_alpha_short, Rn4c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 130,
    label = "Rn4c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 131,
    label = "Rn4c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
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
    index = 132,
    label = "Rn4c5_alpha",
    group = "OR{Rn4c5_alpha_short, Rn4c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 133,
    label = "Rn4c5_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 134,
    label = "Rn4c5_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
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
    index = 135,
    label = "Rn4c6_alpha",
    group = "OR{Rn4c6_alpha_short, Rn4c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 136,
    label = "Rn4c6_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
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
    index = 137,
    label = "Rn4c6_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 138,
    label = "Rn4c7_alpha",
    group = "OR{Rn4c7_alpha_short, Rn4c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 139,
    label = "Rn4c7_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 140,
    label = "Rn4c7_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 141,
    label = "Rn4c8_alpha",
    group = "OR{Rn4c8_alpha_short, Rn4c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 142,
    label = "Rn4c8_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 143,
    label = "Rn4c8_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 144,
    label = "Rn4cx_beta",
    group = "OR{Rn4c4_beta, Rn4c5_beta, Rn4c6_beta, Rn4c7_beta, Rn4c8_beta}",
    kinetics = None,
)

entry(
    index = 145,
    label = "Rn4c4_beta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 146,
    label = "Rn4c5_beta",
    group = "OR{Rn4c5_beta_short, Rn4c5_beta_long}",
    kinetics = None,
)

entry(
    index = 147,
    label = "Rn4c5_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 148,
    label = "Rn4c5_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {9,[S,D,T,B]}
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
    index = 149,
    label = "Rn4c6_beta",
    group = "OR{Rn4c6_beta_short, Rn4c6_beta_long}",
    kinetics = None,
)

entry(
    index = 150,
    label = "Rn4c6_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
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
    index = 151,
    label = "Rn4c6_beta_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {10,[S,D,T,B]}
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
    index = 152,
    label = "Rn4c7_beta",
    group = "OR{Rn4c7_beta_short, Rn4c7_beta_long}",
    kinetics = None,
)

entry(
    index = 153,
    label = "Rn4c7_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 154,
    label = "Rn4c7_beta_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {11,[S,D,T,B]}
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
    index = 155,
    label = "Rn4c8_beta",
    group = "OR{Rn4c8_beta_short, Rn4c8_beta_long}",
    kinetics = None,
)

entry(
    index = 156,
    label = "Rn4c8_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 157,
    label = "Rn4c8_beta_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {12,[S,D,T,B]}
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
    index = 158,
    label = "Rn5cx",
    group = "OR{Rn5cx_alpha}",
    kinetics = None,
)

entry(
    index = 159,
    label = "Rn5cx_alpha",
    group = "OR{Rn5c3_alpha, Rn5c4_alpha, Rn5c5_alpha, Rn5c6_alpha, Rn5c7_alpha, Rn5c8_alpha}",
    kinetics = None,
)

entry(
    index = 160,
    label = "Rn5c3_alpha",
    group = "OR{Rn5c3_alpha_short, Rn5c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 161,
    label = "Rn5c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 162,
    label = "Rn5c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
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
    index = 163,
    label = "Rn5c4_alpha",
    group = "OR{Rn5c4_alpha_short, Rn5c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 164,
    label = "Rn5c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 165,
    label = "Rn5c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
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
    index = 166,
    label = "Rn5c5_alpha",
    group = "OR{Rn5c5_alpha_short, Rn5c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 167,
    label = "Rn5c5_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 168,
    label = "Rn5c5_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
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
    index = 169,
    label = "Rn5c6_alpha",
    group = "OR{Rn5c6_alpha_short, Rn5c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 170,
    label = "Rn5c6_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
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
    index = 171,
    label = "Rn5c6_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
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
    index = 172,
    label = "Rn5c7_alpha",
    group = "OR{Rn5c7_alpha_short, Rn5c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 173,
    label = "Rn5c7_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 174,
    label = "Rn5c7_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
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
    index = 175,
    label = "Rn5c8_alpha",
    group = "OR{Rn5c8_alpha_short, Rn5c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 176,
    label = "Rn5c8_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 177,
    label = "Rn5c8_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
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
    index = 178,
    label = "doublebond_intra",
    group = 
"""
1 *2 Cd       u0 r1 {2,D}
2 *3 [Cd,Cdd] u0 r1 {1,D}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "triplebond_intra",
    group = 
"""
1 *2 Ct u0 r1 {2,T}
2 *3 Ct u0 r1 {1,T}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "benzenebond_intra",
    group = 
"""
1 *2 [Cb,Cbf] u0 r1 {2,B}
2 *3 [Cb,Cbf] u0 r1 {1,B}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "benzenebond_intra_R",
    group = 
"""
1 *2 Cb  u0 r1 {2,B} {3,S}
2 *3 Cb  u0 r1 {1,B}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "benzenebond_intra_RH",
    group = 
"""
1 *2 Cb  u0 r1 {2,B} {3,S}
2 *3 Cb  u0 r1 {1,B} {4,S}
3    R!H u0 {1,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "benzenebond_intra_H",
    group = 
"""
1 *2 Cb u0 r1 {2,B} {3,S}
2 *3 Cb u0 r1 {1,B}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "benzenebond_intra_HH",
    group = 
"""
1 *2 Cb u0 r1 {2,B} {3,S}
2 *3 Cb u0 r1 {1,B} {4,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "benzenebond_intra_CbCbf",
    group = 
"""
1 *2 Cb  u0 r1 {2,B}
2 *3 Cbf u0 r1 {1,B}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "benzenebond_intra_CbfCb",
    group = 
"""
1 *2 Cbf u0 r1 {2,B}
2 *3 Cb  u0 r1 {1,B}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "benzenebond_intra_CbfCbf",
    group = 
"""
1 *2 Cbf u0 r1 {2,B}
2 *3 Cbf u0 r1 {1,B}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "radadd_intra_cs",
    group = 
"""
1 *1 Cs u1
""",
    kinetics = None,
)

entry(
    index = 189,
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
    index = 190,
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
    index = 191,
    label = "radadd_intra_csHDe",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 192,
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
    index = 193,
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
    index = 194,
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
    index = 195,
    label = "radadd_intra_csNdDe",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cs,O,S]      u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "radadd_intra_csNdCd",
    group = 
"""
1 *1 Cs     u1 {2,S} {3,S}
2    [Cs,O] u0 {1,S}
3    Cd     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "radadd_intra_csNdCt",
    group = 
"""
1 *1 Cs     u1 {2,S} {3,S}
2    [Cs,O] u0 {1,S}
3    Ct     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "radadd_intra_csDeDe",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "radadd_intra_O",
    group = 
"""
1 *1 O u1
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "radadd_intra_Cb",
    group = 
"""
1 *1 Cb u1
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "radadd_intra_cdsingle",
    group = 
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "radadd_intra_cdsingleH",
    group = 
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "radadd_intra_cdsingleNd",
    group = 
"""
1 *1 Cd       u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "radadd_intra_cdsingleDe",
    group = 
"""
1 *1 Cd            u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "radadd_intra_cddouble",
    group = 
"""
1 *1 Cd u1 {2,D}
2    Cd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "radadd_intra_CO",
    group = 
"""
1 *1 CO u1 {2,D}
2    O  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "radadd_intra_Ct",
    group = 
"""
1 *1 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

tree(
"""
L1: Rn_cyclic
    L2: Rn0cx
        L3: Rn0cx_beta
            L4: Rn0c4_beta
            L4: Rn0c5_beta
                L5: Rn0c5_beta_short
                L5: Rn0c5_beta_long
            L4: Rn0c6_beta
                L5: Rn0c6_beta_short
                L5: Rn0c6_beta_long
                    L6: Rn0c6_beta_long_SSSD
                    L6: Rn0c6_beta_long_SDSD
                        L7: Rn0c6_beta_long_SDSD_H
                        L7: Rn0c6_beta_long_SDSD_R1
                        L7: Rn0c6_beta_long_SDSD_R2
            L4: Rn0c7_beta
                L5: Rn0c7_beta_short
                L5: Rn0c7_beta_long
            L4: Rn0c8_beta
                L5: Rn0c8_beta_short
                L5: Rn0c8_beta_long
        L3: Rn0cx_gamma
            L4: Rn0c6_gamma
            L4: Rn0c7_gamma
                L5: Rn0c7_gamma_short
                L5: Rn0c7_gamma_long
                    L6: Rn0c7_gamma_long_SDSD
                        L7: Rn0c7_gamma_long_SDSD_R5
            L4: Rn0c8_gamma
                L5: Rn0c8_gamma_short
                L5: Rn0c8_gamma_long
        L3: Rn0cx_delta
            L4: Rn0c8_delta
    L2: Rn1cx
        L3: Rn1cx_alpha
            L4: Rn1c3_alpha
                L5: Rn1c3_alpha_short
                L5: Rn1c3_alpha_long
            L4: Rn1c4_alpha
                L5: Rn1c4_alpha_short
                L5: Rn1c4_alpha_long
            L4: Rn1c5_alpha
                L5: Rn1c5_alpha_short
                L5: Rn1c5_alpha_long
                    L6: Rn1c5_alpha_long_SSSDS
                    L6: Rn1c5_alpha_long_SDSDS
                        L7: Rn1c5_alpha_long_SDSDS_H
                        L7: Rn1c5_alpha_long_SDSDS_R
            L4: Rn1c6_alpha
                L5: Rn1c6_alpha_short
                L5: Rn1c6_alpha_long
            L4: Rn1c7_alpha
                L5: Rn1c7_alpha_short
                L5: Rn1c7_alpha_long
            L4: Rn1c8_alpha
                L5: Rn1c8_alpha_short
                L5: Rn1c8_alpha_long
    L2: Rn2cx
        L3: Rn2cx_alpha
            L4: Rn2c3_alpha
                L5: Rn2c3_alpha_short
                L5: Rn2c3_alpha_long
            L4: Rn2c4_alpha
                L5: Rn2c4_alpha_short
                L5: Rn2c4_alpha_long
            L4: Rn2c5_alpha
                L5: Rn2c5_alpha_short
                L5: Rn2c5_alpha_long
            L4: Rn2c6_alpha
                L5: Rn2c6_alpha_short
                L5: Rn2c6_alpha_long
            L4: Rn2c7_alpha
                L5: Rn2c7_alpha_short
                L5: Rn2c7_alpha_long
            L4: Rn2c8_alpha
                L5: Rn2c8_alpha_short
                L5: Rn2c8_alpha_long
        L3: Rn2cx_beta
            L4: Rn2c4_beta
            L4: Rn2c5_beta
                L5: Rn2c5_beta_short
                    L6: Rn2c5_beta_short_SDSDS
                    L6: Rn2c5_beta_short_SDSSD
                L5: Rn2c5_beta_long
            L4: Rn2c6_beta
                L5: Rn2c6_beta_short
                L5: Rn2c6_beta_long
            L4: Rn2c7_beta
                L5: Rn2c7_beta_short
                L5: Rn2c7_beta_long
            L4: Rn2c8_beta
                L5: Rn2c8_beta_short
                L5: Rn2c8_beta_long
    L2: Rn3cx
        L3: Rn3cx_alpha
            L4: Rn3c3_alpha
                L5: Rn3c3_alpha_short
                L5: Rn3c3_alpha_long
            L4: Rn3c4_alpha
                L5: Rn3c4_alpha_short
                L5: Rn3c4_alpha_long
            L4: Rn3c5_alpha
                L5: Rn3c5_alpha_short
                L5: Rn3c5_alpha_long
            L4: Rn3c6_alpha
                L5: Rn3c6_alpha_short
                L5: Rn3c6_alpha_long
            L4: Rn3c7_alpha
                L5: Rn3c7_alpha_short
                L5: Rn3c7_alpha_long
            L4: Rn3c8_alpha
                L5: Rn3c8_alpha_short
                L5: Rn3c8_alpha_long
        L3: Rn3cx_beta
            L4: Rn3c4_beta
            L4: Rn3c5_beta
                L5: Rn3c5_beta_short
                L5: Rn3c5_beta_long
            L4: Rn3c6_beta
                L5: Rn3c6_beta_short
                L5: Rn3c6_beta_long
            L4: Rn3c7_beta
                L5: Rn3c7_beta_short
                L5: Rn3c7_beta_long
            L4: Rn3c8_beta
                L5: Rn3c8_beta_short
                L5: Rn3c8_beta_long
        L3: Rn3cx_gamma
            L4: Rn3c6_gamma
            L4: Rn3c7_gamma
                L5: Rn3c7_gamma_short
                L5: Rn3c7_gamma_long
            L4: Rn3c8_gamma
                L5: Rn3c8_gamma_short
                L5: Rn3c8_gamma_long
    L2: Rn4cx
        L3: Rn4cx_alpha
            L4: Rn4c3_alpha
                L5: Rn4c3_alpha_short
                L5: Rn4c3_alpha_long
            L4: Rn4c4_alpha
                L5: Rn4c4_alpha_short
                L5: Rn4c4_alpha_long
            L4: Rn4c5_alpha
                L5: Rn4c5_alpha_short
                L5: Rn4c5_alpha_long
            L4: Rn4c6_alpha
                L5: Rn4c6_alpha_short
                L5: Rn4c6_alpha_long
            L4: Rn4c7_alpha
                L5: Rn4c7_alpha_short
                L5: Rn4c7_alpha_long
            L4: Rn4c8_alpha
                L5: Rn4c8_alpha_short
                L5: Rn4c8_alpha_long
        L3: Rn4cx_beta
            L4: Rn4c4_beta
            L4: Rn4c5_beta
                L5: Rn4c5_beta_short
                L5: Rn4c5_beta_long
            L4: Rn4c6_beta
                L5: Rn4c6_beta_short
                L5: Rn4c6_beta_long
            L4: Rn4c7_beta
                L5: Rn4c7_beta_short
                L5: Rn4c7_beta_long
            L4: Rn4c8_beta
                L5: Rn4c8_beta_short
                L5: Rn4c8_beta_long
    L2: Rn5cx
        L3: Rn5cx_alpha
            L4: Rn5c3_alpha
                L5: Rn5c3_alpha_short
                L5: Rn5c3_alpha_long
            L4: Rn5c4_alpha
                L5: Rn5c4_alpha_short
                L5: Rn5c4_alpha_long
            L4: Rn5c5_alpha
                L5: Rn5c5_alpha_short
                L5: Rn5c5_alpha_long
            L4: Rn5c6_alpha
                L5: Rn5c6_alpha_short
                L5: Rn5c6_alpha_long
            L4: Rn5c7_alpha
                L5: Rn5c7_alpha_short
                L5: Rn5c7_alpha_long
            L4: Rn5c8_alpha
                L5: Rn5c8_alpha_short
                L5: Rn5c8_alpha_long
L1: multiplebond_intra
    L2: doublebond_intra
    L2: triplebond_intra
    L2: benzenebond_intra
        L3: benzenebond_intra_R
            L4: benzenebond_intra_RH
        L3: benzenebond_intra_H
            L4: benzenebond_intra_HH
        L3: benzenebond_intra_CbCbf
        L3: benzenebond_intra_CbfCb
        L3: benzenebond_intra_CbfCbf
L1: radadd_intra
    L2: radadd_intra_cs
        L3: radadd_intra_cs2H
        L3: radadd_intra_csHNd
        L3: radadd_intra_csHDe
            L4: radadd_intra_csHCd
            L4: radadd_intra_csHCt
        L3: radadd_intra_csNdNd
        L3: radadd_intra_csNdDe
            L4: radadd_intra_csNdCd
            L4: radadd_intra_csNdCt
        L3: radadd_intra_csDeDe
    L2: radadd_intra_O
    L2: radadd_intra_Cb
    L2: radadd_intra_cdsingle
        L3: radadd_intra_cdsingleH
        L3: radadd_intra_cdsingleNd
        L3: radadd_intra_cdsingleDe
    L2: radadd_intra_cddouble
    L2: radadd_intra_CO
    L2: radadd_intra_Ct
"""
)

forbidden(
    label = "kekule_benzene",
    group = 
"""
1 *2 C ux {2,D} {6,S}
2 *3 C ux {1,D} {3,S}
3    C ux {2,S} {4,D}
4    C ux {3,D} {5,S}
5    C ux {4,S} {6,D}
6    C ux {1,S} {5,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Only aromatic benzene should react in this family.
""",
)

