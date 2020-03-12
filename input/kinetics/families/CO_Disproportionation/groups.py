#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/groups"
shortDesc = ""
longDesc = """
This family describes reactions of the sort:
Y_rad + [CH]=O <=> Y_H + [C-]#[O+]

atom labels:

  R_rad   +        [CH]=O        <=>     RH     +    [C-]#[O+]

R_rad(*1) + H(*4)C_rad(*3)=O(*2) <=> R(*1)H(*4) + [C-](*3)#[O+](*2)
"""

template(reactants=["Y_rad_birad_trirad_quadrad", "HCO_HCS"], products=["Y_H", "CO_CS"], ownReverse=False)

reverse = "CO_Addition"
reversible = True

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['LOSE_PAIR', '*2', '1'],
    ['GAIN_PAIR', '*3', '1'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 0,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_1centerquadrad, Y_1centertrirad, Y_2centerbirad, Y_1centerbirad, Y_rad}",
    kinetics = None,
)

entry(
    index = 1,
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
    index = 2,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet}",
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
    group = "OR{N_atom_quartet, N_atom_doublet, C/H_or_Val7/quartet, C/H_or_Val7/doublet}",
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
    label = "C/H_or_Val7/quartet",
    group = 
"""
1 *1 C        u3 p0 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CH_quartet",
    group = 
"""
1 *1 C u3 p0 {2,S}
2    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "CH_quartet-F",
    group = 
"""
1 *1 C   u3 p0 {2,S}
2    F1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "CH_quartet-Cl",
    group = 
"""
1 *1 C    u3 p0 {2,S}
2    Cl1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "CH_quartet-Br",
    group = 
"""
1 *1 C    u3 p0 {2,S}
2    Br1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "C/H_or_Val7/doublet",
    group = 
"""
1 *1 C        u1 p1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "CH_doublet",
    group = 
"""
1 *1 C u1 p1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "CH_doublet-F",
    group = 
"""
1 *1 C   u1 p1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "CH_doublet-Cl",
    group = 
"""
1 *1 C    u1 p1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "CH_doublet-Br",
    group = 
"""
1 *1 C    u1 p1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Y_2centerbirad",
    group = "OR{O2b, C2b, S2b}",
    kinetics = None,
)

