#!/usr/bin/env python
# encoding: utf-8

name = "API_Fake_HOCK_rearrangement"
shortDesc = u""
longDesc = u"""
he Hock fragmentation (or rearrangement) is a well-known reaction for benzylic, allylic and dienylic hydroperoxides. 
This family describes reactions of the sort:
CC-OOH + [H+] <=>  CC-O[OH2+] <=RDS=> C-O-[C+] + H2O <=> C-O-C-[OH2+] <=> C-[OH+]-C-OH <=> C-OH + C=O
overall taken as:
CC-OOH <=> C-OH + C=O

atom labels:
C(*1)C(*2)-O(*3)O(*4)H <=> C(*1)-O(*4)H + C(*2)=O(*3)
"""

template(reactants=["CC-OOH"], products=["COH", "C=O"], ownReverse=False)

reverse = "reverse_HOCK"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*4'],
    ['CHANGE_BOND', '*2', 1, '*3'],
])

entry(
    index = 0,
    label = "CC-OOH",
    group =
"""
1     R!H u0 p0 c0 {2,D}
2  *1 C   u0 p0 c0 {1,D} {3,S}
3  *2 C   u0 p0 c0 {2,S} {4,S}
4  *3 O   u0 p2 c0 {3,S} {5,S}
5  *4 O   u0 p2 c0 {4,S} {6,S}
6     H   u0 p0 c0 {5,S}
""",
    kinetics = None,
)

tree(
"""
L1: CC-OOH
"""
)
