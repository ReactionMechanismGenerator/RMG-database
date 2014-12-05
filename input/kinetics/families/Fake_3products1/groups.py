#!/usr/bin/env python
# encoding: utf-8

name = "Fake_3products1/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["HORRROO"], products=["P1", "P2", "P3"], ownReverse=False)

reverse = "trimolecular"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*6'],
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['CHANGE_BOND', '*2', '1', '*3'],
    ['BREAK_BOND', '*3', 'S', '*4'],
    ['CHANGE_BOND', '*5', '1', '*6'],
    ['BREAK_BOND', '*6', 'S', '*7'],
])


#entry(
#    index = 1,
#    label = "jOOQOOH",
#    group = "OR{jOOQ2OOH, jOOQ3OOH, jOOQ4OOH, jOOQ5OOH, jOOQ6OOH, jOOQ7OOH}",
#    kinetics = None,
#    reference = None,
#    referenceType = "",
#    shortDesc = u"""""",
#    longDesc = u"""""",
#    history = [
#        ("Thu Oct 10 2013","Victor Lambert <vrlambert@gmail.com","action","""Created to use only for importing other groups chemkin files"""),
#    ],
#)

entry(
    index = 1,
    label = "HORRROO",
    group = """
1 *1 H  0 {2,S}
2 *2 O  0 {1,S} {3,S}
3 *3 R  0 {2,S} {4,S}
4 *4 R  0 {3,S} {5,S}
5 *5 R  0 {4,S} {6,S}
6 *6 O  0 {5,S} {7,S}
7 *7 O  1 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
    history = [
        ("Thu Dec 4 2014","Richard West","action","""Created to use only for importing other groups chemkin files"""),
    ],
)


tree(
"""
L1: HORRROO
"""
)