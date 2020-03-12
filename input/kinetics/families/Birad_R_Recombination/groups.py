#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/groups"
shortDesc = ""
longDesc = """
This reaction family is reserved for recombination of O_atom, S_atom, N_R_birad (triplets only).
The forbidden groups at the bottom prevent it from reacting with other forms of O, S, NH.
"""

template(reactants=["Y_rad", "Birad"], products=["YOS."], ownReverse=False)

reverse = "ROS_Bond_Dissociation"
reversible = True

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
    label = "Val7_or_H/rad",
    group = 
"""
1 *1 [H,Val7] u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "H_rad",
    group = 
"""
1 *1 H u1
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Val7_rad",
    group = 
"""
1 *1 Val7 u1 p3
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "F_rad",
    group = 
"""
1 *1 F u1 p3
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Cl_rad",
    group = 
"""
1 *1 Cl u1 p3
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Br_rad",
    group = 
"""
1 *1 Br u1 p3
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Ct_rad",
    group = 
"""
1 *1 C u1 {2,T}
2    C u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "O_rad",
    group = 
"""
1 *1 O u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "O_pri_rad-H_or_Val7-1",
    group = 
"""
1 *1 O        u1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "O_pri_rad",
    group = 
"""
1 *1 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "O_pri_rad-F",
    group = 
"""
1 *1 O   u1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "O_pri_rad-Cl",
    group = 
"""
1 *1 O    u1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "O_pri_rad-Br",
    group = 
"""
1 *1 O    u1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "O_sec_rad",
    group = 
"""
1 *1 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "O_rad/NonDe",
    group = 
"""
1 *1 O        u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "O_rad/OneDe",
    group = 
"""
1 *1 O                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "S_rad",
    group = 
"""
1 *1 S u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "S_pri_rad-H_or_Val7-1",
    group = 
"""
1 *1 S        u1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "S_pri_rad",
    group = 
"""
1 *1 S u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "S_pri_rad-F",
    group = 
"""
1 *1 S   u1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "S_pri_rad-Cl",
    group = 
"""
1 *1 S    u1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "S_pri_rad-Br",
    group = 
"""
1 *1 S    u1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "S_sec_rad",
    group = 
"""
1 *1 S   u1 {2,S}
2    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "S_rad/NonDe",
    group = 
"""
1 *1 S        u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "S_rad/OneDe",
    group = 
"""
1 *1 S                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
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
    index = 28,
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
    index = 29,
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
    index = 30,
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
    index = 31,
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
    index = 32,
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
    index = 33,
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
    index = 34,
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
    index = 35,
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
    index = 36,
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
    index = 37,
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
    index = 38,
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
    index = 39,
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
    index = 40,
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
    index = 41,
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
    index = 42,
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
    index = 43,
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
    index = 44,
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
    index = 45,
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
    index = 46,
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
    index = 47,
    label = "CS_pri_rad-H_or_Val7-1",
    group = 
"""
1 *1 C        u1 {2,D} {3,S}
2    S        u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
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
    index = 49,
    label = "CS_pri_rad-F",
    group = 
"""
1 *1 C   u1 {2,D} {3,S}
2    S   u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "CS_pri_rad-Cl",
    group = 
"""
1 *1 C    u1 {2,D} {3,S}
2    S    u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "CS_pri_rad-Br",
    group = 
