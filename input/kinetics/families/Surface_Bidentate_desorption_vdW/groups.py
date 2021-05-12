#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_desorption_vdW/groups"
shortDesc = u""
longDesc = u"""
Physisorption of a gas-phase species onto the surface.

     *1                      *1  
   :  |     <-->   ~*2~   +   |
 ~*2~ X                       X

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbed"], products=["VacantSite","Adsorbate"], ownReverse=False)

reversible = False

reactantNum=1
productNum=2

recipe(actions=[
    ['BREAK_BOND', '*1', 0, '*2']
])

entry(
    index = 1,
    label = "Adsorbed",
    group =
"""
1 *1 R u0 px c0 {2,[S,D,T,Q]}
2    Xo u0 px c0 {1,[S,D,T,Q]}
3 *2 Xv u0 p0 c0
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbed
"""
)