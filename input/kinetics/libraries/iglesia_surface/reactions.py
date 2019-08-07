#!/usr/bin/env python
# encoding: utf-8

name = "iglesia_surface"
shortDesc = u"iglesia_surface"
longDesc = u"""
Manually added surface reactions with estimated rates
"""

entry(
    index = 0,
    label = "IC3H7 + HNO <=> propane + NO",
    kinetics = Arrhenius(A=(8.2e+05, 'cm^3/(mol*s)'), n=1.87, Ea=(950, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
RMG's est., unmodified
Taking this reaction in "reverse" on purpose so that the endothermic direction will be set by thermo.
""",
)

entry(
    index = 1,
    label = "NC3H7 + HNO <=> propane + NO",
    kinetics = Arrhenius(A=(8.2e+05, 'cm^3/(mol*s)'), n=1.87, Ea=(950, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
RMG's est., unmodified
Taking this reaction in "reverse" on purpose so that the endothermic direction will be set by thermo.
""",
)

entry(
    index = 2,
    label = "IC3H7 + NO <=> C3H6 + HNO",
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
est., same as NC3H7 + NO <=> C3H6 + HNO
""",
)

entry(
    index = 3,
    label = "NC3H7 + NO <=> C3H6 + HNO",
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
est., same as IC3H7 + NO <=> C3H6 + HNO
""",
)

# entry(
#     index = 4,
#     label = "H2 + NO + NO <=> HNO + HNO",
#     kinetics = Arrhenius(A=(1e+15, 'cm^6/(mol^2*s)'), n=0, Ea=(11, 'kJ/mol'), T0=(1, 'K')),
#     longDesc =
# u"""
# From D.W. Blaylock, Y-A. Zhu, W.H. Green, Top. Catal. 2011, 54, 828-844, doi: 10.1007/s11244-011-9704-z
# Table 7, Reaction 1
# Original dimensions were length/time, other than unit conversion (m to cm).
# Multiplied by 1e+10 when converting to gas phase (n at 1 bar, 873 K = 1.4e-5 mol / cm^3).
# """,
# )

entry(
    index = 4,
    label = "HNO + HNO <=> H2 + NO + NO",
    kinetics = Arrhenius(A=(5e+15, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 5,
    label = "CH3 + HNO <=> CH4 + NO",
    kinetics = Arrhenius(A=(1.6e+15, 'cm^3/(mol*s)'), n=0.76, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
From NOx2018, originally was:
    kinetics = Arrhenius(A=(1.6e+15, 'cm^3/(mol*s)'), n=0.76, Ea=(0.35, 'kcal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 6,
    label = "H + HNO <=> H2 + NO",
    kinetics = Arrhenius(A=(4.46e+11, 'cm^3/(mol*s)'), n=0.72, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
From primaryNitrogenLibrary by Page 1992 at CASSCF//(CASSCF and CISD), originally was:
    kinetics = Arrhenius(A=(4.46e+11, 'cm^3/(mol*s)'), n=0.72, Ea=(0.66, 'kcal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 7,
    label = "H + NO <=> HNO",
    kinetics = Arrhenius(A=(1.5e+15, 'cm^3/(mol*s)'), n=-0.41, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
From NOx2018, only high-P limit rate taken, originally was:

entry(
    index = 653,
    label = "NO + H <=> HNO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+15, 'cm^3/(mol*s)'), n=-0.41, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.4e+14, 'cm^6/(mol^2*s)'),
            n = 0.206,
            Ea = (-1550, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.82,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'N#N': 1.6},
    ),
)
""",
)

entry(
    index = 8,
    label = "CH3 + NO <=> CH3NO",
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
From NOx2018, only high-P limit rate taken, originally was:

entry(
    index = 959,
    label = "CH3 + NO <=> CH3NO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(192, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.5e+16, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-2841, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 5,
        T3 = (1e-30, 'K'),
        T1 = (120, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)
""",
)

