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

forbidden(
    label = "delocalized_radical_chain_1",
    group =
"""
1  *3 Cd u0 {2,S} {3,D}
2  *2 Cd u0 {1,S} {4,D}
3  *4 Cd u0 {1,D} {5,S}
4  *1 C u0 {2,D}  {7,S}
5  *5 Cd u0 {3,S} {6,D}
6  *6 C u0 {5,D}
7     R!H u1 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent this family from reacting resonantly stabilized radicals, to prevent redundancy with Intra_R_Add_Endo
and Exocyclic
""",
)

forbidden(
    label = "delocalized_radical_chain_2",
    group =
"""
1  *3 Cd u0 {2,S} {3,D}
2  *2 Cd u0 {1,S} {4,D}
3  *4 Cd u0 {1,D} {5,S}
4  *1 C u0 {2,D}
5  *5 Cd u0 {3,S} {6,D}
6  *6 C u0 {5,D} {7,S}
7     R!H u1 {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent this family from reacting resonantly stabilized radicals, to prevent redundancy with Intra_R_Add_Endo
and Exocyclic
""",
)

forbidden(
    label = "delocalized_radical_chain_3",
    group =
"""
1  *3 Cd u0 {2,S} {3,D}
2  *2 Cd u0 {1,S} {4,D}
3  *4 Cd u0 {1,D} {5,S}
4  *1 C u0 {2,D}  {7,S}
5  *5 Cd u0 {3,S} {6,D}
6  *6 C u0 {5,D}
7     R!H u0 {4,S} {8,D}
8     R!H u0 {9,S} {7,D}
9     R!H u1 {8,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent this family from reacting resonantly stabilized radicals, to prevent redundancy with Intra_R_Add_Endo
and Exocyclic
""",
)

forbidden(
    label = "delocalized_radical_chain_4",
    group =
"""
1  *3 Cd u0 {2,S} {3,D}
2  *2 Cd u0 {1,S} {4,D}
3  *4 Cd u0 {1,D} {5,S}
4  *1 C u0 {2,D}
5  *5 Cd u0 {3,S} {6,D}
6  *6 C u0 {5,D} {7,S}
7     R!H u0 {6,S} {8,D}
8     R!H u0 {9,S} {7,D}
9     R!H u1 {8,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent this family from reacting resonantly stabilized radicals, to prevent redundancy with Intra_R_Add_Endo
and Exocyclic
""",
)

forbidden(
    label = "styrene_like_molecule_direction_1",
    group =
"""
1  *1 C u0 {2,[D,T]}
2  *2 C u0 {1,[D,T]} {3,S}
3  *3 C u0 {2,S} {4,[D,T]} {8,[S,D,T,B]}
4  *4 C u0 {3,[D,T]} {5,S}
5  *5 C u0 {4,S} {6,[D,T]}
6  *6 C u0 {5,[D,T]} {7,[S,D,T,B]}
7  C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  C u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a molecule from undergoing this reaction if 4 of the necessary carbon atoms are on a ring,
and the other two are on a side chain (like styrene). Atom labels written starting from chaing end.
""",
)

forbidden(
    label = "styrene_like_molecule_direction_2",
    group =
"""
1  *6 C u0 {2,[D,T]}
2  *5 C u0 {1,[D,T]} {3,S}
3  *4 C u0 {2,S} {4,[D,T]} {8,[S,D,T,B]}
4  *3 C u0 {3,[D,T]} {5,S}
5  *2 C u0 {4,S} {6,[D,T]}
6  *1 C u0 {5,[D,T]} {7,[S,D,T,B]}
7  C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  C u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a molecule from undergoing this reaction if 4 of the necessary carbon atoms are on a ring,
and the other two are on a side chain (like styrene). Atom labels written starting from ring end.
""",
)