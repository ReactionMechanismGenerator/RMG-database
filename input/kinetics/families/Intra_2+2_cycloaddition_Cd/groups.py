#!/usr/bin/env python
# encoding: utf-8

name = "Intra_2+2_cycloaddition_Cd/groups"
shortDesc = u"2+2 cycloaddition between alkene subunits on a 1,3-butadiene backbone to form cyclobutene subunit"
longDesc = u"""

"""

template(reactants=["1,3-butadiene_backbone"], products=["unsaturated_four_ring"], ownReverse=False)

reverse = "Four_Ring_Open"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '-1', '*4'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['CHANGE_BOND', '*2', '1', '*4'],
])

entry(
    index = 1,
    label = "1,3-butadiene_backbone",
    group =
"""
1  *1 C u0 {2,D}
2  *2 Cd u0 {1,D} {3,S}
3  *4 Cd u0 {2,S} {4,D}
4  *3 C u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "C=C_1",
    group=
"""
1  *1 C u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "CdH2_1",
    group =
"""
1  *1 Cd u0 {2,S} {3,S}
2  H u0 {1,S}
3  H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "CdH(C)_1",
    group =
"""
1  *1 Cd u0 {2,S} {3,S}
2  H u0 {1,S}
3  C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Cd(C)C_1",
    group =
"""
1  *1 Cd u0 {2,S} {3,S}
2  C u0 {1,S}
3  C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "CddC_1",
    group =
"""
1  *1 Cdd u0 {2,D}
2  C u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "C=C_2",
    group=
"""
1  *3 C u0
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CdH2_2",
    group =
"""
1  *3 Cd u0 {2,S} {3,S}
2  H u0 {1,S}
3  H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CdH(C)_2",
    group =
"""
1  *3 Cd u0 {2,S} {3,S}
2  H u0 {1,S}
3  C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Cd(C)C_2",
    group =
"""
1  *3 Cd u0 {2,S} {3,S}
2  C u0 {1,S}
3  C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "CddC_2",
    group =
"""
1  *3 Cdd u0 {2,D}
2  C u0 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: 1,3-butadiene_backbone
L1: C=C_1
    L2: CdH2_1
    L2: CdH(C)_1
    L2: Cd(C)C_1
    L2: CddC_1
L1: C=C_2
    L2: CdH2_2
    L2: CdH(C)_2
    L2: Cd(C)C_2
    L2: CddC_2
"""
)

forbidden(
    label = "resonant_radical_1",
    group =
"""
1  *1 C u0 {2,D}
2  *2 Cd u0 {1,D} {3,S} {5,S}
3  *4 Cd u0 {2,S} {4,D}
4  *3 C u0 {3,D}
5     R!H u1 {2,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid this family from reacting a resonant radical, to prevent redundancy with Intra_R_Add_Endo or Exocyclic
""",
)

forbidden(
    label = "resonant_radical_2",
    group =
"""
1  *1 C u0 {2,D}
2  *2 Cd u0 {1,D} {3,S}
3  *4 Cd u0 {2,S} {4,D} {5,S}
4  *3 C u0 {3,D}
5     R!H u1 {3,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid this family from reacting a resonant radical, to prevent redundancy with Intra_R_Add_Endo or Exocyclic
""",
)

forbidden(
    label = "resonant_radical_3",
    group =
"""
1  *1 C u0 {2,D}
2  *2 Cd u0 {1,D} {3,S} {5,S}
3  *4 Cd u0 {2,S} {4,D}
4  *3 C u0 {3,D}
5     R!H ux {2,S} {6,D}
6     R!H ux {5,D} {7,S}
7     R!H u1 {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid this family from reacting a resonant radical, to prevent redundancy with Intra_R_Add_Endo or Exocyclic
""",
)

forbidden(
    label = "resonant_radical_4",
    group =
"""
1  *1 C u0 {2,D}
2  *2 Cd u0 {1,D} {3,S}
3  *4 Cd u0 {2,S} {4,D} {5,S}
4  *3 C u0 {3,D}
5     R!H ux {3,S} {6,D}
6     R!H ux {5,D} {7,S}
7     R!H u1 {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid this family from reacting a resonant radical, to prevent redundancy with Intra_R_Add_Endo or Exocyclic
""",
)

forbidden(
    label = "resonant_radical_5",
    group =
"""
1  *1 C u0 {2,D} {5,S}
2  *2 Cd u0 {1,D} {3,S}
3  *4 Cd u0 {2,S} {4,D}
4  *3 C u0 {3,D}
5     R!H u1 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid this family from reacting a resonant radical, to prevent redundancy with Intra_R_Add_Endo or Exocyclic
""",
)

forbidden(
    label = "resonant_radical_6",
    group =
"""
1  *1 C u0 {2,D}
2  *2 Cd u0 {1,D} {3,S}
3  *4 Cd u0 {2,S} {4,D}
4  *3 C u0 {3,D} {5,S}
5     R!H u1 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid this family from reacting a resonant radical, to prevent redundancy with Intra_R_Add_Endo or Exocyclic
""",
)