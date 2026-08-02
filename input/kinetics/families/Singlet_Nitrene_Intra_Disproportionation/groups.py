#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_Nitrene_Intra_Disproportionation/groups"
shortDesc = "Convert a singlet nitrene to a closed-shell molecule through a concerted 1,2-H shift + 1,2-bond formation"
longDesc = """
Reaction site *1 should always be a singlet in this family.

This is the nitrogen analogue of Singlet_Carbene_Intra_Disproportionation. The recipe is
identical; only the reacting centre differs, a singlet nitrene (N u0 p2) in place of a
singlet carbene (C u0 p1). It is a separate family rather than an extension of the carbene
one because RMG group syntax cannot correlate the element with its lone-pair count within a
single atom specification: writing the centre as [C,N] u0 p[1,2] also admits an ordinary
amine nitrogen (N u0 p1), which LOSE_PAIR then drives to p0 and raises an AtomTypeError.
"""

template(reactants=["Root"], products=["NH_N_unsaturated"], ownReverse=False)

reversible = True

reactantNum = 1
productNum = 1

recipe(actions=[
    ['LOSE_PAIR', '*1', '1'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*2'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 *2 R!H u0 p[0,1,2] {2,S} {3,[S,D]}
2 *3 H   u0 p0       {1,S}
3 *1 N   u0 p2 c0    {1,[S,D]}
""",
    kinetics = None,
)

tree(
"""
L1: Root
"""
)