entry(
    index = 19,
    label = "O2b",
    group = 
"""
1 *1 O u1 {2,S}
2    O u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "C2b",
    group = 
"""
1 *1 C u1 {2,T}
2    C u1 {1,T}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "S2b",
    group = 
"""
1 *1 S u1 {2,S}
2    S u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Y_1centerbirad",
    group = 
"""
1 *1 R!H u2
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "CO_birad_triplet",
    group = 
"""
1 *1 C   u2 {2,D}
2    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "O_atom_triplet",
    group = 
"""
1 *1 O u2
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CS_birad_triplet",
    group = 
"""
1 *1 C   u2 {2,D}
2    S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "S_atom_triplet",
    group = 
"""
1 *1 S2s u2 p2
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "C/H_or_Val7/2_triplet",
    group = 
"""
1 *1 C        u2 {2,S} {3,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
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
    index = 29,
    label = "CH2_triplet-HF",
    group = 
"""
1 *1 C   u2 {2,S} {3,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "CH2_triplet-HCl",
    group = 
"""
1 *1 C    u2 {2,S} {3,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "CH2_triplet-HBr",
    group = 
"""
1 *1 C    u2 {2,S} {3,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "CH2_triplet-FF",
    group = 
"""
1 *1 C   u2 {2,S} {3,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "CH2_triplet-FCl",
    group = 
"""
1 *1 C    u2 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "CH2_triplet-FBr",
    group = 
"""
1 *1 C    u2 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "CH2_triplet-ClCl",
    group = 
"""
1 *1 C    u2 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "CH2_triplet-ClBr",
    group = 
"""
1 *1 C    u2 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "CH2_triplet-BrBr",
    group = 
"""
1 *1 C    u2 {2,S} {3,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "N/H_or_Val7/triplet",
    group = 
"""
1 *1 N3s      u2 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "NH_triplet",
    group = 
"""
1 *1 N3s u2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "NH_triplet-F",
    group = 
"""
1 *1 N3s u2 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "NH_triplet-Cl",
    group = 
"""
1 *1 N3s  u2 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "NH_triplet-Br",
    group = 
"""
1 *1 N3s  u2 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "Y_rad",
    group = 
"""
1 *1 R u1
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "H_rad",
    group = 
"""
1 *1 H u1
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Ct_rad",
    group = 
"""
1 *1 Ct  u1 {2,T}
2    R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Ct_rad/Ct",
    group = 
"""
1 *1 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Ct_rad/Nt",
    group = 
"""
1 *1 Ct         u1 {2,T}
2    [N3t,N5tc] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "O_rad",
    group = 
"""
1 *1 O u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "O_pri_rad-H_or_Val7-1",
    group = 
"""
1 *1 O        u1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "O_pri_rad",
    group = 
"""
1 *1 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "O_pri_rad-F",
    group = 
"""
1 *1 O   u1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "O_pri_rad-Cl",
    group = 
"""
1 *1 O    u1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "O_pri_rad-Br",
    group = 
"""
1 *1 O    u1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "O_sec_rad",
    group = 
"""
1 *1 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "O_rad/NonDeC",
    group = 
"""
1 *1 O  u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "O_rad/NonDeO",
    group = 
"""
1 *1 O u1 {2,S}
2    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "O_rad/NonDeN",
    group = 
"""
1 *1 O   u1 {2,S}
2    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "O_rad/OneDe",
    group = 
"""
1 *1 O                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "S_rad",
    group = 
"""
1 *1 S u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "S_pri_rad-H_or_Val7-1",
    group = 
"""
1 *1 S        u1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "S_pri_rad",
    group = 
"""
1 *1 S u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "S_pri_rad-F",
    group = 
"""
1 *1 S   u1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "S_pri_rad-Cl",
    group = 
"""
1 *1 S    u1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "S_pri_rad-Br",
    group = 
"""
1 *1 S    u1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "S_sec_rad",
    group = 
"""
1 *1 S   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "S_rad/NonDeC",
    group = 
"""
1 *1 S  u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "S_rad/NonDeS",
    group = 
"""
1 *1 S u1 {2,S}
2    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "S_rad/OneDe",
    group = 
"""
1 *1 S                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
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
    index = 70,
    label = "Cd_pri_rad-H_or_Val7-1",
    group = 
"""
1 *1 C        u1 {2,D} {3,S}
2    C        u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
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
    index = 72,
    label = "Cd_pri_rad-F",
    group = 
"""
1 *1 C   u1 {2,D} {3,S}
2    C   u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Cd_pri_rad-Cl",
    group = 
"""
1 *1 C    u1 {2,D} {3,S}
2    C    u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Cd_pri_rad-Br",
    group = 
"""
1 *1 C    u1 {2,D} {3,S}
2    C    u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
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
    index = 76,
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
    index = 77,
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
    index = 78,
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
    index = 79,
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
    index = 80,
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
    index = 81,
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
    index = 82,
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
    index = 83,
    label = "CO_pri_rad-H_or_Val7-1",
    group = 
"""
1 *1 C        u1 {2,D} {3,S}
2    O        u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
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
    index = 85,
    label = "CO_pri_rad-F",
    group = 
"""
1 *1 C   u1 {2,D} {3,S}
2    O   u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "CO_pri_rad-Cl",
    group = 
"""
1 *1 C    u1 {2,D} {3,S}
2    O    u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "CO_pri_rad-Br",
    group = 
"""
1 *1 C    u1 {2,D} {3,S}
2    O    u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 88,
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
    index = 89,
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
    index = 90,
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
    index = 91,
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
    index = 92,
    label = "CS_pri_rad-H_or_Val7-1",
    group = 
"""
1 *1 C        u1 {2,D} {3,S}
2    S2d      u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 93,
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
    index = 94,
    label = "CS_pri_rad-F",
    group = 
"""
1 *1 C   u1 {2,D} {3,S}
2    S2d u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "CS_pri_rad-Cl",
    group = 
"""
1 *1 C    u1 {2,D} {3,S}
2    S2d  u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "CS_pri_rad-Br",
    group = 
"""
1 *1 C    u1 {2,D} {3,S}
2    S2d  u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 97,
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
    index = 98,
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
    index = 99,
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
    index = 100,
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
    index = 101,
    label = "C_methyl-H_or_Val7-3",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 102,
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
    index = 103,
    label = "C_methyl-HHF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "C_methyl-HHCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "C_methyl-HHBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "C_methyl-HFF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "C_methyl-HFCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "C_methyl-HFBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "C_methyl-HClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "C_methyl-HClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "C_methyl-HBrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "C_methyl-FFF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "C_methyl-FFCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "C_methyl-FFBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "C_methyl-FClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "C_methyl-FClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "C_methyl-FBrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "C_methyl-ClClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "C_methyl-ClClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "C_methyl-ClBrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "C_methyl-BrBrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "C_pri_rad-H_or_Val7-2",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
4    R!H      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 123,
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
    index = 124,
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
    index = 125,
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
    index = 126,
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
    index = 127,
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
    index = 128,
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
    index = 129,
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
    index = 130,
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
    index = 131,
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
    index = 132,
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
    index = 133,
    label = "C_pri_rad-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "C_rad/H2/Cs-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "C_rad/H2/Cd-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "C_rad/H2/Ct-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "C_rad/H2/Cb-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "C_rad/H2/CO-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "C_rad/H2/O-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "C_rad/H2/CS-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "C_rad/H2/S-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "C_rad/H2/N-HF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "C_pri_rad-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "C_rad/H2/Cs-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "C_rad/H2/Cd-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cd   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "C_rad/H2/Ct-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "C_rad/H2/Cb-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "C_rad/H2/CO-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "C_rad/H2/O-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "C_rad/H2/CS-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "C_rad/H2/S-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "C_rad/H2/N-HCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "C_pri_rad-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "C_rad/H2/Cs-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "C_rad/H2/Cd-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    Cd   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "C_rad/H2/Ct-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "C_rad/H2/Cb-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "C_rad/H2/CO-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "C_rad/H2/O-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "C_rad/H2/CS-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "C_rad/H2/S-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "C_rad/H2/N-HBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "C_pri_rad-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "C_rad/H2/Cs-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "C_rad/H2/Cd-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    Cd  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "C_rad/H2/Ct-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "C_rad/H2/Cb-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "C_rad/H2/CO-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "C_rad/H2/O-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "C_rad/H2/CS-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "C_rad/H2/S-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "C_rad/H2/N-FF",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "C_pri_rad-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "C_rad/H2/Cs-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "C_rad/H2/Cd-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Cd   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "C_rad/H2/Ct-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "C_rad/H2/Cb-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "C_rad/H2/CO-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "C_rad/H2/O-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "C_rad/H2/CS-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "C_rad/H2/S-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "C_rad/H2/N-FCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "C_pri_rad-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "C_rad/H2/Cs-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "C_rad/H2/Cd-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    Cd   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "C_rad/H2/Ct-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "C_rad/H2/Cb-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "C_rad/H2/CO-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "C_rad/H2/O-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "C_rad/H2/CS-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "C_rad/H2/S-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "C_rad/H2/N-FBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "C_pri_rad-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "C_rad/H2/Cs-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "C_rad/H2/Cd-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Cd   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "C_rad/H2/Ct-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "C_rad/H2/Cb-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "C_rad/H2/CO-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "C_rad/H2/O-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "C_rad/H2/CS-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "C_rad/H2/S-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "C_rad/H2/N-ClCl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "C_pri_rad-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "C_rad/H2/Cs-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "C_rad/H2/Cd-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cd   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "C_rad/H2/Ct-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "C_rad/H2/Cb-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "C_rad/H2/CO-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "C_rad/H2/O-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "C_rad/H2/CS-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "C_rad/H2/S-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "C_rad/H2/N-ClBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "C_pri_rad-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "C_rad/H2/Cs-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "C_rad/H2/Cd-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cd   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "C_rad/H2/Ct-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "C_rad/H2/Cb-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "C_rad/H2/CO-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "C_rad/H2/O-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "C_rad/H2/CS-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "C_rad/H2/S-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "C_rad/H2/N-BrBr",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "C_sec_rad-H_or_Val7-1",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    [H,Val7] u0 {1,S}
3    R!H      u0 {1,S}
4    R!H      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 224,
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
    index = 225,
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
    index = 226,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 *1 C      u1 {2,S} {3,S} {4,S}
2    H      u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 227,
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
    index = 228,
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
    index = 229,
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
    index = 230,
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
    index = 231,
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
    index = 232,
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
    index = 233,
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
    index = 234,
    label = "C_rad/H/OneDe",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 235,
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
    index = 236,
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
    index = 237,
    label = "C_rad/H/OneDeN",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    N                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 238,
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
    index = 239,
    label = "C_sec_rad-F",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "C_rad/H/NonDeC-F",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "C_rad/H/NonDeO-F",
    group = 
"""
1 *1 C      u1 {2,S} {3,S} {4,S}
2    F1s    u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "C_rad/H/CsO-F",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Cs  u0 {1,S}
4    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "C_rad/H/O2-F",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    O   u0 {1,S}
4    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "C_rad/H/NonDeN-F",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    F1s      u0 {1,S}
3    N        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "C_rad/H/NonDeS-F",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    F1s      u0 {1,S}
3    S        u0 {1,S}
4    [Cs,S,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "C_rad/H/CsS-F",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    S   u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "C_rad/H/S2-F",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    S   u0 {1,S}
4    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "C_rad/H/SO-F",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    S   u0 {1,S}
4    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "C_rad/H/OneDe-F",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "C_rad/H/OneDeC-F",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "C_rad/H/OneDeO-F",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "C_rad/H/OneDeN-F",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    N                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "C_rad/H/TwoDe-F",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "C_sec_rad-Cl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    R!H  u0 {1,S}
4    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "C_rad/H/NonDeC-Cl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "C_rad/H/NonDeO-Cl",
    group = 
"""
1 *1 C      u1 {2,S} {3,S} {4,S}
2    Cl1s   u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "C_rad/H/CsO-Cl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cs   u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "C_rad/H/O2-Cl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    O    u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 259,
    label = "C_rad/H/NonDeN-Cl",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    Cl1s     u0 {1,S}
3    N        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "C_rad/H/NonDeS-Cl",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    Cl1s     u0 {1,S}
3    S        u0 {1,S}
4    [Cs,S,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "C_rad/H/CsS-Cl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    S    u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "C_rad/H/S2-Cl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    S    u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "C_rad/H/SO-Cl",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    S    u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "C_rad/H/OneDe-Cl",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "C_rad/H/OneDeC-Cl",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "C_rad/H/OneDeO-Cl",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "C_rad/H/OneDeN-Cl",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    N                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "C_rad/H/TwoDe-Cl",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "C_sec_rad-Br",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    R!H  u0 {1,S}
4    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "C_rad/H/NonDeC-Br",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "C_rad/H/NonDeO-Br",
    group = 
"""
1 *1 C      u1 {2,S} {3,S} {4,S}
2    Br1s   u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "C_rad/H/CsO-Br",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Cs   u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "C_rad/H/O2-Br",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    O    u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "C_rad/H/NonDeN-Br",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    Br1s     u0 {1,S}
3    N        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "C_rad/H/NonDeS-Br",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    Br1s     u0 {1,S}
3    S        u0 {1,S}
4    [Cs,S,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "C_rad/H/CsS-Br",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    S    u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "C_rad/H/S2-Br",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    S    u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 278,
    label = "C_rad/H/SO-Br",
    group = 
"""
1 *1 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    S    u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "C_rad/H/OneDe-Br",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "C_rad/H/OneDeC-Br",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "C_rad/H/OneDeO-Br",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "C_rad/H/OneDeN-Br",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    N                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "C_rad/H/TwoDe-Br",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 284,
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
    index = 285,
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
    index = 286,
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
    index = 287,
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
    index = 288,
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
    index = 289,
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
    index = 290,
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
    index = 291,
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
    index = 292,
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
    index = 293,
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
    index = 294,
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
    index = 295,
    label = "N3_rad",
    group = 
"""
1 *1 [N3s,N3d] u1
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "N3s_rad",
    group = 
"""
1 *1 N3s u1
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "N/H_or_Val7/2_rad",
    group = 
"""
1 *1 N3s      u1 {2,S} {3,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 298,
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
    index = 299,
    label = "NH2_rad-HF",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "NH2_rad-HCl",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "NH2_rad-HBr",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "NH2_rad-FF",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "NH2_rad-FCl",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "NH2_rad-FBr",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "NH2_rad-ClCl",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "NH2_rad-ClBr",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "NH2_rad-BrBr",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "N3s_rad_pri-H_or_Val7-1",
    group = 
"""
1 *1 N3s      u1 {2,S} {3,S}
2    R!H      u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 309,
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
    index = 310,
    label = "N3s_rad/H/NonDe",
    group = 
"""
1 *1 N3s          u1 {2,S} {3,S}
2    [Cs,N3s,O2s] u0 {1,S}
3    H            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 311,
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
    index = 312,
    label = "N3s_rad/H/NonDeO",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2    O2s u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 313,
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
    index = 314,
    label = "N3s_rad/H/OneDe",
    group = 
"""
1 *1 N3s                          u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
3    H                            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "N3s_rad_pri-F",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2    R!H u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "N3s_rad/H/NonDe-F",
    group = 
"""
1 *1 N3s          u1 {2,S} {3,S}
2    [Cs,N3s,O2s] u0 {1,S}
3    F1s          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "N3s_rad/H/NonDeC-F",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2    Cs  u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "N3s_rad/H/NonDeO-F",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2    O2s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "N3s_rad/H/NonDeN-F",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2    N3s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "N3s_rad/H/OneDe-F",
    group = 
"""
1 *1 N3s                          u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
3    F1s                          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "N3s_rad_pri-Cl",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    R!H  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "N3s_rad/H/NonDe-Cl",
    group = 
"""
1 *1 N3s          u1 {2,S} {3,S}
2    [Cs,N3s,O2s] u0 {1,S}
3    Cl1s         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "N3s_rad/H/NonDeC-Cl",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    Cs   u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "N3s_rad/H/NonDeO-Cl",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    O2s  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "N3s_rad/H/NonDeN-Cl",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    N3s  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "N3s_rad/H/OneDe-Cl",
    group = 
"""
1 *1 N3s                          u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
3    Cl1s                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "N3s_rad_pri-Br",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    R!H  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "N3s_rad/H/NonDe-Br",
    group = 
"""
1 *1 N3s          u1 {2,S} {3,S}
2    [Cs,N3s,O2s] u0 {1,S}
3    Br1s         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "N3s_rad/H/NonDeC-Br",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    Cs   u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "N3s_rad/H/NonDeO-Br",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    O2s  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "N3s_rad/H/NonDeN-Br",
    group = 
"""
1 *1 N3s  u1 {2,S} {3,S}
2    N3s  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "N3s_rad/H/OneDe-Br",
    group = 
"""
1 *1 N3s                          u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
3    Br1s                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 333,
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
    index = 334,
    label = "N3s_rad/NonDe2",
    group = 
"""
1 *1 N3s          u1 {2,S} {3,S}
2    [Cs,N3s,O2s] u0 {1,S}
3    [Cs,N3s,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "N3s_rad/OneDe",
    group = 
"""
1 *1 N3s                          u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
3    [Cs,N3s,O2s]                 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "N3s_rad/TwoDe",
    group = 
"""
1 *1 N3s                          u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "N3d_rad",
    group = 
"""
1 *1 N3d u1
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "N3d_rad/C",
    group = 
"""
1 *1 N3d u1 {2,D}
2    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "N3d_rad/O",
    group = 
"""
1 *1 N3d u1 {2,D}
2    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "N3d_rad/N",
    group = 
"""
1 *1 N3d u1 {2,D}
2    N   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "N3d_rad/S",
    group = 
"""
1 *1 N3d u1 {2,D}
2    S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "N5_rad",
    group = 
"""
1 *1 [N5sc,N5dc,N5tc,N5b] u1
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "N5s_rad",
    group = 
"""
1 *1 N5sc u1 p0
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "N5dc_rad",
    group = 
"""
1 *1 N5dc                                                       u1 p0 c+1 {2,D} {3,S}
2    R!H                                                        u0 c0 {1,D}
3    [C2sc,N1sc,O0sc,S0sc,S2sc,S2dc,S4dc,S4tdc,S6sc,S6dc,S6tdc] u0 c-1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "N5t_rad",
    group = 
"""
1 *1 N5tc u1 p0 {2,T}
2    R!H  ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 346,
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
    index = 347,
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
    L2: Y_2centerbirad
        L3: O2b
        L3: C2b
        L3: S2b
    L2: Y_1centerbirad
        L3: CO_birad_triplet
        L3: O_atom_triplet
        L3: CS_birad_triplet
        L3: S_atom_triplet
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
        L3: N/H_or_Val7/triplet
            L4: NH_triplet
            L4: NH_triplet-F
            L4: NH_triplet-Cl
            L4: NH_triplet-Br
    L2: Y_rad
        L3: H_rad
        L3: Ct_rad
            L4: Ct_rad/Ct
            L4: Ct_rad/Nt
        L3: O_rad
            L4: O_pri_rad-H_or_Val7-1
                L5: O_pri_rad
                L5: O_pri_rad-F
                L5: O_pri_rad-Cl
                L5: O_pri_rad-Br
            L4: O_sec_rad
                L5: O_rad/NonDeC
                L5: O_rad/NonDeO
                L5: O_rad/NonDeN
                L5: O_rad/OneDe
        L3: S_rad
            L4: S_pri_rad-H_or_Val7-1
                L5: S_pri_rad
                L5: S_pri_rad-F
                L5: S_pri_rad-Cl
                L5: S_pri_rad-Br
            L4: S_sec_rad
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/OneDe
        L3: Cd_rad
            L4: Cd_pri_rad-H_or_Val7-1
                L5: Cd_pri_rad
                L5: Cd_pri_rad-F
                L5: Cd_pri_rad-Cl
                L5: Cd_pri_rad-Br
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                L5: Cd_rad/NonDeN
                L5: Cd_rad/NonDeO
                L5: Cd_rad/NonDeS
                L5: Cd_rad/OneDe
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad-H_or_Val7-1
                L5: CO_pri_rad
                L5: CO_pri_rad-F
                L5: CO_pri_rad-Cl
                L5: CO_pri_rad-Br
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: CS_rad
            L4: CS_pri_rad-H_or_Val7-1
                L5: CS_pri_rad
                L5: CS_pri_rad-F
                L5: CS_pri_rad-Cl
                L5: CS_pri_rad-Br
            L4: CS_sec_rad
                L5: CS_rad/NonDe
                L5: CS_rad/OneDe
        L3: Cs_rad
            L4: C_methyl-H_or_Val7-3
                L5: C_methyl
                L5: C_methyl-HHF
                L5: C_methyl-HHCl
                L5: C_methyl-HHBr
                L5: C_methyl-HFF
                L5: C_methyl-HFCl
                L5: C_methyl-HFBr
                L5: C_methyl-HClCl
                L5: C_methyl-HClBr
                L5: C_methyl-HBrBr
                L5: C_methyl-FFF
                L5: C_methyl-FFCl
                L5: C_methyl-FFBr
                L5: C_methyl-FClCl
                L5: C_methyl-FClBr
                L5: C_methyl-FBrBr
                L5: C_methyl-ClClCl
                L5: C_methyl-ClClBr
                L5: C_methyl-ClBrBr
                L5: C_methyl-BrBrBr
            L4: C_pri_rad-H_or_Val7-2
                L5: C_pri_rad
                    L6: C_rad/H2/Cs
                    L6: C_rad/H2/Cd
                    L6: C_rad/H2/Ct
                    L6: C_rad/H2/Cb
                    L6: C_rad/H2/CO
                    L6: C_rad/H2/O
                    L6: C_rad/H2/CS
                    L6: C_rad/H2/S
                    L6: C_rad/H2/N
                L5: C_pri_rad-HF
                    L6: C_rad/H2/Cs-HF
                    L6: C_rad/H2/Cd-HF
                    L6: C_rad/H2/Ct-HF
                    L6: C_rad/H2/Cb-HF
                    L6: C_rad/H2/CO-HF
                    L6: C_rad/H2/O-HF
                    L6: C_rad/H2/CS-HF
                    L6: C_rad/H2/S-HF
                    L6: C_rad/H2/N-HF
                L5: C_pri_rad-HCl
                    L6: C_rad/H2/Cs-HCl
                    L6: C_rad/H2/Cd-HCl
                    L6: C_rad/H2/Ct-HCl
                    L6: C_rad/H2/Cb-HCl
                    L6: C_rad/H2/CO-HCl
                    L6: C_rad/H2/O-HCl
                    L6: C_rad/H2/CS-HCl
                    L6: C_rad/H2/S-HCl
                    L6: C_rad/H2/N-HCl
                L5: C_pri_rad-HBr
                    L6: C_rad/H2/Cs-HBr
                    L6: C_rad/H2/Cd-HBr
                    L6: C_rad/H2/Ct-HBr
                    L6: C_rad/H2/Cb-HBr
                    L6: C_rad/H2/CO-HBr
                    L6: C_rad/H2/O-HBr
                    L6: C_rad/H2/CS-HBr
                    L6: C_rad/H2/S-HBr
                    L6: C_rad/H2/N-HBr
                L5: C_pri_rad-FF
                    L6: C_rad/H2/Cs-FF
                    L6: C_rad/H2/Cd-FF
                    L6: C_rad/H2/Ct-FF
                    L6: C_rad/H2/Cb-FF
                    L6: C_rad/H2/CO-FF
                    L6: C_rad/H2/O-FF
                    L6: C_rad/H2/CS-FF
                    L6: C_rad/H2/S-FF
                    L6: C_rad/H2/N-FF
                L5: C_pri_rad-FCl
                    L6: C_rad/H2/Cs-FCl
                    L6: C_rad/H2/Cd-FCl
                    L6: C_rad/H2/Ct-FCl
                    L6: C_rad/H2/Cb-FCl
                    L6: C_rad/H2/CO-FCl
                    L6: C_rad/H2/O-FCl
                    L6: C_rad/H2/CS-FCl
                    L6: C_rad/H2/S-FCl
                    L6: C_rad/H2/N-FCl
                L5: C_pri_rad-FBr
                    L6: C_rad/H2/Cs-FBr
                    L6: C_rad/H2/Cd-FBr
                    L6: C_rad/H2/Ct-FBr
                    L6: C_rad/H2/Cb-FBr
                    L6: C_rad/H2/CO-FBr
                    L6: C_rad/H2/O-FBr
                    L6: C_rad/H2/CS-FBr
                    L6: C_rad/H2/S-FBr
                    L6: C_rad/H2/N-FBr
                L5: C_pri_rad-ClCl
                    L6: C_rad/H2/Cs-ClCl
                    L6: C_rad/H2/Cd-ClCl
                    L6: C_rad/H2/Ct-ClCl
                    L6: C_rad/H2/Cb-ClCl
                    L6: C_rad/H2/CO-ClCl
                    L6: C_rad/H2/O-ClCl
                    L6: C_rad/H2/CS-ClCl
                    L6: C_rad/H2/S-ClCl
                    L6: C_rad/H2/N-ClCl
                L5: C_pri_rad-ClBr
                    L6: C_rad/H2/Cs-ClBr
                    L6: C_rad/H2/Cd-ClBr
                    L6: C_rad/H2/Ct-ClBr
                    L6: C_rad/H2/Cb-ClBr
                    L6: C_rad/H2/CO-ClBr
                    L6: C_rad/H2/O-ClBr
                    L6: C_rad/H2/CS-ClBr
                    L6: C_rad/H2/S-ClBr
                    L6: C_rad/H2/N-ClBr
                L5: C_pri_rad-BrBr
                    L6: C_rad/H2/Cs-BrBr
                    L6: C_rad/H2/Cd-BrBr
                    L6: C_rad/H2/Ct-BrBr
                    L6: C_rad/H2/Cb-BrBr
                    L6: C_rad/H2/CO-BrBr
                    L6: C_rad/H2/O-BrBr
                    L6: C_rad/H2/CS-BrBr
                    L6: C_rad/H2/S-BrBr
                    L6: C_rad/H2/N-BrBr
            L4: C_sec_rad-H_or_Val7-1
                L5: C_sec_rad
                    L6: C_rad/H/NonDeC
                    L6: C_rad/H/NonDeO
                        L7: C_rad/H/CsO
                        L7: C_rad/H/O2
                    L6: C_rad/H/NonDeN
                    L6: C_rad/H/NonDeS
                        L7: C_rad/H/CsS
                        L7: C_rad/H/S2
                        L7: C_rad/H/SO
                    L6: C_rad/H/OneDe
                        L7: C_rad/H/OneDeC
                        L7: C_rad/H/OneDeO
                        L7: C_rad/H/OneDeN
                    L6: C_rad/H/TwoDe
                L5: C_sec_rad-F
                    L6: C_rad/H/NonDeC-F
                    L6: C_rad/H/NonDeO-F
                        L7: C_rad/H/CsO-F
                        L7: C_rad/H/O2-F
                    L6: C_rad/H/NonDeN-F
                    L6: C_rad/H/NonDeS-F
                        L7: C_rad/H/CsS-F
                        L7: C_rad/H/S2-F
                        L7: C_rad/H/SO-F
                    L6: C_rad/H/OneDe-F
                        L7: C_rad/H/OneDeC-F
                        L7: C_rad/H/OneDeO-F
                        L7: C_rad/H/OneDeN-F
                    L6: C_rad/H/TwoDe-F
                L5: C_sec_rad-Cl
                    L6: C_rad/H/NonDeC-Cl
                    L6: C_rad/H/NonDeO-Cl
                        L7: C_rad/H/CsO-Cl
                        L7: C_rad/H/O2-Cl
                    L6: C_rad/H/NonDeN-Cl
                    L6: C_rad/H/NonDeS-Cl
                        L7: C_rad/H/CsS-Cl
                        L7: C_rad/H/S2-Cl
                        L7: C_rad/H/SO-Cl
                    L6: C_rad/H/OneDe-Cl
                        L7: C_rad/H/OneDeC-Cl
                        L7: C_rad/H/OneDeO-Cl
                        L7: C_rad/H/OneDeN-Cl
                    L6: C_rad/H/TwoDe-Cl
                L5: C_sec_rad-Br
                    L6: C_rad/H/NonDeC-Br
                    L6: C_rad/H/NonDeO-Br
                        L7: C_rad/H/CsO-Br
                        L7: C_rad/H/O2-Br
                    L6: C_rad/H/NonDeN-Br
                    L6: C_rad/H/NonDeS-Br
                        L7: C_rad/H/CsS-Br
                        L7: C_rad/H/S2-Br
                        L7: C_rad/H/SO-Br
                    L6: C_rad/H/OneDe-Br
                        L7: C_rad/H/OneDeC-Br
                        L7: C_rad/H/OneDeO-Br
                        L7: C_rad/H/OneDeN-Br
                    L6: C_rad/H/TwoDe-Br
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
                L5: N/H_or_Val7/2_rad
                    L6: NH2_rad
                    L6: NH2_rad-HF
                    L6: NH2_rad-HCl
                    L6: NH2_rad-HBr
                    L6: NH2_rad-FF
                    L6: NH2_rad-FCl
                    L6: NH2_rad-FBr
                    L6: NH2_rad-ClCl
                    L6: NH2_rad-ClBr
                    L6: NH2_rad-BrBr
                L5: N3s_rad_pri-H_or_Val7-1
                    L6: N3s_rad_pri
                        L7: N3s_rad/H/NonDe
                            L8: N3s_rad/H/NonDeC
                            L8: N3s_rad/H/NonDeO
                            L8: N3s_rad/H/NonDeN
                        L7: N3s_rad/H/OneDe
                    L6: N3s_rad_pri-F
                        L7: N3s_rad/H/NonDe-F
                            L8: N3s_rad/H/NonDeC-F
                            L8: N3s_rad/H/NonDeO-F
                            L8: N3s_rad/H/NonDeN-F
                        L7: N3s_rad/H/OneDe-F
                    L6: N3s_rad_pri-Cl
                        L7: N3s_rad/H/NonDe-Cl
                            L8: N3s_rad/H/NonDeC-Cl
                            L8: N3s_rad/H/NonDeO-Cl
                            L8: N3s_rad/H/NonDeN-Cl
                        L7: N3s_rad/H/OneDe-Cl
                    L6: N3s_rad_pri-Br
                        L7: N3s_rad/H/NonDe-Br
                            L8: N3s_rad/H/NonDeC-Br
                            L8: N3s_rad/H/NonDeO-Br
                            L8: N3s_rad/H/NonDeN-Br
                        L7: N3s_rad/H/OneDe-Br
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
    shortDesc = """""",
    longDesc = 
"""

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
    shortDesc = """""",
    longDesc = 
"""

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
    shortDesc = """""",
    longDesc = 
"""

""",
)

forbidden(
    label = "XH_N_birad_singlet",
    group = 
"""
1 *3 N   u0 p2 {2,[S,D]}
2 *2 R!H ux {1,[S,D]} {3,S}
3 *4 H   u0 {2,S}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

forbidden(
    label = "XH_birad_singlet",
    group = 
"""
1 *3 [C,Si] u0 p1 {2,[S,D,T]}
2 *2 R!H    ux {1,[S,D,T]} {3,S}
3 *4 H      u0 {2,S}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

forbidden(
    label = "XH_quadrad_singlet",
    group = 
"""
1 *3 [C,Si] u0 p2 {2,[S,D,T]}
2 *2 R!H    ux {1,[S,D,T]} {3,S}
3 *4 H      u0 {2,S}
""",
    shortDesc = """""",
    longDesc = 
"""

""",
)

