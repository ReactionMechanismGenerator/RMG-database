#!/usr/bin/env python
# encoding: utf-8

name = "Intra_5_membered_conjugated_C=C_C=C_addition/groups"
shortDesc = u"Concerted intramolecular addition of two alkene groups in a 5-membered conjugated backbone (C=C=C-C=C) to" \
            u"form a 5-membered conjugated cyclic singlet carbene"
longDesc = u"""
From 2003 Miller and Klippenstein Propargyl recombination PES:

Miller, J. A.; Klippenstein, S. J., The Recombination of Propargyl Radicals and Other Reactions on a C6H6 Potential.
J. Phys. Chem. A 2003, 107, 7783-7799.
"""

template(reactants=["C=C=C-C=C"], products=["C1-CJ2(S)-C=C-C-C1"], ownReverse=False)

reverse = "5_membered_cyclic_conjugated_singlet_carbene_scission"

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*5'],
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*4', -1, '*5'],
    ['GAIN_PAIR', '*5', '1'],

])

entry(
    index = 1,
    label = "C=C=C-C=C",
    group=
"""
1  *4 Cd u0 {2,S} {4,D}
2  *3 Cd u0 {1,S} {5,D}
3  *1 C u0 {4,D}
4  *5 Cdd u0 {1,D} {3,D}
5  *2 C u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "C=C=C_End",
    group =
"""
1  *1 C u0
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

entry(
    index = 3,
    label = "C=C=CdH2",
    group =
"""
1  *1 Cd u0 {2,S} {3,S}
2 H u0 {1,S}
3 H u0 {1,S}
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

entry(
    index = 4,
    label = "C=C=CdHC",
    group =
"""
1  *1 Cd u0 {2,S} {3,S}
2 H u0 {1,S}
3 C u0 {1,S}
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

entry(
    index = 5,
    label = "C=C=Cd(C)C",
    group =
"""
1  *1 Cd u0 {2,S} {3,S}
2 C u0 {1,S}
3 C u0 {1,S}
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

entry(
    index = 6,
    label = "C=C=CddC",
    group =
"""
1  *1 Cdd u0 {2,D}
2 C u0 {1,D}
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

entry(
    index = 7,
    label = "C-C=C_End",
    group =
"""
1  *2 C u0
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

entry(
    index = 8,
    label = "C-C=CdH2",
    group =
"""
1  *2 Cd u0 {2,S} {3,S}
2 H u0 {1,S}
3 H u0 {1,S}
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

entry(
    index = 9,
    label = "C-C=CdHC",
    group =
"""
1  *2 Cd u0 {2,S} {3,S}
2 H u0 {1,S}
3 C u0 {1,S}
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

entry(
    index = 10,
    label = "C-C=Cd(C)C",
    group =
"""
1  *2 Cd u0 {2,S} {3,S}
2 C u0 {1,S}
3 C u0 {1,S}
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

entry(
    index = 11,
    label = "C-C=CddC",
    group =
"""
1  *2 Cdd u0 {2,D}
2 C u0 {1,D}
""",
    kinetics = None,
    shortDesc = "",
    longDesc =
u"""

""",
)

tree(
"""
L1: C=C=C-C=C
L1: C=C=C_End
    L2: C=C=CdH2
    L2: C=C=CdHC
    L2: C=C=Cd(C)C
    L2: C=C=CddC
L1: C-C=C_End
    L2: C-C=CdH2
    L2: C-C=CdHC
    L2: C-C=Cd(C)C
    L2: C-C=CddC
"""
)