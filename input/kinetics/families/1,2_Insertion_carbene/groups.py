#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/groups"
shortDesc = u""
longDesc = u"""
Reaction site *1 should always be a singlet in this family.
"""

template(reactants=["carbene", "RR'"], products=["R_CO_R'"], ownReverse=False)

reverse = "1,1_Elimination"

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['LOSE_PAIR', '*1', '1'],
])

entry(
    index = 4,
    label = "carbene",
    group = 
"""
1 *1 Cs u0 p1 {2,S} {3,S}
2    H  u0 p0 {1,S}
3    H  u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "RR'",
    group = "OR{R_H, R_R'}",
    kinetics = None,
)

entry(
    index = 5,
    label = "R_H",
    group = 
"""
1 *2 [H,Cs,Cd,Cb,Ct,O,Sis,Sid,N] u0 {2,S}
2 *3 H                           u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "H2",
    group = 
"""
1 *2 H u0 {2,S}
2 *3 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Ct_H",
    group = 
"""
1 *2 Ct u0 {2,S}
2 *3 H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
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
    index = 9,
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
    index = 6,
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
    index = 7,
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
    index = 8,
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
    index = 13,
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
    index = 14,
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
    index = 10,
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
    index = 11,
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
    index = 12,
    label = "Cd/H/OneDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S} {4,S}
2    C             u0 {1,D}
3 *3 H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
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
    index = 14,
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
    index = 15,
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
    index = 16,
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
    index = 17,
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
    index = 18,
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
    index = 19,
    label = "C_pri/De",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    H             u0 {1,S}
4    H             u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
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
    index = 26,
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
    index = 27,
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
    index = 21,
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
    index = 22,
    label = "C/H2/NonDeO",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H      u0 {1,S}
3    H      u0 {1,S}
4    O      u0 {1,S}
5    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
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
    index = 24,
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
    index = 25,
    label = "C/H2/OneDe",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    H             u0 {1,S}
4    [Cd,Ct,CO,Cb] u0 {1,S}
5    [Cs,O]        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "C/H2/OneDeC",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    H             u0 {1,S}
4    [Cd,Ct,CO,Cb] u0 {1,S}
5    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "C/H2/OneDeO",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    H             u0 {1,S}
4    [Cd,Ct,CO,Cb] u0 {1,S}
5    O             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "C/H2/TwoDe",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    H             u0 {1,S}
4    [Cd,Ct,CO,Cb] u0 {1,S}
5    [Cd,Ct,CO,Cb] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
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
    index = 30,
    label = "C/H/NonDeC",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H      u0 {1,S}
3    [Cs,O] u0 {1,S}
4    [Cs,O] u0 {1,S}
5    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
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
    index = 32,
    label = "C/H/NDMustO",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H      u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
5    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "C/H/OneDe",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cs,O]        u0 {1,S}
5    [Cs,O]        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "C/H/Cs2",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
5    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "C/H/ODMustO",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    O             u0 {1,S}
5    [Cs,O]        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "C/H/TwoDe",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cs,O]        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "C/H/Cs",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "C/H/TDMustO",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    O             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "C/H/ThreeDe",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "R_R'",
    group = 
"""
1 *2 [Cs,Sis,N]              u0 {2,S} {3,S} {4,S} {5,S}
2 *3 [Cs,Cd,Cb,Ct,Sis,Sid,N] u0 {1,S}
3    H                       u0 {1,S}
4    H                       u0 {1,S}
5    H                       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Cs_Cs",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "C_methyl_C_methyl",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 {1,S} {6,S} {7,S} {8,S}
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
    index = 43,
    label = "C_methyl_C_pri",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 {1,S} {6,S} {7,S} {8,S}
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
    index = 44,
    label = "C_methyl_C_sec",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 {1,S} {6,S} {7,S} {8,S}
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
    index = 45,
    label = "C_methyl_C_ter",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u0 {1,S} {6,S} {7,S} {8,S}
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
    index = 46,
    label = "Cs_Cd",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "C_methyl_Cd_pri",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 {1,S} {6,S} {7,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "C_methyl_Cd_sec",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u0 {1,S} {6,S} {7,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    C  u0 {2,S}
7    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Cs_Cb",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cb u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: carbene
L1: RR'
    L2: R_H
        L3: H2
        L3: Ct_H
            L4: acetylene
        L3: RO_H
            L4: CsO_H
        L3: Cd_H
            L4: Cd_pri
                L5: ethene
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/OneDe
        L3: Cb_H
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C_pri/NonDeC
                L5: C_pri/NonDeO
                L5: C_pri/De
                    L6: C_pri/Cd
                    L6: C_pri/Ct
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

