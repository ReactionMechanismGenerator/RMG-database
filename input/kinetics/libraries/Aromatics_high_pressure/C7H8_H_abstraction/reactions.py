#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C7H8_H_abstraction"
shortDesc = u"H-abstraction reactions for toluene"
longDesc = u"""
Theoretical Prediction of Rate Constants for Hydrogen Abstraction by OH, H, O, CH3, and HO2 Radicals from Toluene
Shu-Hao Li, Jun-Jiang Guo, Rui Li, Fan Wang, Xiang-Yuan Li
J. Phys. Chem. A 2016, 120, 3424−3432

Hydrogen abstraction from toluene by OH, H, O, CH3, and HO2 radicals; Geometries and corresponding harmonic frequencies of the reactants,
transition states as well as products involved in these reactions are determined at the B3LYP/6-31G(2df,p) level.
"""
entry(
    index = 1,
    label = "C6H5CH3 + OH <=> C6H5CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(130169.1, 'cm^3/(mol*s)'), n=2.28048, Ea=(-572.972, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "C6H5CH3 + OH <=> o-C6H4CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(277.7315, 'cm^3/(mol*s)'), n=2.99789, Ea=(1245.721, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "C6H5CH3 + OH <=> m-C6H4CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(819.6653, 'cm^3/(mol*s)'), n=3.09594, Ea=(1507.708, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "C6H5CH3 + OH <=> p-C6H4CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(763.895, 'cm^3/(mol*s)'), n=3.10443, Ea=(1688.651, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "C6H5CH3 + H <=> C6H5CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(75372.24, 'cm^3/(mol*s)'), n=2.57378, Ea=(3145.746, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "C6H5CH3 + H <=> o-C6H4CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(281049.1, 'cm^3/(mol*s)'), n=2.41207, Ea=(8837.35, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "C6H5CH3 + H <=> m-C6H4CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.16e+6, 'cm^3/(mol*s)'), n=2.44202, Ea=(9052.875, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "C6H5CH3 + H <=> p-C6H4CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.57e+6, 'cm^3/(mol*s)'), n=2.40693, Ea=(9440.521, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "C6H5CH3 + O <=> C6H5CH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00788, 'cm^3/(mol*s)'), n=4.29278, Ea=(11250.72, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "C6H5CH3 + O <=> o-C6H4CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71418, 'cm^3/(mol*s)'), n=3.64569, Ea=(21743.27, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "C6H5CH3 + O <=> m-C6H4CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02029, 'cm^3/(mol*s)'), n=3.64209, Ea=(22208.17, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "C6H5CH3 + O <=> p-C6H4CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.79741, 'cm^3/(mol*s)'), n=3.6191, Ea=(22697.45, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "C6H5CH3 + CH3 <=> C6H5CH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07e+06, 'cm^3/(mol*s)'), n=2.26764, Ea=(4392.371, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "C6H5CH3 + CH3 <=> o-C6H4CH3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.21e+07, 'cm^3/(mol*s)'), n=1.81483, Ea=(14155.56, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "C6H5CH3 + CH3 <=> m-C6H4CH3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11e+08, 'cm^3/(mol*s)'), n=1.80464, Ea=(14389.02, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "C6H5CH3 + CH3 <=> p-C6H4CH3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.05e+08, 'cm^3/(mol*s)'), n=1.81188, Ea=(14672.52, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "C6H5CH3 + HO2 <=> C6H5CH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55836, 'cm^3/(mol*s)'), n=3.80712, Ea=(7395.743, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "C6H5CH3 + HO2 <=> o-C6H4CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(91.4407, 'cm^3/(mol*s)'), n=3.28308, Ea=(14233.33, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "C6H5CH3 + HO2 <=> m-C6H4CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(197.2672, 'cm^3/(mol*s)'), n=3.28482, Ea=(14542.45, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "C6H5CH3 + HO2 <=> p-C6H4CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(204.9017, 'cm^3/(mol*s)'), n=3.30806, Ea=(14723.92, 'cal/mol'), T0=(1, 'K')),
)


