#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/groups"
shortDesc = u""
longDesc = u"""
This reaction family is reserved for recombination of O_atom, S_atom, N_R_birad (triplets only).
The forbidden groups at the bottom prevent it from reacting with other forms of O, S, NH.
"""

template(reactants=["Y_rad", "Birad"], products=["YOS."], ownReverse=False)

reverse = "ROS_Bond_Dissociation"
reversible = True

only_forward = True

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 0,
    label = "Y_rad",
    group = 
"""
1 *1 R u1
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "Birad",
    group = 
"""
1 *2 R!H u2
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "H_rad",
    group = 
"""
1 *1 H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Ct_rad",
    group = 
"""
1 *1 C u1 {2,T}
2    C u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O_rad",
    group = 
"""
1 *1 O u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O_pri_rad",
    group = 
"""
1 *1 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "O_sec_rad",
    group = 
"""
1 *1 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "O_rad/NonDe",
    group = 
"""
1 *1 O        u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "O_rad/OneDe",
    group = 
"""
1 *1 O                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "S_rad",
    group = 
"""
1 *1 S u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "S_pri_rad",
    group = 
"""
1 *1 S u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "S_sec_rad",
    group = 
"""
1 *1 S   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "S_rad/NonDe",
    group = 
"""
1 *1 S        u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "S_rad/OneDe",
    group = 
"""
1 *1 S                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Cd_rad",
    group = 
"""
1 *1 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Cd_pri_rad",
    group = 
"""
1 *1 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Cd_sec_rad",
    group = 
"""
1 *1 C   u1 {2,D} {3,S}
2    C   u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Cd_rad/NonDe",
    group = 
"""
1 *1 C        u1 {2,D} {3,S}
2    C        u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Cd_rad/OneDe",
    group = 
