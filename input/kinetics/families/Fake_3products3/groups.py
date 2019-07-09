#!/usr/bin/env python
# encoding: utf-8

name = "Fake_3products3/groups"
shortDesc = u""
longDesc = u"""
Some reaction in which an ROOj radical abstracts an H from
an OH group on itself and falls apart into three products.
It shows up in the LLNL Gasoline Surrogate model.
"""

template(reactants=["OjORROH"], products=["P1", "P2", "P3"], ownReverse=False)

reverse = "Fake_trimolecular3"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*6'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*2', +1, '*3'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*4', +1, '*5'],
    ['BREAK_BOND', '*5', 1, '*6'],
])

entry(
    index = 1,
    label = "OjORROH",
    group =
"""
1 *1 O 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *3 R 0 {2,S} {4,S}
4 *4 R 0 {3,S} {5,S}
5 *5 O 0 {4,S} {6,S}
6 *6 H 0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

tree(
"""
L1: OjORROH
"""
)
