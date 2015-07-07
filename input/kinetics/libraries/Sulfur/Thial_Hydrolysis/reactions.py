#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/Thial_Hydrolysis"
shortDesc = u"reactions from thial to CO2"
longDesc = u"""
calculated rate constants (by Caleb?) for the pathway
from thioformaldehyde and thioacetaldehyde to COS and then CO2.
"""
#entry(
#    index = 1,
#    label = "CH2S + H2O <=> CH2OHSH",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(960, 'cm^3/(mol*s)'), n=2.43, Ea=(28.13, 'kcal/mol'), T0=(1, 'K')),
#)
#
#entry(
#    index = 2,
#    label = "CH3CHS + H2O <=> CHCH3OHSH",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(15.4, 'cm^3/(mol*s)'), n=2.78, Ea=(27.8, 'kcal/mol'), T0=(1, 'K')),
#)
#
entry(
    index = 1,
    label = "CH2OHSJ <=> CHOHS + HJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.51e+08, 's^-1'), n=1.64, Ea=(34.58, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "CHCH3OHSJ <=> CHOHS + CH3J",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.09e+10, 's^-1'), n=1.02, Ea=(29.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "CHOHS <=> CHOSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 's^-1'), n=0.13, Ea=(28.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "CHOSJ <=> COS + HJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.81e+09, 's^-1'), n=1.13, Ea=(17.98, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "COS + H2O <=> CSOHOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5880, 'cm^3/(mol*s)'), n=2.47, Ea=(61.59, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "CSOHOH <=> COSHOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.13e+15, 's^-1'), n=-0.65, Ea=(28.98, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "COSHOH <=> CO2 + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.29, 's^-1'), n=3.63, Ea=(38.18, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "COS + H2O <=> COSHOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.87e-07, 'cm^3/(mol*s)'),
        n = 5.38,
        Ea = (45.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "H2S + CH2O <=> CH2OHSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(50.2, 'cm^3/(mol*s)'), n=3.01, Ea=(38.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
3rd pathway, form aldehyde from first product (reverse)
""",
)

entry(
    index = 10,
    label = "H2S + CH3CHO <=> CHCH3OHSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(46.9, 'cm^3/(mol*s)'), n=2.9, Ea=(37.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "CO + H2O <=> CO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5000, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
	longDesc = 
u"""
Approximate water-gas shift reaction
""",
)

entry(
    index = 12,
    label = "CHCH3OHSH + H2O <=> CH3CHO + H2S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.46, 'cm^3/(mol*s)'), n=3.05, Ea=(21.52, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "CHCH3OHSH + H2S <=> CH3CHO + H2S + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.172, 'cm^3/(mol*s)'), n=3.43, Ea=(27.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "CHCH3OHSH + H2O <=> CH3CHS + H2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13.2, 'cm^3/(mol*s)'), n=2.56, Ea=(20.55, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "CHCH3OHSH + H2S <=> CH3CHS + H2O + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.14, 'cm^3/(mol*s)'), n=2.93, Ea=(28.62, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "COSHOH + H2O <=> COS + H2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(429, 'cm^3/(mol*s)'), n=2.45, Ea=(19.54, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "COSHOH + H2O <=> CO2 + H2S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1180, 'cm^3/(mol*s)'), n=2.49, Ea=(17.76, 'kcal/mol'), T0=(1, 'K')),
)