"""
1 *1 C                u1 {2,D} {3,S}
2    C                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Cb_rad",
    group = 
"""
1 *1 Cb       u1 {2,B} {3,B}
2    [Cb,Cbf] u0 {1,B}
3    [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "CO_rad",
    group = 
"""
1 *1 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "CO_pri_rad",
    group = 
"""
1 *1 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "CO_sec_rad",
    group = 
"""
1 *1 C   u1 {2,D} {3,S}
2    O   u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "CO_rad/NonDe",
    group = 
"""
1 *1 C        u1 {2,D} {3,S}
2    O        u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CO_rad/OneDe",
    group = 
"""
1 *1 C                u1 {2,D} {3,S}
2    O                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CS_rad",
    group = 
"""
1 *1 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "CS_pri_rad",
    group = 
"""
1 *1 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "CS_sec_rad",
    group = 
"""
1 *1 C   u1 {2,D} {3,S}
2    S   u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CS_rad/NonDe",
    group = 
"""
1 *1 C        u1 {2,D} {3,S}
2    S        u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "CS_rad/OneDe",
    group = 
"""
1 *1 C                u1 {2,D} {3,S}
2    S                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Cs_rad",
    group = 
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "C_methyl",
    group = 
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "C_pri_rad",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "C_rad/H2/Cs",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "C_rad/H2/Cd",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "C_rad/H2/Ct",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "C_rad/H2/Cb",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "C_rad/H2/CO",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "C_rad/H2/CS",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "C_rad/H2/O",
    group = 
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "C_rad/H2/S",
    group = 
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "C_sec_rad",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    H        u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "C_rad/H/CsO",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "C_rad/H/O2",
    group = 
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    O u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "C_rad/H/NonDeS",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    H        u0 {1,S}
3    S        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "C_rad/H/OneDe",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "C_rad/H/OneDeO",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "C_rad/H/OneDeS",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "C_ter_rad",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    R!H u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "C_rad/NonDeC",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "C_rad/Cs3",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "C_rad/NDMustO",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    O        u0 {1,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "C_rad/OneDe",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "C_rad/Cs2",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Cs               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "C_rad/ODMustO",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O                u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "C_rad/TwoDe",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "C_rad/Cs",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "C_rad/TDMustO",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "C_rad/ThreeDe",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "O_birad",
    group = 
"""
1 *2 O u2 p2
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "S_birad",
    group = 
"""
1 *2 S u2 p2
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "N_R_birad",
    group = 
"""
1 *2 N u2 p1
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "N_birad/H",
    group = 
"""
1 *2 N u2 p1 {2,S}
2    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "N_birad/C",
    group = 
"""
1 *2 N u2 p1 {2,S}
2    C ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "N_birad/O",
    group = 
"""
1 *2 N u2 p1 {2,S}
2    O ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "N_birad/N",
    group = 
"""
1 *2 N u2 p1 {2,S}
2    N ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "N_birad/S",
    group = 
"""
1 *2 N u2 p1 {2,S}
2    S ux {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: Y_rad
    L2: H_rad
    L2: Ct_rad
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
    L2: S_rad
        L3: S_pri_rad
        L3: S_sec_rad
            L4: S_rad/NonDe
            L4: S_rad/OneDe
    L2: Cd_rad
        L3: Cd_pri_rad
        L3: Cd_sec_rad
            L4: Cd_rad/NonDe
            L4: Cd_rad/OneDe
    L2: Cb_rad
    L2: CO_rad
        L3: CO_pri_rad
        L3: CO_sec_rad
            L4: CO_rad/NonDe
            L4: CO_rad/OneDe
    L2: CS_rad
        L3: CS_pri_rad
        L3: CS_sec_rad
            L4: CS_rad/NonDe
            L4: CS_rad/OneDe
    L2: Cs_rad
        L3: C_methyl
        L3: C_pri_rad
            L4: C_rad/H2/Cs
            L4: C_rad/H2/Cd
            L4: C_rad/H2/Ct
            L4: C_rad/H2/Cb
            L4: C_rad/H2/CO
            L4: C_rad/H2/CS
            L4: C_rad/H2/O
            L4: C_rad/H2/S
        L3: C_sec_rad
            L4: C_rad/H/NonDeC
            L4: C_rad/H/NonDeO
                L5: C_rad/H/CsO
                L5: C_rad/H/O2
            L4: C_rad/H/NonDeS
            L4: C_rad/H/OneDe
                L5: C_rad/H/OneDeC
                L5: C_rad/H/OneDeO
                L5: C_rad/H/OneDeS
            L4: C_rad/H/TwoDe
        L3: C_ter_rad
            L4: C_rad/NonDeC
                L5: C_rad/Cs3
                L5: C_rad/NDMustO
            L4: C_rad/OneDe
                L5: C_rad/Cs2
                L5: C_rad/ODMustO
            L4: C_rad/TwoDe
                L5: C_rad/Cs
                L5: C_rad/TDMustO
            L4: C_rad/ThreeDe
L1: Birad
    L2: O_birad
    L2: S_birad
    L2: N_R_birad
        L3: N_birad/H
        L3: N_birad/C
        L3: N_birad/O
        L3: N_birad/N
        L3: N_birad/S
"""
)

forbidden(
    label = "O2_p1",
    group = 
"""
1 *2 O u2 p1
""",
    shortDesc = u"""""",
    longDesc = 
u"""
This family is intended to handle
[O] u2 p2,    or
[S] u2 p2,    or
[NH] u2 p1,
instances with a different number of lone pairs are forbidden
""",
)

forbidden(
    label = "OS_chain",
    group = 
"""
1 *1 [O,S] u1 p2 {2,S}
2    [O,S] u0 p2 {1,S} {3,S}
3    [O,S] u0 p2 {2,S} {4,S}
4    [O,S] u1 p2 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Group added to forbid this family from forming S-O chains
""",
)

forbidden(
    label = "S2_p0",
    group = 
"""
1 *2 S u2 p0
""",
    shortDesc = u"""""",
    longDesc = 
u"""
This family is intended to handle
[O] u2 p2,    or
[S] u2 p2,    or
[NH] u2 p1,
instances with a different number of lone pairs are forbidden
""",
)

forbidden(
    label = "S2_p1",
    group = 
"""
1 *2 S u2 p1
""",
    shortDesc = u"""""",
    longDesc = 
u"""
This family is intended to handle
[O] u2 p2,    or
[S] u2 p2,    or
[NH] u2 p1,
instances with a different number of lone pairs are forbidden
""",
)

