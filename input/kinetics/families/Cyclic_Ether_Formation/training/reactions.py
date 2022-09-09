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

entry(
    index = 37,
    label = "C4H7O2-3 <=> C4H6O-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.03087e+09,'s^-1'), n=0.954882, Ea=(126.689,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.0422, dn = +|- 0.00549275, dEa = +|- 0.0281353 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: C=C([CH]C)OO <=> CC=C1CO1 + [OH]
""",
)

entry(
    index = 38,
    label = "C3H5O3-2 <=> C3H4O2-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.38891e+10,'s^-1'), n=0.588176, Ea=(114.704,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.02773, dn = +|- 0.00363438, dEa = +|- 0.0186163 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]C(=O)COO <=> O=C1COC1 + [OH]
""",
)

entry(
    index = 39,
    label = "C6H11O2-2 <=> C6H10O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.78705e+09,'s^-1'), n=0.83402, Ea=(101.595,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.01578, dn = +|- 0.002081, dEa = +|- 0.0106594 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: C=C(C)[C](C)COO <=> CC1=C(C)COC1 + [OH]
""",
)

entry(
    index = 40,
    label = "C4H9O2 <=> C4H8O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.63578e+06,'s^-1'), n=1.14162, Ea=(44.4605,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.09413, dn = +|- 0.0119546, dEa = +|- 0.0612349 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]CCCOO <=> C1CCOC1 + [OH]
""",
)

entry(
    index = 41,
    label = "C4H7O2-4 <=> C4H6O-3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41451e+08,'s^-1'), n=1.29418, Ea=(106.291,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.02139, dn = +|- 0.00281178, dEa = +|- 0.0144027 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: C=C[CH]COO <=> C1=CCOC1 + [OH]
""",
)

entry(
    index = 42,
    label = "C3H7O2 <=> C3H6O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.34238e+08,'s^-1'), n=1.1945, Ea=(45.4801,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.02521, dn = +|- 0.00330887, dEa = +|- 0.0169489 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]C(C)OO <=> CC1CO1 + [OH]
""",
)

entry(
    index = 43,
    label = "C2H5O2 <=> C2H4O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.78488e+08,'s^-1'), n=1.3147, Ea=(52.3296,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.03554, dn = +|- 0.00464121, dEa = +|- 0.0237735 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]COO <=> C1CO1 + [OH]
""",
)

entry(
    index = 44,
    label = "C5H11O2 <=> C5H10O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38223e+09,'s^-1'), n=0.839684, Ea=(36.1981,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.01646, dn = +|- 0.00216885, dEa = +|- 0.0111094 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: C[CH]C(C)(C)OO <=> CC1OC1(C)C + [OH]
""",
)

entry(
    index = 45,
    label = "C6H11O2-3 <=> C6H10O-2 + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.92676e+11,'s^-1'), n=0.225643, Ea=(123.232,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.05079, dn = +|- 0.00658344, dEa = +|- 0.0337221 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]C(=C)C(C)(C)OO <=> C=C1COC1(C)C + [OH]
""",
)

entry(
    index = 46,
    label = "C6H13O2 <=> C6H12O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.7757e+10,'s^-1'), n=0.511744, Ea=(35.6076,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.02652, dn = +|- 0.00347829, dEa = +|- 0.0178167 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: C[C](C)C(C)(C)OO <=> CC1(C)OC1(C)C + [OH]
""",
)

entry(
    index = 47,
    label = "C6H11O2-4 <=> C6H10O-3 + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.67792e+10,'s^-1'), n=0.370445, Ea=(90.1509,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.09813, dn = +|- 0.0124387, dEa = +|- 0.0637142 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]C(=C)C(C)COO <=> C=C1COCC1C + [OH]
""",
)

entry(
    index = 48,
    label = "C4H7O2-5 <=> C4H6O-4 + OH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.91622e+08,'s^-1'), n=0.896273, Ea=(131.268,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.02386, dn = +|- 0.00313309, dEa = +|- 0.0160485 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]C(=C)COO <=> C=C1COC1 + [OH]
""",
)

entry(
    index = 49,
    label = "C5H11O2-2 <=> C5H10O-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.10049e+09,'s^-1'), n=0.93255, Ea=(35.7581,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.02603, dn = +|- 0.00341531, dEa = +|- 0.0174941 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: C[C](C)C(C)OO <=> CC1OC1(C)C + [OH]
""",
)

entry(
    index = 50,
    label = "C4H9O2-2 <=> C4H8O-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.69722e+09,'s^-1'), n=0.942572, Ea=(38.7169,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.0153, dn = +|- 0.002018, dEa = +|- 0.0103368 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]C(C)(C)OO <=> CC1(C)CO1 + [OH]
""",
)

