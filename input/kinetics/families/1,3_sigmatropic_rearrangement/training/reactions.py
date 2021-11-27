#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C3H6O <=> C3H6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7040,'s^-1'), n=2.66, Ea=(351.456,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 11,
    shortDesc = """W.H. Green estimate
                   A,n from R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H
                   Ea = C-C BDE""",
    longDesc = 
"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_C
""",
)