"""
1 *1 C    u1 {2,D} {3,S}
2    S    u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
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
    index = 53,
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
    index = 54,
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
    index = 55,
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
    index = 56,
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
    index = 57,
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
    index = 58,
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
    index = 59,
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
    index = 60,
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
    index = 61,
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
    index = 62,
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
    index = 63,
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
    index = 64,
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
    index = 65,
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
    index = 66,
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
    index = 67,
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
    index = 68,
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
    index = 69,
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
    index = 70,
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
    index = 71,
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
    index = 72,
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
    index = 73,
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
    index = 74,
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
    index = 75,
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
    index = 76,
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
    index = 77,
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
    index = 78,
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
    index = 79,
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
    index = 80,
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
    index = 81,
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
    index = 82,
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
    index = 83,
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
    index = 84,
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
    index = 85,
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
    index = 86,
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
    index = 87,
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
    index = 88,
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
    index = 89,
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
    index = 90,
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
    index = 91,
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
    index = 92,
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
    index = 93,
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
    index = 94,
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
    index = 95,
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
    index = 96,
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
    index = 97,
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
    index = 98,
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
    index = 99,
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
    index = 100,
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
    index = 101,
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
    index = 102,
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
    index = 103,
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
    index = 104,
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
    index = 105,
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
    index = 106,
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
    index = 107,
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
    index = 108,
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
    index = 109,
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
    index = 110,
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
    index = 111,
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
    index = 112,
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
    index = 113,
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
    index = 114,
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
    index = 115,
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
    index = 116,
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
    index = 117,
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
    index = 118,
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
    index = 119,
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
    index = 120,
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
    index = 121,
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
    index = 122,
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
    index = 123,
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
    index = 124,
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
    index = 125,
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
    index = 126,
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
    index = 127,
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
    index = 128,
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
    index = 129,
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
    index = 130,
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
    index = 131,
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
    index = 132,
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
    index = 133,
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
    index = 134,
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
    index = 135,
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
    index = 136,
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
    index = 137,
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
    index = 138,
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
    index = 139,
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
    index = 140,
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
    index = 141,
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
    index = 142,
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
    index = 143,
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
    index = 144,
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
    index = 145,
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
    index = 146,
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
    index = 147,
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
    index = 148,
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
    index = 149,
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
    index = 150,
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
    index = 151,
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
    index = 152,
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
    index = 153,
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
    index = 154,
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
    index = 155,
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
    index = 156,
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
    index = 157,
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
    index = 158,
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
    index = 159,
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
    index = 160,
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
    index = 161,
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
    index = 162,
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
    index = 163,
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
    index = 164,
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
    index = 165,
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
    index = 166,
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
    index = 167,
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
    index = 168,
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
    index = 169,
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
    index = 170,
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
    index = 171,
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
    index = 172,
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
    index = 173,
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
    index = 174,
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
    index = 175,
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
    index = 176,
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
    index = 177,
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
    index = 178,
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
    index = 179,
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
    index = 180,
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
    index = 181,
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
    index = 182,
    label = "C_rad/H/NonDeO-F",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    F1s      u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 183,
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
    index = 184,
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
    index = 185,
    label = "C_rad/H/NonDeS-F",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    F1s      u0 {1,S}
3    S        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "C_rad/H/OneDe-F",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 187,
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
    index = 188,
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
    index = 189,
    label = "C_rad/H/OneDeS-F",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 190,
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
    index = 191,
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
    index = 192,
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
    index = 193,
    label = "C_rad/H/NonDeO-Cl",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    Cl1s     u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 194,
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
    index = 195,
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
    index = 196,
    label = "C_rad/H/NonDeS-Cl",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    Cl1s     u0 {1,S}
3    S        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "C_rad/H/OneDe-Cl",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 198,
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
    index = 199,
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
    index = 200,
    label = "C_rad/H/OneDeS-Cl",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 201,
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
    index = 202,
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
    index = 203,
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
    index = 204,
    label = "C_rad/H/NonDeO-Br",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    Br1s     u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 205,
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
    index = 206,
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
    index = 207,
    label = "C_rad/H/NonDeS-Br",
    group = 
"""
1 *1 C        u1 {2,S} {3,S} {4,S}
2    Br1s     u0 {1,S}
3    S        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "C_rad/H/OneDe-Br",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 209,
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
    index = 210,
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
    index = 211,
    label = "C_rad/H/OneDeS-Br",
    group = 
"""
1 *1 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 212,
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
    index = 213,
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
    index = 214,
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
    index = 215,
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
    index = 216,
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
    index = 217,
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
    index = 218,
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
    index = 219,
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
    index = 220,
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
    index = 221,
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
    index = 222,
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
    index = 223,
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
    index = 224,
    label = "O_birad",
    group = 
"""
1 *2 O u2 p2
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "S_birad",
    group = 
"""
1 *2 S u2 p2
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "N_R_birad",
    group = 
"""
1 *2 N u2 p1
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "N_birad/H_or_Val7/",
    group = 
"""
1 *2 N        u2 p1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "N_birad/H",
    group = 
"""
1 *2 N u2 p1 {2,S}
2    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "N_birad/H-F",
    group = 
"""
1 *2 N   u2 p1 {2,S}
2    F1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "N_birad/H-Cl",
    group = 
"""
1 *2 N    u2 p1 {2,S}
2    Cl1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 231,
    label = "N_birad/H-Br",
    group = 
"""
1 *2 N    u2 p1 {2,S}
2    Br1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "N_birad/C",
    group = 
"""
1 *2 N u2 p1 {2,S}
2    C ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "N_birad/O",
    group = 
