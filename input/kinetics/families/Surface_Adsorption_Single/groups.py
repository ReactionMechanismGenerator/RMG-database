#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Single/groups"
shortDesc = u""
longDesc = u"""
Adsorption of a gas-phase radical onto the surface. The unpaired electron in the reactant forms a single bond with the metal.

 *1         *1
     ---->   |
~*2~       ~*2~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate", "VacantSite"], products=["Adsorbed"], ownReverse=False)

reverse = "Surface_Desorption_Single"

reactantNum=2
productNum=1

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*1', 1]
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
multiplicity [2]
1 *1 [H,C,N,O,S,F,Cl,Br] u1
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *2 Xv u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "H",
    group =
"""
multiplicity [2]
1 *1 H u1 p0 c0
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C",
    group =
"""
multiplicity [2]
1 *1 C u1
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "C-H",
    group =
"""
multiplicity [2]
1 *1 C u1 p1 cx {2,S}
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "CH=O",
    group =
"""
multiplicity [2]
1    O u0 p2 cx {2,D}
2 *1 C u1 p0 cx {1,D} {3,S}
3    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "CH2-H",
    group =
"""
multiplicity [2]
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "N",
    group =
"""
multiplicity [2]
1 *1 N u1
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "N=O",
    group =
"""
multiplicity [2]
1 *1 N u1 p1 c0 {2,D}
2    O u0 p2 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "O",
    group =
"""
multiplicity [2]
1 *1 O u1
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "O-H",
    group =
"""
multiplicity [2]
1 *1 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "O-C",
    group =
"""
multiplicity [2]
1 *1 O u1 p2 cx {2,S}
2    C u0 p0 cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "O-CH3",
    group =
"""
multiplicity [2]
1 *1 O u1 p2 c0 {2,S}
2    C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3    H u0 p0 c0 {2,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "O-N",
    group =
"""
multiplicity [2]
1 *1 O u1 p2 cx {2,S}
2    N u0 p1 cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "O-N=O",
    group =
"""
multiplicity [2]
1 *1 O u1 p2 cx {3,S}
2    O u0 p2 cx {3,D}
3    N u0 p1 cx {1,S} {2,D}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate
    L2: H
    L2: C
        L3: C-H
        L3: CH=O
        L3: CH2-H
    L2: N
        L3: N=O
    L2: O
        L3: O-H
        L3: O-C
            L4: O-CH3
        L3: O-N
            L4: O-N=O

L1: VacantSite
"""
)


forbidden(
    label = "adjacentradical",
    group =
"""
1 *1 R u1 {2,S}
2    R u1 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing atom should not be adjacent to a radical.
e.g. this is not allowed:

.O-O.    -->   .O-O
                  |
   X              X
""",
)

forbidden(
    label = "chargedSpecies",
    group =
"""
1 *1 R u1 c[+1,-1]
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing atom should not have a charge
""",
)
