#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Double/groups"
shortDesc = u""
longDesc = u"""
Adsorption of a gas-phase triplet onto the surface. The unpaired electrons in the reactant form a double bond with the metal.

 *1         *1
     ---->  ||
~*2~       ~*2~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate", "VacantSite"], products=["Adsorbed"], ownReverse=False)

reverse = "Surface_Desorption_Double"

reactantNum=2
productNum=1

recipe(actions=[
    ['LOSE_RADICAL', '*1', 2],
    ['FORM_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*1', 1, '*2']
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
1 *1 R!H u2
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
    label = "C",
    group =
"""
1 *1 C u2
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "CH2",
    group =
"""
multiplicity [3]
1 *1 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CO",
    group =
"""
multiplicity [3]
1    O u0 p2 c0 {2,D}
2 *1 C u2 p0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "C2O",
    group =
"""
multiplicity [3]
1    O u0 p2 c0 {2,D}
2    C u0 p0 c0 {1,D} {3,D}
3 *1 C u2 p0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "N",
    group =
"""
1 *1 N u2
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "NH",
    group =
"""
multiplicity [3]
1 *1 N u2 p1 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "NN",
    group =
"""
multiplicity [3]
1    N u0 {2,S}
2 *1 N u2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "N2H2",
    group =
"""
multiplicity [3]
1    N u0 p1 c0 {2,S} {3,S} {4,S}
2 *1 N u2 p1 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "O",
    group =
"""
1 *1 O u2
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate
    L2: C
        L3: CH2
        L3: CO
        L3: C2O
    L2: N
        L3: NH
        L3: NN
            L4: N2H2
    L2: O


L1: VacantSite
"""
)