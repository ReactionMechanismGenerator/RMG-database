#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/groups"
shortDesc = ""
longDesc = """
The reaction site *3 needs a lone pair in order to react. It cannot be 2S or 4S.
"""

template(reactants=["X_H_or_Xrad_H_Xbirad_H_Xtrirad_H", "Y_rad_birad_trirad_quadrad"], products=["X_H_or_Xrad_H_Xbirad_H_Xtrirad_H", "Y_rad_birad_trirad_quadrad"], ownReverse=True)

reversible = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 0,
    label = "X_H_or_Xrad_H_Xbirad_H_Xtrirad_H",
    group = "OR{Xtrirad_H, Xbirad_H, Xrad_H, X_H}",
    kinetics = None,
)

entry(
    index = 1,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_rad, Y_1centerbirad, Y_1centertrirad, Y_1centerquadrad}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Xtrirad_H",
    group = "OR{C_quartet_H, C_doublet_H}",
    kinetics = None,
)

entry(
    index = 3,
    label = "C_doublet_H",
    group =
"""
1 *1 C u1 p1 {2,S}
2 *2 H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C_quartet_H",
    group =
"""
1 *1 C u3 p0 {2,S}
2 *2 H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Xbirad_H",
    group = "OR{NH_triplet_H, NH_singlet_H, C/H_or_Val7/2_triplet_/H_or_Val7/, C/H_or_Val7/2_singlet_/H_or_Val7/}",
    kinetics = None,
)

