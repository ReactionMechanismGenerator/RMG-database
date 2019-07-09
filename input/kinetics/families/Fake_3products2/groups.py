#!/usr/bin/env python
# encoding: utf-8

name = "Fake_3products2/groups"
shortDesc = u""
longDesc = u"""
Some reaction in which a radical of a hydroperoxide falls apart into 3 products.
It's very much like Fake_3products1, only you start with a radical and create
a double bond. It shows up in the LLNL Gasoline Surrogate model.
"""

template(reactants=["HOORRRj"], products=["P1", "P2", "P3"], ownReverse=False)

reverse = "Fake_trimolecular2"

recipe(actions=[
    ['GAIN_RADICAL', '*2', '1'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*3', '1', '*4'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['CHANGE_BOND', '*5', '1', '*6'],
    ['LOSE_RADICAL', '*6', '1'],
])

entry(
    index = 1,
    label = "HOORRRj",
    group = """
1 *1 H  0 {2,S}
2 *2 O  0 {1,S} {3,S}
3 *3 O  0 {2,S} {4,S}
4 *4 R  0 {3,S} {5,S}
5 *5 R  0 {4,S} {6,S}
6 *6 R  1 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

tree(
"""
L1: HOORRRj
"""
)
