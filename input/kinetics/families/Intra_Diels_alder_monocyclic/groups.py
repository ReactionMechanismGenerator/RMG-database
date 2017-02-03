#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Diels_alder_monocyclic/groups"
shortDesc = u"Intramolecular ring-closure by concerted addition of two alkene end groups in a 6-membered conjugated " \
            u"backbone (C=C-C=C-C=C) to an unsaturated  cyclohexane product"
longDesc = u"""

"""

template(reactants=["1_3_5_unsaturated_hexane"], products=["unsaturated_cyclohexane"], ownReverse=False)

reverse = "Intra_Retro_Diels_alder_monocyclic"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '-1', '*4'],
    ['CHANGE_BOND', '*2', '1', '*3'],
    ['CHANGE_BOND', '*5', '-1', '*6'],
    ['CHANGE_BOND', '*4', '1', '*5'],
    ['FORM_BOND', '*1', 'S', '*6'],
])

entry(
    index = 1,
    label = "1_3_5_unsaturated_hexane",
    group="OR{linear_1_3_5_hexatriene, fulvene, linear_1_3_hexadien_5_yne}",
    kinetics = None,
)

entry(
    index = 3,
    label = "linear_1_3_5_hexatriene",
    group =
"""
1  *3 Cd u0 {2,S} {3,D} {10,S}
2  *2 Cd u0 {1,S} {4,D} {9,S}
3  *4 Cd u0 {1,D} {5,S} {11,S}
4  *1 C u0 {2,D}
5  *5 Cd u0 {3,S} {6,D} {12,S}
6  *6 C u0 {5,D}
9 R u0 {2,S}
10 R u0 {1,S}
11 R u0 {3,S}
12 R u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "fulvene",
    group =
"""
1  *3 Cd u0 {2,S} {3,D}
2  *2 Cd u0 {1,S} {4,D} {6,S}
3  *4 Cd u0 {1,D} {5,S}
4  *1 C u0 {2,D}
5  *5 Cd u0 {3,S} {6,D}
6  *6 Cd u0 {5,D} {2,S}
""",
    kinetics = None,
)

entry(
    index = 6,
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
10 R u0 {6,S}
11 R u0 {4,S}
12 R u0 {4,S}
""",
    kinetics = None,
)

tree(
"""
L1: 1_3_5_unsaturated_hexane
    L2: linear_1_3_5_hexatriene
    L2: fulvene
    L2: linear_1_3_hexadien_5_yne
"""
)