entry(
    index = 6,
    label = "C/H_or_Val7/2_triplet_/H_or_Val7/",
    group =
"""
1 *1 Cs       u2 {2,S} {3,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "CH2_triplet_H",
    group =
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CH2_triplet_H-F",
    group =
"""
1 *1 Cs  u2 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CH2_triplet_H-Cl",
    group =
"""
1 *1 Cs   u2 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "CH2_triplet_H-Br",
    group =
"""
1 *1 Cs   u2 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "C/H_or_Val7/2_singlet_/H_or_Val7/",
    group =
"""
1 *1 C        u0 p1 {2,S} {3,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "CH2_singlet_H",
    group =
"""
1 *1 C u0 p1 {2,S} {3,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "CH2_singlet_H-F",
    group =
"""
1 *1 C   u0 p1 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "CH2_singlet_H-Cl",
    group =
"""
1 *1 C    u0 p1 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "CH2_singlet_H-Br",
    group =
"""
1 *1 C    u0 p1 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "NH_triplet_H",
    group =
"""
1 *1 N u2 p1 {2,S}
2 *2 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "NH_singlet_H",
    group =
"""
1 *1 N u0 p2 {2,S}
2 *2 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Xrad_H",
    group =
"""
1 *1 R!H!Val7 u1 {2,S}
2 *2 H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "C_rad_H",
    group =
"""
1 *1 C u1 {2,S}
2 *2 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "C/H_or_Val7/3_rad_/H_or_Val7/",
    group =
"""
1 *1 Cs       u1 {2,S} {3,S} {4,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "CH3_rad_H",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "CH3_rad_H-HF",
    group =
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "CH3_rad_H-HCl",
    group =
"""
1 *1 Cs   u1 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CH3_rad_H-HBr",
    group =
"""
1 *1 Cs   u1 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CH3_rad_H-FF",
    group =
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "CH3_rad_H-FCl",
    group =
"""
1 *1 Cs   u1 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "CH3_rad_H-FBr",
    group =
"""
1 *1 Cs   u1 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CH3_rad_H-ClCl",
    group =
"""
1 *1 Cs   u1 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "CH3_rad_H-ClBr",
    group =
"""
1 *1 Cs   u1 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "CH3_rad_H-BrBr",
    group =
"""
1 *1 Cs   u1 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Cs/H_or_Val7/2/OneDeN",
    group =
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 H          u0 {1,S}
3    [H,Val7]   u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Cs/H2/OneDeN",
    group =
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 H          u0 {1,S}
3    H          u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Cs/H2/OneDeN-F",
    group =
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 H          u0 {1,S}
3    F1s        u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Cs/H2/OneDeN-Cl",
    group =
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 H          u0 {1,S}
3    Cl1s       u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Cs/H2/OneDeN-Br",
    group =
"""
1 *1 C          u1 {2,S} {3,S} {4,S}
2 *2 H          u0 {1,S}
3    Br1s       u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "OH_rad_H",
    group =
"""
1 *1 O u1 {2,S}
2 *2 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "Srad_H",
    group =
"""
1 *1 S u1 {2,S}
2 *2 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "N3s_rad_H",
    group =
"""
1 *1 N3s u1 {2,S}
2 *2 H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "N/H_or_Val7/2_rad_/H_or_Val7/",
    group =
"""
1 *1 N3s      u1 {2,S} {3,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "NH2_rad_H",
    group =
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "NH2_rad_H-F",
    group =
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "NH2_rad_H-Cl",
    group =
"""
1 *1 N3s  u1 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "NH2_rad_H-Br",
    group =
"""
1 *1 N3s  u1 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "N3s_rad_H_pri",
    group =
"""
1 *1 N3s     u1 {2,S} {3,S}
2 *2 H       u0 {1,S}
3    [C,N,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "N3s_rad_H/H/NonDeN",
    group =
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "N5sc_radH",
    group =
"""
1 *1 N5sc u1 {2,S}
2 *2 H    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "X_H",
    group =
"""
1 *1 R u0 {2,S}
2 *2 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "H2",
    group =
"""
1 *1 H u0 {2,S}
2 *2 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Ct_H",
    group =
"""
1 *1 Ct    u0 {2,S} {3,T}
2 *2 H     u0 {1,S}
3    [C,N] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Ct/H/NonDeC",
    group =
"""
1 *1 Ct u0 {2,S} {3,T}
2 *2 H  u0 {1,S}
3    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Ct/H/NonDeN",
    group =
"""
1 *1 Ct  u0 {2,S} {3,T}
2 *2 H   u0 {1,S}
3    N3t u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "O_H",
    group =
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "O_pri-H_or_Val7-1",
    group =
"""
1 *1 O        u0 {2,S} {3,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "O_pri",
    group =
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "O_pri-F",
    group =
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "O_pri-Cl",
    group =
"""
1 *1 O    u0 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "O_pri-Br",
    group =
"""
1 *1 O    u0 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "O_sec",
    group =
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "O/H/NonDeC",
    group =
"""
1 *1 O  u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "O/H/NonDeO",
    group =
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "/H_or_Val7/2O2",
    group =
"""
1 *1 O        u0 {2,S} {3,S}
2    O        u0 {1,S} {4,S}
3 *2 H        u0 {1,S}
4    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "H2O2",
    group =
"""
1 *1 O u0 {2,S} {3,S}
2    O u0 {1,S} {4,S}
3 *2 H u0 {1,S}
4    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "H2O2-F",
    group =
"""
1 *1 O   u0 {2,S} {3,S}
2    O   u0 {1,S} {4,S}
3 *2 H   u0 {1,S}
4    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "H2O2-Cl",
    group =
"""
1 *1 O    u0 {2,S} {3,S}
2    O    u0 {1,S} {4,S}
3 *2 H    u0 {1,S}
4    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "H2O2-Br",
    group =
"""
1 *1 O    u0 {2,S} {3,S}
2    O    u0 {1,S} {4,S}
3 *2 H    u0 {1,S}
4    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "ROO/H_or_Val7/_pri",
    group =
"""
1    C        u0 {2,S} {4,S} {5,S} {6,S}
2    O        u0 {1,S} {3,S}
3 *1 O        u0 {2,S} {7,S}
4    Cs       u0 {1,S}
5    [H,Val7] u0 {1,S}
6    [H,Val7] u0 {1,S}
7 *2 H        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "ROOH_pri",
    group =
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7 *2 H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "ROO/H_or_Val7/_sec",
    group =
"""
1    C        u0 {2,S} {4,S} {5,S} {6,S}
2    O        u0 {1,S} {3,S}
3 *1 O        u0 {2,S} {7,S}
4    Cs       u0 {1,S}
5    Cs       u0 {1,S}
6    [H,Val7] u0 {1,S}
7 *2 H        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "ROOH_sec",
    group =
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    H  u0 {1,S}
7 *2 H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "ROOH_sec-F",
    group =
"""
1    C   u0 {2,S} {4,S} {5,S} {6,S}
2    O   u0 {1,S} {3,S}
3 *1 O   u0 {2,S} {7,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    F1s u0 {1,S}
7 *2 H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "ROOH_sec-Cl",
    group =
"""
1    C    u0 {2,S} {4,S} {5,S} {6,S}
2    O    u0 {1,S} {3,S}
3 *1 O    u0 {2,S} {7,S}
4    Cs   u0 {1,S}
5    Cs   u0 {1,S}
6    Cl1s u0 {1,S}
7 *2 H    u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "ROOH_sec-Br",
    group =
"""
1    C    u0 {2,S} {4,S} {5,S} {6,S}
2    O    u0 {1,S} {3,S}
3 *1 O    u0 {2,S} {7,S}
4    Cs   u0 {1,S}
5    Cs   u0 {1,S}
6    Br1s u0 {1,S}
7 *2 H    u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "ROOH_ter",
    group =
"""
1    C  u0 {2,S} {4,S} {5,S} {6,S}
2    O  u0 {1,S} {3,S}
3 *1 O  u0 {2,S} {7,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {1,S}
7 *2 H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "O/H/NonDeN",
    group =
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "O/H/OneDe",
    group =
"""
1 *1 O                         u0 {2,S} {3,S}
2 *2 H                         u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "O/H/OneDeC",
    group =
"""
1 *1 O                u0 {2,S} {3,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "O/H/OneDeN",
    group =
"""
1 *1 O          u0 {2,S} {3,S}
2 *2 H          u0 {1,S}
3    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "OSrad_O_H",
    group =
"""
1 *1 O     u0 {2,S} {3,S}
2 *2 H     u0 {1,S}
3    [O,S] u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Orad_O_H",
    group =
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    O u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Srad_O_H",
    group =
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    S u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "S_H",
    group =
"""
1 *1 S u0 {2,S}
2 *2 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "S_pri-H_or_Val7-1",
    group =
"""
1 *1 S2s      u0 {2,S} {3,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "S_pri",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "S_pri-F",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "S_pri-Cl",
    group =
"""
1 *1 S2s  u0 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "S_pri-Br",
    group =
"""
1 *1 S2s  u0 {2,S} {3,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "S/H/single",
    group =
"""
1 *1 S   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "S/H/NonDeC",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "S/H/NonDeS",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "S/H/NonDeN",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "S/H/NonDeO",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "S/H/OneDe",
    group =
"""
1 *1 S2s              u0 {2,S} {3,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "S/H/Ct",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "S/H/Cb",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "S/H/CO",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "S/H/Cd",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2    Cd  u0 {1,S} {4,D}
3 *2 H   u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "S/H/CS",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2    CS  u0 {1,S} {4,D}
3 *2 H   u0 {1,S}
4    S   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "S/H/Rad",
    group =
"""
1 *1 S   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    R!H!Val7 u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "S/H/CRad",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    Cs  u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "S/H/SRad",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S   u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "S/H/NRad",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    N   u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "S/H/ORad",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    O   u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "S/H/MulBondRad",
    group =
"""
1 *1 S2s        u0 {2,S} {3,S}
2 *2 H          u0 {1,S}
3    [Cd,CO,CS] u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "S/H/CORad",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    CO  u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "S/H/CdRad",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2    Cd  u1 {1,S} {4,D}
3 *2 H   u0 {1,S}
4    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "S/H/CSRad",
    group =
"""
1 *1 S2s u0 {2,S} {3,S}
2    CS  u1 {1,S} {4,D}
3 *2 H   u0 {1,S}
4    S   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "S/H/double",
    group =
"""
1 *1 S   u0 p[0,1] {2,S} {3,D}
2 *2 H   u0 {1,S}
3    R!H!Val7 ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "S/H/double_val4",
    group =
"""
1 *1 S   u0 p1 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    R!H!Val7 ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "S/H/double_val4C",
    group =
"""
1 *1 S u0 p1 {2,S} {3,D}
2 *2 H u0 {1,S}
3    C ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "S/H/double_val4N",
    group =
"""
1 *1 S u0 p1 {2,S} {3,D}
2 *2 H u0 {1,S}
3    N ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "S/H/double_val4S",
    group =
"""
1 *1 S u0 p1 {2,S} {3,D}
2 *2 H u0 {1,S}
3    S ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "S/H/double_val4O",
    group =
"""
1 *1 S u0 p1 {2,S} {3,D}
2 *2 H u0 {1,S}
3    O ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "S/H/double_val6",
    group =
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    R!H!Val7 ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "S/H/double_val6C",
    group =
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    C   ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "S/H/double_val6N",
    group =
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    N   ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "S/H/double_val6S",
    group =
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    S   ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "S/H/double_val6O",
    group =
"""
1 *1 S6d u0 p0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    O   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "S/H/twoDoubles",
    group =
"""
1 *1 S6dd u0 p0 {2,S} {3,D} {4,D}
2 *2 H    u0 {1,S}
3    R!H!Val7  ux {1,D}
4    R!H!Val7  ux {1,D}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "S/H/twoDoublesOO",
    group =
"""
1 *1 S6dd u0 p0 {2,S} {3,D} {4,D}
2 *2 H    u0 {1,S}
3    O    u0 {1,D}
4    O    u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "S/H/triple",
    group =
"""
1 *1 S   u0 p[0,1] {2,S} {3,T}
2 *2 H   u0 {1,S}
3    R!H!Val7 ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "S/H/triple_val4",
    group =
"""
1 *1 S   u0 p1 {2,S} {3,T}
2 *2 H   u0 {1,S}
3    R!H!Val7 ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "S/H/triple_val4C",
    group =
"""
1 *1 S u0 p1 {2,S} {3,T}
2 *2 H u0 {1,S}
3    C ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "S/H/triple_val4N",
    group =
"""
1 *1 S u0 p1 {2,S} {3,T}
2 *2 H u0 {1,S}
3    N u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "S/H/triple_val4S",
    group =
"""
1 *1 S u0 p1 {2,S} {3,T}
2 *2 H u0 {1,S}
3    S ux p[0,1] {1,T}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "S/H/triple_val6",
    group =
"""
1 *1 S   u0 p0 {2,S} {3,T}
2 *2 H   u0 {1,S}
3    R!H!Val7 ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "S/H/triple_val6C",
    group =
"""
1 *1 S u0 p0 {2,S} {3,T}
2 *2 H u0 {1,S}
3    C ux {1,T}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "S/H/triple_val6N",
    group =
"""
1 *1 S u0 p0 {2,S} {3,T}
2 *2 H u0 {1,S}
3    N u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "S/H/triple_val6S",
    group =
"""
1 *1 S u0 p0 {2,S} {3,T}
2 *2 H u0 {1,S}
3    S ux p[0,1] {1,T}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "Cd_H",
    group =
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2    [C,N] u0 {1,D}
3 *2 H     u0 {1,S}
4    R     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "Cd_pri-H_or_Val7-1",
    group =
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    [Cd,N]   u0 {1,D} {5,S}
3 *2 H        u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "Cd_pri",
    group =
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 H      u0 {1,S}
4    H      u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "Cd/H2/NonDeC",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "Cd/H2/NonDeN",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    N3d u0 {1,D} {5,S}
3 *2 H   u0 {1,S}
4    H   u0 {1,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "Cd_pri-F",
    group =
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 H      u0 {1,S}
4    F1s    u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "Cd/H2/NonDeC-F",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cd  u0 {1,D} {5,S}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "Cd/H2/NonDeN-F",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    N3d u0 {1,D} {5,S}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
5    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "Cd_pri-Cl",
    group =
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 H      u0 {1,S}
4    Cl1s   u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "Cd/H2/NonDeC-Cl",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    Cd   u0 {1,D} {5,S}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "Cd/H2/NonDeN-Cl",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    N3d  u0 {1,D} {5,S}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "Cd_pri-Br",
    group =
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 H      u0 {1,S}
4    Br1s   u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "Cd/H2/NonDeC-Br",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    Cd   u0 {1,D} {5,S}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "Cd/H2/NonDeN-Br",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    N3d  u0 {1,D} {5,S}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
5    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "Cd_sec",
    group =
"""
1 *1 C      u0 {2,D} {3,S} {4,S}
2    [Cd,N] u0 {1,D} {5,S}
3 *2 H      u0 {1,S}
4    R!H!Val7    u0 {1,S}
5    R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "Cd/H/NonDeC",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 H  u0 {1,S}
4    Cs u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "Cd/H/NonDeO",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 H  u0 {1,S}
4    O  u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "Cd/H/NonDeS",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 H  u0 {1,S}
4    S  u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "Cd/H/NonDeN",
    group =
"""
1 *1 C          u0 {2,D} {3,S} {4,S}
2    Cd         u0 {1,D} {5,S}
3 *2 H          u0 {1,S}
4    [N3s,N5sc] u0 {1,S}
5    R          u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "Cd/H/OneDe",
    group =
"""
1 *1 C                                                u0 {2,D} {3,S} {4,S}
2    Cd                                               u0 {1,D} {5,S}
3 *2 H                                                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N3d,N3t,N3b,N5dc,N5ddc,N5tc,N5b] u0 {1,S}
5    R                                                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "Cd/H/Ct",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 H  u0 {1,S}
4    Ct u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "Cd/H/Cb",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 H  u0 {1,S}
4    Cb u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "Cd/H/CO",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 H  u0 {1,S}
4    CO u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "Cd/H/Cd",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {6,S}
3    Cd u0 {1,S} {5,D}
4 *2 H  u0 {1,S}
5    C  u0 {3,D}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Cd/H/CS",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S}
3 *2 H  u0 {1,S}
4    CS u0 {1,S}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "Cd/H/DeN",
    group =
"""
1 *1 C                                 u0 {2,D} {3,S} {4,S}
2    Cd                                u0 {1,D} {5,S}
3 *2 H                                 u0 {1,S}
4    [N3d,N3t,N3b,N5dc,N5ddc,N5tc,N5b] u0 {1,S}
5    R                                 u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Cd_allenic",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cdd u0 {1,D}
3 *2 H   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "Cd_Cdd/H_or_Val7/2",
    group =
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    Cdd      u0 {1,D}
3 *2 H        u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Cd_Cdd/H2",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cdd u0 {1,D}
3 *2 H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "Cd_Cdd/H2-F",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    Cdd u0 {1,D}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "Cd_Cdd/H2-Cl",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    Cdd  u0 {1,D}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Cd_Cdd/H2-Br",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    Cdd  u0 {1,D}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Cb_H",
    group =
"""
1 *1 Cb       u0 {2,B} {3,B} {4,S}
2    [Cb,Cbf] u0 {1,B}
3    [Cb,Cbf] u0 {1,B}
4 *2 H        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "CO_H",
    group =
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    O u0 {1,D}
3 *2 H u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "CO_pri-H_or_Val7-1",
    group =
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    O        u0 {1,D}
3 *2 H        u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "CO_pri",
    group =
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    O u0 {1,D}
3 *2 H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "CO_pri-F",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    O   u0 {1,D}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "CO_pri-Cl",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    O    u0 {1,D}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "CO_pri-Br",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    O    u0 {1,D}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "CO_sec",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    O   u0 {1,D}
3 *2 H   u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "CO/H/NonDe",
    group =
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    O        u0 {1,D}
3 *2 H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "CO/H/Cs",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    O  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "CO/H/Cs\Cs|Cs",
    group =
"""
1 *1 C  u0 {2,S} {4,D} {5,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {6,S}
4    O  u0 {1,D}
5 *2 H  u0 {1,S}
6    Cs u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "CO/H/OneDe",
    group =
"""
1 *1 C                u0 {2,D} {3,S} {4,S}
2    O                u0 {1,D}
3 *2 H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "CS_H",
    group =
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 H u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "CS_pri-H_or_Val7-1",
    group =
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    S        u0 {1,D}
3 *2 H        u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "CS_pri",
    group =
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "CS_pri-F",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    S   u0 {1,D}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "CS_pri-Cl",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    S    u0 {1,D}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "CS_pri-Br",
    group =
"""
1 *1 C    u0 {2,D} {3,S} {4,S}
2    S    u0 {1,D}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "CS_sec",
    group =
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    S   u0 {1,D}
3 *2 H   u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "CS/H/NonDeC",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "CS/H/NonDeO",
    group =
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 H u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "CS/H/NonDeS",
    group =
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 H u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "CS/H/OneDe",
    group =
"""
1 *1 C                u0 {2,D} {3,S} {4,S}
2    S                u0 {1,D}
3 *2 H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "CS/H/Ct",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "CS/H/Cb",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "CS/H/CO",
    group =
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "CS/H/Cd",
    group =
"""
1 *1 C  u0 {2,S} {3,D} {4,S}
2    Cd u0 {1,S} {5,D}
3    S  u0 {1,D}
4 *2 H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "CS/H/CS",
    group =
"""
1 *1 C  u0 {2,S} {3,D} {4,S}
2    CS u0 {1,S} {5,D}
3    S  u0 {1,D}
4 *2 H  u0 {1,S}
5    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "Cs_H",
    group =
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
5    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "C_methane-H_or_Val7-3",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "C_methane",
    group =
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "C_methane-HHF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "C_methane-HHCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "C_methane-HHBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "C_methane-HFF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "C_methane-HFCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "C_methane-HFBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "C_methane-HClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "C_methane-HClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "C_methane-HBrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "C_methane-FFF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "C_methane-FFCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "C_methane-FFBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "C_methane-FClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "C_methane-FClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "C_methane-FBrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "C_methane-ClClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "C_methane-ClClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "C_methane-ClBrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "C_methane-BrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "C_pri-H_or_Val7-2",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R!H!Val7      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "C_pri",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "C/H3/Cs",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "C/H3/Cs\H3",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "C/H3/Cs\OneNonDe",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    H        u0 {2,S}
8    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "C/H3/Cs\H2\Cs",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "C/H3/Cs\H2\Cs|O",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 H     u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "C/H3/Cs\H2\O",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    [O,S] u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "C/H3/Cs\TwoNonDe",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "C/H3/Cs\H\Cs\O",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "C/H3/Cs\H\Cs\Cs|O",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    H     u0 {1,S}
6 *2 H     u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "C/H3/Cs\TwoDe",
    group =
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H             u0 {1,S}
4    H             u0 {1,S}
5    H             u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    H             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "1_methyl_CPD",
    group =
"""
1     Cs u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs u0 {1,S} {8,S} {9,S} {10,S}
3     Cd u0 {1,S} {5,D}
4     Cd u0 {1,S} {6,D}
5     Cd u0 {3,D} {6,S}
6     Cd u0 {4,D} {5,S}
7     H  u0 {1,S}
8  *2 H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "C/H3/O",
    group =
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "C/H3/S",
    group =
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "C/H3/OneDe",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "C/H3/Ct",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "C/H3/Cb",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "C/H3/CO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "C/H3/CS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 231,
    label = "C/H3/Cd",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "2_methyl_CPD",
    group =
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S}
4    C  u0 {2,S} {6,S}
5    Cd u0 {3,S} {6,D}
6    Cd u0 {4,S} {5,D}
7 *2 H  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "3_methyl_CPD",
    group =
"""
1 *1 Cs u0 {2,S} {7,S} {8,S} {9,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {6,S}
4    Cd u0 {2,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    C  u0 {3,S} {5,S}
7 *2 H  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "C/H3/Cd\H_Cd\H2",
    group =
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "C/H3/Cd\H_Cd\H\Cs",
    group =
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    Cs u0 {3,S}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "C/H3/Cd\Cs_Cd\H2",
    group =
"""
1 *1 C  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3    Cd u0 {2,D} {8,S} {9,S}
4 *2 H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    H  u0 {3,S}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "Cs/H3/NonDeN",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 238,
    label = "Cs/H3/OneDeN",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    H          u0 {1,S}
5    H          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "C_pri-HF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "C/H3/O-HF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "C/H3/S-HF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "C/H3/OneDe-HF",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    F1s              u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "C/H3/Ct-HF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "C/H3/Cb-HF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "C/H3/CO-HF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "C/H3/CS-HF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "C/H3/Cd-HF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3 *2 H   u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {1,S}
6    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "Cs/H3/NonDeN-HF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 H   u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "Cs/H3/OneDeN-HF",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    H          u0 {1,S}
5    F1s        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "C_pri-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "C/H3/Cs-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "C/H3/O-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "C/H3/S-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "C/H3/OneDe-HCl",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    Cl1s             u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "C/H3/Ct-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "C/H3/Cb-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "C/H3/CO-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "C/H3/CS-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 259,
    label = "C/H3/Cd-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {1,S}
6    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "Cs/H3/NonDeN-HCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    N3s  u0 {1,S}
3 *2 H    u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "Cs/H3/OneDeN-HCl",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    H          u0 {1,S}
5    Cl1s       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "C_pri-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "C/H3/Cs-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "C/H3/Cs\H3-HBrBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cs   u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {1,S}
6    Br1s u0 {2,S}
7    Br1s u0 {2,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "C/H3/Cs\OneNonDe-HBrBrBr",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H        u0 {1,S}
4    H        u0 {1,S}
5    Br1s     u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    Br1s     u0 {2,S}
8    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "C/H3/Cs\H2\Cs-HBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cs   u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {1,S}
6    Cs   u0 {2,S}
7    Br1s u0 {2,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "C/H3/Cs\H2\O-HBrBrBr",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    H     u0 {1,S}
5    Br1s  u0 {1,S}
6    [O,S] u0 {2,S}
7    Br1s  u0 {2,S}
8    Br1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "C/H3/Cs\TwoNonDe-HBrBr",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H        u0 {1,S}
4    H        u0 {1,S}
5    Br1s     u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    Br1s     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "C/H3/Cs\H\Cs\O-HBrBr",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    H     u0 {1,S}
5    Br1s  u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "C/H3/Cs\H\Cs\Cs|O-HBrBr",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br1s  u0 {1,S}
6 *2 H     u0 {2,S}
7    H     u0 {2,S}
8    Br1s  u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "C/H3/Cs\TwoDe-HBrBr",
    group =
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2    Cs            u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H             u0 {1,S}
4    H             u0 {1,S}
5    Br1s          u0 {1,S}
6    [Cd,CO,Cb,Ct] u0 {2,S}
7    [Cd,CO,Cb,Ct] u0 {2,S}
8    Br1s          u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "1_methyl_CPD-HBrBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs   u0 {1,S} {8,S} {9,S} {10,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {6,S}
6     Cd   u0 {4,D} {5,S}
7     Br1s u0 {1,S}
8  *2 H    u0 {2,S}
9     H    u0 {2,S}
10    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "C/H3/Cs\H2\Cs|O-HHHBr",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *2 H     u0 {2,S}
7    H     u0 {2,S}
8    Br1s  u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "C/H3/O-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "C/H3/S-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "C/H3/OneDe-HBr",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    Br1s             u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "C/H3/Ct-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 278,
    label = "C/H3/Cb-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "C/H3/CO-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "C/H3/CS-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "C/H3/Cd-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {1,S}
6    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "2_methyl_CPD-HBr",
    group =
"""
1 *1 Cs   u0 {2,S} {7,S} {8,S} {9,S}
2    Cd   u0 {1,S} {3,D} {4,S}
3    Cd   u0 {2,D} {5,S}
4    C    u0 {2,S} {6,S}
5    Cd   u0 {3,S} {6,D}
6    Cd   u0 {4,S} {5,D}
7 *2 H    u0 {1,S}
8    H    u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "3_methyl_CPD-HBr",
    group =
"""
1 *1 Cs   u0 {2,S} {7,S} {8,S} {9,S}
2    Cd   u0 {1,S} {3,D} {4,S}
3    Cd   u0 {2,D} {6,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {4,D} {6,S}
6    C    u0 {3,S} {5,S}
7 *2 H    u0 {1,S}
8    H    u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 284,
    label = "C/H3/Cd\H_Cd\H2-HBrBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    H    u0 {1,S}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    Br1s u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "C/H3/Cd\H_Cd\H\Cs-HBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    H    u0 {1,S}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    Cs   u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 286,
    label = "C/H3/Cd\Cs_Cd\H2-HBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    H    u0 {1,S}
6    Br1s u0 {1,S}
7    Cs   u0 {2,S}
8    Br1s u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "Cs/H3/NonDeN-HBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    N3s  u0 {1,S}
3 *2 H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "Cs/H3/OneDeN-HBr",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    H          u0 {1,S}
5    Br1s       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "C_pri-FF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "C/H3/O-FF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "C/H3/S-FF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "C/H3/OneDe-FF",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    F1s              u0 {1,S}
4    F1s              u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "C/H3/Ct-FF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "C/H3/Cb-FF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "C/H3/CO-FF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "C/H3/CS-FF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "C/H3/Cd-FF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
6    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "Cs/H3/NonDeN-FF",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "Cs/H3/OneDeN-FF",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    F1s        u0 {1,S}
5    F1s        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "C/H3/Cs\H2\Cs|O-FFFF",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    F1s   u0 {1,S}
5    F1s   u0 {1,S}
6 *2 H     u0 {2,S}
7    F1s   u0 {2,S}
8    F1s   u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "C_pri-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "C/H3/Cs-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "C/H3/O-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "C/H3/S-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "C/H3/OneDe-FCl",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    F1s              u0 {1,S}
4    Cl1s             u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "C/H3/Ct-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "C/H3/Cb-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "C/H3/CO-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "C/H3/CS-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "C/H3/Cd-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {1,S}
6    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "Cs/H3/NonDeN-FCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    N3s  u0 {1,S}
3 *2 H    u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "Cs/H3/OneDeN-FCl",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    F1s        u0 {1,S}
5    Cl1s       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "C_pri-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "C/H3/Cs-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "C/H3/Cs\H2\Cs-FBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cs   u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H    u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {1,S}
6    Cs   u0 {2,S}
7    Br1s u0 {2,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "C/H3/Cs\H2\O-FBrBrBr",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    F1s   u0 {1,S}
5    Br1s  u0 {1,S}
6    [O,S] u0 {2,S}
7    Br1s  u0 {2,S}
8    Br1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "C/H3/Cs\H\Cs\O-FBrBr",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    F1s   u0 {1,S}
5    Br1s  u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "C/H3/Cs\H\Cs\Cs|O-FBrBr",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br1s  u0 {1,S}
6 *2 H     u0 {2,S}
7    F1s   u0 {2,S}
8    Br1s  u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "1_methyl_CPD-FBrBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs   u0 {1,S} {8,S} {9,S} {10,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {6,S}
6     Cd   u0 {4,D} {5,S}
7     Br1s u0 {1,S}
8  *2 H    u0 {2,S}
9     F1s  u0 {2,S}
10    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "C/H3/O-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "C/H3/S-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "C/H3/OneDe-FBr",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    F1s              u0 {1,S}
4    Br1s             u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "C/H3/Ct-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "C/H3/Cb-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "C/H3/CO-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "C/H3/CS-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "C/H3/Cd-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {1,S}
6    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "2_methyl_CPD-FBr",
    group =
"""
1 *1 Cs   u0 {2,S} {7,S} {8,S} {9,S}
2    Cd   u0 {1,S} {3,D} {4,S}
3    Cd   u0 {2,D} {5,S}
4    C    u0 {2,S} {6,S}
5    Cd   u0 {3,S} {6,D}
6    Cd   u0 {4,S} {5,D}
7 *2 H    u0 {1,S}
8    F1s  u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "3_methyl_CPD-FBr",
    group =
"""
1 *1 Cs   u0 {2,S} {7,S} {8,S} {9,S}
2    Cd   u0 {1,S} {3,D} {4,S}
3    Cd   u0 {2,D} {6,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {4,D} {6,S}
6    C    u0 {3,S} {5,S}
7 *2 H    u0 {1,S}
8    F1s  u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "C/H3/Cd\H_Cd\H2-FBrBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    F1s  u0 {1,S}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    Br1s u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "C/H3/Cd\H_Cd\H\Cs-FBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    F1s  u0 {1,S}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    Cs   u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "C/H3/Cd\Cs_Cd\H2-FBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    F1s  u0 {1,S}
6    Br1s u0 {1,S}
7    Cs   u0 {2,S}
8    Br1s u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "Cs/H3/NonDeN-FBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    N3s  u0 {1,S}
3 *2 H    u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "Cs/H3/OneDeN-FBr",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    F1s        u0 {1,S}
5    Br1s       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "C_pri-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "C/H3/Cs-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "C/H3/Cs\H2\Cs|O-ClClClCl",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cl1s  u0 {1,S}
5    Cl1s  u0 {1,S}
6 *2 H     u0 {2,S}
7    Cl1s  u0 {2,S}
8    Cl1s  u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "C/H3/O-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "C/H3/S-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "C/H3/OneDe-ClCl",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Cl1s             u0 {1,S}
4    Cl1s             u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "C/H3/Ct-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "C/H3/Cb-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "C/H3/CO-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "C/H3/CS-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "C/H3/Cd-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {1,S}
6    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "Cs/H3/NonDeN-ClCl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    N3s  u0 {1,S}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "Cs/H3/OneDeN-ClCl",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    Cl1s       u0 {1,S}
5    Cl1s       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "C_pri-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "C/H3/Cs-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "C/H3/Cs\H2\Cs-ClBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cs   u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {1,S}
6    Cs   u0 {2,S}
7    Br1s u0 {2,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "C/H3/Cs\H2\O-ClBrBrBr",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    Cl1s  u0 {1,S}
5    Br1s  u0 {1,S}
6    [O,S] u0 {2,S}
7    Br1s  u0 {2,S}
8    Br1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "1_methyl_CPD-ClBrBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs   u0 {1,S} {8,S} {9,S} {10,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {6,S}
6     Cd   u0 {4,D} {5,S}
7     Br1s u0 {1,S}
8  *2 H    u0 {2,S}
9     Cl1s u0 {2,S}
10    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "C/H3/Cs\H\Cs\O-ClBrBr",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    Cl1s  u0 {1,S}
5    Br1s  u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "C/H3/Cs\H\Cs\Cs|O-ClBrBr",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br1s  u0 {1,S}
6 *2 H     u0 {2,S}
7    Cl1s  u0 {2,S}
8    Br1s  u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "C/H3/O-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 356,
    label = "C/H3/S-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 357,
    label = "C/H3/OneDe-ClBr",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Cl1s             u0 {1,S}
4    Br1s             u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 358,
    label = "C/H3/Ct-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 359,
    label = "C/H3/Cb-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 360,
    label = "C/H3/CO-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 361,
    label = "C/H3/CS-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 362,
    label = "C/H3/Cd-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {1,S}
6    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 363,
    label = "2_methyl_CPD-ClBr",
    group =
"""
1 *1 Cs   u0 {2,S} {7,S} {8,S} {9,S}
2    Cd   u0 {1,S} {3,D} {4,S}
3    Cd   u0 {2,D} {5,S}
4    C    u0 {2,S} {6,S}
5    Cd   u0 {3,S} {6,D}
6    Cd   u0 {4,S} {5,D}
7 *2 H    u0 {1,S}
8    Cl1s u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 364,
    label = "3_methyl_CPD-ClBr",
    group =
"""
1 *1 Cs   u0 {2,S} {7,S} {8,S} {9,S}
2    Cd   u0 {1,S} {3,D} {4,S}
3    Cd   u0 {2,D} {6,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {4,D} {6,S}
6    C    u0 {3,S} {5,S}
7 *2 H    u0 {1,S}
8    Cl1s u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 365,
    label = "C/H3/Cd\H_Cd\H2-ClBrBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    Cl1s u0 {1,S}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    Br1s u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 366,
    label = "C/H3/Cd\H_Cd\H\Cs-ClBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    Cl1s u0 {1,S}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    Cs   u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 367,
    label = "C/H3/Cd\Cs_Cd\H2-ClBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    Cl1s u0 {1,S}
6    Br1s u0 {1,S}
7    Cs   u0 {2,S}
8    Br1s u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 368,
    label = "Cs/H3/NonDeN-ClBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    N3s  u0 {1,S}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 369,
    label = "Cs/H3/OneDeN-ClBr",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    Cl1s       u0 {1,S}
5    Br1s       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 370,
    label = "C_pri-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 371,
    label = "C/H3/Cs-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 372,
    label = "C/H3/Cs\H2\Cs-BrBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cs   u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
6    Cs   u0 {2,S}
7    Br1s u0 {2,S}
8    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 373,
    label = "C/H3/Cs\H2\Cs|O-BrBrBrBr",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Br1s  u0 {1,S}
5    Br1s  u0 {1,S}
6 *2 H     u0 {2,S}
7    Br1s  u0 {2,S}
8    Br1s  u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 374,
    label = "C/H3/Cs\H2\O-BrBrBrBr",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    Br1s  u0 {1,S}
5    Br1s  u0 {1,S}
6    [O,S] u0 {2,S}
7    Br1s  u0 {2,S}
8    Br1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 375,
    label = "1_methyl_CPD-BrBrBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {4,S} {7,S}
2  *1 Cs   u0 {1,S} {8,S} {9,S} {10,S}
3     Cd   u0 {1,S} {5,D}
4     Cd   u0 {1,S} {6,D}
5     Cd   u0 {3,D} {6,S}
6     Cd   u0 {4,D} {5,S}
7     Br1s u0 {1,S}
8  *2 H    u0 {2,S}
9     Br1s u0 {2,S}
10    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 376,
    label = "C/H3/Cs\H\Cs\O-BrBrBr",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H     u0 {1,S}
4    Br1s  u0 {1,S}
5    Br1s  u0 {1,S}
6    Cs    u0 {2,S}
7    [O,S] u0 {2,S}
8    Br1s  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 377,
    label = "C/H3/Cs\H\Cs\Cs|O-BrBrBr",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3    Cs    u0 {1,S} {9,S}
4    Cs    u0 {1,S}
5    Br1s  u0 {1,S}
6 *2 H     u0 {2,S}
7    Br1s  u0 {2,S}
8    Br1s  u0 {2,S}
9    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 378,
    label = "C/H3/O-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 379,
    label = "C/H3/S-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 380,
    label = "C/H3/OneDe-BrBr",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Br1s             u0 {1,S}
4    Br1s             u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 381,
    label = "C/H3/Ct-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 382,
    label = "C/H3/Cb-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 383,
    label = "C/H3/CO-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 384,
    label = "C/H3/CS-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 385,
    label = "C/H3/Cd-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
6    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 386,
    label = "2_methyl_CPD-BrBr",
    group =
"""
1 *1 Cs   u0 {2,S} {7,S} {8,S} {9,S}
2    Cd   u0 {1,S} {3,D} {4,S}
3    Cd   u0 {2,D} {5,S}
4    C    u0 {2,S} {6,S}
5    Cd   u0 {3,S} {6,D}
6    Cd   u0 {4,S} {5,D}
7 *2 H    u0 {1,S}
8    Br1s u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 387,
    label = "3_methyl_CPD-BrBr",
    group =
"""
1 *1 Cs   u0 {2,S} {7,S} {8,S} {9,S}
2    Cd   u0 {1,S} {3,D} {4,S}
3    Cd   u0 {2,D} {6,S}
4    Cd   u0 {2,S} {5,D}
5    Cd   u0 {4,D} {6,S}
6    C    u0 {3,S} {5,S}
7 *2 H    u0 {1,S}
8    Br1s u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 388,
    label = "C/H3/Cd\H_Cd\H2-BrBrBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    Br1s u0 {1,S}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    Br1s u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 389,
    label = "C/H3/Cd\H_Cd\H\Cs-BrBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    Br1s u0 {1,S}
6    Br1s u0 {1,S}
7    Br1s u0 {2,S}
8    Cs   u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 390,
    label = "C/H3/Cd\Cs_Cd\H2-BrBrBrBr",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3    Cd   u0 {2,D} {8,S} {9,S}
4 *2 H    u0 {1,S}
5    Br1s u0 {1,S}
6    Br1s u0 {1,S}
7    Cs   u0 {2,S}
8    Br1s u0 {3,S}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 391,
    label = "Cs/H3/NonDeN-BrBr",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    N3s  u0 {1,S}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 392,
    label = "Cs/H3/OneDeN-BrBr",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5dc] u0 {1,S}
3 *2 H          u0 {1,S}
4    Br1s       u0 {1,S}
5    Br1s       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 393,
    label = "C_sec-H_or_Val7-1",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    R!H!Val7      u0 {1,S}
5    R!H!Val7      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 394,
    label = "C_sec",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H!Val7 u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 395,
    label = "C/H2/NonDeC",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 396,
    label = "C/H2/Cs/Cs\O",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S}
3 *2 H     u0 {1,S}
4    H     u0 {1,S}
5    Cs    u0 {1,S}
6    [O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 397,
    label = "C/H2/Cs/Cs\Cs|O",
    group =
"""
1 *1 C     u0 {2,S} {4,S} {5,S} {6,S}
2    Cs    u0 {1,S} {3,S}
3    Cs    u0 {2,S} {7,S}
4 *2 H     u0 {1,S}
5    H     u0 {1,S}
6    Cs    u0 {1,S}
7    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 398,
    label = "C/H2/NonDeC_5ring",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {6,S} {7,S}
2    Cs u0 {1,S} {4,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6 *2 H  u0 {1,S}
7    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 399,
    label = "C/H2/NonDeC_5ring_fused6_1",
    group =
"""
1 *1 C  u0 {2,S} {4,S} {8,S} {9,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {4,S} {5,S} {7,S}
4    Cs u0 {1,S} {3,S}
5    Cs u0 {2,S} {3,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 H  u0 {1,S}
9    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 400,
    label = "C/H2/NonDeC_5ring_fused6_2",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {8,S} {9,S}
2    Cs u0 {1,S} {4,S} {6,S}
3    Cs u0 {1,S} {5,S} {7,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8 *2 H  u0 {1,S}
9    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 401,
    label = "C/H2/NonDeC_5ring_alpha6ring",
    group =
"""
1  *1 C  u0 {2,S} {4,S} {10,S} {11,S}
2     Cs u0 {1,S} {3,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {5,S}
5     Cs u0 {3,S} {4,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 H  u0 {1,S}
11    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 402,
    label = "C/H2/NonDeC_5ring_beta6ring",
    group =
"""
1  *1 C  u0 {4,S} {5,S} {10,S} {11,S}
2     Cs u0 {3,S} {4,S} {6,S}
3     Cs u0 {2,S} {5,S} {7,S}
4     Cs u0 {1,S} {2,S}
5     Cs u0 {1,S} {3,S}
6     C  u0 {2,S} {8,S}
7     C  u0 {3,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10 *2 H  u0 {1,S}
11    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 403,
    label = "C/H2/Cs\H3/Cs\H3",
    group =
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     Cs u0 {1,S} {9,S} {10,S} {11,S}
4  *2 H  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 404,
    label = "C/H2/NonDeO",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    H        u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 405,
    label = "C/H2/CsO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 406,
    label = "C/H2/Cs\Cs2/O",
    group =
"""
1     Cs u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C  u0 {1,S} {5,S} {7,S} {8,S}
3     C  u0 {1,S} {9,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     O  u0 {2,S} {15,S}
6     H  u0 {1,S}
7  *2 H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {4,S}
15    H  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 407,
    label = "C/H2/O2",
    group =
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    O u0 {1,S}
5    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 408,
    label = "C/H2/NonDeS",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    H        u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 409,
    label = "C/H2/CsS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 410,
    label = "C/H2/NonDeN",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H          u0 {1,S}
3    H          u0 {1,S}
4    N          u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 411,
    label = "C/H2/OneDe",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 412,
    label = "C/H2/OneDeC",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 413,
    label = "C/H2/CtCs",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 414,
    label = "C/H2/CbCs",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 415,
    label = "C/H2/COCs",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 416,
    label = "C/H2/CO\H/Cs\H3",
    group =
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2     Cs u0 {1,S} {6,S} {7,S} {8,S}
3     CO u0 {1,S} {9,D} {10,S}
4  *2 H  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {2,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     O  u0 {3,D}
10    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 417,
    label = "C/H2/CdCs",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
6    Cd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 418,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3",
    group =
"""
1  *1 C  u0 {2,S} {3,S} {5,S} {6,S}
2     Cs u0 {1,S} {7,S} {8,S} {9,S}
3     Cd u0 {1,S} {4,D} {10,S}
4     Cd u0 {3,D} {11,S} {12,S}
5  *2 H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {4,S}
12    H  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 419,
    label = "C/H2/CSCs",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 420,
    label = "C/H2/OneDeO",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 421,
    label = "C/H2/OneDeS",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 422,
    label = "C/H2/CbS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 423,
    label = "C/H2/CtS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 424,
    label = "C/H2/CdS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    S  u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 425,
    label = "C/H2/CSS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    S  u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 426,
    label = "C/H2/TwoDe",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cd,Ct,CO,CS,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 427,
    label = "C/H2/CtCt",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 428,
    label = "C/H2/CtCb",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 429,
    label = "C/H2/CtCO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 430,
    label = "C/H2/CbCb",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 431,
    label = "C/H2/CbCO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 432,
    label = "C/H2/COCO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
5    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 433,
    label = "C/H2/CdCt",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 434,
    label = "C/H2/CtCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 435,
    label = "C/H2/CdCb",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 436,
    label = "C/H2/CbCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 437,
    label = "C/H2/CdCO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 438,
    label = "C/H2/COCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 439,
    label = "C/H2/CdCd",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    Cd u0 {1,S} {7,D}
4 *2 H  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,D}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 440,
    label = "C/H2/CdCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 H  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 441,
    label = "C/H2/CSCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 H  u0 {1,S}
5    H  u0 {1,S}
6    S  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 442,
    label = "C_sec-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    R!H!Val7 u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 443,
    label = "C/H2/NonDeC-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 444,
    label = "C/H2/NonDeC_5ring_fused6_1-F",
    group =
"""
1 *1 C   u0 {2,S} {4,S} {8,S} {9,S}
2    Cs  u0 {1,S} {5,S} {6,S}
3    Cs  u0 {4,S} {5,S} {7,S}
4    Cs  u0 {1,S} {3,S}
5    Cs  u0 {2,S} {3,S}
6    Cs  u0 {2,S} {7,S}
7    Cs  u0 {3,S} {6,S}
8 *2 H   u0 {1,S}
9    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 445,
    label = "C/H2/NonDeC_5ring_fused6_2-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {8,S} {9,S}
2    Cs  u0 {1,S} {4,S} {6,S}
3    Cs  u0 {1,S} {5,S} {7,S}
4    Cs  u0 {2,S} {5,S}
5    Cs  u0 {3,S} {4,S}
6    Cs  u0 {2,S} {7,S}
7    Cs  u0 {3,S} {6,S}
8 *2 H   u0 {1,S}
9    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 446,
    label = "C/H2/NonDeC_5ring_alpha6ring-F",
    group =
"""
1  *1 C   u0 {2,S} {4,S} {10,S} {11,S}
2     Cs  u0 {1,S} {3,S} {6,S}
3     Cs  u0 {2,S} {5,S} {7,S}
4     Cs  u0 {1,S} {5,S}
5     Cs  u0 {3,S} {4,S}
6     C   u0 {2,S} {8,S}
7     C   u0 {3,S} {9,S}
8     C   u0 {6,S} {9,S}
9     C   u0 {7,S} {8,S}
10 *2 H   u0 {1,S}
11    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 447,
    label = "C/H2/NonDeC_5ring_beta6ring-F",
    group =
"""
1  *1 C   u0 {4,S} {5,S} {10,S} {11,S}
2     Cs  u0 {3,S} {4,S} {6,S}
3     Cs  u0 {2,S} {5,S} {7,S}
4     Cs  u0 {1,S} {2,S}
5     Cs  u0 {1,S} {3,S}
6     C   u0 {2,S} {8,S}
7     C   u0 {3,S} {9,S}
8     C   u0 {6,S} {9,S}
9     C   u0 {7,S} {8,S}
10 *2 H   u0 {1,S}
11    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 448,
    label = "C/H2/NonDeO-F",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    F1s      u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 449,
    label = "C/H2/CsO-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    O   u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 450,
    label = "C/H2/O2-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    O   u0 {1,S}
5    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 451,
    label = "C/H2/NonDeS-F",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    F1s      u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 452,
    label = "C/H2/CsS-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    S   u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 453,
    label = "C/H2/NonDeN-F",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H          u0 {1,S}
3    F1s        u0 {1,S}
4    N          u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 454,
    label = "C/H2/OneDe-F",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    F1s              u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 455,
    label = "C/H2/OneDeC-F",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    F1s              u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 456,
    label = "C/H2/CtCs-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    Ct  u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 457,
    label = "C/H2/CbCs-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    Cb  u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 458,
    label = "C/H2/COCs-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    CO  u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 459,
    label = "C/H2/CdCs-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {1,S}
6    Cd  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 460,
    label = "C/H2/CSCs-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    CS  u0 {1,S} {6,D}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {1,S}
6    S   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 461,
    label = "C/H2/OneDeO-F",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    F1s              u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 462,
    label = "C/H2/OneDeS-F",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    F1s              u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 463,
    label = "C/H2/CbS-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    Cb  u0 {1,S}
5    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 464,
    label = "C/H2/CtS-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    Ct  u0 {1,S}
5    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 465,
    label = "C/H2/CdS-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
5    S   u0 {1,S}
6    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 466,
    label = "C/H2/CSS-F",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    CS  u0 {1,S} {6,D}
3 *2 H   u0 {1,S}
4    F1s u0 {1,S}
5    S   u0 {1,S}
6    S   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 467,
    label = "C/H2/TwoDe-F",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    F1s              u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cd,Ct,CO,CS,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 468,
    label = "C_sec-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
5    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 469,
    label = "C/H2/NonDeC-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 470,
    label = "C/H2/NonDeC_5ring_fused6_1-Cl",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {8,S} {9,S}
2    Cs   u0 {1,S} {5,S} {6,S}
3    Cs   u0 {4,S} {5,S} {7,S}
4    Cs   u0 {1,S} {3,S}
5    Cs   u0 {2,S} {3,S}
6    Cs   u0 {2,S} {7,S}
7    Cs   u0 {3,S} {6,S}
8 *2 H    u0 {1,S}
9    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 471,
    label = "C/H2/NonDeC_5ring_fused6_2-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {8,S} {9,S}
2    Cs   u0 {1,S} {4,S} {6,S}
3    Cs   u0 {1,S} {5,S} {7,S}
4    Cs   u0 {2,S} {5,S}
5    Cs   u0 {3,S} {4,S}
6    Cs   u0 {2,S} {7,S}
7    Cs   u0 {3,S} {6,S}
8 *2 H    u0 {1,S}
9    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 472,
    label = "C/H2/NonDeC_5ring_alpha6ring-Cl",
    group =
"""
1  *1 C    u0 {2,S} {4,S} {10,S} {11,S}
2     Cs   u0 {1,S} {3,S} {6,S}
3     Cs   u0 {2,S} {5,S} {7,S}
4     Cs   u0 {1,S} {5,S}
5     Cs   u0 {3,S} {4,S}
6     C    u0 {2,S} {8,S}
7     C    u0 {3,S} {9,S}
8     C    u0 {6,S} {9,S}
9     C    u0 {7,S} {8,S}
10 *2 H    u0 {1,S}
11    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 473,
    label = "C/H2/NonDeC_5ring_beta6ring-Cl",
    group =
"""
1  *1 C    u0 {4,S} {5,S} {10,S} {11,S}
2     Cs   u0 {3,S} {4,S} {6,S}
3     Cs   u0 {2,S} {5,S} {7,S}
4     Cs   u0 {1,S} {2,S}
5     Cs   u0 {1,S} {3,S}
6     C    u0 {2,S} {8,S}
7     C    u0 {3,S} {9,S}
8     C    u0 {6,S} {9,S}
9     C    u0 {7,S} {8,S}
10 *2 H    u0 {1,S}
11    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 474,
    label = "C/H2/NonDeO-Cl",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    Cl1s     u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 475,
    label = "C/H2/CsO-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    O    u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 476,
    label = "C/H2/O2-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    O    u0 {1,S}
5    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 477,
    label = "C/H2/NonDeS-Cl",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    Cl1s     u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 478,
    label = "C/H2/CsS-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    S    u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 479,
    label = "C/H2/NonDeN-Cl",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H          u0 {1,S}
3    Cl1s       u0 {1,S}
4    N          u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 480,
    label = "C/H2/OneDe-Cl",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Cl1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 481,
    label = "C/H2/OneDeC-Cl",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Cl1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 482,
    label = "C/H2/CtCs-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 483,
    label = "C/H2/CbCs-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cb   u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 484,
    label = "C/H2/COCs-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    CO   u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 485,
    label = "C/H2/CO\H/Cs\H3-ClClClClCl",
    group =
"""
1  *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2     Cs   u0 {1,S} {6,S} {7,S} {8,S}
3     CO   u0 {1,S} {9,D} {10,S}
4  *2 H    u0 {1,S}
5     Cl1s u0 {1,S}
6     Cl1s u0 {2,S}
7     Cl1s u0 {2,S}
8     Cl1s u0 {2,S}
9     O    u0 {3,D}
10    Cl1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 486,
    label = "C/H2/CO\H/Cs\H3-ClClClClBr",
    group =
"""
1  *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2     Cs   u0 {1,S} {6,S} {7,S} {8,S}
3     CO   u0 {1,S} {9,D} {10,S}
4  *2 H    u0 {1,S}
5     Cl1s u0 {1,S}
6     Cl1s u0 {2,S}
7     Cl1s u0 {2,S}
8     Cl1s u0 {2,S}
9     O    u0 {3,D}
10    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 487,
    label = "C/H2/CO\H/Cs\H3-ClClClBrBr",
    group =
"""
1  *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2     Cs   u0 {1,S} {6,S} {7,S} {8,S}
3     CO   u0 {1,S} {9,D} {10,S}
4  *2 H    u0 {1,S}
5     Cl1s u0 {1,S}
6     Cl1s u0 {2,S}
7     Cl1s u0 {2,S}
8     Br1s u0 {2,S}
9     O    u0 {3,D}
10    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 488,
    label = "C/H2/CO\H/Cs\H3-ClClBrBrBr",
    group =
"""
1  *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2     Cs   u0 {1,S} {6,S} {7,S} {8,S}
3     CO   u0 {1,S} {9,D} {10,S}
4  *2 H    u0 {1,S}
5     Cl1s u0 {1,S}
6     Cl1s u0 {2,S}
7     Br1s u0 {2,S}
8     Br1s u0 {2,S}
9     O    u0 {3,D}
10    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 489,
    label = "C/H2/CO\H/Cs\H3-ClBrBrBrBr",
    group =
"""
1  *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2     Cs   u0 {1,S} {6,S} {7,S} {8,S}
3     CO   u0 {1,S} {9,D} {10,S}
4  *2 H    u0 {1,S}
5     Cl1s u0 {1,S}
6     Br1s u0 {2,S}
7     Br1s u0 {2,S}
8     Br1s u0 {2,S}
9     O    u0 {3,D}
10    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 490,
    label = "C/H2/CdCs-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {1,S}
6    Cd   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 491,
    label = "C/H2/CSCs-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    CS   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {1,S}
6    S    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 492,
    label = "C/H2/OneDeO-Cl",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Cl1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 493,
    label = "C/H2/OneDeS-Cl",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Cl1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 494,
    label = "C/H2/CbS-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cb   u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 495,
    label = "C/H2/CtS-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 496,
    label = "C/H2/CdS-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    S    u0 {1,S}
6    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 497,
    label = "C/H2/CSS-Cl",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    CS   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Cl1s u0 {1,S}
5    S    u0 {1,S}
6    S    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 498,
    label = "C/H2/TwoDe-Cl",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Cl1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cd,Ct,CO,CS,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 499,
    label = "C_sec-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
5    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 500,
    label = "C/H2/NonDeC-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 501,
    label = "C/H2/Cs/Cs\O-Br",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2    Cs    u0 {1,S} {6,S}
3 *2 H     u0 {1,S}
4    Br1s  u0 {1,S}
5    Cs    u0 {1,S}
6    [O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 502,
    label = "C/H2/Cs/Cs\Cs|O-Br",
    group =
"""
1 *1 C     u0 {2,S} {4,S} {5,S} {6,S}
2    Cs    u0 {1,S} {3,S}
3    Cs    u0 {2,S} {7,S}
4 *2 H     u0 {1,S}
5    Br1s  u0 {1,S}
6    Cs    u0 {1,S}
7    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 503,
    label = "C/H2/NonDeC_5ring-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {6,S} {7,S}
2    Cs   u0 {1,S} {4,S}
3    Cs   u0 {1,S} {5,S}
4    Cs   u0 {2,S} {5,S}
5    Cs   u0 {3,S} {4,S}
6 *2 H    u0 {1,S}
7    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 504,
    label = "C/H2/NonDeC_5ring_fused6_1-Br",
    group =
"""
1 *1 C    u0 {2,S} {4,S} {8,S} {9,S}
2    Cs   u0 {1,S} {5,S} {6,S}
3    Cs   u0 {4,S} {5,S} {7,S}
4    Cs   u0 {1,S} {3,S}
5    Cs   u0 {2,S} {3,S}
6    Cs   u0 {2,S} {7,S}
7    Cs   u0 {3,S} {6,S}
8 *2 H    u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 505,
    label = "C/H2/NonDeC_5ring_fused6_2-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {8,S} {9,S}
2    Cs   u0 {1,S} {4,S} {6,S}
3    Cs   u0 {1,S} {5,S} {7,S}
4    Cs   u0 {2,S} {5,S}
5    Cs   u0 {3,S} {4,S}
6    Cs   u0 {2,S} {7,S}
7    Cs   u0 {3,S} {6,S}
8 *2 H    u0 {1,S}
9    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 506,
    label = "C/H2/NonDeC_5ring_alpha6ring-Br",
    group =
"""
1  *1 C    u0 {2,S} {4,S} {10,S} {11,S}
2     Cs   u0 {1,S} {3,S} {6,S}
3     Cs   u0 {2,S} {5,S} {7,S}
4     Cs   u0 {1,S} {5,S}
5     Cs   u0 {3,S} {4,S}
6     C    u0 {2,S} {8,S}
7     C    u0 {3,S} {9,S}
8     C    u0 {6,S} {9,S}
9     C    u0 {7,S} {8,S}
10 *2 H    u0 {1,S}
11    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 507,
    label = "C/H2/NonDeC_5ring_beta6ring-Br",
    group =
"""
1  *1 C    u0 {4,S} {5,S} {10,S} {11,S}
2     Cs   u0 {3,S} {4,S} {6,S}
3     Cs   u0 {2,S} {5,S} {7,S}
4     Cs   u0 {1,S} {2,S}
5     Cs   u0 {1,S} {3,S}
6     C    u0 {2,S} {8,S}
7     C    u0 {3,S} {9,S}
8     C    u0 {6,S} {9,S}
9     C    u0 {7,S} {8,S}
10 *2 H    u0 {1,S}
11    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 508,
    label = "C/H2/Cs\H3/Cs\H3-BrBrBrBrBrBrBr",
    group =
"""
1  *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2     Cs   u0 {1,S} {6,S} {7,S} {8,S}
3     Cs   u0 {1,S} {9,S} {10,S} {11,S}
4  *2 H    u0 {1,S}
5     Br1s u0 {1,S}
6     Br1s u0 {2,S}
7     Br1s u0 {2,S}
8     Br1s u0 {2,S}
9     Br1s u0 {3,S}
10    Br1s u0 {3,S}
11    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 509,
    label = "C/H2/NonDeO-Br",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    Br1s     u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 510,
    label = "C/H2/CsO-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 511,
    label = "C/H2/Cs\Cs2/O-HBrBrBrBrBrBrBrBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C    u0 {1,S} {5,S} {7,S} {8,S}
3     C    u0 {1,S} {9,S} {10,S} {11,S}
4     C    u0 {1,S} {12,S} {13,S} {14,S}
5     O    u0 {2,S} {15,S}
6     H    u0 {1,S}
7  *2 H    u0 {2,S}
8     Br1s u0 {2,S}
9     Br1s u0 {3,S}
10    Br1s u0 {3,S}
11    Br1s u0 {3,S}
12    Br1s u0 {4,S}
13    Br1s u0 {4,S}
14    Br1s u0 {4,S}
15    Br1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 512,
    label = "C/H2/Cs\Cs2/O-FBrBrBrBrBrBrBrBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C    u0 {1,S} {5,S} {7,S} {8,S}
3     C    u0 {1,S} {9,S} {10,S} {11,S}
4     C    u0 {1,S} {12,S} {13,S} {14,S}
5     O    u0 {2,S} {15,S}
6     F1s  u0 {1,S}
7  *2 H    u0 {2,S}
8     Br1s u0 {2,S}
9     Br1s u0 {3,S}
10    Br1s u0 {3,S}
11    Br1s u0 {3,S}
12    Br1s u0 {4,S}
13    Br1s u0 {4,S}
14    Br1s u0 {4,S}
15    Br1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 513,
    label = "C/H2/Cs\Cs2/O-ClBrBrBrBrBrBrBrBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C    u0 {1,S} {5,S} {7,S} {8,S}
3     C    u0 {1,S} {9,S} {10,S} {11,S}
4     C    u0 {1,S} {12,S} {13,S} {14,S}
5     O    u0 {2,S} {15,S}
6     Cl1s u0 {1,S}
7  *2 H    u0 {2,S}
8     Br1s u0 {2,S}
9     Br1s u0 {3,S}
10    Br1s u0 {3,S}
11    Br1s u0 {3,S}
12    Br1s u0 {4,S}
13    Br1s u0 {4,S}
14    Br1s u0 {4,S}
15    Br1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 514,
    label = "C/H2/Cs\Cs2/O-BrBrBrBrBrBrBrBrBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {4,S} {6,S}
2  *1 C    u0 {1,S} {5,S} {7,S} {8,S}
3     C    u0 {1,S} {9,S} {10,S} {11,S}
4     C    u0 {1,S} {12,S} {13,S} {14,S}
5     O    u0 {2,S} {15,S}
6     Br1s u0 {1,S}
7  *2 H    u0 {2,S}
8     Br1s u0 {2,S}
9     Br1s u0 {3,S}
10    Br1s u0 {3,S}
11    Br1s u0 {3,S}
12    Br1s u0 {4,S}
13    Br1s u0 {4,S}
14    Br1s u0 {4,S}
15    Br1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 515,
    label = "C/H2/O2-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
5    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 516,
    label = "C/H2/NonDeS-Br",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    Br1s     u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 517,
    label = "C/H2/CsS-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 518,
    label = "C/H2/NonDeN-Br",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H          u0 {1,S}
3    Br1s       u0 {1,S}
4    N          u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 519,
    label = "C/H2/OneDe-Br",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Br1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 520,
    label = "C/H2/OneDeC-Br",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Br1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 521,
    label = "C/H2/CtCs-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 522,
    label = "C/H2/CbCs-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 523,
    label = "C/H2/COCs-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
5    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 524,
    label = "C/H2/CO\H/Cs\H3-BrBrBrBrBr",
    group =
"""
1  *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2     Cs   u0 {1,S} {6,S} {7,S} {8,S}
3     CO   u0 {1,S} {9,D} {10,S}
4  *2 H    u0 {1,S}
5     Br1s u0 {1,S}
6     Br1s u0 {2,S}
7     Br1s u0 {2,S}
8     Br1s u0 {2,S}
9     O    u0 {3,D}
10    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 525,
    label = "C/H2/CdCs-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {1,S}
6    Cd   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 526,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3-BrBrBrBrBrBrBr",
    group =
"""
1  *1 C    u0 {2,S} {3,S} {5,S} {6,S}
2     Cs   u0 {1,S} {7,S} {8,S} {9,S}
3     Cd   u0 {1,S} {4,D} {10,S}
4     Cd   u0 {3,D} {11,S} {12,S}
5  *2 H    u0 {1,S}
6     Br1s u0 {1,S}
7     Br1s u0 {2,S}
8     Br1s u0 {2,S}
9     Br1s u0 {2,S}
10    Br1s u0 {3,S}
11    Br1s u0 {4,S}
12    Br1s u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 527,
    label = "C/H2/CSCs-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    CS   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {1,S}
6    S    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 528,
    label = "C/H2/OneDeO-Br",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Br1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 529,
    label = "C/H2/OneDeS-Br",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Br1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 530,
    label = "C/H2/CbS-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 531,
    label = "C/H2/CtS-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
5    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 532,
    label = "C/H2/CdS-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    Cd   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
5    S    u0 {1,S}
6    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 533,
    label = "C/H2/CSS-Br",
    group =
"""
1 *1 C    u0 {2,S} {3,S} {4,S} {5,S}
2    CS   u0 {1,S} {6,D}
3 *2 H    u0 {1,S}
4    Br1s u0 {1,S}
5    S    u0 {1,S}
6    S    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 534,
    label = "C/H2/TwoDe-Br",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    Br1s             u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cd,Ct,CO,CS,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 535,
    label = "C_ter",
    group =
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    R!H!Val7 u0 {1,S}
4    R!H!Val7 u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 536,
    label = "C/H/NonDe",
    group =
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H          u0 {1,S}
3    [Cs,O,S,N] u0 {1,S}
4    [Cs,O,S,N] u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 537,
    label = "C/H/Cs3",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 538,
    label = "C/H_or_Val7/Cs2/Cs\O",
    group =
"""
1  *1 C        u0 {2,S} {3,S} {4,S} {6,S}
2     Cs       u0 {1,S} {5,S} {7,S} {8,S}
3     Cs       u0 {1,S} {9,S} {10,S} {11,S}
4     Cs       u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S]    u0 {2,S} {15,S}
6  *2 H        u0 {1,S}
7     [H,Val7] u0 {2,S}
8     [H,Val7] u0 {2,S}
9     [H,Val7] u0 {3,S}
10    [H,Val7] u0 {3,S}
11    [H,Val7] u0 {3,S}
12    [H,Val7] u0 {4,S}
13    [H,Val7] u0 {4,S}
14    [H,Val7] u0 {4,S}
15    [H,Val7] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 539,
    label = "C/H/Cs2/Cs\O",
    group =
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {12,S} {13,S} {14,S}
5     [O,S] u0 {2,S} {15,S}
6  *2 H     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {4,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    H     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 540,
    label = "C/H_or_Val7/Cs2/Cs\Cs|O",
    group =
"""
1  *1 Cs       u0 {2,S} {3,S} {4,S} {6,S}
2     Cs       u0 {1,S} {5,S} {7,S} {8,S}
3     Cs       u0 {1,S} {9,S} {10,S} {11,S}
4     Cs       u0 {1,S} {13,S} {14,S} {15,S}
5     Cs       u0 {2,S} {12,S} {16,S} {17,S}
6  *2 H        u0 {1,S}
7     [H,Val7] u0 {2,S}
8     [H,Val7] u0 {2,S}
9     [H,Val7] u0 {3,S}
10    [H,Val7] u0 {3,S}
11    [H,Val7] u0 {3,S}
12    [H,Val7] u0 {5,S}
13    [H,Val7] u0 {4,S}
14    [H,Val7] u0 {4,S}
15    [H,Val7] u0 {4,S}
16    [H,Val7] u0 {5,S}
17    [O,S]    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 541,
    label = "C/H/Cs2/Cs\Cs|O",
    group =
"""
1  *1 Cs    u0 {2,S} {3,S} {4,S} {6,S}
2     Cs    u0 {1,S} {5,S} {7,S} {8,S}
3     Cs    u0 {1,S} {9,S} {10,S} {11,S}
4     Cs    u0 {1,S} {13,S} {14,S} {15,S}
5     Cs    u0 {2,S} {12,S} {16,S} {17,S}
6  *2 H     u0 {1,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {5,S}
13    H     u0 {4,S}
14    H     u0 {4,S}
15    H     u0 {4,S}
16    H     u0 {5,S}
17    [O,S] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 542,
    label = "C/H/Cs3_5ring",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {6,S} {7,S}
2    Cs u0 {1,S} {4,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6 *2 H  u0 {1,S}
7    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 543,
    label = "C/H/Cs3_5ring_fused6",
    group =
"""
1 *1 C  u0 {3,S} {4,S} {5,S} {8,S}
2    Cs u0 {3,S} {6,S} {7,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {1,S} {6,S}
5    Cs u0 {1,S} {7,S}
6    Cs u0 {2,S} {4,S}
7    Cs u0 {2,S} {5,S}
8 *2 H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 544,
    label = "C/H/Cs3_5ring_adj5",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {9,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {1,S} {7,S}
4    Cs u0 {1,S} {8,S}
5    Cs u0 {2,S} {7,S}
6    Cs u0 {2,S} {8,S}
7    Cs u0 {3,S} {5,S}
8    Cs u0 {4,S} {6,S}
9 *2 H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 545,
    label = "C/H/Cs2N",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    N  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 546,
    label = "C/H/NDMustO",
    group =
"""
1 *1 C      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
5    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 547,
    label = "C/H/Cs2O",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 548,
    label = "C/H/CsO2",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 549,
    label = "C/H/O3",
    group =
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    O u0 {1,S}
4    O u0 {1,S}
5    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 550,
    label = "C/H/NDMustS",
    group =
"""
1 *1 C      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      u0 {1,S}
3    S      u0 {1,S}
4    [Cs,S] u0 {1,S}
5    [Cs,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 551,
    label = "C/H/Cs2S",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 552,
    label = "C/H/CsS2",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    S  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 553,
    label = "C/H/S3",
    group =
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    S u0 {1,S}
4    S u0 {1,S}
5    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 554,
    label = "C/H/NDMustOS",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    O        u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 555,
    label = "C/H/CsOS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 556,
    label = "C/H/OneDe",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 557,
    label = "C/H/Cs2",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 558,
    label = "C/H/Cs2Ct",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 559,
    label = "C/H/Cs2Cb",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 560,
    label = "C/H/Cs2CO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 561,
    label = "C/H/Cs2Cd",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 562,
    label = "C/H/Cs2CS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 563,
    label = "C/H/CsO",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 564,
    label = "C/H/CsS",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 565,
    label = "C/H/CbCsS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 566,
    label = "C/H/CtCsS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 567,
    label = "C/H/CdCsS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 568,
    label = "C/H/CSCsS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 569,
    label = "C/H/OO",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 570,
    label = "C/H/OS",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 571,
    label = "C/H/SS",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 572,
    label = "C/H/TwoDe",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 573,
    label = "C/H/Cs",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 574,
    label = "C/H/CtCt",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 575,
    label = "C/H/CtCb",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 576,
    label = "C/H/CtCO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 577,
    label = "C/H/CbCb",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 578,
    label = "C/H/CbCO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 579,
    label = "C/H/COCO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    CO u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 580,
    label = "C/H/CdCt",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 581,
    label = "C/H/CtCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 582,
    label = "C/H/CdCb",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 583,
    label = "C/H/CbCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    CS u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 584,
    label = "C/H/CdCO",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 585,
    label = "C/H/COCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3 *2 H  u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 586,
    label = "C/H/CdCd",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    Cd u0 {1,S} {7,D}
4 *2 H  u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
7    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 587,
    label = "C/H/CdCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 H  u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 588,
    label = "C/H/CSCS",
    group =
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    CS u0 {1,S} {6,D}
3    CS u0 {1,S} {7,D}
4 *2 H  u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {2,D}
7    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 589,
    label = "C/H/TDMustO",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 590,
    label = "C/H/TDMustS",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 591,
    label = "C/H/ThreeDe",
    group =
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 592,
    label = "N3_H",
    group =
"""
1 *1 [N3s,N3d] u0 {2,S}
2 *2 H         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 593,
    label = "N3s_H",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 594,
    label = "N/H_or_Val7/3",
    group =
"""
1 *1 N3s      u0 {2,S} {3,S} {4,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 595,
    label = "NH3",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 596,
    label = "NH3-HF",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 597,
    label = "NH3-HCl",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 598,
    label = "NH3-HBr",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 599,
    label = "NH3-FF",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 600,
    label = "NH3-FCl",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 601,
    label = "NH3-FBr",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 602,
    label = "NH3-ClCl",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 603,
    label = "NH3-ClBr",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 604,
    label = "NH3-BrBr",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 605,
    label = "N3s_pri_/H_or_Val7/",
    group =
"""
1 *1 N3s      u0 {2,S} {3,S} {4,S}
2 *2 H        u0 {1,S}
3    [H,Val7] u0 {1,S}
4    R!H!Val7      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 606,
    label = "N3s_pri_H",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 607,
    label = "N3s/H2/NonDe",
    group =
"""
1 *1 N3s          u0 {2,S} {3,S} {4,S}
2 *2 H            u0 {1,S}
3    H            u0 {1,S}
4    [N3s,Cs,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 608,
    label = "N3s/H2/NonDeC",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 609,
    label = "N3s/H2/NonDeO",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 610,
    label = "N3s/H2/NonDeN",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 611,
    label = "N3s/H2/OneDe",
    group =
"""
1 *1 N3s                        u0 {2,S} {3,S} {4,S}
2 *2 H                          u0 {1,S}
3    H                          u0 {1,S}
4    [Cd,Cdd,Ct,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 612,
    label = "N3s/H2/OneDeN",
    group =
"""
1 *1 N3s        u0 {2,S} {3,S} {4,S}
2 *2 H          u0 {1,S}
3    H          u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 613,
    label = "N3s_pri_H-F",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 614,
    label = "N3s/H2/NonDe-F",
    group =
"""
1 *1 N3s          u0 {2,S} {3,S} {4,S}
2 *2 H            u0 {1,S}
3    F1s          u0 {1,S}
4    [N3s,Cs,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 615,
    label = "N3s/H2/NonDeC-F",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 616,
    label = "N3s/H2/NonDeO-F",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 617,
    label = "N3s/H2/NonDeN-F",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    F1s u0 {1,S}
4    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 618,
    label = "N3s/H2/OneDe-F",
    group =
"""
1 *1 N3s                        u0 {2,S} {3,S} {4,S}
2 *2 H                          u0 {1,S}
3    F1s                        u0 {1,S}
4    [Cd,Cdd,Ct,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 619,
    label = "N3s/H2/OneDeN-F",
    group =
"""
1 *1 N3s        u0 {2,S} {3,S} {4,S}
2 *2 H          u0 {1,S}
3    F1s        u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 620,
    label = "N3s_pri_H-Cl",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 621,
    label = "N3s/H2/NonDe-Cl",
    group =
"""
1 *1 N3s          u0 {2,S} {3,S} {4,S}
2 *2 H            u0 {1,S}
3    Cl1s         u0 {1,S}
4    [N3s,Cs,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 622,
    label = "N3s/H2/NonDeC-Cl",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 623,
    label = "N3s/H2/NonDeO-Cl",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 624,
    label = "N3s/H2/NonDeN-Cl",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Cl1s u0 {1,S}
4    N3s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 625,
    label = "N3s/H2/OneDe-Cl",
    group =
"""
1 *1 N3s                        u0 {2,S} {3,S} {4,S}
2 *2 H                          u0 {1,S}
3    Cl1s                       u0 {1,S}
4    [Cd,Cdd,Ct,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 626,
    label = "N3s/H2/OneDeN-Cl",
    group =
"""
1 *1 N3s        u0 {2,S} {3,S} {4,S}
2 *2 H          u0 {1,S}
3    Cl1s       u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 627,
    label = "N3s_pri_H-Br",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 628,
    label = "N3s/H2/NonDe-Br",
    group =
"""
1 *1 N3s          u0 {2,S} {3,S} {4,S}
2 *2 H            u0 {1,S}
3    Br1s         u0 {1,S}
4    [N3s,Cs,O2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 629,
    label = "N3s/H2/NonDeC-Br",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 630,
    label = "N3s/H2/NonDeO-Br",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 631,
    label = "N3s/H2/NonDeN-Br",
    group =
"""
1 *1 N3s  u0 {2,S} {3,S} {4,S}
2 *2 H    u0 {1,S}
3    Br1s u0 {1,S}
4    N3s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 632,
    label = "N3s/H2/OneDe-Br",
    group =
"""
1 *1 N3s                        u0 {2,S} {3,S} {4,S}
2 *2 H                          u0 {1,S}
3    Br1s                       u0 {1,S}
4    [Cd,Cdd,Ct,CO,CS,N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 633,
    label = "N3s/H2/OneDeN-Br",
    group =
"""
1 *1 N3s        u0 {2,S} {3,S} {4,S}
2 *2 H          u0 {1,S}
3    Br1s       u0 {1,S}
4    [N3d,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 634,
    label = "N3s_sec_H",
    group =
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    R!H!Val7 u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 635,
    label = "N3d_H",
    group =
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    R!H!Val7 u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 636,
    label = "N3d/H/NonDe",
    group =
"""
1 *1 N3d          u0 {2,S} {3,D}
2 *2 H            u0 {1,S}
3    [N3d,O2d,Cd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 637,
    label = "N3d/H/NonDeC",
    group =
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2 *1 N3d u0 {1,D} {5,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
5 *2 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 638,
    label = "N3d/H/NonDeO",
    group =
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 639,
    label = "N3d/H/NonDeN",
    group =
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 640,
    label = "N3d/H/OneDe",
    group =
"""
1 *1 N3d u0 {2,D} {3,S}
2    Cdd u0 {1,D} {4,D}
3 *2 H   u0 {1,S}
4    R!H!Val7 u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 641,
    label = "N3d/H/CddO",
    group =
"""
1 *1 N3d u0 {2,D} {3,S}
2    Cdd u0 {1,D} {4,D}
3 *2 H   u0 {1,S}
4    O2d u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 642,
    label = "N5_H",
    group =
"""
1 *1 [N5sc,N5dc,N5ddc,N5tc,N5b] u0 p0 c+1 {2,S}
2 *2 H                          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 643,
    label = "N5dc_H",
    group =
"""
1 *1 N5dc u0 p0 c+1 {2,S}
2 *2 H    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 644,
    label = "N5dc/H/NonDeOO",
    group =
"""
1 *1 N5dc u0 p0 c+1 {2,S} {3,S} {4,D}
2 *2 H    u0 {1,S}
3    O2s  u0 {1,S}
4    O2d  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 645,
    label = "HCl",
    group =
"""
1 *1 Cl1s u0 {2,S}
2 *2 H    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 646,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet}",
    kinetics = None,
)

entry(
    index = 647,
    label = "C_quintet",
    group =
"""
1 *3 C u4 p0
""",
    kinetics = None,
)

entry(
    index = 648,
    label = "C_triplet",
    group =
"""
1 *3 C u2 p1
""",
    kinetics = None,
)

entry(
    index = 649,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, C/H_or_Val7/quartet, C/H_or_Val7/doublet}",
    kinetics = None,
)

entry(
    index = 650,
    label = "N_atom_quartet",
    group =
"""
1 *3 N u3 p1
""",
    kinetics = None,
)

entry(
    index = 651,
    label = "N_atom_doublet",
    group =
"""
1 *3 N u1 p2
""",
    kinetics = None,
)

entry(
    index = 652,
    label = "C/H_or_Val7/quartet",
    group =
"""
1 *3 C        u3 p0 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 653,
    label = "CH_quartet",
    group =
"""
1 *3 C u3 p0 {2,S}
2    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 654,
    label = "CH_quartet-F",
    group =
"""
1 *3 C   u3 p0 {2,S}
2    F1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 655,
    label = "CH_quartet-Cl",
    group =
"""
1 *3 C    u3 p0 {2,S}
2    Cl1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 656,
    label = "CH_quartet-Br",
    group =
"""
1 *3 C    u3 p0 {2,S}
2    Br1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 657,
    label = "C/H_or_Val7/doublet",
    group =
"""
1 *3 C        u1 p1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 658,
    label = "CH_doublet",
    group =
"""
1 *3 C u1 p1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 659,
    label = "CH_doublet-F",
    group =
"""
1 *3 C   u1 p1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 660,
    label = "CH_doublet-Cl",
    group =
"""
1 *3 C    u1 p1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 661,
    label = "CH_doublet-Br",
    group =
"""
1 *3 C    u1 p1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 662,
    label = "Y_1centerbirad",
    group =
"""
1 *3 [Cs,Cd,CO,CS,O,S,N] u2
""",
    kinetics = None,
)

entry(
    index = 663,
    label = "O_atom_triplet",
    group =
"""
1 *3 O u2
""",
    kinetics = None,
)

entry(
    index = 664,
    label = "S_atom_triplet",
    group =
"""
1 *3 S u2
""",
    kinetics = None,
)

entry(
    index = 665,
    label = "C/H_or_Val7/2_triplet",
    group =
"""
1 *3 Cs       u2 {2,S} {3,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 666,
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
    index = 667,
    label = "CH2_triplet-HF",
    group =
"""
1 *3 Cs  u2 {2,S} {3,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 668,
    label = "CH2_triplet-HCl",
    group =
"""
1 *3 Cs   u2 {2,S} {3,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 669,
    label = "CH2_triplet-HBr",
    group =
"""
1 *3 Cs   u2 {2,S} {3,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 670,
    label = "CH2_triplet-FF",
    group =
"""
1 *3 Cs  u2 {2,S} {3,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 671,
    label = "CH2_triplet-FCl",
    group =
"""
1 *3 Cs   u2 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 672,
    label = "CH2_triplet-FBr",
    group =
"""
1 *3 Cs   u2 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 673,
    label = "CH2_triplet-ClCl",
    group =
"""
1 *3 Cs   u2 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 674,
    label = "CH2_triplet-ClBr",
    group =
"""
1 *3 Cs   u2 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 675,
    label = "CH2_triplet-BrBr",
    group =
"""
1 *3 Cs   u2 {2,S} {3,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 676,
    label = "N/H_or_Val7/_triplet",
    group =
"""
1 *3 N3s      u2 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 677,
    label = "NH_triplet",
    group =
"""
1 *3 N3s u2 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 678,
    label = "NH_triplet-F",
    group =
"""
1 *3 N3s u2 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 679,
    label = "NH_triplet-Cl",
    group =
"""
1 *3 N3s  u2 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 680,
    label = "NH_triplet-Br",
    group =
"""
1 *3 N3s  u2 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 681,
    label = "Y_rad",
    group =
"""
1 *3 R u1
""",
    kinetics = None,
)

entry(
    index = 682,
    label = "H_rad",
    group =
"""
1 *3 H u1
""",
    kinetics = None,
)

entry(
    index = 683,
    label = "Y_2centeradjbirad",
    group =
"""
1 *3 [Ct,O2s,S2s] u1 {2,[S,T]}
2    [Ct,O2s,S2s] u1 {1,[S,T]}
""",
    kinetics = None,
)

entry(
    index = 684,
    label = "O2b",
    group =
"""
1 *3 O2s u1 {2,S}
2    O2s u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 685,
    label = "S2b",
    group =
"""
1 *3 S2s u1 p2 {2,S}
2    S2s u1 p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 686,
    label = "C2b",
    group =
"""
1 *3 Ct u1 {2,T}
2    Ct u1 {1,T}
""",
    kinetics = None,
)

entry(
    index = 687,
    label = "Ct_rad",
    group =
"""
1 *3 C     u1 {2,T}
2    [C,N] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 688,
    label = "Ct_rad/Ct",
    group =
"""
1 *3 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 689,
    label = "Ct_rad/N",
    group =
"""
1 *3 Ct         u1 {2,T}
2    [N3t,N5tc] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 690,
    label = "O_rad",
    group =
"""
1 *3 O u1 {2,S}
2    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 691,
    label = "O_pri_rad-H_or_Val7-1",
    group =
"""
1 *3 O        u1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 692,
    label = "O_pri_rad",
    group =
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 693,
    label = "O_pri_rad-F",
    group =
"""
1 *3 O   u1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 694,
    label = "O_pri_rad-Cl",
    group =
"""
1 *3 O    u1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 695,
    label = "O_pri_rad-Br",
    group =
"""
1 *3 O    u1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 696,
    label = "O_sec_rad",
    group =
"""
1 *3 O   u1 {2,S}
2    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 697,
    label = "O_rad/NonDeC",
    group =
"""
1 *3 O  u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 698,
    label = "O_rad/Cs\/H_or_Val7/2\Cs|/H_or_Val7/|Cs2",
    group =
"""
1     C        u0 {2,S} {3,S} {4,S} {5,S}
2     C        u0 {1,S} {7,S} {8,S} {9,S}
3     Cs       u0 {1,S} {6,S} {10,S} {11,S}
4     C        u0 {1,S} {12,S} {13,S} {14,S}
5     [H,Val7] u0 {1,S}
6  *3 O        u1 {3,S}
7     [H,Val7] u0 {2,S}
8     [H,Val7] u0 {2,S}
9     [H,Val7] u0 {2,S}
10    [H,Val7] u0 {3,S}
11    [H,Val7] u0 {3,S}
12    [H,Val7] u0 {4,S}
13    [H,Val7] u0 {4,S}
14    [H,Val7] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 699,
    label = "O_rad/Cs\H2\Cs|H|Cs2",
    group =
"""
1     C  u0 {2,S} {3,S} {4,S} {5,S}
2     C  u0 {1,S} {7,S} {8,S} {9,S}
3     Cs u0 {1,S} {6,S} {10,S} {11,S}
4     C  u0 {1,S} {12,S} {13,S} {14,S}
5     H  u0 {1,S}
6  *3 O  u1 {3,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 700,
    label = "O_rad/NonDeO",
    group =
"""
1 *3 O u1 {2,S}
2    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 701,
    label = "OOC",
    group =
"""
1    O u0 {2,S} {3,S}
2 *3 O u1 {1,S}
3    C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 702,
    label = "O_rad/NonDeN",
    group =
"""
1 *3 O   u1 {2,S}
2    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 703,
    label = "O_rad/OneDe",
    group =
"""
1 *3 O                             u1 {2,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N3t,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 704,
    label = "O_rad/OneDeC",
    group =
"""
1 *3 O                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 705,
    label = "O_rad/Cd",
    group =
"""
1    Cd       u0 {2,S} {3,D}
2 *3 O        u1 {1,S}
3    [Cd,Cdd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 706,
    label = "O_rad/Cd\Cs_Cd\Cs2",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 707,
    label = "O_rad/Cd\H_Cd\H\Cs",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 708,
    label = "O_rad/Cd\H_Cd\H2",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 709,
    label = "O_rad/Cd\H_Cd\Cs2",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 710,
    label = "O_rad/Cd\H_Cd\Cs2-F",
    group =
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2    Cd  u0 {1,D} {5,S} {6,S}
3 *3 O   u1 {1,S}
4    F1s u0 {1,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 711,
    label = "O_rad/Cd\H_Cd\Cs2-Cl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2    Cd   u0 {1,D} {5,S} {6,S}
3 *3 O    u1 {1,S}
4    Cl1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cs   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 712,
    label = "O_rad/Cd\H_Cd\Cs2-Br",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2    Cd   u0 {1,D} {5,S} {6,S}
3 *3 O    u1 {1,S}
4    Br1s u0 {1,S}
5    Cs   u0 {2,S}
6    Cs   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 713,
    label = "O_rad/Cd\Cs_Cd\H2",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 714,
    label = "O_rad/Cd\Cs_Cd\H\Cs",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 O  u1 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 715,
    label = "O_rad/Cd\Cs_Cd\H\Cs-F",
    group =
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2    Cd  u0 {1,D} {5,S} {6,S}
3 *3 O   u1 {1,S}
4    Cs  u0 {1,S}
5    Cs  u0 {2,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 716,
    label = "O_rad/Cd\Cs_Cd\H\Cs-Cl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2    Cd   u0 {1,D} {5,S} {6,S}
3 *3 O    u1 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 717,
    label = "O_rad/Cd\Cs_Cd\H\Cs-Br",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2    Cd   u0 {1,D} {5,S} {6,S}
3 *3 O    u1 {1,S}
4    Cs   u0 {1,S}
5    Cs   u0 {2,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 718,
    label = "O_rad/OneDeN",
    group =
"""
1 *3 O              u1 {2,S}
2    [N3d,N3t,N5dc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 719,
    label = "InChI=1S/NO3/c2-1(3)4",
    group =
"""
1    N5dc u0 {2,S} {3,D} {4,S}
2 *3 O2s  u1 {1,S}
3    O2d  u0 {1,D}
4    O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 720,
    label = "S_rad",
    group =
"""
1 *3 S u1
""",
    kinetics = None,
)

entry(
    index = 721,
    label = "S_pri_rad-H_or_Val7-1",
    group =
"""
1 *3 S2s      u1 {2,S}
2    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 722,
    label = "S_pri_rad",
    group =
"""
1 *3 S2s u1 {2,S}
2    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 723,
    label = "S_pri_rad-F",
    group =
"""
1 *3 S2s u1 {2,S}
2    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 724,
    label = "S_pri_rad-Cl",
    group =
"""
1 *3 S2s  u1 {2,S}
2    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 725,
    label = "S_pri_rad-Br",
    group =
"""
1 *3 S2s  u1 {2,S}
2    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 726,
    label = "S_rad/single",
    group =
"""
1 *3 S   u1 {2,S}
2    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 727,
    label = "S_rad/NonDeC",
    group =
"""
1 *3 S2s u1 {2,S}
2    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 728,
    label = "S_rad/NonDeS",
    group =
"""
1 *3 S2s u1 {2,S}
2    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 729,
    label = "S_rad/NonDeN",
    group =
"""
1 *3 S2s u1 {2,S}
2    N   u0 p1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 730,
    label = "S_rad/NonDeO",
    group =
"""
1 *3 S2s u1 {2,S}
2    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 731,
    label = "S_rad/OneDe",
    group =
"""
1 *3 S2s              u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 732,
    label = "S_rad/Ct",
    group =
"""
1 *3 S2s u1 {2,S}
2    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 733,
    label = "S_rad/Cb",
    group =
"""
1 *3 S2s u1 {2,S}
2    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 734,
    label = "S_rad/CO",
    group =
"""
1 *3 S2s u1 {2,S}
2    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 735,
    label = "S_rad/Cd",
    group =
"""
1    Cd  u0 {2,S} {3,D}
2 *3 S2s u1 {1,S}
3    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 736,
    label = "S_rad/CS",
    group =
"""
1    CS  u0 {2,S} {3,D}
2 *3 S2s u1 {1,S}
3    S   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 737,
    label = "S_rad/double",
    group =
"""
1 *3 S   u1 p[0,1] {2,D}
2    R!H!Val7 u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 738,
    label = "S_rad/double_val4",
    group =
"""
1 *3 S   u1 p1 {2,D}
2    R!H!Val7 u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 739,
    label = "S_rad/double_val4C",
    group =
"""
1 *3 S u1 p1 {2,D}
2    C u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 740,
    label = "S_rad/double_val4N",
    group =
"""
1 *3 S u1 p1 {2,D}
2    N u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 741,
    label = "S_rad/double_val4S",
    group =
"""
1 *3 S u1 p1 {2,D}
2    S u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 742,
    label = "S_rad/double_val4O",
    group =
"""
1 *3 S u1 p1 {2,D}
2    O u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 743,
    label = "S_rad/double_val6",
    group =
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    R!H!Val7        u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 744,
    label = "S_rad/double_val6C",
    group =
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    C          u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 745,
    label = "S_rad/double_val6N",
    group =
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    N          u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 746,
    label = "S_rad/double_val6S",
    group =
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    S          u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 747,
    label = "S_rad/double_val6O",
    group =
"""
1 *3 [S6d,S6dc] u1 p0 {2,D}
2    O          u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 748,
    label = "S_rad/twoDoubles",
    group =
"""
1 *3 [S6dd,S6dc] u1 p0 {2,D} {3,D}
2    R!H!Val7         u0 {1,D}
3    R!H!Val7         u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 749,
    label = "S_rad/twoDoublesOO",
    group =
"""
1 *3 [S6dd,S6dc] u1 p0 {2,D} {3,D}
2    O           u0 {1,D}
3    O           u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 750,
    label = "S_rad/triple",
    group =
"""
1 *3 S   u1 p[0,1] {2,T}
2    R!H!Val7 u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 751,
    label = "S_rad/triple_val4",
    group =
"""
1 *3 S   u1 p1 {2,T}
2    R!H!Val7 u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 752,
    label = "S_rad/triple_val4C",
    group =
"""
1 *3 S u1 p1 {2,T}
2    C u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 753,
    label = "S_rad/triple_val4N",
    group =
"""
1 *3 S u1 p1 {2,T}
2    N u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 754,
    label = "S_rad/triple_val4S",
    group =
"""
1 *3 S u1 p1 {2,T}
2    S u0 p[0,1] {1,T}
""",
    kinetics = None,
)

entry(
    index = 755,
    label = "S_rad/triple_val6",
    group =
"""
1 *3 S   u1 p0 {2,T}
2    R!H!Val7 u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 756,
    label = "S_rad/triple_val6C",
    group =
"""
1 *3 S u1 p0 {2,T}
2    C u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 757,
    label = "S_rad/triple_val6N",
    group =
"""
1 *3 S u1 p0 {2,T}
2    N u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 758,
    label = "S_rad/triple_val6S",
    group =
"""
1 *3 S u1 p0 {2,T}
2    S u0 p[0,1] {1,T}
""",
    kinetics = None,
)

entry(
    index = 759,
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
    index = 760,
    label = "Cd_pri_rad-H_or_Val7-1",
    group =
"""
1 *3 C        u1 {2,D} {3,S}
2    Cd       u0 {1,D} {4,S}
3    [H,Val7] u0 {1,S}
4    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 761,
    label = "Cd_pri_rad",
    group =
"""
1 *3 C  u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    H  u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 762,
    label = "Cd_Cd\H2_pri_rad",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 763,
    label = "Cd_Cd\H\Cs_pri_rad",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 C  u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 764,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad",
    group =
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {7,S}
3 *3 Cd u1 {2,D} {8,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 765,
    label = "Cd_Cd\Cs2_pri_rad",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 766,
    label = "Cd_pri_rad-F",
    group =
"""
1 *3 C   u1 {2,D} {3,S}
2    Cd  u0 {1,D} {4,S}
3    F1s u0 {1,S}
4    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 767,
    label = "Cd_Cd\H2_pri_rad-HHF",
    group =
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2 *3 C   u1 {1,D} {5,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 768,
    label = "Cd_Cd\H2_pri_rad-HFF",
    group =
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2 *3 C   u1 {1,D} {5,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 769,
    label = "Cd_Cd\H2_pri_rad-FFF",
    group =
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2 *3 C   u1 {1,D} {5,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 770,
    label = "Cd_Cd\H\Cs_pri_rad-HF",
    group =
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2 *3 C   u1 {1,D} {5,S}
3    Cs  u0 {1,S}
4    H   u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 771,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHHF",
    group =
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd  u0 {1,S} {3,D} {7,S}
3 *3 Cd  u1 {2,D} {8,S}
4    C   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {2,S}
8    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 772,
    label = "Cd_Cd\H\Cs_pri_rad-FF",
    group =
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2 *3 C   u1 {1,D} {5,S}
3    Cs  u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 773,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHFF",
    group =
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd  u0 {1,S} {3,D} {7,S}
3 *3 Cd  u1 {2,D} {8,S}
4    C   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    F1s u0 {2,S}
8    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 774,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HFFF",
    group =
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd  u0 {1,S} {3,D} {7,S}
3 *3 Cd  u1 {2,D} {8,S}
4    C   u0 {1,S}
5    H   u0 {1,S}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
8    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 775,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FFFF",
    group =
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2    Cd  u0 {1,S} {3,D} {7,S}
3 *3 Cd  u1 {2,D} {8,S}
4    C   u0 {1,S}
5    F1s u0 {1,S}
6    F1s u0 {1,S}
7    F1s u0 {2,S}
8    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 776,
    label = "Cd_Cd\Cs2_pri_rad-F",
    group =
"""
1    Cd  u0 {2,D} {3,S} {4,S}
2 *3 Cd  u1 {1,D} {5,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
5    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 777,
    label = "Cd_pri_rad-Cl",
    group =
"""
1 *3 C    u1 {2,D} {3,S}
2    Cd   u0 {1,D} {4,S}
3    Cl1s u0 {1,S}
4    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 778,
    label = "Cd_Cd\H2_pri_rad-HHCl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 779,
    label = "Cd_Cd\H2_pri_rad-HFCl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 780,
    label = "Cd_Cd\H2_pri_rad-HClCl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 781,
    label = "Cd_Cd\H2_pri_rad-FFCl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 782,
    label = "Cd_Cd\H2_pri_rad-FClCl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 783,
    label = "Cd_Cd\H2_pri_rad-ClClCl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 784,
    label = "Cd_Cd\H\Cs_pri_rad-HCl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 785,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHHCl",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3 *3 Cd   u1 {2,D} {8,S}
4    C    u0 {1,S}
5    H    u0 {1,S}
6    H    u0 {1,S}
7    H    u0 {2,S}
8    Cl1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 786,
    label = "Cd_Cd\H\Cs_pri_rad-FCl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 787,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHFCl",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3 *3 Cd   u1 {2,D} {8,S}
4    C    u0 {1,S}
5    H    u0 {1,S}
6    H    u0 {1,S}
7    F1s  u0 {2,S}
8    Cl1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 788,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HFFCl",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3 *3 Cd   u1 {2,D} {8,S}
4    C    u0 {1,S}
5    H    u0 {1,S}
6    F1s  u0 {1,S}
7    F1s  u0 {2,S}
8    Cl1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 789,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FFFCl",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3 *3 Cd   u1 {2,D} {8,S}
4    C    u0 {1,S}
5    F1s  u0 {1,S}
6    F1s  u0 {1,S}
7    F1s  u0 {2,S}
8    Cl1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 790,
    label = "Cd_Cd\H\Cs_pri_rad-ClCl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 791,
    label = "Cd_Cd\Cs2_pri_rad-Cl",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 Cd   u1 {1,D} {5,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 792,
    label = "Cd_pri_rad-Br",
    group =
"""
1 *3 C    u1 {2,D} {3,S}
2    Cd   u0 {1,D} {4,S}
3    Br1s u0 {1,S}
4    R    u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 793,
    label = "Cd_Cd\H2_pri_rad-HHBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    H    u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 794,
    label = "Cd_Cd\H2_pri_rad-HFBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    H    u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 795,
    label = "Cd_Cd\H2_pri_rad-HClBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 796,
    label = "Cd_Cd\H2_pri_rad-HBrBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 797,
    label = "Cd_Cd\H2_pri_rad-FFBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    F1s  u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 798,
    label = "Cd_Cd\H2_pri_rad-FClBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 799,
    label = "Cd_Cd\H2_pri_rad-FBrBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 800,
    label = "Cd_Cd\H2_pri_rad-ClClBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 801,
    label = "Cd_Cd\H2_pri_rad-ClBrBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 802,
    label = "Cd_Cd\H2_pri_rad-BrBrBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 803,
    label = "Cd_Cd\H\Cs_pri_rad-HBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cs   u0 {1,S}
4    H    u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 804,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHHBr",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3 *3 Cd   u1 {2,D} {8,S}
4    C    u0 {1,S}
5    H    u0 {1,S}
6    H    u0 {1,S}
7    H    u0 {2,S}
8    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 805,
    label = "Cd_Cd\H\Cs_pri_rad-FBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cs   u0 {1,S}
4    F1s  u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 806,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HHFBr",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3 *3 Cd   u1 {2,D} {8,S}
4    C    u0 {1,S}
5    H    u0 {1,S}
6    H    u0 {1,S}
7    F1s  u0 {2,S}
8    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 807,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-HFFBr",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3 *3 Cd   u1 {2,D} {8,S}
4    C    u0 {1,S}
5    H    u0 {1,S}
6    F1s  u0 {1,S}
7    F1s  u0 {2,S}
8    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 808,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad-FFFBr",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2    Cd   u0 {1,S} {3,D} {7,S}
3 *3 Cd   u1 {2,D} {8,S}
4    C    u0 {1,S}
5    F1s  u0 {1,S}
6    F1s  u0 {1,S}
7    F1s  u0 {2,S}
8    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 809,
    label = "Cd_Cd\H\Cs_pri_rad-ClBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cs   u0 {1,S}
4    Cl1s u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 810,
    label = "Cd_Cd\H\Cs_pri_rad-BrBr",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 C    u1 {1,D} {5,S}
3    Cs   u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 811,
    label = "Cd_Cd\Cs2_pri_rad-Br",
    group =
"""
1    Cd   u0 {2,D} {3,S} {4,S}
2 *3 Cd   u1 {1,D} {5,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
5    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 812,
    label = "Cd_sec_rad",
    group =
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cd  u0 {1,D} {4,S}
3    R!H!Val7 u0 {1,S}
4    R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 813,
    label = "Cd_rad/NonDeC",
    group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    Cs u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 814,
    label = "Cd_Cd\/H_or_Val7/2_rad/Cs",
    group =
"""
1    Cd       u0 {2,D} {3,S} {4,S}
2 *3 Cd       u1 {1,D} {5,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    Cs       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 815,
    label = "Cd_Cd\H2_rad/Cs",
    group =
"""
1    Cd u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D} {5,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 816,
    label = "Cd_Cd\/H_or_Val7/\Cs_rad/Cs",
    group =
"""
1    Cs       u0 {3,S} {4,S} {5,S} {6,S}
2    Cd       u0 {3,D} {7,S} {8,S}
3 *3 Cd       u1 {1,S} {2,D}
4    [H,Val7] u0 {1,S}
5    [H,Val7] u0 {1,S}
6    [H,Val7] u0 {1,S}
7    Cs       u0 {2,S}
8    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 817,
    label = "Cd_Cd\H\Cs_rad/Cs",
    group =
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cd u0 {3,D} {7,S} {8,S}
3 *3 Cd u1 {1,S} {2,D}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    Cs u0 {2,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 818,
    label = "Cd_rad/NonDeO",
    group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    O  u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 819,
    label = "Cd_rad/NonDeS",
    group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    S  u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 820,
    label = "Cd_rad/NonDeN",
    group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    N  u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 821,
    label = "Cd_rad/OneDe",
    group =
"""
1 *3 Cd               u1 {2,D} {3,S}
2    Cd               u0 {1,D} {4,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    R                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 822,
    label = "Cd_rad/Ct",
    group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    Ct u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 823,
    label = "Cd_rad/Cb",
    group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    Cb u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 824,
    label = "Cd_rad/CO",
    group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {4,S}
3    CO u0 {1,S}
4    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 825,
    label = "Cd_rad/Cd",
    group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {5,S}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 826,
    label = "Cd_rad/CS",
    group =
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd u0 {1,D} {5,S}
3    CS u0 {1,S} {4,D}
4    S  u0 {3,D}
5    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 827,
    label = "Cd_allenic_rad",
    group =
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 828,
    label = "Cd_Cdd_rad/H_or_Val7/",
    group =
"""
1 *3 Cd       u1 {2,D} {3,S}
2    Cdd      u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 829,
    label = "Cd_Cdd_rad/H",
    group =
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 830,
    label = "Cd_Cdd_rad/H-F",
    group =
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 831,
    label = "Cd_Cdd_rad/H-Cl",
    group =
"""
1 *3 Cd   u1 {2,D} {3,S}
2    Cdd  u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 832,
    label = "Cd_Cdd_rad/H-Br",
    group =
"""
1 *3 Cd   u1 {2,D} {3,S}
2    Cdd  u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 833,
    label = "Cb_rad",
    group =
"""
1 *3 Cb       u1 {2,B} {3,B}
2    [Cb,Cbf] u0 {1,B}
3    [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 834,
    label = "CO_rad",
    group =
"""
1 *3 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 835,
    label = "CO_pri_rad-H_or_Val7-1",
    group =
"""
1 *3 C        u1 {2,D} {3,S}
2    O        u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 836,
    label = "CO_pri_rad",
    group =
"""
1 *3 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 837,
    label = "CO_pri_rad-F",
    group =
"""
1 *3 C   u1 {2,D} {3,S}
2    O   u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 838,
    label = "CO_pri_rad-Cl",
    group =
"""
1 *3 C    u1 {2,D} {3,S}
2    O    u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 839,
    label = "CO_pri_rad-Br",
    group =
"""
1 *3 C    u1 {2,D} {3,S}
2    O    u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 840,
    label = "CO_sec_rad",
    group =
"""
1 *3 C   u1 {2,D} {3,S}
2    O   u0 {1,D}
3    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 841,
    label = "CO_rad/NonDe",
    group =
"""
1 *3 C        u1 {2,D} {3,S}
2    O        u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 842,
    label = "CO_rad/Cs",
    group =
"""
1 *3 C  u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 843,
    label = "CO_rad/OneDe",
    group =
"""
1 *3 C                u1 {2,D} {3,S}
2    O                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 844,
    label = "CS_rad",
    group =
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 845,
    label = "CS_pri_rad-H_or_Val7-1",
    group =
"""
1 *3 C        u1 {2,D} {3,S}
2    S        u0 {1,D}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 846,
    label = "CS_pri_rad",
    group =
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 847,
    label = "CS_pri_rad-F",
    group =
"""
1 *3 C   u1 {2,D} {3,S}
2    S   u0 {1,D}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 848,
    label = "CS_pri_rad-Cl",
    group =
"""
1 *3 C    u1 {2,D} {3,S}
2    S    u0 {1,D}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 849,
    label = "CS_pri_rad-Br",
    group =
"""
1 *3 C    u1 {2,D} {3,S}
2    S    u0 {1,D}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 850,
    label = "CS_sec_rad",
    group =
"""
1 *3 C   u1 {2,D} {3,S}
2    S   u0 {1,D}
3    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 851,
    label = "CS_rad/NonDe",
    group =
"""
1 *3 C        u1 {2,D} {3,S}
2    S        u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 852,
    label = "CS_rad/Cs",
    group =
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 853,
    label = "CS_rad/O",
    group =
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 854,
    label = "CS_rad/S",
    group =
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 855,
    label = "CS_rad/OneDe",
    group =
"""
1 *3 C                u1 {2,D} {3,S}
2    S                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 856,
    label = "CS_rad/Ct",
    group =
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 857,
    label = "CS_rad/Cb",
    group =
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 858,
    label = "CS_rad/CO",
    group =
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 859,
    label = "CS_rad/Cd",
    group =
"""
1 *3 C  u1 {2,S} {3,D}
2    Cd u0 {1,S} {4,D}
3    S  u0 {1,D}
4    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 860,
    label = "CS_rad/CS",
    group =
"""
1 *3 C  u1 {2,S} {3,D}
2    CS u0 {1,S} {4,D}
3    S  u0 {1,D}
4    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 861,
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

entry(
    index = 862,
    label = "C_methyl-H_or_Val7-3",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 863,
    label = "C_methyl",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 864,
    label = "C_methyl-HHF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 865,
    label = "C_methyl-HHCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 866,
    label = "C_methyl-HHBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 867,
    label = "C_methyl-HFF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 868,
    label = "C_methyl-HFCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 869,
    label = "C_methyl-HFBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 870,
    label = "C_methyl-HClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 871,
    label = "C_methyl-HClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 872,
    label = "C_methyl-HBrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 873,
    label = "C_methyl-FFF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 874,
    label = "C_methyl-FFCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 875,
    label = "C_methyl-FFBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 876,
    label = "C_methyl-FClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 877,
    label = "C_methyl-FClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 878,
    label = "C_methyl-FBrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 879,
    label = "C_methyl-ClClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 880,
    label = "C_methyl-ClClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 881,
    label = "C_methyl-ClBrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 882,
    label = "C_methyl-BrBrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 883,
    label = "C_pri_rad-H_or_Val7-2",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
4    R!H!Val7      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 884,
    label = "C_pri_rad",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 885,
    label = "C_rad/H2/Cs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 886,
    label = "C_rad/H2/Cs\H3",
    group =
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 887,
    label = "C_rad/H2/Cs\Cs2\O",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S}
4    [O,S] u0 {1,S}
5    C     u0 {1,S}
6    H     u0 {2,S}
7    H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 888,
    label = "C_rad/H2/Cs\H\Cs\Cs|O",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    C     u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    H     u0 {2,S}
8    [O,S] u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 889,
    label = "C_rad/H2/Cs\H\Cs|Cs\O",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {6,S} {7,S}
3    C     u0 {1,S} {8,S}
4    [O,S] u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {2,S}
7    H     u0 {2,S}
8    C     u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 890,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O",
    group =
"""
1    Cs    u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C     u1 {1,S} {8,S} {9,S}
3    C     u0 {1,S} {6,S} {7,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6    C     u0 {3,S}
7    [O,S] u0 {3,S}
8    H     u0 {2,S}
9    H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 891,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O",
    group =
"""
1    Cs    u0 {2,S} {3,S} {5,S} {6,S}
2 *3 C     u1 {1,S} {7,S} {8,S}
3    C     u0 {1,S} {4,S}
4    C     u0 {3,S} {9,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9    [O,S] u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 892,
    label = "C_rad/H2/Ct",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 893,
    label = "C_rad/H2/Cb",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 894,
    label = "C_rad/H2/CO",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 895,
    label = "C_rad/H2/CS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 896,
    label = "C_rad/H2/O",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 897,
    label = "C_rad/H2/S",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 898,
    label = "C_rad/H2/Cd",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    C u0 {1,S} {5,D}
3    H u0 {1,S}
4    H u0 {1,S}
5    C u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 899,
    label = "C_rad/H2/Cd\H_Cd\H2",
    group =
"""
1 *3 C u1 {2,S} {4,S} {5,S}
2    C u0 {1,S} {3,D} {6,S}
3    C u0 {2,D}
4    H u0 {1,S}
5    H u0 {1,S}
6    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 900,
    label = "C_rad/H2/Cd\H_Cd\H2-HHF",
    group =
"""
1 *3 C   u1 {2,S} {4,S} {5,S}
2    C   u0 {1,S} {3,D} {6,S}
3    C   u0 {2,D}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 901,
    label = "C_rad/H2/Cd\H_Cd\H2-HHCl",
    group =
"""
1 *3 C    u1 {2,S} {4,S} {5,S}
2    C    u0 {1,S} {3,D} {6,S}
3    C    u0 {2,D}
4    H    u0 {1,S}
5    H    u0 {1,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 902,
    label = "C_rad/H2/Cd\H_Cd\H2-HHBr",
    group =
"""
1 *3 C    u1 {2,S} {4,S} {5,S}
2    C    u0 {1,S} {3,D} {6,S}
3    C    u0 {2,D}
4    H    u0 {1,S}
5    H    u0 {1,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 903,
    label = "C_rad/H2/Cd\Cs_Cd\H2",
    group =
"""
1     C u0 {2,S} {5,S} {6,S} {7,S}
2     C u0 {1,S} {3,D} {4,S}
3     C u0 {2,D} {8,S} {9,S}
4  *3 C u1 {2,S} {10,S} {11,S}
5     H u0 {1,S}
6     H u0 {1,S}
7     H u0 {1,S}
8     H u0 {3,S}
9     H u0 {3,S}
10    H u0 {4,S}
11    H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 904,
    label = "C_rad/H2/N",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    N u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 905,
    label = "C_pri_rad-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 906,
    label = "C_rad/H2/Cs-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 907,
    label = "C_rad/H2/Ct-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 908,
    label = "C_rad/H2/Cb-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 909,
    label = "C_rad/H2/CO-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 910,
    label = "C_rad/H2/CS-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 911,
    label = "C_rad/H2/O-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 912,
    label = "C_rad/H2/S-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 913,
    label = "C_rad/H2/Cd-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    C   u0 {1,S} {5,D}
3    H   u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 914,
    label = "C_rad/H2/Cd\H_Cd\H2-HFF",
    group =
"""
1 *3 C   u1 {2,S} {4,S} {5,S}
2    C   u0 {1,S} {3,D} {6,S}
3    C   u0 {2,D}
4    H   u0 {1,S}
5    F1s u0 {1,S}
6    F1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 915,
    label = "C_rad/H2/Cd\H_Cd\H2-HFCl",
    group =
"""
1 *3 C    u1 {2,S} {4,S} {5,S}
2    C    u0 {1,S} {3,D} {6,S}
3    C    u0 {2,D}
4    H    u0 {1,S}
5    F1s  u0 {1,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 916,
    label = "C_rad/H2/Cd\H_Cd\H2-HFBr",
    group =
"""
1 *3 C    u1 {2,S} {4,S} {5,S}
2    C    u0 {1,S} {3,D} {6,S}
3    C    u0 {2,D}
4    H    u0 {1,S}
5    F1s  u0 {1,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 917,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHHF",
    group =
"""
1     C   u0 {2,S} {5,S} {6,S} {7,S}
2     C   u0 {1,S} {3,D} {4,S}
3     C   u0 {2,D} {8,S} {9,S}
4  *3 C   u1 {2,S} {10,S} {11,S}
5     H   u0 {1,S}
6     H   u0 {1,S}
7     H   u0 {1,S}
8     H   u0 {3,S}
9     H   u0 {3,S}
10    H   u0 {4,S}
11    F1s u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 918,
    label = "C_rad/H2/N-HF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
4    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 919,
    label = "C_pri_rad-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 920,
    label = "C_rad/H2/Cs-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 921,
    label = "C_rad/H2/Ct-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 922,
    label = "C_rad/H2/Cb-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 923,
    label = "C_rad/H2/CO-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 924,
    label = "C_rad/H2/CS-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 925,
    label = "C_rad/H2/O-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 926,
    label = "C_rad/H2/S-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 927,
    label = "C_rad/H2/Cd-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    C    u0 {1,S} {5,D}
3    H    u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 928,
    label = "C_rad/H2/Cd\H_Cd\H2-HClCl",
    group =
"""
1 *3 C    u1 {2,S} {4,S} {5,S}
2    C    u0 {1,S} {3,D} {6,S}
3    C    u0 {2,D}
4    H    u0 {1,S}
5    Cl1s u0 {1,S}
6    Cl1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 929,
    label = "C_rad/H2/Cd\H_Cd\H2-HClBr",
    group =
"""
1 *3 C    u1 {2,S} {4,S} {5,S}
2    C    u0 {1,S} {3,D} {6,S}
3    C    u0 {2,D}
4    H    u0 {1,S}
5    Cl1s u0 {1,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 930,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHHCl",
    group =
"""
1     C    u0 {2,S} {5,S} {6,S} {7,S}
2     C    u0 {1,S} {3,D} {4,S}
3     C    u0 {2,D} {8,S} {9,S}
4  *3 C    u1 {2,S} {10,S} {11,S}
5     H    u0 {1,S}
6     H    u0 {1,S}
7     H    u0 {1,S}
8     H    u0 {3,S}
9     H    u0 {3,S}
10    H    u0 {4,S}
11    Cl1s u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 931,
    label = "C_rad/H2/N-HCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 932,
    label = "C_pri_rad-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 933,
    label = "C_rad/H2/Cs-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 934,
    label = "C_rad/H2/Ct-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 935,
    label = "C_rad/H2/Cb-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 936,
    label = "C_rad/H2/CO-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 937,
    label = "C_rad/H2/CS-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 938,
    label = "C_rad/H2/O-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 939,
    label = "C_rad/H2/S-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 940,
    label = "C_rad/H2/Cd-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    C    u0 {1,S} {5,D}
3    H    u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 941,
    label = "C_rad/H2/Cd\H_Cd\H2-HBrBr",
    group =
"""
1 *3 C    u1 {2,S} {4,S} {5,S}
2    C    u0 {1,S} {3,D} {6,S}
3    C    u0 {2,D}
4    H    u0 {1,S}
5    Br1s u0 {1,S}
6    Br1s u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 942,
    label = "C_rad/H2/Cd\Cs_Cd\H2-HHHHHHBr",
    group =
"""
1     C    u0 {2,S} {5,S} {6,S} {7,S}
2     C    u0 {1,S} {3,D} {4,S}
3     C    u0 {2,D} {8,S} {9,S}
4  *3 C    u1 {2,S} {10,S} {11,S}
5     H    u0 {1,S}
6     H    u0 {1,S}
7     H    u0 {1,S}
8     H    u0 {3,S}
9     H    u0 {3,S}
10    H    u0 {4,S}
11    Br1s u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 943,
    label = "C_rad/H2/N-HBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 944,
    label = "C_pri_rad-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 945,
    label = "C_rad/H2/Cs-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 946,
    label = "C_rad/H2/Ct-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    Ct  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 947,
    label = "C_rad/H2/Cb-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 948,
    label = "C_rad/H2/CO-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 949,
    label = "C_rad/H2/CS-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    CS  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 950,
    label = "C_rad/H2/O-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 951,
    label = "C_rad/H2/S-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 952,
    label = "C_rad/H2/Cd-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    C   u0 {1,S} {5,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 953,
    label = "C_rad/H2/N-FF",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
4    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 954,
    label = "C_pri_rad-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 955,
    label = "C_rad/H2/Cs-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 956,
    label = "C_rad/H2/Ct-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 957,
    label = "C_rad/H2/Cb-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 958,
    label = "C_rad/H2/CO-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 959,
    label = "C_rad/H2/CS-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 960,
    label = "C_rad/H2/O-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 961,
    label = "C_rad/H2/S-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 962,
    label = "C_rad/H2/Cd-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    C    u0 {1,S} {5,D}
3    F1s  u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 963,
    label = "C_rad/H2/N-FCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 964,
    label = "C_pri_rad-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 965,
    label = "C_rad/H2/Cs-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 966,
    label = "C_rad/H2/Ct-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 967,
    label = "C_rad/H2/Cb-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 968,
    label = "C_rad/H2/CO-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 969,
    label = "C_rad/H2/CS-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 970,
    label = "C_rad/H2/O-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 971,
    label = "C_rad/H2/S-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 972,
    label = "C_rad/H2/Cd-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    C    u0 {1,S} {5,D}
3    F1s  u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 973,
    label = "C_rad/H2/N-FBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 974,
    label = "C_pri_rad-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 975,
    label = "C_rad/H2/Cs-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 976,
    label = "C_rad/H2/Ct-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 977,
    label = "C_rad/H2/Cb-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 978,
    label = "C_rad/H2/CO-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 979,
    label = "C_rad/H2/CS-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 980,
    label = "C_rad/H2/O-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 981,
    label = "C_rad/H2/S-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 982,
    label = "C_rad/H2/Cd-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    C    u0 {1,S} {5,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 983,
    label = "C_rad/H2/N-ClCl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 984,
    label = "C_pri_rad-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 985,
    label = "C_rad/H2/Cs-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 986,
    label = "C_rad/H2/Ct-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 987,
    label = "C_rad/H2/Cb-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 988,
    label = "C_rad/H2/CO-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 989,
    label = "C_rad/H2/CS-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 990,
    label = "C_rad/H2/O-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 991,
    label = "C_rad/H2/S-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 992,
    label = "C_rad/H2/Cd-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    C    u0 {1,S} {5,D}
3    Cl1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 993,
    label = "C_rad/H2/N-ClBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 994,
    label = "C_pri_rad-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 995,
    label = "C_rad/H2/Cs-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 996,
    label = "C_rad/H2/Ct-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Ct   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 997,
    label = "C_rad/H2/Cb-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    Cb   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 998,
    label = "C_rad/H2/CO-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 999,
    label = "C_rad/H2/CS-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    CS   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1000,
    label = "C_rad/H2/O-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1001,
    label = "C_rad/H2/S-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1002,
    label = "C_rad/H2/Cd-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    C    u0 {1,S} {5,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1003,
    label = "C_rad/H2/N-BrBr",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1004,
    label = "C_sec_rad-H_or_Val7-1",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    [H,Val7] u0 {1,S}
3    R!H!Val7      u0 {1,S}
4    R!H!Val7      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1005,
    label = "C_sec_rad",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    R!H!Val7 u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1006,
    label = "C_rad/H/NonDeC",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1007,
    label = "C_rad/H/NonDeC_5ring_fused6_1",
    group =
"""
1    Cs u0 {3,S} {4,S} {6,S}
2    Cs u0 {4,S} {5,S} {7,S}
3 *3 C  u1 {1,S} {5,S} {8,S}
4    Cs u0 {1,S} {2,S}
5    Cs u0 {2,S} {3,S}
6    Cs u0 {1,S} {7,S}
7    Cs u0 {2,S} {6,S}
8    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1008,
    label = "C_rad/H/NonDeC_5ring_fused6_2",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {8,S}
2    Cs u0 {1,S} {4,S} {6,S}
3    Cs u0 {1,S} {5,S} {7,S}
4    Cs u0 {2,S} {5,S}
5    Cs u0 {3,S} {4,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {3,S} {6,S}
8    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1009,
    label = "C_rad/H/Cs\H3/Cs\H3",
    group =
"""
1     Cs u0 {3,S} {4,S} {5,S} {6,S}
2     Cs u0 {3,S} {7,S} {8,S} {9,S}
3  *3 C  u1 {1,S} {2,S} {10,S}
4     H  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1010,
    label = "C_rad/H/NonDeC_5ring_alpha6ring",
    group =
"""
1     Cs u0 {2,S} {3,S} {5,S}
2     Cs u0 {1,S} {4,S} {7,S}
3  *3 C  u1 {1,S} {6,S} {10,S}
4     Cs u0 {2,S} {6,S}
5     C  u0 {1,S} {8,S}
6     Cs u0 {3,S} {4,S}
7     C  u0 {2,S} {9,S}
8     C  u0 {5,S} {9,S}
9     C  u0 {7,S} {8,S}
10    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1011,
    label = "C_rad/H/NonDeC_5ring_beta6ring",
    group =
"""
1     Cs u0 {2,S} {4,S} {6,S}
2     Cs u0 {1,S} {5,S} {7,S}
3  *3 C  u1 {4,S} {5,S} {10,S}
4     Cs u0 {1,S} {3,S}
5     Cs u0 {2,S} {3,S}
6     C  u0 {1,S} {8,S}
7     C  u0 {2,S} {9,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {7,S} {8,S}
10    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1012,
    label = "C_rad/H/Cs\H2\CO/Cs",
    group =
"""
1    Cs      u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C       u1 {1,S} {6,S} {7,S}
3    [CO,CS] u0 {1,S}
4    H       u0 {1,S}
5    H       u0 {1,S}
6    Cs      u0 {2,S}
7    H       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1013,
    label = "C_rad/H/Cs\H2\Cs/Cs\H2\O",
    group =
"""
1     Cs    u0 {3,S} {4,S} {6,S} {7,S}
2     Cs    u0 {4,S} {5,S} {11,S} {12,S}
3     C     u0 {1,S} {8,S} {9,S} {10,S}
4  *3 C     u1 {1,S} {2,S} {13,S}
5     [O,S] u0 {2,S} {14,S}
6     H     u0 {1,S}
7     H     u0 {1,S}
8     H     u0 {3,S}
9     H     u0 {3,S}
10    H     u0 {3,S}
11    H     u0 {2,S}
12    H     u0 {2,S}
13    H     u0 {4,S}
14    H     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1014,
    label = "C_rad/H/Cs\H\Cs\O/Cs",
    group =
"""
1     Cs        u0 {2,S} {4,S} {5,S} {6,S}
2     Cs        u0 {1,S} {7,S} {8,S} {9,S}
3     Cs        u0 {4,S} {10,S} {11,S} {12,S}
4  *3 C         u1 {1,S} {3,S} {13,S}
5     [O2s,S2s] u0 {1,S} {14,S}
6     H         u0 {1,S}
7     H         u0 {2,S}
8     H         u0 {2,S}
9     H         u0 {2,S}
10    H         u0 {3,S}
11    H         u0 {3,S}
12    H         u0 {3,S}
13    H         u0 {4,S}
14    H         u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1015,
    label = "C_rad/H/Cs\H2\Cs|O/Cs",
    group =
"""
1     Cs    u0 {2,S} {4,S} {6,S} {7,S}
2     C     u0 {1,S} {5,S} {8,S} {9,S}
3     Cs    u0 {4,S} {10,S} {11,S} {12,S}
4  *3 C     u1 {1,S} {3,S} {13,S}
5     [O,S] u0 {2,S} {14,S}
6     H     u0 {1,S}
7     H     u0 {1,S}
8     H     u0 {2,S}
9     H     u0 {2,S}
10    H     u0 {3,S}
11    H     u0 {3,S}
12    H     u0 {3,S}
13    H     u0 {4,S}
14    H     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1016,
    label = "C_rad/H/NonDeO",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    H        u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1017,
    label = "C_rad/H/CsO",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1018,
    label = "C_rad/H/Cs\H2\Cs/O",
    group =
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C  u1 {1,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
6    H  u0 {2,S}
7    O  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1019,
    label = "C_rad/H/Cs\H2\Cs|H2|Cs/O",
    group =
"""
1     Cs u0 {2,S} {3,S} {6,S} {7,S}
2     Cs u0 {1,S} {4,S} {8,S} {9,S}
3     C  u0 {1,S} {10,S} {11,S} {12,S}
4  *3 C  u1 {2,S} {5,S} {13,S}
5     O  u0 {4,S} {14,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {3,S}
13    H  u0 {4,S}
14    H  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1020,
    label = "C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHHHHHHF",
    group =
"""
1     Cs  u0 {2,S} {3,S} {6,S} {7,S}
2     Cs  u0 {1,S} {4,S} {8,S} {9,S}
3     C   u0 {1,S} {10,S} {11,S} {12,S}
4  *3 C   u1 {2,S} {5,S} {13,S}
5     O   u0 {4,S} {14,S}
6     H   u0 {1,S}
7     H   u0 {1,S}
8     H   u0 {2,S}
9     H   u0 {2,S}
10    H   u0 {3,S}
11    H   u0 {3,S}
12    H   u0 {3,S}
13    H   u0 {4,S}
14    F1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1021,
    label = "C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHHHHHHCl",
    group =
"""
1     Cs   u0 {2,S} {3,S} {6,S} {7,S}
2     Cs   u0 {1,S} {4,S} {8,S} {9,S}
3     C    u0 {1,S} {10,S} {11,S} {12,S}
4  *3 C    u1 {2,S} {5,S} {13,S}
5     O    u0 {4,S} {14,S}
6     H    u0 {1,S}
7     H    u0 {1,S}
8     H    u0 {2,S}
9     H    u0 {2,S}
10    H    u0 {3,S}
11    H    u0 {3,S}
12    H    u0 {3,S}
13    H    u0 {4,S}
14    Cl1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1022,
    label = "C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHHHHHHBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {6,S} {7,S}
2     Cs   u0 {1,S} {4,S} {8,S} {9,S}
3     C    u0 {1,S} {10,S} {11,S} {12,S}
4  *3 C    u1 {2,S} {5,S} {13,S}
5     O    u0 {4,S} {14,S}
6     H    u0 {1,S}
7     H    u0 {1,S}
8     H    u0 {2,S}
9     H    u0 {2,S}
10    H    u0 {3,S}
11    H    u0 {3,S}
12    H    u0 {3,S}
13    H    u0 {4,S}
14    Br1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1023,
    label = "C_rad/H/Cs\H\Cs2/O",
    group =
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2 *3 C  u1 {1,S} {3,S} {7,S}
3    O  u0 {2,S} {8,S}
4    C  u0 {1,S}
5    C  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1024,
    label = "C_rad/H/Cs\H\Cs2/O-HHF",
    group =
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *3 C   u1 {1,S} {3,S} {7,S}
3    O   u0 {2,S} {8,S}
4    C   u0 {1,S}
5    C   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {2,S}
8    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1025,
    label = "C_rad/H/Cs\H\Cs2/O-HHCl",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2 *3 C    u1 {1,S} {3,S} {7,S}
3    O    u0 {2,S} {8,S}
4    C    u0 {1,S}
5    C    u0 {1,S}
6    H    u0 {1,S}
7    H    u0 {2,S}
8    Cl1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1026,
    label = "C_rad/H/Cs\H\Cs2/O-HHBr",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2 *3 C    u1 {1,S} {3,S} {7,S}
3    O    u0 {2,S} {8,S}
4    C    u0 {1,S}
5    C    u0 {1,S}
6    H    u0 {1,S}
7    H    u0 {2,S}
8    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1027,
    label = "C_rad/H/O2",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    O u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1028,
    label = "C_rad/H/NonDeS",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    H        u0 {1,S}
3    S        u0 {1,S}
4    [Cs,S,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1029,
    label = "C_rad/H/CsS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1030,
    label = "C_rad/H/S2",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    S u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1031,
    label = "C_rad/H/NonDeCN",
    group =
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
4    N  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1032,
    label = "C_rad/H/NonDeON",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    O u0 {1,S}
4    N u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1033,
    label = "C_rad/H/NonDeNN",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    N u0 {1,S}
4    N u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1034,
    label = "C_rad/H/OneDe",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1035,
    label = "C_rad/H/OneDeC",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1036,
    label = "C_rad/H/CtCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1037,
    label = "C_rad/H/CbCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1038,
    label = "C_rad/H/CO/Cs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1039,
    label = "C_rad/H/CO\H/Cs\H3",
    group =
"""
1    Cs u0 {2,S} {4,S} {5,S} {6,S}
2 *3 C  u1 {1,S} {3,S} {7,S}
3    CO u0 {2,S} {8,D} {9,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    O  u0 {3,D}
9    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1040,
    label = "C_rad/H/CO\H/Cs\H3-HHHHF",
    group =
"""
1    Cs  u0 {2,S} {4,S} {5,S} {6,S}
2 *3 C   u1 {1,S} {3,S} {7,S}
3    CO  u0 {2,S} {8,D} {9,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    H   u0 {1,S}
7    H   u0 {2,S}
8    O   u0 {3,D}
9    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1041,
    label = "C_rad/H/CO\H/Cs\H3-HHHHCl",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2 *3 C    u1 {1,S} {3,S} {7,S}
3    CO   u0 {2,S} {8,D} {9,S}
4    H    u0 {1,S}
5    H    u0 {1,S}
6    H    u0 {1,S}
7    H    u0 {2,S}
8    O    u0 {3,D}
9    Cl1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1042,
    label = "C_rad/H/CO\H/Cs\H3-HHHHBr",
    group =
"""
1    Cs   u0 {2,S} {4,S} {5,S} {6,S}
2 *3 C    u1 {1,S} {3,S} {7,S}
3    CO   u0 {2,S} {8,D} {9,S}
4    H    u0 {1,S}
5    H    u0 {1,S}
6    H    u0 {1,S}
7    H    u0 {2,S}
8    O    u0 {3,D}
9    Br1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1043,
    label = "C_rad/H/CdCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1044,
    label = "C_rad/H/CSCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1045,
    label = "C_rad/H/OneDeO",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1046,
    label = "C_rad/H/OneDeS",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1047,
    label = "C_rad/H/CtS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1048,
    label = "C_rad/H/CbS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1049,
    label = "C_rad/H/CdS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    S  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1050,
    label = "C_rad/H/CSS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S} {5,D}
3    H  u0 {1,S}
4    S  u0 {1,S}
5    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1051,
    label = "C_rad/H/OneDeN",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
4    N  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1052,
    label = "C_rad/H/TwoDe",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1053,
    label = "C_rad/H/CtCt",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1054,
    label = "C_rad/H/CtCb",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1055,
    label = "C_rad/H/CtCO",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1056,
    label = "C_rad/H/CbCb",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1057,
    label = "C_rad/H/CbCO",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1058,
    label = "C_rad/H/COCO",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    CO u0 {1,S}
4    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1059,
    label = "C_rad/H/CdCt",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1060,
    label = "C_rad/H/CtCS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S} {5,D}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1061,
    label = "C_rad/H/CdCb",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1062,
    label = "C_rad/H/CbCS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S} {5,D}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    S  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1063,
    label = "C_rad/H/CdCO",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    CO u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1064,
    label = "C_rad/H/COCS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    CO u0 {1,S}
4    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1065,
    label = "C_rad/H/CdCd",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1066,
    label = "C_rad/H/CdCS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S} {6,D}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1067,
    label = "C_rad/H/CSCS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S} {5,D}
3    CS u0 {1,S} {6,D}
4    H  u0 {1,S}
5    S  u0 {2,D}
6    S  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1068,
    label = "C_sec_rad-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    R!H!Val7 u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1069,
    label = "C_rad/H/NonDeC-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Cs  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1070,
    label = "C_rad/H/NonDeO-F",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    F1s      u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1071,
    label = "C_rad/H/CsO-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Cs  u0 {1,S}
4    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1072,
    label = "C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHFFFFFF",
    group =
"""
1     Cs  u0 {2,S} {3,S} {6,S} {7,S}
2     Cs  u0 {1,S} {4,S} {8,S} {9,S}
3     C   u0 {1,S} {10,S} {11,S} {12,S}
4  *3 C   u1 {2,S} {5,S} {13,S}
5     O   u0 {4,S} {14,S}
6     H   u0 {1,S}
7     H   u0 {1,S}
8     H   u0 {2,S}
9     F1s u0 {2,S}
10    F1s u0 {3,S}
11    F1s u0 {3,S}
12    F1s u0 {3,S}
13    F1s u0 {4,S}
14    F1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1073,
    label = "C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHFFFFFCl",
    group =
"""
1     Cs   u0 {2,S} {3,S} {6,S} {7,S}
2     Cs   u0 {1,S} {4,S} {8,S} {9,S}
3     C    u0 {1,S} {10,S} {11,S} {12,S}
4  *3 C    u1 {2,S} {5,S} {13,S}
5     O    u0 {4,S} {14,S}
6     H    u0 {1,S}
7     H    u0 {1,S}
8     H    u0 {2,S}
9     F1s  u0 {2,S}
10    F1s  u0 {3,S}
11    F1s  u0 {3,S}
12    F1s  u0 {3,S}
13    F1s  u0 {4,S}
14    Cl1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1074,
    label = "C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHFFFFFBr",
    group =
"""
1     Cs   u0 {2,S} {3,S} {6,S} {7,S}
2     Cs   u0 {1,S} {4,S} {8,S} {9,S}
3     C    u0 {1,S} {10,S} {11,S} {12,S}
4  *3 C    u1 {2,S} {5,S} {13,S}
5     O    u0 {4,S} {14,S}
6     H    u0 {1,S}
7     H    u0 {1,S}
8     H    u0 {2,S}
9     F1s  u0 {2,S}
10    F1s  u0 {3,S}
11    F1s  u0 {3,S}
12    F1s  u0 {3,S}
13    F1s  u0 {4,S}
14    Br1s u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1075,
    label = "C_rad/H/O2-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    O   u0 {1,S}
4    O   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1076,
    label = "C_rad/H/NonDeS-F",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    F1s      u0 {1,S}
3    S        u0 {1,S}
4    [Cs,S,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1077,
    label = "C_rad/H/CsS-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    S   u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1078,
    label = "C_rad/H/S2-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    S   u0 {1,S}
4    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1079,
    label = "C_rad/H/NonDeCN-F",
    group =
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Cs  u0 {1,S}
4    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1080,
    label = "C_rad/H/NonDeON-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    O   u0 {1,S}
4    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1081,
    label = "C_rad/H/NonDeNN-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    N   u0 {1,S}
4    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1082,
    label = "C_rad/H/OneDe-F",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1083,
    label = "C_rad/H/OneDeC-F",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1084,
    label = "C_rad/H/CtCs-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Ct  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1085,
    label = "C_rad/H/CbCs-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Cb  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1086,
    label = "C_rad/H/CO/Cs-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Cs  u0 {1,S}
4    CO  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1087,
    label = "C_rad/H/CdCs-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S} {5,D}
3    F1s u0 {1,S}
4    Cs  u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1088,
    label = "C_rad/H/CSCs-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    CS  u0 {1,S}
4    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1089,
    label = "C_rad/H/OneDeO-F",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1090,
    label = "C_rad/H/OneDeS-F",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1091,
    label = "C_rad/H/CtS-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Ct  u0 {1,S}
4    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1092,
    label = "C_rad/H/CbS-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Cb  u0 {1,S}
4    S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1093,
    label = "C_rad/H/CdS-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    Cd  u0 {1,S} {5,D}
3    F1s u0 {1,S}
4    S   u0 {1,S}
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1094,
    label = "C_rad/H/CSS-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    CS  u0 {1,S} {5,D}
3    F1s u0 {1,S}
4    S   u0 {1,S}
5    S   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1095,
    label = "C_rad/H/OneDeN-F",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    F1s u0 {1,S}
3    Cd  u0 {1,S}
4    N   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1096,
    label = "C_rad/H/TwoDe-F",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    F1s              u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1097,
    label = "C_sec_rad-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    R!H!Val7  u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1098,
    label = "C_rad/H/NonDeC-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1099,
    label = "C_rad/H/NonDeO-Cl",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    Cl1s     u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1100,
    label = "C_rad/H/CsO-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cs   u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1101,
    label = "C_rad/H/O2-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    O    u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1102,
    label = "C_rad/H/NonDeS-Cl",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    Cl1s     u0 {1,S}
3    S        u0 {1,S}
4    [Cs,S,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1103,
    label = "C_rad/H/CsS-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    S    u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1104,
    label = "C_rad/H/S2-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    S    u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1105,
    label = "C_rad/H/NonDeCN-Cl",
    group =
"""
1 *3 Cs   u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cs   u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1106,
    label = "C_rad/H/NonDeON-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    O    u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1107,
    label = "C_rad/H/NonDeNN-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    N    u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1108,
    label = "C_rad/H/OneDe-Cl",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1109,
    label = "C_rad/H/OneDeC-Cl",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1110,
    label = "C_rad/H/CtCs-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1111,
    label = "C_rad/H/CbCs-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1112,
    label = "C_rad/H/CO/Cs-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cs   u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1113,
    label = "C_rad/H/CdCs-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    Cl1s u0 {1,S}
4    Cs   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1114,
    label = "C_rad/H/CSCs-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    CS   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1115,
    label = "C_rad/H/OneDeO-Cl",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1116,
    label = "C_rad/H/OneDeS-Cl",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1117,
    label = "C_rad/H/CtS-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Ct   u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1118,
    label = "C_rad/H/CbS-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cb   u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1119,
    label = "C_rad/H/CdS-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    Cl1s u0 {1,S}
4    S    u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1120,
    label = "C_rad/H/CSS-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    CS   u0 {1,S} {5,D}
3    Cl1s u0 {1,S}
4    S    u0 {1,S}
5    S    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1121,
    label = "C_rad/H/OneDeN-Cl",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cl1s u0 {1,S}
3    Cd   u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1122,
    label = "C_rad/H/TwoDe-Cl",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Cl1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1123,
    label = "C_sec_rad-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    R!H!Val7  u0 {1,S}
4    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1124,
    label = "C_rad/H/NonDeC-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Cs   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1125,
    label = "C_rad/H/NonDeO-Br",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    Br1s     u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1126,
    label = "C_rad/H/CsO-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Cs   u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1127,
    label = "C_rad/H/O2-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    O    u0 {1,S}
4    O    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1128,
    label = "C_rad/H/NonDeS-Br",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    Br1s     u0 {1,S}
3    S        u0 {1,S}
4    [Cs,S,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1129,
    label = "C_rad/H/CsS-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    S    u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1130,
    label = "C_rad/H/S2-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    S    u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1131,
    label = "C_rad/H/NonDeCN-Br",
    group =
"""
1 *3 Cs   u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Cs   u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1132,
    label = "C_rad/H/NonDeON-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    O    u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1133,
    label = "C_rad/H/NonDeNN-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    N    u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1134,
    label = "C_rad/H/OneDe-Br",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1135,
    label = "C_rad/H/OneDeC-Br",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1136,
    label = "C_rad/H/CtCs-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Ct   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1137,
    label = "C_rad/H/CbCs-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Cb   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1138,
    label = "C_rad/H/CO/Cs-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Cs   u0 {1,S}
4    CO   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1139,
    label = "C_rad/H/CdCs-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    Br1s u0 {1,S}
4    Cs   u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1140,
    label = "C_rad/H/CSCs-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    CS   u0 {1,S}
4    Cs   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1141,
    label = "C_rad/H/OneDeO-Br",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1142,
    label = "C_rad/H/OneDeS-Br",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1143,
    label = "C_rad/H/CtS-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Ct   u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1144,
    label = "C_rad/H/CbS-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Cb   u0 {1,S}
4    S    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1145,
    label = "C_rad/H/CdS-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Cd   u0 {1,S} {5,D}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
5    C    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1146,
    label = "C_rad/H/CSS-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    CS   u0 {1,S} {5,D}
3    Br1s u0 {1,S}
4    S    u0 {1,S}
5    S    u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1147,
    label = "C_rad/H/OneDeN-Br",
    group =
"""
1 *3 C    u1 {2,S} {3,S} {4,S}
2    Br1s u0 {1,S}
3    Cd   u0 {1,S}
4    N    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1148,
    label = "C_rad/H/TwoDe-Br",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    Br1s             u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1149,
    label = "C_ter_rad",
    group =
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    R!H!Val7 u0 {1,S}
3    R!H!Val7 u0 {1,S}
4    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1150,
    label = "C_rad/NonDe",
    group =
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1151,
    label = "C_rad/Cs3",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1152,
    label = "C_rad/Cs2/Cs\O",
    group =
"""
1 *3 C     u1 {2,S} {3,S} {4,S}
2    Cs    u0 {1,S} {5,S}
3    Cs    u0 {1,S}
4    Cs    u0 {1,S}
5    [O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1153,
    label = "C_rad/Cs3_5ring_fused6",
    group =
"""
1 *3 C  u1 {3,S} {4,S} {5,S}
2    Cs u0 {3,S} {6,S} {7,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {1,S} {6,S}
5    Cs u0 {1,S} {7,S}
6    Cs u0 {2,S} {4,S}
7    Cs u0 {2,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 1154,
    label = "C_rad/Cs3_5ring_adj5",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {1,S} {7,S}
4    Cs u0 {1,S} {8,S}
5    Cs u0 {2,S} {7,S}
6    Cs u0 {2,S} {8,S}
7    Cs u0 {3,S} {5,S}
8    Cs u0 {4,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 1155,
    label = "C_rad/NDMustO",
    group =
"""
1 *3 C      u1 {2,S} {3,S} {4,S}
2    O      u0 {1,S}
3    [Cs,O] u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1156,
    label = "C_rad/Cs2O",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1157,
    label = "C_rad/OOH/Cs/Cs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O  u0 {1,S} {5,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    O  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1158,
    label = "C_rad/O/Cs/Cs\Cs-H_or_Val7-9",
    group =
"""
1     Cs       u0 {2,S} {4,S} {6,S} {7,S}
2     C        u0 {1,S} {8,S} {9,S} {10,S}
3     Cs       u0 {4,S} {11,S} {12,S} {13,S}
4  *3 C        u1 {1,S} {3,S} {5,S}
5     O        u0 {4,S} {14,S}
6     [H,Val7] u0 {1,S}
7     [H,Val7] u0 {1,S}
8     [H,Val7] u0 {2,S}
9     [H,Val7] u0 {2,S}
10    [H,Val7] u0 {2,S}
11    [H,Val7] u0 {3,S}
12    [H,Val7] u0 {3,S}
13    [H,Val7] u0 {3,S}
14    [H,Val7] u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1159,
    label = "C_rad/O/Cs/Cs\Cs",
    group =
"""
1     Cs u0 {2,S} {4,S} {6,S} {7,S}
2     C  u0 {1,S} {8,S} {9,S} {10,S}
3     Cs u0 {4,S} {11,S} {12,S} {13,S}
4  *3 C  u1 {1,S} {3,S} {5,S}
5     O  u0 {4,S} {14,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
11    H  u0 {3,S}
12    H  u0 {3,S}
13    H  u0 {3,S}
14    H  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 1160,
    label = "C_rad/CsO2",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O  u0 {1,S}
3    O  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1161,
    label = "C_rad/O3",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    O u0 {1,S}
3    O u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1162,
    label = "C_rad/NDMustS",
    group =
"""
1 *3 C      u1 {2,S} {3,S} {4,S}
2    S      u0 {1,S}
3    [Cs,S] u0 {1,S}
4    [Cs,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1163,
    label = "C_rad/Cs2S",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    S  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1164,
    label = "C_rad/CsS2",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    S  u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1165,
    label = "C_rad/S3",
    group =
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    S u0 {1,S}
3    S u0 {1,S}
4    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1166,
    label = "C_rad/OneDe",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1167,
    label = "C_rad/Cs2",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Cs               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1168,
    label = "C_rad/CtCs2",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1169,
    label = "C_rad/CbCs2",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1170,
    label = "C_rad/COCs2",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1171,
    label = "C_rad/CdCs2",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1172,
    label = "C_rad/CSCs2",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1173,
    label = "C_rad/CsO",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O                u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1174,
    label = "C_rad/CsS",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S                u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1175,
    label = "C_rad/CtCsS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1176,
    label = "C_rad/CbCsS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1177,
    label = "C_rad/CdCsS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    S  u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1178,
    label = "C_rad/CSCsS",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1179,
    label = "C_rad/O2",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    O                u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1180,
    label = "C_rad/OS",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S                u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1181,
    label = "C_rad/S2",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S                u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1182,
    label = "C_rad/TwoDe",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1183,
    label = "C_rad/Cs",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1184,
    label = "C_rad/CtCtCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1185,
    label = "C_rad/CtCbCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1186,
    label = "C_rad/CtCOCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1187,
    label = "C_rad/CbCbCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1188,
    label = "C_rad/CbCOCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1189,
    label = "C_rad/COCOCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1190,
    label = "C_rad/CdCtCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1191,
    label = "C_rad/CtCSCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1192,
    label = "C_rad/CdCbCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1193,
    label = "C_rad/CbCSCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1194,
    label = "C_rad/CdCOCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1195,
    label = "C_rad/COCSCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1196,
    label = "C_rad/CdCdCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 1197,
    label = "C_rad/CdCSCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 1198,
    label = "C_rad/CSCSCs",
    group =
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1199,
    label = "C_rad/TDMustO",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1200,
    label = "C_rad/TDMustS",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1201,
    label = "C_rad/ThreeDe",
    group =
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1202,
    label = "N3_rad",
    group =
"""
1 *3 [N3s,N3d] u1
""",
    kinetics = None,
)

entry(
    index = 1203,
    label = "N3s_rad",
    group =
"""
1 *3 N3s u1     {2,S} {3,S}
2    R   u[0,1] {1,S}
3    R   u0     {1,S}
""",
    kinetics = None,
)

entry(
    index = 1204,
    label = "N/H_or_Val7/2_rad",
    group =
"""
1 *3 N3s      u1 {2,S} {3,S}
2    [H,Val7] u0 {1,S}
3    [H,Val7] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1205,
    label = "NH2_rad",
    group =
"""
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1206,
    label = "NH2_rad-HF",
    group =
"""
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1207,
    label = "NH2_rad-HCl",
    group =
"""
1 *3 N3s  u1 {2,S} {3,S}
2    H    u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1208,
    label = "NH2_rad-HBr",
    group =
"""
1 *3 N3s  u1 {2,S} {3,S}
2    H    u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1209,
    label = "NH2_rad-FF",
    group =
"""
1 *3 N3s u1 {2,S} {3,S}
2    F1s u0 {1,S}
3    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1210,
    label = "NH2_rad-FCl",
    group =
"""
1 *3 N3s  u1 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1211,
    label = "NH2_rad-FBr",
    group =
"""
1 *3 N3s  u1 {2,S} {3,S}
2    F1s  u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1212,
    label = "NH2_rad-ClCl",
    group =
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1213,
    label = "NH2_rad-ClBr",
    group =
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1214,
    label = "NH2_rad-BrBr",
    group =
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Br1s u0 {1,S}
3    Br1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1215,
    label = "N3s_rad_pri-H_or_Val7-1",
    group =
"""
1 *3 N3s      u1 {2,S} {3,S}
2    [H,Val7] u0 {1,S}
3    R!H!Val7      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1216,
    label = "N3s_rad_pri",
    group =
"""
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1217,
    label = "N3s_rad_pri-F",
    group =
"""
1 *3 N3s u1 {2,S} {3,S}
2    F1s u0 {1,S}
3    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1218,
    label = "N3s_rad_pri-Cl",
    group =
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Cl1s u0 {1,S}
3    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1219,
    label = "N3s_rad_pri-Br",
    group =
"""
1 *3 N3s  u1 {2,S} {3,S}
2    Br1s u0 {1,S}
3    R!H!Val7  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1220,
    label = "N3s_rad_sec",
    group =
"""
1 *3 N3s u1 {2,S} {3,S}
2    R!H!Val7 u0 {1,S}
3    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1221,
    label = "N3d_rad",
    group =
"""
1 *3 N3d u1 {2,D}
2    R!H!Val7 u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1222,
    label = "N3d_rad/OneDe",
    group =
"""
1 *3 N3d      u1 {2,D}
2    [Cd,Cdd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1223,
    label = "N3d_rad/OneDeC",
    group =
"""
1 *3 N3d u1 {2,D}
2    Cdd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1224,
    label = "N3d_rad/OneDeCdd_O",
    group =
"""
1    Cdd u0 {2,D} {3,D}
2 *3 N3d u1 {1,D}
3    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 1225,
    label = "N5_rad",
    group =
"""
1 *3 [N5sc,N5dc,N5tc] u1
""",
    kinetics = None,
)

entry(
    index = 1226,
    label = "N5dc_rad",
    group =
"""
1 *3 N5dc u1
""",
    kinetics = None,
)

entry(
    index = 1227,
    label = "Val7_rad",
    group =
"""
1 *3 Val7 u1
""",
    kinetics = None,
)

entry(
    index = 1228,
    label = "F_rad",
    group =
"""
1 *3 F1s u1
""",
    kinetics = None,
)

entry(
    index = 1229,
    label = "Cl_rad",
    group =
"""
1 *3 Cl1s u1
""",
    kinetics = None,
)

entry(
    index = 1230,
    label = "Br_rad",
    group =
"""
1 *3 Br1s u1
""",
    kinetics = None,
)

entry(
   index = 1231,
   label = "I_rad",
   group =
"""
1 *3 I1s u1
""",
    kinetics = None,
)

entry(
    index = 1232,
    label = "HI",
    group =
"""
1 *1 I1s u0 {2,S}
2 *2 H u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: X_H_or_Xrad_H_Xbirad_H_Xtrirad_H
    L2: Xtrirad_H
        L3: C_doublet_H
        L3: C_quartet_H
    L2: Xbirad_H
        L3: C/H_or_Val7/2_triplet_/H_or_Val7/
            L4: CH2_triplet_H
            L4: CH2_triplet_H-F
            L4: CH2_triplet_H-Cl
            L4: CH2_triplet_H-Br
        L3: C/H_or_Val7/2_singlet_/H_or_Val7/
            L4: CH2_singlet_H
            L4: CH2_singlet_H-F
            L4: CH2_singlet_H-Cl
            L4: CH2_singlet_H-Br
        L3: NH_triplet_H
        L3: NH_singlet_H
    L2: Xrad_H
        L3: C_rad_H
            L4: C/H_or_Val7/3_rad_/H_or_Val7/
                L5: CH3_rad_H
                L5: CH3_rad_H-HF
                L5: CH3_rad_H-HCl
                L5: CH3_rad_H-HBr
                L5: CH3_rad_H-FF
                L5: CH3_rad_H-FCl
                L5: CH3_rad_H-FBr
                L5: CH3_rad_H-ClCl
                L5: CH3_rad_H-ClBr
                L5: CH3_rad_H-BrBr
            L4: Cs/H_or_Val7/2/OneDeN
                L5: Cs/H2/OneDeN
                L5: Cs/H2/OneDeN-F
                L5: Cs/H2/OneDeN-Cl
                L5: Cs/H2/OneDeN-Br
        L3: OH_rad_H
        L3: Srad_H
        L3: N3s_rad_H
            L4: N/H_or_Val7/2_rad_/H_or_Val7/
                L5: NH2_rad_H
                L5: NH2_rad_H-F
                L5: NH2_rad_H-Cl
                L5: NH2_rad_H-Br
            L4: N3s_rad_H_pri
                L5: N3s_rad_H/H/NonDeN
        L3: N5sc_radH
    L2: X_H
        L3: H2
        L3: Ct_H
            L4: Ct/H/NonDeC
            L4: Ct/H/NonDeN
        L3: O_H
            L4: O_pri-H_or_Val7-1
                L5: O_pri
                L5: O_pri-F
                L5: O_pri-Cl
                L5: O_pri-Br
            L4: O_sec
                L5: O/H/NonDeC
                L5: O/H/NonDeO
                    L6: /H_or_Val7/2O2
                        L7: H2O2
                        L7: H2O2-F
                        L7: H2O2-Cl
                        L7: H2O2-Br
                    L6: ROO/H_or_Val7/_pri
                        L7: ROOH_pri
                    L6: ROO/H_or_Val7/_sec
                        L7: ROOH_sec
                        L7: ROOH_sec-F
                        L7: ROOH_sec-Cl
                        L7: ROOH_sec-Br
                    L6: ROOH_ter
                L5: O/H/NonDeN
                L5: O/H/OneDe
                    L6: O/H/OneDeC
                    L6: O/H/OneDeN
        L3: OSrad_O_H
            L4: Orad_O_H
            L4: Srad_O_H
        L3: S_H
            L4: S_pri-H_or_Val7-1
                L5: S_pri
                L5: S_pri-F
                L5: S_pri-Cl
                L5: S_pri-Br
            L4: S/H/single
                L5: S/H/NonDeC
                L5: S/H/NonDeS
                L5: S/H/NonDeN
                L5: S/H/NonDeO
                L5: S/H/OneDe
                    L6: S/H/Ct
                    L6: S/H/Cb
                    L6: S/H/CO
                    L6: S/H/Cd
                    L6: S/H/CS
            L4: S/H/Rad
                L5: S/H/CRad
                L5: S/H/SRad
                L5: S/H/NRad
                L5: S/H/ORad
                L5: S/H/MulBondRad
                    L6: S/H/CORad
                    L6: S/H/CdRad
                    L6: S/H/CSRad
            L4: S/H/double
                L5: S/H/double_val4
                    L6: S/H/double_val4C
                    L6: S/H/double_val4N
                    L6: S/H/double_val4S
                    L6: S/H/double_val4O
                L5: S/H/double_val6
                    L6: S/H/double_val6C
                    L6: S/H/double_val6N
                    L6: S/H/double_val6S
                    L6: S/H/double_val6O
                L5: S/H/twoDoubles
                    L6: S/H/twoDoublesOO
            L4: S/H/triple
                L5: S/H/triple_val4
                    L6: S/H/triple_val4C
                    L6: S/H/triple_val4N
                    L6: S/H/triple_val4S
                L5: S/H/triple_val6
                    L6: S/H/triple_val6C
                    L6: S/H/triple_val6N
                    L6: S/H/triple_val6S
        L3: Cd_H
            L4: Cd_pri-H_or_Val7-1
                L5: Cd_pri
                    L6: Cd/H2/NonDeC
                    L6: Cd/H2/NonDeN
                L5: Cd_pri-F
                    L6: Cd/H2/NonDeC-F
                    L6: Cd/H2/NonDeN-F
                L5: Cd_pri-Cl
                    L6: Cd/H2/NonDeC-Cl
                    L6: Cd/H2/NonDeN-Cl
                L5: Cd_pri-Br
                    L6: Cd/H2/NonDeC-Br
                    L6: Cd/H2/NonDeN-Br
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/NonDeS
                L5: Cd/H/NonDeN
                L5: Cd/H/OneDe
                    L6: Cd/H/Ct
                    L6: Cd/H/Cb
                    L6: Cd/H/CO
                    L6: Cd/H/Cd
                    L6: Cd/H/CS
                    L6: Cd/H/DeN
            L4: Cd_allenic
                L5: Cd_Cdd/H_or_Val7/2
                    L6: Cd_Cdd/H2
                    L6: Cd_Cdd/H2-F
                    L6: Cd_Cdd/H2-Cl
                    L6: Cd_Cdd/H2-Br
        L3: Cb_H
        L3: CO_H
            L4: CO_pri-H_or_Val7-1
                L5: CO_pri
                L5: CO_pri-F
                L5: CO_pri-Cl
                L5: CO_pri-Br
            L4: CO_sec
                L5: CO/H/NonDe
                    L6: CO/H/Cs
                        L7: CO/H/Cs\Cs|Cs
                L5: CO/H/OneDe
        L3: CS_H
            L4: CS_pri-H_or_Val7-1
                L5: CS_pri
                L5: CS_pri-F
                L5: CS_pri-Cl
                L5: CS_pri-Br
            L4: CS_sec
                L5: CS/H/NonDeC
                L5: CS/H/NonDeO
                L5: CS/H/NonDeS
                L5: CS/H/OneDe
                    L6: CS/H/Ct
                    L6: CS/H/Cb
                    L6: CS/H/CO
                    L6: CS/H/Cd
                    L6: CS/H/CS
        L3: Cs_H
            L4: C_methane-H_or_Val7-3
                L5: C_methane
                L5: C_methane-HHF
                L5: C_methane-HHCl
                L5: C_methane-HHBr
                L5: C_methane-HFF
                L5: C_methane-HFCl
                L5: C_methane-HFBr
                L5: C_methane-HClCl
                L5: C_methane-HClBr
                L5: C_methane-HBrBr
                L5: C_methane-FFF
                L5: C_methane-FFCl
                L5: C_methane-FFBr
                L5: C_methane-FClCl
                L5: C_methane-FClBr
                L5: C_methane-FBrBr
                L5: C_methane-ClClCl
                L5: C_methane-ClClBr
                L5: C_methane-ClBrBr
                L5: C_methane-BrBrBr
            L4: C_pri-H_or_Val7-2
                L5: C_pri
                    L6: C/H3/Cs
                        L7: C/H3/Cs\H3
                        L7: C/H3/Cs\OneNonDe
                            L8: C/H3/Cs\H2\Cs
                                L9: C/H3/Cs\H2\Cs|O
                            L8: C/H3/Cs\H2\O
                        L7: C/H3/Cs\TwoNonDe
                            L8: C/H3/Cs\H\Cs\O
                            L8: C/H3/Cs\H\Cs\Cs|O
                        L7: C/H3/Cs\TwoDe
                            L8: 1_methyl_CPD
                    L6: C/H3/O
                    L6: C/H3/S
                    L6: C/H3/OneDe
                        L7: C/H3/Ct
                        L7: C/H3/Cb
                        L7: C/H3/CO
                        L7: C/H3/CS
                        L7: C/H3/Cd
                            L8: 2_methyl_CPD
                            L8: 3_methyl_CPD
                            L8: C/H3/Cd\H_Cd\H2
                            L8: C/H3/Cd\H_Cd\H\Cs
                            L8: C/H3/Cd\Cs_Cd\H2
                    L6: Cs/H3/NonDeN
                    L6: Cs/H3/OneDeN
                L5: C_pri-HF
                    L6: C/H3/O-HF
                    L6: C/H3/S-HF
                    L6: C/H3/OneDe-HF
                        L7: C/H3/Ct-HF
                        L7: C/H3/Cb-HF
                        L7: C/H3/CO-HF
                        L7: C/H3/CS-HF
                        L7: C/H3/Cd-HF
                    L6: Cs/H3/NonDeN-HF
                    L6: Cs/H3/OneDeN-HF
                L5: C_pri-HCl
                    L6: C/H3/Cs-HCl
                    L6: C/H3/O-HCl
                    L6: C/H3/S-HCl
                    L6: C/H3/OneDe-HCl
                        L7: C/H3/Ct-HCl
                        L7: C/H3/Cb-HCl
                        L7: C/H3/CO-HCl
                        L7: C/H3/CS-HCl
                        L7: C/H3/Cd-HCl
                    L6: Cs/H3/NonDeN-HCl
                    L6: Cs/H3/OneDeN-HCl
                L5: C_pri-HBr
                    L6: C/H3/Cs-HBr
                        L7: C/H3/Cs\H3-HBrBrBrBr
                        L7: C/H3/Cs\OneNonDe-HBrBrBr
                            L8: C/H3/Cs\H2\Cs-HBrBrBr
                            L8: C/H3/Cs\H2\O-HBrBrBr
                        L7: C/H3/Cs\TwoNonDe-HBrBr
                            L8: C/H3/Cs\H\Cs\O-HBrBr
                            L8: C/H3/Cs\H\Cs\Cs|O-HBrBr
                        L7: C/H3/Cs\TwoDe-HBrBr
                            L8: 1_methyl_CPD-HBrBr
                        L7: C/H3/Cs\H2\Cs|O-HHHBr
                    L6: C/H3/O-HBr
                    L6: C/H3/S-HBr
                    L6: C/H3/OneDe-HBr
                        L7: C/H3/Ct-HBr
                        L7: C/H3/Cb-HBr
                        L7: C/H3/CO-HBr
                        L7: C/H3/CS-HBr
                        L7: C/H3/Cd-HBr
                            L8: 2_methyl_CPD-HBr
                            L8: 3_methyl_CPD-HBr
                            L8: C/H3/Cd\H_Cd\H2-HBrBrBrBr
                            L8: C/H3/Cd\H_Cd\H\Cs-HBrBrBr
                            L8: C/H3/Cd\Cs_Cd\H2-HBrBrBr
                    L6: Cs/H3/NonDeN-HBr
                    L6: Cs/H3/OneDeN-HBr
                L5: C_pri-FF
                    L6: C/H3/O-FF
                    L6: C/H3/S-FF
                    L6: C/H3/OneDe-FF
                        L7: C/H3/Ct-FF
                        L7: C/H3/Cb-FF
                        L7: C/H3/CO-FF
                        L7: C/H3/CS-FF
                        L7: C/H3/Cd-FF
                    L6: Cs/H3/NonDeN-FF
                    L6: Cs/H3/OneDeN-FF
                    L6: C/H3/Cs\H2\Cs|O-FFFF
                L5: C_pri-FCl
                    L6: C/H3/Cs-FCl
                    L6: C/H3/O-FCl
                    L6: C/H3/S-FCl
                    L6: C/H3/OneDe-FCl
                        L7: C/H3/Ct-FCl
                        L7: C/H3/Cb-FCl
                        L7: C/H3/CO-FCl
                        L7: C/H3/CS-FCl
                        L7: C/H3/Cd-FCl
                    L6: Cs/H3/NonDeN-FCl
                    L6: Cs/H3/OneDeN-FCl
                L5: C_pri-FBr
                    L6: C/H3/Cs-FBr
                        L7: C/H3/Cs\H2\Cs-FBrBrBr
                        L7: C/H3/Cs\H2\O-FBrBrBr
                        L7: C/H3/Cs\H\Cs\O-FBrBr
                        L7: C/H3/Cs\H\Cs\Cs|O-FBrBr
                        L7: 1_methyl_CPD-FBrBr
                    L6: C/H3/O-FBr
                    L6: C/H3/S-FBr
                    L6: C/H3/OneDe-FBr
                        L7: C/H3/Ct-FBr
                        L7: C/H3/Cb-FBr
                        L7: C/H3/CO-FBr
                        L7: C/H3/CS-FBr
                        L7: C/H3/Cd-FBr
                            L8: 2_methyl_CPD-FBr
                            L8: 3_methyl_CPD-FBr
                            L8: C/H3/Cd\H_Cd\H2-FBrBrBrBr
                            L8: C/H3/Cd\H_Cd\H\Cs-FBrBrBr
                            L8: C/H3/Cd\Cs_Cd\H2-FBrBrBr
                    L6: Cs/H3/NonDeN-FBr
                    L6: Cs/H3/OneDeN-FBr
                L5: C_pri-ClCl
                    L6: C/H3/Cs-ClCl
                        L7: C/H3/Cs\H2\Cs|O-ClClClCl
                    L6: C/H3/O-ClCl
                    L6: C/H3/S-ClCl
                    L6: C/H3/OneDe-ClCl
                        L7: C/H3/Ct-ClCl
                        L7: C/H3/Cb-ClCl
                        L7: C/H3/CO-ClCl
                        L7: C/H3/CS-ClCl
                        L7: C/H3/Cd-ClCl
                    L6: Cs/H3/NonDeN-ClCl
                    L6: Cs/H3/OneDeN-ClCl
                L5: C_pri-ClBr
                    L6: C/H3/Cs-ClBr
                        L7: C/H3/Cs\H2\Cs-ClBrBrBr
                        L7: C/H3/Cs\H2\O-ClBrBrBr
                        L7: 1_methyl_CPD-ClBrBr
                        L7: C/H3/Cs\H\Cs\O-ClBrBr
                        L7: C/H3/Cs\H\Cs\Cs|O-ClBrBr
                    L6: C/H3/O-ClBr
                    L6: C/H3/S-ClBr
                    L6: C/H3/OneDe-ClBr
                        L7: C/H3/Ct-ClBr
                        L7: C/H3/Cb-ClBr
                        L7: C/H3/CO-ClBr
                        L7: C/H3/CS-ClBr
                        L7: C/H3/Cd-ClBr
                            L8: 2_methyl_CPD-ClBr
                            L8: 3_methyl_CPD-ClBr
                            L8: C/H3/Cd\H_Cd\H2-ClBrBrBrBr
                            L8: C/H3/Cd\H_Cd\H\Cs-ClBrBrBr
                            L8: C/H3/Cd\Cs_Cd\H2-ClBrBrBr
                    L6: Cs/H3/NonDeN-ClBr
                    L6: Cs/H3/OneDeN-ClBr
                L5: C_pri-BrBr
                    L6: C/H3/Cs-BrBr
                        L7: C/H3/Cs\H2\Cs-BrBrBrBr
                            L8: C/H3/Cs\H2\Cs|O-BrBrBrBr
                        L7: C/H3/Cs\H2\O-BrBrBrBr
                        L7: 1_methyl_CPD-BrBrBr
                        L7: C/H3/Cs\H\Cs\O-BrBrBr
                        L7: C/H3/Cs\H\Cs\Cs|O-BrBrBr
                    L6: C/H3/O-BrBr
                    L6: C/H3/S-BrBr
                    L6: C/H3/OneDe-BrBr
                        L7: C/H3/Ct-BrBr
                        L7: C/H3/Cb-BrBr
                        L7: C/H3/CO-BrBr
                        L7: C/H3/CS-BrBr
                        L7: C/H3/Cd-BrBr
                            L8: 2_methyl_CPD-BrBr
                            L8: 3_methyl_CPD-BrBr
                            L8: C/H3/Cd\H_Cd\H2-BrBrBrBrBr
                            L8: C/H3/Cd\H_Cd\H\Cs-BrBrBrBr
                            L8: C/H3/Cd\Cs_Cd\H2-BrBrBrBr
                    L6: Cs/H3/NonDeN-BrBr
                    L6: Cs/H3/OneDeN-BrBr
            L4: C_sec-H_or_Val7-1
                L5: C_sec
                    L6: C/H2/NonDeC
                        L7: C/H2/Cs/Cs\O
                        L7: C/H2/Cs/Cs\Cs|O
                        L7: C/H2/NonDeC_5ring
                            L8: C/H2/NonDeC_5ring_fused6_1
                            L8: C/H2/NonDeC_5ring_fused6_2
                            L8: C/H2/NonDeC_5ring_alpha6ring
                            L8: C/H2/NonDeC_5ring_beta6ring
                        L7: C/H2/Cs\H3/Cs\H3
                    L6: C/H2/NonDeO
                        L7: C/H2/CsO
                            L8: C/H2/Cs\Cs2/O
                        L7: C/H2/O2
                    L6: C/H2/NonDeS
                        L7: C/H2/CsS
                    L6: C/H2/NonDeN
                    L6: C/H2/OneDe
                        L7: C/H2/OneDeC
                            L8: C/H2/CtCs
                            L8: C/H2/CbCs
                            L8: C/H2/COCs
                                L9: C/H2/CO\H/Cs\H3
                            L8: C/H2/CdCs
                                L9: C/H2/Cd\H_Cd\H2/Cs\H3
                            L8: C/H2/CSCs
                        L7: C/H2/OneDeO
                        L7: C/H2/OneDeS
                            L8: C/H2/CbS
                            L8: C/H2/CtS
                            L8: C/H2/CdS
                            L8: C/H2/CSS
                    L6: C/H2/TwoDe
                        L7: C/H2/CtCt
                        L7: C/H2/CtCb
                        L7: C/H2/CtCO
                        L7: C/H2/CbCb
                        L7: C/H2/CbCO
                        L7: C/H2/COCO
                        L7: C/H2/CdCt
                        L7: C/H2/CtCS
                        L7: C/H2/CdCb
                        L7: C/H2/CbCS
                        L7: C/H2/CdCO
                        L7: C/H2/COCS
                        L7: C/H2/CdCd
                        L7: C/H2/CdCS
                        L7: C/H2/CSCS
                L5: C_sec-F
                    L6: C/H2/NonDeC-F
                        L7: C/H2/NonDeC_5ring_fused6_1-F
                        L7: C/H2/NonDeC_5ring_fused6_2-F
                        L7: C/H2/NonDeC_5ring_alpha6ring-F
                        L7: C/H2/NonDeC_5ring_beta6ring-F
                    L6: C/H2/NonDeO-F
                        L7: C/H2/CsO-F
                        L7: C/H2/O2-F
                    L6: C/H2/NonDeS-F
                        L7: C/H2/CsS-F
                    L6: C/H2/NonDeN-F
                    L6: C/H2/OneDe-F
                        L7: C/H2/OneDeC-F
                            L8: C/H2/CtCs-F
                            L8: C/H2/CbCs-F
                            L8: C/H2/COCs-F
                            L8: C/H2/CdCs-F
                            L8: C/H2/CSCs-F
                        L7: C/H2/OneDeO-F
                        L7: C/H2/OneDeS-F
                            L8: C/H2/CbS-F
                            L8: C/H2/CtS-F
                            L8: C/H2/CdS-F
                            L8: C/H2/CSS-F
                    L6: C/H2/TwoDe-F
                L5: C_sec-Cl
                    L6: C/H2/NonDeC-Cl
                        L7: C/H2/NonDeC_5ring_fused6_1-Cl
                        L7: C/H2/NonDeC_5ring_fused6_2-Cl
                        L7: C/H2/NonDeC_5ring_alpha6ring-Cl
                        L7: C/H2/NonDeC_5ring_beta6ring-Cl
                    L6: C/H2/NonDeO-Cl
                        L7: C/H2/CsO-Cl
                        L7: C/H2/O2-Cl
                    L6: C/H2/NonDeS-Cl
                        L7: C/H2/CsS-Cl
                    L6: C/H2/NonDeN-Cl
                    L6: C/H2/OneDe-Cl
                        L7: C/H2/OneDeC-Cl
                            L8: C/H2/CtCs-Cl
                            L8: C/H2/CbCs-Cl
                            L8: C/H2/COCs-Cl
                                L9: C/H2/CO\H/Cs\H3-ClClClClCl
                                L9: C/H2/CO\H/Cs\H3-ClClClClBr
                                L9: C/H2/CO\H/Cs\H3-ClClClBrBr
                                L9: C/H2/CO\H/Cs\H3-ClClBrBrBr
                                L9: C/H2/CO\H/Cs\H3-ClBrBrBrBr
                            L8: C/H2/CdCs-Cl
                            L8: C/H2/CSCs-Cl
                        L7: C/H2/OneDeO-Cl
                        L7: C/H2/OneDeS-Cl
                            L8: C/H2/CbS-Cl
                            L8: C/H2/CtS-Cl
                            L8: C/H2/CdS-Cl
                            L8: C/H2/CSS-Cl
                    L6: C/H2/TwoDe-Cl
                L5: C_sec-Br
                    L6: C/H2/NonDeC-Br
                        L7: C/H2/Cs/Cs\O-Br
                        L7: C/H2/Cs/Cs\Cs|O-Br
                        L7: C/H2/NonDeC_5ring-Br
                            L8: C/H2/NonDeC_5ring_fused6_1-Br
                            L8: C/H2/NonDeC_5ring_fused6_2-Br
                            L8: C/H2/NonDeC_5ring_alpha6ring-Br
                            L8: C/H2/NonDeC_5ring_beta6ring-Br
                        L7: C/H2/Cs\H3/Cs\H3-BrBrBrBrBrBrBr
                    L6: C/H2/NonDeO-Br
                        L7: C/H2/CsO-Br
                            L8: C/H2/Cs\Cs2/O-HBrBrBrBrBrBrBrBr
                            L8: C/H2/Cs\Cs2/O-FBrBrBrBrBrBrBrBr
                            L8: C/H2/Cs\Cs2/O-ClBrBrBrBrBrBrBrBr
                            L8: C/H2/Cs\Cs2/O-BrBrBrBrBrBrBrBrBr
                        L7: C/H2/O2-Br
                    L6: C/H2/NonDeS-Br
                        L7: C/H2/CsS-Br
                    L6: C/H2/NonDeN-Br
                    L6: C/H2/OneDe-Br
                        L7: C/H2/OneDeC-Br
                            L8: C/H2/CtCs-Br
                            L8: C/H2/CbCs-Br
                            L8: C/H2/COCs-Br
                                L9: C/H2/CO\H/Cs\H3-BrBrBrBrBr
                            L8: C/H2/CdCs-Br
                                L9: C/H2/Cd\H_Cd\H2/Cs\H3-BrBrBrBrBrBrBr
                            L8: C/H2/CSCs-Br
                        L7: C/H2/OneDeO-Br
                        L7: C/H2/OneDeS-Br
                            L8: C/H2/CbS-Br
                            L8: C/H2/CtS-Br
                            L8: C/H2/CdS-Br
                            L8: C/H2/CSS-Br
                    L6: C/H2/TwoDe-Br
            L4: C_ter
                L5: C/H/NonDe
                    L6: C/H/Cs3
                        L7: C/H_or_Val7/Cs2/Cs\O
                            L8: C/H/Cs2/Cs\O
                        L7: C/H_or_Val7/Cs2/Cs\Cs|O
                            L8: C/H/Cs2/Cs\Cs|O
                        L7: C/H/Cs3_5ring
                            L8: C/H/Cs3_5ring_fused6
                            L8: C/H/Cs3_5ring_adj5
                    L6: C/H/Cs2N
                    L6: C/H/NDMustO
                        L7: C/H/Cs2O
                        L7: C/H/CsO2
                        L7: C/H/O3
                    L6: C/H/NDMustS
                        L7: C/H/Cs2S
                        L7: C/H/CsS2
                        L7: C/H/S3
                    L6: C/H/NDMustOS
                        L7: C/H/CsOS
                L5: C/H/OneDe
                    L6: C/H/Cs2
                        L7: C/H/Cs2Ct
                        L7: C/H/Cs2Cb
                        L7: C/H/Cs2CO
                        L7: C/H/Cs2Cd
                        L7: C/H/Cs2CS
                    L6: C/H/CsO
                    L6: C/H/CsS
                        L7: C/H/CbCsS
                        L7: C/H/CtCsS
                        L7: C/H/CdCsS
                        L7: C/H/CSCsS
                    L6: C/H/OO
                    L6: C/H/OS
                    L6: C/H/SS
                L5: C/H/TwoDe
                    L6: C/H/Cs
                        L7: C/H/CtCt
                        L7: C/H/CtCb
                        L7: C/H/CtCO
                        L7: C/H/CbCb
                        L7: C/H/CbCO
                        L7: C/H/COCO
                        L7: C/H/CdCt
                        L7: C/H/CtCS
                        L7: C/H/CdCb
                        L7: C/H/CbCS
                        L7: C/H/CdCO
                        L7: C/H/COCS
                        L7: C/H/CdCd
                        L7: C/H/CdCS
                        L7: C/H/CSCS
                    L6: C/H/TDMustO
                    L6: C/H/TDMustS
                L5: C/H/ThreeDe
        L3: N3_H
            L4: N3s_H
                L5: N/H_or_Val7/3
                    L6: NH3
                    L6: NH3-HF
                    L6: NH3-HCl
                    L6: NH3-HBr
                    L6: NH3-FF
                    L6: NH3-FCl
                    L6: NH3-FBr
                    L6: NH3-ClCl
                    L6: NH3-ClBr
                    L6: NH3-BrBr
                L5: N3s_pri_/H_or_Val7/
                    L6: N3s_pri_H
                        L7: N3s/H2/NonDe
                            L8: N3s/H2/NonDeC
                            L8: N3s/H2/NonDeO
                            L8: N3s/H2/NonDeN
                        L7: N3s/H2/OneDe
                            L8: N3s/H2/OneDeN
                    L6: N3s_pri_H-F
                        L7: N3s/H2/NonDe-F
                            L8: N3s/H2/NonDeC-F
                            L8: N3s/H2/NonDeO-F
                            L8: N3s/H2/NonDeN-F
                        L7: N3s/H2/OneDe-F
                            L8: N3s/H2/OneDeN-F
                    L6: N3s_pri_H-Cl
                        L7: N3s/H2/NonDe-Cl
                            L8: N3s/H2/NonDeC-Cl
                            L8: N3s/H2/NonDeO-Cl
                            L8: N3s/H2/NonDeN-Cl
                        L7: N3s/H2/OneDe-Cl
                            L8: N3s/H2/OneDeN-Cl
                    L6: N3s_pri_H-Br
                        L7: N3s/H2/NonDe-Br
                            L8: N3s/H2/NonDeC-Br
                            L8: N3s/H2/NonDeO-Br
                            L8: N3s/H2/NonDeN-Br
                        L7: N3s/H2/OneDe-Br
                            L8: N3s/H2/OneDeN-Br
                L5: N3s_sec_H
            L4: N3d_H
                L5: N3d/H/NonDe
                    L6: N3d/H/NonDeC
                    L6: N3d/H/NonDeO
                    L6: N3d/H/NonDeN
                L5: N3d/H/OneDe
                    L6: N3d/H/CddO
        L3: N5_H
            L4: N5dc_H
                L5: N5dc/H/NonDeOO
        L3: HCl
        L3: HI
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
    L2: Y_1centerbirad
        L3: O_atom_triplet
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
        L3: N/H_or_Val7/_triplet
            L4: NH_triplet
            L4: NH_triplet-F
            L4: NH_triplet-Cl
            L4: NH_triplet-Br
    L2: Y_rad
        L3: H_rad
        L3: Y_2centeradjbirad
            L4: O2b
            L4: S2b
            L4: C2b
        L3: Ct_rad
            L4: Ct_rad/Ct
            L4: Ct_rad/N
        L3: O_rad
            L4: O_pri_rad-H_or_Val7-1
                L5: O_pri_rad
                L5: O_pri_rad-F
                L5: O_pri_rad-Cl
                L5: O_pri_rad-Br
            L4: O_sec_rad
                L5: O_rad/NonDeC
                    L6: O_rad/Cs\/H_or_Val7/2\Cs|/H_or_Val7/|Cs2
                        L7: O_rad/Cs\H2\Cs|H|Cs2
                L5: O_rad/NonDeO
                    L6: OOC
                L5: O_rad/NonDeN
                L5: O_rad/OneDe
                    L6: O_rad/OneDeC
                        L7: O_rad/Cd
                            L8: O_rad/Cd\Cs_Cd\Cs2
                            L8: O_rad/Cd\H_Cd\H\Cs
                            L8: O_rad/Cd\H_Cd\H2
                            L8: O_rad/Cd\H_Cd\Cs2
                            L8: O_rad/Cd\H_Cd\Cs2-F
                            L8: O_rad/Cd\H_Cd\Cs2-Cl
                            L8: O_rad/Cd\H_Cd\Cs2-Br
                            L8: O_rad/Cd\Cs_Cd\H2
                            L8: O_rad/Cd\Cs_Cd\H\Cs
                            L8: O_rad/Cd\Cs_Cd\H\Cs-F
                            L8: O_rad/Cd\Cs_Cd\H\Cs-Cl
                            L8: O_rad/Cd\Cs_Cd\H\Cs-Br
                    L6: O_rad/OneDeN
                        L7: InChI=1S/NO3/c2-1(3)4
        L3: S_rad
            L4: S_pri_rad-H_or_Val7-1
                L5: S_pri_rad
                L5: S_pri_rad-F
                L5: S_pri_rad-Cl
                L5: S_pri_rad-Br
            L4: S_rad/single
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/NonDeN
                L5: S_rad/NonDeO
                L5: S_rad/OneDe
                    L6: S_rad/Ct
                    L6: S_rad/Cb
                    L6: S_rad/CO
                    L6: S_rad/Cd
                    L6: S_rad/CS
            L4: S_rad/double
                L5: S_rad/double_val4
                    L6: S_rad/double_val4C
                    L6: S_rad/double_val4N
                    L6: S_rad/double_val4S
                    L6: S_rad/double_val4O
                L5: S_rad/double_val6
                    L6: S_rad/double_val6C
                    L6: S_rad/double_val6N
                    L6: S_rad/double_val6S
                    L6: S_rad/double_val6O
                L5: S_rad/twoDoubles
                    L6: S_rad/twoDoublesOO
            L4: S_rad/triple
                L5: S_rad/triple_val4
                    L6: S_rad/triple_val4C
                    L6: S_rad/triple_val4N
                    L6: S_rad/triple_val4S
                L5: S_rad/triple_val6
                    L6: S_rad/triple_val6C
                    L6: S_rad/triple_val6N
                    L6: S_rad/triple_val6S
        L3: Cd_rad
            L4: Cd_pri_rad-H_or_Val7-1
                L5: Cd_pri_rad
                    L6: Cd_Cd\H2_pri_rad
                    L6: Cd_Cd\H\Cs_pri_rad
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad
                    L6: Cd_Cd\Cs2_pri_rad
                L5: Cd_pri_rad-F
                    L6: Cd_Cd\H2_pri_rad-HHF
                    L6: Cd_Cd\H2_pri_rad-HFF
                    L6: Cd_Cd\H2_pri_rad-FFF
                    L6: Cd_Cd\H\Cs_pri_rad-HF
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-HHHF
                    L6: Cd_Cd\H\Cs_pri_rad-FF
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-HHFF
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-HFFF
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-FFFF
                    L6: Cd_Cd\Cs2_pri_rad-F
                L5: Cd_pri_rad-Cl
                    L6: Cd_Cd\H2_pri_rad-HHCl
                    L6: Cd_Cd\H2_pri_rad-HFCl
                    L6: Cd_Cd\H2_pri_rad-HClCl
                    L6: Cd_Cd\H2_pri_rad-FFCl
                    L6: Cd_Cd\H2_pri_rad-FClCl
                    L6: Cd_Cd\H2_pri_rad-ClClCl
                    L6: Cd_Cd\H\Cs_pri_rad-HCl
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-HHHCl
                    L6: Cd_Cd\H\Cs_pri_rad-FCl
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-HHFCl
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-HFFCl
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-FFFCl
                    L6: Cd_Cd\H\Cs_pri_rad-ClCl
                    L6: Cd_Cd\Cs2_pri_rad-Cl
                L5: Cd_pri_rad-Br
                    L6: Cd_Cd\H2_pri_rad-HHBr
                    L6: Cd_Cd\H2_pri_rad-HFBr
                    L6: Cd_Cd\H2_pri_rad-HClBr
                    L6: Cd_Cd\H2_pri_rad-HBrBr
                    L6: Cd_Cd\H2_pri_rad-FFBr
                    L6: Cd_Cd\H2_pri_rad-FClBr
                    L6: Cd_Cd\H2_pri_rad-FBrBr
                    L6: Cd_Cd\H2_pri_rad-ClClBr
                    L6: Cd_Cd\H2_pri_rad-ClBrBr
                    L6: Cd_Cd\H2_pri_rad-BrBrBr
                    L6: Cd_Cd\H\Cs_pri_rad-HBr
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-HHHBr
                    L6: Cd_Cd\H\Cs_pri_rad-FBr
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-HHFBr
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-HFFBr
                        L7: Cd_Cd\H\Cs|H2|Cs_pri_rad-FFFBr
                    L6: Cd_Cd\H\Cs_pri_rad-ClBr
                    L6: Cd_Cd\H\Cs_pri_rad-BrBr
                    L6: Cd_Cd\Cs2_pri_rad-Br
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                    L6: Cd_Cd\/H_or_Val7/2_rad/Cs
                        L7: Cd_Cd\H2_rad/Cs
                    L6: Cd_Cd\/H_or_Val7/\Cs_rad/Cs
                        L7: Cd_Cd\H\Cs_rad/Cs
                L5: Cd_rad/NonDeO
                L5: Cd_rad/NonDeS
                L5: Cd_rad/NonDeN
                L5: Cd_rad/OneDe
                    L6: Cd_rad/Ct
                    L6: Cd_rad/Cb
                    L6: Cd_rad/CO
                    L6: Cd_rad/Cd
                    L6: Cd_rad/CS
            L4: Cd_allenic_rad
                L5: Cd_Cdd_rad/H_or_Val7/
                    L6: Cd_Cdd_rad/H
                    L6: Cd_Cdd_rad/H-F
                    L6: Cd_Cdd_rad/H-Cl
                    L6: Cd_Cdd_rad/H-Br
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad-H_or_Val7-1
                L5: CO_pri_rad
                L5: CO_pri_rad-F
                L5: CO_pri_rad-Cl
                L5: CO_pri_rad-Br
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                    L6: CO_rad/Cs
                L5: CO_rad/OneDe
        L3: CS_rad
            L4: CS_pri_rad-H_or_Val7-1
                L5: CS_pri_rad
                L5: CS_pri_rad-F
                L5: CS_pri_rad-Cl
                L5: CS_pri_rad-Br
            L4: CS_sec_rad
                L5: CS_rad/NonDe
                    L6: CS_rad/Cs
                    L6: CS_rad/O
                    L6: CS_rad/S
                L5: CS_rad/OneDe
                    L6: CS_rad/Ct
                    L6: CS_rad/Cb
                    L6: CS_rad/CO
                    L6: CS_rad/Cd
                    L6: CS_rad/CS
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
                        L7: C_rad/H2/Cs\H3
                        L7: C_rad/H2/Cs\Cs2\O
                        L7: C_rad/H2/Cs\H\Cs\Cs|O
                        L7: C_rad/H2/Cs\H\Cs|Cs\O
                        L7: C_rad/H2/Cs\H2\Cs|Cs|O
                        L7: C_rad/H2/Cs\H2\Cs|Cs#O
                    L6: C_rad/H2/Ct
                    L6: C_rad/H2/Cb
                    L6: C_rad/H2/CO
                    L6: C_rad/H2/CS
                    L6: C_rad/H2/O
                    L6: C_rad/H2/S
                    L6: C_rad/H2/Cd
                        L7: C_rad/H2/Cd\H_Cd\H2
                        L7: C_rad/H2/Cd\H_Cd\H2-HHF
                        L7: C_rad/H2/Cd\H_Cd\H2-HHCl
                        L7: C_rad/H2/Cd\H_Cd\H2-HHBr
                        L7: C_rad/H2/Cd\Cs_Cd\H2
                    L6: C_rad/H2/N
                L5: C_pri_rad-HF
                    L6: C_rad/H2/Cs-HF
                    L6: C_rad/H2/Ct-HF
                    L6: C_rad/H2/Cb-HF
                    L6: C_rad/H2/CO-HF
                    L6: C_rad/H2/CS-HF
                    L6: C_rad/H2/O-HF
                    L6: C_rad/H2/S-HF
                    L6: C_rad/H2/Cd-HF
                        L7: C_rad/H2/Cd\H_Cd\H2-HFF
                        L7: C_rad/H2/Cd\H_Cd\H2-HFCl
                        L7: C_rad/H2/Cd\H_Cd\H2-HFBr
                        L7: C_rad/H2/Cd\Cs_Cd\H2-HHHHHHF
                    L6: C_rad/H2/N-HF
                L5: C_pri_rad-HCl
                    L6: C_rad/H2/Cs-HCl
                    L6: C_rad/H2/Ct-HCl
                    L6: C_rad/H2/Cb-HCl
                    L6: C_rad/H2/CO-HCl
                    L6: C_rad/H2/CS-HCl
                    L6: C_rad/H2/O-HCl
                    L6: C_rad/H2/S-HCl
                    L6: C_rad/H2/Cd-HCl
                        L7: C_rad/H2/Cd\H_Cd\H2-HClCl
                        L7: C_rad/H2/Cd\H_Cd\H2-HClBr
                        L7: C_rad/H2/Cd\Cs_Cd\H2-HHHHHHCl
                    L6: C_rad/H2/N-HCl
                L5: C_pri_rad-HBr
                    L6: C_rad/H2/Cs-HBr
                    L6: C_rad/H2/Ct-HBr
                    L6: C_rad/H2/Cb-HBr
                    L6: C_rad/H2/CO-HBr
                    L6: C_rad/H2/CS-HBr
                    L6: C_rad/H2/O-HBr
                    L6: C_rad/H2/S-HBr
                    L6: C_rad/H2/Cd-HBr
                        L7: C_rad/H2/Cd\H_Cd\H2-HBrBr
                        L7: C_rad/H2/Cd\Cs_Cd\H2-HHHHHHBr
                    L6: C_rad/H2/N-HBr
                L5: C_pri_rad-FF
                    L6: C_rad/H2/Cs-FF
                    L6: C_rad/H2/Ct-FF
                    L6: C_rad/H2/Cb-FF
                    L6: C_rad/H2/CO-FF
                    L6: C_rad/H2/CS-FF
                    L6: C_rad/H2/O-FF
                    L6: C_rad/H2/S-FF
                    L6: C_rad/H2/Cd-FF
                    L6: C_rad/H2/N-FF
                L5: C_pri_rad-FCl
                    L6: C_rad/H2/Cs-FCl
                    L6: C_rad/H2/Ct-FCl
                    L6: C_rad/H2/Cb-FCl
                    L6: C_rad/H2/CO-FCl
                    L6: C_rad/H2/CS-FCl
                    L6: C_rad/H2/O-FCl
                    L6: C_rad/H2/S-FCl
                    L6: C_rad/H2/Cd-FCl
                    L6: C_rad/H2/N-FCl
                L5: C_pri_rad-FBr
                    L6: C_rad/H2/Cs-FBr
                    L6: C_rad/H2/Ct-FBr
                    L6: C_rad/H2/Cb-FBr
                    L6: C_rad/H2/CO-FBr
                    L6: C_rad/H2/CS-FBr
                    L6: C_rad/H2/O-FBr
                    L6: C_rad/H2/S-FBr
                    L6: C_rad/H2/Cd-FBr
                    L6: C_rad/H2/N-FBr
                L5: C_pri_rad-ClCl
                    L6: C_rad/H2/Cs-ClCl
                    L6: C_rad/H2/Ct-ClCl
                    L6: C_rad/H2/Cb-ClCl
                    L6: C_rad/H2/CO-ClCl
                    L6: C_rad/H2/CS-ClCl
                    L6: C_rad/H2/O-ClCl
                    L6: C_rad/H2/S-ClCl
                    L6: C_rad/H2/Cd-ClCl
                    L6: C_rad/H2/N-ClCl
                L5: C_pri_rad-ClBr
                    L6: C_rad/H2/Cs-ClBr
                    L6: C_rad/H2/Ct-ClBr
                    L6: C_rad/H2/Cb-ClBr
                    L6: C_rad/H2/CO-ClBr
                    L6: C_rad/H2/CS-ClBr
                    L6: C_rad/H2/O-ClBr
                    L6: C_rad/H2/S-ClBr
                    L6: C_rad/H2/Cd-ClBr
                    L6: C_rad/H2/N-ClBr
                L5: C_pri_rad-BrBr
                    L6: C_rad/H2/Cs-BrBr
                    L6: C_rad/H2/Ct-BrBr
                    L6: C_rad/H2/Cb-BrBr
                    L6: C_rad/H2/CO-BrBr
                    L6: C_rad/H2/CS-BrBr
                    L6: C_rad/H2/O-BrBr
                    L6: C_rad/H2/S-BrBr
                    L6: C_rad/H2/Cd-BrBr
                    L6: C_rad/H2/N-BrBr
            L4: C_sec_rad-H_or_Val7-1
                L5: C_sec_rad
                    L6: C_rad/H/NonDeC
                        L7: C_rad/H/NonDeC_5ring_fused6_1
                        L7: C_rad/H/NonDeC_5ring_fused6_2
                        L7: C_rad/H/Cs\H3/Cs\H3
                        L7: C_rad/H/NonDeC_5ring_alpha6ring
                        L7: C_rad/H/NonDeC_5ring_beta6ring
                        L7: C_rad/H/Cs\H2\CO/Cs
                        L7: C_rad/H/Cs\H2\Cs/Cs\H2\O
                        L7: C_rad/H/Cs\H\Cs\O/Cs
                        L7: C_rad/H/Cs\H2\Cs|O/Cs
                    L6: C_rad/H/NonDeO
                        L7: C_rad/H/CsO
                            L8: C_rad/H/Cs\H2\Cs/O
                                L9: C_rad/H/Cs\H2\Cs|H2|Cs/O
                                L9: C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHHHHHHF
                                L9: C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHHHHHHCl
                                L9: C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHHHHHHBr
                            L8: C_rad/H/Cs\H\Cs2/O
                            L8: C_rad/H/Cs\H\Cs2/O-HHF
                            L8: C_rad/H/Cs\H\Cs2/O-HHCl
                            L8: C_rad/H/Cs\H\Cs2/O-HHBr
                        L7: C_rad/H/O2
                    L6: C_rad/H/NonDeS
                        L7: C_rad/H/CsS
                        L7: C_rad/H/S2
                    L6: C_rad/H/NonDeCN
                    L6: C_rad/H/NonDeON
                    L6: C_rad/H/NonDeNN
                    L6: C_rad/H/OneDe
                        L7: C_rad/H/OneDeC
                            L8: C_rad/H/CtCs
                            L8: C_rad/H/CbCs
                            L8: C_rad/H/CO/Cs
                                L9: C_rad/H/CO\H/Cs\H3
                                L9: C_rad/H/CO\H/Cs\H3-HHHHF
                                L9: C_rad/H/CO\H/Cs\H3-HHHHCl
                                L9: C_rad/H/CO\H/Cs\H3-HHHHBr
                            L8: C_rad/H/CdCs
                            L8: C_rad/H/CSCs
                        L7: C_rad/H/OneDeO
                        L7: C_rad/H/OneDeS
                            L8: C_rad/H/CtS
                            L8: C_rad/H/CbS
                            L8: C_rad/H/CdS
                            L8: C_rad/H/CSS
                        L7: C_rad/H/OneDeN
                    L6: C_rad/H/TwoDe
                        L7: C_rad/H/CtCt
                        L7: C_rad/H/CtCb
                        L7: C_rad/H/CtCO
                        L7: C_rad/H/CbCb
                        L7: C_rad/H/CbCO
                        L7: C_rad/H/COCO
                        L7: C_rad/H/CdCt
                        L7: C_rad/H/CtCS
                        L7: C_rad/H/CdCb
                        L7: C_rad/H/CbCS
                        L7: C_rad/H/CdCO
                        L7: C_rad/H/COCS
                        L7: C_rad/H/CdCd
                        L7: C_rad/H/CdCS
                        L7: C_rad/H/CSCS
                L5: C_sec_rad-F
                    L6: C_rad/H/NonDeC-F
                    L6: C_rad/H/NonDeO-F
                        L7: C_rad/H/CsO-F
                            L8: C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHFFFFFF
                            L8: C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHFFFFFCl
                            L8: C_rad/H/Cs\H2\Cs|H2|Cs/O-HHHFFFFFBr
                        L7: C_rad/H/O2-F
                    L6: C_rad/H/NonDeS-F
                        L7: C_rad/H/CsS-F
                        L7: C_rad/H/S2-F
                    L6: C_rad/H/NonDeCN-F
                    L6: C_rad/H/NonDeON-F
                    L6: C_rad/H/NonDeNN-F
                    L6: C_rad/H/OneDe-F
                        L7: C_rad/H/OneDeC-F
                            L8: C_rad/H/CtCs-F
                            L8: C_rad/H/CbCs-F
                            L8: C_rad/H/CO/Cs-F
                            L8: C_rad/H/CdCs-F
                            L8: C_rad/H/CSCs-F
                        L7: C_rad/H/OneDeO-F
                        L7: C_rad/H/OneDeS-F
                            L8: C_rad/H/CtS-F
                            L8: C_rad/H/CbS-F
                            L8: C_rad/H/CdS-F
                            L8: C_rad/H/CSS-F
                        L7: C_rad/H/OneDeN-F
                    L6: C_rad/H/TwoDe-F
                L5: C_sec_rad-Cl
                    L6: C_rad/H/NonDeC-Cl
                    L6: C_rad/H/NonDeO-Cl
                        L7: C_rad/H/CsO-Cl
                        L7: C_rad/H/O2-Cl
                    L6: C_rad/H/NonDeS-Cl
                        L7: C_rad/H/CsS-Cl
                        L7: C_rad/H/S2-Cl
                    L6: C_rad/H/NonDeCN-Cl
                    L6: C_rad/H/NonDeON-Cl
                    L6: C_rad/H/NonDeNN-Cl
                    L6: C_rad/H/OneDe-Cl
                        L7: C_rad/H/OneDeC-Cl
                            L8: C_rad/H/CtCs-Cl
                            L8: C_rad/H/CbCs-Cl
                            L8: C_rad/H/CO/Cs-Cl
                            L8: C_rad/H/CdCs-Cl
                            L8: C_rad/H/CSCs-Cl
                        L7: C_rad/H/OneDeO-Cl
                        L7: C_rad/H/OneDeS-Cl
                            L8: C_rad/H/CtS-Cl
                            L8: C_rad/H/CbS-Cl
                            L8: C_rad/H/CdS-Cl
                            L8: C_rad/H/CSS-Cl
                        L7: C_rad/H/OneDeN-Cl
                    L6: C_rad/H/TwoDe-Cl
                L5: C_sec_rad-Br
                    L6: C_rad/H/NonDeC-Br
                    L6: C_rad/H/NonDeO-Br
                        L7: C_rad/H/CsO-Br
                        L7: C_rad/H/O2-Br
                    L6: C_rad/H/NonDeS-Br
                        L7: C_rad/H/CsS-Br
                        L7: C_rad/H/S2-Br
                    L6: C_rad/H/NonDeCN-Br
                    L6: C_rad/H/NonDeON-Br
                    L6: C_rad/H/NonDeNN-Br
                    L6: C_rad/H/OneDe-Br
                        L7: C_rad/H/OneDeC-Br
                            L8: C_rad/H/CtCs-Br
                            L8: C_rad/H/CbCs-Br
                            L8: C_rad/H/CO/Cs-Br
                            L8: C_rad/H/CdCs-Br
                            L8: C_rad/H/CSCs-Br
                        L7: C_rad/H/OneDeO-Br
                        L7: C_rad/H/OneDeS-Br
                            L8: C_rad/H/CtS-Br
                            L8: C_rad/H/CbS-Br
                            L8: C_rad/H/CdS-Br
                            L8: C_rad/H/CSS-Br
                        L7: C_rad/H/OneDeN-Br
                    L6: C_rad/H/TwoDe-Br
            L4: C_ter_rad
                L5: C_rad/NonDe
                    L6: C_rad/Cs3
                        L7: C_rad/Cs2/Cs\O
                        L7: C_rad/Cs3_5ring_fused6
                        L7: C_rad/Cs3_5ring_adj5
                    L6: C_rad/NDMustO
                        L7: C_rad/Cs2O
                            L8: C_rad/OOH/Cs/Cs
                            L8: C_rad/O/Cs/Cs\Cs-H_or_Val7-9
                                L9: C_rad/O/Cs/Cs\Cs
                        L7: C_rad/CsO2
                        L7: C_rad/O3
                    L6: C_rad/NDMustS
                        L7: C_rad/Cs2S
                        L7: C_rad/CsS2
                        L7: C_rad/S3
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                        L7: C_rad/CtCs2
                        L7: C_rad/CbCs2
                        L7: C_rad/COCs2
                        L7: C_rad/CdCs2
                        L7: C_rad/CSCs2
                    L6: C_rad/CsO
                    L6: C_rad/CsS
                        L7: C_rad/CtCsS
                        L7: C_rad/CbCsS
                        L7: C_rad/CdCsS
                        L7: C_rad/CSCsS
                    L6: C_rad/O2
                    L6: C_rad/OS
                    L6: C_rad/S2
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                        L7: C_rad/CtCtCs
                        L7: C_rad/CtCbCs
                        L7: C_rad/CtCOCs
                        L7: C_rad/CbCbCs
                        L7: C_rad/CbCOCs
                        L7: C_rad/COCOCs
                        L7: C_rad/CdCtCs
                        L7: C_rad/CtCSCs
                        L7: C_rad/CdCbCs
                        L7: C_rad/CbCSCs
                        L7: C_rad/CdCOCs
                        L7: C_rad/COCSCs
                        L7: C_rad/CdCdCs
                        L7: C_rad/CdCSCs
                        L7: C_rad/CSCSCs
                    L6: C_rad/TDMustO
                    L6: C_rad/TDMustS
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
                    L6: N3s_rad_pri-F
                    L6: N3s_rad_pri-Cl
                    L6: N3s_rad_pri-Br
                L5: N3s_rad_sec
            L4: N3d_rad
                L5: N3d_rad/OneDe
                    L6: N3d_rad/OneDeC
                        L7: N3d_rad/OneDeCdd_O
        L3: N5_rad
            L4: N5dc_rad
        L3: Val7_rad
            L4: F_rad
            L4: Cl_rad
            L4: Br_rad
            L4: I_rad
"""
)

forbidden(
    label = "C_quintet",
    group =
"""
1 *3 C u4 p0 c0
""",
    shortDesc = """""",
    longDesc =
"""
""",
)

forbidden(
    label = "disprop1_OS_rad",
    group =
"""
1 *1 [C,N] u0 {2,S} {3,S}
2    [O,S] u1 {1,S}
3 *2 H     u0 {1,S}
""",
    shortDesc = """""",
    longDesc =
"""
This group forbids `H[C,N][O,S].`, where the radical site is O or S, but the non-rad site isn't O or S.
""",
)

forbidden(
    label = "disprop1_base_case",
    group =
"""
1 *1 R     u0 {2,S} {3,S}
2    [C,N] u1 {1,S}
3 *2 H     u0 {1,S}
""",
    shortDesc = """""",
    longDesc =
"""
Generally, we'd like to forbid `HR[R.]` from reacting here (`.` marks a radical), since this is a disprop reaction.
However, the following specific cases must not be forbidden here: `HO2`, `HSS`, `HOS`, `HSO`
(since they form the ground state triplets O2, S2, and SO).
This group forbids `HR[C,N].`, where the radical site isn't O or S
""",
)

forbidden(
    label = "disprop1_hyperS_H",
    group =
"""
1 *1 S     u0 p[0,1] {2,S} {3,S}
2    [O,S] u1 {1,S}
3 *2 H     u0 {1,S}
""",
    shortDesc = """""",
    longDesc =
"""
This group forbids `H[S p0,1][O,S].`, where hypervalance S is allowed at the H site
""",
)

forbidden(
    label = "disprop1_hyperS_rad",
    group =
"""
1 *1 [O,S] u0 {2,S} {3,S}
2    S     u1 p[0,1] {1,S}
3 *2 H     u0 {1,S}
""",
    shortDesc = """""",
    longDesc =
"""
This group forbids `H[O,S][S p0,1].`, where hypervalance S is allowed at the rad site
""",
)

forbidden(
    label = "disprop2",
    group =
"""
1    R u0 {2,S} {3,D}
2 *1 R u0 {1,S} {4,S}
3    R u0 {1,D} {5,S}
4 *2 H u0 {2,S}
5    R u1 {3,S}
""",
    shortDesc = """""",
    longDesc =
"""

""",
)

forbidden(
    label = "disprop3",
    group =
"""
1    R u0 {2,S} {3,T}
2 *1 R u0 {1,S} {4,S}
3    R u0 {1,T} {5,S}
4 *2 H u0 {2,S}
5    R u1 {3,S}
""",
    shortDesc = """""",
    longDesc =
"""

""",
)

forbidden(
    label = "disprop4",
    group =
"""
1    R u0 {2,D} {3,S}
2    R u0 {1,D} {4,S}
3    R u0 {1,S} {5,D}
4 *1 R u0 {2,S} {6,S}
5    R u0 {3,D} {7,S}
6 *2 H u0 {4,S}
7    R u1 {5,S}
""",
    shortDesc = """""",
    longDesc =
"""

""",
)

forbidden(
    label = "disprop5",
    group =
"""
1    R u0 {2,D} {3,S}
2    R u0 {1,D} {4,S}
3    R u0 {1,S} {5,D}
4 *1 R u0 {2,S} {6,S}
5    R u0 {3,D} {7,S}
6 *2 H u0 {4,S}
7    R u1 {5,S}
""",
    shortDesc = """""",
    longDesc =
"""

""",
)

forbidden(
    label = "disprop6_mul_bonds",
    group =
"""
1 *1 R u0 {2,[D,T]} {3,S}
2    R u1 {1,[D,T]}
3 *2 H u0 {1,S}
""",
    shortDesc = """""",
    longDesc =
"""
Forbidding cases such as:
R + [HC]=CH2 <=> RH + [CH]=[CH]
R + [C]#CH <=> RH + [C]#[C]
R + [N]=NH <=> RH + [N]=[N]
""",
)

forbidden(
    label = "disprop7_birad",
    group =
"""
1 *1 R     u1 {2,S} {3,S}
2    [C,N] u1 {1,S}
3 *2 H     u0 {1,S}
""",
    shortDesc = """""",
    longDesc =
"""
Forbidding cases such as:
R + [NH][NH] <=> RH + [N][NH]
""",
)
