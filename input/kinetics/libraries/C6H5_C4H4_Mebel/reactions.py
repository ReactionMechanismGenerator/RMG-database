#!/usr/bin/env python
# encoding: utf-8

name = "C6H5_C4H4_Mebel"
shortDesc = u"level of theory: G3(MP2,CC)//B3LYP/6-311G(d,p)"
longDesc = u"""
Kinetics from:
Formation Mechanism of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames
A. M. Mebel*, A. Landera, R. I. Kaiser*
Department of Chemistry and Biochemistry, Florida International UniVersity, Miami, FL 33199
Chemical Science and Engineering Devision, Argonne National Laboratory, Argonne, IL 60439
Department of Chemistry, University of Hawaii at Manoa, Honolulu, HI 96822

Include all the rates in supporting information except for the rates without specific products (reactant->all)
Species P2(cis-) an P3(trans-) are lumped in this library, only P3 appear in final kinetics
All the rates at each pressure are the sum of MultiArrhenius expressions
Duplicated rates (backward rate if there is the forward rate) are deleted after we checked the backward rates are similar to those rates calculated from thermo by using plot kinetics tool in RMG website
"""
entry(
    index = 1,
    label = "C6H5 + C4H4 <=> W1",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.62e+84, 'cm^3/(mol*s)'),
                        n = -21.48,
                        Ea = (42190, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.16e+43, 'cm^3/(mol*s)'),
                        n = -10.07,
                        Ea = (12890, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.63e+69, 'cm^3/(mol*s)'),
                        n = -16.52,
                        Ea = (40770, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.89e+26, 'cm^3/(mol*s)'),
                        n = -4.68,
                        Ea = (7584, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (7.59e+49, 'cm^3/(mol*s)'),
                        n = -10.65,
                        Ea = (32900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.04e+17, 'cm^3/(mol*s)'),
                        n = -1.72,
                        Ea = (4254, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.35e+27, 'cm^3/(mol*s)'),
                        n = -4.11,
                        Ea = (18320, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.27e+20, 'cm^3/(mol*s)'),
                        n = -2.72,
                        Ea = (5193, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 1375 K with MAE of 1.9%, 4.6%\nfit btw. 500 and 1650 K with MAE of 2.8%, 6.0%\nfit btw. 500 and 1800 K with MAE of 2.5%, 4.6%\nfit btw. 500 and 2250 K with MAE of 3.7%, 12.1%',
    ),
    longDesc = 
u"""
fit btw. 500 and 1375 K with MAE of 1.9%, 4.6%
fit btw. 500 and 1650 K with MAE of 2.8%, 6.0%
fit btw. 500 and 1800 K with MAE of 2.5%, 4.6%
fit btw. 500 and 2250 K with MAE of 3.7%, 12.1%
""",
)

