#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C7H8"
shortDesc = u"Toluene formation from phenyl+CH3 and benzyl+H"
longDesc = u"""
On the formation and decomposition of C7H8
Stephen J. Klippenstein, Lawrence B. Harding, Yuri Georgievskii
Proceedings of the Combustion Institute 31 (2007) 221–229 

The kinetics of reactions on the C7H8 surface were studied with state-of-the-art ab initio transition state theory (TST) and master equation methodologies. A priori predictions of the capture rate for C6H5+ CH3 and for C7H7 + H are obtained from direct VRC-TST simulations. These simulations
employ small basis set CASPT2 interaction energies coupled with one-dimensional reaction path correctionsbased on higher level simulations for related reactions.
"""
entry(
    index = 1,
    label = "C6H5 + CH3 <=> Toluene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.87e-10, 'cm^3/(molecule*s)'), n=-0.283, Ea=(-0.191, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "C7H7 + H <=> Toluene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.20e-10, 'cm^3/(molecule*s)'), n=0.062, Ea=(-0.044, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "C7H7 + H <=> OiT",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.28e-13, 'cm^3/(molecule*s)'), n=0.611, Ea=(-0.436, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "C7H7 + H <=> PiT",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07e-11, 'cm^3/(molecule*s)'), n=0.245, Ea=(-0.333, 'kcal/mol'), T0=(1, 'K')),
)



