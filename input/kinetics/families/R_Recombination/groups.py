#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_rad", "Y_rad"], products=["Y_Y"], ownReverse=False)

reverse = "Bond_Dissociation"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_rad",
    group = 
"""
1 * R 1
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
    index = 2,
    label = "H_rad",
    group = 
"""
1 * H 1
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
    label = "S_rad",
    group = 
"""
1 * S 1
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
    label = "SJ",
    group = 
"""
1 * Ss 1
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
    label = "SsJ-H",
    group = 
"""
1 * Ss 1 {2,S}
2   H  0 {1,S}
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
    label = "SsJ-C",
    group = 
"""
1 * Ss 1 {2,S}
2   C  0 {1,S}
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
    label = "SsJ-Cs",
    group = 
"""
1 * Ss 1 {2,S}
2   Cs 0 {1,S}
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
    index = 8,
    label = "SsJ-Ct",
    group = 
"""
1 * Ss 1 {2,S}
2   Ct 0 {1,S}
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
    index = 9,
    label = "SsJ-Cb",
    group = 
"""
1 * Ss 1 {2,S}
2   Cb 0 {1,S}
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
    label = "SsJ-Cd",
    group = 
"""
1 * Ss 1 {2,S}
2   Cd 0 {1,S} {3,D}
3   C  0 {2,D}
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
    label = "SsJ-C=S",
    group = 
"""
1 * Ss 1 {2,S}
2   Cd 0 {1,S} {3,D}
3   Sd 0 {2,D}
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
    label = "SsJ-Ss",
    group = 
"""
1 * Ss 1 {2,S}
2   Ss 0 {1,S}
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
    label = "SsJ-Os",
    group = 
"""
1 * Ss 1 {2,S}
2   Os 0 {1,S}
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
    label = "Ct_rad/Ct",
    group = 
"""
1 * C 1 {2,T}
2   C 0 {1,T}
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
    label = "O_rad",
    group = 
"""
1 * O 1 {2,S}
2   R 0 {1,S}
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
    label = "O_pri_rad",
    group = 
"""
1 * O 1 {2,S}
2   H 0 {1,S}
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
    label = "O_sec_rad",
    group = 
"""
1 * O   1 {2,S}
2   R!H 0 {1,S}
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
    label = "O_rad/NonDe",
    group = 
"""
1 * O      1 {2,S}
2   {Cs,O} 0 {1,S}
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
    label = "O_rad/OneDe",
    group = 
"""
1 * O             1 {2,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "O2_birad",
    group = 
"""
1 * O 1 {2,S}
2   O 1 {1,S}
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
    label = "Cd_rad",
    group = 
"""
1 * C 1 {2,D} {3,S}
2   C 0 {1,D}
3   R 0 {1,S}
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
    label = "Cd_pri_rad",
    group = 
"""
1 * C 1 {2,D} {3,S}
2   C 0 {1,D}
3   H 0 {1,S}
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
    label = "Cd_sec_rad",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   C   0 {1,D}
3   R!H 0 {1,S}
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
    label = "Cd_rad/NonDe",
    group = 
