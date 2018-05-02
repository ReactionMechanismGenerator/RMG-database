#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/rules"
shortDesc = u""
longDesc = u"""
Reaction family added by gmagoon, 3/1/10

Correlation used for #1-16 below:
        log10(tau(s)) = -8.0 + 0.2 * m + 0.3 * n
        where m = number of alkyl substituents, n = number of aryl/vinyl substituents

References for this correlation and for treatment of alkene triplets as 1,2-biradicals:
1. R. A. Caldwell, Intersystem crossing in organic photochemical intermediates, Pure Appl. Chem., 56 (1984) 1167-1177. DOI: 10.1351/pac198456091167
2. R. A. Caldwell, Laser flash photolysis studies of intersystem crossing in biradicals and alkene triplets, p. 110, in Kinetics and spectroscopy of carbenes and biradicals, ed. M. S. Platz, 1990. DOI: 10.1007/978-1-4899-3707-0_4
3. D. J. Unett and R. A. Caldwell, The triplet state of alkenes: structure, dynamics, energetics and chemistry, Res. Chem. Intermed., 21 (1995) 665-709. DOI: 10.1163/156856795X00639
4. T. Ni, R. A. Caldwell, and L. A. Melton, The relaxed and spectroscopic energies of olefin triplets, J. Am. Chem. Soc., 111 (1989) 457-464. DOI: 10.1021/ja00184a008

To extrapolate to other groups, I am basing my (rough) assignments on the author's argument in Ref. 1,
that this effect is mainly related to number of hydrogens and mass of substituents, rather than electronic
stabilization/polar effects; note however, that this will not correctly account for large mass of extended groups like
large alkyl chains (in any case, the effect is relatively small, and the resulting estimate should still be within an
order or magnitude or so of what we would obtain if we assigned groups differently)

The assignments I use are:
                    no slow-down: H
                    m slow-down: Cs, Os
                    n slow-down: Cd, Ct, Cb, CO

it is assumed that k = 1/tau(s)
nomenclature used is `Y_12_mn`, where m and n are defined as above

No. Y_12birad   Temp.       A         n    a    E0     DA   Dn   Da   DE0  Rank
1.  Y_12birad   300-1500    1.0E+8    0    0    0.0    0    0    0    0    0
2.  Y_12_00     300-1500    1.0E+8    0    0    0.0    0    0    0    0    5
3.  Y_12_10     300-1500    6.31E+7   0    0    0.0    0    0    0    0    5
4.  Y_12_20     300-1500    3.98E+7   0    0    0.0    0    0    0    0    5
5.  Y_12_30     300-1500    2.51E+7   0    0    0.0    0    0    0    0    5
6.  Y_12_40     300-1500    1.58E+7   0    0    0.0    0    0    0    0    5
7.  Y_12_01     300-1500    5.01E+7   0    0    0.0    0    0    0    0    5
8.  Y_12_02     300-1500    2.51E+7   0    0    0.0    0    0    0    0    5
9.  Y_12_03     300-1500    1.26E+7   0    0    0.0    0    0    0    0    5
10. Y_12_04     300-1500    6.31E+6   0    0    0.0    0    0    0    0    5
11. Y_12_11     300-1500    3.16E+7   0    0    0.0    0    0    0    0    5
12. Y_12_12     300-1500    1.58E+7   0    0    0.0    0    0    0    0    5
13. Y_12_21     300-1500    2.00E+7   0    0    0.0    0    0    0    0    5
14. Y_12_22     300-1500    1.0E+7    0    0    0.0    0    0    0    0    5
15. Y_12_13     300-1500    7.94E+6   0    0    0.0    0    0    0    0    5
16. Y_12_31     300-1500    1.26E+7   0    0    0.0    0    0    0    0    5
"""

entry(
    index = 1,
    label = "Y_12birad",
    kinetics = ArrheniusEP(
        A = (1e+08, 's^-1'),
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
    index = 2,
    label = "Y_12_00",
    kinetics = ArrheniusEP(
        A = (1e+08, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 3,
    label = "Y_12_10",
    kinetics = ArrheniusEP(
        A = (6.31e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 4,
    label = "Y_12_20",
    kinetics = ArrheniusEP(
        A = (3.98e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 5,
    label = "Y_12_30",
    kinetics = ArrheniusEP(
        A = (2.51e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 6,
    label = "Y_12_40",
    kinetics = ArrheniusEP(
        A = (1.58e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 7,
    label = "Y_12_01",
    kinetics = ArrheniusEP(
        A = (5.01e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 8,
    label = "Y_12_02",
    kinetics = ArrheniusEP(
        A = (2.51e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 9,
    label = "Y_12_03",
    kinetics = ArrheniusEP(
        A = (1.26e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 10,
    label = "Y_12_04",
    kinetics = ArrheniusEP(
        A = (6.31e+06, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 11,
    label = "Y_12_11",
    kinetics = ArrheniusEP(
        A = (3.16e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 12,
    label = "Y_12_12",
    kinetics = ArrheniusEP(
        A = (1.58e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 13,
    label = "Y_12_21",
    kinetics = ArrheniusEP(
        A = (2e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 14,
    label = "Y_12_22",
    kinetics = ArrheniusEP(
        A = (1e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 15,
    label = "Y_12_13",
    kinetics = ArrheniusEP(
        A = (7.94e+06, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)

entry(
    index = 16,
    label = "Y_12_31",
    kinetics = ArrheniusEP(
        A = (1.26e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see description above""",
)
