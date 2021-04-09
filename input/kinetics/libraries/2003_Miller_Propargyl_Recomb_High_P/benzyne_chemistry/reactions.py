#!/usr/bin/env python
# encoding: utf-8

name = "2010_Tranter_C6H5_recombination"
shortDesc = u""
longDesc = u"""
L. V. Moskaleva, L. K. Madden, and M. C. Lin, Phys. Chem. Chem. Phys., 1999, 1, 3967-3972 covers 100 Torr to 10 atm, 1000 - 3000 K,
C. Xu, M. Braun-Unkhoff, C. Naumann, and P. Frank, Proc. Comb. Ins., 31 (2007) 231-239
M. Derudi, D. Polino, and C. Cavallotti, Phys. Chem. Chem. Phys., 2011, 13, 21308-21318
o-benzyne + benzene  = naphthalene + C2H2, geometry from Comandini et al.,2011 and recalculated at CBS-QB3
o-benzyne + naphthalene = anthracene + C2H2 and recalculated at CBS-QB3

"""
entry(
    index = 1,
    label = "o-benzyne <=> C4H2 + C2H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.13, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.95e+90, '1/s'),
                n = 21.3,
                Ea = (139390, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.07e+85, '1/s'),
                n = -19.6,
                Ea = (138895, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            
            Arrhenius(
                A = (7.89e+75, '1/s'),
                n = -16.8,
                Ea = (134897, 'cal/mol'),
                T0 = (1, 'K'),
            ),

        ],
    ),
)

entry(
    index = 2,
    label = "o-benzyne <=> c-C6H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.0e+15, '1/s'),
        n = 0.00,
        Ea = (98157.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "c-C6H3 <=> C6H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+10, '1/s'),
        n = 0.00,
        Ea = (36044.18, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "phenyl <=> o-benzyne + H",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.3e+12, '1/s'), n=0.62, Ea=(77298.274, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.0e+84, 'cm^3/(mol*s)'),
            n = -18.87,
            Ea = (90100.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.902,
        T3 = (696, 'K'),
        T1 = (358, 'K'),
        T2 = (3856, 'K'),
        efficiencies = {'O=C=O': 2, 'O': 6, '[H][H]': 2, '[He]': 0.67, '[C-]#[O+]': 1.5, '[Ar]': 0.85, 'C': 2, 'C=O': 2.5, 'CC': 3, 'CO': 3},
    ),
    shortDesc = u"""The chemkin file reaction is phenyl <=> o-benzyne + H""",
)

entry(
    index = 5,
    label = "benzene <=> phenyl + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+15, '1/s'),
        n = 0.00,
        Ea = (106304.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "benzene + H <=> phenyl + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.0e+15, 'cm^3/(mol*s)'),
        n = 0.00,
        Ea = (20787.994, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 7,
    label = "toluene <=> benzyl + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.585e+13, '1/s'),
        n = 0.68,
        Ea = (89200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "toluene <=> phenyl + methyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.202e+16, '1/s'),
        n = 0.00,
        Ea = (99800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "benzyl <=> o-benzyne + methyl",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.13, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.042e+135, '1/s'),
                n = -34.08,
                Ea = (169130, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.457e+112, '1/s'),
                n = -27.50,
                Ea = (155360, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.495e+89, '1/s'),
                n = -20.82,
                Ea = (141680, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.129e+55, '1/s'),
                n = -11.23,
                Ea = (116580, 'cal/mol'),
                T0 = (1, 'K'),
            ),

        ],
    ),
)

entry(
    index = 10,
    label = "benzyl <=> C7H6 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.13, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.467e+129, '1/s)'),
                n = -32.57,
                Ea = (162410, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.288e+123, '1/s'),
                n = -30.34,
                Ea = (163830, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.951e+97, '1/s)'),
                n = -22.95,
                Ea = (148280, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.259e+39, '1/s)'),
                n = -6.76,
                Ea = (99710, 'cal/mol'),
                T0 = (1, 'K'),
            ),

        ],
    ),
)

entry(
    index = 11,
    label = "o-benzyne + benzene <=> naphthalene + C2H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-4.80336, 0.429149, -0.074814, -0.00303819],
            [15.2185, 0.782947, -0.123835, -0.00979289],
            [-0.457678, 0.59071, -0.0614154, -0.0172572],
            [-0.388024, 0.360779, 0.00408033, -0.0210338],
            [-0.235647, 0.169358, 0.044246, -0.0169907],
            [-0.123228, 0.0526044, 0.0517873, -0.00773163],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

entry(
    index = 12,
    label = "o-benzyne + naphthalene <=> anthracene + C2H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.37954, -2.06133, -0.0833111, 0.0006373],
            [6.24242, 0.797292, -0.135396, -0.00506145],
            [0.944826, 0.595185, -0.0605872, -0.0183169],
            [-0.16869, 0.358867, 0.0158503, -0.0267162],
            [-0.0850209, 0.169509, 0.059417, -0.0232453],
            [0.0434045, 0.0602714, 0.0630793, -0.0111546],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

