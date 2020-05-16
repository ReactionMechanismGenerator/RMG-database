#!/usr/bin/env python
# encoding: utf-8

name = "hemiaminal_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of hemiaminal groups:
C(OH)N(R1)R2 + H2O <=> C=O + HN(R1)R2 + H2O
ignoring H2O on both sides for simplicity
(training reactions do include H2O in the calculation, rates divided by 18 ml/mol)

atom labels:

C[*1]_(O[*2]_H[*3])_N[*4]_(R1)_R2 <=> C[*1]_=O[*2] + H[*3]_N[*4]_(R1)_R2
"""

template(reactants=["hemiaminal"], products=["CdO", "NH2"], ownReverse=False)

reverse = "condensation_to_amino_alcohol"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*3', 1, '*4'],
])

entry(
    index=0,
    label="hemiaminal",
    group=
"""
1 *2 O u0 p2 c0 {2,S} {4,S}
2 *1 C u0 p0 c0 {1,S} {3,S}
3 *4 N3s u0 p1 c0 {2,S}
4 *3 H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: hemiaminal
"""
)
