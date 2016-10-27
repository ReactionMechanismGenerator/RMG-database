#!/usr/bin/env python
# encoding: utf-8

name = "2005_Senosiain_OH_C2H2"
shortDesc = u"Calculated T,P-dependent rates for significant pathways on the OH + acetylene surface of 2005 Senosiain"
longDesc = u"""
T,P-dependent k's for the significant pathways on the OH + acetylene surface computed with RQCISD(T)/CBS//UB3LYP/6-311++G(d,p) by:
J. P. Senosiain, et al.,
"The Reaction of Acetylene with Hydroxyl Radicals",
J. Phys. Chem. A 2005, 109, 6045-6055
PLog rates taken directly from Table 6 of this paper.
Rates are for an Argon bath gas
"""
entry(
    index = 1,
    label = "OH + C2H2 <=> H2O + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.37e-18, 'cm^3/(molecule*s)'),
        n = 2.14,
        Ea = (71388.1, 'J/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "OH + C2H2 <=> HCCOH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.65e-19, 'cm^3/(molecule*s)'),
                n = 2.28,
                Ea = (51965.5, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.24e-18, 'cm^3/(molecule*s)'),
                n = 2.16,
                Ea = (52505.9, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.95e-18, 'cm^3/(molecule*s)'),
                n = 2.04,
                Ea = (53013.1, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.01e-18, 'cm^3/(molecule*s)'),
                n = 2,
                Ea = (53196, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.33e-18, 'cm^3/(molecule*s)'),
                n = 1.97,
                Ea = (53603.4, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.22e-17, 'cm^3/(molecule*s)'),
                n = 1.89,
                Ea = (56920.9, 'J/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 3,
    label = "OH + C2H2 <=> CH2CO + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.62e-21, 'cm^3/(molecule*s)'),
                n = 2.56,
                Ea = (-3533.65, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.52e-20, 'cm^3/(molecule*s)'),
                n = 2.28,
                Ea = (-1222.23, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.01e-19, 'cm^3/(molecule*s)'),
                n = 1.92,
                Ea = (2502.66, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.25e-17, 'cm^3/(molecule*s)'),
                n = 1.55,
                Ea = (8813.34, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.47e-18, 'cm^3/(molecule*s)'),
                n = 1.65,
                Ea = (14226.1, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.42e-20, 'cm^3/(molecule*s)'),
                n = 2.45,
                Ea = (18732.5, 'J/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 4,
    label = "OH + C2H2 <=> CO + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (7.9e-19, 'cm^3/(molecule*s)'),
                n = 1.68,
                Ea = (-1380.2, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.26e-18, 'cm^3/(molecule*s)'),
                n = 1.4,
                Ea = (947.85, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.27e-16, 'cm^3/(molecule*s)'),
                n = 1.05,
                Ea = (4664.42, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.12e-15, 'cm^3/(molecule*s)'),
                n = 0.73,
                Ea = (10792.2, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.16e-16, 'cm^3/(molecule*s)'),
                n = 0.92,
                Ea = (15631.2, 'J/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.37e-18, 'cm^3/(molecule*s)'),
                n = 1.77,
                Ea = (19655.4, 'J/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 5,
    label = "OH + C2H2 <=> HOC2H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (4.77e+40, 'cm^3/(molecule*s)'),
                        n = -18.57,
                        Ea = (41880, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.38e+09, 'cm^3/(molecule*s)'),
                        n = -7.36,
                        Ea = (26747.7, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (7.79e+35, 'cm^3/(molecule*s)'),
                        n = -16.87,
                        Ea = (38022.1, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.27e+08, 'cm^3/(molecule*s)'),
                        n = -7.02,
                        Ea = (24827, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (20600, 'cm^3/(molecule*s)'),
                        n = -5.56,
                        Ea = (15581.3, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+19, 'cm^3/(molecule*s)'),
                        n = -9.96,
                        Ea = (49113.6, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.16e+20, 'cm^3/(molecule*s)'),
                        n = -11.38,
                        Ea = (26356.9, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.79e+07, 'cm^3/(molecule*s)'),
                        n = -6.2,
                        Ea = (27762, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.47, 'cm^3/(molecule*s)'),
                        n = -4.06,
                        Ea = (13644, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.48e+07, 'cm^3/(molecule*s)'),
                        n = -5.92,
                        Ea = (36658.5, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (0.00103, 'cm^3/(molecule*s)'),
                        n = -2.8,
                        Ea = (11848.1, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (266000, 'cm^3/(molecule*s)'),
                        n = -4.91,
                        Ea = (40732.6, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

