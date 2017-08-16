#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C2H3O3 <=> C2H3O3-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.3e+09, 's^-1', '*|/', 2.51189),
        n = 0.75,
        Ea = (23.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["J. W. Allen", "C. F. Goldsmith", "W. H. Green"],
        title = u'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "???",
        pages = """???-???""",
        year = "2011 (accepted)",
    ),
    referenceType = "theory",
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
""",
)

entry(
    index = 1,
    label = "S1C4 <=> S1C4b",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.775e+09, 's^-1', '*|/', 3),
        n = 0.686,
        Ea = (6.774, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["E. E. Dames", "W. H. Green"],
        title = u'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = "Intl. J. Chem. Kin.",
        volume = "???",
        pages = """???-???""",
        year = "2015",
    ),
    referenceType = "theory",
    shortDesc = u"""TST calculations at M08SO/MG3S level""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S level
using Qchem. High-pressure-limit rate coefficient computed
using Cantherm with 1D hindered rotor treatment.
""",
)

entry(
    index = 2,
    label = "S2C4 <=> S2C4b",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (15400, 's^-1', '*|/', 3),
        n = 2.338,
        Ea = (7.127, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["E. E. Dames", "W. H. Green"],
        title = u'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = "Intl. J. Chem. Kin.",
        volume = "???",
        pages = """???-???""",
        year = "2015",
    ),
    referenceType = "theory",
    shortDesc = u"""TST calculations at M08SO/MG3S level""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S level
using Qchem. High-pressure-limit rate coefficient computed
using Cantherm with 1D hindered rotor treatment.
""",
)

entry(
    index = 3,
    label = "C4H7O2 <=> C4H7O2b",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (63.58, 's^-1', '*|/', 3.66),
        n = 2.81162,
        Ea = (8.231, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    referenceType = "theory",
    shortDesc = u"""TST calculations at M08SO/MG3S level by edames""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S* level using Qchem. High-pressure-limit rate coefficient computed using Cantherm with 1D hindered rotor treatment for all relevant rotors. (*A computational grid with 75 radial points and 434 angular points per radial point was used in the calculations for all species)
""",
)

entry(
    index = 4,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.97e+06, 's^-1'), n=1.8, Ea=(37.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addA <=> addB
""",
)

entry(
    index = 5,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.81e+07, 's^-1'), n=1.72, Ea=(44.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addC <=> addD
""",
)

entry(
    index = 6,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.37e+06, 's^-1'), n=1.6, Ea=(25.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product7
""",
)

entry(
    index = 7,
    label = "C7H9-7 <=> C7H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.88e+09, 's^-1'), n=1, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addA <=> product7
""",
)

entry(
    index = 8,
    label = "C7H9-9 <=> C7H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.36e+08, 's^-1'), n=1.39, Ea=(24.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addD <=> product10
""",
)

entry(
    index = 9,
    label = "C7H9-11 <=> C7H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.11e+09, 's^-1'), n=1.34, Ea=(47.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product4 <=> product9
""",
)

entry(
    index = 10,
    label = "C7H9-13 <=> C7H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.03e+06, 's^-1'), n=1.96, Ea=(50.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product2 <=> product5
""",
)

entry(
    index = 11,
    label = "C7H9-15 <=> C7H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(367000, 's^-1'), n=2.24, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product17 <=> product6
""",
)

entry(
    index = 12,
    label = "C7H9-17 <=> C7H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.9e+10, 's^-1'), n=0.87, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product29 <=> product23
""",
)

entry(
    index = 13,
    label = "C7H9-19 <=> C7H9-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(285000, 's^-1'), n=2.15, Ea=(43.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product31 <=> product35
""",
)

entry(
    index = 14,
    label = "C7H9-21 <=> C7H9-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(671000, 's^-1'), n=2.07, Ea=(48.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product32 <=> product38
""",
)

entry(
    index = 15,
    label = "C7H7 <=> C7H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41e+08, 's^-1'), n=1.52, Ea=(38.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product34 <=> product46
""",
)

entry(
    index = 16,
    label = "C7H7-3 <=> C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product44 <=> vinylCPDyl
""",
)

entry(
    index = 17,
    label = "C7H7-5 <=> C7H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product44 <=> product41
""",
)

entry(
    index = 18,
    label = "C7H7-7 <=> C7H7-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: vinylCPDyl <=> product41
""",
)

entry(
    index = 19,
    label = "C5H5 <=> C5H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+10, 's^-1'), n=0.98, Ea=(26.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_24 <=> CPDyl
""",
)

entry(
    index = 20,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.71e+10, 's^-1'), n=1.01, Ea=(27.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_26 <=> meCPDyl
""",
)

entry(
    index = 21,
    label = "C6H7-3 <=> C6H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+10, 's^-1'), n=1.01, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_28 <=> meCPDyl
""",
)

entry(
    index = 22,
    label = "C6H7-5 <=> C6H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.24e+09, 's^-1'), n=1.12, Ea=(39.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_30 <=> prod_33
""",
)

entry(
    index = 23,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.107, 's^-1'), n=3.67, Ea=(29.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt20
""",
)

entry(
    index = 24,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(250000, 's^-1'), n=1.95, Ea=(24, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt18 <=> pdt25
""",
)

entry(
    index = 25,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.59e+08, 's^-1'), n=1.01, Ea=(26.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt16 <=> pdt20
""",
)

entry(
    index = 26,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.67e+09, 's^-1'), n=1.14, Ea=(22.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt28 <=> pdt29
""",
)

entry(
    index = 27,
    label = "C10H11-9 <=> C10H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.46e+07, 's^-1'), n=1.66, Ea=(31.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt28 <=> pdt23
""",
)

entry(
    index = 28,
    label = "C10H11-11 <=> C10H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.83e+08, 's^-1'), n=1.45, Ea=(31.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt10bis <=> pdt37
""",
)

entry(
    index = 29,
    label = "C10H11-13 <=> C10H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.36e+06, 's^-1'), n=1.7, Ea=(31.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: adductd <=> pdt55
""",
)

entry(
    index = 30,
    label = "C10H11-15 <=> C10H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.78e+06, 's^-1'), n=1.75, Ea=(25.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt15 <=> pdt55
""",
)

entry(
    index = 31,
    label = "C10H11-17 <=> C10H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04e+07, 's^-1'), n=1.61, Ea=(27.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt58 <=> pdt20
""",
)

entry(
    index = 32,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.48e+08, 's^-1'),
        n = 1.62,
        Ea = (162.172, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: [5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green.

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 33,
    label = "C3H7 <=> C3H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.918e+09, 's^-1'),
        n = 1.39,
        Ea = (166.105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: [5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green.

Converted to training reaction from rate rule: R2H_S;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 34,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.39e+09, 's^-1'),
        n = 0.98,
        Ea = (141.252, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: [5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 35,
    label = "C4H9 <=> C4H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.76e+09, 's^-1'),
        n = 0.76,
        Ea = (145.185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: [5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 36,
    label = "C4H9-3 <=> C4H9-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.54e+09, 's^-1'),
        n = 0.35,
        Ea = (82.6758, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: [5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.

Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 37,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.22e+09, 's^-1'),
        n = 0.13,
        Ea = (86.6088, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: [5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.

Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 38,
    label = "C6H13 <=> C6H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.86e+10, 's^-1'),
        n = 0.58,
        Ea = (109.579, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: [5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. 

NEEDS TO BE CHECKED

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_single;Cs_H_out_noH
""",
)

