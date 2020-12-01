#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/groups"
shortDesc = u""
longDesc = u"""
Physisorption of a gas-phase species onto the surface.

 *1         *1
     ---->   :
~*2~       ~*2~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate", "VacantSite"], products=["Adsorbed"], ownReverse=False)

reverse = "Surface_Desorption_vdW"

reactantNum=2
productNum=1

recipe(actions=[
    ['FORM_BOND', '*1', 0, '*2']
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
multiplicity [1]
1 *1 R u0 px c0
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *2 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "H2O",
    group =
"""
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "CO2",
    group =
"""
1 *1 C u0 p0 c0 {2,D} {3,D}
2    O u0 p2 c0 {1,D}
3    O u0 p2 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CH4",
    group =
"""
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate
    L2: H2O
    L2: CO2
    L2: CH4

L1: VacantSite
"""
)

forbidden(
    label = "charge",
    group =
"""
1 R ux c[+1,-1]
""",
    shortDesc = u"""Charges not allowed""",
    longDesc =
u"""
""",
)
