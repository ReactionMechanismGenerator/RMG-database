#!/usr/bin/env python
# encoding: utf-8

name = "Tranter2010_C6H5recomb"
shortDesc = u""
longDesc = u"""
Robert S. Tranter,*,† Stephen J. Klippenstein,*,† Lawrence B. Harding,† Binod R. Giri,†,§
Xueliang Yang,† and John H. Kiefer‡; Experimental and Theoretical Investigation of 
the Self-Reaction of Phenyl Radicals; J. Phys. Chem. A 2010, 114, 8240–8261
"""
entry(
    index = 1,
    label = "C6H5 + C6H5 <=> biphenyl",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.66e+64, 'cm^3/(mol*s)'),
                n = -14.68,
                Ea = (33.262, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.14e+37, 'cm^3/(mol*s)'),
                n = -7.140,
                Ea = (15.703, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.34e+20, 'cm^3/(mol*s)'),
                n = -2.335,
                Ea = (4.125, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.11e+14, 'cm^3/(mol*s)'),
                n = -0.405,
                Ea = (-0.610, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.09e+12, 'cm^3/(mol*s)'),
                n = 0.036,
                Ea = (-1.7029, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2,
    label = "C6H5 + C6H5 <=> oC12H9 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.51e+76, 'cm^3/(mol*s)'),
                n = -16.8,
                Ea = (78.2679, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.20e+48, 'cm^3/(mol*s)'),
                n = -8.82,
                Ea = (64.1205, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.44e+13, 'cm^3/(mol*s)'),
                n = 0.885,
                Ea = (43.1775, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.76e-12, 'cm^3/(mol*s)'),
                n = 7.72,
                Ea = (27.3212, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.65e-20, 'cm^3/(mol*s)'),
                n = 9.58,
                Ea = (22.8902, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 3,
    label = "C6H5 + C6H5 <=> mC12H9 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.44e+76, 'cm^3/(mol*s)'),
                n = -16.86,
                Ea = (78.3673, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.81e+48, 'cm^3/(mol*s)'),
                n = -8.90,
                Ea = (64.3589, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.44e+13, 'cm^3/(mol*s)'),
                n = 0.868,
                Ea = (43.2172, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.92e-12, 'cm^3/(mol*s)'),
                n = 7.63,
                Ea = (27.5597, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.60e-19, 'cm^3/(mol*s)'),
                n = 9.52,
                Ea = (23.0889, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 4,
    label = "C6H5 + C6H5 <=> pC12H9 + H",
    degeneracy = 1,
    allow_max_rate_violation=True,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.25e+76, 'cm^3/(mol*s)'),
                n = -16.88,
                Ea = (78.5262, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.10e+48, 'cm^3/(mol*s)'),
                n = -8.89,
                Ea = (64.3987, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.13e+35, 'cm^3/(mol*s)'),
                n = 0.826,
                Ea = (43.4557, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.34e-12, 'cm^3/(mol*s)'),
                n = 7.62,
                Ea = (27.6988, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.61e-20, 'cm^3/(mol*s)'),
                n = 9.49,
                Ea = (23.2678, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

#entry(
#    index = 1,
#    label = "C6H5 + C6H5 <=> biphenyl",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (1.55e+14, 'cm^3/(mol*s)'),
#        n = -0.446,
#        Ea = (-0.55, 'kcal/mol'),
#        T0 = (1, 'K'),
#    ),
#)
#
#entry(
#    index = 2,
#    label = "oC12H9 + H <=> biphenyl",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (4.27e+13, 'cm^3/(mol*s)'),
#        n = 0.338,
#        Ea = (-0.158, 'kcal/mol'),
#        T0 = (1, 'K'),
#    ),
#)
#
#entry(
#    index = 3,
#    label = "mC12H9 + H <=> biphenyl",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (1.25e+13, 'cm^3/(mol*s)'),
#        n = 0.284,
#        Ea = (-0.155, 'kcal/mol'),
#        T0 = (1, 'K'),
#    ),
#)
#
#entry(
#    index = 4,
#    label = "pC12H9 + H <=> biphenyl",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (2.78e+13, 'cm^3/(mol*s)'),
#        n = 0.185,
#        Ea = (0.015, 'kcal/mol'),
#        T0 = (1, 'K'),
#    ),
#)

entry(
    index = 5,
    label = "C6H5 + C6H5 <=> C6H6 + oC6H4s",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+03, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (-4.403, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "C6H5 + C6H5 <=> C6H6 + mC6H4s",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(4.88e+02, 'cm^3/(mol*s)'),
        n=2.9,
        Ea=(-2.786, 'kcal/mol'),
        T0=(1, 'K')),
)

entry(
    index = 7,
    label = "C6H5 + C6H5 <=> C6H6 + pC6H4s",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(7.83e+01, 'cm^3/(mol*s)'),
        n=3.13,
        Ea=(0.982, 'kcal/mol'),
        T0=(1, 'K')),
)

entry(
    index = 8,
    label = "C6H5 + C6H5 <=> C6H6 + oC6H4t",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.49e+02, 'cm^3/(mol*s)'),
        n = 3.07,
        Ea = (3.98, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "C6H5 + C6H5 <=> C6H6 + mC6H4t",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(5.26e+02, 'cm^3/(mol*s)'),
        n=3.12,
        Ea=(2.64, 'kcal/mol'),
        T0=(1, 'K')),
)

entry(
    index = 10,
    label = "C6H5 + C6H5 <=> C6H6 + pC6H4t",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(2.43e+01, 'cm^3/(mol*s)'),
        n=3.13,
        Ea=(1.60, 'kcal/mol'),
        T0=(1, 'K')),
)