entry(
    index = 51,
    label = "C4H7O2-6 <=> C4H6O-5 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.68408e+09,'s^-1'), n=0.88186, Ea=(47.0691,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.03612, dn = +|- 0.00471472, dEa = +|- 0.0241501 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]C(C=C)OO <=> C=CC1CO1 + [OH]
""",
)

entry(
    index = 52,
    label = "C3H7O2-2 <=> C3H6O-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.02182e+07,'s^-1'), n=1.14033, Ea=(75.0043,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.03392, dn = +|- 0.00443305, dEa = +|- 0.0227072 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]CCOO <=> C1COC1 + [OH]
""",
)

entry(
    index = 53,
    label = "C3H5O3-3 <=> C3H4O2-3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.12077e+09,'s^-1'), n=0.58338, Ea=(77.122,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.05338, dn = +|- 0.0069104, dEa = +|- 0.0353969 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]CC(=O)OO <=> O=C1CCO1 + [OH]
""",
)

entry(
    index = 54,
    label = "C4H7O2-7 <=> C4H6O-6 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.62354e+07,'s^-1'), n=1.27837, Ea=(73.7629,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.04105, dn = +|- 0.00534606, dEa = +|- 0.0273839 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]CC(=C)OO <=> C=C1CCO1 + [OH]
""",
)

entry(
    index = 55,
    label = "C4H7O2-8 <=> C4H6O-7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.14245e+08,'s^-1'), n=1.24018, Ea=(72.064,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.01544, dn = +|- 0.00203621, dEa = +|- 0.01043 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: C=C[CH]COO <=> C=CC1CO1 + [OH]
""",
)

entry(
    index = 56,
    label = "C4H9O2-3 <=> C4H8O-3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.78368e+07,'s^-1'), n=1.21142, Ea=(66.0469,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.02043, dn = +|- 0.00268731, dEa = +|- 0.0137651 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: C[CH]CCOO <=> CC1CCO1 + [OH]
""",
)

entry(
    index = 57,
    label = "C4H7O2-9 <=> C4H6O-8 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.14036e+08,'s^-1'), n=1.13262, Ea=(38.277,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.04968, dn = +|- 0.00644356, dEa = +|- 0.0330056 kJ/mol"""),
    rank = 5,
    shortDesc = u"""Calculated at CBS-QB3 + 1DSHR by Xiaorui Dong""",
    longDesc =
"""
Training reaction from kinetics library: cyclic_ether
Original entry: [CH2]CC=COO <=> C1=COCC1 + [OH]
""",
)

entry(
    index = 58,
    label = "C5H11O2-3 <=> C5H10O-3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.29e+09,'s^-1'), n=0.67, Ea=(18.154,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 59,
    label = "C5H11O2-4 <=> C5H10O-4 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.4e+10,'s^-1'), n=0.73, Ea=(12.459,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CC[C](C)COO <=> OH + C1OC1(C)CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 60,
    label = "C5H11O2-5 <=> C5H10O-5 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+09,'s^-1'), n=0.84, Ea=(17.137,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CC[C](C)COO <=> OH + C1OC1(C)CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 61,
    label = "C5H11O2-6 <=> C5H10O-6 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.41e+08,'s^-1'), n=0.84, Ea=(11.715,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CC[C](C)COO <=> OH + C1OC1(C)CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 62,
    label = "C5H11O2-7 <=> C5H10O-7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.56e+11,'s^-1'), n=0.59, Ea=(13.83,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CC[C](C)COO <=> OH + C1OC1(C)CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 63,
    label = "C5H11O2-8 <=> C5H10O-8 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.33e+07,'s^-1'), n=1.16, Ea=(15.287,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 64,
    label = "C5H11O2-9 <=> C5H10O-9 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.63e+08,'s^-1'), n=0.89, Ea=(11.911,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 65,
    label = "C5H11O2-10 <=> C5H10O-10 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.98e+09,'s^-1'), n=1.03, Ea=(13.191,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 66,
    label = "C5H11O2-2 <=> C5H10O-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04e+12,'s^-1'), n=0.42, Ea=(10.506,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 67,
    label = "C5H11O2-11 <=> C5H10O-11 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.79e+09,'s^-1'), n=0.85, Ea=(16.351,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 68,
    label = "C5H11O2-12 <=> C5H10O-12 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.43e+10,'s^-1'), n=0.75, Ea=(12.588,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 69,
    label = "C5H11O2-13 <=> C5H10O-13 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.36e+08,'s^-1'), n=1.01, Ea=(17.108,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 70,
    label = "C5H11O2 <=> C5H10O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.21e+10,'s^-1'), n=0.69, Ea=(11.244,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR by Ye et al.""",
    longDesc =
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC

Ye, Lili, Lidong Zhang, and Fei Qi. "Ab initio kinetics on low temperature
oxidation of iso-pentane: the first oxygen addition." Combustion and Flame 190 (2018): 119-132.
""",
)

entry(
    index = 71,
    label = "C4H9O3 <=> C4H8O2 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(217200,'s^-1'), n=1.242, Ea=(9.946,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q-1J <=> MPO1-1OCYC + OH
""",
)

