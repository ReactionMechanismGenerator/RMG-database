#!/usr/bin/env python
# encoding: utf-8

name = "Concerted_Intra_Diels_alder_monocyclic_1,2_shiftH/groups"
shortDesc = u"Intramolecular ring-closure by concerted addition of two alkene end groups in  a 1_3_hexadien_5_yne backbone " \
            u"(C=C-C=C-C#C) with simultaneous 1,2-H shift over an unsaturated bond to form an unsaturated singlet carbene " \
            u"cyclohexane product"
longDesc = u"""
From 2003 Miller and Klippenstein Propargyl recombination PES:

Miller, J. A.; Klippenstein, S. J., The Recombination of Propargyl Radicals and Other Reactions on a C6H6 Potential.
J. Phys. Chem. A 2003, 107, 7783-7799.
"""

template(reactants=["1_3_hexadien_5_yne"], products=["unsaturated_singlet_carbene_cyclohexane"], ownReverse=False)

reverse = "Concerted_Retro_Intra_Diels_alder_monocyclic_singlet_carbene_disproportionation"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '-1', '*4'],
    ['CHANGE_BOND', '*2', '1', '*3'],
    ['CHANGE_BOND', '*5', '-1', '*6'],
    ['CHANGE_BOND', '*4', '1', '*5'],
    ['FORM_BOND', '*1', 'S', '*6'],
    ['CHANGE_BOND', '*5', '-1', '*6'],
    ['BREAK_BOND', '*6', 'S', '*7'],
    ['FORM_BOND', '*5', 'S', '*7'],
    ['GAIN_PAIR', '*6', '1'],
])

entry(
    index = 1,
    label = "1_3_hexadien_5_yne",
    group = 'OR{linear_1_3_hexadien_5_yne}',
    kinetics = None,
)

entry(
    index = 2,
    label = "linear_1_3_hexadien_5_yne",
    group =
"""
1  *3 Cd u0 {2,S} {3,D} {8,S}
2  *2 Cd u0 {1,S} {4,D} {7,S}
3  *4 Cd u0 {1,D} {5,S} {9,S}
4  *1 Cd u0 {2,D} {11,S} {12,S}
5  *5 Ct u0 {3,S} {6,T}
6  *6 Ct u0 p0 {5,T} {10,S}
7 R u0 {2,S}
8 R u0 {1,S}
9 R u0 {3,S}
10  *7 H u0 {6,S}
11 R u0 {4,S}
12 R u0 {4,S}
""",
    kinetics = None,
)

tree(
"""
L1: 1_3_hexadien_5_yne
    L2: linear_1_3_hexadien_5_yne
"""
)

