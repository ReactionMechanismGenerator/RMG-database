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

entry(
    index = 7,
    label = "C9H11 <=> C9H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.399e+11, 's^-1'), n=0.121, Ea=(15.859, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2012_Kislov_Phenyl_Propene_w_new_pathway""",
    longDesc = 
u"""
Taken from entry: i2 <=> i3
""",
)

entry(
    index = 8,
    label = "C9H11-5 <=> C9H11-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.815e+11, 's^-1'), n=0.121, Ea=(32.19, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2012_Kislov_Phenyl_Propene_w_new_pathway""",
    longDesc = 
u"""
Taken from entry: i2 <=> i8
""",
)

entry(
    index = 9,
    label = "C9H11-3 <=> C9H11-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.528e+11, 's^-1'), n=0.199, Ea=(16.505, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2012_Kislov_Phenyl_Propene_w_new_pathway""",
    longDesc = 
u"""
Taken from entry: i1 <=> i3
""",
)

entry(
    index = 10,
    label = "C9H11-7 <=> C9H11-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.31e+11, 's^-1'), n=0.001, Ea=(17.806, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2012_Kislov_Phenyl_Propene_w_new_pathway""",
    longDesc = 
u"""
Taken from entry: i4 <=> i5
""",
)
