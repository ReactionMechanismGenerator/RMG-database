#!/usr/bin/env python
# encoding: utf-8

name = "concerted_intra_H_alphaQOOH_break/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H5O4 <=> C2H4O3 + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.47e+12,'s^-1'), n=-0.24, Ea=(28,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOCCO[O] <=> O=CCOO + [OH]
""",
)

entry(
    index = 2,
    label = "C3H7O4 <=> C3H6O3 + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.22e+07,'s^-1'), n=1.6, Ea=(27.9,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOCC(C)O[O] <=> O=CC(C)OO + [OH]
""",
)

entry(
    index = 3,
    label = "C3H7O4-2 <=> C3H6O3-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.76e+08,'s^-1'), n=1.2, Ea=(25.7,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOC(C)CO[O] <=> O=C(C)COO + [OH]
""",
)

entry(
    index = 4,
    label = "C4H9O4 <=> C4H8O3 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.75e+08,'s^-1'), n=1.7, Ea=(26,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOC(C)C(C)O[O] <=> O=C(C)C(C)OO + [OH]
""",
)

entry(
    index = 5,
    label = "C3H7O4-3 <=> C3H6O3-3 + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(25900,'s^-1'), n=1.9, Ea=(18.8,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOCCCO[O] <=> O=CCCOO + [OH]
""",
)

entry(
    index = 6,
    label = "C4H9O4-2 <=> C4H8O3-2 + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5490,'s^-1'), n=2.4, Ea=(19.9,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOCCC(C)O[O] <=> O=CCC(C)OO + [OH]
""",
)

entry(
    index = 7,
    label = "C5H11O4 <=> C5H10O3 + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.5,'s^-1'), n=3.6, Ea=(17.7,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOCC(C)(C)CO[O] <=> O=CC(C)(C)COO + [OH]
""",
)

entry(
    index = 8,
    label = "C4H9O4-3 <=> C4H8O3-3 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(57.9,'s^-1'), n=2.9, Ea=(17,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOC(C)CCO[O] <=> O=C(C)CCOO + [OH]
""",
)

entry(
    index = 9,
    label = "C5H11O4-2 <=> C5H10O3-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(175,'s^-1'), n=3.1, Ea=(17.5,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOC(C)CC(C)O[O] <=> O=C(C)CC(C)OO + [OH]
""",
)

entry(
    index = 10,
    label = "C4H9O4-4 <=> C4H8O3-4 + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2380,'s^-1'), n=1.7, Ea=(16.6,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOCCCCO[O] <=> O=CCCCOO + [OH]
""",
)

entry(
    index = 11,
    label = "C5H11O4-3 <=> C5H10O3-3 + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(628,'s^-1'), n=2.2, Ea=(17.4,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOCCCC(C)O[O] <=> O=CCCC(C)OO + [OH]
""",
)

entry(
    index = 12,
    label = "C5H11O4-4 <=> C5H10O3-4 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(377,'s^-1'), n=2.2, Ea=(15.3,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOC(C)CCCO[O] <=> O=C(C)CCCOO + [OH]
""",
)

entry(
    index = 13,
    label = "C6H13O4 <=> C6H12O3 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(254,'s^-1'), n=2.6, Ea=(16.2,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOC(C)CCC(C)O[O] <=> O=C(C)CCC(C)OO + [OH]
""",
)

entry(
    index = 14,
    label = "C5H11O4-5 <=> C5H10O3-5 + HO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(557,'s^-1'), n=1.8, Ea=(16.6,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOCCCCCO[O] <=> O=CCCCCOO + [OH]
""",
)

entry(
    index = 15,
    label = "C6H13O4-2 <=> C6H12O3-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2000,'s^-1'), n=1.9, Ea=(14.9,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Sharma_alphaQOOH_2010
Original entry: OOC(C)CCCCO[O] <=> O=C(C)CCCCOO + [OH]
""",
)

entry(
    index = 16,
    label = "C4H9O5 <=> C4H8O4 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.658e+10,'s^-1'), n=0.13, Ea=(14.506,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q-1QJ <=> MPO1O-1Q + OH
changed REF: G4 calculations and HID from RMG
""",
)

entry(
    index = 17,
    label = "C4H9O5-2 <=> C4H8O4-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.24e+10,'s^-1'), n=0.555, Ea=(15.724,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q3QJ <=> MPO1O3Q + OH
changed
""",
)
