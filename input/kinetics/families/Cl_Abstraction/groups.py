#!/usr/bin/env python
# encoding: utf-8

name = "Cl_Abstraction/groups"
shortDesc = u""
longDesc = u"""
The reaction site *3 needs a lone pair in order to react. It cannot be 2S or 4S.
"""

template(reactants=["X_Cl_or_Xrad_Cl_Xbirad_Cl_Xtrirad_Cl", "Y_rad_birad_trirad_quadrad"], products=["X_Cl_or_Xrad_Cl_Xbirad_Cl_Xtrirad_Cl", "Y_rad_birad_trirad_quadrad"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "X_Cl_or_Xrad_Cl_Xbirad_Cl_Xtrirad_Cl",
    group = "OR{X_Cl, Xrad_Cl, Xbirad_Cl, Xtrirad_Cl}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad, Y_1centertrirad, Y_1centerquadrad}",
    kinetics = None,
)

entry(
    index = 3,
    label = "X_Cl",
    group =
"""
1 *1 R u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Cl2",
    group =
"""
1 *1 [H,Cl] u0 {2,S}
2 *2 Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Ct_Cl",
    group =
"""
1 *1 Ct    u0 {2,S} {3,T}
2 *2 Cl     u0 {1,S}
3    [C,N] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 457,
    label = "Ct/Cl/NonDeC",
    group =
"""
1 *1 Ct u0 {2,S} {3,T}
2 *2 Cl  u0 {1,S}
3    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 458,
    label = "Ct/Cl/NonDeN",
    group =
"""
1 *1 Ct  u0 {2,S} {3,T}
2 *2 Cl   u0 {1,S}
3    N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Cd_Cl",
    group =
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2    C u0 {1,D}
3 *2 Cl     u0 {1,S}
4    R     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Cd_pri",
    group =
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 Cl     u0 {1,S}
4    H     u0 {1,S}
5   R   u0 {2,S}
""",
    kinetics = None,
)


entry(
    index = 30,
    label = "Cd_sec",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cd  u0 {1,D} {5,S}
3 *2 Cl   u0 {1,S}
4    R!H u0 {1,S}
5   R u0 {2,S}
""",
    kinetics = None,
)
entry(
    index = 40,
    label = "Cd_allenic",
    group =
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 Cdd u0 {1,D}
3 *2 Cl u0 {1,S}
4 R u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 60,
    label = "Cs_Cl",
    group =
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cl u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
5    R u0 {1,S}
""",
    kinetics = None,
)

#entry(
#    index = 61,
#    label = "C_methane",
#    group =
#"""
#1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
#2 *2 Cl u0 {1,S}
#3    [H,Cl] u0 {1,S}
#4    [H,Cl] u0 {1,S}
#5    [H,Cl] u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 62,
#    label = "C_pri",
#    group =
#"""
#1 *1 C       u0 {2,S} {3,S} {4,S} {5,S}
#2 *2 Cl      u0 {1,S}
#3    [H,Cl]  u0 {1,S}
#4    [H,Cl]  u0 {1,S}
#5    R!H     u0 {1,S}
#""",
#    kinetics = None,
#)

entry(
    index = 83,
    label = "C_sec",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cl   u0 {1,S}
3    [H,Cl]   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "C_ter",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cl   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Xrad_Cl",
    group =
"""
1 *1 R u1 {2,S}
2 *2 Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 469,
    label = "C_rad_Cl",
    group =
"""
1 *1 C u1 {2,S}
2 *2 Cl u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 442,
    label = "C_H2_Cl2_HCl_rad_Cl",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Cl  u0 {1,S}
3    [H,Cl]  u0 {1,S}
4    [H,Cl]  u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 444,
    label = "Xbirad_Cl",
    group = "OR{C_HCl_Cl2_triplet_Cl, C_HCl_Cl2_singlet_Cl}",
    kinetics = None,
)

entry(
    index = 476,
    label = "C_HCl_Cl2_triplet_Cl",
    group =
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 Cl  u0 {1,S}
3    [H,Cl]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 477,
    label = "C_HCl_Cl2_singlet_Cl",
    group =
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 Cl u0 {1,S}
3    [H,Cl] u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 474,
    label = "Xtrirad_Cl",
    group = "OR{C_quartet_Cl, C_doublet_Cl}",
    kinetics = None,
)

entry(
    index = 480,
    label = "C_quartet_Cl",
    group =
"""
1 *1 C u3 p0 {2,S}
2 *2 Cl u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 481,
    label = "C_doublet_Cl",
    group =
"""
1 *1 C u1 p1 {2,S}
2 *2 Cl u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 475,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet}",
    kinetics = None,
)
entry(
    index = 482,
    label = "C_quintet",
    group =
"""
1 *3 C u4 p0
""",
    kinetics = None,
)

