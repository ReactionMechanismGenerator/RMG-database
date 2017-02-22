#!/usr/bin/env python
# encoding: utf-8

name = "new"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "c-C5H5 + CH3 <=> C5H5CH3-5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38482e-08, 'cm^3/(molecule*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "R2 + H <=> C5H5CH3-5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.582e-10, 'cm^3/(molecule*s)'),
        n = -0.1,
        Ea = (0.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "R2 + H <=> C5H5CH3-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7982e-11, 'cm^3/(molecule*s)'),
        n = 0.3,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "R1 + H <=> C5H5CH3-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74338e-12, 'cm^3/(molecule*s)'),
        n = 0.6,
        Ea = (-0.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "R2 + H <=> C5H5CH3-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.50356e-10, 'cm^3/(molecule*s)'),
        n = 0.1,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "R3 + H <=> C5H5CH3-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6921e-12, 'cm^3/(molecule*s)'),
        n = 0.5,
        Ea = (-0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 7,
    label = "R4 + H <=> C5H5CH3-5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.48677e-12, 'cm^3/(molecule*s)'),
        n = 0.6,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "C5H5CH3-5 <=> C5H5CH3-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.0333e+08, 's^-1'),
        n = 1.2,
        Ea = (24.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "C5H5CH3-1 <=> C5H5CH3-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6539e+07, 's^-1'),
        n = 2.1,
        Ea = (25.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "fulvene + H2 <=> C5H5CH3-5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3943e-19, 'cm^3/(molecule*s)'),
        n = 3.9,
        Ea = (81.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "fulvene + H2 <=> C5H5CH3-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0095e-16, 'cm^3/(molecule*s)'),
        n = 1.4,
        Ea = (71, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 12,
    label = "fulvene + H2 <=> C5H5CH3-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6943e-18, 'cm^3/(molecule*s)'),
        n = 1.6,
        Ea = (55.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

