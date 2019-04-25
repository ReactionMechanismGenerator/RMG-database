#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. Atom *1 is bonded to the surface (*3). The image below shows a single bond, but single, double, and triple are possible. What matters is that the bond between *1 and *2 must be single.
    # NOTE: we should probably include vdW, too!

 *1--*2                 *1     *2
  |            ---->    ||      |
~*3~ + ~*4~~           ~*3~ + ~*4~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association"

recipe(actions=[
    ['FORM_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['BREAK_BOND', '*1', 1, '*2']
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 {2,S} {3,[S,D,T]}
2 *2 R   u0 {1,S}
3 *3 Xo  u0 {1,[S,D,T]}
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
