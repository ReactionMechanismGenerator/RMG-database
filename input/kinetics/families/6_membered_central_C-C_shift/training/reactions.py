#!/usr/bin/env python
# encoding: utf-8

name = "6_membered_central_C-C_shift/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.30946e+10, 's^-1'),
        n = 0.360276,
        Ea = (144.706, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: I <=> II
""",
)

entry(
    index = 1,
    label = "C6H6-3 <=> C6H6-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.06322e+11, 's^-1'),
        n = -0.0265989,
        Ea = (166.561, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P_reverse""",
    longDesc = 
u"""
Taken from entry: II <=> I
""",
)

entry(
    index = 2,
    label = "C10H10 <=> C10H10-2",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(2.214e+09, 's^-1'), n=0.749, Ea=(47.859, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W1 <=> W4
""",
)

entry(
    index = 3,
    label = "C10H10-2 <=> C10H10",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(3.213e+11, 's^-1'), n=0.07, Ea=(18.329, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W4 <=> W1
""",
)

entry(
    index = 4,
    label = "C10H10-3 <=> C10H10-4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(4.484e+11, 's^-1'), n=0.032, Ea=(50.631, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W2 <=> W3
""",
)

entry(
    index = 5,
    label = "C10H10-4 <=> C10H10-3",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(3.626e+11, 's^-1'), n=0.119, Ea=(18.066, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W3 <=> W2
""",
)

