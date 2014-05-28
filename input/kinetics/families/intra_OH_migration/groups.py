#!/usr/bin/env python
# encoding: utf-8

name = "intra_OH_migration/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RnOOH"], products=["HORO."], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

entry(
    index = 1,
    label = "RnOOH",
    group = "OR{ROOH, R2OOH, R3OOH, R4OOH}",
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
1 *1 {C,Sid,Sis,N} 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "ROOH",
    group = 
"""
1 *1 {Cd,Cs,Sid,Sis,N} 1 {2,S}
2 *2 O                 0 {1,S} {3,S}
3 *3 O                 0 {2,S} {4,S}
4    H                 0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "R2OOH",
    group = 
"""
1 *1 {Cd,Cs,Sid,Sis,N} 1 {2,{S,D}}
2 *4 {Cd,Cs,Sid,Sis,N} 0 {1,{S,D}} {3,S}
3 *2 O                 0 {2,S} {4,S}
4 *3 O                 0 {3,S} {5,S}
5    H                 0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R2OOH_S",
    group = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    H       0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "R2OOH_D",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *2 O  0 {2,S} {4,S}
4 *3 O  0 {3,S} {5,S}
5    H  0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "R3OOH",
    group = 
"""
1 *1 {Cd,Cs,Sid,Sis,N} 1 {2,{S,D}}
2 *4 {Cd,Cs,Sid,Sis,N} 0 {1,{S,D}} {3,{S,D}}
3    {Cd,Cs,Sid,Sis,N} 0 {2,{S,D}} {4,S}
4 *2 O                 0 {3,S} {5,S}
5 *3 O                 0 {4,S} {6,S}
6    H                 0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "R3OOH_SS",
    group = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3    {Cd,Cs} 0 {2,S} {4,S}
4 *2 O       0 {3,S} {5,S}
5 *3 O       0 {4,S} {6,S}
6    H       0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "R3OOH_SD",
    group = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 Cd      0 {1,S} {3,D}
3    Cd      0 {2,D} {4,S}
4 *2 O       0 {3,S} {5,S}
5 *3 O       0 {4,S} {6,S}
6    H       0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "R3OOH_DS",
    group = 
"""
1 *1 Cd      1 {2,D}
2 *4 Cd      0 {1,D} {3,S}
3    {Cd,Cs} 0 {2,S} {4,S}
4 *2 O       0 {3,S} {5,S}
5 *3 O       0 {4,S} {6,S}
6    H       0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "R4OOH",
    group = 
"""
1 *1 {Cd,Cs,Sid,Sis,N} 1 {2,{S,D}}
2 *4 {Cd,Cs,Sid,Sis,N} 0 {1,{S,D}} {3,{S,D}}
3    {Cd,Cs,Sid,Sis,N} 0 {2,{S,D}} {4,{S,D}}
4    {Cd,Cs,Sid,Sis,N} 0 {3,{S,D}} {5,S}
5 *2 O                 0 {4,S} {6,S}
6 *3 O                 0 {5,S} {7,S}
7    H                 0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "R4OOH_SSS",
    group = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3    {Cd,Cs} 0 {2,S} {4,S}
4    {Cd,Cs} 0 {3,S} {5,S}
5 *2 O       0 {4,S} {6,S}
6 *3 O       0 {5,S} {7,S}
7    H       0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "R4OOH_SSD",
    group = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3    Cd      0 {2,S} {4,D}
4    Cd      0 {3,D} {5,S}
5 *2 O       0 {4,S} {6,S}
6 *3 O       0 {5,S} {7,S}
7    H       0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "R4OOH_SDS",
    group = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 Cd      0 {1,S} {3,D}
3    Cd      0 {2,D} {4,S}
4    {Cd,Cs} 0 {3,S} {5,S}
5 *2 O       0 {4,S} {6,S}
6 *3 O       0 {5,S} {7,S}
7    H       0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "R4OOH_DSS",
    group = 
"""
1 *1 Cd      1 {2,D}
2 *4 Cd      0 {1,D} {3,S}
3    {Cd,Cs} 0 {2,S} {4,S}
4    {Cd,Cs} 0 {3,S} {5,S}
5 *2 O       0 {4,S} {6,S}
6 *3 O       0 {5,S} {7,S}
7    H       0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "R4OOH_DSD",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3    Cd 0 {2,S} {4,D}
4    Cd 0 {3,D} {5,S}
5 *2 O  0 {4,S} {6,S}
6 *3 O  0 {5,S} {7,S}
7    H  0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "Cd_rad_out",
    group = 
"""
1 *1 Cd 1 {2,D}
2    Cd 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
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
    index = 19,
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
    index = 20,
    label = "CdsingleND_rad_out",
    group = 
"""
1 *1 Cd     1 {2,S}
2    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
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
    index = 22,
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
    index = 23,
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
    index = 24,
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
    index = 25,
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
    index = 26,
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
    index = 27,
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
    index = 28,
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
    index = 29,
    label = "C_rad_out_NonDe",
    group = 
"""
1 *1 C      1 {2,S} {3,S}
2    {Cs,O} 0 {1,S}
3    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
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
    index = 31,
    label = "C_rad_out_NDMustO",
    group = 
"""
1 *1 C      1 {2,S} {3,S}
2    O      0 {1,S}
3    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C_rad_out_OneDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
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
    index = 34,
    label = "C_rad_out_OneDe/O",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    O             0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
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

tree(
"""
L1: RnOOH
    L2: ROOH
    L2: R2OOH
        L3: R2OOH_S
        L3: R2OOH_D
    L2: R3OOH
        L3: R3OOH_SS
        L3: R3OOH_SD
        L3: R3OOH_DS
    L2: R4OOH
        L3: R4OOH_SSS
        L3: R4OOH_SSD
        L3: R4OOH_SDS
        L3: R4OOH_DSS
        L3: R4OOH_DSD
L1: Y_rad_out
    L2: Cd_rad_out
    L2: Cdsingle_rad_out
        L3: CdsingleH_rad_out
        L3: CdsingleND_rad_out
        L3: CdsingleDe_rad_out
    L2: C_rad_out_single
        L3: C_rad_out_2H
        L3: C_rad_out_1H
            L4: C_rad_out_H/NonDeC
            L4: C_rad_out_H/NonDeO
            L4: C_rad_out_H/OneDe
        L3: C_rad_out_noH
            L4: C_rad_out_NonDe
                L5: C_rad_out_Cs2
                L5: C_rad_out_NDMustO
            L4: C_rad_out_OneDe
                L5: C_rad_out_OneDe/Cs
                L5: C_rad_out_OneDe/O
            L4: C_rad_out_TwoDe
"""
)

