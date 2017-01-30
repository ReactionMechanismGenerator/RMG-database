#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/GlarborgMarshall"
shortDesc = u""
longDesc = u"""
Interactions between nitrogen and sulfur species in combustion

Taken from:
Hidden interactions - Trace species governing combustion and emmision
Peter Glarborg
Proceedings of the Combustion Institute, 31 (2007) 77-98
DOI: 10.1016/j.proci.2006.08.119
"""

entry(
    index = 1,
    label = "SO + N <=> S + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.0e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[265,266],rv
""",
)

entry(
    index = 2,
    label = "SO2 + N <=> SO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.4e+09, 'cm^3/(mol*s)'),
        n = 1.00,
        Ea = (6280, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Estimated as O2 + N
""",
)

entry(
    index = 3,
    label = "SO2 + NO2 <=> NO + SO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (27000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[267]
""",
)

entry(
    index = 4,
    label = "SO2 + NH <=> SO + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.0e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Estimated as SO2 + O
""",
)

entry(
    index = 5,
    label = "S + NO <=> SNO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.4e+13, 's^-1'), n=0.24, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.2e+15, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (-1870, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.22,
        T3 = (7445, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
    ),
    longDesc = 
u"""
[262]
""",
)

entry(
    index = 6,
    label = "SH + NO <=> HSNO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.6e+13, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.4e+23, 'cm^3/(mol*s)'),
            n = -2.50,
            Ea = (-1870, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e+30, 'K'),
        T1 = (1e-30, 'K'),
        T2 = (1e+30, 'K'),
    ),
    longDesc = 
u"""
[263,268]
""",
)

entry(
    index = 7,
    label = "NS + O <=> S + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.0e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
[265], rv
""",
)

entry(
    index = 8,
    label = "SNO + H <=> SH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 9,
    label = "S + HNO <=> SH + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 10,
    label = "SO + NH <=> NS + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.0e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
See text
""",
)

