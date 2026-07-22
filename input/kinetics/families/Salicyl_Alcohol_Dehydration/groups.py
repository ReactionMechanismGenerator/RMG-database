#!/usr/bin/env python
# encoding: utf-8

name = "Salicyl_Alcohol_Dehydration/groups"
shortDesc = u""
longDesc = u"""
Closed-shell dehydration of a salicyl-alcohol-type (2-hydroxybenzyl alcohol)
motif to an ortho-quinone methide (o-QM) plus water:

    2-HO-C6H4-CH2OH -> o-QM (6-methylene-2,4-cyclohexadien-1-one) + H2O

The phenolic H and the benzylic OH depart as water; the phenol C-O becomes the
quinone carbonyl and the benzylic carbon becomes the exocyclic methylene; the
ring dearomatizes. This is the o-QM inlet channel of resole-type phenolic
chemistry (methylol-bearing repeat units and incompletely-cured novolac
defects). It cannot be hosted by Retroene: Retroene's H-accepting atom *1 must
carry a reducible pi bond ({x,[D,T,B]} plus a CHANGE_BOND -1), and water's
oxygen is saturated (template proof recorded in the phase-6 status document).

Aromatic-template machinery: same devices as Ketoenol_Aromatic --
the two ring atoms are [Cb,Cbf] sets and the changed ring bond is [D,B]
so that group-level recipe application resolves atom types and does not
trip the purely-aromatic-template guard in apply_recipe; at the molecule
level the recipe runs on the aromatic (reactive) representation and the
product is kekulized to the quinoid o-QM.

Atom labeling:
*1 - ortho ring carbon bearing the CH2OH (becomes the methide carbon's ring
     attachment, C=CH2 exocyclic)
*2 - ipso ring carbon bearing the phenolic O (becomes the carbonyl carbon)
*3 - phenolic oxygen
*4 - phenolic hydrogen (migrates to *6, forming water)
*5 - benzylic (methylol) carbon
*6 - benzylic hydroxyl oxygen (departs in water)

Benchmark scope note (honest): the TACOT novolac benchmark is methyl-capped
with no -CH2OH groups, so this family adds generalizable phenolic-resin value
(resole chemistry, hexamine-cure defects) but no flux on that benchmark. It
supplies the missing inlet for o-QM decomposition chemistry (see the
carbon_phenol library's o-QM -> benzene + CO entry, da Silva & Bozzelli 2007,
DOI 10.1021/jp073335c).
"""

template(reactants=["Root"], products=["oQM", "H2O"], ownReverse=False)

reverse = "oQM_Water_Addition"
reversible = True

reactantNum = 1

productNum = 2

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*5', 1, '*6'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*4', 1, '*6'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*5'],
])

entry(
    index = 0,
    label = "Root",
    group =
"""
1 *2 [Cb,Cbf] u0 {2,S} {3,[D,B]}
2 *3 O2s      u0 {1,S} {4,S}
3 *1 [Cb,Cbf] u0 {1,[D,B]} {5,S}
4 *4 H        u0 {2,S}
5 *5 C        u0 {3,S} {6,S}
6 *6 O2s      u0 {5,S} {7,S}
7    H        u0 {6,S}
""",
    kinetics = None,
)

tree(
"""
L1: Root
"""
)