"""
1 *2 N u2 p1 {2,S}
2    O ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "N_birad/N",
    group = 
"""
1 *2 N u2 p1 {2,S}
2    N ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 235,
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
    L2: Val7_or_H/rad
        L3: H_rad
        L3: Val7_rad
            L4: F_rad
            L4: Cl_rad
            L4: Br_rad
    L2: Ct_rad
    L2: O_rad
        L3: O_pri_rad-H_or_Val7-1
            L4: O_pri_rad
            L4: O_pri_rad-F
            L4: O_pri_rad-Cl
            L4: O_pri_rad-Br
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
    L2: S_rad
        L3: S_pri_rad-H_or_Val7-1
            L4: S_pri_rad
            L4: S_pri_rad-F
            L4: S_pri_rad-Cl
            L4: S_pri_rad-Br
        L3: S_sec_rad
            L4: S_rad/NonDe
            L4: S_rad/OneDe
    L2: Cd_rad
        L3: Cd_pri_rad-H_or_Val7-1
            L4: Cd_pri_rad
            L4: Cd_pri_rad-F
            L4: Cd_pri_rad-Cl
            L4: Cd_pri_rad-Br
        L3: Cd_sec_rad
            L4: Cd_rad/NonDe
            L4: Cd_rad/OneDe
    L2: Cb_rad
    L2: CO_rad
        L3: CO_pri_rad-H_or_Val7-1
            L4: CO_pri_rad
            L4: CO_pri_rad-F
            L4: CO_pri_rad-Cl
            L4: CO_pri_rad-Br
        L3: CO_sec_rad
            L4: CO_rad/NonDe
            L4: CO_rad/OneDe
    L2: CS_rad
        L3: CS_pri_rad-H_or_Val7-1
            L4: CS_pri_rad
            L4: CS_pri_rad-F
            L4: CS_pri_rad-Cl
            L4: CS_pri_rad-Br
        L3: CS_sec_rad
            L4: CS_rad/NonDe
            L4: CS_rad/OneDe
    L2: Cs_rad
        L3: C_methyl-H_or_Val7-3
            L4: C_methyl
            L4: C_methyl-HHF
            L4: C_methyl-HHCl
            L4: C_methyl-HHBr
            L4: C_methyl-HFF
            L4: C_methyl-HFCl
            L4: C_methyl-HFBr
            L4: C_methyl-HClCl
            L4: C_methyl-HClBr
            L4: C_methyl-HBrBr
            L4: C_methyl-FFF
            L4: C_methyl-FFCl
            L4: C_methyl-FFBr
            L4: C_methyl-FClCl
            L4: C_methyl-FClBr
            L4: C_methyl-FBrBr
            L4: C_methyl-ClClCl
            L4: C_methyl-ClClBr
            L4: C_methyl-ClBrBr
            L4: C_methyl-BrBrBr
        L3: C_pri_rad-H_or_Val7-2
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                L5: C_rad/H2/Cd
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/CS
                L5: C_rad/H2/O
                L5: C_rad/H2/S
            L4: C_pri_rad-HF
                L5: C_rad/H2/Cs-HF
                L5: C_rad/H2/Cd-HF
                L5: C_rad/H2/Ct-HF
                L5: C_rad/H2/Cb-HF
                L5: C_rad/H2/CO-HF
                L5: C_rad/H2/CS-HF
                L5: C_rad/H2/O-HF
                L5: C_rad/H2/S-HF
            L4: C_pri_rad-HCl
                L5: C_rad/H2/Cs-HCl
                L5: C_rad/H2/Cd-HCl
                L5: C_rad/H2/Ct-HCl
                L5: C_rad/H2/Cb-HCl
                L5: C_rad/H2/CO-HCl
                L5: C_rad/H2/CS-HCl
                L5: C_rad/H2/O-HCl
                L5: C_rad/H2/S-HCl
            L4: C_pri_rad-HBr
                L5: C_rad/H2/Cs-HBr
                L5: C_rad/H2/Cd-HBr
                L5: C_rad/H2/Ct-HBr
                L5: C_rad/H2/Cb-HBr
                L5: C_rad/H2/CO-HBr
                L5: C_rad/H2/CS-HBr
                L5: C_rad/H2/O-HBr
                L5: C_rad/H2/S-HBr
            L4: C_pri_rad-FF
                L5: C_rad/H2/Cs-FF
                L5: C_rad/H2/Cd-FF
                L5: C_rad/H2/Ct-FF
                L5: C_rad/H2/Cb-FF
                L5: C_rad/H2/CO-FF
                L5: C_rad/H2/CS-FF
                L5: C_rad/H2/O-FF
                L5: C_rad/H2/S-FF
            L4: C_pri_rad-FCl
                L5: C_rad/H2/Cs-FCl
                L5: C_rad/H2/Cd-FCl
                L5: C_rad/H2/Ct-FCl
                L5: C_rad/H2/Cb-FCl
                L5: C_rad/H2/CO-FCl
                L5: C_rad/H2/CS-FCl
                L5: C_rad/H2/O-FCl
                L5: C_rad/H2/S-FCl
            L4: C_pri_rad-FBr
                L5: C_rad/H2/Cs-FBr
                L5: C_rad/H2/Cd-FBr
                L5: C_rad/H2/Ct-FBr
                L5: C_rad/H2/Cb-FBr
                L5: C_rad/H2/CO-FBr
                L5: C_rad/H2/CS-FBr
                L5: C_rad/H2/O-FBr
                L5: C_rad/H2/S-FBr
            L4: C_pri_rad-ClCl
                L5: C_rad/H2/Cs-ClCl
                L5: C_rad/H2/Cd-ClCl
                L5: C_rad/H2/Ct-ClCl
                L5: C_rad/H2/Cb-ClCl
                L5: C_rad/H2/CO-ClCl
                L5: C_rad/H2/CS-ClCl
                L5: C_rad/H2/O-ClCl
                L5: C_rad/H2/S-ClCl
            L4: C_pri_rad-ClBr
                L5: C_rad/H2/Cs-ClBr
                L5: C_rad/H2/Cd-ClBr
                L5: C_rad/H2/Ct-ClBr
                L5: C_rad/H2/Cb-ClBr
                L5: C_rad/H2/CO-ClBr
                L5: C_rad/H2/CS-ClBr
                L5: C_rad/H2/O-ClBr
                L5: C_rad/H2/S-ClBr
            L4: C_pri_rad-BrBr
                L5: C_rad/H2/Cs-BrBr
                L5: C_rad/H2/Cd-BrBr
                L5: C_rad/H2/Ct-BrBr
                L5: C_rad/H2/Cb-BrBr
                L5: C_rad/H2/CO-BrBr
                L5: C_rad/H2/CS-BrBr
                L5: C_rad/H2/O-BrBr
                L5: C_rad/H2/S-BrBr
        L3: C_sec_rad-H_or_Val7-1
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                    L6: C_rad/H/O2
                L5: C_rad/H/NonDeS
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                    L6: C_rad/H/OneDeO
                    L6: C_rad/H/OneDeS
                L5: C_rad/H/TwoDe
            L4: C_sec_rad-F
                L5: C_rad/H/NonDeC-F
                L5: C_rad/H/NonDeO-F
                    L6: C_rad/H/CsO-F
                    L6: C_rad/H/O2-F
                L5: C_rad/H/NonDeS-F
                L5: C_rad/H/OneDe-F
                    L6: C_rad/H/OneDeC-F
                    L6: C_rad/H/OneDeO-F
                    L6: C_rad/H/OneDeS-F
                L5: C_rad/H/TwoDe-F
            L4: C_sec_rad-Cl
                L5: C_rad/H/NonDeC-Cl
                L5: C_rad/H/NonDeO-Cl
                    L6: C_rad/H/CsO-Cl
                    L6: C_rad/H/O2-Cl
                L5: C_rad/H/NonDeS-Cl
                L5: C_rad/H/OneDe-Cl
                    L6: C_rad/H/OneDeC-Cl
                    L6: C_rad/H/OneDeO-Cl
                    L6: C_rad/H/OneDeS-Cl
                L5: C_rad/H/TwoDe-Cl
            L4: C_sec_rad-Br
                L5: C_rad/H/NonDeC-Br
                L5: C_rad/H/NonDeO-Br
                    L6: C_rad/H/CsO-Br
                    L6: C_rad/H/O2-Br
                L5: C_rad/H/NonDeS-Br
                L5: C_rad/H/OneDe-Br
                    L6: C_rad/H/OneDeC-Br
                    L6: C_rad/H/OneDeO-Br
                    L6: C_rad/H/OneDeS-Br
                L5: C_rad/H/TwoDe-Br
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
        L3: N_birad/H_or_Val7/
            L4: N_birad/H
            L4: N_birad/H-F
            L4: N_birad/H-Cl
            L4: N_birad/H-Br
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
    shortDesc = """""",
    longDesc = 
"""
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
    shortDesc = """""",
    longDesc = 
"""
Group added to forbid this family from forming S-O chains
""",
)

forbidden(
    label = "S2_p0",
    group = 
"""
1 *2 S u2 p0
""",
    shortDesc = """""",
    longDesc = 
"""
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
    shortDesc = """""",
    longDesc = 
"""
This family is intended to handle
[O] u2 p2,    or
[S] u2 p2,    or
[NH] u2 p1,
instances with a different number of lone pairs are forbidden
""",
)

