#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""


entry(
    index = 1,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.32e+10, 's^-1'), n=0.35, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product38 <=> product39
""",
)

entry(
    index = 2,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.95e+12, 's^-1'), n=0.12, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product39 <=> product37
""",
)



entry(
    index = 3,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.69e+11, 's^-1'), n=0.22, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt18 <=> pdt19
""",
)

entry(
    index = 4,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt23
""",
)

entry(
    index = 5,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.02e+11, 's^-1'), n=0.79, Ea=(35.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt55 <=> pdt58
""",
)



entry(
    index = 6,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 's^-1'), n=0.45, Ea=(25.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod2 <=> prod5
""",
)



# entry(
#     index = 7,
#     label = "C9H11 <=> C9H11-2",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(5.01e+07, 's^-1'), n=1.03, Ea=(14.13, 'kcal/mol'), T0=(1, 'K')),
#     rank = 3,
#     shortDesc = u"""Training reaction from kinetics library: ipso""",
#     longDesc = 
# u"""
# Taken from entry: R2 <=> M2
# """,
# )

# entry(
#     index = 8,
#     label = "C9H11-3 <=> C9H11-4",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(5.25e+12, 's^-1'), n=0.19, Ea=(4.1, 'kcal/mol'), T0=(1, 'K')),
#     rank = 3,
#     shortDesc = u"""Training reaction from kinetics library: ipso""",
#     longDesc = 
# u"""
# Taken from entry: M2 <=> P2
# """,
# )

# entry(
#     index = 9,
#     label = "C10H13 <=> C10H13-2",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(363000, 's^-1'), n=1.23, Ea=(17.56, 'kcal/mol'), T0=(1, 'K')),
#     rank = 3,
#     shortDesc = u"""Training reaction from kinetics library: ipso""",
#     longDesc = 
# u"""
# Taken from entry: R4 <=> M4
# """,
# )

# entry(
#     index = 10,
#     label = "C10H13-3 <=> C10H13-4",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(8.51e+12, 's^-1'), n=0.19, Ea=(9.77, 'kcal/mol'), T0=(1, 'K')),
#     rank = 3,
#     shortDesc = u"""Training reaction from kinetics library: ipso""",
#     longDesc = 
# u"""
# Taken from entry: M4 <=> P4
# """,
# )

# entry(
#     index = 11,
#     label = "C11H15 <=> C11H15-2",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(5370, 's^-1'), n=1.38, Ea=(8.62, 'kcal/mol'), T0=(1, 'K')),
#     rank = 3,
#     shortDesc = u"""Training reaction from kinetics library: ipso""",
#     longDesc = 
# u"""
# Taken from entry: R6 <=> M6
# """,
# )

entry(
    index = 12,
    label = "C11H15-3 <=> C11H15-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+13, 's^-1'), n=0.11, Ea=(18.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: ipso""",
    longDesc = 
u"""
Taken from entry: M6 <=> P6
""",
)



entry(
    index = 13,
    label = "C12H17 <=> C12H17-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.46139e+07, 's^-1'),
        n = 1.30419,
        Ea = (55.0202, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: HBPhenylMigration""",
    longDesc = 
u"""
Taken from entry: HBrad2 <=> Ringrad2
""",
)

entry(
    index = 14,
    label = "C12H17-3 <=> C12H17-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1705e+13, 's^-1'),
        n = 0.383545,
        Ea = (19.8224, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: HBPhenylMigration""",
    longDesc = 
u"""
Taken from entry: Ringrad2 <=> 2HBrad
""",
)

entry(
    index = 15,
    label = "C12H17-5 <=> C12H17-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(966131, 's^-1'), n=1.86605, Ea=(70.406, 'kJ/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: HBPhenylMigration""",
    longDesc = 
u"""
Taken from entry: HBrad3 <=> Ringrad3
""",
)

entry(
    index = 16,
    label = "C12H17-7 <=> C12H17-8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.0336e+12, 's^-1'),
        n = 0.135082,
        Ea = (42.4869, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: HBPhenylMigration""",
    longDesc = 
u"""
Taken from entry: Ringrad3 <=> 3HBrad
""",
)

entry(
    index = 17,
    label = "C12H17-9 <=> C12H17-10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(905.719, 's^-1'), n=2.15234, Ea=(31.5813, 'kJ/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: HBPhenylMigration""",
    longDesc = 
u"""
Taken from entry: HBrad4 <=> Ringrad4
""",
)

entry(
    index = 18,
    label = "C12H17-11 <=> C12H17-12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3477e+12, 's^-1'),
        n = 0.514347,
        Ea = (72.4192, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: HBPhenylMigration""",
    longDesc = 
u"""
Taken from entry: Ringrad4 <=> 4HBrad
""",
)

entry(
    index = 19,
    label = "C12H17-13 <=> C12H17-14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(284.136, 's^-1'), n=1.70342, Ea=(26.0501, 'kJ/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: HBPhenylMigration""",
    longDesc = 
u"""
Taken from entry: HBrad5 <=> Ringrad5
""",
)

entry(
    index = 20,
    label = "C12H17-15 <=> C12H17-16",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.86326e+12, 's^-1'),
        n = 0.527375,
        Ea = (90.7394, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: HBPhenylMigration""",
    longDesc = 
u"""
Taken from entry: Ringrad5 <=> 5HBrad
""",
)

