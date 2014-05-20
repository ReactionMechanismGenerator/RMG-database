#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Disproportionation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["Y"], ownReverse=False)

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
    label = "Rn",
    group = "OR{R3, R4, R5, R6, R7}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Y_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "XH_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U1 {2,S}
2 *2 R!H U0 {1,S} {3,S}
3 *4 H   U0 {2,S}
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
    group = "OR{R3radEndo, R3radExo}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R3radEndo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2 *3 R!H U1 {1,{S,D,B,T}} {3,S}
3 *2 R!H U0 {2,S} {4,S}
4 *4 H   U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "R3radExo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2    R!H U0 {1,{S,D,B,T}} {3,{S,D,B}}
3 *2 R!H U0 {2,{S,D,B}} {4,S} {5,S}
4 *3 R!H U1 {3,S}
5 *4 H   U0 {3,S}
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
    group = "OR{R4radEndo, R4radExo}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "R4radEndo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2    R!H U0 {1,{S,D,B,T}} {3,{S,D,B,T}}
3 *3 R!H U1 {2,{S,D,B,T}} {4,S}
4 *2 R!H U0 {3,S} {5,S}
5 *4 H   U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "R4radExo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2    R!H U0 {1,{S,D,B,T}} {3,{S,D,B,T}}
3    R!H U0 {2,{S,D,B,T}} {4,{S,D,B}}
4 *2 R!H U0 {3,{S,D,B}} {5,S} {6,S}
5 *3 R!H U1 {4,S}
6 *4 H   U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "R5",
    group = "OR{R5radEndo, R5radExo}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "R5radEndo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2    R!H U0 {1,{S,D,B,T}} {3,{S,D,B,T}}
3    R!H U0 {2,{S,D,B,T}} {4,{S,D,B,T}}
4 *3 R!H U1 {3,{S,D,B,T}} {5,S}
5 *2 R!H U0 {4,S} {6,S}
6 *4 H   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "R5radExo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2    R!H U0 {1,{S,D,B,T}} {3,{S,D,B,T}}
3    R!H U0 {2,{S,D,B,T}} {4,{S,D,B,T}}
4    R!H U0 {3,{S,D,B,T}} {5,{S,D,B}}
5 *2 R!H U0 {4,{S,D,B}} {6,S} {7,S}
6 *3 R!H U1 {5,S}
7 *4 H   U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "R6",
    group = "OR{R6radEndo, R6radExo}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "R6radEndo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2    R!H U0 {1,{S,D,B,T}} {3,{S,D,B,T}}
3    R!H U0 {2,{S,D,B,T}} {4,{S,D,B,T}}
4    R!H U0 {3,{S,D,B,T}} {5,{S,D,B,T}}
5 *3 R!H U1 {4,{S,D,B,T}} {6,S}
6 *2 R!H U0 {5,S} {7,S}
7 *4 H   U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "R6radExo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2    R!H U0 {1,{S,D,B,T}} {3,{S,D,B,T}}
3    R!H U0 {2,{S,D,B,T}} {4,{S,D,B,T}}
4    R!H U0 {3,{S,D,B,T}} {5,{S,D,B,T}}
5    R!H U0 {4,{S,D,B,T}} {6,{S,D,B}}
6 *2 R!H U0 {5,{S,D,B}} {7,S} {8,S}
7 *3 R!H U1 {6,S}
8 *4 H   U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "R7",
    group = "OR{R7radEndo, R7radExo}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "R7radEndo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2    R!H U0 {1,{S,D,B,T}} {3,{S,D,B,T}}
3    R!H U0 {2,{S,D,B,T}} {4,{S,D,B,T}}
4    R!H U0 {3,{S,D,B,T}} {5,{S,D,B,T}}
5    R!H U0 {4,{S,D,B,T}} {6,{S,D,B,T}}
6 *3 R!H U1 {5,{S,D,B,T}} {7,S}
7 *2 R!H U0 {6,S} {8,S}
8 *4 H   U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "R7radExo",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,{S,D,B,T}}
2    R!H U0 {1,{S,D,B,T}} {3,{S,D,B,T}}
3    R!H U0 {2,{S,D,B,T}} {4,{S,D,B,T}}
4    R!H U0 {3,{S,D,B,T}} {5,{S,D,B,T}}
5    R!H U0 {4,{S,D,B,T}} {6,{S,D,B,T}}
6    R!H U0 {5,{S,D,B,T}} {7,{S,D,B}}
7 *2 R!H U0 {6,{S,D,B}} {8,S} {9,S}
8 *3 R!H U1 {7,S}
9 *4 H   U0 {7,S}
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
        L3: R3radEndo
        L3: R3radExo
    L2: R4
        L3: R4radEndo
        L3: R4radExo
    L2: R5
        L3: R5radEndo
        L3: R5radExo
    L2: R6
        L3: R6radEndo
        L3: R6radExo
    L2: R7
        L3: R7radEndo
        L3: R7radExo
L1: Y_rad
L1: XH_Rrad
"""
)

forbidden(
    label = "fused5rings_1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 C U1 {2,S} {5,S}
2 C U0 {1,S} {3,S}
3 C U0 {2,S} {4,S}
4 C U0 {3,S} {5,S} {8,S}
5 C U0 {1,S} {4,S} {6,S}
6 C U1 {5,S} {7,S}
7 C U0 {6,S} {8,S}
8 C U0 {4,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "fused5rings_2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 C U1 {2,S} {5,S}
2 C U0 {1,S} {3,S}
3 C U0 {2,S} {4,S}
4 C U0 {3,S} {5,S} {8,S}
5 C U0 {1,S} {4,S} {6,S}
6 C U0 {5,S} {7,S}
7 C U1 {6,S} {8,S}
8 C U0 {4,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "fused5rings_3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 C U1 {2,S} {5,S}
2 C U0 {1,S} {3,S}
3 C U0 {2,S} {4,S}
4 C U0 {3,S} {5,S} {8,S}
5 C U0 {1,S} {4,S} {6,S}
6 C U0 {5,S} {7,S}
7 C U0 {6,S} {8,S}
8 C U1 {4,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "fused5rings_4",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 C U0 {2,S} {5,S}
2 C U1 {1,S} {3,S}
3 C U0 {2,S} {4,S}
4 C U0 {3,S} {5,S} {8,S}
5 C U0 {1,S} {4,S} {6,S}
6 C U0 {5,S} {7,S}
7 C U1 {6,S} {8,S}
8 C U0 {4,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

