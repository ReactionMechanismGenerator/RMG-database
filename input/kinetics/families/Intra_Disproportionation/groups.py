#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Disproportionation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_birad"], products=["Y"], ownReverse=False)

reverse = "BiradFromMultipleBond"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*4'],
    ['BREAK_BOND', '*2', 'S', '*4'],
    ['CHANGE_BOND', '*2', '1', '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "Y_birad",
    group = "OR{Y_biCyc3, Y_biCyc4, Y_biCyc5, Y_biCyc6, Y_biCyc7}",
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
    label = "Y_rad",
    group = 
"""
1 *1 R!H 1
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
    label = "XH_Rrad",
    group = 
"""
1 *2 R!H 0 {2,{S,D}} {3,S}
2 *3 R!H 1 {1,{S,D}}
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
    index = 4,
    label = "Y_biCyc3",
    group = 
"""
1 *1 R!H 1 {2,{S,D,B}}
2 *2 R!H 0 {1,{S,D,B}} {3,{S,D}} {4,S}
3 *3 R!H 1 {2,{S,D}}
4 *4 H   0 {2,S}
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
    label = "Y_biCyc4",
    group = 
"""
1 *1 R!H 1 {5,{S,D,B,T}}
2 *2 R!H 0 {3,{S,D}} {4,S} {5,{S,D,B}}
3 *3 R!H 1 {2,{S,D}}
4 *4 H   0 {2,S}
5    R!H 0 {1,{S,D,B,T}} {2,{S,D,B}}
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
    label = "Y_biCyc5",
    group = "OR{Y_biCyc5radEndo, Y_biCyc5radExo}",
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
    label = "Y_biCyc6",
    group = "OR{Y_biCyc6radEndo, Y_biCyc6radExo}",
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
    label = "Y_biCyc7",
    group = "OR{Y_biCyc7radEndo, Y_biCyc7radExo}",
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
    index = -1,
    label = "Y_biCyc5radEndo",
    group = 
"""
1 *1 R!H 1 {5,{S,D,B,T}}
2 *2 R!H 0 {3,{S,D}} {4,S}
3 *3 R!H 1 {2,{S,D}} {5,{S,D,B}}
4 *4 H   0 {2,S}
5    R!H 0 {1,{S,D,B,T}} {3,{S,D,B}}
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
    index = -1,
    label = "Y_biCyc5radExo",
    group = 
"""
1 *1 R!H 1 {5,{S,D,B,T}}
2 *2 R!H 0 {3,{S,D}} {4,S} {6,{S,D,B}}
3 *3 R!H 1 {2,{S,D}}
4 *4 H   0 {2,S}
5    R!H 0 {1,{S,D,B,T}} {6,{S,D,B,T}}
6    R!H 0 {2,{S,D,B}} {5,{S,D,B,T}}
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
    index = -1,
    label = "Y_biCyc6radEndo",
    group = 
"""
1 *1 R!H 1 {6,{S,D,B,T}}
2 *2 R!H 0 {3,{S,D}} {4,S}
3 *3 R!H 1 {2,{S,D}} {5,{S,D,B}}
4 *4 H   0 {2,S}
5    R!H 0 {3,{S,D,B}} {6,{S,D,B,T}}
6    R!H 0 {1,{S,D,B,T}} {5,{S,D,B,T}}
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
    index = -1,
    label = "Y_biCyc6radExo",
    group = 
"""
1 *1 R!H 1 {5,{S,D,B,T}}
2 *2 R!H 0 {3,{S,D}} {4,S} {6,{S,D,B}}
3 *3 R!H 1 {2,{S,D}}
4 *4 H   0 {2,S}
5    R!H 0 {1,{S,D,B,T}} {7,{S,D,B,T}}
6    R!H 0 {2,{S,D,B}} {7,{S,D,B,T}}
7    R!H 0 {5,{S,D,B,T}} {6,{S,D,B,T}}
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
    index = -1,
    label = "Y_biCyc7radEndo",
    group = 
"""
1 *1 R!H 1 {6,{S,D,B,T}}
2 *2 R!H 0 {3,{S,D}} {4,S}
3 *3 R!H 1 {2,{S,D}} {5,{S,D,B}}
4 *4 H   0 {2,S}
5    R!H 0 {3,{S,D,B}} {7,{S,D,B,T}}
6    R!H 0 {1,{S,D,B,T}} {7,{S,D,B,T}}
7    R!H 0 {5,{S,D,B,T}} {6,{S,D,B,T}}
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
    index = -1,
    label = "Y_biCyc7radExo",
    group = 
"""
1 *1 R!H 1 {5,{S,D,B,T}}
2 *2 R!H 0 {3,{S,D}} {4,S} {6,{S,D,B}}
3 *3 R!H 1 {2,{S,D}}
4 *4 H   0 {2,S}
5    R!H 0 {1,{S,D,B,T}} {7,{S,D,B,T}}
6    R!H 0 {2,{S,D,B}} {8,{S,D,B,T}}
7    R!H 0 {5,{S,D,B,T}} {8,{S,D,B,T}}
8    R!H 0 {6,{S,D,B,T}} {7,{S,D,B,T}}
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

tree(
"""
L1: Y_birad
    L2: Y_biCyc3
    L2: Y_biCyc4
    L2: Y_biCyc5
    L2: Y_biCyc6
    L2: Y_biCyc7
L1: Y_rad
L1: XH_Rrad
"""
)

