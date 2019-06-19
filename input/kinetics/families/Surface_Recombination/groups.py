#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Recombination/groups"
shortDesc = u""
longDesc = u"""
Recombination of two surface-bound species, to form one, singly bound.
i.e. the opposite of bond fission.

 *1   *3             *1--*3   
 ||    |      ---->   |       
~*2~~~*4~~          ~*2~~*4~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Adsorbate1", "Adsorbate2"], products=["Combined", "VacantSite"], ownReverse=False)

reverse = "Surface_Bond_Fission"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4']
])

entry(
    index = 1,
    label = "Adsorbate1",
    group = 
"""
1 *1 R!H ux {2,[D,T]}
2 *2 Xo  u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Adsorbate2",
    group = 
"""
1 *3 R  ux {2,S}
2 *4 Xo u0 {1,S}
""",
    kinetics = None,
)


tree(
"""
L1: Adsorbate1

L1: Adsorbate2
"""
)

