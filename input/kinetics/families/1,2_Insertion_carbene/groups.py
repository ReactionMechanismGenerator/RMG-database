#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/groups"
shortDesc = u""
longDesc = u"""
Reaction site *1 should always be a singlet in this family.
"""

template(reactants=["carbene", "RR'"], products=["R_CO_R'"], ownReverse=False)

reverse = "1,1_Elimination"

reversible = True
recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['LOSE_PAIR', '*1', '1'],
])

entry(
    index = 0,
    label = "carbene",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    [H,Val7]   u0 px {1,S}
3    [H,Val7]   u0 px {1,S}
""",
    kinetics = None,
)

entry(
    index = 1000,
    label = "carbene-HH",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    H   u0 p0 {1,S}
3    H   u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1001,
    label = "carbene-YHY",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    Val7  u0 p3 {1,S}
3    [H,Val7]   u0 px {1,S}
""",
    kinetics = None,
)

entry(
    index = 1002,
    label = "carbene-YY",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    Val7 u0 p3 {1,S}
3    Val7 u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10020,
    label = "carbene-YH",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    Val7 u0 p3 {1,S}
3    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1003,
    label = "carbene-HF",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    F1s u0 p3 {1,S}
3    H  u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1004,
    label = "carbene-FF",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    F1s u0 p3 {1,S}
3    F1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1005,
    label = "carbene-HCl",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    Cl1s u0 p3 {1,S}
3    H  u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1006,
    label = "carbene-ClCl",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    Cl1s u0 p3 {1,S}
3    Cl1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1007,
    label = "carbene-HBr",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    Br1s  u0 p3 {1,S}
3    H  u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1008,
    label = "carbene-BrBr",
    group = 
"""
1 *1 C2s u0 p1 {2,S} {3,S}
2    Br1s  u0 p3 {1,S}
3    Br1s  u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "RR'",
    group = "OR{R_HY, R_R'}",
    kinetics = None,
)

entry(
    index = 2,
    label = "R_HY",
    group = 
"""
1 *2 [H,Cs,Cd,Cb,Ct,O,Sis,Sid,N,S,Val7] u0 {2,S}
2 *3 [H,Val7]                            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2000,
    label = "R_H",
    group = 
"""
1 *2 [H,Cs,Cd,Cb,Ct,O,Sis,Sid,N,S,Val7] u0 {2,S}
2 *3 H                          u0  {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "H2",
    group = 
"""
1 *2 H u0 {2,S}
2 *3 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3000,
    label = "YH",
    group = 
"""
1 *2 Val7 u0 {2,S}
2 *3 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3001,
    label = "FH",
    group = 
"""
1 *2 F1s u0 p3 {2,S}
2 *3 H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3002,
    label = "ClH",
    group = 
"""
1 *2 Cl1s u0 p3 {2,S}
2 *3 H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3003,
    label = "BrH",
    group = 
"""
1 *2 Br1s u0 p3 {2,S}
2 *3 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3004,
    label = "FF",
    group = 
"""
1 *2 F1s u0 p3 {2,S}
2 *3 F1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3005,
    label = "ClCl",
    group = 
"""
1 *2 Cl1s u0 p3 {2,S}
2 *3 Cl1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3006,
    label = "BrBr",
    group = 
"""
1 *2 Br1s u0 p3 {2,S}
2 *3 Br1s u0 p3 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Ct_H",
    group = 
"""
1 *2 Ct u0 {2,S}
2 *3 H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "acetylene",
    group = 
"""
1 *2 Ct u0 {2,S} {3,T}
2 *3 H  u0 {1,S}
3    Ct u0 {1,T} {4,S}
4    H  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 5000,
    label = "acetylene-YH",
    group = 
"""
1 *2 Ct u0 {2,S} {3,T}
2 *3 H  u0 {1,S}
3    Ct u0 {1,T} {4,S}
4    [H,Val7]  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 5001,
    label = "acetylene-F",
    group = 
"""
1 *2 Ct u0 {2,S} {3,T}
2 *3 H  u0 {1,S}
3    Ct u0 {1,T} {4,S}
4    F1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 5002,
    label = "acetylene-Cl",
    group = 
"""
1 *2 Ct u0 {2,S} {3,T}
2 *3 H  u0 {1,S}
3    Ct u0 {1,T} {4,S}
4    Cl1s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 5003,
    label = "acetylene-Br",
    group = 
"""
1 *2 Ct u0 {2,S} {3,T}
2 *3 H  u0 {1,S}
3    Ct u0 {1,T} {4,S}
4    Br1s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "RO_H",
    group = 
"""
1 *2 O u0 {2,S} {3,S}
2 *3 H u0 {1,S}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "CsO_H",
    group = 
"""
1 *2 O  u0 {2,S} {3,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "RS_H",
    group = 
"""
1 *2 S2s u0 {2,S} {3,S}
2 *3 H   u0 {1,S}
3    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CsS_H",
    group = 
"""
1 *2 S2s u0 {2,S} {3,S}
2 *3 H   u0 {1,S}
3    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Cd_H",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *3 H  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Cd_pri",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *3 H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1100,
    label = "Cd_pri-YH",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *3 H  u0 {1,S}
4    [H,Val7]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11001,
    label = "Cd_pri-F",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *3 H  u0 {1,S}
4    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11002,
    label = "Cd_pri-Cl",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *3 H  u0 {1,S}
4    Cl1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11003,
    label = "Cd_pri-Br",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *3 H  u0 {1,S}
4    Br1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "ethene",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D} {5,S} {6,S}
3 *3 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Cd_sec",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2    C   u0 {1,D}
3 *3 H   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Cd/H/NonDeC",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *3 H  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Cd/H/NonDeO",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *3 H  u0 {1,S}
4    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Cd/H/NonDeS",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S} {4,S}
2    C   u0 {1,D}
3 *3 H   u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Cd/H/OneDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S} {4,S}
2    C                u0 {1,D}
3 *3 H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Cb_H",
    group = 
"""
1 *2 Cb       u0 {2,B} {3,B} {4,S}
2    [Cb,Cbf] u0 {1,B}
3    [Cb,Cbf] u0 {1,B}
4 *3 H        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Cs_H",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20000,
    label = "C_methane",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20001,
    label = "C_methane-YH",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    [H,Val7]  u0 {1,S}
4    [H,Val7]  u0 {1,S}
5    [H,Val7]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20002,
    label = "C_methane-HFFF",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20003,
    label = "C_methane-HClClCl",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    Cl1s  u0 {1,S}
4    Cl1s  u0 {1,S}
5    Cl1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20004,
    label = "C_methane-HBrBrBr",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    Br1s  u0 {1,S}
4    Br1s  u0 {1,S}
5    Br1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "C_pri",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2100,
    label = "C_pri-YH",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    [H,Val7]   u0 {1,S}
4    [H,Val7]    u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2103,
    label = "C_pri-FF",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    F1s    u0 {1,S}
4    F1s    u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2101,
    label = "C_pri-ClCl",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    Cl1s   u0 {1,S}
4    Cl1s   u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2102,
    label = "C_pri-BrBr",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    Br1s  u0 {1,S}
4    Br1s  u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "C_pri/NonDeC",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "C_pri/NonDeO",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "C_pri/NonDeS",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "C_pri/De",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "C_pri/Cd",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "C_pri/Ct",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "C_sec",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2800,
    label = "C_sec-YH",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    [H,Val7]   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2801,
    label = "C_sec-F",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    F1s u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2802,
    label = "C_sec-Cl",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    Cl1s   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2803,
    label = "C_sec-Br",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    Br1s   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "C/H2/NonDeC",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "C/H2/NonDeO",
    group = 
"""
1 *2 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H        u0 {1,S}
3    H        u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "C/H2/CsO",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "C/H2/O2",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "C/H2/NonDeS",
    group = 
"""
1 *2 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H        u0 {1,S}
3    H        u0 {1,S}
4    S2s      u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "C/H2/CsS",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    H   u0 {1,S}
4    S2s u0 {1,S}
5    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "C/H2/S2",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    H   u0 {1,S}
4    S2s u0 {1,S}
5    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "C/H2/OneDe",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,Cb,CS] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "C/H2/OneDeC",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,Cb,CS] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "C/H2/OneDeO",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,Cb,CS] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "C/H2/OneDeS",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,Cb,CS] u0 {1,S}
5    S2s              u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "C/H2/TwoDe",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,Cb,CS] u0 {1,S}
5    [Cd,Ct,CO,Cb,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "C_ter",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "C/H/NonDeC",
    group = 
"""
1 *2 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H        u0 {1,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "C/H/Cs3",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "C/H/NDMustO",
    group = 
"""
1 *2 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H        u0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "C/H/NDMustS",
    group = 
"""
1 *2 Cs       u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H        u0 {1,S}
3    S2s      u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "C/H/OneDe",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "C/H/Cs2",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "C/H/ODMustO",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "C/H/ODMustS",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S2s              u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "C/H/TwoDe",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "C/H/Cs",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "C/H/TDMustO",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "C/H/TDMustS",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    S2s              u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "C/H/ThreeDe",
    group = 
"""
1 *2 Cs               u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "R_R'",
    group = 
"""
1 *2 [Cs,Sis,N]                u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 [Cs,Cd,Cb,Ct,Sis,Sid,N,S] u0 c0 {1,S}
3    [H,Val7]                         u0 {1,S}
4    [H,Val7]                         u0 {1,S}
5    [H,Val7]                         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Cs_Cs",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 c0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5601,
    label = "Cs_Cs-YH",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 c0 {1,S}
3    [H,Val7]  u0 {1,S}
4    [H,Val7]  u0 {1,S}
5    [H,Val7]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5602,
    label = "Cs_Cs-FFF",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 c0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5603,
    label = "Cs_Cs-ClClCl",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 c0 {1,S}
3    Cl1s  u0 {1,S}
4    Cl1s  u0 {1,S}
5    Cl1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5604,
    label = "Cs_Cs-BrBrBr",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 c0 {1,S}
3    Br1s  u0 {1,S}
4    Br1s  u0 {1,S}
5    Br1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "C_methyl_C_methyl",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 c0 {1,S} {6,S} {7,S} {8,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "C_methyl_C_pri",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 c0 {1,S} {6,S} {7,S} {8,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    C  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "C_methyl_C_sec",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 c0 {1,S} {6,S} {7,S} {8,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {2,S}
8    C  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "C_methyl_C_ter",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 c0 {1,S} {6,S} {7,S} {8,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,S}
7    C  u0 {2,S}
8    C  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cs_Cd",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 c0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6100,
    label = "Cs_Cd-YH",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 c0 {1,S}
3    [H,Val7]  u0 {1,S}
4    [H,Val7]  u0 {1,S}
5    [H,Val7]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6101,
    label = "Cs_Cd-FFF",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 c0 {1,S}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6102,
    label = "Cs_Cd-ClClCl",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 c0 {1,S}
3    Cl1s  u0 {1,S}
4    Cl1s  u0 {1,S}
5    Cl1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6103,
    label = "Cs_Cd-BrBrBr",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 c0 {1,S}
3    Br1s  u0 {1,S}
4    Br1s  u0 {1,S}
5    Br1s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "C_methyl_Cd_pri",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 c0 {1,S} {6,S} {7,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "C_methyl_Cd_sec",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 c0 {1,S} {6,S} {7,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,S}
7    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Cs_Cb",
    group = 
"""
1 *2 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cb u0 c0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: carbene
    L2: carbene-HH
    L2: carbene-YHY
        L3: carbene-YY
            L4: carbene-FF
            L4: carbene-ClCl
            L4: carbene-BrBr
        L3: carbene-YH
            L4: carbene-HF
            L4: carbene-HCl
            L4: carbene-HBr
L1: RR'
    L2: R_HY
        L3: FF
        L3: ClCl
        L3: BrBr
        L3: R_H
            L4: H2
            L4: YH
                L5: FH
                L5: ClH
                L5: BrH
            L4: Ct_H
                L5: acetylene-YH
                    L6: acetylene
                    L6: acetylene-F
                    L6: acetylene-Cl
                    L6: acetylene-Br
            L4: RO_H
                L5: CsO_H
            L4: RS_H
                L5: CsS_H
            L4: Cd_H
                L5: Cd_pri-YH
                    L6: Cd_pri-F
                    L6: Cd_pri-Cl
                    L6: Cd_pri-Br
                    L6: Cd_pri
                        L7: ethene
                L5: Cd_sec
                    L6: Cd/H/NonDeC
                    L6: Cd/H/NonDeO
                    L6: Cd/H/NonDeS
                    L6: Cd/H/OneDe
            L4: Cb_H
            L4: Cs_H
                L5: C_methane-YH
                    L6: C_methane-HFFF
                    L6: C_methane-HClClCl
                    L6: C_methane-HBrBrBr
                    L6: C_methane
                L5: C_pri-YH
                    L6: C_pri-FF
                    L6: C_pri-ClCl
                    L6: C_pri-BrBr
                    L6: C_pri
                        L7: C_pri/NonDeC
                        L7: C_pri/NonDeO
                        L7: C_pri/NonDeS
                        L7: C_pri/De
                            L8: C_pri/Cd
                            L8: C_pri/Ct
                L5: C_sec-YH
                    L6: C_sec-F
                    L6: C_sec-Cl
                    L6: C_sec-Br
                    L6: C_sec
                        L7: C/H2/NonDeC
                        L7: C/H2/NonDeO
                            L8: C/H2/CsO
                            L8: C/H2/O2
                        L7: C/H2/NonDeS
                            L8: C/H2/CsS
                            L8: C/H2/S2
                        L7: C/H2/OneDe
                            L8: C/H2/OneDeC
                            L8: C/H2/OneDeO
                            L8: C/H2/OneDeS
                        L7: C/H2/TwoDe
                L5: C_ter
                    L6: C/H/NonDeC
                        L7: C/H/Cs3
                        L7: C/H/NDMustO
                        L7: C/H/NDMustS
                    L6: C/H/OneDe
                        L7: C/H/Cs2
                        L7: C/H/ODMustO
                        L7: C/H/ODMustS
                    L6: C/H/TwoDe
                        L7: C/H/Cs
                        L7: C/H/TDMustO
                        L7: C/H/TDMustS
                    L6: C/H/ThreeDe
    L2: R_R'
        L3: Cs_Cs-YH
            L4: Cs_Cs-FFF
            L4: Cs_Cs-ClClCl
            L4: Cs_Cs-BrBrBr
            L4: Cs_Cs
                L5: C_methyl_C_methyl
                L5: C_methyl_C_pri
                L5: C_methyl_C_sec
                L5: C_methyl_C_ter
        L3: Cs_Cd-YH
            L4: Cs_Cd-FFF
            L4: Cs_Cd-ClClCl
            L4: Cs_Cd-BrBrBr
            L4: Cs_Cd
                L5: C_methyl_Cd_pri
                L5: C_methyl_Cd_sec
        L3: Cs_Cb
"""
)

