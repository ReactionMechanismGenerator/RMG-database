#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_Carbene_Intra_Disproportionation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
Sources:
[1] Characterization of the 1,1-HCl Elimination Reaction of Vibrationally Excited CD3CHFCl Molecules and Assignment of Threshold Energies for 1,1-HCl and 1,2-DCl plus 1,1-HF and 1,2-DF Elimination Reactions
    Timothy M. Brown, Matthew J. Nestler, Samuel M. Rossabi, George L. Heard, D. W. Setser, and Bert E. Holmes
    The Journal of Physical Chemistry A 2015 119 (36), 9441-9451
    DOI: 10.1021/acs.jpca.5b06638

[2] Unimolecular HBr and HF Elimination Reactions of Vibrationally Excited C2H5CH2Br and C2D5CHFBr: Identification of the 1,1-HBr Elimination Reaction from C2D5CHFBr and Search for the C2D5(F)C:HBr Adduct
    Timothy M. Brown, Blanton R. Gillespie, Mallory M. Rothrock, Anthony J. Ranieri, Melinda K. Schueneman, George L. Heard, Donald W. Setser, and Bert E. Holmes
    The Journal of Physical Chemistry A 2019 123 (41), 8776-8786
    DOI: 10.1021/acs.jpca.9b07029
"""
entry(
    index = 0,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.067e+10, 's^-1'), n=0.649, Ea=(8.03, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: A <=> IV
""",
)

entry(
    index = 1,
    label = "C6H6-3 <=> C6H6-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.454e+12, 's^-1'), n=0.178, Ea=(0.205, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: IX <=> VII
""",
)

entry(
    index = 2,
    label = "C6H6-5 <=> C6H6-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.865e+11, 's^-1'), n=0.577, Ea=(29.169, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: X <=> IX
""",
)

entry(
    index = 3,
    label = "C6H6-7 <=> C6H6-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.355e+12, 's^-1'), n=0.294, Ea=(35.954, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: X <=> XI
""",
)

entry(
    index = 4,
    label = "C2F4 <=> C2F4-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(5.731e+10,'s^-1'), n=0.827, Ea=(35644,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CF3CF <=> CF2:CF2""",
    longDesc = 
"""
Training reaction from kinetics library: YF
Original entry: CF3CF <=> CF2:CF2
""",
)

entry(
    index = 5,
    label = "CH3CF <=> CH2CHF",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1e13,'s^-1'), n=0, Ea=(15,'kcal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Ea is threshold energy for CD3CF -> CD2=CDF from Figure 1 in [1]
A factor estimated
""",
)

entry(
    index = 6,
    label = "CH3CCl <=> CH2CHCl",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1e13,'s^-1'), n=0, Ea=(10,'kcal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Ea is threshold energy for CD3CCl -> CD2=CDCl from Figure 1 in [1]
A factor estimated
""",
)

entry(
    index = 7,
    label = "CH3CH2CBr <=> CH3CHCHBr",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1e13,'s^-1'), n=0, Ea=(4.2,'kcal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Ea is threshold energy for CD3CD2CCl -> CD3CD=CDCl from Figure 6 in [2]
A factor estimated
""",
)

