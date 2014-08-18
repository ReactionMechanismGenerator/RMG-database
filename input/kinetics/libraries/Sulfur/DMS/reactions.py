#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DMS"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "CS2H2(2) + HJ <=> CS2H(2)J + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17400, 'cm^3/(mol*s)'), n=2.9, Ea=(5.87, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "CS2H2(2) + CH3J <=> CS2H(2)J + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000155, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.73, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "CS2H2(2) + HSJ <=> CS2H(2)J + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(156, 'cm^3/(mol*s)'), n=3.53, Ea=(8.32, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "CS2H2(2) + CH3SJ <=> CS2H(2)J + CH3SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(22.9, 'cm^3/(mol*s)'), n=3.69, Ea=(11.61, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "CH3SSCH2J <=> CH3SCH2SJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.13e+11, 's^-1'), n=0.22, Ea=(31.93, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "CH2S + CH3SJ <=> CH3SSCH2J",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25500, 'cm^3/(mol*s)'),
        n = 2.77,
        Ea = (-2.31, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 7,
    label = "CH2S + CH3SJ <=> CH3SCH2SJ",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.79,
        Ea = (-2.27, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "CH3CH2SSCH2J <=> CH3CH2SCH2SJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.13e+11, 's^-1'), n=0.22, Ea=(31.93, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "CH2S + CH3CH2SJ <=> CH3CH2SSCH2J",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25500, 'cm^3/(mol*s)'),
        n = 2.77,
        Ea = (-2.31, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "CH2S + CH3CH2SJ <=> CH3CH2SCH2SJ",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.79,
        Ea = (-2.27, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "CS2H2(2) + CH3J <=> CH3SSCH2J",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3120, 'cm^3/(mol*s)'), n=2.72, Ea=(7.28, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "CS2H2(2) + CH3J <=> CH3SCH2SJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6180, 'cm^3/(mol*s)'), n=2.57, Ea=(-1.16, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "CS2H2(2) + C2H5J <=> CH3CH2SSCH2J",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3120, 'cm^3/(mol*s)'), n=2.72, Ea=(7.28, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "CS2H2(2) + C2H5J <=> CH3CH2SCH2SJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6180, 'cm^3/(mol*s)'), n=2.57, Ea=(-1.16, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "CS2H2JJ <=> CS2H2(2)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.08e+10, 's^-1'), n=1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "CS2H(2)J <=> CS2H(1)J",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.08e+10, 's^-1'), n=1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "CS2H2JJ <=> HJ + CS2H(1)J",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.19e+09, 's^-1'), n=1.55, Ea=(36.55, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "CS2H(1)J <=> CS2 + HJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52e+08, 's^-1'), n=1.74, Ea=(30.56, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "CH2S + HJ <=> HCSJ + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(95000, 'cm^3/(mol*s)'), n=2.72, Ea=(3.68, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "CH2S + CH3J <=> HCSJ + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0033, 'cm^3/(mol*s)'), n=4.85, Ea=(3.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "CH2S + HSJ <=> HCSJ + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(127, 'cm^3/(mol*s)'), n=3.7, Ea=(1.93, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "CH2S + CH3SJ <=> HCSJ + CH3SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.49, 'cm^3/(mol*s)'), n=3.96, Ea=(5.36, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "C2H3S2(1)J <=> HCSJ + CH2S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.52e+14, 's^-1'), n=-0.05, Ea=(36.87, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "C2H3S2(1)J <=> C2H3S2(2)J",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e-21, 's^-1'), n=9.96, Ea=(19.14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "C2H3S2(2)J <=> CS2 + CH3J",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+12, 's^-1'), n=0.67, Ea=(10.64, 'kcal/mol'), T0=(1, 'K')),
)