entry(
    index = 39,
    label = "C5H11-3 <=> C5H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.28e+11, 's^-1'),
        n = -1.05,
        Ea = (49.2038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: [5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green

Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 40,
    label = "C6H13-3 <=> C6H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.36e+10, 's^-1'),
        n = -0.66,
        Ea = (59.7475, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: [5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green

Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 41,
    label = "C3H7O <=> C3H7O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3e+11, 's^-1'),
        n = 0,
        Ea = (123.01, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R4H_SSS;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 42,
    label = "C4H9O <=> C4H9O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2e+11, 's^-1'),
        n = 0,
        Ea = (112.34, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R4H_SSS;O_rad_out;Cs_H_out_1H
""",
)

entry(
    index = 43,
    label = "C5H11O <=> C5H11O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0,
        Ea = (100.834, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R4H_SSS;O_rad_out;Cs_H_out_noH
""",
)

entry(
    index = 44,
    label = "C4H9O-3 <=> C4H9O-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.75e+10, 's^-1'),
        n = 0,
        Ea = (102.09, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R5H_SSSS;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 45,
    label = "C5H11O-3 <=> C5H11O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.5e+10, 's^-1'),
        n = 0,
        Ea = (87.2364, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R5H_SSSS;O_rad_out;Cs_H_out_1H
""",
)

entry(
    index = 46,
    label = "C6H13O <=> C6H13O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+10, 's^-1'),
        n = 0,
        Ea = (79.9144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R5H_SSSS;O_rad_out;Cs_H_out_noH
""",
)

entry(
    index = 47,
    label = "C5H11O-5 <=> C5H11O-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.68e+09, 's^-1'),
        n = 0,
        Ea = (93.5124, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R6H_SSSSS;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 48,
    label = "C6H13O-3 <=> C6H13O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.12e+09, 's^-1'),
        n = 0,
        Ea = (79.7052, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R6H_SSSSS;O_rad_out;Cs_H_out_1H
""",
)

entry(
    index = 49,
    label = "C7H15O <=> C7H15O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.56e+09, 's^-1'),
        n = 0,
        Ea = (71.3372, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R6H_SSSSS;O_rad_out;Cs_H_out_noH
""",
)

entry(
    index = 50,
    label = "C6H13O-5 <=> C6H13O-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (5.85e+08, 's^-1'),
        n = 0,
        Ea = (106.901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R7H;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 51,
    label = "C7H15O-3 <=> C7H15O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.9e+08, 's^-1'),
        n = 0,
        Ea = (106.901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R7H;O_rad_out;Cs_H_out_1H
""",
)

entry(
    index = 52,
    label = "C8H17O <=> C8H17O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.95e+08, 's^-1'),
        n = 0,
        Ea = (106.901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R7H;O_rad_out;Cs_H_out_noH
""",
)

entry(
    index = 53,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.45e+09, 's^-1'),
        n = 1.12,
        Ea = (161.921, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_2H
""",
)

entry(
    index = 54,
    label = "C3H7-2 <=> C3H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.86e+09, 's^-1'),
        n = 1.32,
        Ea = (168.615, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 55,
    label = "C3H7 <=> C3H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (718000, 's^-1'),
        n = 2.05,
        Ea = (151.879, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""JWA CCSD(T)-F12/cc-pVTZ-F12 with 1d-HR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 56,
    label = "C4H9-4 <=> C4H9-5",
    degeneracy = 9.0,
    kinetics = Arrhenius(
        A = (7.308e+08, 's^-1'),
        n = 1.66,
        Ea = (169.87, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 57,
    label = "C4H9-5 <=> C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.04e+10, 's^-1'),
        n = 0.64,
        Ea = (141.838, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 58,
    label = "C6H13-5 <=> C6H13-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28e+10, 's^-1'),
        n = 0.97,
        Ea = (161.084, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 59,
    label = "C4H9-6 <=> C4H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.38e+09, 's^-1'),
        n = 0.88,
        Ea = (158.992, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 60,
    label = "C5H11-5 <=> C5H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.25e+10, 's^-1'),
        n = 0.6,
        Ea = (154.39, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 61,
    label = "C5H11-6 <=> C5H11-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.24e+09, 's^-1'),
        n = 1.19,
        Ea = (163.176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 62,
    label = "C3H5 <=> C3H5-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (7.32e+09, 's^-1'),
        n = 1.12,
        Ea = (172.799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;Cd_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 63,
    label = "C3H5-2 <=> C3H5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.36e+11, 's^-1'),
        n = 0.63,
        Ea = (260.245, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cd_H_out_doubleC
""",
)

entry(
    index = 64,
    label = "C5H7 <=> C5H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.448e+10, 's^-1'),
        n = 0.82,
        Ea = (156.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;Cd_rad_out;Cs_H_out_H/OneDe
""",
)

entry(
    index = 65,
    label = "C5H7-2 <=> C5H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.876e+11, 's^-1'),
        n = 0.71,
        Ea = (262.755, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/OneDe;Cd_H_out_doubleC
""",
)

entry(
    index = 66,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.06e+09, 's^-1'),
        n = 1.31,
        Ea = (263.174, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_OneDe/Cs;Cd_H_out_doubleC
""",
)

entry(
    index = 67,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6.18e+09, 's^-1'),
        n = 1.22,
        Ea = (199.995, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/OneDe;Cs_H_out_2H
""",
)

entry(
    index = 68,
    label = "C4H7-2 <=> C4H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.82e+08, 's^-1'),
        n = 1.28,
        Ea = (116.734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 69,
    label = "C5H9 <=> C5H9-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.9e+10, 's^-1'),
        n = 0.75,
        Ea = (190.79, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/OneDe;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 70,
    label = "C5H9-2 <=> C5H9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.682e+10, 's^-1'),
        n = 0.35,
        Ea = (125.102, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe
""",
)

entry(
    index = 71,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.01e+12, 's^-1'),
        n = 0.33,
        Ea = (176.983, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/OneDe;Cs_H_out_Cs2
""",
)

entry(
    index = 72,
    label = "C6H11-2 <=> C6H11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.94e+08, 's^-1'),
        n = 1.27,
        Ea = (125.938, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_H/OneDe
""",
)

entry(
    index = 73,
    label = "C5H9-3 <=> C5H9-4",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.614e+09, 's^-1'),
        n = 1.31,
        Ea = (203.342, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_2H
""",
)

entry(
    index = 74,
    label = "C6H11-3 <=> C6H11-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.26e+10, 's^-1'),
        n = 0.77,
        Ea = (192.464, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 75,
    label = "C7H13 <=> C7H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.62e+13, 's^-1'),
        n = -0.14,
        Ea = (184.096, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_Cs2
""",
)

entry(
    index = 76,
    label = "C2H3 <=> C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.28e+10, 's^-1'),
        n = 0.86,
        Ea = (191.209, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_D;Cd_rad_out_singleH;Cd_H_out_singleH
""",
)

entry(
    index = 77,
    label = "C3H5-3 <=> C3H5-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.24e+11, 's^-1'),
        n = 0.73,
        Ea = (177.402, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd
""",
)

entry(
    index = 78,
    label = "C3H5-4 <=> C3H5-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.24e+11, 's^-1'),
        n = 0.8,
        Ea = (198.74, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_D;Cd_rad_out_singleNd;Cd_H_out_singleH
""",
)

entry(
    index = 79,
    label = "C4H7-3 <=> C4H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.94e+11, 's^-1'),
        n = 0.69,
        Ea = (186.606, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_D;Cd_rad_out_singleNd;Cd_H_out_singleNd
""",
)

entry(
    index = 80,
    label = "C4H7-4 <=> C4H7-5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.374e+10, 's^-1'),
        n = 1.08,
        Ea = (169.034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_2H
""",
)

entry(
    index = 81,
    label = "C4H7-5 <=> C4H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.14e+10, 's^-1'),
        n = 0.81,
        Ea = (192.882, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 82,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.266e+11, 's^-1'),
        n = 0.65,
        Ea = (161.921, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 83,
    label = "C5H9-6 <=> C5H9-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.74e+09, 's^-1'),
        n = 0.98,
        Ea = (194.974, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 84,
    label = "C6H11-5 <=> C6H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.9e+11, 's^-1'),
        n = 0.36,
        Ea = (149.787, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_Cs2
""",
)

entry(
    index = 85,
    label = "C6H11-6 <=> C6H11-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.44e+08, 's^-1'),
        n = 1.39,
        Ea = (197.485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 86,
    label = "C5H9-7 <=> C5H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.75e+09, 's^-1'),
        n = 0.98,
        Ea = (153.134, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 87,
    label = "C5H9-8 <=> C5H9-7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.232e+09, 's^-1'),
        n = 1.2,
        Ea = (174.473, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_2H
""",
)

entry(
    index = 88,
    label = "C6H11-7 <=> C6H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.64e+09, 's^-1'),
        n = 1,
        Ea = (162.339, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 89,
    label = "C6H11-8 <=> C6H11-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.312e+10, 's^-1'),
        n = 0.81,
        Ea = (166.105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 90,
    label = "C7H13-3 <=> C7H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.31e+08, 's^-1'),
        n = 1.21,
        Ea = (162.758, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 91,
    label = "C7H13-4 <=> C7H13-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.86e+10, 's^-1'),
        n = 0.58,
        Ea = (159.829, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_Cs2
""",
)

entry(
    index = 92,
    label = "C6H11-9 <=> C6H11-10",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.21e+09, 's^-1'),
        n = 1.19,
        Ea = (179.075, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_2H
""",
)

entry(
    index = 93,
    label = "C6H11-10 <=> C6H11-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.35e+09, 's^-1'),
        n = 0.99,
        Ea = (141.001, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 94,
    label = "C7H13-5 <=> C7H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.29e+09, 's^-1'),
        n = 0.89,
        Ea = (152.298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 95,
    label = "C7H13-6 <=> C7H13-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.16e+10, 's^-1'),
        n = 0.81,
        Ea = (172.381, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 96,
    label = "C8H15 <=> C8H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.48e+07, 's^-1'),
        n = 1.45,
        Ea = (156.482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 97,
    label = "C8H15-2 <=> C8H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.24e+11, 's^-1'),
        n = 1.47,
        Ea = (166.523, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_Cs2
""",
)

entry(
    index = 98,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.25e+11, 's^-1'),
        n = 0.6,
        Ea = (184.096, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 99,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.72e+12, 's^-1'),
        n = 0.37,
        Ea = (174.054, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 100,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.69e+11, 's^-1'),
        n = 0.51,
        Ea = (181.167, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy3;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 101,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.56e+12, 's^-1'),
        n = 0.24,
        Ea = (163.176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 102,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.49e+10, 's^-1'),
        n = 0.79,
        Ea = (178.238, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 103,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.71e+11, 's^-1'),
        n = 0.61,
        Ea = (175.31, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 104,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.72e+12, 's^-1'),
        n = 0.26,
        Ea = (164.013, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 105,
    label = "C2H5 <=> C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.88e+11, 's^-1'),
        n = 0.51,
        Ea = (174.473, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 106,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.76e+08, 's^-1'),
        n = 1.17,
        Ea = (153.553, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_2H
""",
)

entry(
    index = 107,
    label = "C4H9 <=> C4H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.9e+09, 's^-1'),
        n = 0.82,
        Ea = (146.858, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 108,
    label = "C4H9-2 <=> C4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.19e+08, 's^-1'),
        n = 1.32,
        Ea = (161.502, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 109,
    label = "C5H11-7 <=> C5H11-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.5e+08, 's^-1'),
        n = 1.01,
        Ea = (152.298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 110,
    label = "C5H11-8 <=> C5H11-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.25e+10, 's^-1'),
        n = 0.66,
        Ea = (137.654, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 111,
    label = "C5H11-9 <=> C5H11-8",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.167e+07, 's^-1'),
        n = 1.77,
        Ea = (158.574, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 112,
    label = "C6H13-6 <=> C6H13-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.27e+09, 's^-1'),
        n = 0.66,
        Ea = (144.766, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 113,
    label = "C6H13-7 <=> C6H13-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.42e+07, 's^-1'),
        n = 1.41,
        Ea = (151.042, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 114,
    label = "C7H15 <=> C7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.78e+08, 's^-1'),
        n = 1,
        Ea = (147.695, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 115,
    label = "C3H5-5 <=> C3H5-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.53e+10, 's^-1'),
        n = 0.97,
        Ea = (157.737, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleH;Cs_H_out_2H
""",
)

entry(
    index = 116,
    label = "C3H5-6 <=> C3H5-5",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (19040, 's^-1'),
        n = 2.82,
        Ea = (238.906, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""calculated BMK/cbsb7 Aaron Vandeputte""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_2H;Cd_H_out_singleH
""",
)

entry(
    index = 117,
    label = "C4H7-6 <=> C4H7-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.846e+10, 's^-1'),
        n = 0.74,
        Ea = (145.185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleH;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 118,
    label = "C4H7-7 <=> C4H7-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.32e+10, 's^-1'),
        n = 0.77,
        Ea = (268.194, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_H/NonDeC;Cd_H_out_singleH
""",
)

entry(
    index = 119,
    label = "C5H9-9 <=> C5H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.04e+10, 's^-1'),
        n = 0.59,
        Ea = (135.98, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleH;Cs_H_out_Cs2
""",
)

entry(
    index = 120,
    label = "C5H9-10 <=> C5H9-9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.706e+09, 's^-1'),
        n = 1.27,
        Ea = (267.358, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_Cs2;Cd_H_out_singleH
""",
)

entry(
    index = 121,
    label = "C4H7-8 <=> C4H7-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.58e+09, 's^-1'),
        n = 1.08,
        Ea = (161.921, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleNd;Cs_H_out_2H
""",
)

entry(
    index = 122,
    label = "C4H7-9 <=> C4H7-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.91e+11, 's^-1'),
        n = 0.63,
        Ea = (255.224, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SD;C_rad_out_2H;Cd_H_out_singleNd
""",
)

entry(
    index = 123,
    label = "C5H9-11 <=> C5H9-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.182e+10, 's^-1'),
        n = 0.86,
        Ea = (149.369, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleNd;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 124,
    label = "C5H9-12 <=> C5H9-11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.92e+10, 's^-1'),
        n = 0.83,
        Ea = (257.734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_H/NonDeC;Cd_H_out_singleNd
""",
)

entry(
    index = 125,
    label = "C6H11-11 <=> C6H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.05e+09, 's^-1'),
        n = 0.86,
        Ea = (139.746, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleNd;Cs_H_out_Cs2
""",
)

entry(
    index = 126,
    label = "C6H11-12 <=> C6H11-11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.05e+10, 's^-1'),
        n = 0.79,
        Ea = (255.224, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_Cs2;Cd_H_out_singleNd
""",
)

entry(
    index = 127,
    label = "C4H7-10 <=> C4H7-11",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.304e+09, 's^-1'),
        n = 1.24,
        Ea = (151.879, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;Cd_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 128,
    label = "C4H7-11 <=> C4H7-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.24e+08, 's^-1'),
        n = 1.14,
        Ea = (172.799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cd_H_out_doubleC
""",
)

entry(
    index = 129,
    label = "C5H9-13 <=> C5H9-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.32e+09, 's^-1'),
        n = 0.99,
        Ea = (141.419, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;Cd_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 130,
    label = "C5H9-14 <=> C5H9-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.37e+07, 's^-1'),
        n = 1.41,
        Ea = (177.82, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cd_H_out_doubleC
""",
)

entry(
    index = 131,
    label = "C6H11-13 <=> C6H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+10, 's^-1'),
        n = 0.78,
        Ea = (132.633, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;Cd_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 132,
    label = "C6H11-14 <=> C6H11-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.5e+06, 's^-1'),
        n = 1.68,
        Ea = (176.983, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cd_H_out_doubleC
""",
)

entry(
    index = 133,
    label = "C4H7-12 <=> C4H7-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.93e+09, 's^-1'),
        n = 1.26,
        Ea = (221.334, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_2H
""",
)

entry(
    index = 134,
    label = "C5H9-15 <=> C5H9-16",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.68e+11, 's^-1'),
        n = 0.82,
        Ea = (205.853, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 135,
    label = "C5H9-16 <=> C5H9-15",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.692e+09, 's^-1'),
        n = 1.47,
        Ea = (223.007, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 136,
    label = "C6H11-15 <=> C6H11-16",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.86e+11, 's^-1'),
        n = 0.65,
        Ea = (198.74, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 137,
    label = "C6H11-16 <=> C6H11-15",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.136e+08, 's^-1'),
        n = 1.72,
        Ea = (216.731, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 138,
    label = "C6H11-17 <=> C6H11-17",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+10, 's^-1'),
        n = 0.91,
        Ea = (205.016, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 139,
    label = "C7H13-7 <=> C7H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.46e+10, 's^-1'),
        n = 0.76,
        Ea = (199.577, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 140,
    label = "C7H13-8 <=> C7H13-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.228e+11, 's^-1'),
        n = 0.8,
        Ea = (201.25, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 141,
    label = "C8H15-3 <=> C8H15-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.76e+09, 's^-1'),
        n = 1.18,
        Ea = (183.259, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 142,
    label = "C5H9-17 <=> C5H9-18",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.14e+10, 's^-1'),
        n = 0.99,
        Ea = (203.761, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/OneDe;Cs_H_out_2H
""",
)

entry(
    index = 143,
    label = "C5H9-18 <=> C5H9-17",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.32e+08, 's^-1'),
        n = 1.1,
        Ea = (123.01, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 144,
    label = "C6H11-18 <=> C6H11-19",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.354e+10, 's^-1'),
        n = 0.74,
        Ea = (192.882, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/OneDe;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 145,
    label = "C6H11-19 <=> C6H11-18",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.82e+09, 's^-1'),
        n = 0.73,
        Ea = (127.612, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe
""",
)

entry(
    index = 146,
    label = "C7H13-9 <=> C7H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.06e+10, 's^-1'),
        n = 0.44,
        Ea = (182.422, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/OneDe;Cs_H_out_Cs2
""",
)

entry(
    index = 147,
    label = "C7H13-10 <=> C7H13-9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.28e+07, 's^-1'),
        n = 1.56,
        Ea = (126.775, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_H/OneDe
""",
)

entry(
    index = 148,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.62e+10, 's^-1'),
        n = 0.69,
        Ea = (146.858, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 149,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.04e+10, 's^-1'),
        n = 0.71,
        Ea = (146.022, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 150,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.16e+11, 's^-1'),
        n = 0.26,
        Ea = (140.164, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 151,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.63e+08, 's^-1'),
        n = 1.01,
        Ea = (189.954, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 152,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.26e+13, 's^-1'),
        n = 0.26,
        Ea = (134.306, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 153,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.68e+07, 's^-1'),
        n = 1.42,
        Ea = (193.719, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 154,
    label = "C5H9-19 <=> C5H9-20",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (5.34e+09, 's^-1'),
        n = 1.04,
        Ea = (151.879, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_2H
""",
)

entry(
    index = 155,
    label = "C5H9-20 <=> C5H9-19",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.72e+09, 's^-1'),
        n = 0.78,
        Ea = (164.431, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 156,
    label = "C6H11-20 <=> C6H11-21",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.78e+09, 's^-1'),
        n = 0.77,
        Ea = (141.419, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 157,
    label = "C6H11-21 <=> C6H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.73e+08, 's^-1'),
        n = 1.14,
        Ea = (169.034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 158,
    label = "C7H13-11 <=> C7H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.08e+10, 's^-1'),
        n = 0.36,
        Ea = (133.051, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_Cs2
""",
)

entry(
    index = 159,
    label = "C7H13-12 <=> C7H13-11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.86e+06, 's^-1'),
        n = 1.65,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 160,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.9e+10, 's^-1'),
        n = 0.57,
        Ea = (166.523, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 161,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.43e+09, 's^-1'),
        n = 0.93,
        Ea = (160.247, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 162,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.9e+11, 's^-1'),
        n = 0.27,
        Ea = (158.574, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 163,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.59e+08, 's^-1'),
        n = 1.2,
        Ea = (166.105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 164,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.63e+12, 's^-1'),
        n = -0.04,
        Ea = (154.808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 165,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.19e+07, 's^-1'),
        n = 1.55,
        Ea = (167.778, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 166,
    label = "C6H11-22 <=> C6H11-23",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.24e+08, 's^-1'),
        n = 1.25,
        Ea = (165.686, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_2H
""",
)

entry(
    index = 167,
    label = "C6H11-23 <=> C6H11-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.09e+09, 's^-1'),
        n = 0.84,
        Ea = (144.348, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 168,
    label = "C7H13-13 <=> C7H13-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.1e+08, 's^-1'),
        n = 0.99,
        Ea = (156.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 169,
    label = "C7H13-14 <=> C7H13-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.69e+08, 's^-1'),
        n = 0.97,
        Ea = (150.206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 170,
    label = "C8H15-4 <=> C8H15-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.2e+09, 's^-1'),
        n = 0.54,
        Ea = (148.532, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_Cs2
""",
)

entry(
    index = 171,
    label = "C8H15-5 <=> C8H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.49e+07, 's^-1'),
        n = 1.38,
        Ea = (148.114, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 172,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.85e+10, 's^-1'),
        n = 0.6,
        Ea = (170.707, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 173,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+09, 's^-1'),
        n = 0.99,
        Ea = (145.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 174,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.67e+11, 's^-1'),
        n = 0.29,
        Ea = (159.829, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 175,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.42e+08, 's^-1'),
        n = 1.14,
        Ea = (150.624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 176,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.42e+11, 's^-1'),
        n = 0.12,
        Ea = (156.482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 177,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.58e+06, 's^-1'),
        n = 1.78,
        Ea = (166.105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 178,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (9.42e+08, 's^-1'),
        n = 1.26,
        Ea = (171.962, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_2H
""",
)

entry(
    index = 179,
    label = "C7H13-16 <=> C7H13-15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.9e+09, 's^-1'),
        n = 0.82,
        Ea = (137.654, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 180,
    label = "C8H15-6 <=> C8H15-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.5e+08, 's^-1'),
        n = 1.01,
        Ea = (163.594, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 181,
    label = "C8H15-7 <=> C8H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.5e+08, 's^-1'),
        n = 0.9,
        Ea = (143.093, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 182,
    label = "C9H17 <=> C9H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.97e+10, 's^-1'),
        n = 0.46,
        Ea = (156.063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_Cs2
""",
)

entry(
    index = 183,
    label = "C9H17-2 <=> C9H17",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.21e+08, 's^-1'),
        n = 1.04,
        Ea = (143.093, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 184,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.64e+09, 's^-1'),
        n = 0.84,
        Ea = (27.196, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 185,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.02e+10, 's^-1'),
        n = 0.56,
        Ea = (178.657, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 186,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.22e+11, 's^-1'),
        n = 0.4,
        Ea = (145.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 187,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.34e+09, 's^-1'),
        n = 0.81,
        Ea = (182.422, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 188,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.72e+12, 's^-1'),
        n = -0.04,
        Ea = (139.746, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 189,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.61e+08, 's^-1'),
        n = 1.26,
        Ea = (175.728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 190,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.78e+11, 's^-1'),
        n = 0.29,
        Ea = (227.191, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 191,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.48e+10, 's^-1'),
        n = 0.6,
        Ea = (228.446, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 192,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.66e+12, 's^-1'),
        n = 0,
        Ea = (215.058, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 193,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.55e+11, 's^-1'),
        n = 0.37,
        Ea = (216.313, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy4;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 194,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.36e+11, 's^-1'),
        n = 0.46,
        Ea = (197.485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 195,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.72e+09, 's^-1'),
        n = 0.86,
        Ea = (197.485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 196,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+12, 's^-1'),
        n = 0.23,
        Ea = (185.77, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 197,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.07e+10, 's^-1'),
        n = 0.62,
        Ea = (181.586, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy5;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 198,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.84e+09, 's^-1'),
        n = 1.05,
        Ea = (171.962, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 199,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.51e+09, 's^-1'),
        n = 0.86,
        Ea = (140.164, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 200,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.04e+09, 's^-1'),
        n = 0.74,
        Ea = (162.339, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 201,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.95e+09, 's^-1'),
        n = 0.88,
        Ea = (146.858, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 202,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.44e+10, 's^-1'),
        n = 0.74,
        Ea = (156.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 203,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.85e+07, 's^-1'),
        n = 1.46,
        Ea = (152.298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 204,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.28e+08, 's^-1'),
        n = 1.07,
        Ea = (170.289, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 205,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.93e+10, 's^-1'),
        n = 0.75,
        Ea = (152.716, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 206,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.41e+09, 's^-1'),
        n = 0.77,
        Ea = (162.339, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 207,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.96e+09, 's^-1'),
        n = 0.96,
        Ea = (160.666, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 208,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.37e+10, 's^-1'),
        n = 0.62,
        Ea = (157.318, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 209,
    label = "C3H7-3 <=> C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.96e+07, 's^-1'),
        n = 1.46,
        Ea = (164.85, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Taken from entry: Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 210,
    label = "CH3O2 <=> CH3O2-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.71e+08, 's^-1'),
        n = 1.45,
        Ea = (176.858, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Taken from entry: CH3OO to CH2OOH, degeneracy=3, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 211,
    label = "C2H5O2 <=> C2H5O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.66e+08, 's^-1'),
        n = 1.28,
        Ea = (166.272, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Taken from entry: CH3CH2OO to CH3CHOOH, degeneracy=2, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 212,
    label = "C3H7O2 <=> C3H7O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.44e+09, 's^-1'),
        n = 1.17,
        Ea = (165.937, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Taken from entry: CH3CH2CH2OO to CH3CH2CHOOH, degeneracy=2, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 213,
    label = "C4H9O2 <=> C4H9O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.07e+10, 's^-1'),
        n = 0.98,
        Ea = (165.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Taken from entry: (CH3)2CHCH2OO to (CH3)2CHCHOOH, degeneracy=2, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/(NonDeC/Cs/Cs)
""",
)

entry(
    index = 214,
    label = "C5H11O2 <=> C5H11O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.62e+09, 's^-1'),
        n = 1.04,
        Ea = (164.599, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Taken from entry: (CH3)3CCH2OO to (CH3)3CCHOOH, degeneracy=2, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/(NonDeC/Cs/Cs/Cs)
""",
)

entry(
    index = 215,
    label = "C3H7O2-3 <=> C3H7O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.97e+09, 's^-1'),
        n = 1.01,
        Ea = (160.958, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Taken from entry: (CH3)2CHOO to (CH3)2COOH, degeneracy=1, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 216,
    label = "C2H5O2-3 <=> C2H5O2-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.989e+11, 's^-1'),
        n = 0.15,
        Ea = (143.135, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Taken from entry: CH3CH2OO to CH2CH2OOH, degeneracy=3, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 217,
    label = "C3H7O2-5 <=> C3H7O2-6",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (6.36e+08, 's^-1'),
        n = 1.06,
        Ea = (140.206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Taken from entry: (CH3)2CHOO to CH3(CH2)CHOOH, degeneracy=6, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 218,
    label = "C4H9O2-3 <=> C4H9O2-4",
    degeneracy = 9.0,
    kinetics = Arrhenius(
        A = (5.058e+08, 's^-1'),
        n = 1.2,
        Ea = (140.29, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Taken from entry: (CH3)3COO to (CH3)2(CH2)COOH, degeneracy=9, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R4H_SSS_O(Cs)CsCs;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 219,
    label = "C3H7O2-7 <=> C3H7O2-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4e+08, 's^-1'),
        n = 1.1,
        Ea = (125.897, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 220,
    label = "C4H9O2-5 <=> C4H9O2-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.962e+09, 's^-1'),
        n = 0.88,
        Ea = (123.344, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 221,
    label = "C5H11O2-3 <=> C5H11O2-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.06e+09, 's^-1'),
        n = 0.69,
        Ea = (125.98, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_O(Cs)CsCs;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 222,
    label = "C4H9O2-7 <=> C4H9O2-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.64e+09, 's^-1'),
        n = 0.78,
        Ea = (113.428, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 223,
    label = "C5H11O2-5 <=> C5H11O2-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.25e+09, 's^-1'),
        n = 0.57,
        Ea = (114.265, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 224,
    label = "C6H13O2 <=> C6H13O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.87e+10, 's^-1'),
        n = 0.35,
        Ea = (110.416, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_O(Cs)CsCs;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 225,
    label = "C3H7O2-9 <=> C3H7O2-10",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (5.07e+06, 's^-1'),
        n = 1.55,
        Ea = (87.9477, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 226,
    label = "C4H9O2-9 <=> C4H9O2-10",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.034e+07, 's^-1'),
        n = 1.35,
        Ea = (87.1946, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 227,
    label = "C5H11O2-7 <=> C5H11O2-8",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.305e+08, 's^-1'),
        n = 1.12,
        Ea = (91.5459, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC_CC;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 228,
    label = "C4H9O2-11 <=> C4H9O2-12",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (8.46e+07, 's^-1'),
        n = 1.32,
        Ea = (89.956, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCs(Cs/Cs);O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 229,
    label = "C5H11O2-9 <=> C5H11O2-10",
    degeneracy = 9.0,
    kinetics = Arrhenius(
        A = (9.81e+08, 's^-1'),
        n = 1.23,
        Ea = (90.4581, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCs(Cs/Cs/Cs);O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 230,
    label = "C4H9O2-13 <=> C4H9O2-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.788e+07, 's^-1'),
        n = 1.26,
        Ea = (76.0233, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 231,
    label = "C5H11O2-11 <=> C5H11O2-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.76e+10, 's^-1'),
        n = 0.21,
        Ea = (77.404, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 232,
    label = "C5H11O2-13 <=> C5H11O2-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.174e+08, 's^-1'),
        n = 1.15,
        Ea = (64.3081, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 233,
    label = "C4H9O2-15 <=> C4H9O2-16",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.107e+06, 's^-1'),
        n = 1.52,
        Ea = (83.8892, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 234,
    label = "C5H11O2-15 <=> C5H11O2-16",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.24e+06, 's^-1'),
        n = 1.22,
        Ea = (69.4544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. 
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 235,
    label = "C6H13O2-3 <=> C6H13O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.48e+06, 's^-1'),
        n = 1.22,
        Ea = (57.9066, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 236,
    label = "C5H11O2-17 <=> C5H11O2-18",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (271800, 's^-1'),
        n = 1.51,
        Ea = (83.4708, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 237,
    label = "C6H13O2-5 <=> C6H13O2-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.74e+06, 's^-1'),
        n = 0.99,
        Ea = (76.0233, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. 
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 238,
    label = "C7H15O2 <=> C7H15O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (562000, 's^-1'),
        n = 1.09,
        Ea = (59.7475, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 239,
    label = "CH3O3 <=> CH3O3-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6e+08, 's^-1'),
        n = 1.23,
        Ea = (154.18, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 240,
    label = "C2H5O3 <=> C2H5O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3e+08, 's^-1'),
        n = 1.23,
        Ea = (154.18, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 241,
    label = "C2H5O3-3 <=> C2H5O3-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.22e+08, 's^-1'),
        n = 1.09,
        Ea = (109.37, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 242,
    label = "C3H7O3 <=> C3H7O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.29e+09, 's^-1'),
        n = 0.75,
        Ea = (103.847, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 243,
    label = "C3H7O3-3 <=> C3H7O3-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.84e+09, 's^-1'),
        n = 0.82,
        Ea = (109.956, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 244,
    label = "C4H9O3 <=> C4H9O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.18e+11, 's^-1'),
        n = 0.51,
        Ea = (109.621, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 245,
    label = "C3H7O3-5 <=> C3H7O3-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (23000, 's^-1'),
        n = 2.11,
        Ea = (64.7265, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 246,
    label = "C4H9O3-3 <=> C4H9O3-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.9e+07, 's^-1'),
        n = 1.1,
        Ea = (64.4336, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 247,
    label = "C4H9O3-5 <=> C4H9O3-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.58e+08, 's^-1'),
        n = 1.12,
        Ea = (64.3499, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 248,
    label = "C5H11O3 <=> C5H11O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.17e+11, 's^-1'),
        n = 0.43,
        Ea = (64.4336, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 249,
    label = "C4H9O3-7 <=> C4H9O3-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1098, 's^-1'),
        n = 2.21,
        Ea = (60.1659, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 250,
    label = "C5H11O3-3 <=> C5H11O3-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (72300, 's^-1'),
        n = 1.65,
        Ea = (50.2917, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 251,
    label = "C5H11O3-5 <=> C5H11O3-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.866e+06, 's^-1'),
        n = 0.75,
        Ea = (53.6389, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 252,
    label = "C6H13O3 <=> C6H13O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.41e+06, 's^-1'),
        n = 1.09,
        Ea = (52.3, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 253,
    label = "C5H7-3 <=> C5H7-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.64e+06, 's^-1'),
        n = 1.6229,
        Ea = (184.393, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R4H_SDS;C_rad_out_2H;Cd_H_out_doubleC
""",
)

entry(
    index = 254,
    label = "C5H7-4 <=> C5H7-3",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.33e+08, 's^-1'),
        n = 1.1915,
        Ea = (103.605, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R4H_SDS;Cd_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 255,
    label = "C5H7-5 <=> C5H7-6",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (876000, 's^-1'),
        n = 1.7613,
        Ea = (160.143, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R5H_SMSD;C_rad_out_2H;Cd_H_out_singleH
""",
)

entry(
    index = 256,
    label = "C5H7-7 <=> C5H7-5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (408000, 's^-1'),
        n = 1.9199,
        Ea = (33.0402, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R5H_DSMS;Cd_rad_out_singleH;Cs_H_out_2H
""",
)

entry(
    index = 257,
    label = "C5H7-8 <=> C5H7-9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.18e+07, 's^-1'),
        n = 1.4638,
        Ea = (277.467, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R3H_SD;C_rad_out_2H;Cd_H_out_singleDe
""",
)

entry(
    index = 258,
    label = "C5H7-9 <=> C5H7-8",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.85113e+09, 's^-1'),
        n = 1.0541,
        Ea = (193.078, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Taken from entry: Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleDe;Cs_H_out_2H
""",
)

entry(
    index = 259,
    label = "C4H7O <=> C4H7O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.22e+06, 's^-1', '*|/', 3),
        n = 1.78,
        Ea = (113.721, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 calculations.""",
    longDesc = 
u"""
Taken from entry: MHS CBS-QB3 calculations for CH3-CH2-CH=CH-O* == CH3-C*H-CH=CH-OH.  
Product is the cis configuration because TS is also cis.  
Note--this only affects the tunneling correction (b/c in products).  
Only methyl rotor was considered for TS.

Converted to training reaction from rate rule: R4H_SDS;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 260,
    label = "C4H7O-3 <=> C4H7O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.468e+06, 's^-1', '*|/', 3),
        n = 1.554,
        Ea = (111.445, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/1d h.r. corrections""",
    longDesc = 
u"""
Taken from entry: MRH CBS-QB3 calculations with 1-d hindered rotor corrections for CH2=CH-CH2-OO => CH=CH-CH2-OOH

Previous RMG estimate for this reaction was an "Average of average" estimate.  This reaction was of
interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => C2H2+CH2O+OH.  The high-p
limit kinetics were necessary to estimate a k(T,P) for this PES.

Reactant: 2 hindered rotors were considered (the OO and CH2OO torsions)
TS: 0 hindered rotors were considered (MRH did not think 1-d separable rotor approximation was valid
	for cyclic TS)
Product: 3 hindered rotors were considered (the HO, HOO, and HOOCH2 torsions)

All external symmetry numbers were set equal to one.  The k(T) was calculated from 600 - 2000 K,
in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.468e+06 * (T/1K)^1.554 * exp(-26.636 kcal/mol / RT) cm3/mol/s.
The number appearing in the database has been divided by two to account for the reaction path degeneracy.

Converted to training reaction from rate rule: R5H_SSSD;O_rad_out;Cd_H_out_singleH
""",
)

entry(
    index = 261,
    label = "C2H5O4 <=> C2H5O4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.47e+12, 's^-1'),
        n = -0.24,
        Ea = (117.152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 262,
    label = "C3H7O4 <=> C3H7O4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.76e+08, 's^-1'),
        n = 1.2,
        Ea = (107.529, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 263,
    label = "C3H7O4-3 <=> C3H7O4-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.44e+07, 's^-1'),
        n = 1.6,
        Ea = (116.734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 264,
    label = "C4H9O4 <=> C4H9O4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.75e+08, 's^-1'),
        n = 1.7,
        Ea = (108.784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 265,
    label = "C3H7O4-5 <=> C3H7O4-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (25900, 's^-1'),
        n = 1.9,
        Ea = (78.6592, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 266,
    label = "C4H9O4-3 <=> C4H9O4-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (10980, 's^-1'),
        n = 2.4,
        Ea = (83.2616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 267,
    label = "C5H11O4 <=> C5H11O4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.5, 's^-1'),
        n = 3.6,
        Ea = (74.0568, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS_OCs(Cs/Cs/Cs);O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 268,
    label = "C4H9O4-5 <=> C4H9O4-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (57.9, 's^-1'),
        n = 2.9,
        Ea = (71.128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 269,
    label = "C5H11O4-3 <=> C5H11O4-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (175, 's^-1'),
        n = 3.1,
        Ea = (73.22, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 270,
    label = "C4H9O4-7 <=> C4H9O4-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2380, 's^-1'),
        n = 1.7,
        Ea = (69.4544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 271,
    label = "C5H11O4-5 <=> C5H11O4-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1256, 's^-1'),
        n = 2.2,
        Ea = (72.8016, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6H_SSSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 272,
    label = "C5H11O-7 <=> C5H11O-8",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1131, 's^-1'),
        n = 2.2,
        Ea = (64.0152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6H_SSSSS_OOCCC(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 273,
    label = "C6H13O-7 <=> C6H13O-8",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (762, 's^-1'),
        n = 2.6,
        Ea = (67.7808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 274,
    label = "C5H11O4-7 <=> C5H11O4-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (557, 's^-1'),
        n = 1.8,
        Ea = (69.4544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 275,
    label = "C6H13O-9 <=> C6H13O-10",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6000, 's^-1'),
        n = 1.9,
        Ea = (62.3416, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R7H_OOCCCC(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 276,
    label = "C4H9O-3 <=> C4H9O-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.2e+11, 's^-1'),
        n = 0,
        Ea = (31.8402, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of primary H (per H atom)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_CCC;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 277,
    label = "C5H11O-3 <=> C5H11O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8e+10, 's^-1'),
        n = 0,
        Ea = (25.7316, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of secondary H (per H atom)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_CCC;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 278,
    label = "C4H9O-3 <=> C4H9O-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.2e+11, 's^-1'),
        n = 0,
        Ea = (21.3384, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of tertiary H""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_CCC;O_rad_out;Cs_H_out
""",
)

entry(
    index = 279,
    label = "CH3S <=> CH3S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0722, 's^-1'),
        n = 4.07,
        Ea = (87.4456, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 280,
    label = "C2H5S <=> C2H5S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (85.5, 's^-1'),
        n = 3.04,
        Ea = (48.6181, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3H_SS_Cs;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 281,
    label = "CH3S2 <=> CH3S2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.000821, 's^-1'),
        n = 4.56,
        Ea = (67.1532, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3H_SS_S;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 282,
    label = "C3H7S <=> C3H7S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.73e+08, 's^-1'),
        n = 0.882,
        Ea = (22.3844, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 283,
    label = "C4H9S <=> C4H9S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.21e+10, 's^-1'),
        n = 0.214,
        Ea = (12.3846, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 284,
    label = "C5H11S <=> C5H11S-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00228, 's^-1'),
        n = 3.95,
        Ea = (46.7353, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_CsS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 285,
    label = "C6H13S <=> C6H13S-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0564, 's^-1'),
        n = 3.28,
        Ea = (24.7274, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_SSSS_CsCsS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 286,
    label = "C5H11S-3 <=> C5H11S-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.58e-05, 's^-1'),
        n = 4.5,
        Ea = (49.9151, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeS
""",
)

entry(
    index = 287,
    label = "C6H13S-3 <=> C6H13S-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.1016, 's^-1'),
        n = 3.24,
        Ea = (29.037, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeS
""",
)

entry(
    index = 288,
    label = "CH3OS <=> CH3OS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.99e+11, 's^-1'),
        n = 0.26,
        Ea = (66.9022, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3H_SS;O_rad_out;S_H_out
""",
)

entry(
    index = 289,
    label = "C3H7O-3 <=> C3H7O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.71, 's^-1'),
        n = 3.021,
        Ea = (105.562, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;O_H_out
""",
)

entry(
    index = 290,
    label = "C4H7S <=> C4H7S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.61e+11, 's^-1'),
        n = 0.22,
        Ea = (88.2824, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1550, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc, HO approx""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SDS;C_rad_out_H/NonDeC;S_H_out
""",
)

entry(
    index = 291,
    label = "C4H9O-5 <=> C4H9O-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (83700, 's^-1'),
        n = 1.97,
        Ea = (96.6504, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_H/NonDeO;Cs_H_out_2H
""",
)

entry(
    index = 292,
    label = "C2H5O <=> C2H5O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4500, 's^-1'),
        n = 2.62,
        Ea = (129.286, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;O_H_out
""",
)

entry(
    index = 293,
    label = "C4H9O-2 <=> C4H9O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2960, 's^-1'),
        n = 2.11,
        Ea = (84.0984, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_H/NonDeC;O_H_out
""",
)

entry(
    index = 294,
    label = "C4H9O-6 <=> C4H9O-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (304, 's^-1'),
        n = 2.77,
        Ea = (62.3834, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_2H;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 295,
    label = "C3H7O-5 <=> C3H7O-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (153000, 's^-1'),
        n = 2.26,
        Ea = (88.9937, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2H_S;O_rad_out;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 296,
    label = "C4H9O <=> C4H9O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (210000, 's^-1'),
        n = 1.76,
        Ea = (53.8899, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 297,
    label = "C4H9O-7 <=> C4H9O-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (18000, 's^-1'),
        n = 2.287,
        Ea = (84.6842, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Obtained by reversing rate rule 1006""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3H_SS;O_rad_out;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 298,
    label = "C4H9-7 <=> C4H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (150000, 's^-1'),
        n = 2.15,
        Ea = (135.478, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Obtained by reversing rate rule 1010""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 299,
    label = "C6H11-24 <=> C6H11-25",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000226, 's^-1'),
        n = 4.37,
        Ea = (33.723, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 300,
    label = "C7H13-17 <=> C7H13-18",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (92.2, 's^-1'),
        n = 3.21,
        Ea = (27.3215, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 301,
    label = "C7H11 <=> C7H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4800, 's^-1'),
        n = 2.15,
        Ea = (92.4664, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 1D-HR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5H_SMSS;C_rad_out_2H;Cs_H_out_H/Cd
""",
)

entry(
    index = 302,
    label = "C7H13-19 <=> C7H13-20",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.502, 's^-1'),
        n = 3.86,
        Ea = (41.6308, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe
""",
)

entry(
    index = 303,
    label = "C8H15-8 <=> C8H15-9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (92.2, 's^-1'),
        n = 3.21,
        Ea = (27.3215, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6H_SSSSS;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 304,
    label = "C6H13-8 <=> C6H13-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (10500, 's^-1'),
        n = 2.14,
        Ea = (66.8185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R6H_SSSSS_bicyclopentane;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe
""",
)

entry(
    index = 305,
    label = "C4H7-13 <=> C4H7-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (418.4, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""estimate""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SMS;Y_rad_out;XH_out
""",
)

entry(
    index = 306,
    label = "C7H13-21 <=> C7H13-22",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2e+10, 's^-1'),
        n = 0,
        Ea = (418.4, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""estimate""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SDS;C_rad_out_H/NonDeC;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 307,
    label = "C6H13-8 <=> C6H13-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.28e+11, 's^-1'),
        n = -1.05,
        Ea = (49.2038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R6H_SSSSS;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 308,
    label = "C7H15-2 <=> C7H15-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.36e+10, 's^-1'),
        n = -0.66,
        Ea = (59.7475, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R6H_SSSSS;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 309,
    label = "C3H5O2 <=> C3H5O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.32e+07, 's^-1'),
        n = 1.69,
        Ea = (159.41, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/Cd
""",
)

entry(
    index = 310,
    label = "C3H5O2-3 <=> C3H5O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (274, 's^-1'),
        n = 3.09,
        Ea = (145.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cd_H_out_doubleC
""",
)

entry(
    index = 311,
    label = "C3H7O-7 <=> C3H7O-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.4e-16, 's^-1'),
        n = 7.98,
        Ea = (104.6, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/(NonDeC/O)
""",
)

entry(
    index = 312,
    label = "C3H7O-9 <=> C3H7O-10",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.3e-15, 's^-1'),
        n = 8.11,
        Ea = (117.152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 313,
    label = "C3H7O-2 <=> C3H7O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.6e-09, 's^-1'),
        n = 5.55,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_2H;O_H_out
""",
)

entry(
    index = 314,
    label = "C3H7O-11 <=> C3H7O-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.4e-20, 's^-1'),
        n = 9.13,
        Ea = (108.784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 315,
    label = "C3H7O-12 <=> C3H7O-11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.4e-19, 's^-1'),
        n = 8.84,
        Ea = (125.52, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeO;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 316,
    label = "C3H7O-10 <=> C3H7O-9",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6e-15, 's^-1'),
        n = 8.23,
        Ea = (142.674, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeO;Cs_H_out_2H
""",
)

entry(
    index = 317,
    label = "C4H9O-9 <=> C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7e-08, 's^-1'),
        n = 6.3,
        Ea = (82.634, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3H_SS;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 318,
    label = "CH3O <=> CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (25600, 's^-1'),
        n = 2.36,
        Ea = (138.49, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Aaron BMK/cbsb7 with 1-dHR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;O_H_out
""",
)

entry(
    index = 319,
    label = "C2H5O-3 <=> C2H5O-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.41e+13, 's^-1', '+|-', 2),
        n = 0,
        Ea = (188.28, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""
Taken from entry: RQCISD(T)/CBS TST calculations with Eckart and 1-dHR corrections from Enoch for 
alpha-hydroxyethyl surface, reference: doi 10.1002/kin.20844

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeO;Cs_H_out_2H
""",
)

entry(
    index = 320,
    label = "C2H5O-4 <=> C2H5O-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.7e+13, 's^-1', '+|-', 2),
        n = -0.1,
        Ea = (158.364, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1800, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""
Taken from entry: RQCISD(T)/CBS TST calculations with Eckart and 1-dHR corrections from Enoch for 
alpha-hydroxyethyl surface, reference: doi 10.1002/kin.20844

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 321,
    label = "C2H5O-2 <=> C2H5O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.3e+14, 's^-1', '+|-', 2),
        n = -0.27,
        Ea = (113.972, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1800, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""
Taken from entry: RQCISD(T)/CBS TST calculations with Eckart and 1-dHR corrections from Enoch for 
alpha-hydroxyethyl surface, reference: doi 10.1002/kin.20844

Converted to training reaction from rate rule: R2H_S;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 322,
    label = "C7H11-3 <=> C7H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.52e+08, 's^-1'),
        n = 1.11,
        Ea = (87.4456, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2d,d,p)""",
    longDesc = 
u"""
Taken from entry: BMK/6-311G(2d,d,p) TST Eckart, no HR. calculated for cycC5H5-CH2 -> cycC5H4-CH3

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_CdCd
""",
)

entry(
    index = 323,
    label = "C4H9-3 <=> C4H9-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e-10, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""Aaron Vandeputte guess""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_MMS;Cd_rad_out;Cs_H_out
""",
)

entry(
    index = 324,
    label = "C4H5 <=> C4H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e-10, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""Aaron Vandeputte guess""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_D;Cd_rad_out_singleH;Cd_H_out_singleDe
""",
)