entry(
    index = 483,
    label = "C_triplet",
    group =
"""
1 *3 C u2 p1
""",
    kinetics = None,
)

entry(
    index = 419,
    label = "Y_1centertrirad",
    group = "OR{C_H_Cl_quartet, C_H_Cl_doublet}",
    kinetics = None,
)


entry(
    index = 487,
    label = "C_H_Cl_quartet",
    group =
"""
1 *3 C u3 p0 {2,S}
2    [H,Cl] u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 487,
    label = "C_H_Cl_doublet",
    group =
"""
1 *3 C u1 p1 {2,S}
2    [H,Cl] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Y_1centerbirad",
    group =
"""
1 *3 [Cs,Cd,CO,CS,O,S,N,Cl] u2
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "O_atom_triplet",
    group =
"""
1 *3 O u2
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "CH2_triplet",
    group =
"""
1 *3 Cs u2 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 422,
    label = "NH_triplet",
    group =
"""
1 *3 N3s u2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "Y_rad",
    group =
"""
1 *3 R u1
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "H_rad",
    group =
"""
1 *3 H u1
""",
    kinetics = None,
)

entry(
    index = 19200,
    label = "Cl_rad",
    group =
"""
1 *3 Cl u1
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "Y_2centeradjbirad",
    group =
"""
1 *3 [Ct,O2s,S2s] u1 {2,[S,T]}
2    [Ct,O2s,S2s] u1 {1,[S,T]}
""",
    kinetics = None,
)


