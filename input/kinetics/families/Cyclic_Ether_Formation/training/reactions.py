#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C2H3O3 <=> C2H2O2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.9e+17, 's^-1', '*|/', 2.51189),
        n = -1.1,
        Ea = (27.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['J. W. Allen', 'C. F. Goldsmith', 'W. H. Green'],
        title = 'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '???',
        pages = '???-???',
        year = '2011 (accepted)',
    ),
    referenceType = "theory",
    rank = 10,
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
    label = "C3H5O2 <=> C3H4O + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.96e+12, 's^-1', '*|/', 1.2),
        n = 0,
        Ea = (45.6433, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;C_pri_rad_intra;OOH
""",
)

entry(
    index = 2,
    label = "C4H7O2 <=> C3H4O + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.96e+12, 's^-1', '*|/', 1.2),
        n = 0,
        Ea = (63.953, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;C_pri_rad_intra;OOR
""",
)

entry(
    index = 3,
    label = "C4H7O2-2 <=> C4H6O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38e+12, 's^-1', '*|/', 1.2),
        n = 0,
        Ea = (45.6433, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;C_sec_rad_intra;OOH
""",
)

entry(
    index = 4,
    label = "C5H9O2 <=> C4H6O + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38e+12, 's^-1', '*|/', 1.2),
        n = 0,
        Ea = (63.953, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;C_sec_rad_intra;OOR
""",
)

entry(
    index = 5,
    label = "C6H11O2 <=> C5H8O + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.09e+12, 's^-1', '*|/', 1.2),
        n = 0,
        Ea = (63.953, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;C_ter_rad_intra;OOR
""",
)

entry(
    index = 6,
    label = "C5H9O2-2 <=> C5H8O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.09e+12, 's^-1', '*|/', 1.2),
        n = 0,
        Ea = (45.6433, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;C_ter_rad_intra;OOH
""",
)

entry(
    index = 7,
    label = "C5H7O2 <=> C5H6O + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.94e+11, 's^-1', '*|/', 1.74),
        n = 0,
        Ea = (75.8559, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SS;C_pri_rad_intra;OOH
""",
)

entry(
    index = 8,
    label = "C6H9O2 <=> C5H6O + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.94e+11, 's^-1', '*|/', 1.74),
        n = 0,
        Ea = (89.9403, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SS;C_pri_rad_intra;OOR
""",
)

entry(
    index = 9,
    label = "C6H9O2-2 <=> C6H8O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.04e+11, 's^-1', '*|/', 1.74),
        n = 0,
        Ea = (75.8559, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SS;C_sec_rad_intra;OOH
""",
)

entry(
    index = 10,
    label = "C7H11O2 <=> C6H8O + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.04e+11, 's^-1', '*|/', 1.74),
        n = 0,
        Ea = (89.9403, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SS;C_sec_rad_intra;OOR
""",
)

entry(
    index = 11,
    label = "C8H13O2 <=> C7H10O + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.31e+11, 's^-1', '*|/', 1.74),
        n = 0,
        Ea = (89.9403, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SS;C_ter_rad_intra;OOR
""",
)

entry(
    index = 12,
    label = "C7H11O2-2 <=> C7H10O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.31e+11, 's^-1', '*|/', 1.74),
        n = 0,
        Ea = (75.8559, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SS;C_ter_rad_intra;OOH
""",
)

entry(
    index = 13,
    label = "C8H11O2 <=> C7H8O + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.026e+11, 's^-1', '*|/', 1.41),
        n = 0,
        Ea = (61.9232, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSS;C_pri_rad_intra;OOR
""",
)

entry(
    index = 14,
    label = "C7H9O2 <=> C7H8O + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.026e+11, 's^-1', '*|/', 1.41),
        n = 0,
        Ea = (61.9232, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSS;C_pri_rad_intra;OOH
""",
)

entry(
    index = 15,
    label = "C9H13O2 <=> C8H10O + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.63e+10, 's^-1', '*|/', 1.41),
        n = 0,
        Ea = (54.392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSS;C_sec_rad_intra;OOR
""",
)

entry(
    index = 16,
    label = "C8H11O2-2 <=> C8H10O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.63e+10, 's^-1', '*|/', 1.41),
        n = 0,
        Ea = (54.392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSS;C_sec_rad_intra;OOH
""",
)

entry(
    index = 17,
    label = "C10H15O2 <=> C9H12O + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.57e+10, 's^-1', '*|/', 1.41),
        n = 0,
        Ea = (48.116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSS;C_ter_rad_intra;OOR
""",
)

entry(
    index = 18,
    label = "C9H13O2-2 <=> C9H12O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.57e+10, 's^-1', '*|/', 1.41),
        n = 0,
        Ea = (48.116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSS;C_ter_rad_intra;OOH
""",
)

entry(
    index = 19,
    label = "C4H7O2 <=> C3H4O + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.2e+12, 's^-1'),
        n = 0,
        Ea = (92.048, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;Cs_rad_intra;OOR
""",
)

entry(
    index = 20,
    label = "C3H5O2 <=> C3H4O + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.2e+12, 's^-1'),
        n = 0,
        Ea = (92.048, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;Cs_rad_intra;OOH
""",
)

entry(
    index = 21,
    label = "C6H9O2 <=> C5H6O + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.5e+11, 's^-1'),
        n = 0,
        Ea = (63.806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SS;Cs_rad_intra;OOR
""",
)

entry(
    index = 22,
    label = "C5H7O2 <=> C5H6O + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.5e+11, 's^-1'),
        n = 0,
        Ea = (63.806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SS;Cs_rad_intra;OOH
""",
)

entry(
    index = 23,
    label = "C8H11O2 <=> C7H8O + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.876e+10, 's^-1'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSS;Cs_rad_intra;OOR
""",
)

entry(
    index = 24,
    label = "C7H9O2 <=> C7H8O + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.876e+10, 's^-1'),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSS;Cs_rad_intra;OOH
""",
)

entry(
    index = 25,
    label = "C9H11O2 <=> C9H10O + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.34e+09, 's^-1'),
        n = 0,
        Ea = (7.5312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5OO_SSSS;Cs_rad_intra;OOH
""",
)

entry(
    index = 26,
    label = "C10H13O2 <=> C9H10O + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.34e+09, 's^-1'),
        n = 0,
        Ea = (7.5312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5OO_SSSS;Cs_rad_intra;OOR
""",
)

entry(
    index = 27,
    label = "C9H11O3 <=> C8H8O2 + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        Ea = (78.3663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""CBS-QB3 Including treatment of hindered rotor (SSM)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5OO_SSSSCO;Cs_rad_intra;OOR
""",
)

entry(
    index = 28,
    label = "C8H9O3 <=> C8H8O2 + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        Ea = (78.3663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""CBS-QB3 Including treatment of hindered rotor (SSM)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5OO_SSSSCO;Cs_rad_intra;OOH
""",
)

entry(
    index = 29,
    label = "C3H5O3 <=> C2H2O2 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.92e+15, 's^-1'),
        n = -0.53,
        Ea = (101.839, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""CBS-QB3 Including treatment for hindered rotor, QTST Calculation (CFG & JWA)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_SCO;Cs_rad_intra;OOR
""",
)

entry(
    index = 30,
    label = "C2H3O3 <=> C2H2O2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.92e+15, 's^-1'),
        n = -0.53,
        Ea = (101.839, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""CBS-QB3 Including treatment for hindered rotor, QTST Calculation (CFG & JWA)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_SCO;Cs_rad_intra;OOH
""",
)

entry(
    index = 31,
    label = "C7H9O3 <=> C6H6O2 + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        Ea = (78.3663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSSCO;Cs_rad_intra;OOR
""",
)

entry(
    index = 32,
    label = "C6H7O3 <=> C6H6O2 + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        Ea = (78.3663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OO_SSSCO;Cs_rad_intra;OOH
""",
)

entry(
    index = 33,
    label = "C4H5O3 <=> C4H4O2 + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        Ea = (78.3663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SSCO;Cs_rad_intra;OOH
""",
)

entry(
    index = 34,
    label = "C5H7O3 <=> C4H4O2 + CH3O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.54e+08, 's^-1'),
        n = 0.77,
        Ea = (78.3663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OO_SSCO;Cs_rad_intra;OOR
""",
)

entry(
    index = 35,
    label = "C3H4O2 <=> C3H4O + O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.24e+09, 's^-1'),
        n = 1.1,
        Ea = (133.47, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;C_pri_rad_intra;OOJ
""",
)

entry(
    index = 36,
    label = "C4H6O2 <=> C4H6O + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.27e+09, 's^-1'),
        n = 1.06,
        Ea = (129.704, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_S;C_rad/H/NonDeC_intra;OOJ
""",
)

