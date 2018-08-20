#!/usr/bin/env python
# encoding: utf-8

name = "H2_Loss/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "C14H12 <=> C14H10 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.73e+09, '1/s'), n=0.797, Ea=(17.176, 'kcal/mol'), T0=(1, 'K')),
    rank = 8,
    longDesc = 
u"""
V. V. Kislov, N. I. Islamova, A. M. Kolker, S. H. Lin, and A. M. Mebel;
Hydrogen Abstraction Acetylene Addition and Diels-Alder Mechanisms of PAH Formation: A Detailed Study Using First Principles Calculations; 
J. Chem. Theory Comput. 2005, 1, 908-924.
Original entry: B2 <=> P + H2
""",
)

entry(
    index = 2,
    label = "C16H12 <=> C16H10 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.52e+10, '1/s'), n=0.533, Ea=(17.938, 'kcal/mol'), T0=(1, 'K')),
    rank = 8,
    longDesc = 
u"""
V. V. Kislov, N. I. Islamova, A. M. Kolker, S. H. Lin, and A. M. Mebel;
Hydrogen Abstraction Acetylene Addition and Diels-Alder Mechanisms of PAH Formation: A Detailed Study Using First Principles Calculations;
J. Chem. Theory Comput. 2005, 1, 908-924.
Original entry: P1 <=> PYR + H2
""",
)

