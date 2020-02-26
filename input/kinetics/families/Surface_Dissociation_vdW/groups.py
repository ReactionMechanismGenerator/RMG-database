#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one vdW species into two distinct adsorbates. Atom *3 is vdW, but we leave that out of the graph.

 *1--*2                 *1     *2
  :            ---->     |      |
~*3~ + ~*4~~           ~*3~ + ~*4~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['BREAK_BOND', '*1', 1, '*2'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
multiplicity [1,3]
1 *1 R!H ux px cx {2,S}
2 *2 R   ux px cx {1,S}
3 *3 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *4 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R-H",
    group =
"""
multiplicity [1,3]
1 *1 R!H ux px cx {2,S}
2 *2 H   u0 p0 c0 {1,S}
3 *3 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C-H",
    group =
"""
multiplicity [1,3]
1 *1 C  ux px cx {2,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O-H",
    group =
"""
multiplicity [1,3]
1 *1 O  ux px cx {2,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "N-H",
    group =
"""
multiplicity [1,3]
1 *1 N  ux px cx {2,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 Xv u0 p0 c0
""",
    kinetics = None,
)

tree(
"""
L1: Combined
    L2: R-H
        L3: C-H
        L3: O-H
        L3: N-H
L1: VacantSite
"""
)
