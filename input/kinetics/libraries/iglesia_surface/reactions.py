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
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(1.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
too high, 1e12, small Ea, 1 kcal
""",
)

entry(
    index = 1,
    label = "NC3H7 + HNO <=> propane + NO",
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(1.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
too high, 1e12, small Ea, 1 kcal
""",
)

entry(
    index = 2,
    label = "C2H5 + HNO <=> C2H6 + NO",
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(1.0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
too high, 1e12, small Ea, 1 kcal
""",
)

entry(
    index = 3,
    label = "IC3H7 + NO <=> C3H6 + HNO",
    kinetics = Arrhenius(A=(1.0e+11, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""
A too high, 1e13
two cases: if Eley-Rideal case, 1e13
if migrates on the surface, higher, calc gas kinetic theory of collision w surface
""",
)

entry(
    index = 4,
    label = "NC3H7 + NO <=> C3H6 + HNO",
    kinetics = Arrhenius(A=(1.0e+11, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 5,
    label = "C2H5 + NO <=> C2H4 + HNO",
    kinetics = Arrhenius(A=(1.0e+11, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 6,
    label = "H + NO <=> HNO",
    kinetics = Arrhenius(A=(1.0e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
It's correct if this is an Eley-Rideal behaviour, higher if collision behaviour
""",
)

# entry(
#     index = 6,
#     label = "HNO <=> H + NO",
#     kinetics = Arrhenius(A=(1.0e+10, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
#     longDesc =
# u"""
# high-P limit of C2H5 + NO
# """,
# )

entry(
    index = 7,
    label = "CH3 + NO <=> CH3NO",
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
an order of magnitude lower than "H + NO <=> HNO"
""",
)

# entry(
#     index = 7,
#     label = "CH3NO <=> CH3 + NO",
#     kinetics = Arrhenius(A=(1e+8, 's^-1'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
#     longDesc =
# u"""
# an order of magnitude lower than "H + NO <=> HNO"
# """,
# )

entry(
    index = 8,
    label = "C2H5 + NO <=> C2H5NO",
    kinetics = Arrhenius(A=(5e+11, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 9,
    label = "IC3H7 + NO <=> IC3H7NO",
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 10,
    label = "NC3H7 + NO <=> NC3H7NO",
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0.0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""

""",
)

entry(
    index = 11,
    label = "H + HNO <=> H2 + NO",
    kinetics = Arrhenius(A=(4.46e+12, 'cm^3/(mol*s)'), n=0.72, Ea=(0.66, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
From primaryNitrogenLibrary by Page 1992 at CASSCF//(CASSCF and CISD), originally was:
    kinetics = Arrhenius(A=(4.46e+11, 'cm^3/(mol*s)'), n=0.72, Ea=(0.66, 'kcal/mol'), T0=(1, 'K')),
    
    
make it a bit higher A, small Ea
""",
)

entry(
    index = 12,
    label = "CH3 + HNO <=> CH4 + NO",
    kinetics = Arrhenius(A=(5.0e+11, 'cm^3/(mol*s)'), n=0.72, Ea=(0.66, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
like 11, a bit lower
""",
)

# entry(
#     index = 12,
#     label = "CH3 + HNO <=> CH4 + NO",
#     kinetics = Arrhenius(A=(4.46e+10, 'cm^3/(mol*s)'), n=0.72, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
#     longDesc =
# u"""
#
# """,
# )

entry(
    index = 13,
    label = "HNO + C3H5_allyl <=> C3H6 + NO",
    kinetics = Arrhenius(A=(5.0e+11, 'cm^3/(mol*s)'), n=0.0, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
high barrier, 5 kcal? A like 12
""",
)

entry(
    index = 14,
    label = "HNO + HNO <=> H2 + NO + NO",
    kinetics = Arrhenius(A=(2.0e+15, 'cm^3/(mol*s)'), n=0.0, Ea=(5.80, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
A = kB T / h * 100 (surface, not gas phase)
Ea = 2 * H(HNO) - automatically determined per BDE
""",
)

