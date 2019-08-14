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
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2.0, Ea=(0.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 1,
    label = "NC3H7 + HNO <=> propane + NO",
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2.0, Ea=(0.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 2,
    label = "C2H5 + HNO <=> C2H6 + HNO",
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2.0, Ea=(0.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
* new
""",
)

entry(
    index = 3,
    label = "IC3H7 + NO <=> C3H6 + HNO",
    kinetics = Arrhenius(A=(1.0e+15, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "NC3H7 + NO <=> C3H6 + HNO",
    kinetics = Arrhenius(A=(1.0e+15, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "C2H5 + NO <=> C2H4 + HNO",
    kinetics = Arrhenius(A=(1.0e+15, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
* new
""",
)

entry(
    index = 6,
    label = "H + NO <=> HNO",
    kinetics = Arrhenius(A=(1.0e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
high-P limit of C2H5 + NO
""",
)

entry(
    index = 7,
    label = "CH3 + NO <=> CH3NO",
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
an order of magnitude lower than "H + NO <=> HNO"
""",
)

entry(
    index = 8,
    label = "C2H5 + NO <=> C2H5NO",
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 9,
    label = "IC3H7 + NO <=> IC3H7NO",
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 10,
    label = "NC3H7 + NO <=> NC3H7NO",
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 11,
    label = "H + HNO <=> H2 + NO",
    kinetics = Arrhenius(A=(1.0e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From primaryNitrogenLibrary by Page 1992 at CASSCF//(CASSCF and CISD), originally was:
    kinetics = Arrhenius(A=(4.46e+11, 'cm^3/(mol*s)'), n=0.72, Ea=(0.66, 'kcal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 12,
    label = "CH3 + HNO <=> CH4 + NO",
    kinetics = Arrhenius(A=(1.0e+11, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 13,
    label = "HNO + propenyl <=> C3H6 + NO",
    kinetics = Arrhenius(A=(1.0e+11, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
* new
""",
)
