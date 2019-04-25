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



tree(
"""
L1: Adsorbate

L1: VacantSite
"""
)
