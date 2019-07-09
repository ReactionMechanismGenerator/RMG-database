#!/usr/bin/env python
# encoding: utf-8

name = "Mebel_C6H5_C2H2"
shortDesc = u""
longDesc = u"""
A. M. Mebel, Y. Georgievskii, A. W. Jasper, S. J. Klippenstein, Temperature and pressure dependent rate coefficients 
for the HACA pathways from benzene to naphthalene, Proceedings of the Combust. Inst. (2016) 1-8
"""
entry(
    index = 1,
    label = "C6H5 + C2H2 <=> C6H5C2H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.75e+69, 'cm^3/(mol*s)'),
                n = -17.46,
                Ea = (28430, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.91e+61, 'cm^3/(mol*s)'),
                n = -14.55,
                Ea = (28610, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.22e+50, 'cm^3/(mol*s)'),
                n = -11.01,
                Ea = (24920, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.11e+43, 'cm^3/(mol*s)'),
                n = -8.7,
                Ea = (24030, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2,
    label = "C6H5 + C2H2 <=> C6H4C2H3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.09e+75, 'cm^3/(mol*s)'),
                n = -19.12,
                Ea = (32380, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.36e+75, 'cm^3/(mol*s)'),
                n = -18.42,
                Ea = (40880, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.95e+69, 'cm^3/(mol*s)'),
                n = -16.33,
                Ea = (45900, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.13e+48, 'cm^3/(mol*s)'),
                n = -9.83,
                Ea = (39300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 3,
    label = "C6H5 + C2H2 <=> C6H5C2H + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.56e+17, 'cm^3/(mol*s)'),
                n = -1.33,
                Ea = (12690, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+31, 'cm^3/(mol*s)'),
                n = -4.83,
                Ea = (26620, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.38e+33, 'cm^3/(mol*s)'),
                n = -5.39,
                Ea = (32690, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.13e+33, 'cm^3/(mol*s)'),
                n = -5.11,
                Ea = (37820, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

