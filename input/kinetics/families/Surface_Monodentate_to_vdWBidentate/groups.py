#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Monodentate_to_vdWBidentate"
shortDesc = u""
longDesc = u"""
If a monodentate adsorbate bound through oxygen with a single bond has
double bond to another oxygen in the beta position, the adsorbate can fall
over into a resonant vdW bidentate configuration.

 *1-*2=*3                 *1-*2=*3  
  |              ---->     |     :     
~*4~ + ~*5~~             ~*4~~~~*5~~ 

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Monodentate", "VacantSite"], products=["Bidentate"], ownReverse=False)

reverse = "Surface_vdWBidentate_to_Monodentate"

recipe(actions=[
['FORM_BOND', '*3', 1, '*5'],
['CHANGE_BOND', '*3', -1, '*5'],
]) 

entry(
    index = 1,
    label = "Monodentate",
    group =
"""
1 *1 O  u0 p2 {2,S} {4,S}
2 *2 R!H u0 p0 {1,S} {3,D}
3 *3 O  u0 p2 {2,D} 
4 *4 Xo u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *5 Xv u0
""",
    kinetics = None,
)


tree(
"""
L1: Monodentate

L1: VacantSite
"""
)

