#!/usr/bin/env python
# encoding: utf-8

name = "Birad_recombination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["Rncycle"], ownReverse=False)

reverse = "Ring_Open"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Rn",
    group = "OR{R3, R4, R5, R6}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Y_rad_out",
    group = 
"""
1 *1 R!H 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Ypri_rad_out",
    group = 
"""
1 *2 R!H 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "R3",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss,N3s} 1 {2,{S,D}}
2 *3 {Cs,Cd,CO,Os,Ss,N3s} 0 {1,{S,D}} {3,{S,D}}
3 *2 {Cs,Cd,CO,Os,Ss,N3s} 1 {2,{S,D}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R3_SS",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3 *2 {Cs,Cd,CO,Os,Ss} 1 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "R3_SD",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 Cd               0 {1,S} {3,D}
3 *2 Cd               1 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "R4",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss,N3s} 1 {2,{S,D}}
2 *3 {Cs,Cd,CO,Os,Ss,N3s} 0 {1,{S,D}} {3,{S,D}}
3 *4 {Cs,Cd,CO,Os,Ss,N3s} 0 {2,{S,D}} {4,{S,D}}
4 *2 {Cs,Cd,CO,Os,Ss,N3s} 1 {3,{S,D}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "R4_SSS",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3 *4 {Cs,Cd,CO,Os,Ss} 0 {2,S} {4,S}
4 *2 {Cs,Cd,CO,Os,Ss} 1 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "R4_SSD",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3 *4 Cd               0 {2,S} {4,D}
4 *2 Cd               1 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "R4_SDS",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 Cd               0 {1,S} {3,D}
3 *4 Cd               0 {2,D} {4,S}
4 *2 {Cs,Cd,CO,Os,Ss} 1 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "R4_DSD",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *3 Cd 0 {1,D} {3,S}
3 *4 Cd 0 {2,S} {4,D}
4 *2 Cd 1 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "R5",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss,N3s} 1 {2,{S,D}}
2 *3 {Cs,Cd,CO,Os,Ss,N3s} 0 {1,{S,D}} {3,{S,D}}
3    {Cs,Cd,CO,Os,Ss,N3s} 0 {2,{S,D}} {4,{S,D}}
4 *4 {Cs,Cd,CO,Os,Ss,N3s} 0 {3,{S,D}} {5,{S,D}}
5 *2 {Cs,Cd,CO,Os,Ss,N3s} 1 {4,{S,D}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "R5_SSSS",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3    {Cs,Cd,CO,Os,Ss} 0 {2,S} {4,S}
4 *4 {Cs,Cd,CO,Os,Ss} 0 {3,S} {5,S}
5 *2 {Cs,Cd,CO,Os,Ss} 1 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "R5_SSSD",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3    {Cs,Cd,CO,Os,Ss} 0 {2,S} {4,S}
4 *4 Cd               0 {3,S} {5,D}
5 *2 Cd               1 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "R5_SSDS",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3    Cd               0 {2,S} {4,D}
4 *4 Cd               0 {3,D} {5,S}
5 *2 {Cs,Cd,CO,Os,Ss} 1 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "R5_SDSD",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 Cd               0 {1,S} {3,D}
3    Cd               0 {2,D} {4,S}
4 *4 Cd               0 {3,S} {5,D}
5 *2 Cd               1 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "R5_DSSD",
    group = 
"""
1 *1 Cd               1 {2,D}
2 *3 Cd               0 {1,D} {3,S}
3    {Cs,Cd,CO,Os,Ss} 0 {2,S} {4,S}
4 *4 Cd               0 {3,S} {5,D}
5 *2 Cd               1 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "R6",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss,N3s} 1 {2,{S,D}}
2 *3 {Cs,Cd,CO,Os,Ss,N3s} 0 {1,{S,D}} {3,{S,D}}
3    {Cs,Cd,CO,Os,Ss,N3s} 0 {2,{S,D}} {4,{S,D}}
4    {Cs,Cd,CO,Os,Ss,N3s} 0 {3,{S,D}} {5,{S,D}}
5 *4 {Cs,Cd,CO,Os,Ss,N3s} 0 {4,{S,D}} {6,{S,D}}
6 *2 {Cs,Cd,CO,Os,Ss,N3s} 1 {5,{S,D}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "R6_SSSSS",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3    {Cs,Cd,CO,Os,Ss} 0 {2,S} {4,S}
4    {Cs,Cd,CO,Os,Ss} 0 {3,S} {5,S}
5 *4 {Cs,Cd,CO,Os,Ss} 0 {4,S} {6,S}
6 *2 {Cs,Cd,CO,Os,Ss} 1 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "R6_SSSSD",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3    {Cs,Cd,CO,Os,Ss} 0 {2,S} {4,S}
4    {Cs,Cd,CO,Os,Ss} 0 {3,S} {5,S}
5 *4 Cd               0 {4,S} {6,D}
6 *2 Cd               1 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "R6_SSSDS",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3    {Cs,Cd,CO,Os,Ss} 0 {2,S} {4,S}
4    Cd               0 {3,S} {5,D}
5 *4 Cd               0 {4,D} {6,S}
6 *2 {Cs,Cd,CO,Os,Ss} 1 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "R6_SSDSS",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3    Cd               0 {2,S} {4,D}
4    Cd               0 {3,D} {5,S}
5 *4 {Cs,Cd,CO,Os,Ss} 0 {4,S} {6,S}
6 *2 {Cs,Cd,CO,Os,Ss} 1 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "R6_SSDSD",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 {Cs,Cd,CO,Os,Ss} 0 {1,S} {3,S}
3    Cd               0 {2,S} {4,D}
4    Cd               0 {3,D} {5,S}
5 *4 Cd               0 {4,S} {6,D}
6 *2 Cd               1 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "R6_SDSDS",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 Cd               0 {1,S} {3,D}
3    Cd               0 {2,D} {4,S}
4    Cd               0 {3,S} {5,D}
5 *4 Cd               0 {4,D} {6,S}
6 *2 {Cs,Cd,CO,Os,Ss} 1 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "R6_SDSSD",
    group = 
"""
1 *1 {Cs,Cd,CO,Os,Ss} 1 {2,S}
2 *3 Cd               0 {1,S} {3,D}
3    Cd               0 {2,D} {4,S}
4    {Cs,Cd,CO,Os,Ss} 0 {3,S} {5,S}
5 *4 Cd               0 {4,S} {6,D}
6 *2 Cd               1 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "R6_DSSSD",
    group = 
"""
1 *1 Cd               1 {2,D}
2 *3 Cd               0 {1,D} {3,S}
3    {Cs,Cd,CO,Os,Ss} 0 {2,S} {4,S}
4    {Cs,Cd,CO,Os,Ss} 0 {3,S} {5,S}
5 *4 Cd               0 {4,S} {6,D}
6 *2 Cd               1 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "R6_DSDSD",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *3 Cd 0 {1,D} {3,S}
3    Cd 0 {2,S} {4,D}
4    Cd 0 {3,D} {5,S}
5 *4 Cd 0 {4,S} {6,D}
6 *2 Cd 1 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "O_rad",
    group = 
"""
1 *1 Os 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "S_rad",
    group = 
"""
1 *1 Ss 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "Cd_rad_out",
    group = 
"""
1 *1 C       1 {2,D}
2    {C,O,S} 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "Cd_rad_out_C",
    group = 
"""
1 *1 C 1 {2,D}
2    C 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "Cd_rad_out_O",
    group = 
"""
1 *1 C 1 {2,D}
2    O 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "Cd_rad_out_S",
    group = 
"""
1 *1 C 1 {2,D}
2    S 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "Cdsingle_rad_out",
    group = 
"""
1 *1 Cd 1 {2,S}
2    R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "CdsingleH_rad_out",
    group = 
"""
1 *1 Cd 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "CdsingleND_rad_out",
    group = 
"""
1 *1 Cd         1 {2,S}
2    {Cs,Os,Ss} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "CdsingleDe_rad_out",
    group = 
"""
1 *1 Cd            1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C_rad_out_single",
    group = 
"""
1 *1 C 1 {2,S} {3,S}
2    R 0 {1,S}
3    R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C_rad_out_2H",
    group = 
"""
1 *1 C 1 {2,S} {3,S}
2    H 0 {1,S}
3    H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C_rad_out_1H",
    group = 
"""
1 *1 C   1 {2,S} {3,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C_rad_out_H/NonDeC",
    group = 
"""
1 *1 C  1 {2,S} {3,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C_rad_out_H/NonDeO",
    group = 
"""
1 *1 C 1 {2,S} {3,S}
2    H 0 {1,S}
3    O 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C_rad_out_H/NonDeS",
    group = 
"""
1 *1 C 1 {2,S} {3,S}
2    H 0 {1,S}
3    S 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C_rad_out_H/OneDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C_rad_out_noH",
    group = 
"""
1 *1 C   1 {2,S} {3,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C_rad_out_NonDe",
    group = 
"""
1 *1 C          1 {2,S} {3,S}
2    {Cs,Os,Ss} 0 {1,S}
3    {Cs,Os,Ss} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C_rad_out_Cs2",
    group = 
"""
1 *1 C  1 {2,S} {3,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C_rad_out_NDMustO",
    group = 
"""
1 *1 C       1 {2,S} {3,S}
2    Os      0 {1,S}
3    {Cs,Os} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C_rad_out_NDMustS",
    group = 
"""
1 *1 C       1 {2,S} {3,S}
2    Ss      0 {1,S}
3    {Cs,Ss} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C_rad_out_OneDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cs,Os,Ss}    0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C_rad_out_OneDe/Cs",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Cs            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C_rad_out_OneDe/O",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Os            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "C_rad_out_OneDe/S",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Ss            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C_rad_out_TwoDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "Opri_rad",
    group = 
"""
1 *2 Os 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "Spri_rad",
    group = 
"""
1 *2 Ss 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "Cdpri_rad_out",
    group = 
"""
1 *2 C       1 {2,D}
2    {C,O,S} 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "Cdpri_rad_out_C",
    group = 
"""
1 *2 C 1 {2,D}
2    C 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "Cdpri_rad_out_O",
    group = 
"""
1 *2 C 1 {2,D}
2    O 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "Cdpri_rad_out_S",
    group = 
"""
1 *2 C 1 {2,D}
2    S 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "Cdsinglepri_rad_out",
    group = 
"""
1 *2 Cd 1 {2,S}
2    R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "CdsinglepriH_rad_out",
    group = 
"""
1 *2 Cd 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "CdsinglepriND_rad_out",
    group = 
"""
1 *2 Cd         1 {2,S}
2    {Cs,Os,Ss} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "CdsinglepriDe_rad_out",
    group = 
"""
1 *2 Cd            1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "Cpri_rad_out_single",
    group = 
"""
1 *2 C 1 {2,S} {3,S}
2    R 0 {1,S}
3    R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "Cpri_rad_out_2H",
    group = 
"""
1 *2 C 1 {2,S} {3,S}
2    H 0 {1,S}
3    H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "Cpri_rad_out_1H",
    group = 
"""
1 *2 C   1 {2,S} {3,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "Cpri_rad_out_H/NonDeC",
    group = 
"""
1 *2 C  1 {2,S} {3,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "Cpri_rad_out_H/NonDeO",
    group = 
"""
1 *2 C  1 {2,S} {3,S}
2    H  0 {1,S}
3    Os 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "Cpri_rad_out_H/NonDeS",
    group = 
"""
1 *2 C  1 {2,S} {3,S}
2    H  0 {1,S}
3    Ss 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "Cpri_rad_out_H/OneDe",
    group = 
"""
1 *2 C             1 {2,S} {3,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "Cpri_rad_out_noH",
    group = 
"""
1 *2 C   1 {2,S} {3,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "Cpri_rad_out_NonDe",
    group = 
"""
1 *2 C          1 {2,S} {3,S}
2    {Cs,Os,Ss} 0 {1,S}
3    {Cs,Os,Ss} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "Cpri_rad_out_Cs2",
    group = 
"""
1 *2 C  1 {2,S} {3,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "Cpri_rad_out_NDMustO",
    group = 
"""
1 *2 C       1 {2,S} {3,S}
2    Os      0 {1,S}
3    {Cs,Os} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "Cpri_rad_out_NDMustS",
    group = 
"""
1 *2 C       1 {2,S} {3,S}
2    Ss      0 {1,S}
3    {Cs,Ss} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "Cpri_rad_out_OneDe",
    group = 
"""
1 *2 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cs,Os,Ss}    0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "Cpri_rad_out_OneDe/Cs",
    group = 
"""
1 *2 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Cs            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "Cpri_rad_out_OneDe/O",
    group = 
"""
1 *2 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Os            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "Cpri_rad_out_OneDe/S",
    group = 
"""
1 *2 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Ss            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "Cpri_rad_out_TwoDe",
    group = 
"""
1 *2 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
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
L1: Y_rad_out
    L2: O_rad
    L2: S_rad
    L2: Cd_rad_out
        L3: Cd_rad_out_C
        L3: Cd_rad_out_O
        L3: Cd_rad_out_S
    L2: Cdsingle_rad_out
        L3: CdsingleH_rad_out
        L3: CdsingleND_rad_out
        L3: CdsingleDe_rad_out
    L2: C_rad_out_single
        L3: C_rad_out_2H
        L3: C_rad_out_1H
            L4: C_rad_out_H/NonDeC
            L4: C_rad_out_H/NonDeO
            L4: C_rad_out_H/NonDeS
            L4: C_rad_out_H/OneDe
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
L1: Ypri_rad_out
    L2: Opri_rad
    L2: Spri_rad
    L2: Cdpri_rad_out
        L3: Cdpri_rad_out_C
        L3: Cdpri_rad_out_O
        L3: Cdpri_rad_out_S
    L2: Cdsinglepri_rad_out
        L3: CdsinglepriH_rad_out
        L3: CdsinglepriND_rad_out
        L3: CdsinglepriDe_rad_out
    L2: Cpri_rad_out_single
        L3: Cpri_rad_out_2H
        L3: Cpri_rad_out_1H
            L4: Cpri_rad_out_H/NonDeC
            L4: Cpri_rad_out_H/NonDeO
            L4: Cpri_rad_out_H/NonDeS
            L4: Cpri_rad_out_H/OneDe
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
"""
)

forbidden(
    label = "RR_d",
    group = 
"""
1 *1 R!H 1 {2,D}
2 *2 R!H 1 {1,D}
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
1 *1 R!H 1 {2,S}
2 *2 R!H 1 {1,S}
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
1 *1 R!H 1 {2,T}
2 *2 R!H 1 {1,T}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

