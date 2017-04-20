#!/usr/bin/env python
# encoding: utf-8

name = "intra_NO2_ONO_conversion/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "CH3NO2 <=> CH3ONO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7.05e+54, 'cm^3/(mol*s)'), n=-2.35, Ea=(62398, 'kcal/mol'), T0=(1, 'K'))),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
R.S. Zhu, P. Raghunath, M.C. Lin, J. Phys. Chem. A, 2013, 117, 7308-7313, doi: 10.1021/jp401148q
p. 7311
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
""",
)

