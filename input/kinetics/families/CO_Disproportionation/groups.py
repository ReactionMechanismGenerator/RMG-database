#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:
Y_rad + [CH]=O <=> Y_H + [C-]#[O+]

atom labels:

  R_rad   +        [CH]=O        <=>     RH     +    [C-]#[O+]

R_rad(*1) + H(*4)C_rad(*3)=O(*2) <=> R(*1)H(*4) + [C-](*3)#[O+](*2)
"""

template(reactants=["Y_rad_birad_trirad_quadrad", "HCO_HCS"], products=["Y_H", "CO_CS"], ownReverse=False)

reverse = "CO_Addition"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['LOSE_PAIR', '*2', '1'],
    ['GAIN_PAIR', '*3', '1'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
    ['GAIN_CHARGE', '*2', '1'],
    ['LOSE_CHARGE', '*3', '1'],
])

entry(
    index = 1,
    label = "Y_rad_birad_trirad_quadrad",
    group ="OR{Y_1centerquadrad, Y_1centertrirad, Y_2centerbirad, Y_1centerbirad, Y_rad}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Y_1centerquadrad",
    group ="OR{C_quintet, C_triplet}",
    kinetics = None,
)

entry(
    index = 3,
    label = "C_quintet",
    group =
"""
1 *1 C u4 p0
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C_triplet",
    group =
"""
1 *1 C u2 p1
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Y_1centertrirad",
    group ="OR{N_atom_quartet, N_atom_doublet, CH_quartet, CH_doublet}",
    kinetics = None,
)

entry(
    index = 6,
    label = "N_atom_quartet",
    group =
"""
1 *1 N u3 p1
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "N_atom_doublet",
    group =
"""
1 *1 N u1 p2
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CH_quartet",
    group =
"""
1 *1 C u3 p0 {2,S}
2    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CH_doublet",
    group =
"""
1 *1 C u1 p1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Y_2centerbirad",
    group ="OR{O2b, C2b, S2b}",
    kinetics = None,
)

entry(
    index = 11,
    label = "O2b",
    group =
"""
1 *1 O u1 {2,S}
2    O u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "C2b",
    group =
"""
1 *1 C u1 {2,T}
2    C u1 {1,T}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "S2b",
    group =
"""
1 *1 S u1 {2,S}
2    S u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Y_1centerbirad",
    group =
"""
1 *1 R!H u2
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "CO_birad_triplet",
    group =
"""
1 *1 C  u2 {2,D}
2    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "O_atom_triplet",
    group =
"""
1 *1 O u2
""",
    kinetics = None,
)

