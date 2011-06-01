#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation"
shortDesc = ""
longDesc = """

"""

template(reactants=["Y_rad_birad", "XH_Rrad"], products=["Y_H", "X_R"], ownReverse=False)

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*4'],
    ['BREAK_BOND', '*2', 'S', '*4'],
    ['CHANGE_BOND', '*2', '1', '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "Y_rad_birad",
    group = "OR{Y_1centerbirad, Y_rad}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "XH_Rrad",
    group = 
"""
1  *2 R!H 0 {2,S} {3,S}
2  *3 R!H 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "Y_1centerbirad",
    group = 
"""
1  *1 {Cs,Cd,O} 2T
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "O_atom_triplet",
    group = 
"""
1  *1 O 2T
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "CH2_triplet",
    group = 
"""
1  *1 C 2T {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "Y_rad",
    group = 
"""
1  *1 R 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "H_rad",
    group = 
"""
1  *1 H 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "O2_birad",
    group = 
"""
1  *1 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "C2b",
    group = 
"""
1  *1 C 1 {2,T}
2     C 1 {1,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "Ct_rad",
    group = 
"""
1  *1 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "O_rad",
    group = 
"""
1  *1 O 1 {2,S}
2     R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "O_pri_rad",
    group = 
"""
1  *1 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "O_sec_rad",
    group = 
"""
1  *1 O 1 {2,S}
2     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "O_rad/NonDeC",
    group = 
"""
1  *1 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "O_rad/NonDeO",
    group = 
"""
1  *1 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "O_rad/OneDe",
    group = 
"""
1  *1 O 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "Cd_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "Cd_pri_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "Cd_sec_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "Cd_rad/NonDeC",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "Cd_rad/NonDeO",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "Cd_rad/OneDe",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "Cb_rad",
    group = 
"""
1  *1 Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "CO_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "CO_pri_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "CO_sec_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "CO_rad/NonDe",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "CO_rad/OneDe",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "Cs_rad",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "C_methyl",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "C_pri_rad",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "C_rad/H2/Cs",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "C_rad/H2/Cd",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "C_rad/H2/Ct",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "C_rad/H2/Cb",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cb 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "C_rad/H2/CO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     CO 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "C_rad/H2/O",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "C_sec_rad",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "C_rad/H/NonDeC",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "C_rad/H/NonDeO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "C_rad/H/CsO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "C_rad/H/O2",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     O 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "C_rad/H/OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "C_rad/H/OneDeC",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "C_rad/H/OneDeO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "C_rad/H/TwoDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "C_ter_rad",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     R!H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "C_rad/NonDeC",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cs,O} 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "C_rad/Cs3",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "C_rad/NDMustO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "C_rad/OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "C_rad/Cs2",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "C_rad/ODMustO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "C_rad/TwoDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "C_rad/Cs",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "C_rad/TDMustO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "C_rad/ThreeDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "Cdpri_Rrad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "Cdpri_Csrad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "Cdpri_Cdrad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "Cdpri_COrad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "Cdpri_Orad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "COpri_Rrad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "COpri_Csrad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "COpri_Cdrad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "COpri_COrad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "COpri_Orad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "O_Rrad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 {Cs,Cd,CO} 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "O_Csrad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "O_Cdrad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "O_COrad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "Cmethyl_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "Cmethyl_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "Cmethyl_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "Cmethyl_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "Cmethyl_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "Cpri_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "C/H2/Nd_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "C/H2/Nd_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "C/H2/Nd_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "C/H2/Nd_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "C/H2/Nd_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "C/H2/De_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "C/H2/De_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "C/H2/De_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "C/H2/De_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "C/H2/De_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "Csec_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "C/H/NdNd_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "C/H/NdNd_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "C/H/NdNd_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "C/H/NdNd_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "C/H/NdNd_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    label = "C/H/NdDe_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "C/H/NdDe_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    label = "C/H/NdDe_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "C/H/NdDe_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "C/H/NdDe_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    label = "C/H/DeDe_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "C/H/DeDe_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "C/H/DeDe_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "C/H/DeDe_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "C/H/DeDe_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

tree(
"""
L1: Y_rad_birad
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CH2_triplet
    L2: Y_rad
        L3: H_rad
        L3: O2_birad
        L3: C2b
        L3: Ct_rad
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                L5: O_rad/NonDeO
                L5: O_rad/OneDe
        L3: Cd_rad
            L4: Cd_pri_rad
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                L5: Cd_rad/NonDeO
                L5: Cd_rad/OneDe
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                L5: C_rad/H2/Cd
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                    L6: C_rad/H/O2
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                    L6: C_rad/H/OneDeO
                L5: C_rad/H/TwoDe
            L4: C_ter_rad
                L5: C_rad/NonDeC
                    L6: C_rad/Cs3
                    L6: C_rad/NDMustO
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                    L6: C_rad/ODMustO
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                    L6: C_rad/TDMustO
                L5: C_rad/ThreeDe
L1: XH_Rrad
    L2: Cdpri_Rrad
        L3: Cdpri_Csrad
        L3: Cdpri_Cdrad
        L3: Cdpri_COrad
        L3: Cdpri_Orad
    L2: COpri_Rrad
        L3: COpri_Csrad
        L3: COpri_Cdrad
        L3: COpri_COrad
        L3: COpri_Orad
    L2: O_Rrad
        L3: O_Csrad
        L3: O_Cdrad
        L3: O_COrad
    L2: Cmethyl_Rrad
        L3: Cmethyl_Csrad
        L3: Cmethyl_Cdrad
        L3: Cmethyl_COrad
        L3: Cmethyl_Orad
    L2: Cpri_Rrad
        L3: C/H2/Nd_Rrad
            L4: C/H2/Nd_Csrad
            L4: C/H2/Nd_Cdrad
            L4: C/H2/Nd_COrad
            L4: C/H2/Nd_Orad
        L3: C/H2/De_Rrad
            L4: C/H2/De_Csrad
            L4: C/H2/De_Cdrad
            L4: C/H2/De_COrad
            L4: C/H2/De_Orad
    L2: Csec_Rrad
        L3: C/H/NdNd_Rrad
            L4: C/H/NdNd_Csrad
            L4: C/H/NdNd_Cdrad
            L4: C/H/NdNd_COrad
            L4: C/H/NdNd_Orad
        L3: C/H/NdDe_Rrad
            L4: C/H/NdDe_Csrad
            L4: C/H/NdDe_Cdrad
            L4: C/H/NdDe_COrad
            L4: C/H/NdDe_Orad
        L3: C/H/DeDe_Rrad
            L4: C/H/DeDe_Csrad
            L4: C/H/DeDe_Cdrad
            L4: C/H/DeDe_COrad
            L4: C/H/DeDe_Orad
"""
)

forbidden(
    label = "O2d",
    group = 
"""
1  *2 O 0 {2,D}
2  *3 O 0 {1,D}
""",
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
    ],
)

forbidden(
    label = "O_Orad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
""",
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
    ],
)

