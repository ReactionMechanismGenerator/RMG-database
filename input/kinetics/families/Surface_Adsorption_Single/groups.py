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

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1']
])

entry(
    index = 1,
    label = "Adsorbate",
    group = 
"""
1 *1 R u1
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



forbidden(
    label = "disigma1",
    group = 
"""
1 *1 R u1 {2,[S,D]}
2    R u0 {1,[S,D]} {3,[S,D]}
3    X u0 {2,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
The adsorbing atom should not be adjacent to a molecule that is already adsorbed.
e.g. this is not allowed:

H2C-O   <-->  H2C*-O
  | |              |
  X X           X  X
""",
)

forbidden(
    label = "adjacentradical1",
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