"""
1 * C      1 {2,D} {3,S}
2   C      0 {1,D}
3   {Cs,O} 0 {1,S}
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
    label = "Cd_rad/OneDe",
    group = 
"""
1 * C             1 {2,D} {3,S}
2   C             0 {1,D}
3   {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "Cd_rad/Cd",
    group = 
"""
1 * C  1 {2,D} {3,S}
2   C  0 {1,D}
3   Cd 0 {1,S}
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
    label = "Cb_rad",
    group = 
"""
1 * Cb       1 {2,B} {3,B}
2   {Cb,Cbf} 0 {1,B}
3   {Cb,Cbf} 0 {1,B}
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
    label = "CO_rad",
    group = 
"""
1 * C 1 {2,D} {3,S}
2   O 0 {1,D}
3   R 0 {1,S}
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
    label = "CO_pri_rad",
    group = 
"""
1 * C 1 {2,D} {3,S}
2   O 0 {1,D}
3   H 0 {1,S}
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
    label = "CO_sec_rad",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   O   0 {1,D}
3   R!H 0 {1,S}
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
    label = "CO_rad/NonDe",
    group = 
"""
1 * C      1 {2,D} {3,S}
2   O      0 {1,D}
3   {Cs,O} 0 {1,S}
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
    label = "CO_rad/OneDe",
    group = 
"""
1 * C             1 {2,D} {3,S}
2   O             0 {1,D}
3   {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C=SJ",
    group = 
"""
1 * Cd 1 {2,D} {3,S}
2   Sd 0 {1,D}
3   R  0 {1,S}
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
    label = "C=SJ-H",
    group = 
"""
1 * Cd 1 {2,S} {3,D}
2   H  0 {1,S}
3   Sd 0 {1,D}
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
    label = "C=SJ-C",
    group = 
"""
1 * Cd 1 {2,S} {3,D}
2   C  0 {1,S}
3   Sd 0 {1,D}
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
    label = "C=SJ-Cs",
    group = 
"""
1 * Cd 1 {2,S} {3,D}
2   Cs 0 {1,S}
3   Sd 0 {1,D}
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
    label = "C=SJ-Ss",
    group = 
"""
1 * Cd 1 {2,S} {3,D}
2   Ss 0 {1,S}
3   Sd 0 {1,D}
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
    label = "Cs_rad",
    group = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   R 0 {1,S}
3   R 0 {1,S}
4   R 0 {1,S}
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
    label = "C_methyl",
    group = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   H 0 {1,S}
3   H 0 {1,S}
4   H 0 {1,S}
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
    label = "C_pri_rad",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   H   0 {1,S}
4   R!H 0 {1,S}
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
    label = "C_rad/H2/Cs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   Cs 0 {1,S}
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
    label = "C_rad/H2/Cd",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   Cd 0 {1,S}
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
    label = "C_rad/H2/Ct",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   Ct 0 {1,S}
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
    label = "C_rad/H2/Cb",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   Cb 0 {1,S}
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
    label = "C_rad/H2/CO",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   H  0 {1,S}
4   CO 0 {1,S}
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
    label = "C_rad/H2/O",
    group = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   H 0 {1,S}
3   H 0 {1,S}
4   O 0 {1,S}
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
    label = "CsJ-SsHH",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Ss 0 {1,S}
3   H  0 {1,S}
4   H  0 {1,S}
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
    label = "C_sec_rad",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
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
    label = "C_rad/H/NonDeC",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   Cs 0 {1,S}
4   Cs 0 {1,S}
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
    label = "C_rad/H/NonDeO",
    group = 
"""
1 * C      1 {2,S} {3,S} {4,S}
2   H      0 {1,S}
3   O      0 {1,S}
4   {Cs,O} 0 {1,S}
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
    label = "C_rad/H/CsO",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   Cs 0 {1,S}
4   O  0 {1,S}
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
    label = "C_rad/H/O2",
    group = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   H 0 {1,S}
3   O 0 {1,S}
4   O 0 {1,S}
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
    label = "C_rad/H/OneDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   H             0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   {Cs,O}        0 {1,S}
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
    label = "C_rad/H/OneDeC",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   H             0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   Cs            0 {1,S}
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
    label = "C_rad/H/CdCs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   Cd 0 {1,S}
4   Cs 0 {1,S}
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
    label = "C_rad/H/CtCs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   Ct 0 {1,S}
4   Cs 0 {1,S}
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
    label = "C_rad/H/OneDeO",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   H             0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   O             0 {1,S}
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
    label = "C_rad/H/TwoDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   H             0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C_rad/H/CdCd",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   H  0 {1,S}
3   Cd 0 {1,S}
4   Cd 0 {1,S}
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
    label = "CsJ-CSH",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   C  0 {1,S}
3   Ss 0 {1,S}
4   H  0 {1,S}
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
    label = "CsJ-CsSsH",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cs 0 {1,S}
3   Ss 0 {1,S}
4   H  0 {1,S}
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
    label = "CsJ-CtSsH",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Ct 0 {1,S}
3   Ss 0 {1,S}
4   H  0 {1,S}
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
    label = "CsJ-CbSsH",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cb 0 {1,S}
3   Ss 0 {1,S}
4   H  0 {1,S}
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
    label = "CsJ-CdSsH",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cd 0 {1,S} {5,D}
3   Ss 0 {1,S}
4   H  0 {1,S}
5   C  0 {2,D}
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
    label = "CsJ-C=SSsH",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cd 0 {1,S} {5,D}
3   Ss 0 {1,S}
4   H  0 {1,S}
5   Sd 0 {2,D}
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
    label = "CsJ-SsSsH",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Ss 0 {1,S}
3   Ss 0 {1,S}
4   H  0 {1,S}
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
    label = "C_ter_rad",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
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
    label = "C_rad/NonDeC",
    group = 
"""
1 * C      1 {2,S} {3,S} {4,S}
2   {Cs,O} 0 {1,S}
3   {Cs,O} 0 {1,S}
4   {Cs,O} 0 {1,S}
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
    label = "C_rad/Cs3",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cs 0 {1,S}
3   Cs 0 {1,S}
4   Cs 0 {1,S}
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
    label = "C_rad/NDMustO",
    group = 
"""
1 * C      1 {2,S} {3,S} {4,S}
2   O      0 {1,S}
3   {Cs,O} 0 {1,S}
4   {Cs,O} 0 {1,S}
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
    label = "C_rad/OneDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cs,O}        0 {1,S}
4   {Cs,O}        0 {1,S}
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
    label = "C_rad/Cs2",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   Cs            0 {1,S}
4   Cs            0 {1,S}
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
    label = "C_rad/ODMustO",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   O             0 {1,S}
4   {Cs,O}        0 {1,S}
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
    label = "C_rad/TwoDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   {Cs,O}        0 {1,S}
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
    label = "C_rad/Cs",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   Cs            0 {1,S}
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
    label = "C_rad/TDMustO",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   O             0 {1,S}
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
    label = "C_rad/ThreeDe",
    group = 
"""
1 * C             1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} 0 {1,S}
3   {Cd,Ct,Cb,CO} 0 {1,S}
4   {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "CsJ-CSS",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   C  0 {1,S}
3   Ss 0 {1,S}
4   Ss 0 {1,S}
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
    label = "CsJ-CsSsSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cs 0 {1,S}
3   Ss 0 {1,S}
4   Ss 0 {1,S}
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
    label = "CsJ-CtSsSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Ct 0 {1,S}
3   Ss 0 {1,S}
4   Ss 0 {1,S}
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
    label = "CsJ-CbSsSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cb 0 {1,S}
3   Ss 0 {1,S}
4   Ss 0 {1,S}
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
    label = "CsJ-CdSsSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cd 0 {1,S} {5,D}
3   Ss 0 {1,S}
4   Ss 0 {1,S}
5   C  0 {2,D}
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
    label = "CsJ-C=SSsSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cd 0 {1,S} {5,D}
3   Ss 0 {1,S}
4   Ss 0 {1,S}
5   Sd 0 {2,D}
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
    label = "CsJ-CCS",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   C  0 {1,S}
3   C  0 {1,S}
4   Ss 0 {1,S}
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
    label = "CsJ-CsCsSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cs 0 {1,S}
3   Cs 0 {1,S}
4   Ss 0 {1,S}
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
    label = "CsJ-CsCtSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cs 0 {1,S}
3   Ct 0 {1,S}
4   Ss 0 {1,S}
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
    label = "CsJ-CsCbSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cs 0 {1,S}
3   Cb 0 {1,S}
4   Ss 0 {1,S}
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
    label = "CsJ-CsCdSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cs 0 {1,S}
3   Cd 0 {1,S} {5,D}
4   Ss 0 {1,S}
5   C  0 {3,D}
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
    label = "CsJ-CsC=SSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Cs 0 {1,S}
3   Cd 0 {1,S} {5,D}
4   Ss 0 {1,S}
5   Sd 0 {3,D}
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
    label = "CsJ-SsSsSs",
    group = 
"""
1 * C  1 {2,S} {3,S} {4,S}
2   Ss 0 {1,S}
3   Ss 0 {1,S}
4   Ss 0 {1,S}
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
    label = "Ct_rad",
    group = 
"""
1 * Ct  1 {2,T}
2   R!H 0 {1,T}
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
    index = 101,
    label = "Ct_rad/Nt",
    group = 
"""
1 * Ct        1 {2,T}
2   {N3t,N5t} 0 {1,T}
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
    index = 102,
    label = "C_rad/H2/N",
    group = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   H 0 {1,S}
3   H 0 {1,S}
4   N 0 {1,S}
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
    index = 103,
    label = "C_rad/H/NonDeN",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   Cs  0 {1,S}
4   N3s 0 {1,S}
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
    index = 104,
    label = "N3_rad",
    group = 
"""
1 * {N3s,N3d} 1
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
    index = 105,
    label = "N3s_rad",
    group = 
"""
1 * N3s 1
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
    index = 106,
    label = "NH2_rad",
    group = 
"""
1 * N3s 1 {2,S} {3,S}
2   H   0 {1,S}
3   H   0 {1,S}
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
    index = 107,
    label = "N3s_rad_pri",
    group = 
"""
1 * N3s 1 {2,S} {3,S}
2   H   0 {1,S}
3   R!H 0 {1,S}
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
    index = 108,
    label = "N3s_rad_sec",
    group = 
"""
1 * N3s 1 {2,S} {3,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
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
    index = 109,
    label = "N3d_rad",
    group = 
"""
1 * N3d 1 {2,D}
2   R!H 0 {1,D}
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
    index = 110,
    label = "N5_rad",
    group = 
"""
1 * {N5s,N5d,N5t} 1
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
    index = 111,
    label = "N5d_rad",
    group = 
"""
1 * N5d 1
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

tree(
"""
L1: Y_rad
        L2: H_rad
        L2: S_rad
            L3: SJ
                L4: SsJ-H
                L4: SsJ-C
                    L5: SsJ-Cs
                    L5: SsJ-Ct
                    L5: SsJ-Cb
                    L5: SsJ-Cd
                    L5: SsJ-C=S
                L4: SsJ-Ss
                L4: SsJ-Os
        L2: Ct_rad
            L3: Ct_rad/Ct
            L3: Ct_rad/Nt
        L2: O_rad
            L3: O_pri_rad
            L3: O_sec_rad
                L4: O_rad/NonDe
                L4: O_rad/OneDe
        L2: O2_birad
        L2: Cd_rad
            L3: Cd_pri_rad
            L3: Cd_sec_rad
                L4: Cd_rad/NonDe
                L4: Cd_rad/OneDe
                    L5: Cd_rad/Cd
        L2: Cb_rad
        L2: CO_rad
            L3: CO_pri_rad
            L3: CO_sec_rad
                L4: CO_rad/NonDe
                L4: CO_rad/OneDe
        L2: C=SJ
            L3: C=SJ-H
            L3: C=SJ-C
                L4: C=SJ-Cs
            L3: C=SJ-Ss
        L2: Cs_rad
            L3: C_methyl
            L3: C_pri_rad
                L4: C_rad/H2/Cs
                L4: C_rad/H2/Cd
                L4: C_rad/H2/Ct
                L4: C_rad/H2/Cb
                L4: C_rad/H2/CO
                L4: C_rad/H2/O
                L4: C_rad/H2/N
                L4: CsJ-SsHH
            L3: C_sec_rad
                L4: C_rad/H/NonDeN
                L4: C_rad/H/NonDeC
                L4: C_rad/H/NonDeO
                    L5: C_rad/H/CsO
                    L5: C_rad/H/O2
                L4: C_rad/H/OneDe
                    L5: C_rad/H/OneDeC
                        L6: C_rad/H/CdCs
                        L6: C_rad/H/CtCs
                    L5: C_rad/H/OneDeO
                L4: C_rad/H/TwoDe
                    L5: C_rad/H/CdCd
                L4: CsJ-CSH
                    L5: CsJ-CsSsH
                    L5: CsJ-CtSsH
                    L5: CsJ-CbSsH
                    L5: CsJ-CdSsH
                    L5: CsJ-C=SSsH
                L4: CsJ-SsSsH
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
                L4: CsJ-CSS
                    L5: CsJ-CsSsSs
                    L5: CsJ-CtSsSs
                    L5: CsJ-CbSsSs
                    L5: CsJ-CdSsSs
                    L5: CsJ-C=SSsSs
                L4: CsJ-CCS
                    L5: CsJ-CsCsSs
                    L5: CsJ-CsCtSs
                    L5: CsJ-CsCbSs
                    L5: CsJ-CsCdSs
                    L5: CsJ-CsC=SSs
                L4: CsJ-SsSsSs
        L2: N3_rad
            L3: N3s_rad
                L4: NH2_rad
                L4: N3s_rad_pri
                L4: N3s_rad_sec
            L3: N3d_rad 
        L2: N5_rad 
"""
)

forbidden(
    label = "O4",
    group = 
"""
1    O 1 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 O 0 {2,S} {4,S}
4    O 1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)