entry(
    index = 197,
    label = "O_rad",
    group =
"""
1 *3 O u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "O_pri_rad",
    group =
"""
1 *3 O u1 {2,S}
2    [H,Cl] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "O_sec_rad",
    group =
"""
1 *3 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 223,
    label = "Cd_rad",
    group =
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 260,
    label = "Cs_rad",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

#entry(
#    index = 261,
#    label = "C_methyl",
#    group =
#"""
#1 *3 C u1 {2,S} {3,S} {4,S}
#2    H u0 {1,S}
#3    H u0 {1,S}
#4    H u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 26100,
#    label = "C_Chloro",
#    group =
#"""
#1 *3 C u1 {2,S} {3,S} {4,S}
#2    Cl u0 {1,S}
#3    Cl u0 {1,S}
#4    Cl u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 262,
#    label = "C_pri_rad",
#    group =
#"""
#1 *3 C   u1 {2,S} {3,S} {4,S}
#2    [H,Cl]   u0 {1,S}
#3    [H,Cl]   u0 {1,S}
#4    R!H u0 {1,S}
#""",
#    kinetics = None,
#)
#
#
#
#entry(
#    index = 279,
#    label = "C_sec_rad",
#    group =
#"""
#1 *3 C   u1 {2,S} {3,S} {4,S}
#2    [H,Cl]   u0 {1,S}
#3    R!H u0 {1,S}
#4    R!H u0 {1,S}
#""",
#    kinetics = None,
#)
#
#
#entry(
#    index = 328,
#    label = "C_ter_rad",
#    group =
#"""
#1 *3 C   u1 {2,S} {3,S} {4,S}
#2    R!H u0 {1,S}
#3    R!H u0 {1,S}
#4    R!H u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 329,
#    label = "C_rad/NonDe",
#    group =
#"""
#1 *3 C        u1 {2,S} {3,S} {4,S}
#2    [Cs,O,S] u0 {1,S}
#3    [Cs,O,S] u0 {1,S}
#4    [Cs,O,S] u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 344,
#    label = "C_rad/OneDe",
#    group =
#"""
#1 *3 C             u1 {2,S} {3,S} {4,S}
#2    [Cd,Ct,Cb,CO] u0 {1,S}
#3    [Cs,O,S]      u0 {1,S}
#4    [Cs,O,S]      u0 {1,S}
#""",
#    kinetics = None,
#)
#
#
#entry(
#    index = 360,
#    label = "C_rad/TwoDe",
#    group =
#"""
#1 *3 C             u1 {2,S} {3,S} {4,S}
#2    [Cd,Ct,Cb,CO] u0 {1,S}
#3    [Cd,Ct,Cb,CO] u0 {1,S}
#4    [Cs,O,S]      u0 {1,S}
#""",
#    kinetics = None,
#)
#
#entry(
#    index = 379,
#    label = "C_rad/ThreeDe",
#    group =
#"""
#1 *3 C             u1 {2,S} {3,S} {4,S}
#2    [Cd,Ct,Cb,CO] u0 {1,S}
#3    [Cd,Ct,Cb,CO] u0 {1,S}
#4    [Cd,Ct,Cb,CO] u0 {1,S}
#""",
#    kinetics = None,
#)
#
tree(
"""
L1: X_Cl_or_Xrad_Cl_Xbirad_Cl_Xtrirad_Cl
    L2: X_Cl
        L3: Cl2
        L3: Ct_Cl
            L4: Ct/Cl/NonDeC
            L4: Ct/Cl/NonDeN
        L3: Cd_Cl
            L4: Cd_pri
            L4: Cd_sec
            L4: Cd_allenic
        L3: Cs_Cl
            L4: C_sec
            L4: C_ter
    L2: Xrad_Cl
        L3: C_rad_Cl
            L4: C_H2_Cl2_HCl_rad_Cl
    L2: Xbirad_Cl
        L3: C_HCl_Cl2_triplet_Cl
        L3: C_HCl_Cl2_singlet_Cl
    L2: Xtrirad_Cl
        L3: C_quartet_Cl
        L3: C_doublet_Cl
L1: Y_rad_birad_trirad_quadrad
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
    L2: Y_1centertrirad
        L3: C_H_Cl_quartet
        L3: C_H_Cl_doublet
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CH2_triplet
        L3: NH_triplet
    L2: Y_rad
        L3: H_rad
        L3: Cl_rad
        L3: Y_2centeradjbirad
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
        L3: Cs_rad
        L3: Cd_rad

"""
)

forbidden(
    label = "OS_birad_singlet",
    group =
"""
1 *3 [O,S] u0 p3
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "birad_singlet",
    group =
"""
1 *3 [C,N,Si] u0 p1
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "quadrad_singlet",
    group =
"""
1 *3 [C,N,Si] u0 p2
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)


forbidden(
    label = "disprop1",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    C u1 {1,S}
3 *2 Cl u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "disprop2",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    R u0 {1,S} {4,D}
3 *2 Cl u0 {1,S}
4    R u0 {2,D} {5,S}
5    R u1 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "disprop3",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    R u0 {1,S} {4,T}
3 *2 Cl u0 {1,S}
4    R u0 {2,T} {5,S}
5    R u1 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "disprop4",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    R u0 {1,S} {4,D}
3 *2 Cl u0 {1,S}
4    R u0 {2,D} {5,S}
5    R u0 {4,S} {6,D}
6    R u0 {5,D} {7,S}
7    R u1 {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

forbidden(
    label = "disprop5",
    group =
"""
1 *1 R u0 {2,S} {3,S}
2    R u0 {1,S} {4,D}
3 *2 Cl u0 {1,S}
4    R u0 {2,D} {5,S}
5    R u0 {4,S} {6,D}
6    R u0 {5,D} {7,S}
7    R u1 {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)
