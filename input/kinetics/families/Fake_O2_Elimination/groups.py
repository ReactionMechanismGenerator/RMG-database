#!/usr/bin/env python
# encoding: utf-8

name = "Fake_O2_Elimination/groups"
shortDesc = u""
longDesc = u"""
Some reaction in which an oxygen atom is abstracted by a radical. Shows up in
the LLNL butanol model.
"""

template(reactants=["X_OO", "Y_OO"], products=["P1", "P2", "P3"], ownReverse=False)

reverse = "Fake_bimolecular_O2_addition"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*3'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['GAIN_RADICAL', '*2', '1'],
    ['GAIN_RADICAL', '*4', '1'],
])

entry(
    index = 1,
    label = "X_OO",
    group = """
1 *1 O u1 {2,S}
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
    label = "Y_OO",
    group = """
1 *3 O u1 {2,S}
2 *4 O ux {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
)

tree(
"""
L1: X_OO
L1: Y_OO
"""
)
