#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["CO2", "RR'"], products=["R_(CO2)_R'"], ownReverse=False)

reverse = "1,2_Elimination_CO2"

recipe(actions=[
    ['BREAK_BOND', '*3', 'S', '*4'],
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*4'],
])

entry(
    index = 1,
    label = "CO2",
    group = "OR{CO2_Od, CO2_Cdd}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "RR'",
    group = "OR{R_H, R_R'}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CO2_Od",
    group = 
"""
1 *2 Cdd 0 {2,D} {3,D}
2 *1 Od  0 {1,D}
3    Od  0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CO2_Cdd",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    Od  0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R_H",
    group = 
"""
1 *3 {H,Cs,Cd,Cb,Sis,Sid,N} 0 {2,S}
2 *4 H                      0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "H2",
    group = 
"""
1 *3 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "Cb_H",
    group = 
"""
1 *3 Cb       0 {2,B} {3,S}
2    {Cb,Cbf} 0 {1,B}
3 *4 H        0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "Cd_H",
    group = 
"""
1 *3 Cd 0 {2,D} {3,S} {4,S}
2    Cd 0 {1,D}
3 *4 H  0 {1,S}
4    R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "Cd_pri",
    group = 
"""
1 *3 Cd 0 {2,D} {3,S} {4,S}
2    Cd 0 {1,D}
3 *4 H  0 {1,S}
4    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Cd_sec",
    group = 
"""
1 *3 Cd  0 {2,D} {3,S} {4,S}
2    Cd  0 {1,D}
3 *4 H   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Cd/H/NonDeC",
    group = 
"""
1 *3 Cd 0 {2,D} {3,S} {4,S}
2    Cd 0 {1,D}
3 *4 H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "Cd/H/NonDeO",
    group = 
"""
1 *3 Cd 0 {2,D} {3,S} {4,S}
2    Cd 0 {1,D}
3 *4 H  0 {1,S}
4    Os 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "Cd/H/OneDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2    Cd            0 {1,D}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "Cs_H",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    R  0 {1,S}
4    R  0 {1,S}
5    R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "C_methane",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C_pri",
    group = 
"""
1 *3 Cs  0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   0 {1,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    R!H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C_pri/NonDeC",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "C_pri/NonDeO",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Os 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "C_pri/De",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C_sec",
    group = 
"""
1 *3 Cs  0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "C/H2/NonDeC",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C/H2/NonDeO",
    group = 
"""
1 *3 Cs     0 {2,S} {3,S} {4,S} {5,S}
2 *4 H      0 {1,S}
3    H      0 {1,S}
4    O      0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C/H2/CsO",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    H  0 {1,S}
4    O  0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C/H2/O2",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    H  0 {1,S}
4    O  0 {1,S}
5    O  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C/H2/OneDe",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C/H2/OneDeC",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    Cs            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C/H2/OneDeO",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    O             0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C/H2/TwoDe",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    H             0 {1,S}
4    {Cd,Ct,CO,Cb} 0 {1,S}
5    {Cd,Ct,CO,Cb} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C_ter",
    group = 
"""
1 *3 Cs  0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C/H/NonDeC",
    group = 
"""
1 *3 Cs     0 {2,S} {3,S} {4,S} {5,S}
2 *4 H      0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C/H/Cs3",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C/H/NDMustO",
    group = 
"""
1 *3 Cs     0 {2,S} {3,S} {4,S} {5,S}
2 *4 H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C/H/OneDe",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C/H/Cs2",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
5    Cs            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C/H/ODMustO",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    O             0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C/H/TwoDe",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C/H/Cs",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Cs            0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C/H/TDMustO",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    O             0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C/H/ThreeDe",
    group = 
"""
1 *3 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "R_R'",
    group = 
"""
1 *3 {Cs,Sis,N}           0 {2,S} {3,S} {4,S} {5,S}
2 *4 {Cs,Cd,Cb,Sis,Sid,N} 0 {1,S}
3    H                    0 {1,S}
4    H                    0 {1,S}
5    H                    0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "Cs_Cs",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C_methyl_C_methyl",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs 0 {1,S} {6,S} {7,S} {8,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
7    H  0 {2,S}
8    H  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C_methyl_C_pri",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs 0 {1,S} {6,S} {7,S} {8,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
7    H  0 {2,S}
8    C  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C_methyl_C_sec",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs 0 {1,S} {6,S} {7,S} {8,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
7    C  0 {2,S}
8    C  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C_methyl_C_ter",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs 0 {1,S} {6,S} {7,S} {8,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    C  0 {2,S}
7    C  0 {2,S}
8    C  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "Cs_Cd",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cd 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C_methyl_Cd_pri",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cd 0 {1,S} {6,S} {7,D}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
7    C  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C_methyl_Cd_sec",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cd 0 {1,S} {6,S} {7,D}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    C  0 {2,S}
7    C  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "Cs_Cb",
    group = 
"""
1 *3 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cb 0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: CO2
    L2: CO2_Od
    L2: CO2_Cdd
L1: RR'
    L2: R_H
        L3: H2
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
                L5: C_pri/De
            L4: C_sec
                L5: C/H2/NonDeC
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                    L6: C/H2/O2
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

