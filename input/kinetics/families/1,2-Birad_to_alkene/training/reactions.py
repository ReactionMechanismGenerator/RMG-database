#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "SO2(T) => SO2(S)",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+10, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    rank = 1,
    longDesc = 
u"""
taken from:
F.B. Wampler, K. Otsuka, J.G. Calvert, E.K. Damon, Int. J. Chem. Kin., 1973, 5(4), 669-690, doi: 10.1002/kin.550050417
and adjusted to a first order reaction at 1 atm
Similar rates were determined by:
T.N. Rao, S.S. Collier, J.G. Calvet, JACS, 1969, 91(7), 1616-1612, doi: 10.1021/ja01035a006
""",
)

entry(
    index = 1,
    label = "C2H4 => C2H4-2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (1e+08, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""see description above""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_12_00
""",
)

entry(
    index = 2,
    label = "C3H6 => C3H6-2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.31e+07, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""see description above""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_12_10
""",
)

entry(
    index = 3,
    label = "C5H10 => C5H10-2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.51e+07, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""see description above""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_12_30
""",
)

entry(
    index = 4,
    label = "C6H12 => C6H12-2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.58e+07, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""see description above""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_12_40
""",
)

entry(
    index = 5,
    label = "C4H6 => C4H6-2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.01e+07, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""see description above""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_12_01
""",
)

entry(
    index = 6,
    label = "C8H10 => C8H10-2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.26e+07, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""see description above""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_12_03
""",
)

entry(
    index = 7,
    label = "C10H12 => C10H12-2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.31e+06, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""see description above""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_12_04
""",
)

entry(
    index = 8,
    label = "C9H12 => C9H12-2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.94e+06, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""see description above""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_12_13
""",
)

entry(
    index = 9,
    label = "C7H12 => C7H12-2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.26e+07, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""see description above""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_12_31
""",
)

