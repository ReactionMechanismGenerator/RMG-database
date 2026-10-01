#!/usr/bin/env python
# encoding: utf-8

name = "Ketoenol_Aromatic/groups"
shortDesc = u""
longDesc = u"""
Aromatic (dearomatizing) keto-enol tautomerization: an aromatic enol (phenol-type
Ar-OH) converts to its non-aromatic cyclohexadienone keto tautomer by a 1,3-H shift
from the phenolic oxygen to the ortho ring carbon, e.g.

    phenol <=> cyclohexa-2,4-dien-1-one

This chemistry cannot be hosted by the existing Ketoenol family: that family's
template requires a localized C=C double bond ({x,D}) and its group tree contains no
Cb/Cbf nodes, so it never matches the aromatic representation of a phenol. The
Kekule resonance structure of an aromatic molecule, which would match, is marked
reactive=False by RMG's resonance filtration and is therefore never reacted
(verified empirically on the polymer branch, 2026-07-22: end-to-end react() on a
phenol Species returns zero Ketoenol reactions). This family instead matches the
aromatic form directly (Cb atoms, benzene B bonds); the recipe's CHANGE_BOND on the
ring B bond flags validAromatic=False and apply_recipe kekulizes the product, the
same machinery used by Diels_alder_addition_Aromatic.

Why this family exists (phenolic-polymer phase 6): the ortho-hydroxyl acceleration
of diarylmethane (novolac methylene-bridge) scission does NOT proceed through a
weakened aromatic Ar-CH2 bond -- Benjamin et al. (Fuel 57 (1978) 269,
DOI 10.1016/0016-2361(78)90003-0) and McMillen, Ogier & Ross (J. Org. Chem. 46
(1981) 3322, DOI 10.1021/jo00329a034) showed the aromatic bond is not weakened and
the acceleration runs through an enol->keto tautomerization pre-equilibrium
followed by fast homolysis of the weak benzylic C-C bond of the cyclohexadienone
keto tautomer. This family supplies that tautomerization step as an elementary,
citable reaction; the subsequent keto benzylic C-C homolysis is R_Recombination
(reverse) chemistry.

Atom labeling:
*1 - ortho ring carbon (Cb) that receives the H (becomes the sp3 ring carbon of
     the dienone; in a novolac bridge this is the carbon carrying the CH2 bridge)
*2 - ipso ring carbon (Cb) bearing the phenolic O (becomes the carbonyl carbon)
*3 - phenolic oxygen
*4 - phenolic hydrogen (migrates to *1)

Scope note: this template is the ortho (1,3-shift, 2,4-cyclohexadienone) channel,
for which a citable CBS-QB3 rate exists (Zhu & Bozzelli 2003, DOI 10.1021/jp0212545).
The para channel (1,5-shift to the 2,5-cyclohexadienone) is deliberately not
included until a citable rate for it is in hand.

Implementation note: *1/*2 are written as [Cb,Cbf] sets rather than plain Cb
because GroupAtom action resolution requires a non-empty product atomtype list
(Cb.decrement_bond is empty while Cbf.decrement_bond = [Cb]); this is the same
device Diels_alder_addition_Aromatic uses. A Cbf atom cannot actually occupy *2
(its three benzene bonds leave no room for the {2,S} bond to the phenolic O), so
the match set is effectively Cb, as chemistry requires.
"""

template(reactants=["Root"], products=["cyclohexadienone"], ownReverse=False)

reverse = "Cyclohexadienone_To_Aromatic_Enol"
reversible = True

reactantNum = 1

productNum = 1

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*4', 1, '*1'],
    ['CHANGE_BOND', '*2', 1, '*3'],
])

entry(
    index = 0,
    label = "Root",
    group =
"""
1 *2 [Cb,Cbf] u0 {2,S} {3,[D,B]}
2 *3 O2s      u0 {1,S} {4,S}
3 *1 [Cb,Cbf] u0 {1,[D,B]}
4 *4 H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "ortho_H",
    group =
"""
1 *2 [Cb,Cbf] u0 {2,S} {3,[D,B]}
2 *3 O2s      u0 {1,S} {4,S}
3 *1 [Cb,Cbf] u0 {1,[D,B]} {5,S}
4 *4 H        u0 {2,S}
5    H        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "ortho_C",
    group =
"""
1 *2 [Cb,Cbf] u0 {2,S} {3,[D,B]}
2 *3 O2s      u0 {1,S} {4,S}
3 *1 [Cb,Cbf] u0 {1,[D,B]} {5,S}
4 *4 H        u0 {2,S}
5    C        ux {3,S}
""",
    kinetics = None,
)

tree(
"""
L1: Root
    L2: ortho_H
    L2: ortho_C
"""
)
