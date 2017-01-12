#!/usr/bin/env python
# encoding: utf-8

name = "Cyclopentadiene_scission/groups"
shortDesc = u"Scission of one of the adjacent single bonds in a CPD subunit to form a conjugated singlet carbene"
longDesc = u"""
Currently, family will only scission a fused CPD + cyclopropane bicyclic subunit using calculated kinetics from 2003
Miller and Klippenstein Propargyl recombination PES. Data needed before other entries can be added (e.g., simple CPD
scission)
"""

template(reactants=["CPD_backbone"], products=["conjugated_singlet_carbene"], ownReverse=False)

reverse = "Intra_singlet_carbene_addition"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['CHANGE_BOND', '*4', -1, '*5'],
    ['CHANGE_BOND', '*1', 1, '*5'],
    ['CHANGE_BOND', '*4', 1, '*3'],
    ['GAIN_PAIR', '*2', '1']
])
entry(
    index = 1,
    label = "CPD_backbone",
    group ='OR{fused_CPD_cyclopropane_bicyclic}',
    kinetics = None,
)

entry(
    index = 2,
    label = "fused_CPD_cyclopropane_bicyclic",
    group =
"""
1 *1 C u0 {2,S} {5,S} {6,S}
2 *2 Cd u0 {1,S} {3,D} {6,S}
3 *3 Cd u0 {2,D} {4,S}
4 *4 Cd u0 {3,S} {5,D}
5 *5 Cd u0 {1,S} {4,D}
6 C u0 {1,S} {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: CPD_backbone
    L2: fused_CPD_cyclopropane_bicyclic
"""
)