entry(
    index = 2,
    label = "C6H5 + C4H4 <=> W2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(A=(0.974, 'cm^3/(mol*s)'), n=2.9, Ea=(-2716, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (5.19e+42, 'cm^3/(mol*s)'),
                        n = -9.67,
                        Ea = (16100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (5.11e+71, 'cm^3/(mol*s)'),
                        n = -17.71,
                        Ea = (36780, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.14e+25, 'cm^3/(mol*s)'),
                        n = -4.3,
                        Ea = (10590, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (6.21e+50, 'cm^3/(mol*s)'),
                        n = -10.96,
                        Ea = (31890, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.19e+26, 'cm^3/(mol*s)'),
                        n = -4.37,
                        Ea = (11290, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 800 K with MAE of 4.3%, 7.4%\nfit btw. 500 and 1000 K with MAE of 1.6%, 2.7%\nfit btw. 500 and 1250 K with MAE of 0.1%, 0.2%\nfit btw. 500 and 1650 K with MAE of 1.3%, 2.2%',
    ),
    longDesc = 
u"""
fit btw. 500 and 800 K with MAE of 4.3%, 7.4%
fit btw. 500 and 1000 K with MAE of 1.6%, 2.7%
fit btw. 500 and 1250 K with MAE of 0.1%, 0.2%
fit btw. 500 and 1650 K with MAE of 1.3%, 2.2%
""",
)

entry(
    index = 3,
    label = "C6H5 + C4H4 <=> W3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.93e+100, 'cm^3/(mol*s)'),
                        n = -26.66,
                        Ea = (46050, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.2e+63, 'cm^3/(mol*s)'),
                        n = -16.41,
                        Ea = (20390, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.9e+83, 'cm^3/(mol*s)'),
                        n = -21.12,
                        Ea = (43890, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.27e+40, 'cm^3/(mol*s)'),
                        n = -9.21,
                        Ea = (13650, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.28e+59, 'cm^3/(mol*s)'),
                        n = -13.82,
                        Ea = (33050, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.59e+49, 'cm^3/(mol*s)'),
                        n = -12.04,
                        Ea = (16650, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (7.99e+47, 'cm^3/(mol*s)'),
                        n = -10.2,
                        Ea = (30490, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.09e+23, 'cm^3/(mol*s)'),
                        n = -3.6,
                        Ea = (7851, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 1250 K with MAE of 0.7%, 2.6%\nfit btw. 500 and 1375 K with MAE of 1.6%, 3.8%\nfit btw. 500 and 1650 K with MAE of 4.1%, 11.3%\nfit btw. 500 and 1800 K with MAE of 2.8%, 8.3%',
    ),
    longDesc = 
u"""
fit btw. 500 and 1250 K with MAE of 0.7%, 2.6%
fit btw. 500 and 1375 K with MAE of 1.6%, 3.8%
fit btw. 500 and 1650 K with MAE of 4.1%, 11.3%
fit btw. 500 and 1800 K with MAE of 2.8%, 8.3%
""",
)

entry(
    index = 4,
    label = "C6H5 + C4H4 <=> W9",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.12e+104, 'cm^3/(mol*s)'),
                        n = -27.48,
                        Ea = (50700, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.9e+66, 'cm^3/(mol*s)'),
                        n = -17.14,
                        Ea = (25190, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.16e+89, 'cm^3/(mol*s)'),
                        n = -22.37,
                        Ea = (50870, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.39e+40, 'cm^3/(mol*s)'),
                        n = -8.41,
                        Ea = (20600, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.83e+69, 'cm^3/(mol*s)'),
                        n = -16.09,
                        Ea = (46530, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.19e+36, 'cm^3/(mol*s)'),
                        n = -7.38,
                        Ea = (20950, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.54e+51, 'cm^3/(mol*s)'),
                        n = -10.64,
                        Ea = (42550, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.24e+19, 'cm^3/(mol*s)'),
                        n = -2.03,
                        Ea = (15810, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 1250 K with MAE of 0.5%, 1.5%\nfit btw. 500 and 1500 K with MAE of 3.0%, 7.7%\nfit btw. 500 and 1650 K with MAE of 4.6%, 12.6%\nfit btw. 500 and 2000 K with MAE of 5.6%, 16.9%',
    ),
    longDesc = 
u"""
fit btw. 500 and 1250 K with MAE of 0.5%, 1.5%
fit btw. 500 and 1500 K with MAE of 3.0%, 7.7%
fit btw. 500 and 1650 K with MAE of 4.6%, 12.6%
fit btw. 500 and 2000 K with MAE of 5.6%, 16.9%
""",
)

entry(
    index = 5,
    label = "C6H5 + C4H4 <=> W14",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (5.79e-30, 'cm^3/(mol*s)'),
                        n = 11.82,
                        Ea = (-14160, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (5.61e+28, 'cm^3/(mol*s)'),
                        n = -5.59,
                        Ea = (9901, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.05e+25, 'cm^3/(mol*s)'),
                        n = -4.19,
                        Ea = (11700, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.61e+12, 'cm^3/(mol*s)'),
                        n = -1.02,
                        Ea = (2055, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (4.98e+26, 'cm^3/(mol*s)'),
                        n = -4.17,
                        Ea = (17780, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.1e+15, 'cm^3/(mol*s)'),
                        n = -1.16,
                        Ea = (5818, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 800 K with MAE of 7.9%, 13.7%\nfit btw. 500 and 1000 K with MAE of 2.4%, 5.5%\nfit btw. 500 and 1250 K with MAE of 0.6%, 1.5%\nfit btw. 500 and 1650 K with MAE of 0.4%, 0.6%',
    ),
    longDesc = 
u"""
fit btw. 500 and 800 K with MAE of 7.9%, 13.7%
fit btw. 500 and 1000 K with MAE of 2.4%, 5.5%
fit btw. 500 and 1250 K with MAE of 0.6%, 1.5%
fit btw. 500 and 1650 K with MAE of 0.4%, 0.6%
""",
)

entry(
    index = 6,
    label = "C6H5 + C4H4 <=> W16",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (6.08e+80, 'cm^3/(mol*s)'),
                        n = -20.63,
                        Ea = (41150, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.1e+48, 'cm^3/(mol*s)'),
                        n = -11.78,
                        Ea = (18430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.05e+67, 'cm^3/(mol*s)'),
                        n = -16.24,
                        Ea = (39650, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.81e+42, 'cm^3/(mol*s)'),
                        n = -9.42,
                        Ea = (20090, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (4.25e+59, 'cm^3/(mol*s)'),
                        n = -13.53,
                        Ea = (41900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.74e+29, 'cm^3/(mol*s)'),
                        n = -5.4,
                        Ea = (17340, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.75e+52, 'cm^3/(mol*s)'),
                        n = -11.34,
                        Ea = (42480, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (0.00221, 'cm^3/(mol*s)'),
                        n = 4.37,
                        Ea = (6920, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 1125 K with MAE of 1.1%, 2.5%\nfit btw. 500 and 1375 K with MAE of 3.1%, 6.3%\nfit btw. 500 and 1650 K with MAE of 7.5%, 24.6%\nfit btw. 500 and 2000 K with MAE of 8.9%, 35.7%',
    ),
    longDesc = 
u"""
fit btw. 500 and 1125 K with MAE of 1.1%, 2.5%
fit btw. 500 and 1375 K with MAE of 3.1%, 6.3%
fit btw. 500 and 1650 K with MAE of 7.5%, 24.6%
fit btw. 500 and 2000 K with MAE of 8.9%, 35.7%
""",
)

entry(
    index = 7,
    label = "C6H5 + C4H4 <=> P1 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.05e+84, 'cm^3/(mol*s)'),
                        n = -20.96,
                        Ea = (56410, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.61e+32, 'cm^3/(mol*s)'),
                        n = -5.92,
                        Ea = (26750, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (5.42e+191, 'cm^3/(mol*s)'),
                        n = -55.82,
                        Ea = (91430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.01e+67, 'cm^3/(mol*s)'),
                        n = -15.36,
                        Ea = (58800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.78e+62, 'cm^3/(mol*s)'),
                        n = -15.14,
                        Ea = (52980, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.8e+74, 'cm^3/(mol*s)'),
                        n = -17.11,
                        Ea = (76440, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.33e-73, 'cm^3/(mol*s)'),
                        n = 23.5,
                        Ea = (-16820, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.4e+51, 'cm^3/(mol*s)'),
                        n = -10.55,
                        Ea = (70860, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 2.0%, 5.3%\nfit btw. 600 and 2500 K with MAE of 7.5%, 17.2%\nfit btw. 600 and 2500 K with MAE of 4.3%, 14.0%\nfit btw. 500 and 2500 K with MAE of 27.1%, 73.7%',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 2.0%, 5.3%
fit btw. 600 and 2500 K with MAE of 7.5%, 17.2%
fit btw. 600 and 2500 K with MAE of 4.3%, 14.0%
fit btw. 500 and 2500 K with MAE of 27.1%, 73.7%
""",
)

entry(
    index = 8,
    label = "C6H5 + C4H4 <=> P3 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.16e+75, 'cm^3/(mol*s)'),
                        n = -18.09,
                        Ea = (53030, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.11e+22, 'cm^3/(mol*s)'),
                        n = -2.77,
                        Ea = (21620, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.81e+69, 'cm^3/(mol*s)'),
                        n = -16.03,
                        Ea = (48640, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.18e+19, 'cm^3/(mol*s)'),
                        n = -1.76,
                        Ea = (19320, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.46e+63, 'cm^3/(mol*s)'),
                        n = -14.19,
                        Ea = (55500, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.71e+19, 'cm^3/(mol*s)'),
                        n = -1.87,
                        Ea = (25250, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.16e+46, 'cm^3/(mol*s)'),
                        n = -9.15,
                        Ea = (43460, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.6e+60, 'cm^3/(mol*s)'),
                        n = -15.29,
                        Ea = (33300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.02e+48, 'cm^3/(mol*s)'),
                        n = -9.65,
                        Ea = (52910, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.89e+39, 'cm^3/(mol*s)'),
                        n = -8.51,
                        Ea = (34000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(171, 'cm^3/(mol*s)'), n=2.96, Ea=(14790, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (1.53e+53, 'cm^3/(mol*s)'),
                        n = -10.7,
                        Ea = (56220, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(A=(0.01, 'cm^3/(mol*s)'), n=4.19, Ea=(22630, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (5.28e+50, 'cm^3/(mol*s)'),
                        n = -10.01,
                        Ea = (65610, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.23e+47, 'cm^3/(mol*s)'),
                        n = -8.81,
                        Ea = (61090, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.37e-13, 'cm^3/(mol*s)'),
                        n = 7.42,
                        Ea = (10080, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 0.9%, 2.7% from P2\nfit btw. 500 and 2500 K with MAE of 1.2%, 3.1% from P3\nfit btw. 500 and 2500 K with MAE of 2.1%, 4.1% from P2\nfit btw. 500 and 2500 K with MAE of 5.4%, 12.4% from P3\nfit btw. 500 and 2500 K with MAE of 5.9%, 10.9% from P2\nfit btw. 500 and 2500 K with MAE of 4.8%, 13.7% from P3\nfit btw. 500 and 2500 K with MAE of 6.6%, 19.7% from P2\nfit btw. 500 and 2500 K with MAE of 6.3%, 15.6% from P3',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 0.9%, 2.7% from P2
fit btw. 500 and 2500 K with MAE of 1.2%, 3.1% from P3
fit btw. 500 and 2500 K with MAE of 2.1%, 4.1% from P2
fit btw. 500 and 2500 K with MAE of 5.4%, 12.4% from P3
fit btw. 500 and 2500 K with MAE of 5.9%, 10.9% from P2
fit btw. 500 and 2500 K with MAE of 4.8%, 13.7% from P3
fit btw. 500 and 2500 K with MAE of 6.6%, 19.7% from P2
fit btw. 500 and 2500 K with MAE of 6.3%, 15.6% from P3
""",
)

entry(
    index = 9,
    label = "C6H5 + C4H4 <=> P4 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (9.34e+36, 'cm^3/(mol*s)'),
                        n = -6.72,
                        Ea = (25850, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.63e+76, 'cm^3/(mol*s)'),
                        n = -16.56,
                        Ea = (96340, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (6.43e+41, 'cm^3/(mol*s)'),
                        n = -7.82,
                        Ea = (35290, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.72e+175, 'cm^3/(mol*s)'),
                        n = -51.49,
                        Ea = (69040, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (6.42e+56, 'cm^3/(mol*s)'),
                        n = -11.85,
                        Ea = (52060, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.94e+08, 'cm^3/(mol*s)'),
                        n = 1.28,
                        Ea = (16580, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.26e+35, 'cm^3/(mol*s)'),
                        n = -5.68,
                        Ea = (42490, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.66e+27, 'cm^3/(mol*s)'),
                        n = -4.96,
                        Ea = (23290, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 5.0%, 18.5%\nfit btw. 500 and 2500 K with MAE of 6.7%, 16.3%\nfit btw. 500 and 2500 K with MAE of 3.3%, 7.1%\nfit btw. 500 and 2500 K with MAE of 10.3%, 28.6%',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 5.0%, 18.5%
fit btw. 500 and 2500 K with MAE of 6.7%, 16.3%
fit btw. 500 and 2500 K with MAE of 3.3%, 7.1%
fit btw. 500 and 2500 K with MAE of 10.3%, 28.6%
""",
)

entry(
    index = 10,
    label = "C6H5 + C4H4 <=> P5 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.42e+27, 'cm^3/(mol*s)'),
                        n = -4.54,
                        Ea = (27070, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.6e+39, 'cm^3/(mol*s)'),
                        n = -7.04,
                        Ea = (60180, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (7.65e+26, 'cm^3/(mol*s)'),
                        n = -4.11,
                        Ea = (32520, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.23e+128, 'cm^3/(mol*s)'),
                        n = -39.42,
                        Ea = (47670, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.11e+34, 'cm^3/(mol*s)'),
                        n = -6.03,
                        Ea = (42520, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.54e+70, 'cm^3/(mol*s)'),
                        n = -18.97,
                        Ea = (42100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (6.23e+31, 'cm^3/(mol*s)'),
                        n = -5.14,
                        Ea = (46860, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.96e+23, 'cm^3/(mol*s)'),
                        n = -4.33,
                        Ea = (27970, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 2.8%, 10.3%\nfit btw. 500 and 2500 K with MAE of 8.8%, 18.5%\nfit btw. 500 and 2500 K with MAE of 5.5%, 12.4%\nfit btw. 500 and 2500 K with MAE of 8.4%, 14.5%',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 2.8%, 10.3%
fit btw. 500 and 2500 K with MAE of 8.8%, 18.5%
fit btw. 500 and 2500 K with MAE of 5.5%, 12.4%
fit btw. 500 and 2500 K with MAE of 8.4%, 14.5%
""",
)

entry(
    index = 11,
    label = "C6H5 + C4H4 <=> P6 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.78e+21, 'cm^3/(mol*s)'),
                        n = -2.39,
                        Ea = (23660, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (79300, 'cm^3/(mol*s)'),
                        n = -3.4,
                        Ea = (-20220, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.35e+49, 'cm^3/(mol*s)'),
                        n = -10.24,
                        Ea = (48890, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(55100, 'cm^3/(mol*s)'), n=2.26, Ea=(15650, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (6.67e+27, 'cm^3/(mol*s)'),
                        n = -3.97,
                        Ea = (36910, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.89e+07, 'cm^3/(mol*s)'),
                        n = 1.14,
                        Ea = (17980, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.62e+25, 'cm^3/(mol*s)'),
                        n = -3.21,
                        Ea = (40420, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(0.585, 'cm^3/(mol*s)'), n=3.48, Ea=(16210, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 9.8%, 18.0%\nfit btw. 500 and 2500 K with MAE of 1.4%, 3.9%\nfit btw. 500 and 2500 K with MAE of 2.8%, 5.8%\nfit btw. 500 and 2500 K with MAE of 4.2%, 12.1%',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 9.8%, 18.0%
fit btw. 500 and 2500 K with MAE of 1.4%, 3.9%
fit btw. 500 and 2500 K with MAE of 2.8%, 5.8%
fit btw. 500 and 2500 K with MAE of 4.2%, 12.1%
""",
)

entry(
    index = 12,
    label = "P3 + H <=> W21",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (9.29e+86, 'cm^3/(mol*s)'),
                        n = -22.77,
                        Ea = (29260, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.89e+68, 'cm^3/(mol*s)'),
                        n = -18.15,
                        Ea = (14760, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.7e+82, 'cm^3/(mol*s)'),
                        n = -21.48,
                        Ea = (26900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.97e+65, 'cm^3/(mol*s)'),
                        n = -18.07,
                        Ea = (8834, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (8.6e+81, 'cm^3/(mol*s)'),
                        n = -20.06,
                        Ea = (37990, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.37e+49, 'cm^3/(mol*s)'),
                        n = -11.13,
                        Ea = (14150, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.18e+81, 'cm^3/(mol*s)'),
                        n = -19.84,
                        Ea = (37610, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.57e+48, 'cm^3/(mol*s)'),
                        n = -10.9,
                        Ea = (13740, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.44e+79, 'cm^3/(mol*s)'),
                        n = -18.62,
                        Ea = (44110, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.87e+61, 'cm^3/(mol*s)'),
                        n = -14.45,
                        Ea = (21430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.16e+78, 'cm^3/(mol*s)'),
                        n = -18.43,
                        Ea = (43710, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.4e+60, 'cm^3/(mol*s)'),
                        n = -14.07,
                        Ea = (20780, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (5.97e+26, 'cm^3/(mol*s)'),
                        n = -3.55,
                        Ea = (10840, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.11e+21, 'cm^3/(mol*s)'),
                        n = -3.85,
                        Ea = (-3820, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.6e+26, 'cm^3/(mol*s)'),
                        n = -3.51,
                        Ea = (10590, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.23e+21, 'cm^3/(mol*s)'),
                        n = -3.78,
                        Ea = (-4017, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 1125 K with MAE of 0.3%, 0.8% from P2\nfit btw. 500 and 1125 K with MAE of 0.7%, 1.3% from P3\nfit btw. 500 and 1375 K with MAE of 0.9%, 1.8% from P2\nfit btw. 500 and 1375 K with MAE of 0.9%, 1.6% from P3\nfit btw. 500 and 1650 K with MAE of 1.7%, 3.5% from P2\nfit btw. 500 and 1650 K with MAE of 1.7%, 3.7% from P3\nfit btw. 500 and 2000 K with MAE of 31.6%, 154.8% from P2\nfit btw. 500 and 2000 K with MAE of 29.8%, 142.2% from P3',
    ),
    longDesc = 
u"""
fit btw. 500 and 1125 K with MAE of 0.3%, 0.8% from P2
fit btw. 500 and 1125 K with MAE of 0.7%, 1.3% from P3
fit btw. 500 and 1375 K with MAE of 0.9%, 1.8% from P2
fit btw. 500 and 1375 K with MAE of 0.9%, 1.6% from P3
fit btw. 500 and 1650 K with MAE of 1.7%, 3.5% from P2
fit btw. 500 and 1650 K with MAE of 1.7%, 3.7% from P3
fit btw. 500 and 2000 K with MAE of 31.6%, 154.8% from P2
fit btw. 500 and 2000 K with MAE of 29.8%, 142.2% from P3
""",
)

entry(
    index = 13,
    label = "P3 + H <=> P1 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (4.42e+38, 'cm^3/(mol*s)'),
                        n = -7.06,
                        Ea = (16830, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.18e-15, 'cm^3/(mol*s)'),
                        n = 7.83,
                        Ea = (-12950, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.31e+53, 'cm^3/(mol*s)'),
                        n = -11.45,
                        Ea = (27780, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.08e+35, 'cm^3/(mol*s)'),
                        n = -6.12,
                        Ea = (13800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (8.21e+48, 'cm^3/(mol*s)'),
                        n = -9.77,
                        Ea = (28270, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.88e+190, 'cm^3/(mol*s)'),
                        n = -55.83,
                        Ea = (66750, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.45e+71, 'cm^3/(mol*s)'),
                        n = -16.2,
                        Ea = (43440, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.23e+31, 'cm^3/(mol*s)'),
                        n = -5.07,
                        Ea = (15960, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.39e+66, 'cm^3/(mol*s)'),
                        n = -14.42,
                        Ea = (46740, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.98e+18, 'cm^3/(mol*s)'),
                        n = -1.43,
                        Ea = (11810, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+68, 'cm^3/(mol*s)'),
                        n = -14.92,
                        Ea = (48160, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.64e+34, 'cm^3/(mol*s)'),
                        n = -5.93,
                        Ea = (20520, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (6.77e+22, 'cm^3/(mol*s)'),
                        n = -2.22,
                        Ea = (19550, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.36e+20, 'cm^3/(mol*s)'),
                        n = -2.53,
                        Ea = (10430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.27e+21, 'cm^3/(mol*s)'),
                        n = -2.09,
                        Ea = (20250, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.57e+70, 'cm^3/(mol*s)'),
                        n = -15.27,
                        Ea = (59300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 1.5%, 2.7% from P2\nfit btw. 500 and 2500 K with MAE of 1.3%, 2.0% from P3\nfit btw. 500 and 2500 K with MAE of 6.5%, 17.4% from P2\nfit btw. 500 and 2500 K with MAE of 1.3%, 5.7% from P3\nfit btw. 500 and 2500 K with MAE of 3.7%, 9.9% from P2\nfit btw. 500 and 2500 K with MAE of 4.4%, 13.2% from P3\nfit btw. 500 and 2500 K with MAE of 22.8%, 76.6% from P2\nfit btw. 500 and 2500 K with MAE of 6.4%, 14.7% from P3',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 1.5%, 2.7% from P2
fit btw. 500 and 2500 K with MAE of 1.3%, 2.0% from P3
fit btw. 500 and 2500 K with MAE of 6.5%, 17.4% from P2
fit btw. 500 and 2500 K with MAE of 1.3%, 5.7% from P3
fit btw. 500 and 2500 K with MAE of 3.7%, 9.9% from P2
fit btw. 500 and 2500 K with MAE of 4.4%, 13.2% from P3
fit btw. 500 and 2500 K with MAE of 22.8%, 76.6% from P2
fit btw. 500 and 2500 K with MAE of 6.4%, 14.7% from P3
""",
)

entry(
    index = 14,
    label = "P3 + H <=> W1",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.36e+91, 'cm^3/(mol*s)'),
                        n = -22.77,
                        Ea = (47640, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.4e+45, 'cm^3/(mol*s)'),
                        n = -9.91,
                        Ea = (15250, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.23e+79, 'cm^3/(mol*s)'),
                        n = -18.72,
                        Ea = (48990, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.4e+28, 'cm^3/(mol*s)'),
                        n = -4.61,
                        Ea = (9988, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.36e+44, 'cm^3/(mol*s)'),
                        n = -8.51,
                        Ea = (28970, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.28e+22, 'cm^3/(mol*s)'),
                        n = -2.74,
                        Ea = (7706, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.66e+46, 'cm^3/(mol*s)'),
                        n = -8.92,
                        Ea = (34580, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.99e+17, 'cm^3/(mol*s)'),
                        n = -1.13,
                        Ea = (6157, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 1375 K with MAE of 2.2%, 6.2%\nfit btw. 500 and 1650 K with MAE of 3.2%, 8.6%\nfit btw. 500 and 1800 K with MAE of 2.2%, 4.4%\nfit btw. 500 and 2250 K with MAE of 2.5%, 4.4%',
    ),
    longDesc = 
u"""
fit btw. 500 and 1375 K with MAE of 2.2%, 6.2%
fit btw. 500 and 1650 K with MAE of 3.2%, 8.6%
fit btw. 500 and 1800 K with MAE of 2.2%, 4.4%
fit btw. 500 and 2250 K with MAE of 2.5%, 4.4%
""",
)

entry(
    index = 15,
    label = "P3 + H <=> P5 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (6.75e+27, 'cm^3/(mol*s)'),
                        n = -3.51,
                        Ea = (30280, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.28e+73, 'cm^3/(mol*s)'),
                        n = -19.01,
                        Ea = (39310, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (4.65e+36, 'cm^3/(mol*s)'),
                        n = -5.9,
                        Ea = (38760, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.35e+146, 'cm^3/(mol*s)'),
                        n = -41.89,
                        Ea = (65670, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.53e+58, 'cm^3/(mol*s)'),
                        n = -11.85,
                        Ea = (59030, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.54e+11, 'cm^3/(mol*s)'),
                        n = 1.04,
                        Ea = (25140, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (-4.69e+48, 'cm^3/(mol*s)'),
                        n = -9.57,
                        Ea = (47060, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.28e+27, 'cm^3/(mol*s)'),
                        n = -3.24,
                        Ea = (37500, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 0.7%, 1.2%\nfit btw. 500 and 2500 K with MAE of 3.5%, 7.6%\nfit btw. 500 and 2500 K with MAE of 2.3%, 5.9%\nfit btw. 500 and 2500 K with MAE of 17.2%, 39.2%',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 0.7%, 1.2%
fit btw. 500 and 2500 K with MAE of 3.5%, 7.6%
fit btw. 500 and 2500 K with MAE of 2.3%, 5.9%
fit btw. 500 and 2500 K with MAE of 17.2%, 39.2%
""",
)

entry(
    index = 16,
    label = "P3 + H <=> P6 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.16e+76, 'cm^3/(mol*s)'),
                        n = -17.77,
                        Ea = (57170, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.2e+27, 'cm^3/(mol*s)'),
                        n = -3.68,
                        Ea = (27490, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.5e+65, 'cm^3/(mol*s)'),
                        n = -14.14,
                        Ea = (58860, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.03e+26, 'cm^3/(mol*s)'),
                        n = -3.22,
                        Ea = (31900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (-2.07e+30, 'cm^3/(mol*s)'),
                        n = -3.32,
                        Ea = (57920, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.26e+11, 'cm^3/(mol*s)'),
                        n = 1.7,
                        Ea = (32950, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(A=(33900, 'cm^3/(mol*s)'), n=2.86, Ea=(29300, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (7.12e+54, 'cm^3/(mol*s)'),
                        n = -10.69,
                        Ea = (70370, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 1.1%, 2.6%\nfit btw. 500 and 2500 K with MAE of 1.7%, 3.3%\nfit btw. 500 and 2500 K with MAE of 16.8%, 45.7%\nfit btw. 500 and 2500 K with MAE of 6.1%, 18.2%',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 1.1%, 2.6%
fit btw. 500 and 2500 K with MAE of 1.7%, 3.3%
fit btw. 500 and 2500 K with MAE of 16.8%, 45.7%
fit btw. 500 and 2500 K with MAE of 6.1%, 18.2%
""",
)

entry(
    index = 17,
    label = "P4 + H <=> W3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.87e+108, 'cm^3/(mol*s)'),
                        n = -28.25,
                        Ea = (50010, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.05e+68, 'cm^3/(mol*s)'),
                        n = -17.03,
                        Ea = (22610, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.69e+91, 'cm^3/(mol*s)'),
                        n = -22.6,
                        Ea = (47230, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.88e+46, 'cm^3/(mol*s)'),
                        n = -10.23,
                        Ea = (16120, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (5.99e+66, 'cm^3/(mol*s)'),
                        n = -15.22,
                        Ea = (35840, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.13e+56, 'cm^3/(mol*s)'),
                        n = -13.15,
                        Ea = (19190, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (7.27e+61, 'cm^3/(mol*s)'),
                        n = -13.48,
                        Ea = (38160, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.21e+30, 'cm^3/(mol*s)'),
                        n = -4.98,
                        Ea = (10860, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 1250 K with MAE of 0.8%, 1.3%\nfit btw. 500 and 1375 K with MAE of 1.6%, 3.1%\nfit btw. 500 and 1650 K with MAE of 4.0%, 10.0%\nfit btw. 500 and 1800 K with MAE of 2.4%, 4.7%',
    ),
    longDesc = 
u"""
fit btw. 500 and 1250 K with MAE of 0.8%, 1.3%
fit btw. 500 and 1375 K with MAE of 1.6%, 3.1%
fit btw. 500 and 1650 K with MAE of 4.0%, 10.0%
fit btw. 500 and 1800 K with MAE of 2.4%, 4.7%
""",
)

entry(
    index = 18,
    label = "P4 + H <=> W9",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.04e+111, 'cm^3/(mol*s)'),
                        n = -28.88,
                        Ea = (56820, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.29e+49, 'cm^3/(mol*s)'),
                        n = -11.38,
                        Ea = (17660, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (4.12e+40, 'cm^3/(mol*s)'),
                        n = -7.8,
                        Ea = (21160, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.9e+80, 'cm^3/(mol*s)'),
                        n = -21.25,
                        Ea = (26740, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (8.4e+64, 'cm^3/(mol*s)'),
                        n = -14.47,
                        Ea = (42510, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.05e+25, 'cm^3/(mol*s)'),
                        n = -3.52,
                        Ea = (9724, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.22e+37, 'cm^3/(mol*s)'),
                        n = -6.46,
                        Ea = (25920, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.58e+17, 'cm^3/(mol*s)'),
                        n = -1.09,
                        Ea = (6788, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 1250 K with MAE of 1.1%, 2.4%\nfit btw. 500 and 1500 K with MAE of 5.1%, 20.8%\nfit btw. 500 and 1650 K with MAE of 3.6%, 6.4%\nfit btw. 500 and 2000 K with MAE of 1.1%, 1.8%',
    ),
    longDesc = 
u"""
fit btw. 500 and 1250 K with MAE of 1.1%, 2.4%
fit btw. 500 and 1500 K with MAE of 5.1%, 20.8%
fit btw. 500 and 1650 K with MAE of 3.6%, 6.4%
fit btw. 500 and 2000 K with MAE of 1.1%, 1.8%
""",
)

entry(
    index = 19,
    label = "P4 + H <=> P1 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.39e+68, 'cm^3/(mol*s)'),
                        n = -15.84,
                        Ea = (47740, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.19e+65, 'cm^3/(mol*s)'),
                        n = -14.12,
                        Ea = (78080, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (4.15e+215, 'cm^3/(mol*s)'),
                        n = -53,
                        Ea = (281400, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.17e+70, 'cm^3/(mol*s)'),
                        n = -16.15,
                        Ea = (59770, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (4.44e+204, 'cm^3/(mol*s)'),
                        n = -58.64,
                        Ea = (108900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7e+72, 'cm^3/(mol*s)'),
                        n = -16.33,
                        Ea = (72210, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.39e-56, 'cm^3/(mol*s)'),
                        n = 18.93,
                        Ea = (-8745, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.94e+54, 'cm^3/(mol*s)'),
                        n = -10.88,
                        Ea = (69960, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 6.0%, 22.1%\nfit btw. 600 and 2500 K with MAE of 9.0%, 24.4%\nfit btw. 600 and 2500 K with MAE of 7.8%, 19.9%\nfit btw. 500 and 2500 K with MAE of 20.8%, 47.5%',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 6.0%, 22.1%
fit btw. 600 and 2500 K with MAE of 9.0%, 24.4%
fit btw. 600 and 2500 K with MAE of 7.8%, 19.9%
fit btw. 500 and 2500 K with MAE of 20.8%, 47.5%
""",
)

entry(
    index = 20,
    label = "P4 + H <=> P3 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.16e+62, 'cm^3/(mol*s)'),
                        n = -13.64,
                        Ea = (44450, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.08e+83, 'cm^3/(mol*s)'),
                        n = -18.39,
                        Ea = (99730, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.22e+44, 'cm^3/(mol*s)'),
                        n = -8.74,
                        Ea = (42920, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.4e+33, 'cm^3/(mol*s)'),
                        n = -5.18,
                        Ea = (52710, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (7.21e+61, 'cm^3/(mol*s)'),
                        n = -13.13,
                        Ea = (54490, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.03e+187, 'cm^3/(mol*s)'),
                        n = -54.57,
                        Ea = (83960, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.43e+80, 'cm^3/(mol*s)'),
                        n = -19,
                        Ea = (72770, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.19e+26, 'cm^3/(mol*s)'),
                        n = -3.28,
                        Ea = (40820, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (-8.9e+47, 'cm^3/(mol*s)'),
                        n = -9.38,
                        Ea = (46240, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.14e+37, 'cm^3/(mol*s)'),
                        n = -6,
                        Ea = (42120, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.71e+59, 'cm^3/(mol*s)'),
                        n = -12.43,
                        Ea = (69320, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.62e+98, 'cm^3/(mol*s)'),
                        n = -26.73,
                        Ea = (66880, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (1.2e+09, 'cm^3/(mol*s)'),
                        n = 1.63,
                        Ea = (32240, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.24e+65, 'cm^3/(mol*s)'),
                        n = -13.47,
                        Ea = (77240, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(3690, 'cm^3/(mol*s)'), n=3.14, Ea=(37750, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (4.52e+72, 'cm^3/(mol*s)'),
                        n = -15.77,
                        Ea = (90010, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 6.8%, 24.2% from P3\nfit btw. 500 and 2500 K with MAE of 1.8%, 6.8% from P2\nfit btw. 500 and 2500 K with MAE of 12.0%, 26.5% from P3\nfit btw. 500 and 2500 K with MAE of 0.8%, 1.8% from P2\nfit btw. 500 and 2500 K with MAE of 33.5%, 126.4% from P3\nfit btw. 500 and 2500 K with MAE of 9.1%, 20.9% from P2\nfit btw. 500 and 2500 K with MAE of 8.8%, 21.0% from P3\nfit btw. 500 and 2500 K with MAE of 7.9%, 23.5% from P2',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 6.8%, 24.2% from P3
fit btw. 500 and 2500 K with MAE of 1.8%, 6.8% from P2
fit btw. 500 and 2500 K with MAE of 12.0%, 26.5% from P3
fit btw. 500 and 2500 K with MAE of 0.8%, 1.8% from P2
fit btw. 500 and 2500 K with MAE of 33.5%, 126.4% from P3
fit btw. 500 and 2500 K with MAE of 9.1%, 20.9% from P2
fit btw. 500 and 2500 K with MAE of 8.8%, 21.0% from P3
fit btw. 500 and 2500 K with MAE of 7.9%, 23.5% from P2
""",
)

entry(
    index = 21,
    label = "P4 + H <=> P5 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1, 10, 100], 'atm'),
        arrhenius = [
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (3.19e+39, 'cm^3/(mol*s)'),
                        n = -7.34,
                        Ea = (34810, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.7e+39, 'cm^3/(mol*s)'),
                        n = -6.51,
                        Ea = (54500, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (4.36e+33, 'cm^3/(mol*s)'),
                        n = -5.31,
                        Ea = (37580, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (0.00101, 'cm^3/(mol*s)'),
                        n = -6.44,
                        Ea = (-53030, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.59e+40, 'cm^3/(mol*s)'),
                        n = -7.06,
                        Ea = (46770, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.81e+107, 'cm^3/(mol*s)'),
                        n = -29.67,
                        Ea = (57790, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (7.47e+40, 'cm^3/(mol*s)'),
                        n = -7,
                        Ea = (53240, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.86e+32, 'cm^3/(mol*s)'),
                        n = -5.99,
                        Ea = (34670, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
        comment = 'fit btw. 500 and 2500 K with MAE of 2.6%, 9.1%\nfit btw. 500 and 2500 K with MAE of 11.0%, 21.9%\nfit btw. 500 and 2500 K with MAE of 6.7%, 14.9%\nfit btw. 500 and 2500 K with MAE of 6.8%, 12.3%',
    ),
    longDesc = 
u"""
fit btw. 500 and 2500 K with MAE of 2.6%, 9.1%
fit btw. 500 and 2500 K with MAE of 11.0%, 21.9%
fit btw. 500 and 2500 K with MAE of 6.7%, 14.9%
fit btw. 500 and 2500 K with MAE of 6.8%, 12.3%
""",
)

entry(
    index = 22,
    label = "C6H5 + C4H4 <=> i-C4H3 + C6H6",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(103000, 'cm^3/(mol*s)'), n=2.19, Ea=(9446, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (391, 'cm^3/(mol*s)'),
                n = 2.96,
                Ea = (4436.3, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'fit btw. 500 and 2500 K',
            ),
        ],
    ),
)

entry(
    index = 23,
    label = "C6H5 + C4H4 <=> n-C4H3 + C6H6",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (695000, 'cm^3/(mol*s)'),
                n = 2.11,
                Ea = (14668, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1660, 'cm^3/(mol*s)'),
                n = 2.88,
                Ea = (8611.9, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'fit btw. 500 and 2500 K',
            ),
        ],
    ),
)

