#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/Thial_Hydrolysis"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "CH2S + H2O <=> CH2OHSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(960, 'cm^3/(mol*s)'), n=2.43, Ea=(28.13, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "CH3CHS + H2O <=> CHCH3OHSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(15.4, 'cm^3/(mol*s)'), n=2.78, Ea=(27.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "CH2OHSJ <=> CHOHS + HJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.51e+08, 's^-1'), n=1.64, Ea=(34.58, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "CHCH3OHSJ <=> CHOHS + CH3J",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.09e+10, 's^-1'), n=1.02, Ea=(29.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "CHOHS <=> CHOSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+12, 's^-1'), n=0.13, Ea=(28.48, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "CHOSJ <=> COS + HJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.81e+09, 's^-1'), n=1.13, Ea=(17.98, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "COS + H2O <=> CSOHOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.16, 'cm^3/(mol*s)'), n=3.67, Ea=(27.56, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
1st pathway, 1st step 53.85 w/o catalysis
""",
)

entry(
    index = 8,
    label = "CSOHOH <=> COSHOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.13e+15, 's^-1'), n=-0.65, Ea=(28.98, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "COSHOH <=> CO2 + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.25e+13, 's^-1'), n=-0.09, Ea=(37.78, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "COS + H2O <=> COSHOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13, 'cm^3/(mol*s)'), n=3.35, Ea=(25.79, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
2nd pathway, 1st step 43.86 w/o catalysis
""",
)

entry(
    index = 11,
    label = "H2S + CH2O <=> CH2OHSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(50.2, 'cm^3/(mol*s)'), n=3.01, Ea=(38.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
3rd pathway, form aldehyde from first product (reverse)
""",
)

entry(
    index = 12,
    label = "H2S + CH3CHO <=> CHCH3OHSH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(46.9, 'cm^3/(mol*s)'), n=2.9, Ea=(37.1, 'kcal/mol'), T0=(1, 'K')),
)

