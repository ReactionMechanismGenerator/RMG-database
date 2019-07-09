#!/usr/bin/env python
# encoding: utf-8

name = "Fake_Ketohydroperoxides/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["jOOQOOH"], products=["HOOQ=O", "jOH"], ownReverse=False)

reverse = "Keto-breaker"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['BREAK_BOND', '*3', 1, '*2'],
    ['CHANGE_BOND', '*3', +1, '*4'],
    ['GAIN_RADICAL', '*5', '1'],
    ['LOSE_RADICAL', '*1', '1']
])


entry(
    index = 1,
    label = "jOOQOOH",
    group = "OR{jOOQ2OOH, jOOQ3OOH, jOOQ4OOH, jOOQ5OOH, jOOQ6OOH, jOOQ7OOH}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

entry(
    index = 1,
    label = "jOOQ2OOH",
    group = """
1 *1 O                  1 {2,S}
2    O                  0 {1,S} {3,S}
3    {Cs,Cd}            0 {2,S} {4,S}
4 *3 {Cs,Cd}            0 {3,S} {5,S} {7,S}
5 *4 O                  0 {4,S} {6,S}
6 *5 O                  0 {5,S}
7 *2 H                  0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

entry(
    index = 2,
    label = "jOOQ3OOH",
    group = """
1 *1 O                  1 {2,S}
2    O                  0 {1,S} {3,S}
3    {Cs,Cd,Ct}         0 {2,S} {4,S}
4    {Cs,Cd,Ct}         0 {3,S} {5,S}
5 *3 {Cs,Cd}            0 {4,S} {6,S} {8,S}
6 *4 O                  0 {5,S} {7,S}
7 *5 O                  0 {6,S}
8 *2 H                  0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

entry(
    index = 3,
    label = "jOOQ4OOH",
    group = """
1 *1 O                  1 {2,S}
2    O                  0 {1,S} {3,S}
3    {Cs,Cd,Ct}         0 {2,S} {4,S}
4    {Cs,Cd,Ct}         0 {3,S} {5,S}
5    {Cs,Cd,Ct}         0 {4,S} {6,S}
6 *3 {Cs,Cd}            0 {5,S} {7,S} {9,S}
7 *4 O                  0 {6,S} {8,S}
8 *5 O                  0 {7,S}
9 *2 H                  0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

entry(
    index = 4,
    label = "jOOQ5OOH",
    group = """
1 *1 O                  1 {2,S}
2    O                  0 {1,S} {3,S}
3    {Cs,Cd,Ct}         0 {2,S} {4,S}
4    {Cs,Cd,Ct}         0 {3,S} {5,S}
5    {Cs,Cd,Ct}         0 {4,S} {6,S}
6    {Cs,Cd,Ct}         0 {5,S} {7,S}
7 *3 {Cs,Cd}            0 {6,S} {8,S} {10,S}
8 *4 O                  0 {7,S} {9,S}
9 *5 O                  0 {8,S}
10 *2 H                 0 {7,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

entry(
    index = 5,
    label = "jOOQ6OOH",
    group = """
1 *1 O                  1 {2,S}
2    O                  0 {1,S} {3,S}
3    {Cs,Cd,Ct}         0 {2,S} {4,S}
4    {Cs,Cd,Ct}         0 {3,S} {5,S}
5    {Cs,Cd,Ct}         0 {4,S} {6,S}
6    {Cs,Cd,Ct}         0 {5,S} {7,S}
7    {Cs,Cd,Ct}         0 {6,S} {8,S}
8 *3 {Cs,Cd}            0 {7,S} {9,S} {11,S}
9 *4 O                  0 {8,S} {10,S}
10 *5 O                 0 {9,S}
11 *2 H                 0 {8,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

entry(
    index = 6,
    label = "jOOQ7OOH",
    group = """
1 *1 O                  1 {2,S}
2    O                  0 {1,S} {3,S}
3    {Cs,Cd,Ct}         0 {2,S} {4,S}
4    {Cs,Cd,Ct}         0 {3,S} {5,S}
5    {Cs,Cd,Ct}         0 {4,S} {6,S}
6    {Cs,Cd,Ct}         0 {5,S} {7,S}
7    {Cs,Cd,Ct}         0 {6,S} {8,S}
8    {Cs,Cd,Ct}         0 {7,S} {9,S}
9 *3 {Cs,Cd}            0 {8,S} {10,S} {12,S}
10 *4 O                 0 {9,S} {11,S}
11 *5 O                 0 {10,S}
12 *2 H                 0 {9,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

tree(
"""
L1: jOOQOOH
"""
)
