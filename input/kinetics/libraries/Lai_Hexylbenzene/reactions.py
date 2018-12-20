#!/usr/bin/env python
# encoding: utf-8

name = "Lai_Hexylbenzene"
shortDesc = u"Reactions for Hexylbenzene pyrolysis at 450C"
longDesc = u"""
In conjunction with the Lai_Hexylbenzene thermo library,
this reaction library contains CBS-QB3 calculations for reactions
relevant to Hexylbenzene pyrolysis and supercritical water treatment.

Lai, Lawrence, Gudiyella, Soumya, Liu, Mengjie, Green, William H. "Chemistry of Alkylaromatics Reconsidered". To be submitted to Energy and Fuels, 2017.

Both calculations are done in CBS-QB3 level of theory.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
3. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step, using B3LYP/CBSB7
4. All files generated were fed to Cantherm.
5. Frequency scaling factor was 0.99
6. Bond additivity corrections were not used.

Disclaimer: The number of significant figures displayed does not reflect the accuracy of thermochemistry values. Sommers and Simmie esimates
the error in enthalpy of formation (and therefore the activation energy) by CBS-QB3 calculations to be + or - 2.4kcal/mol 
(http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448). 
"""
entry(
    index = 1,
    label = "butyl + styrene <=> rad1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(236.006, 'cm^3/(mol*s)'), n=2.7878, Ea=(15.4228, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, April 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Kinetics
    """
)

entry(
    index = 2,
    label = "Hexylbenzene <=> Toluene + 1-Pentene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.62907e+07, 's^-1'), n=1.6863, Ea=(309.226, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Max Liu, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Kinetics
    """
)

entry(
    index = 3,
    label = "Hexylbenzene + H <=> HexylbenzenePlusHSub",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.76237e+07, 'cm^3/(mol*s)'), n=1.70829, Ea=(25.4744, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 4,
    label = "Toluene + H <=> ToluenePlusHOrtho",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.02442e+09, 'cm^3/(mol*s)'), n=1.43982, Ea=(18.8871, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 5,
    label = "Toluene + H <=> ToluenePlusHMeta",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.07929e+09, 'cm^3/(mol*s)'), n=1.42903, Ea=(22.7647, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 6,
    label = "Toluene + H <=> ToluenePlusHPara",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1233e+09, 'cm^3/(mol*s)'), n=1.42368, Ea=(22.5731, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 7,
    label = "Toluene + H <=> ToluenePlusHSub",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.20433e+08, 'cm^3/(mol*s)'), n=1.56916, Ea=(26.7856, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 8,
    label = "Toluene + CH3 <=> ToluenePlusCH3Ortho",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3383.86, 'cm^3/(mol*s)'), n=2.311, Ea=(37.9756, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 9,
    label = "Toluene + CH3 <=> ToluenePlusCH3Meta",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3356.39, 'cm^3/(mol*s)'), n=2.32609, Ea=(41.1979, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 10,
    label = "Toluene + CH3 <=> ToluenePlusCH3Para",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3945.69, 'cm^3/(mol*s)'), n=2.31104, Ea=(41.6199, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 11,
    label = "Toluene + CH3 <=> ToluenePlusCH3Sub",
    degeneracy = 1,
    kinetics = Arrhenius(A=(144.44, 'cm^3/(mol*s)'), n=2.6469, Ea=(43.8158, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, December 2017, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals
    """
)

entry(
    index = 12,
    label = "rad4 <=> EthyltetralinRad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29023.5, 's^-1'), n=1.19861, Ea=(27.5998, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, March 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/intra_R_Add_Exocyclic
    """
)

entry(
    index = 13,
    label = "rad3 <=> PropylindaneRad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14489047644, 's^-1'), n=1.22276, Ea=(57.6245, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, March 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/intra_R_Add_Exocyclic
    """
)

entry(
    index = 14,
    label = "EthyltetralinRad <=> Ethyltetralin + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59167e+10, 's^-1'), n=0.899322, Ea=(121.108, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, March 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission
    """
)

entry(
    index = 15,
    label = "PropylindaneRad <=> Propylindane + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44564e+10, 's^-1'), n=0.96702, Ea=(108.102, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, March 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission
    """
)

entry(
    index = 16,
    label = "Toluene + Benzyl <=> ToluenePlusBenzylOrtho",
    degeneracy = 2,
    kinetics = Arrhenius(A=(75.2016, 'cm^3/(mol*s)'), n=2.87538, Ea=(47.3967, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 17,
    label = "Toluene + Benzyl <=> ToluenePlusBenzylMeta",
    degeneracy = 2,
    kinetics = Arrhenius(A=(333.522, 'cm^3/(mol*s)'), n=2.81143, Ea=(52.4195, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 18,
    label = "Toluene + Benzyl <=> ToluenePlusBenzylPara",
    degeneracy = 1,
    kinetics = Arrhenius(A=(203.185, 'cm^3/(mol*s)'), n=2.7789, Ea=(51.957, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 19,
    label = "Toluene + Benzyl <=> ToluenePlusBenzylSub",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.0143, 'cm^3/(mol*s)'), n=3.28044, Ea=(49.7678, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 20,
    label = "Toluene + Ethylbenzyl <=> ToluenePlusEBenzylOrtho",
    degeneracy = 2,
    kinetics = Arrhenius(A=(9.9686, 'cm^3/(mol*s)'), n=3.05153, Ea=(47.5686, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 21,
    label = "Toluene + Ethylbenzyl <=> ToluenePlusEBenzylMeta",
    degeneracy = 2,
    kinetics = Arrhenius(A=(6.36177, 'cm^3/(mol*s)'), n=3.21235, Ea=(47.2354, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 22,
    label = "Toluene + Ethylbenzyl <=> ToluenePlusEBenzylPara",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8336, 'cm^3/(mol*s)'), n=3.1834, Ea=(47.5562, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 23,
    label = "Toluene + Ethylbenzyl <=> ToluenePlusEBenzylSub",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0289968, 'cm^3/(mol*s)'), n=3.67504, Ea=(50.8048, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2018/AdditionToRing
    """
)

entry(
    index = 24,
    label = "EthylDihydronaphthaleneRadNear <=> EthylDihydronaphthaleneNear + H",
    degeneracy = 1,
    kinetics = Arrhenius(A = (3.68955e+10, 's^-1'), n=1.08869, Ea=(183.348, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission/
    """
)

entry(
    index = 25,
    label = "EthylnaphthaleneRadFar <=> Ethylnaphthalene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.224e+11, 's^-1'), n=0.872685, Ea=(137.28, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission/
    """
)

entry(
    index = 26,
    label = "EthylnaphthaleneRadFar2 <=> Ethylnaphthalene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.44555e+10, 's^-1'), n=0.95781, Ea=(120.415, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission/
    """
)

entry(
    index = 27,
    label = "EthylnaphthaleneRadNear <=> Ethylnaphthalene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.36561e+09, 's^-1'), n=1.10493, Ea=(137.408, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission/
    """
)

entry(
    index = 28,
    label = "EthylnaphthaleneRadNear2 <=> Ethylnaphthalene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.05825e+09, 's^-1'), n=1.15256, Ea=(119.092, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission/
    """
)

entry(
    index = 29,
    label = "PropylindeneRadFar <=> PropylindeneFar + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.75035e+09, 's^-1'), n=1.25622, Ea=(174.095, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"Calculation performed by Lawrence Lai, July 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclic Betascission/
    """
)
