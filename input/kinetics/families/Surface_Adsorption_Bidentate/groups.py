#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Bidentate/groups"
shortDesc = u""
longDesc = u"""
Bidentate adsorption of a gas-phase species onto the surface. 
The multiple-bond in the gas-phase species is decrease; 
the atoms at either end are each singled bonded to the surface.

 *1=*2                *1-*2
             ---->    |   |
~*3~ + ~*4~         ~*3~ *4~~

Note that it does not form a bond between *3 and *4.

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2) * (mol/m3)
so k should be in (m5/mol2/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate", "VacantSite1", "VacantSite2"], products=["Adsorbed"], ownReverse=False)

reverse = "Surface_Desorption_Bidentate"

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4']
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
1 *1 R!H u0 {2,[D,T]}
2 *2 R!H u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite1",
    group =
"""
1 *3 Xv u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label="VacantSite2",
    group =
"""
1 *4 Xv u0
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate

L1: VacantSite1

L1: VacantSite2
"""
)


forbidden(
    label = "chargedSurface1",
    group =
"""
1 *1 R!H u0 c-1 {2,T}
2 *2 R!H u0 c+1 {1,T}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing molecule should not have a charge on the surface. 
I've written it specifically for the case of CO adsorption for now.

e.g. this is not allowed:

-C#O+    -->  -C=O+
               | |
 X X           X X
""",
)

forbidden(
    label = "chargedSurface2",
    group =
"""
1 *1 R!H u0 c+1 {2,T}
2 *2 R!H u0 c-1 {1,T}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing molecule should not have a charge on the surface. 
I've written it specifically for the case of CO adsorption for now.
e.g. this is not allowed:

-C#O+    -->  -C=O+
               | |
 X X           X X
""",
)
