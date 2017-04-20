#!/usr/bin/env python
# encoding: utf-8

name = "Birad_recombination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["Rncycle"], ownReverse=False)

reverse = "Ring_Open"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Rn",
    group = "OR{R3, R4, R5, R6, R7, R8}",
    kinetics = None,
)

boundaryAtoms = ["*1", "*2"]

entry(
    index = 2,
    label = "Y_rad_out",
    group = 
"""
1 *1 R!H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Ypri_rad_out",
    group = 
"""
1 *2 R!H u1
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R3",
    group = 
"""
1 *1 R!H u1 {2,[S,D]}
2 *3 [Cs,Cd,CO,Os,S2s,N3s] u0 {1,[S,D]} {3,[S,D]}
3 *2 R!H u1 {2,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R3_SS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *2 R!H u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R3_SD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 Cd               u0 {1,S} {3,D}
3 *2 R!H              u1 {2,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R4",
    group = 
"""
1 *1 R!H u1 {2,[S,D]}
2 *3 [Cs,Cd,CO,Os,S2s,N3s] u0 {1,[S,D]} {3,[S,D]}
3 *4 [Cs,Cd,CO,Os,S2s,N3s] u0 {2,[S,D]} {4,[S,D]}
4 *2 R!H u1 {3,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "R4_SSS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *4 [Cs,Cd,CO,Os,S2s] u0 {2,S} {4,S}
4 *2 R!H u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "R4_SSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *4 Cd               u0 {2,S} {4,D}
4 *2 R!H              u1 {3,D}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R4_SDS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 Cd               u0 {1,S} {3,D}
3 *4 Cd               u0 {2,D} {4,S}
4 *2 R!H u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "R4_DSD",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *3 Cd u0 {1,D} {3,S}
3 *4 Cd u0 {2,S} {4,D}
4 *2 R!H u1 {3,D}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "R5",
    group = 
"""
1 *1 R!H u1 {2,[S,D]}
2 *3 [Cs,Cd,CO,Os,S2s,N3s] u0 {1,[S,D]} {3,[S,D]}
3 *5 [Cs,Cd,CO,Os,S2s,N3s] u0 {2,[S,D]} {4,[S,D]}
4 *4 [Cs,Cd,CO,Os,S2s,N3s] u0 {3,[S,D]} {5,[S,D]}
5 *2 R!H u1 {4,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "R5_SSSS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *5 [Cs,Cd,CO,Os,S2s] u0 {2,S} {4,S}
4 *4 [Cs,Cd,CO,Os,S2s] u0 {3,S} {5,S}
5 *2 R!H u1 {4,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R5_SSSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *5 [Cs,Cd,CO,Os,S2s] u0 {2,S} {4,S}
4 *4 Cd               u0 {3,S} {5,D}
5 *2 R!H              u1 {4,D}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "R5_SSDS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *4 Cd               u0 {3,D} {5,S}
5 *2 R!H u1 {4,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "R5_SDSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 Cd               u0 {1,S} {3,D}
3 *5 Cd               u0 {2,D} {4,S}
4 *4 Cd               u0 {3,S} {5,D}
5 *2 R!H              u1 {4,D}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "R5_DSSD",
    group = 
"""
1 *1 R!H              u1 {2,D}
2 *3 Cd               u0 {1,D} {3,S}
3 *5 [Cs,Cd,CO,Os,S2s] u0 {2,S} {4,S}
4 *4 Cd               u0 {3,S} {5,D}
5 *2 R!H              u1 {4,D}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "R6",
    group = 
"""
1 *1 R!H u1 {2,[S,D]}
2 *3 [Cs,Cd,CO,Os,S2s,N3s] u0 {1,[S,D]} {3,[S,D]}
3 *5 [Cs,Cd,CO,Os,S2s,N3s] u0 {2,[S,D]} {4,[S,D]}
4 *6 [Cs,Cd,CO,Os,S2s,N3s] u0 {3,[S,D]} {5,[S,D]}
5 *4 [Cs,Cd,CO,Os,S2s,N3s] u0 {4,[S,D]} {6,[S,D]}
6 *2 R!H u1 {5,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "R6_SSSSS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *5 [Cs,Cd,CO,Os,S2s] u0 {2,S} {4,S}
4 *6 [Cs,Cd,CO,Os,S2s] u0 {3,S} {5,S}
5 *4 [Cs,Cd,CO,Os,S2s] u0 {4,S} {6,S}
6 *2 R!H u1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "R6_SSSSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *5 [Cs,Cd,CO,Os,S2s] u0 {2,S} {4,S}
4 *6 [Cs,Cd,CO,Os,S2s] u0 {3,S} {5,S}
5 *4 Cd               u0 {4,S} {6,D}
6 *2 R!H              u1 {5,D}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "R6_SSSDS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *5 [Cs,Cd,CO,Os,S2s] u0 {2,S} {4,S}
4 *6 Cd               u0 {3,S} {5,D}
5 *4 Cd               u0 {4,D} {6,S}
6 *2 R!H u1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "R6_SSDSS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {5,S}
5 *4 [Cs,Cd,CO,Os,S2s] u0 {4,S} {6,S}
6 *2 R!H u1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R6_SSDSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *5 Cd               u0 {2,S} {4,D}
4 *6 Cd               u0 {3,D} {5,S}
5 *4 Cd               u0 {4,S} {6,D}
6 *2 R!H              u1 {5,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "R6_SDSDS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 Cd               u0 {1,S} {3,D}
3 *5 Cd               u0 {2,D} {4,S}
4 *6 Cd               u0 {3,S} {5,D}
5 *4 Cd               u0 {4,D} {6,S}
6 *2 R!H u1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "R6_SDSSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 Cd               u0 {1,S} {3,D}
3 *5 Cd               u0 {2,D} {4,S}
4 *6 [Cs,Cd,CO,Os,S2s] u0 {3,S} {5,S}
5 *4 Cd               u0 {4,S} {6,D}
6 *2 R!H              u1 {5,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R6_DSSSD",
    group = 
"""
1 *1 R!H              u1 {2,D}
2 *3 Cd               u0 {1,D} {3,S}
3 *5 [Cs,Cd,CO,Os,S2s] u0 {2,S} {4,S}
4 *6 [Cs,Cd,CO,Os,S2s] u0 {3,S} {5,S}
5 *4 Cd               u0 {4,S} {6,D}
6 *2 R!H              u1 {5,D}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "R6_DSDSD",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *3 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *6 Cd u0 {3,D} {5,S}
5 *4 Cd u0 {4,S} {6,D}
6 *2 R!H u1 {5,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "R7",
    group = 
"""
1 *1 R!H u1 {2,[S,D]}
2 *3 [Cs,Cd,CO,Os,S2s,N3s] u0 {1,[S,D]} {3,[S,D]}
3 *5 [Cs,Cd,CO,Os,S2s,N3s] u0 {2,[S,D]} {4,[S,D]}
4 *6 [Cs,Cd,CO,Os,S2s,N3s] u0 {3,[S,D]} {5,[S,D]}
5 *7 [Cs,Cd,CO,Os,S2s,N3s] u0 {4,[S,D]} {6,[S,D]}
6 *4 [Cs,Cd,CO,Os,S2s,N3s] u0 {5,[S,D]} {7,[S,D]}
7 *2 R!H u1 {6,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "R8",
    group = 
"""
1 *1 R!H u1 {2,[S,D]}
2 *3 [Cs,Cd,CO,Os,S2s,N3s] u0 {1,[S,D]} {3,[S,D]}
3 *5 [Cs,Cd,CO,Os,S2s,N3s] u0 {2,[S,D]} {4,[S,D]}
4 *6 [Cs,Cd,CO,Os,S2s,N3s] u0 {3,[S,D]} {5,[S,D]}
5 *7 [Cs,Cd,CO,Os,S2s,N3s] u0 {4,[S,D]} {6,[S,D]}
6 *8 [Cs,Cd,CO,Os,S2s,N3s] u0 {5,[S,D]} {7,[S,D]}
7 *4 [Cs,Cd,CO,Os,S2s,N3s] u0 {6,[S,D]} {8,[S,D]}
8 *2 R!H u1 {7,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "R8_SSSSSSS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *3 [Cs,Cd,CO,Os,S2s] u0 {1,S} {3,S}
3 *5 [Cs,Cd,CO,Os,S2s] u0 {2,S} {4,S}
4 *6 [Cs,Cd,CO,Os,S2s] u0 {3,S} {5,S}
5 *7 [Cs,Cd,CO,Os,S2s] u0 {4,S} {6,S}
6 *8 [Cs,Cd,CO,Os,S2s] u0 {5,S} {7,S}
7 *4 [Cs,Cd,CO,Os,S2s] u0 {6,S} {8,S}
8 *2 R!H u1 {7,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "O_rad",
    group = 
"""
1 *1 Os u1
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "S_rad",
    group = 
"""
1 *1 S2s u1
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Cdsingle_rad_out",
    group = 
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "CdsingleH_rad_out",
    group = 
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "CdsingleND_rad_out",
    group = 
"""
1 *1 Cd         u1 {2,S}
2    [Cs,Os,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "CdsingleDe_rad_out",
    group = 
"""
1 *1 Cd            u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "C_rad_out_single",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    R u0 {1,S}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "C_rad_out_2H",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    H u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "C_rad_out_1H",
    group = 
"""
1 *1 C   u1 {2,S} {3,S}
2    H   u0 {1,S}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "C_rad_out_H/NonDeC",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "C_rad_out_H/NonDeO",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    H u0 {1,S}
3    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "C_rad_out_H/NonDeS",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    H u0 {1,S}
3    S u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "C_rad_out_H/OneDe",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "C_rad_out_noH",
    group = 
"""
1 *1 C   u1 {2,S} {3,S}
2    R!H u0 {1,S}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "C_rad_out_NonDe",
    group = 
"""
1 *1 C          u1 {2,S} {3,S}
2    [Cs,Os,S2s] u0 {1,S}
3    [Cs,Os,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "C_rad_out_Cs2",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "C_rad_out_NDMustO",
    group = 
"""
1 *1 C       u1 {2,S} {3,S}
2    Os      u0 {1,S}
3    [Cs,Os] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "C_rad_out_NDMustS",
    group = 
"""
1 *1 C       u1 {2,S} {3,S}
2    S2s      u0 {1,S}
3    [Cs,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "C_rad_out_OneDe",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cs,Os,S2s]    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "C_rad_out_OneDe/Cs",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "C_rad_out_OneDe/O",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Os            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "C_rad_out_OneDe/S",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    S2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "C_rad_out_TwoDe",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Opri_rad",
    group = 
"""
1 *2 Os u1
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Spri_rad",
    group = 
"""
1 *2 S2s u1
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cdsinglepri_rad_out",
    group = 
"""
1 *2 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "CdsinglepriH_rad_out",
    group = 
"""
1 *2 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "CdsinglepriND_rad_out",
    group = 
"""
1 *2 Cd         u1 {2,S}
2    [Cs,Os,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "CdsinglepriDe_rad_out",
    group = 
"""
1 *2 Cd            u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Cpri_rad_out_single",
    group = 
"""
1 *2 C u1 {2,S} {3,S}
2    R u0 {1,S}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Cpri_rad_out_2H",
    group = 
"""
1 *2 C u1 {2,S} {3,S}
2    H u0 {1,S}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Cpri_rad_out_1H",
    group = 
"""
1 *2 C   u1 {2,S} {3,S}
2    H   u0 {1,S}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Cpri_rad_out_H/NonDeC",
    group = 
"""
1 *2 C  u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Cpri_rad_out_H/NonDeO",
    group = 
"""
1 *2 C  u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Os u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Cpri_rad_out_H/NonDeS",
    group = 
"""
1 *2 C  u1 {2,S} {3,S}
2    H  u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Cpri_rad_out_H/OneDe",
    group = 
"""
1 *2 C             u1 {2,S} {3,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Cpri_rad_out_noH",
    group = 
"""
1 *2 C   u1 {2,S} {3,S}
2    R!H u0 {1,S}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Cpri_rad_out_NonDe",
    group = 
"""
1 *2 C          u1 {2,S} {3,S}
2    [Cs,Os,S2s] u0 {1,S}
3    [Cs,Os,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Cpri_rad_out_Cs2",
    group = 
"""
1 *2 C  u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Cpri_rad_out_NDMustO",
    group = 
"""
1 *2 C       u1 {2,S} {3,S}
2    Os      u0 {1,S}
3    [Cs,Os] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Cpri_rad_out_NDMustS",
    group = 
"""
1 *2 C       u1 {2,S} {3,S}
2    S2s      u0 {1,S}
3    [Cs,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Cpri_rad_out_OneDe",
    group = 
"""
1 *2 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cs,Os,S2s]    u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Cpri_rad_out_OneDe/Cs",
    group = 
"""
1 *2 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Cpri_rad_out_OneDe/O",
    group = 
"""
1 *2 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Os            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Cpri_rad_out_OneDe/S",
    group = 
"""
1 *2 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    S2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Cpri_rad_out_TwoDe",
    group = 
"""
1 *2 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: Rn
    L2: R3
        L3: R3_SS
        L3: R3_SD
    L2: R4
        L3: R4_SSS
        L3: R4_SSD
        L3: R4_SDS
        L3: R4_DSD
    L2: R5
        L3: R5_SSSS
        L3: R5_SSSD
        L3: R5_SSDS
        L3: R5_SDSD
        L3: R5_DSSD
    L2: R6
        L3: R6_SSSSS
        L3: R6_SSSSD
        L3: R6_SSSDS
        L3: R6_SSDSS
        L3: R6_SSDSD
        L3: R6_SDSDS
        L3: R6_SDSSD
        L3: R6_DSSSD
        L3: R6_DSDSD
    L2: R7
    L2: R8
        L3: R8_SSSSSSS
L1: Y_rad_out
    L2: O_rad
    L2: S_rad
    L2: Cdsingle_rad_out
        L3: CdsingleDe_rad_out
        L3: CdsingleND_rad_out
        L3: CdsingleH_rad_out
    L2: C_rad_out_single
        L3: C_rad_out_noH
            L4: C_rad_out_NonDe
                L5: C_rad_out_Cs2
                L5: C_rad_out_NDMustO
                L5: C_rad_out_NDMustS
            L4: C_rad_out_OneDe
                L5: C_rad_out_OneDe/Cs
                L5: C_rad_out_OneDe/O
                L5: C_rad_out_OneDe/S
            L4: C_rad_out_TwoDe
        L3: C_rad_out_1H
            L4: C_rad_out_H/NonDeC
            L4: C_rad_out_H/NonDeO
            L4: C_rad_out_H/NonDeS
            L4: C_rad_out_H/OneDe
        L3: C_rad_out_2H
L1: Ypri_rad_out
    L2: Opri_rad
    L2: Spri_rad
    L2: Cdsinglepri_rad_out
        L3: CdsinglepriH_rad_out
        L3: CdsinglepriND_rad_out
        L3: CdsinglepriDe_rad_out
    L2: Cpri_rad_out_single
        L3: Cpri_rad_out_noH
            L4: Cpri_rad_out_NonDe
                L5: Cpri_rad_out_Cs2
                L5: Cpri_rad_out_NDMustO
                L5: Cpri_rad_out_NDMustS
            L4: Cpri_rad_out_OneDe
                L5: Cpri_rad_out_OneDe/Cs
                L5: Cpri_rad_out_OneDe/O
                L5: Cpri_rad_out_OneDe/S
            L4: Cpri_rad_out_TwoDe
        L3: Cpri_rad_out_1H
            L4: Cpri_rad_out_H/NonDeC
            L4: Cpri_rad_out_H/NonDeO
            L4: Cpri_rad_out_H/NonDeS
            L4: Cpri_rad_out_H/OneDe
        L3: Cpri_rad_out_2H
"""
)

forbidden(
    label = "RR_d",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *2 R!H u1 {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "RR_s",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 R!H u1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "RR_t",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *2 R!H u1 {1,T}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

