#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/GlarborgNS"
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
        arrheniusHigh = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(300, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.2e+15, 'cm^6/(mol^2*s)'),
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
https://doi.org/10.1063/1.1806419
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
[263] is https://doi.org/10.5194/acp-4-1461-2004, where the rate is only given at 250-300K
[268] is https://doi.org/10.1063/1.447287, where the rate is only given at 250-445K
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

alongd comment: 3.0e13 cm^3/(mol*s) was reported [10.1524/zpch.2010.6138] to be the overall rate between SO + NH
regardless of the products. Since the SO + NH <=> NO + SH is also an important reaction [10.1039/b102061g],
the above rate should be slower.
""",
)