entry(
    index = 72,
    label = "C4H9O3-2 <=> C4H8O2-2 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(1.408e+10,'s^-1'), n=0.591, Ea=(14.27,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q2J <=> MPO12OCYC + OH
added
""",
)

entry(
    index = 73,
    label = "C4H9O3-3 <=> C4H8O2-3 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(31610,'s^-1'), n=1.706, Ea=(7.488,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q3J <=> MPO13OCYC + OH
changed
""",
)

entry(
    index = 74,
    label = "C4H9O5 <=> C4H8O4 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(2.105e+17,'s^-1'), n=-1.948, Ea=(43.801,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q-1QJ <=> Ozoind1-1 + OH
changed
""",
)

entry(
    index = 75,
    label = "C4H9O5-2 <=> C4H8O4-2 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(4.81e+16,'s^-1'), n=-1.277, Ea=(44,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q3QJ <=> Ozoind13 + OH
changed
""",
)

entry(
    index = 76,
    label = "C4H9O5-3 <=> C4H8O4-3 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(7.382e+15,'s^-1'), n=-1.199, Ea=(17.561,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q2J-1Q <=> MPO1Q2-1OCYC + OH
changed
""",
)

entry(
    index = 77,
    label = "C4H9O5-4 <=> C4H8O4-4 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(1.103e+17,'s^-1'), n=-1.498, Ea=(7.076,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q2J-1Q <=> MPO-1Q12OCYC + OH
changed
""",
)

entry(
    index = 78,
    label = "C4H9O5-5 <=> C4H8O4-5 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(1.285e+10,'s^-1'), n=1.123, Ea=(14.77,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q2J3Q <=> MPO1Q23OCYC + OH
changed
""",
)

entry(
    index = 79,
    label = "C4H9O5-6 <=> C4H8O4-6 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(4.741e+07,'s^-1'), n=1.777, Ea=(12.108,'kcal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: MPO1Q2J3Q <=> MPO3Q12OCYC + OH
changed
""",
)

entry(
    index = 80,
    label = "C3H7O3 <=> C3H6O2 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(5.67109e+15,'s^-1'), n=-0.889523, Ea=(115.476,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: dOCCCOO <=> OH + C1COOC1
Matt Johnson using ARC guess from Sarah Khaniche at CBS-QB3 with 1dhr
Optimized TS geometry:
C       0.21807800    1.01072400   -0.06473000
C      -1.30397100    0.94894800   -0.16311200
C      -1.61870800   -0.41633600    0.44295300
O      -0.73847700   -1.31305300   -0.16376700
O       0.70380000   -0.30464600   -0.38488700
H      -1.52004500   -0.40938800    1.53872200
H      -2.63135000   -0.75452000    0.18223700
H       0.66135400    1.70705500   -0.77883400
H       0.54439600    1.26227700    0.94737900
H      -1.62262400    0.96892700   -1.20743000
H      -1.76897900    1.78241600    0.36982100
O       2.41153100   -0.10184700    0.15290200
H       2.66937600   -0.95845500   -0.21924100
""",
)

entry(
    index = 81,
    label = "C3H5O3-3 <=> C3H4O2-3 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(1.12e+11,'s^-1'), n=0.455, Ea=(22.226,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: [CH2]CC(OO)=O <=> C1CC(O1)=O + OH
Mark Nimlos CBS-QB3 HR
""",
)

entry(
    index = 82,
    label = "C3H5O3-4 <=> C3H4O2-4 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(3.03e+16,'s^-1'), n=-0.986, Ea=(24.147,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: CC(OO)[C]=O <=> CC1OC1=O + OH
Mark Nimlos CBS-QB3 HR
""",
)

entry(
    index = 83,
    label = "C3H5O3-5 <=> C3H4O2-5 + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(2.49e+09,'s^-1'), n=1.18, Ea=(18.385,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: C(OO)C[C]=O <=> C1CC(O1)=O + OH
Mark Nimlos CBS-QB3 HR
""",
)

entry(
    index = 84,
    label = "C2H5O2 <=> C2H4O + OH",
    degeneracy = 1.0,

    kinetics = Arrhenius(A=(6.093e+08,'s^-1'), n=1.294, Ea=(14.894,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc =
"""
Training reaction from kinetics library: Johnson_methyl_propyl_ether_2021
Original entry: [CH2]COO <=> C1OC1 + OH
Mark Nimlos CBS-QB3 HR
""",
)
