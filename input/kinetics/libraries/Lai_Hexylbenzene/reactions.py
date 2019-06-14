#!/usr/bin/env python
# encoding: utf-8

name = "Lai_Hexylbenzene"
shortDesc = u"Reactions for Hexylbenzene pyrolysis at 450C"
longDesc = u"""
In conjunction with the Lai_Hexylbenzene thermo library,
this reaction library contains CBS-QB3 calculations for reactions
relevant to Hexylbenzene pyrolysis and supercritical water treatment.

Lai, Lawrence, Gudiyella, Soumya, Liu, Mengjie, Green, William H. "Chemistry of Alkylaromatics Reconsidered". Energy Fuels, 2018, 32 (4), pp 5489-5500.
Lai, Lawrence, Green, William H. "Thermochemistry and Kinetics of Intermolecular Addition of Radicals to Toluene and Alkylaromatics". J. Phys. Chem. A., 2019, 123 (14), pp 3176-3184
Khanniche, Sarah, Lai, Lawrence, Green, William H. "Kinetics of Intramolecular Phenyl Migration and Fused Ring Formation in Hexylbenzene Radicals". J. Phys. Chem. A, 2018, 122 (51), pp 9778-9791.
Lai, Lawrence, Pang, Hao-Wei, Green, William H. "Formation of 2-Ring Aromatics in Hexylbenzene Pyrolysis". To be submitted to Energy Fuels, 2019.

All calculations are done in CBS-QB3 level of theory.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
3. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step, using B3LYP/CBSB7
4. All files generated were fed to Arkane.
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

entry(
    index = 30,
    label = "rad2 <=> PM2Rad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.46139e+07, 's^-1'),
        n = 1.30419,
        Ea = (55.0202, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
	Location of calculations Pharos/home/laitcl/Gaussian/2019/
    """
)

entry(
    index = 31,
    label = "PM2Rad <=> 2-Phenyl-1-hexylRad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1705e+13, 's^-1'),
        n = 0.383545,
        Ea = (19.8224, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
	allow_max_rate_violation=True,
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
	Location of calculations Pharos/home/laitcl/Gaussian/2019/
	This rate violates the TST limit by a factor of 2 at 1000K. Likely caused by thermo. 
    """
)

entry(
    index = 32,
    label = "rad3 <=> PM3Rad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (966131, 's^-1'),
        n = 1.86605,
        Ea = (70.406, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
    Location of calculations Pharos/home/laitcl/Gaussian/2019/
	"""
)

entry(
    index = 33,
    label = "PM3Rad <=> 3-Phenyl-1-hexylRad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.0336e+12, 's^-1'),
        n = 0.135082,
        Ea = (42.4869, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
    Location of calculations Pharos/home/laitcl/Gaussian/2019/
	"""
)

entry(
    index = 34,
    label = "rad4 <=> PM4Rad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (905.58, 's^-1'),
        n = 2.15236,
        Ea = (31.9171, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
	Location of calculations Pharos/home/laitcl/Gaussian/2019/
    """
)

entry(
    index = 35,
    label = "PM4Rad <=> 4-phenyl-1-hexylRad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2027e+12, 's^-1'),
        n = 0.53843,
        Ea = (76.0115, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
    Location of calculations Pharos/home/laitcl/Gaussian/2019/
	"""
)

entry(
    index = 36,
    label = "rad5 <=> PM5Rad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (284.136, 's^-1'),
        n = 1.70342,
        Ea = (26.0501, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
    Location of calculations Pharos/home/laitcl/Gaussian/2019/
	"""
)

entry(
    index = 37,
    label = "PM5Rad <=> 5-Phenyl-1-hexylRad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.86326e+12, 's^-1'),
        n = 0.527375,
        Ea = (90.7394, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
    Location of calculations Pharos/home/laitcl/Gaussian/2019/
	"""
)

entry(
    index = 38,
    label = "phenylrad + ethylbenzene <=> ethylbiphenylRad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.05685, 'cm^3/(mol*s)'),
        n = 3.09388,
        Ea = (8.15269, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2019/
	"""
)

entry(
    index = 39,
    label = "ethylrad + biphenyl <=> ethylbiphenylRad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (103.514, 'cm^3/(mol*s)'),
        n = 2.90893,
        Ea = (44.9425, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2019/
	"""
)

entry(
    index = 40,
    label = "Benzene + CH3 <=> ToluenePlusHSub",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (126531, 'cm^3/(mol*s)'),
        n = 2.32659,
        Ea = (42.0038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2019/
	"""
)

entry(
    index = 41,
    label = "rad5 <=> methylbenozocyclohepteneRad",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17725.7, 's^-1'),
        n = 1.16281,
        Ea = (42.1994, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    shortDesc = u"Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory",
    longDesc = 
    u"""
    Location of calculations Pharos/home/laitcl/Gaussian/2019/
	"""
)
