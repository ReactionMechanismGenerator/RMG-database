#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["CO2_CS2", "RR'"], products=["R_(CS2)_R'"], ownReverse=False)

reverse = "1,2_Elimination_CO2"
reversible = True

recipe(actions=[
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 0,
    label = "CO2_CS2",
    group = "OR{CO2, CS2}",
    kinetics = None,
)

entry(
    index = 1,
    label = "RR'",
    group = "OR{R_H, R_R'}",
    kinetics = None,
)

entry(
    index = 2,
    label = "CO2",
    group = "OR{CO2_Od, CO2_Cdd}",
    kinetics = None,
)

entry(
    index = 3,
    label = "CO2_Od",
    group = 
"""
1 *2 Cdd u0 {2,D} {3,D}
2 *1 O2d u0 {1,D}
3    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "CO2_Cdd",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O2d u0 {1,D}
3    O2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CS2",
    group = "OR{CS2_Sd, CS2_Cdd}",
    kinetics = None,
)

entry(
    index = 6,
    label = "CS2_Sd",
    group = 
"""
1 *2 Cdd u0 {2,D} {3,D}
2 *1 S2d u0 {1,D}
3    S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "CS2_Cdd",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 S2d u0 {1,D}
3    S2d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "R_H",
    group = 
"""
1 *3 [H,Cs,Cd,Cb,Sis,Sid,N,Val7] u0 c0 {2,S}
2 *4 H                      u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "H2",
    group = 
"""
1 *3 H u0 p0 c0 {2,S}
2 *4 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9000,
    label = "YH",
    group = 
"""
1 *3 Val7 u0 p3 c0 {2,S}
2 *4 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9001,
    label = "FH",
    group = 
"""
1 *3 F1s u0 p3 c0 {2,S}
2 *4 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9003,
    label = "ClH",
    group = 
"""
1 *3 Cl1s u0 p3 c0 {2,S}
2 *4 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9004,
    label = "BrH",
    group = 
"""
1 *3 Br1s u0 p3 c0 {2,S}
2 *4 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Cb_H",
    group = 
"""
1 *3 Cb       u0 c0 {2,B} {3,S}
2    [Cb,Cbf] u0 {1,B}
3 *4 H        u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Cd_H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D}
3 *4 H  u0 p0 c0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Cd_pri",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D}
3 *4 H  u0 p0 c0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Cd_sec",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {3,S} {4,S}
2    Cd  u0 {1,D}
3 *4 H   u0 p0 c0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Cd/H/NonDeC",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D}
3 *4 H  u0 p0 c0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Cd/H/NonDeO",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {3,S} {4,S}
2    Cd  u0 {1,D}
3 *4 H   u0 p0 c0 {1,S}
4    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Cd/H/OneDe",
    group = 
"""
1 *3 Cd               u0 c0 {2,D} {3,S} {4,S}
2    Cd               u0 {1,D}
3 *4 H                u0 p0 c0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Cs_H",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  u0 p0 c0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "C_methane",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  u0 p0 c0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "C_pri",
    group = 
"""
1 *3 Cs  u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   u0 p0 c0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "C_pri/NonDeC",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  u0 p0 c0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "C_pri/NonDeO",
    group = 
"""
1 *3 Cs  u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   u0 p0 c0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "C_pri/NonDeS",
    group = 
"""
1 *3 Cs  u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   u0 p0 c0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "C_pri/De",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "C_sec",
    group = 
"""
1 *3 Cs  u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   u0 p0 c0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "C/H2/NonDeC",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  u0 p0 c0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "C/H2/NonDeO",
    group = 
"""
1 *3 Cs       u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H        u0 p0 c0 {1,S}
3    H        u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "C/H2/CsO",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  u0 p0 c0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "C/H2/O2",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  u0 p0 c0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
5    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "C/H2/NonDeS",
    group = 
"""
1 *3 Cs       u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H        u0 p0 c0 {1,S}
3    H        u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "C/H2/CsS",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  u0 p0 c0 {1,S}
3    H  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "C/H2/S2",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  u0 p0 c0 {1,S}
3    H  u0 {1,S}
4    S  u0 {1,S}
5    S  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "C/H2/OneDe",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cs,O]           u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "C/H2/OneDeC",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "C/H2/OneDeO",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "C/H2/TwoDe",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,CS,Cb] u0 {1,S}
5    [Cd,Ct,CO,CS,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "C_ter",
    group = 
"""
1 *3 Cs  u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   u0 p0 c0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "C/H/NonDeC",
    group = 
"""
1 *3 Cs       u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H        u0 p0 c0 {1,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "C/H/Cs3",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  u0 p0 c0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "C/H/NDMustO",
    group = 
"""
1 *3 Cs       u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H        u0 p0 c0 {1,S}
3    O        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "C/H/OneDe",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "C/H/Cs2",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "C/H/ODMustO",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    O                u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "C/H/TwoDe",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "C/H/Cs",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "C/H/TDMustO",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    O                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "C/H/ThreeDe",
    group = 
"""
1 *3 Cs               u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 H                u0 p0 c0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "R_R'",
    group = 
"""
1 *3 [Cs,Sis,N,S]           u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 [Cs,Cd,Cb,Sis,Sid,N,S] u0 c0 {1,S}
3    H                      u0 {1,S}
4    H                      u0 {1,S}
5    H                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Cs_Cs",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs u0 c0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "C_methyl_C_methyl",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs u0 c0 {1,S} {6,S} {7,S} {8,S}
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
    index = 50,
    label = "C_methyl_C_pri",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs u0 c0 {1,S} {6,S} {7,S} {8,S}
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
    index = 51,
    label = "C_methyl_C_sec",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs u0 c0 {1,S} {6,S} {7,S} {8,S}
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
    index = 52,
    label = "C_methyl_C_ter",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs u0 c0 {1,S} {6,S} {7,S} {8,S}
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
    index = 53,
    label = "Cs_Cd",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cd u0 c0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "C_methyl_Cd_pri",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cd u0 c0 {1,S} {6,S} {7,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "C_methyl_Cd_sec",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cd u0 c0 {1,S} {6,S} {7,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,S}
7    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Cs_Cb",
    group = 
"""
1 *3 Cs u0 c0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cb u0 c0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: CO2_CS2
    L2: CO2
        L3: CO2_Od
        L3: CO2_Cdd
    L2: CS2
        L3: CS2_Sd
        L3: CS2_Cdd
L1: RR'
    L2: R_H
        L3: H2
        L3: YH
            L4: FH
            L4: ClH
            L4: BrH
        L3: Cb_H
        L3: Cd_H
            L4: Cd_pri
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/OneDe
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C_pri/NonDeC
                L5: C_pri/NonDeO
                L5: C_pri/NonDeS
                L5: C_pri/De
            L4: C_sec
                L5: C/H2/NonDeC
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                    L6: C/H2/O2
                L5: C/H2/NonDeS
                    L6: C/H2/CsS
                    L6: C/H2/S2
                L5: C/H2/OneDe
                    L6: C/H2/OneDeC
                    L6: C/H2/OneDeO
                L5: C/H2/TwoDe
            L4: C_ter
                L5: C/H/NonDeC
                    L6: C/H/Cs3
                    L6: C/H/NDMustO
                L5: C/H/OneDe
                    L6: C/H/Cs2
                    L6: C/H/ODMustO
                L5: C/H/TwoDe
                    L6: C/H/Cs
                    L6: C/H/TDMustO
                L5: C/H/ThreeDe
    L2: R_R'
        L3: Cs_Cs
            L4: C_methyl_C_methyl
            L4: C_methyl_C_pri
            L4: C_methyl_C_sec
            L4: C_methyl_C_ter
        L3: Cs_Cd
            L4: C_methyl_Cd_pri
            L4: C_methyl_Cd_sec
        L3: Cs_Cb
"""
)

