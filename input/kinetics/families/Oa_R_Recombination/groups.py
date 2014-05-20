#!/usr/bin/env python
# encoding: utf-8

name = "Oa_R_Recombination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_rad", "Oa"], products=["YO."], ownReverse=False)

reverse = "RO_Bond_Dissociation"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Oa",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 O U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "H_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 H U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "Ct_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,T}
2    C U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "O_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U1 {2,S}
2    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "O_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U1 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "O_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O   U1 {2,S}
2    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "O_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O      U1 {2,S}
2    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "O_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O             U1 {2,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Cd_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2    C U0 {1,D}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Cd_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2    C U0 {1,D}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "Cd_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,D} {3,S}
2    C   U0 {1,D}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "Cd_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U1 {2,D} {3,S}
2    C      U0 {1,D}
3    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "Cd_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,D} {3,S}
2    C             U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "Cb_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U1 {2,B} {3,B}
2    {Cb,Cbf} U0 {1,B}
3    {Cb,Cbf} U0 {1,B}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "CO_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2    O U0 {1,D}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "CO_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2    O U0 {1,D}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "CO_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,D} {3,S}
2    O   U0 {1,D}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "CO_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U1 {2,D} {3,S}
2    O      U0 {1,D}
3    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "CO_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,D} {3,S}
2    O             U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "Cs_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    R U0 {1,S}
3    R U0 {1,S}
4    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C_methyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,S} {3,S} {4,S}
2    H   U0 {1,S}
3    H   U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C_rad/H2/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C_rad/H2/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    Cd U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C_rad/H2/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C_rad/H2/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C_rad/H2/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C_rad/H2/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,S} {3,S} {4,S}
2    H   U0 {1,S}
3    R!H U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C_rad/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C_rad/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U1 {2,S} {3,S} {4,S}
2    H      U0 {1,S}
3    O      U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C_rad/H/CsO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cs U0 {1,S}
4    O  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C_rad/H/O2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    O U0 {1,S}
4    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C_rad/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C_rad/H/OneDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C_rad/H/OneDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C_rad/H/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C_ter_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,S} {3,S} {4,S}
2    R!H U0 {1,S}
3    R!H U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U1 {2,S} {3,S} {4,S}
2    {Cs,O} U0 {1,S}
3    {Cs,O} U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C_rad/Cs3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    Cs U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C_rad/NDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U1 {2,S} {3,S} {4,S}
2    O      U0 {1,S}
3    {Cs,O} U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cs,O}        U0 {1,S}
4    {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C_rad/Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Cs            U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C_rad/ODMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    O             U0 {1,S}
4    {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C_rad/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C_rad/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C_rad/TDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C_rad/ThreeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: Y_rad
    L2: H_rad
    L2: Ct_rad
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
    L2: Cd_rad
        L3: Cd_pri_rad
        L3: Cd_sec_rad
            L4: Cd_rad/NonDe
            L4: Cd_rad/OneDe
    L2: Cb_rad
    L2: CO_rad
        L3: CO_pri_rad
        L3: CO_sec_rad
            L4: CO_rad/NonDe
            L4: CO_rad/OneDe
    L2: Cs_rad
        L3: C_methyl
        L3: C_pri_rad
            L4: C_rad/H2/Cs
            L4: C_rad/H2/Cd
            L4: C_rad/H2/Ct
            L4: C_rad/H2/Cb
            L4: C_rad/H2/CO
            L4: C_rad/H2/O
        L3: C_sec_rad
            L4: C_rad/H/NonDeC
            L4: C_rad/H/NonDeO
                L5: C_rad/H/CsO
                L5: C_rad/H/O2
            L4: C_rad/H/OneDe
                L5: C_rad/H/OneDeC
                L5: C_rad/H/OneDeO
            L4: C_rad/H/TwoDe
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
L1: Oa
"""
)

forbidden(
    label = "O2_birad",
    multiplicity = [3],
    group = 
"""
1 *1 O U1 {2,S}
2    O U1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "O_(S)",
    multiplicity = [1],
    group = 
"""
1 *1 O U2 L2
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

