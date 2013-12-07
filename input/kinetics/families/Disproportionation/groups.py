#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_rad_birad_trirad_quadrad", "XH_Rrad_birad"], products=["Y_H", "X_R"], ownReverse=False)

reverse = "Molecular_Addition"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*4'],
    ['BREAK_BOND', '*2', 'S', '*4'],
    ['CHANGE_BOND', '*2', '1', '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_1centerquadrad, Y_1centertrirad, Y_2centerbirad, Y_1centerbirad, Y_rad}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "XH_Rrad",
    group = 
"""
1 *2 R!H 0 {2,S} {3,S}
2 *3 R!H 1 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "Y_1centerbirad",
    group = 
"""
1 *1 R!H 2
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "O_atom_triplet",
    group = 
"""
1 *1 O 2T
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "CH2_triplet",
    group = 
"""
1 *1 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "Y_rad",
    group = 
"""
1 *1 R 1 {2,S}
2    R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "H_rad",
    group = 
"""
1 *1 H 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "Ct_rad/Ct",
    group = 
"""
1 *1 C 1 {2,T}
2    C 0 {1,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "O_rad",
    group = 
"""
1 *1 O 1 {2,S}
2    R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "O_pri_rad",
    group = 
"""
1 *1 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "O_sec_rad",
    group = 
"""
1 *1 O   1 {2,S}
2    R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "O_rad/NonDeC",
    group = 
"""
1 *1 O  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "O_rad/NonDeO",
    group = 
"""
1 *1 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "O_rad/OneDe",
    group = 
"""
1 *1 O             1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "S_rad",
    group = 
"""
1 *1 S 1 {2,S}
2    R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "S_pri_rad",
    group = 
"""
1 *1 S 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "S_sec_rad",
    group = 
"""
1 *1 S   1 {2,S}
2    R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "S_rad/NonDeC",
    group = 
"""
1 *1 S  1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "S_rad/NonDeS",
    group = 
"""
1 *1 S 1 {2,S}
2    S 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "S_rad/OneDe",
    group = 
"""
1 *1 S             1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "Cd_rad",
    group = 
"""
1 *1 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "Cd_pri_rad",
    group = 
"""
1 *1 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "Cd_sec_rad",
    group = 
"""
1 *1 C   1 {2,D} {3,S}
2    C   0 {1,D}
3    R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "Cd_rad/NonDeC",
    group = 
"""
1 *1 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "Cd_rad/NonDeO",
    group = 
"""
1 *1 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "Cd_rad/OneDe",
    group = 
"""
1 *1 C             1 {2,D} {3,S}
2    C             0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "Cb_rad",
    group = 
"""
1 *1 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "CO_rad",
    group = 
"""
1 *1 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "CO_pri_rad",
    group = 
"""
1 *1 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "CO_sec_rad",
    group = 
"""
1 *1 C   1 {2,D} {3,S}
2    O   0 {1,D}
3    R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "CO_rad/NonDe",
    group = 
"""
1 *1 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "CO_rad/OneDe",
    group = 
"""
1 *1 C             1 {2,D} {3,S}
2    O             0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "Cs_rad",
    group = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "C_methyl",
    group = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "C_pri_rad",
    group = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "C_rad/H2/Cs",
    group = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "C_rad/H2/Cd",
    group = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "C_rad/H2/Ct",
    group = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "C_rad/H2/Cb",
    group = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "C_rad/H2/CO",
    group = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "C_rad/H2/O",
    group = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "C_sec_rad",
    group = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 *1 C        1 {2,S} {3,S} {4,S}
2    H        0 {1,S}
3    O        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "C_rad/H/CsO",
    group = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    O  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "C_rad/H/O2",
    group = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    O 0 {1,S}
4    O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "C_rad/H/NonDeS",
    group = 
"""
1 *1 C      1 {2,S} {3,S} {4,S}
2    H      0 {1,S}
3    S      0 {1,S}
4    {Cs,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "C_rad/H/CsS",
    group = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "C_rad/H/S2",
    group = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    S 0 {1,S}
4    S 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "C_rad/H/OneDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O,S}      0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "C_rad/H/OneDeO",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    O             0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "C_ter_rad",
    group = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "C_rad/NonDeC",
    group = 
"""
1 *1 C        1 {2,S} {3,S} {4,S}
2    {Cs,O,S} 0 {1,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "C_rad/Cs3",
    group = 
"""
1 *1 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "C_rad/NDMustO",
    group = 
"""
1 *1 C        1 {2,S} {3,S} {4,S}
2    O        0 {1,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "C_rad/OneDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cs,O,S}      0 {1,S}
4    {Cs,O,S}      0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "C_rad/Cs2",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Cs            0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "C_rad/ODMustO",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    O             0 {1,S}
4    {Cs,O,S}      0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "C_rad/TwoDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O,S}      0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "C_rad/Cs",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    Cs            0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "C_rad/TDMustO",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    O             0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "C_rad/ThreeDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "Cdpri_Rrad",
    group = 
"""
1 *2 Cd             0 {2,S} {3,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "Cdpri_Csrad",
    group = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "Cdpri_Cdrad",
    group = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 Cd 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "Cdpri_COrad",
    group = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 CO 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "Cdpri_Orad",
    group = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 O  1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "COpri_Rrad",
    group = 
"""
1 *2 CO             0 {2,S} {3,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "COpri_Csrad",
    group = 
"""
1 *2 CO 0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "COpri_Cdrad",
    group = 
"""
1 *2 CO 0 {2,S} {3,S}
2 *3 Cd 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "COpri_COrad",
    group = 
"""
1 *2 CO 0 {2,S} {3,S}
2 *3 CO 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "COpri_Orad",
    group = 
"""
1 *2 CO 0 {2,S} {3,S}
2 *3 O  1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "O_Rrad",
    group = 
"""
1 *2 O              0 {2,S} {3,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "O_Csrad",
    group = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "O_Cdrad",
    group = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 Cd 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "O_COrad",
    group = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 CO 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "O_Orad",
    group = 
"""
1 *2 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "S_Rrad",
    group = 
"""
1 *2 S         0 {2,S} {3,S}
2 *3 {Cs,Cd,S} 1 {1,S}
3 *4 H         0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "S_Csrad",
    group = 
"""
1 *2 S  0 {2,S} {3,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "S_Cdrad",
    group = 
"""
1 *2 S  0 {2,S} {3,S}
2 *3 Cd 1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "S_Srad",
    group = 
"""
1 *2 S 0 {2,S} {3,S}
2 *3 S 1 {1,S}
3 *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "Cmethyl_Rrad",
    group = 
"""
1 *2 C              0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
4    H              0 {1,S}
5    H              0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "Cmethyl_Csrad",
    group = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 1 {1,S}
3 *4 H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "Cmethyl_Cdrad",
    group = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd 1 {1,S}
3 *4 H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "Cmethyl_COrad",
    group = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO 1 {1,S}
3 *4 H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "Cmethyl_Orad",
    group = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 O 1 {1,S}
3 *4 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "Cmethyl_Srad",
    group = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 S 1 {1,S}
3 *4 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "Cpri_Rrad",
    group = 
"""
1 *2 C              0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
4    H              0 {1,S}
5    R!H            0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "C/H2/Nd_Rrad",
    group = 
"""
1 *2 C              0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
4    H              0 {1,S}
5    {Cs,O,S}       0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    label = "C/H2/Nd_Csrad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs       1 {1,S}
3 *4 H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "C/H2/Nd_Cdrad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd       1 {1,S}
3 *4 H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    label = "C/H2/Nd_COrad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO       1 {1,S}
3 *4 H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "C/H2/Nd_Orad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 O        1 {1,S}
3 *4 H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "C/H2/De_Rrad",
    group = 
"""
1 *2 C              0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
4    H              0 {1,S}
5    {Cd,Ct,Cb,CO}  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    label = "C/H2/De_Csrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs            1 {1,S}
3 *4 H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "C/H2/De_Cdrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd            1 {1,S}
3 *4 H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "C/H2/De_COrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO            1 {1,S}
3 *4 H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "C/H2/De_Orad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 O             1 {1,S}
3 *4 H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "Csec_Rrad",
    group = 
"""
1 *2 C              0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
4    R!H            0 {1,S}
5    R!H            0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "C/H/NdNd_Rrad",
    group = 
"""
1 *2 C              0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
4    {Cs,O,S}       0 {1,S}
5    {Cs,O,S}       0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    label = "C/H/NdNd_Csrad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs       1 {1,S}
3 *4 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    label = "C/H/NdNd_Cdrad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd       1 {1,S}
3 *4 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    label = "C/H/NdNd_COrad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO       1 {1,S}
3 *4 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    label = "C/H/NdNd_Orad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 O        1 {1,S}
3 *4 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    label = "C/H/NdDe_Rrad",
    group = 
"""
1 *2 C              0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
4    {Cs,O,S}       0 {1,S}
5    {Cd,Ct,Cb,CO}  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    label = "C/H/NdDe_Csrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs            1 {1,S}
3 *4 H             0 {1,S}
4    {Cs,O,S}      0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "C/H/NdDe_Cdrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd            1 {1,S}
3 *4 H             0 {1,S}
4    {Cs,O,S}      0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    label = "C/H/NdDe_COrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO            1 {1,S}
3 *4 H             0 {1,S}
4    {Cs,O,S}      0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    label = "C/H/NdDe_Orad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 O             1 {1,S}
3 *4 H             0 {1,S}
4    {Cs,O,S}      0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    label = "C/H/DeDe_Rrad",
    group = 
"""
1 *2 C              0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S} 1 {1,S}
3 *4 H              0 {1,S}
4    {Cd,Ct,Cb,CO}  0 {1,S}
5    {Cd,Ct,Cb,CO}  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "C/H/DeDe_Csrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs            1 {1,S}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "C/H/DeDe_Cdrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd            1 {1,S}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    label = "C/H/DeDe_COrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO            1 {1,S}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    label = "C/H/DeDe_Orad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 O             1 {1,S}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, CH_quartet, CH_doublet}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 201,
    label = "N3_atom_quartet",
    group = 
"""
1 *1 N3s 3
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 202,
    label = "CH_quartet",
    group = 
"""
1 *1 C 3 {2,s}
2    H 0 {1,s}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 203,
    label = "Y_2centerbirad",
    group = "OR{O2b, C2b}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 204,
    label = "O2b",
    group = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 205,
    label = "C2b",
    group = 
"""
1 *1 C 1 {2,T}
2    C 1 {1,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 206,
    label = "CO_birad",
    group = 
"""
1 *1 C  2 {2,D}
2    Od 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 207,
    label = "NH_triplet",
    group = 
"""
1 *1 N3s 2T {2,S}
2    H   0  {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 208,
    label = "Ct_rad",
    group = 
"""
1 *1 Ct  1 {2,T}
2    R!H 0 {1,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 209,
    label = "Ct_rad/Nt",
    group = 
"""
1 *1 Ct        1 {2,T}
2    {N3t,N5t} 0 {1,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 210,
    label = "O_rad/NonDeN",
    group = 
"""
1 *1 O   1 {2,S}
2    N3s 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 211,
    label = "Cd_rad/NonDeN",
    group = 
"""
1 *1 C   1 {2,D} {3,S}
2    C   0 {1,D}
3    N3s 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 212,
    label = "C_rad/H2/N",
    group = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    N 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 213,
    label = "C_rad/H/NonDeN",
    group = 
"""
1 *1 C        1 {2,S} {3,S} {4,S}
2    H        0 {1,S}
3    N        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 214,
    label = "C_rad/H/OneDeN",
    group = 
"""
1 *1 C             1 {2,S} {3,S} {4,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    N             0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 215,
    label = "N3_rad",
    group = 
"""
1 *1 {N3s,N3d} 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 216,
    label = "N3s_rad",
    group = 
"""
1 *1 N3s 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 217,
    label = "NH2_rad",
    group = 
"""
1 *1 N3s 1 {2,S} {3,S}
2    H   0 {1,S}
3    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 218,
    label = "N3s_rad_pri",
    group = 
"""
1 *1 N3s 1 {2,S} {3,S}
2    R!H 0 {1,S}
3    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 219,
    label = "N3s_rad/H/NonDe",
    group = 
"""
1 *1 N3s         1 {2,S} {3,S}
2    {Cs,N3s,Os} 0 {1,S}
3    H           0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 220,
    label = "N3s_rad/H/NonDeC",
    group = 
"""
1 *1 N3s 1 {2,S} {3,S}
2    Cs  0 {1,S}
3    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 221,
    label = "N3s_rad/H/NonDeO",
    group = 
"""
1 *1 N3s 1 {2,S} {3,S}
2    Os  0 {1,S}
3    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 222,
    label = "N3s_rad/H/NonDeN",
    group = 
"""
1 *1 N3s 1 {2,S} {3,S}
2    N3s 0 {1,S}
3    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 223,
    label = "N3s_rad/H/OneDe",
    group = 
"""
1 *1 N3s                      1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
3    H                        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 224,
    label = "N3s_rad_sec",
    group = 
"""
1 *1 N3s 1 {2,S} {3,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 225,
    label = "N3s_rad/NonDe2",
    group = 
"""
1 *1 N3s         1 {2,S} {3,S}
2    {Cs,N3s,Os} 0 {1,S}
3    {Cs,N3s,Os} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 226,
    label = "N3s_rad/OneDe",
    group = 
"""
1 *1 N3s                      1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
3    {Cs,N3s,Os}              0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 227,
    label = "N3s_rad/TwoDe",
    group = 
"""
1 *1 N3s                      1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 228,
    label = "N3d_rad",
    group = 
"""
1 *1 N3d 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 229,
    label = "N3d_rad/C",
    group = 
"""
1 *1 N3d 1 {2,D}
2    C   0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 230,
    label = "N3d_rad/O",
    group = 
"""
1 *1 N3d 1 {2,D}
2    Od  0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 231,
    label = "N3d_rad/N",
    group = 
"""
1 *1 N3d 1 {2,D}
2    N   0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 232,
    label = "N5_rad",
    group = 
"""
1 *1 {N5d,N5dd,N5t} 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 233,
    label = "N5d_rad",
    group = 
"""
1 *1 N5d 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 234,
    label = "XH_Rrad_birad",
    group = "OR{XH_Rrad, XH_Rbirad}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 235,
    label = "XH_Rbirad",
    group = 
"""
1 *2 R!H 0 {2,{S,D}} {3,S}
2 *3 R!H 2 {1,{S,D}}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 236,
    label = "XH_s_Rrad",
    group = 
"""
1 *2 R!H 0 {2,S} {3,S}
2 *3 R!H 1 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 237,
    label = "Cdpri_Nrad",
    group = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 N  1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 238,
    label = "COpri_Nrad",
    group = 
"""
1 *2 CO 0 {2,S} {3,S}
2 *3 N  1 {1,S}
3 *4 H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 239,
    label = "O_Nrad",
    group = 
"""
1 *2 O 0 {2,S} {3,S}
2 *3 N 1 {1,S}
3 *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 240,
    label = "Cmethyl_Nrad",
    group = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 N 1 {1,S}
3 *4 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 241,
    label = "C/H2/Nd_Nrad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 N3s      1 {1,S}
3 *4 H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 242,
    label = "C/H2/De_Nrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 N             1 {1,S}
3 *4 H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 243,
    label = "C/H/NdNd_Nrad",
    group = 
"""
1 *2 C        0 {2,S} {3,S} {4,S} {5,S}
2 *3 N        1 {1,S}
3 *4 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 244,
    label = "C/H/NdDe_Nrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 N             1 {1,S}
3 *4 H             0 {1,S}
4    {Cs,O,S}      0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 245,
    label = "C/H/DeDe_Nrad",
    group = 
"""
1 *2 C             0 {2,S} {3,S} {4,S} {5,S}
2 *3 N             1 {1,S}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 246,
    label = "NH_s_Rrad",
    group = 
"""
1 *2 N 0 {2,S} {3,S}
2 *3 R 1 {1,S}
3 *4 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 247,
    label = "N3H_s_Rrad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S}
2 *3 R   1 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 248,
    label = "N3s/H2_s_Rrad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S} {4,S}
2 *3 R   1 {1,S}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 249,
    label = "N3s/H2_s_Crad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S} {4,S}
2 *3 C   1 {1,S}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 250,
    label = "N3s/H2_s_Cssrad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S} {4,S}
2 *3 Cs  1 {1,S}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 251,
    label = "N3s/H2_s_Cdsrad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S} {4,S}
2 *3 Cd  1 {1,S}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 252,
    label = "N3s/H2_s_Orad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S} {4,S}
2 *3 O   1 {1,S}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 253,
    label = "N3s/H2_s_Nrad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S} {4,S}
2 *3 N   1 {1,S}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 254,
    label = "N3s/H/NonDe_s_Rrad",
    group = 
"""
1 *2 N3s         0 {2,S} {3,S} {4,S}
2 *3 N           1 {1,S}
3 *4 H           0 {1,S}
4    {Cs,N3s,Os} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 255,
    label = "N3s/H/Deloc_s_Rrad",
    group = 
"""
1 *2 N3s           0 {2,S} {3,S} {4,S}
2 *3 N             1 {1,S}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 256,
    label = "N5H_s_Rrad",
    group = 
"""
1 *2 {N5s,N5d} 0 {2,S} {3,S}
2 *3 R         1 {1,S}
3 *4 H         0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 257,
    label = "XH_d_Rrad",
    group = 
"""
1 *2 R!H 0 {2,D} {3,S}
2 *3 R!H 1 {1,D}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 258,
    label = "CH_d_Rrad",
    group = 
"""
1 *2 C   0 {2,D} {3,S}
2 *3 R!H 1 {1,D}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 259,
    label = "Cds/H2_d_Rrad",
    group = 
"""
1 *2 C   0 {2,D} {3,S} {4,S}
2 *3 R!H 1 {1,D}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 260,
    label = "Cds/H2_d_Crad",
    group = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2 *3 C 1 {1,D}
3 *4 H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 261,
    label = "Cds/H2_d_N3rad",
    group = 
"""
1 *2 C   0 {2,D} {3,S} {4,S}
2 *3 N3d 1 {1,D}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 262,
    label = "Cds/H2_d_N5rad",
    group = 
"""
1 *2 C              0 {2,D} {3,S} {4,S}
2 *3 {N5d,N5dd,N5t} 1 {1,D}
3 *4 H              0 {1,S}
4    H              0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 263,
    label = "Cds/H2_d_N5drad",
    group = 
"""
1 *2 C   0 {2,D} {3,S} {4,S}
2 *3 N5d 1 {1,D}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 264,
    label = "Cds/H2_d_N5ddrad",
    group = 
"""
1 *2 C    0 {2,D} {3,S} {4,S}
2 *3 N5dd 1 {1,D}
3 *4 H    0 {1,S}
4    H    0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 265,
    label = "Cds/H2_d_N5ddrad/C",
    group = 
"""
1 *2 C    0 {2,D} {3,S} {4,S}
2 *3 N5dd 1 {1,D} {5,D}
3 *4 H    0 {1,S}
4    H    0 {1,S}
5    C    0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 266,
    label = "Cds/H2_d_N5ddrad/O",
    group = 
"""
1 *2 C    0 {2,D} {3,S} {4,S}
2 *3 N5dd 1 {1,D} {5,D}
3 *4 H    0 {1,S}
4    H    0 {1,S}
5    O    0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 267,
    label = "Cds/H2_d_N5ddrad/N",
    group = 
"""
1 *2 C    0 {2,D} {3,S} {4,S}
2 *3 N5dd 1 {1,D} {5,D}
3 *4 H    0 {1,S}
4    H    0 {1,S}
5    N    0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 268,
    label = "Cds/H/NonDe_d_Rrad",
    group = 
"""
1 *2 C           0 {2,D} {3,S} {4,S}
2 *3 R!H         1 {1,D}
3 *4 H           0 {1,S}
4    {Cs,N3s,Os} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 269,
    label = "Cds/H/Deloc_d_Rrad",
    group = 
"""
1 *2 C             0 {2,D} {3,S} {4,S}
2 *3 R!H           1 {1,D}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 270,
    label = "NH_d_Rrad",
    group = 
"""
1 *2 N   0 {2,D} {3,S}
2 *3 R!H 1 {1,D}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 271,
    label = "N3d/H_d_Rrad",
    group = 
"""
1 *2 N3d 0 {2,D} {3,S}
2 *3 R!H 1 {1,D}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 272,
    label = "N3d/H_d_Crad",
    group = 
"""
1 *2 N3d 0 {2,D} {3,S}
2 *3 C   1 {1,D}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 273,
    label = "N3d/H_d_Nrad",
    group = 
"""
1 *2 N3d 0 {2,D} {3,S}
2 *3 N   1 {1,D}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)
 
entry(
    index = 274,
    label = "N5d/H_d_Rrad",
    group = 
"""
1 *2 N3d 0 {2,D} {3,S}
2 *3 R!H 1 {1,D}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 275,
    label = "N5dd/H_d_Rrad",
    group = 
"""
1 *2 N3d 0 {2,D} {3,S}
2 *3 R!H 1 {1,D}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)   
    
entry(
    index = 276,
    label = "XH_Rbirad",
    group = 
"""
1 *2 R!H 0 {2,{S,D}} {3,S}
2 *3 R!H 2 {1,{S,D}}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 277,
    label = "XH_s_Rbirad",
    group = 
"""
1 *2 R!H 0 {2,S} {3,S}
2 *3 R!H 2 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 278,
    label = "CH_s_Rbirad",
    group = 
"""
1 *2 C   0 {2,S} {3,S}
2 *3 R!H 2 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 279,
    label = "NH_s_Rbirad",
    group = 
"""
1 *2 N   0 {2,S} {3,S}
2 *3 R!H 2 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 280,
    label = "N3H_s_Rbirad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S}
2 *3 R!H 2 {1,S}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 281,
    label = "N3s/H2_s_Rbirad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S} {4,S}
2 *3 R!H 2 {1,S}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 282,
    label = "N3s/H2_s_Cbirad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S} {4,S}
2 *3 C   2 {1,S}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 283,
    label = "N3s/H2_s_Nbirad",
    group = 
"""
1 *2 N3s 0 {2,S} {3,S} {4,S}
2 *3 N   2 {1,S}
3 *4 H   0 {1,S}
4    H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 284,
    label = "N3s/H/NonDe_s_Rbirad",
    group = 
"""
1 *2 N3s         0 {2,S} {3,S} {4,S}
2 *3 N           2 {1,S}
3 *4 H           0 {1,S}
4    {Cs,N3s,Os} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 285,
    label = "N3s/H/Deloc_s_Rbirad",
    group = 
"""
1 *2 N3s           0 {2,S} {3,S} {4,S}
2 *3 N             2 {1,S}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 286,
    label = "N5H_s_Rbirad",
    group = 
"""
1 *2 {N5s,N5d}     0 {2,S} {3,S} {4,S}
2 *3 N             2 {1,S}
3 *4 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)
              
entry(
    index = 287,
    label = "XH_d_Rbirad",
    group = 
"""
1 *2 R!H 0 {2,D} {3,S}
2 *3 R!H 2 {1,D}
3 *4 H   0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 288,
    label = "C_quintet",
    group = 
"""
1 *1 C 4V
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 289,
    label = "C_triplet",
    group = 
"""
1 *1 C 4T
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 290,
    label = "C_singlet",
    group = 
"""
1 *1 C 4S
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 291,
    label = "N_atom_quartet",
    group = 
"""
1 *1 N 3Q
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 292,
    label = "N_atom_doublet",
    group = 
"""
1 *1 N 3D
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 293,
    label = "CH_quartet",
    group = 
"""
1 *1 C 3Q {2,S}
2    H 0  {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 294,
    label = "CH_doublet",
    group = 
"""
1 *1 C 3D {2,S}
2    H 0  {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 295,
    label = "O_atom_singlet",
    group = 
"""
1 *1 O 2S
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 296,
    label = "CH2_singlet",
    group = 
"""
1 *1 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 297,
    label = "NH_singlet",
    group = 
"""
1 *1 N 2S {2,S}
2    H 0  {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 298,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet, C_singlet}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Nov  4 10:25:25 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

tree(
"""
L1: Y_rad_birad_trirad_quadrad
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
        L3: C_singlet
    L2: Y_1centertrirad
        L3: N_atom_quartet
        L3: N_atom_doublet
        L3: CH_quartet
        L3: CH_doublet
    L2: Y_2centerbirad    
        L3: O2b
        L3: C2b
    L2: Y_1centerbirad
        L3: CO_birad
        L3: O_atom_triplet
        L3: O_atom_singlet
        L3: CH2_triplet
        L3: CH2_singlet
        L3: NH_triplet
        L3: NH_singlet
    L2: H_rad
    L2: Y_rad
        L3: Ct_rad
            L4: Ct_rad/Ct
            L4: Ct_rad/Nt
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                L5: O_rad/NonDeO
                L5: O_rad/NonDeN
                L5: O_rad/OneDe
        L3: S_rad
            L4: S_pri_rad
            L4: S_sec_rad
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/OneDe
        L3: Cd_rad
            L4: Cd_pri_rad
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                L5: Cd_rad/NonDeN
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
                L5: C_rad/H2/N
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                L5: C_rad/H/NonDeO
                L5: C_rad/H/NonDeN
                    L6: C_rad/H/CsO
                    L6: C_rad/H/O2
                L5: C_rad/H/NonDeS
                    L6: C_rad/H/CsS
                    L6: C_rad/H/S2
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                    L6: C_rad/H/OneDeO
                    L6: C_rad/H/OneDeN
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
        L3: N3_rad                    
            L4: N3s_rad                
                L5: NH2_rad            
                L5: N3s_rad_pri            
                    L6: N3s_rad/H/NonDe        
                        L7: N3s_rad/H/NonDeC    
                        L7: N3s_rad/H/NonDeO    
                        L7: N3s_rad/H/NonDeN    
                    L6: N3s_rad/H/OneDe        
                L5: N3s_rad_sec            
                    L6: N3s_rad/NonDe2        
                    L6: N3s_rad/OneDe        
                    L6: N3s_rad/TwoDe        
            L4: N3d_rad                           
                L5: N3d_rad/C        
                L5: N3d_rad/O        
                L5: N3d_rad/N            
        L3: N5_rad                    
            L4: N5d_rad          
L1: XH_Rrad_birad
    L2: XH_Rrad
        L3: XH_s_Rrad
            L4: Cdpri_Rrad
                L5: Cdpri_Csrad
                L5: Cdpri_Cdrad
                L5: Cdpri_COrad
                L5: Cdpri_Orad
                L5: Cdpri_Nrad
            L4: COpri_Rrad
                L5: COpri_Csrad
                L5: COpri_Cdrad
                L5: COpri_COrad
                L5: COpri_Orad
                L5: COpri_Nrad
            L4: O_Rrad
                L5: O_Csrad
                L5: O_Cdrad
                L5: O_COrad
                L5: O_Orad
                L5: O_Nrad
            L4: S_Rrad
                L5: S_Csrad
                L5: S_Cdrad
                L5: S_Srad
            L4: Cmethyl_Rrad
                L5: Cmethyl_Csrad
                L5: Cmethyl_Cdrad
                L5: Cmethyl_COrad
                L5: Cmethyl_Orad
                L5: Cmethyl_Srad
                L5: Cmethyl_Nrad
            L4: Cpri_Rrad
                L5: C/H2/Nd_Rrad
                    L6: C/H2/Nd_Csrad
                    L6: C/H2/Nd_Cdrad
                    L6: C/H2/Nd_COrad
                    L6: C/H2/Nd_Orad
                    L6: C/H2/Nd_Nrad
                L5: C/H2/De_Rrad
                    L6: C/H2/De_Csrad
                    L6: C/H2/De_Cdrad
                    L6: C/H2/De_COrad
                    L6: C/H2/De_Orad
                    L6: C/H2/De_Nrad
            L4: Csec_Rrad
                L5: C/H/NdNd_Rrad
                    L6: C/H/NdNd_Csrad
                    L6: C/H/NdNd_Cdrad
                    L6: C/H/NdNd_COrad
                    L6: C/H/NdNd_Orad
                    L6: C/H/NdNd_Nrad
                L5: C/H/NdDe_Rrad
                    L6: C/H/NdDe_Csrad
                    L6: C/H/NdDe_Cdrad
                    L6: C/H/NdDe_COrad
                    L6: C/H/NdDe_Orad
                    L6: C/H/NdDe_Nrad
                L5: C/H/DeDe_Rrad
                    L6: C/H/DeDe_Csrad
                    L6: C/H/DeDe_Cdrad
                    L6: C/H/DeDe_COrad
                    L6: C/H/DeDe_Orad
                    L6: C/H/DeDe_Nrad
            L4: NH_s_Rrad                    
                L5: N3H_s_Rrad                
                    L6: N3s/H2_s_Rrad            
                        L7: N3s/H2_s_Crad        
                            L8: N3s/H2_s_Cssrad    
                            L8: N3s/H2_s_Cdsrad    
                        L7: N3s/H2_s_Orad        
                        L7: N3s/H2_s_Nrad        
                    L6: N3s/H/NonDe_s_Rrad            
                    L6: N3s/H/Deloc_s_Rrad            
                L5: N5H_s_Rrad
        L3: XH_d_Rrad                    
            L4: CH_d_Rrad                
                L5: Cds/H2_d_Rrad            
                    L6: Cds/H2_d_Crad        
                    L6: Cds/H2_d_N3rad        
                    L6: Cds/H2_d_N5rad        
                        L7: Cds/H2_d_N5drad    
                        L7: Cds/H2_d_N5ddrad    
                            L8: Cds/H2_d_N5ddrad/C
                            L8: Cds/H2_d_N5ddrad/O
                            L8: Cds/H2_d_N5ddrad/N
                L5: Cds/H/NonDe_d_Rrad            
                L5: Cds/H/Deloc_d_Rrad            
            L4: NH_d_Rrad                
                L5: N3d/H_d_Rrad            
                    L6: N3d/H_d_Crad        
                    L6: N3d/H_d_Nrad        
                L5: N5d/H_d_Rrad            
                L5: N5dd/H_d_Rrad            
    L2: XH_Rbirad                        
        L3: XH_s_Rbirad                    
            L4: CH_s_Rbirad                
            L4: NH_s_Rbirad                
                L5: N3H_s_Rbirad            
                    L6: N3s/H2_s_Rbirad        
                        L7: N3s/H2_s_Cbirad    
                        L7: N3s/H2_s_Nbirad    
                    L6: N3s/H/NonDe_s_Rbirad        
                    L6: N3s/H/Deloc_s_Rbirad        
                L5: N5H_s_Rbirad            
        L3: XH_d_Rbirad
"""
)

forbidden(
    label = "O2d",
    group = 
"""
1 *2 O 0 {2,D}
2 *3 O 0 {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

forbidden(
    label = "O_Orad",
    group = 
"""
1 *2 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *4 H 0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

