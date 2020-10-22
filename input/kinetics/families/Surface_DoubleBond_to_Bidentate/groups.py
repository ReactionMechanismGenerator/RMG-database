#!/usr/bin/env python
# encoding: utf-8

name = "Surface_DoubleBond_to_Bidentate"
shortDesc = u""
longDesc = u"""
If an adsorbate has an internal double bond, then it can fall over onto a vacant site, creating a bidentate.

 *1=*2                    *1--*2  
  |              ---->    ||   |     
~*3~ + ~*4~~             ~*3~~*4~~ 

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate"], ownReverse=False)

reverse = "Surface_Bidentate_to_DoubleBond"

recipe(actions=[
    ['FORM_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*1', 1, '*3'],
]) 

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 [C,N]   u0 {2,[D,T]} {3,[S,D]}
2 *2 R!H     u0 {1,[D,T]} 
3 *3 Xo      u0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *4 Xv u0
""",
    kinetics = None,
)


tree(
"""
L1: Combined

L1: VacantSite
"""
)


forbidden(
    label = "bidentate1",
    group =
"""
1 *1 R u0 {2,[D,T]} {3,[S,D]} 
2 *2 R u0 {1,[D,T]} {4,[S,D]}
3 *3 X u0 {1,[S,D]}
4    X u0 {2,[S,D]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The reactant should not be bidentate to begin with.
""",
)

forbidden(
    label = "bidentate2",
    group =
"""
1 *1 R u0 {2,[D,T]} {4,[S,D]}
2 *2 R u0 {1,[D,T]} {3,[S,D]}
3 *3 X u0 {2,[S,D]}
4    X u0 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The reactant should not be bidentate to begin with.
""",
)
