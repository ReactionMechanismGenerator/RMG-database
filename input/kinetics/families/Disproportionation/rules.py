#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 485,
    label = "Y_rad_birad_trirad_quadrad;XH_Rrad_birad",
    kinetics = ArrheniusEP(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 556,
    label = "O2b;XH_Rrad_birad",
    kinetics = ArrheniusEP(
        A = (5e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A.G. Vandeputte estimated value""",
)

entry(
    index = 556,
    label = "Y_rad_birad_trirad_quadrad;Cdpri_Csrad",
    kinetics = ArrheniusEP(
        A = (1e+09, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Estimated value, AG Vandeputte""",
)

entry(
    index = 654,
    label = "H_rad;Cds/H2_d_N5ddrad/O",
    kinetics = ArrheniusEP(
        A = (4.8e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        alpha = 0,
        E0 = (-0.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: CH2NO + H = HCNO + H2 (B&D #57c2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 655,
    label = "O_pri_rad;Cds/H2_d_N5ddrad/O",
    kinetics = ArrheniusEP(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 2,
        alpha = 0,
        E0 = (-1.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: CH2NO + OH = HCNO + H2O (B&D #57e2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 656,
    label = "C_methyl;Cds/H2_d_N5ddrad/O",
    kinetics = ArrheniusEP(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        alpha = 0,
        E0 = (-1.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: CH2NO + CH3 = HCNO + CH4 (B&D #57f2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 657,
    label = "NH2_rad;Cds/H2_d_N5ddrad/O",
    kinetics = ArrheniusEP(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        alpha = 0,
        E0 = (-1.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: CH2NO + NH2 = HCNO + NH3 (B&D #57g2) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

