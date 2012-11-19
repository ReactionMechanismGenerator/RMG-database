#!/usr/bin/env python
# encoding: utf-8

name = "Enol_keto_tautomerism/groups"
shortDesc = ""
longDesc = """

"""
recommended = True

template(reactants=["enol"], products=["keto"], ownReverse=False)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*4'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['CHANGE_BOND', '*2', '-1', '*3'],
    ['CHANGE_BOND', '*3', '1', '*4'],
])

entry(
    index = 1,
    label = "enol",
    group = 
"""
1 *2 {Cd,Cdd} {0,1,2} {2,D}
2 *3 Cd       {0,1}   {1,D} {3,S}
3 *4 Os       0       {2,S} {4,S}
4 *1 H        0       {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov  1 13:04:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "ene",
    group = 
"""
1 *2 {Cd,Cdd} {0,1,2} {2,D}
2 *3 Cd       {0,1}   {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov  1 13:04:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "enol_rad",
    group = 
"""
1 *2 {Cd,Cdd} {0,1,2} {2,D}
2 *3 Cd       1       {1,D} {3,S}
3 *4 Os       0       {2,S} {4,S}
4 *1 H        0       {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov  1 13:04:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "enol_R",
    group = 
"""
1 *2 {Cd,Cdd} {0,1,2} {2,D}
2 *3 Cd       0       {1,D} {3,S}
3 *4 Os       0       {2,S} {4,S}
4 *1 H        0       {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov  1 13:04:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "ene_birad",
    group = 
"""
1 *2 {Cd,Cdd} 2       {2,D}
2 *3 Cd       {0,1}   {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov  1 13:04:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "ene_rad",
    group = 
"""
1 *2 {Cd,Cdd} 1       {2,D}
2 *3 Cd       {0,1}   {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov  1 13:04:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "ene_SS",
    group = 
"""
1 *2 Cd       0       {2,D}
2 *3 Cd       {0,1}   {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov  1 13:04:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "ene_D",
    group = 
"""
1 *2 Cdd      0       {2,D}
2 *3 Cd       {0,1}   {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov  1 13:04:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

tree(
"""
L1: enol
    L2: enol_rad
    L2: enol_R
L1: ene
    L2: ene_birad
    L2: ene_rad
    L2: ene_SS
    L2: ene_D
"""
)