entry(
    index = 505,
    label = "CS_birad_triplet",
    group =
"""
1 *1 C   u2 {2,D}
2    S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 506,
    label = "S_atom_triplet",
    group =
"""
1 *1 S2s u2 p2
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "CH2_triplet",
    group =
"""
1 *1 C u2 {2,S} {3,S}
2    H u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "NH_triplet",
    group =
"""
1 *1 N3s u2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Y_rad",
    group =
"""
1 *1 R u1
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "H_rad",
    group =
"""
1 *1 H u1
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Ct_rad",
    group =
"""
1 *1 Ct  u1 {2,T}
2    R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Ct_rad/Ct",
    group =
"""
1 *1 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Ct_rad/Nt",
    group =
"""
1 *1 Ct        u1 {2,T}
2    [N3t,N5tc] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "O_rad",
    group =
"""
1 *1 O u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "O_pri_rad",
    group =
"""
1 *1 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "O_sec_rad",
    group =
"""
1 *1 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "O_rad/NonDeC",
    group =
"""
1 *1 O  u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "O_rad/NonDeO",
    group =
"""
1 *1 O u1 {2,S}
2    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "O_rad/NonDeN",
    group =
"""
1 *1 O   u1 {2,S}
2    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "O_rad/OneDe",
    group =
"""
1 *1 O             u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "S_rad",
    group =
"""
1 *1 S u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "S_pri_rad",
    group =
"""
1 *1 S u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "S_sec_rad",
    group =
"""
1 *1 S   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "S_rad/NonDeC",
    group =
"""
1 *1 S  u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "S_rad/NonDeS",
    group =
"""
1 *1 S u1 {2,S}
2    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "S_rad/OneDe",
    group =
"""
1 *1 S             u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
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
    index = 38,
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
    index = 39,
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
    index = 40,
    label = "Cd_rad/NonDeC",
    group =
"""
1 *1 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Cd_rad/NonDeN",
    group =
"""
1 *1 C   u1 {2,D} {3,S}
2    C   u0 {1,D}
3    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Cd_rad/NonDeO",
    group =
"""
1 *1 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Cd_rad/NonDeS",
    group =
"""
1 *1 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
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
    index = 44,
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
    index = 45,
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
    index = 46,
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
    index = 47,
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
    index = 48,
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
    index = 49,
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
    index = 510,
    label = "CS_rad",
    group =
"""
1 *1 C   u1 {2,D} {3,S}
2    S2d u0 {1,D}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 511,
    label = "CS_pri_rad",
    group =
"""
1 *1 C   u1 {2,D} {3,S}
2    S2d u0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 512,
    label = "CS_sec_rad",
    group =
"""
1 *1 C   u1 {2,D} {3,S}
2    S2d u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 513,
    label = "CS_rad/NonDe",
    group =
"""
1 *1 C        u1 {2,D} {3,S}
2    S2d      u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 514,
    label = "CS_rad/OneDe",
    group =
"""
1 *1 C                u1 {2,D} {3,S}
2    S2d              u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
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
    index = 51,
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
    index = 52,
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
    index = 53,
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
    index = 54,
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
    index = 55,
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
    index = 56,
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
    index = 57,
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
    index = 58,
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
    index = 520,
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
    index = 521,
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
    index = 59,
    label = "C_rad/H2/N",
    group =
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    N u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
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
    index = 61,
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
    index = 62,
    label = "C_rad/H/NonDeO",
    group =
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    H        u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
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
    index = 64,
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
    index = 65,
    label = "C_rad/H/NonDeN",
    group =
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    H        u0 {1,S}
3    N        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "C_rad/H/NonDeS",
    group =
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    H        u0 {1,S}
3    S        u0 {1,S}
4    [Cs,S,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "C_rad/H/CsS",
    group =
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "C_rad/H/S2",
    group =
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    S u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 530,
    label = "C_rad/H/SO",
    group =
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    S u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "C_rad/H/OneDe",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "C_rad/H/OneDeC",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "C_rad/H/OneDeO",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "C_rad/H/OneDeN",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    N             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "C_rad/H/TwoDe",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
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
    index = 75,
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
    index = 76,
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
    index = 77,
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
    index = 78,
    label = "C_rad/OneDe",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "C_rad/Cs2",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Cs            u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "C_rad/ODMustO",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O             u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "C_rad/TwoDe",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "C_rad/Cs",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "C_rad/TDMustO",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "C_rad/ThreeDe",
    group =
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "N3_rad",
    group =
"""
1 *1 [N3s,N3d] u1
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "N3s_rad",
    group =
"""
1 *1 N3s u1
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "NH2_rad",
    group =
"""
1 *1 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "N3s_rad_pri",
    group =
"""
1 *1 N3s u1 {2,S} {3,S}
2    R!H u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "N3s_rad/H/NonDe",
    group =
"""
1 *1 N3s         u1 {2,S} {3,S}
2    [Cs,N3s,O2s] u0 {1,S}
3    H           u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "N3s_rad/H/NonDeC",
    group =
"""
1 *1 N3s u1 {2,S} {3,S}
2    Cs  u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "N3s_rad/H/NonDeO",
    group =
"""
1 *1 N3s u1 {2,S} {3,S}
2    O2s  u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "N3s_rad/H/NonDeN",
    group =
"""
1 *1 N3s u1 {2,S} {3,S}
2    N3s u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "N3s_rad/H/OneDe",
    group =
"""
1 *1 N3s                      u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
3    H                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "N3s_rad_sec",
    group =
"""
1 *1 N3s u1 {2,S} {3,S}
2    R!H u0 {1,S}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "N3s_rad/NonDe2",
    group =
"""
1 *1 N3s         u1 {2,S} {3,S}
2    [Cs,N3s,O2s] u0 {1,S}
3    [Cs,N3s,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "N3s_rad/OneDe",
    group =
"""
1 *1 N3s                      u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
3    [Cs,N3s,O2s]              u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "N3s_rad/TwoDe",
    group =
"""
1 *1 N3s                      u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "N3d_rad",
    group =
"""
1 *1 N3d u1
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "N3d_rad/C",
    group =
"""
1 *1 N3d u1 {2,D}
2    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "N3d_rad/O",
    group =
"""
1 *1 N3d u1 {2,D}
2    O2d  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "N3d_rad/N",
    group =
"""
1 *1 N3d u1 {2,D}
2    N   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 540,
    label = "N3d_rad/S",
    group =
"""
1 *1 N3d u1 {2,D}
2    S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "N5_rad",
    group =
"""
1 *1 [N5sc,N5dc,N5t,N5tc,N5b] u1
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "N5s_rad",
    group =
"""
1 *1 N5sc u1 p0
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "N5dc_rad",
    group =
"""
1 *1 N5dc u1 p0 c+1 {2,D} {3,S}
2    R!H u0 px c0  {1,D}
3    [C2sc,N1sc,O0sc,S0sc,S2sc,S2dc,S4dc,S4tdc,S6sc,S6dc,S6tdc] u0 px c-1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "N5t_rad",
    group =
"""
1 *1 N5tc u1 p0 cx {2,T}
2    R!H ux px cx {1,T}
""",
    kinetics = None,
)

entry(
    index = 501,
    label = "HCO_HCS",
    group =
"""
1 *3 C       u1 p0 c0 {2,S} {3,D}
2 *4 H       u0 p0 c0 {1,S}
3 *2 [O,S2d] u0 p2 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 502,
    label = "HCO",
    group =
"""
1 *3 C u1 p0 c0 {2,S} {3,D}
2 *4 H u0 p0 c0 {1,S}
3 *2 O u0 p2 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 503,
    label = "HCS",
    group =
"""
1 *3 C   u1 p0 c0 {2,S} {3,D}
2 *4 H   u0 p0 c0 {1,S}
3 *2 S2d u0 p2 c0 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: Y_rad_birad_trirad_quadrad
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
    L2: Y_1centertrirad
        L3: N_atom_quartet
        L3: N_atom_doublet
        L3: CH_quartet
        L3: CH_doublet
    L2: Y_2centerbirad
        L3: O2b
        L3: C2b
        L3: S2b
    L2: Y_1centerbirad
        L3: CO_birad_triplet
        L3: O_atom_triplet
        L3: CS_birad_triplet
        L3: S_atom_triplet
        L3: CH2_triplet
        L3: NH_triplet
    L2: Y_rad
        L3: H_rad
        L3: Ct_rad
            L4: Ct_rad/Ct
            L4: Ct_rad/Nt
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                L5: O_rad/NonDeO
                L5: O_rad/NonDeN
                L5: O_rad/OneDe
        L3: S_rad
            L4: S_pri_rad
            L4: S_sec_rad
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/OneDe
        L3: Cd_rad
            L4: Cd_pri_rad
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                L5: Cd_rad/NonDeN
                L5: Cd_rad/NonDeO
                L5: Cd_rad/NonDeS
                L5: Cd_rad/OneDe
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: CS_rad
            L4: CS_pri_rad
            L4: CS_sec_rad
                L5: CS_rad/NonDe
                L5: CS_rad/OneDe
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                L5: C_rad/H2/Cd
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
                L5: C_rad/H2/CS
                L5: C_rad/H2/S
                L5: C_rad/H2/N
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                    L6: C_rad/H/O2
                L5: C_rad/H/NonDeS
                    L6: C_rad/H/CsS
                    L6: C_rad/H/S2
                L5: C_rad/H/NonDeN
                L5: C_rad/H/NonDeS
                    L6: C_rad/H/CsS
                    L6: C_rad/H/S2
                    L6: C_rad/H/SO
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                    L6: C_rad/H/OneDeO
                    L6: C_rad/H/OneDeN
                L5: C_rad/H/TwoDe
            L4: C_ter_rad
                L5: C_rad/NonDeC
                    L6: C_rad/Cs3
                    L6: C_rad/NDMustO
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                    L6: C_rad/ODMustO
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                    L6: C_rad/TDMustO
                L5: C_rad/ThreeDe
        L3: N3_rad
            L4: N3s_rad
                L5: NH2_rad
                L5: N3s_rad_pri
                    L6: N3s_rad/H/NonDe
                        L7: N3s_rad/H/NonDeC
                        L7: N3s_rad/H/NonDeO
                        L7: N3s_rad/H/NonDeN
                    L6: N3s_rad/H/OneDe
                L5: N3s_rad_sec
                    L6: N3s_rad/NonDe2
                    L6: N3s_rad/OneDe
                    L6: N3s_rad/TwoDe
            L4: N3d_rad
                L5: N3d_rad/C
                L5: N3d_rad/O
                L5: N3d_rad/N
                L5: N3d_rad/S
        L3: N5_rad
            L4: N5s_rad
            L4: N5dc_rad
            L4: N5t_rad
L1: HCO_HCS
    L2: HCO
    L2: HCS
"""
)

forbidden(
    label = "O2d",
    group =
"""
1 *2 O u0 {2,D}
2 *3 O u0 {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "OS_XH_birad_singlet",
    group =
"""
1 *3 [O,S] u0 p3 {2,[S,D,T]}
2 *2 R!H   ux {1,[S,D,T]} {3,S}
3 *4 H     u0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "O_Orad",
    group =
"""
1 *2 O u0 {2,S} {3,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "XH_birad_singlet",
    group =
"""
1 *3 [C,Si] u0 p1 {2,[S,D,T]}
2 *2 R!H      ux {1,[S,D,T]} {3,S}
3 *4 H        u0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "XH_quadrad_singlet",
    group =
"""
1 *3 [C,Si] u0 p2 {2,[S,D,T]}
2 *2 R!H      ux {1,[S,D,T]} {3,S}
3 *4 H        u0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "XH_N_birad_singlet",
    group =
"""
1 *3 N u0 p2 {2,[S,D]}
2 *2 R!H      ux {1,[S,D]} {3,S}
3 *4 H        u0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

