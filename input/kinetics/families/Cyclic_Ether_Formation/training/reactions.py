#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C3H5O2 <=> C3H4O + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (7.96e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;C_pri_rad_intra;OOH
""",
)

entry(
    index = 1,
    label = "C4H7O2 <=> C3H4O + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (7.96e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;C_pri_rad_intra;OOR
""",
)

entry(
    index = 2,
    label = "C4H7O2-2 <=> C4H6O + OH",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.38e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;C_sec_rad_intra;OOH
""",
)

entry(
    index = 3,
    label = "C5H9O2 <=> C4H6O + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.38e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;C_sec_rad_intra;OOR
""",
)

entry(
    index = 4,
    label = "C6H11O2 <=> C5H8O + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.09e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;C_ter_rad_intra;OOR
""",
)

entry(
    index = 5,
    label = "C5H9O2-2 <=> C5H8O + OH",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.09e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;C_ter_rad_intra;OOH
""",
)

entry(
    index = 6,
    label = "C5H7O2 <=> C5H6O + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (8.94e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SS;C_pri_rad_intra;OOH
""",
)

entry(
    index = 7,
    label = "C6H9O2 <=> C5H6O + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (8.94e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SS;C_pri_rad_intra;OOR
""",
)

entry(
    index = 8,
    label = "C6H9O2-2 <=> C6H8O + OH",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.04e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SS;C_sec_rad_intra;OOH
""",
)

entry(
    index = 9,
    label = "C7H11O2 <=> C6H8O + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.04e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SS;C_sec_rad_intra;OOR
""",
)

entry(
    index = 10,
    label = "C8H13O2 <=> C7H10O + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.31e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SS;C_ter_rad_intra;OOR
""",
)

entry(
    index = 11,
    label = "C7H11O2-2 <=> C7H10O + OH",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.31e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SS;C_ter_rad_intra;OOH
""",
)

entry(
    index = 12,
    label = "C8H11O2 <=> C7H8O + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.026e+11, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (14.8, 'kcal/mol', '+|-', 2),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSS;C_pri_rad_intra;OOR
""",
)

entry(
    index = 13,
    label = "C7H9O2 <=> C7H8O + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.026e+11, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (14.8, 'kcal/mol', '+|-', 2),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSS;C_pri_rad_intra;OOH
""",
)

entry(
    index = 14,
    label = "C9H13O2 <=> C8H10O + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.63e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (13, 'kcal/mol', '+|-', 2.5),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSS;C_sec_rad_intra;OOR
""",
)

entry(
    index = 15,
    label = "C8H11O2-2 <=> C8H10O + OH",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.63e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (13, 'kcal/mol', '+|-', 2.5),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSS;C_sec_rad_intra;OOH
""",
)

entry(
    index = 16,
    label = "C10H15O2 <=> C9H12O + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.57e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (11.5, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSS;C_ter_rad_intra;OOR
""",
)

entry(
    index = 17,
    label = "C9H13O2-2 <=> C9H12O + OH",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.57e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (11.5, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSS;C_ter_rad_intra;OOH
""",
)

entry(
    index = 18,
    label = "C4H7O2 <=> C3H4O + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.2e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;Cs_rad_intra;OOR
""",
)

entry(
    index = 19,
    label = "C3H5O2 <=> C3H4O + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.2e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;Cs_rad_intra;OOH
""",
)

entry(
    index = 20,
    label = "C6H9O2 <=> C5H6O + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.5e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SS;Cs_rad_intra;OOR
""",
)

entry(
    index = 21,
    label = "C5H7O2 <=> C5H6O + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.5e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SS;Cs_rad_intra;OOH
""",
)

entry(
    index = 22,
    label = "C8H11O2 <=> C7H8O + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.876e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSS;Cs_rad_intra;OOR
""",
)

entry(
    index = 23,
    label = "C7H9O2 <=> C7H8O + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.876e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSS;Cs_rad_intra;OOH
""",
)

entry(
    index = 24,
    label = "C9H11O2 <=> C9H10O + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.34e+09, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5OO_SSSS;Cs_rad_intra;OOH
""",
)

entry(
    index = 25,
    label = "C10H13O2 <=> C9H10O + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.34e+09, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5OO_SSSS;Cs_rad_intra;OOR
""",
)

entry(
    index = 26,
    label = "C9H11O3 <=> C8H8O2 + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment of hindered rotor (SSM)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5OO_SSSSCO;Cs_rad_intra;OOR
""",
)

entry(
    index = 27,
    label = "C8H9O3 <=> C8H8O2 + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment of hindered rotor (SSM)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5OO_SSSSCO;Cs_rad_intra;OOH
""",
)

entry(
    index = 28,
    label = "C3H5O3 <=> C2H2O2 + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (6.92e+15, 's^-1'),
        n = -0.53,
        alpha = 0,
        E0 = (24.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment for hindered rotor, QTST Calculation (CFG & JWA)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_SCO;Cs_rad_intra;OOR
""",
)

entry(
    index = 29,
    label = "C2H3O3 <=> C2H2O2 + OH",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (6.92e+15, 's^-1'),
        n = -0.53,
        alpha = 0,
        E0 = (24.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment for hindered rotor, QTST Calculation (CFG & JWA)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_SCO;Cs_rad_intra;OOH
""",
)

entry(
    index = 30,
    label = "C7H9O3 <=> C6H6O2 + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSSCO;Cs_rad_intra;OOR
""",
)

entry(
    index = 31,
    label = "C6H7O3 <=> C6H6O2 + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OO_SSSCO;Cs_rad_intra;OOH
""",
)

entry(
    index = 32,
    label = "C4H5O3 <=> C4H4O2 + OH",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SSCO;Cs_rad_intra;OOH
""",
)

entry(
    index = 33,
    label = "C5H7O3 <=> C4H4O2 + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OO_SSCO;Cs_rad_intra;OOR
""",
)

entry(
    index = 34,
    label = "C3H4O2 <=> C3H4O + O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (3.24e+09, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (31.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;C_pri_rad_intra;OOJ
""",
)

entry(
    index = 35,
    label = "C4H6O2 <=> C4H6O + O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.27e+09, 's^-1'),
        n = 1.06,
        alpha = 0,
        E0 = (31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OO_S;C_rad/H/NonDeC_intra;OOJ
""",
)

