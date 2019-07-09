#!/usr/bin/env python
# encoding: utf-8

name = "Fake_O_Abstraction/groups"
shortDesc = u""
longDesc = u"""
Some reaction in which an oxygen atom is abstracted by a radical. Shows up in
the LLNL butanol model.
"""

template(reactants=["X_O", "Y_rad"], products=["X_rad", "Y_O"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "X_O",
    group = """
1 *1 R u0 {2,S}
2 *2 O ux {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

entry(
    index = 2,
    label = "Y_rad",
    group = """
1 *3 R u1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

tree(
"""
L1: X_O
L1: Y_rad
"""
)
