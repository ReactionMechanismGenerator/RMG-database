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
o-benzyne + toluene chemistry calculated at CBS-QB3 by Jeehyun Yang

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
                n = -21.3,
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
                A = (4.467e+129, '1/s'),
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
                A = (2.951e+97, '1/s'),
                n = -22.95,
                Ea = (148280, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.259e+39, '1/s'),
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

entry(
    index = 13,
    label = "o-benzyne + toluene <=> 1_int",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.72348, 0.565451, -0.0890679, -0.000286698],
            [1.30642, 0.982356, -0.126445, -0.00943187],
            [-0.365612, 0.634875, -0.0168072, -0.0229997],
            [-0.318517, 0.287352, 0.0660834, -0.0213021],
            [-0.18726, 0.0713931, 0.0824759, -0.00406585],
            [-0.0994362, -0.0104256, 0.0553901, 0.0121047],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

entry(
    index = 14,
    label = "o-benzyne + toluene <=> 2_int",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.25514, 0.610504, -0.0923716, -0.000105478],
            [1.00347, 1.04096, -0.123184, -0.0108117],
            [-0.407055, 0.633034, 0.000644846, -0.025122],
            [-0.319057, 0.250903, 0.0813071, -0.0191626],
            [-0.17554, 0.038059, 0.0826312, 0.00280639],
            [-0.0888865, -0.0286766, 0.0453284, 0.0185459],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

entry(
    index = 15,
    label = "1_int <=> 1_methylnaphthalene + C2H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.71294, 0.483827, -0.0711982, -0.00255115],
            [14.4658, 0.874917, -0.112827, -0.008895],
            [-0.599734, 0.640765, -0.0427971, -0.0159058],
            [-0.473783, 0.366792, 0.0268687, -0.0177847],
            [-0.278247, 0.147215, 0.0640666, -0.0109785],
            [-0.141234, 0.0224159, 0.0639693, 1.82896e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

entry(
    index = 16,
    label = "o-benzyne + toluene <=> 1_methylnaphthalene + C2H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.07284, -1.79241, -0.108156, -0.000834904],
            [5.53316, 1.15017, -0.127063, -0.0153905],
            [0.456323, 0.586388, 0.0378077, -0.0297213],
            [-0.151644, 0.135793, 0.115515, -0.0136528],
            [0.00915519, -0.0325605, 0.0798014, 0.0163935],
            [0.0587599, -0.0308923, 0.0187618, 0.0272439],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

entry(
    index = 17,
    label = "2_int <=> 2_methylnaphthalene + C2H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.13277, 0.523916, -0.0726087, -0.00284549],
            [13.7272, 0.93577, -0.110781, -0.00983849],
            [-0.639543, 0.657975, -0.0317121, -0.0167165],
            [-0.486533, 0.345205, 0.0411463, -0.0164268],
            [-0.270134, 0.110146, 0.0724809, -0.00637898],
            [-0.126793, -0.0093407, 0.0632288, 0.00628277],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

entry(
    index = 18,
    label = "o-benzyne + toluene <=> 2_methylnaphthalene + C2H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.67636, -1.74082, -0.112673, -0.000624136],
            [5.15737, 1.20088, -0.120001, -0.0173884],
            [0.40755, 0.554384, 0.0608643, -0.0306345],
            [-0.121763, 0.0858761, 0.123998, -0.00784121],
            [0.032293, -0.0507948, 0.0659099, 0.0231697],
            [0.0546236, -0.0296938, 0.00233176, 0.0275718],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

entry(
    index = 19,
    label = "2_int <=> propyne + naphthalene",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.02241, 0.518484, -0.0716475, -0.00291297],
            [13.4597, 0.928207, -0.11001, -0.00977314],
            [-0.662712, 0.657506, -0.0331318, -0.0163912],
            [-0.490256, 0.350136, 0.0387649, -0.0162849],
            [-0.272667, 0.115872, 0.0710952, -0.00677564],
            [-0.128693, -0.00603158, 0.0635545, 0.00553699],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

entry(
    index = 20,
    label = "o-benzyne + toluene <=> naphthalene + propyne",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.65295, -1.74551, -0.111981, -0.000605724],
            [5.01626, 1.19667, -0.120277, -0.0171362],
            [0.378409, 0.558207, 0.0588192, -0.0305253],
            [-0.12844, 0.0910778, 0.123148, -0.00839402],
            [0.030365, -0.0493118, 0.0670675, 0.0225538],
            [0.0547404, -0.0307123, 0.00368741, 0.0276097],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.00133322, 'bar'),
        Pmax = (133.322, 'bar'),
    ),
)

