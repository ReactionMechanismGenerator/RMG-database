#!/usr/bin/env python
# encoding: utf-8

name = "Chernov"
shortDesc = u""
longDesc = u"""
From: Chernov, V.; Thomson, M. J.; Dworkin, S. B.; Slavinskaya, N. A.; Riedel, U., 
Soot formation with C1 and C2 fuels using an improved chemical mechanism for PAH growth. Combust. Flame 2014, 161, 592-601
"""
entry(
    index = 1,
    label = "H2 + O2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0.47,
        Ea = (292013, 'J/mol'),
        T0 = (1, 'K'),
        comment = '1',
    ),
    longDesc = 
u"""
1
""",
)

entry(
    index = 2,
    label = "H + H + AR <=> H2 + AR",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.53e+17, 'cm^6/(mol^2*s)'),
        n = -1,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '2',
    ),
    longDesc = 
u"""
2
""",
)

entry(
    index = 3,
    label = "H + H + H2 <=> H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+17, 'cm^6/(mol^2*s)'),
        n = -0.6,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '3',
    ),
    longDesc = 
u"""
3
""",
)

entry(
    index = 4,
    label = "H + H + N2 <=> H2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+18, 'cm^6/(mol^2*s)'),
        n = -1.3,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '4',
    ),
    longDesc = 
u"""
4
""",
)

entry(
    index = 5,
    label = "H + H + H2O <=> H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+19, 'cm^6/(mol^2*s)'),
        n = -1,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '5',
    ),
    longDesc = 
u"""
5
""",
)

entry(
    index = 6,
    label = "H + H + H <=> H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+15, 'cm^6/(mol^2*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '6',
    ),
    longDesc = 
u"""
6
""",
)

entry(
    index = 7,
    label = "H + H <=> H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7.47e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3.75, 'O': 0, '[H][H]': 0, '[H]': 0, 'N#N': 0, '[C-]#[O+]': 1.87, '[Ar]': 0},
        comment = '7',
    ),
    longDesc = 
u"""
7
""",
)

entry(
    index = 8,
    label = "H2 + O <=> OH + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3.82e+12, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (33257.9, 'J/mol'),
                T0 = (1, 'K'),
                comment = 'AR/0/ CO2/3.75/ CO/1.87/ H2O/0/ H2/0/ H/0/ HE/0.87/ N2/0/\n8',
            ),
            Arrhenius(
                A = (8.79e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (80234.7, 'J/mol'),
                T0 = (1, 'K'),
                comment = '9',
            ),
        ],
    ),
)

entry(
    index = 9,
    label = "OH + H2 <=> H2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (14467.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '10',
    ),
    longDesc = 
u"""
10
""",
)

entry(
    index = 10,
    label = "OH + OH <=> H2O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.23e+13, 'cm^3/(mol*s)'), n=-0.37, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(5.53e+19, 'cm^6/(mol^2*s)'), n=-0.76, Ea=(0, 'J/mol'), T0=(1, 'K')),
        alpha = 1,
        T3 = (1, 'K'),
        T1 = (1, 'K'),
        T2 = (1040, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, 'C=C': 3, '[Ar]': 0.2},
        comment = '11',
    ),
    longDesc = 
u"""
11
""",
)

entry(
    index = 11,
    label = "H + O2 <=> OH + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+14, 'cm^3/(mol*s)'),
        n = -0.097,
        Ea = (62857.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '12',
    ),
    longDesc = 
u"""
12
""",
)

entry(
    index = 12,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.66e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.75e+19, 'cm^6/(mol^2*s)'), n=-1.23, Ea=(0, 'J/mol'), T0=(1, 'K')),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'O=C=O': 1.06, 'O': 0, '[H][H]': 1.5, '[O][O]': 0, 'N#N': 0, '[Ar]': 0},
        comment = '13',
    ),
    longDesc = 
u"""
13
""",
)

entry(
    index = 13,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.4e+13, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-7480.45, 'J/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[C-]#[O+]': 1.87, '[H][H]': 2.5, 'O=C=O': 3.75, 'O': 16.25, '[Ar]': 0.87},
        comment = 'BATH GAS REACTIONS COMMENTED OUT BY CONNIE\n14\nH+O2(+HE) = HO2(+HE) 4.660E+12 0.4400 0.00\nLOW / 6.130E+18 -1.20 0.00 /\nTROE / 5.0000E-01 1.0000E-30 1.0000E+30 /\n15\nH+O2(+AR) = HO2(+AR) 4.660E+12 0.4400 0.00\nLOW / 7.430E+18 -1.20 0.00 /\nTROE / 5.0000E-01 1.0000E-30 1.0000E+30 /\n16\nH+O2(+O2) = HO2(+O2) 4.660E+12 0.4400 0.00\nLOW / 5.690E+18 -1.09 0.00 /\nTROE / 5.0000E-01 1.0000E-30 1.0000E+30 /\n17\nH+O2(+N2) = HO2(+N2) 4.660E+12 0.4400 0.00\nLOW / 1.750E+19 -1.23 0.00 /\nTROE / 5.0000E-01 1.0000E-30 1.0000E+30 /\n18\nH+O2(+H2O) = HO2(+H2O) 9.020E+12 0.2000 0.00\nLOW / 3.670E+19 -1.00 0.00 /\nTROE / 8.0000E-01 1.0000E-30 1.0000E+30 /\n19',
    ),
    longDesc = 
u"""
BATH GAS REACTIONS COMMENTED OUT BY CONNIE
14
H+O2(+HE) = HO2(+HE) 4.660E+12 0.4400 0.00
LOW / 6.130E+18 -1.20 0.00 /
TROE / 5.0000E-01 1.0000E-30 1.0000E+30 /
15
H+O2(+AR) = HO2(+AR) 4.660E+12 0.4400 0.00
LOW / 7.430E+18 -1.20 0.00 /
TROE / 5.0000E-01 1.0000E-30 1.0000E+30 /
16
H+O2(+O2) = HO2(+O2) 4.660E+12 0.4400 0.00
LOW / 5.690E+18 -1.09 0.00 /
TROE / 5.0000E-01 1.0000E-30 1.0000E+30 /
17
H+O2(+N2) = HO2(+N2) 4.660E+12 0.4400 0.00
LOW / 1.750E+19 -1.23 0.00 /
TROE / 5.0000E-01 1.0000E-30 1.0000E+30 /
18
H+O2(+H2O) = HO2(+H2O) 9.020E+12 0.2000 0.00
LOW / 3.670E+19 -1.00 0.00 /
TROE / 8.0000E-01 1.0000E-30 1.0000E+30 /
19
""",
)

entry(
    index = 14,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.511e+13, 'cm^3/(mol*s)'),
            n = 0.234,
            Ea = (-478.082, 'J/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.533e+21, 'cm^6/(mol^2*s)'),
            n = -1.81,
            Ea = (2086.93, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.27,
        T3 = (1e+33, 'K'),
        T1 = (1e+33, 'K'),
        efficiencies = {'[H][H]': 2.5, 'O=C=O': 3.75, 'O': 16.39, '[Ar]': 0},
        comment = 'H2/2.5/ H2O/16.25/ AR/0.87/ HE/0.87/ CO/1.87/ CO2/3.75/\n20',
    ),
    longDesc = 
u"""
H2/2.5/ H2O/16.25/ AR/0.87/ HE/0.87/ CO/1.87/ CO2/3.75/
20
""",
)

entry(
    index = 15,
    label = "H + O <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7.73e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 7.5, 'O=C=O': 3.75, 'CC': 7.5, 'O': 16.25, '[H][H]': 2.5, '[C-]#[O+]': 1.87, '[Ar]': 0.87},
        comment = 'H2/2.5/ H2O/16.39/ HE/0.87/ AR/0/ CO2/3.75/\nCOMMENTED OUT BY CONNIE\n21\nH+OH(+AR) = H2O(+AR) 2.511E+13 0.2340 -57.50\nLOW / 3.114E+20 -1.51 185.00 /\nTROE / 2.8000E-01 1.0000E+33 1.0000E+33 /\n22',
    ),
    longDesc = 
u"""
H2/2.5/ H2O/16.39/ HE/0.87/ AR/0/ CO2/3.75/
COMMENTED OUT BY CONNIE
21
H+OH(+AR) = H2O(+AR) 2.511E+13 0.2340 -57.50
LOW / 3.114E+20 -1.51 185.00 /
TROE / 2.8000E-01 1.0000E+33 1.0000E+33 /
22
""",
)

entry(
    index = 16,
    label = "H + HO2 <=> H2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8563.91, 'J/mol'),
        T0 = (1, 'K'),
        comment = 'H2/2.5/ H2O/16.25/ AR/0.87/ HE/0.87/ CO/1.87/ CO2/3.75/ CH4/7.5/ C2H6/7.5/\n23',
    ),
    longDesc = 
u"""
H2/2.5/ H2O/16.25/ AR/0.87/ HE/0.87/ CO/1.87/ CO2/3.75/ CH4/7.5/ C2H6/7.5/
23
""",
)

entry(
    index = 17,
    label = "H + HO2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5820.13, 'J/mol'),
        T0 = (1, 'K'),
        comment = '24',
    ),
    longDesc = 
u"""
24
""",
)

entry(
    index = 18,
    label = "H + HO2 <=> H2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.44e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '25',
    ),
    longDesc = 
u"""
25
""",
)

entry(
    index = 19,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15710.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '26',
    ),
    longDesc = 
u"""
26
""",
)

entry(
    index = 20,
    label = "H2O2 + H <=> OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14970.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '27',
    ),
    longDesc = 
u"""
27
""",
)

entry(
    index = 21,
    label = "OH + OH <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33500, 'cm^3/(mol*s)'),
        n = 2.42,
        Ea = (-8065.04, 'J/mol'),
        T0 = (1, 'K'),
        comment = '28',
    ),
    longDesc = 
u"""
28
""",
)

entry(
    index = 22,
    label = "OH + HO2 <=> H2O + O2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (9.27e+15, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (73250.5, 'J/mol'),
                T0 = (1, 'K'),
                comment = '29',
            ),
            Arrhenius(
                A = (2.89e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-2078.62, 'J/mol'),
                T0 = (1, 'K'),
                comment = '30',
            ),
        ],
    ),
)

entry(
    index = 23,
    label = "H2O2 + OH <=> H2O + HO2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.64e+18, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (123054, 'J/mol'),
                T0 = (1, 'K'),
                comment = '31',
            ),
            Arrhenius(
                A = (1.93e+12, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (1787.61, 'J/mol'),
                T0 = (1, 'K'),
                comment = '32',
            ),
        ],
    ),
)

entry(
    index = 24,
    label = "O + HO2 <=> O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1862.44, 'J/mol'),
        T0 = (1, 'K'),
        comment = '33',
    ),
    longDesc = 
u"""
33
""",
)

entry(
    index = 25,
    label = "H2O2 + O <=> OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16628.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '34',
    ),
    longDesc = 
u"""
34
""",
)

entry(
    index = 26,
    label = "HO2 + HO2 <=> H2O2 + O2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (4.22e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (50142.8, 'J/mol'),
                T0 = (1, 'K'),
                comment = '35',
            ),
            Arrhenius(
                A = (1.32e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-6820.36, 'J/mol'),
                T0 = (1, 'K'),
                comment = '36',
            ),
        ],
    ),
)

entry(
    index = 27,
    label = "O2 + CO <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196911, 'J/mol'),
        T0 = (1, 'K'),
        comment = '37',
    ),
    longDesc = 
u"""
37
""",
)

entry(
    index = 28,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.01e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (66931.5, 'J/mol'),
                T0 = (1, 'K'),
                comment = '38',
            ),
            Arrhenius(
                A = (9.03e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (19123.3, 'J/mol'),
                T0 = (1, 'K'),
                comment = '39',
            ),
            Arrhenius(
                A = (1.01e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (249.434, 'J/mol'),
                T0 = (1, 'K'),
                comment = '40',
            ),
        ],
    ),
)

entry(
    index = 29,
    label = "CO + O <=> CO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.17e+14, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (12560.7, 'J/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 3.75, 'CC': 3, 'O': 16.25, '[H][H]': 2.5, '[C-]#[O+]': 1.87, '[Ar]': 0.87},
        comment = '41',
    ),
    longDesc = 
u"""
41
""",
)

entry(
    index = 30,
    label = "CO + HO2 <=> CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (320000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (75079.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = 'H2/2.5/ CO/1.87/ CO2/3.75/ H2O/16.25/ AR/0.87/ HE/0.87/ CH4/3/ C2H6/3/\n42',
    ),
    longDesc = 
u"""
H2/2.5/ CO/1.87/ CO2/3.75/ H2O/16.25/ AR/0.87/ HE/0.87/ CH4/3/ C2H6/3/
42
""",
)

entry(
    index = 31,
    label = "HCO + O2 <=> HO2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+10, 'cm^3/(mol*s)'),
        n = 0.68,
        Ea = (-1962.22, 'J/mol'),
        T0 = (1, 'K'),
        comment = '43',
    ),
    longDesc = 
u"""
43
""",
)

entry(
    index = 32,
    label = "HCO + O2 <=> OH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+10, 'cm^3/(mol*s)'),
        n = 0.68,
        Ea = (-1962.22, 'J/mol'),
        T0 = (1, 'K'),
        comment = '44',
    ),
    longDesc = 
u"""
44
""",
)

entry(
    index = 33,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '45',
    ),
    longDesc = 
u"""
45
""",
)

entry(
    index = 34,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '46',
    ),
    longDesc = 
u"""
46
""",
)

entry(
    index = 35,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '47',
    ),
    longDesc = 
u"""
47
""",
)

entry(
    index = 36,
    label = "HCO + OH <=> H2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '48',
    ),
    longDesc = 
u"""
48
""",
)

entry(
    index = 37,
    label = "HCO + HO2 <=> CO2 + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '49',
    ),
    longDesc = 
u"""
49
""",
)

entry(
    index = 38,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(65933.8, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'[C-]#[O+]': 1.87, '[H][H]': 2.5, 'O=C=O': 3.75, 'O': 16.25, '[Ar]': 0.87},
        comment = '50',
    ),
    longDesc = 
u"""
50
""",
)

entry(
    index = 39,
    label = "HCCO + O2 <=> CO + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3580.21, 'J/mol'),
        T0 = (1, 'K'),
        comment = 'H2/2.5/ CO/1.87/ CO2/3.75/ H2O/16.25/ AR/0.87/ HE/0.87/\n51',
    ),
    longDesc = 
u"""
H2/2.5/ CO/1.87/ CO2/3.75/ H2O/16.25/ AR/0.87/ HE/0.87/
51
""",
)

entry(
    index = 40,
    label = "HCCO + O2 <=> HCO + CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3575.22, 'J/mol'),
        T0 = (1, 'K'),
        comment = '52',
    ),
    longDesc = 
u"""
52
""",
)

entry(
    index = 41,
    label = "HCCO + O2 <=> CO2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3575.22, 'J/mol'),
        T0 = (1, 'K'),
        comment = '53',
    ),
    longDesc = 
u"""
53
""",
)

entry(
    index = 42,
    label = "HCCO + O2 <=> CO2 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '54',
    ),
    longDesc = 
u"""
54
""",
)

entry(
    index = 43,
    label = "HCCO + OH <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '55',
    ),
    longDesc = 
u"""
55
""",
)

entry(
    index = 44,
    label = "HCCO + OH <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '56',
    ),
    longDesc = 
u"""
56
""",
)

entry(
    index = 45,
    label = "HCCO + O <=> H + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '57',
    ),
    longDesc = 
u"""
57
""",
)

entry(
    index = 46,
    label = "O2 + CH <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '58',
    ),
    longDesc = 
u"""
58
""",
)

entry(
    index = 47,
    label = "O2 + CH <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '59',
    ),
    longDesc = 
u"""
59
""",
)

entry(
    index = 48,
    label = "CO + CH <=> HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.77e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-7150.45, 'J/mol'),
        T0 = (1, 'K'),
        comment = '60',
    ),
    longDesc = 
u"""
60
""",
)

entry(
    index = 49,
    label = "CO2 + CH <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2870.16, 'J/mol'),
        T0 = (1, 'K'),
        comment = '61',
    ),
    longDesc = 
u"""
61
""",
)

entry(
    index = 50,
    label = "CH + O <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '62',
    ),
    longDesc = 
u"""
62
""",
)

entry(
    index = 51,
    label = "CH + OH <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '63',
    ),
    longDesc = 
u"""
63
""",
)

entry(
    index = 52,
    label = "H2 + CH2(S) <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '64',
    ),
    longDesc = 
u"""
64
""",
)

entry(
    index = 53,
    label = "CH4 + O2 <=> CH3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (238053, 'J/mol'),
        T0 = (1, 'K'),
        comment = '65',
    ),
    longDesc = 
u"""
65
""",
)

entry(
    index = 54,
    label = "CH4 + C <=> CH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (100486, 'J/mol'),
        T0 = (1, 'K'),
        comment = '66',
    ),
    longDesc = 
u"""
66
""",
)

entry(
    index = 55,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (45064.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '67',
    ),
    longDesc = 
u"""
67
""",
)

entry(
    index = 56,
    label = "CH4 + CH <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1660.07, 'J/mol'),
        T0 = (1, 'K'),
        comment = '68',
    ),
    longDesc = 
u"""
68
""",
)

entry(
    index = 57,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (42002.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '69',
    ),
    longDesc = 
u"""
69
""",
)

entry(
    index = 58,
    label = "CH4 + CH2(S) <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '70',
    ),
    longDesc = 
u"""
70
""",
)

entry(
    index = 59,
    label = "CH4 + C2H <=> CH3 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '71',
    ),
    longDesc = 
u"""
71
""",
)

entry(
    index = 60,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (35502, 'J/mol'),
        T0 = (1, 'K'),
        comment = '72',
    ),
    longDesc = 
u"""
72
""",
)

entry(
    index = 61,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.57e+07, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (11640.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '73',
    ),
    longDesc = 
u"""
73
""",
)

entry(
    index = 62,
    label = "C2H2 + C2H2 <=> H2CCCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (242014, 'J/mol'),
        T0 = (1, 'K'),
        comment = '74',
    ),
    longDesc = 
u"""
74
""",
)

entry(
    index = 63,
    label = "C2H2 + O2 <=> C2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (312018, 'J/mol'),
        T0 = (1, 'K'),
        comment = '75',
    ),
    longDesc = 
u"""
75
""",
)

entry(
    index = 64,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.43e+12, 'cm^3/(mol*s)'), n=0, Ea=(10810.6, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.43e+18, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (6150.38, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1, 'K'),
        T1 = (1, 'K'),
        T2 = (1231, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.35},
        comment = '76\nH2+C2H = C2H2+H 1.080E+13 0.0000 1089.73\n77',
    ),
    longDesc = 
u"""
76
H2+C2H = C2H2+H 1.080E+13 0.0000 1089.73
77
""",
)

entry(
    index = 65,
    label = "C2H2 + CH <=> C2H + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-510.01, 'J/mol'),
        T0 = (1, 'K'),
        comment = '78\nRxn 78 commented out because reverse rate coefficient is above Z',
    ),
    longDesc = 
u"""
78
Rxn 78 commented out because reverse rate coefficient is above Z
""",
)

entry(
    index = 66,
    label = "C2H2 + CH2 <=> C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (27691.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '79',
    ),
    longDesc = 
u"""
79
""",
)

entry(
    index = 67,
    label = "C2H2 + CH2(S) <=> H2CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '80',
    ),
    longDesc = 
u"""
80
""",
)

entry(
    index = 68,
    label = "C2H2 + C2H <=> C4H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '81',
    ),
    longDesc = 
u"""
81
""",
)

entry(
    index = 69,
    label = "C2H2 + OH <=> C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (54043.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '82',
    ),
    longDesc = 
u"""
82
""",
)

entry(
    index = 70,
    label = "C2H2 <=> C2H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.14e+17, 'cm^3/(mol*s)'), n=0, Ea=(447025, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.35},
        comment = '83\nReation 83 commented out because k > Z for T<1200 K',
    ),
    longDesc = 
u"""
83
Reation 83 commented out because k > Z for T<1200 K
""",
)

entry(
    index = 71,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (3.97e+09, 'cm^3/(mol*s)'),
            n = 1.28,
            Ea = (5400.33, 'J/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.35e+19, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (3160.16, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.76,
        T3 = (40, 'K'),
        T1 = (1025, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.35},
        comment = '84',
    ),
    longDesc = 
u"""
84
""",
)

entry(
    index = 72,
    label = "C2H4 + CH <=> C3H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1440.07, 'J/mol'),
        T0 = (1, 'K'),
        comment = '85',
    ),
    longDesc = 
u"""
85
""",
)

entry(
    index = 73,
    label = "C2H4 + CH2(S) <=> C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '86',
    ),
    longDesc = 
u"""
86
""",
)

entry(
    index = 74,
    label = "C2H4 + CH3 <=> CH4 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.16e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46562.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '87',
    ),
    longDesc = 
u"""
87
""",
)

entry(
    index = 75,
    label = "C2H4 + O <=> H + CH2HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.74e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (750.049, 'J/mol'),
        T0 = (1, 'K'),
        comment = '88',
    ),
    longDesc = 
u"""
88
""",
)

entry(
    index = 76,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.13e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (750.049, 'J/mol'),
        T0 = (1, 'K'),
        comment = '89',
    ),
    longDesc = 
u"""
89
""",
)

entry(
    index = 77,
    label = "C2H4 + O <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (680000, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (750.049, 'J/mol'),
        T0 = (1, 'K'),
        comment = '90',
    ),
    longDesc = 
u"""
90
""",
)

entry(
    index = 78,
    label = "C2H4 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(9.97e+16, 'cm^3/(mol*s)'), n=0, Ea=(299337, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.35},
        comment = '91',
    ),
    longDesc = 
u"""
91
""",
)

entry(
    index = 79,
    label = "C2H4 <=> C2H3 + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7.4e+17, 'cm^3/(mol*s)'), n=0, Ea=(404113, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.2},
        comment = '92',
    ),
    longDesc = 
u"""
92
""",
)

entry(
    index = 80,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (31011.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '93',
    ),
    longDesc = 
u"""
93
""",
)

entry(
    index = 81,
    label = "C2H6 + CH <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1100.09, 'J/mol'),
        T0 = (1, 'K'),
        comment = '94',
    ),
    longDesc = 
u"""
94
""",
)

entry(
    index = 82,
    label = "C2H6 + CH2(S) <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '95',
    ),
    longDesc = 
u"""
95
""",
)

entry(
    index = 83,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e-07, 'cm^3/(mol*s)'),
        n = 6,
        Ea = (25301.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '96',
    ),
    longDesc = 
u"""
96
""",
)

entry(
    index = 84,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (24281.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '97',
    ),
    longDesc = 
u"""
97
""",
)

entry(
    index = 85,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3620.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '98',
    ),
    longDesc = 
u"""
98
""",
)

entry(
    index = 86,
    label = "C2H6 + HO2 <=> H2O2 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (85634.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '99',
    ),
    longDesc = 
u"""
99
""",
)

entry(
    index = 87,
    label = "C4H2 + O <=> C3H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.89e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5640.29, 'J/mol'),
        T0 = (1, 'K'),
        comment = '100',
    ),
    longDesc = 
u"""
100
""",
)

entry(
    index = 88,
    label = "C4H2 + OH <=> C3H2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.68e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1710.12, 'J/mol'),
        T0 = (1, 'K'),
        comment = '101',
    ),
    longDesc = 
u"""
101
""",
)

entry(
    index = 89,
    label = "O2 + CH2O <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (170120, 'J/mol'),
        T0 = (1, 'K'),
        comment = '102',
    ),
    longDesc = 
u"""
102
""",
)

entry(
    index = 90,
    label = "O2 + C <=> CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16710.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '103',
    ),
    longDesc = 
u"""
103
""",
)

entry(
    index = 91,
    label = "O2 + CH2 <=> CO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6240.34, 'J/mol'),
        T0 = (1, 'K'),
        comment = '104',
    ),
    longDesc = 
u"""
104
""",
)

entry(
    index = 92,
    label = "O2 + CH2 <=> CO2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6240.34, 'J/mol'),
        T0 = (1, 'K'),
        comment = '105',
    ),
    longDesc = 
u"""
105
""",
)

entry(
    index = 93,
    label = "O2 + CH2 <=> CO + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.15e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6240.34, 'J/mol'),
        T0 = (1, 'K'),
        comment = '106',
    ),
    longDesc = 
u"""
106
""",
)

entry(
    index = 94,
    label = "O2 + CH2 <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.48e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6240.34, 'J/mol'),
        T0 = (1, 'K'),
        comment = '107',
    ),
    longDesc = 
u"""
107
""",
)

entry(
    index = 95,
    label = "O2 + CH2 <=> CH2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6240.34, 'J/mol'),
        T0 = (1, 'K'),
        comment = '108',
    ),
    longDesc = 
u"""
108
""",
)

entry(
    index = 96,
    label = "O2 + CH2(S) <=> CO + OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.13e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '109',
    ),
    longDesc = 
u"""
109
""",
)

entry(
    index = 97,
    label = "O2 + CH3 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (37422.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '110',
    ),
    longDesc = 
u"""
110
""",
)

entry(
    index = 98,
    label = "O2 + C2H <=> HCCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '111',
    ),
    longDesc = 
u"""
111
""",
)

entry(
    index = 99,
    label = "O2 + C2H <=> CO2 + CH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '112',
    ),
    longDesc = 
u"""
112
""",
)

entry(
    index = 100,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-9150.49, 'J/mol'),
        T0 = (1, 'K'),
        comment = '113',
    ),
    longDesc = 
u"""
113
""",
)

entry(
    index = 101,
    label = "O2 + C3H2 <=> HCO + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '114',
    ),
    longDesc = 
u"""
114
""",
)

entry(
    index = 102,
    label = "O2 + H2CCCH <=> CH2CO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12000.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '115',
    ),
    longDesc = 
u"""
115
""",
)

entry(
    index = 103,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7320.39, 'J/mol'),
        T0 = (1, 'K'),
        comment = '116',
    ),
    longDesc = 
u"""
116
""",
)

entry(
    index = 104,
    label = "O2 + CH2OH <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.57e+15, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '117',
    ),
    longDesc = 
u"""
117
""",
)

entry(
    index = 105,
    label = "CO2 + CH2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '118',
    ),
    longDesc = 
u"""
118
""",
)

entry(
    index = 106,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+08, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (9060.53, 'J/mol'),
        T0 = (1, 'K'),
        comment = '119',
    ),
    longDesc = 
u"""
119
""",
)

entry(
    index = 107,
    label = "CH2O + CH <=> CH2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2160.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '120',
    ),
    longDesc = 
u"""
120
""",
)

entry(
    index = 108,
    label = "CH2O + CH3 <=> CH4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.83e-08, 'cm^3/(mol*s)'),
        n = 6.1,
        Ea = (8230.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '121',
    ),
    longDesc = 
u"""
121
""",
)

entry(
    index = 109,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.16e+11, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (11560.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '122',
    ),
    longDesc = 
u"""
122
""",
)

entry(
    index = 110,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-1870.09, 'J/mol'),
        T0 = (1, 'K'),
        comment = '123',
    ),
    longDesc = 
u"""
123
""",
)

entry(
    index = 111,
    label = "CH2O + HO2 <=> H2O2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (54713.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '124',
    ),
    longDesc = 
u"""
124
""",
)

entry(
    index = 112,
    label = "CH2O <=> HCO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.4e+36, 'cm^3/(mol*s)'),
            n = -5.54,
            Ea = (404603, 'J/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.2},
        comment = '125',
    ),
    longDesc = 
u"""
125
""",
)

entry(
    index = 113,
    label = "CH2O <=> H2 + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.26e+36, 'cm^3/(mol*s)'),
            n = -5.54,
            Ea = (404603, 'J/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.2},
        comment = '126',
    ),
    longDesc = 
u"""
126
""",
)

entry(
    index = 114,
    label = "CH2CO + H <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14130.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '127',
    ),
    longDesc = 
u"""
127
""",
)

entry(
    index = 115,
    label = "CH2CO + O <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5650.35, 'J/mol'),
        T0 = (1, 'K'),
        comment = '128',
    ),
    longDesc = 
u"""
128
""",
)

entry(
    index = 116,
    label = "CH2CO + O <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5650.35, 'J/mol'),
        T0 = (1, 'K'),
        comment = '129',
    ),
    longDesc = 
u"""
129
""",
)

entry(
    index = 117,
    label = "CH2CO + O <=> HCO + H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5650.35, 'J/mol'),
        T0 = (1, 'K'),
        comment = '130',
    ),
    longDesc = 
u"""
130
""",
)

entry(
    index = 118,
    label = "CH2CO + O <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5650.35, 'J/mol'),
        T0 = (1, 'K'),
        comment = '131',
    ),
    longDesc = 
u"""
131
""",
)

entry(
    index = 119,
    label = "CH2CO + OH <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '132',
    ),
    longDesc = 
u"""
132
""",
)

entry(
    index = 120,
    label = "CH2CO + OH <=> CH2OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.68e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '133',
    ),
    longDesc = 
u"""
133
""",
)

entry(
    index = 121,
    label = "CH2CO <=> CH2 + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.57e+15, 'cm^3/(mol*s)'), n=0, Ea=(241044, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.2},
        comment = '134',
    ),
    longDesc = 
u"""
134
""",
)

entry(
    index = 122,
    label = "C + CH2 <=> C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '135',
    ),
    longDesc = 
u"""
135
""",
)

entry(
    index = 123,
    label = "C + CH3 <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '136',
    ),
    longDesc = 
u"""
136
""",
)

entry(
    index = 124,
    label = "C + OH <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '137',
    ),
    longDesc = 
u"""
137
""",
)

entry(
    index = 125,
    label = "H + CH <=> C + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '138',
    ),
    longDesc = 
u"""
138
""",
)

entry(
    index = 126,
    label = "H + CH2 <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-7480.45, 'J/mol'),
        T0 = (1, 'K'),
        comment = '139',
    ),
    longDesc = 
u"""
139
""",
)

entry(
    index = 127,
    label = "H + CH2(S) <=> CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '140',
    ),
    longDesc = 
u"""
140
""",
)

entry(
    index = 128,
    label = "H + C2H3 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '141',
    ),
    longDesc = 
u"""
141
""",
)

entry(
    index = 129,
    label = "CH3 + CH3 <=> C2H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (56538.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '142',
    ),
    longDesc = 
u"""
142
""",
)

entry(
    index = 130,
    label = "H + CH3O <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '143',
    ),
    longDesc = 
u"""
143
""",
)

entry(
    index = 131,
    label = "H + CH2OH <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '144',
    ),
    longDesc = 
u"""
144
""",
)

entry(
    index = 132,
    label = "H + CH2OH <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.08e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '145',
    ),
    longDesc = 
u"""
145
""",
)

entry(
    index = 133,
    label = "H + HCCO <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '146',
    ),
    longDesc = 
u"""
146
""",
)

entry(
    index = 134,
    label = "CH + CH2 <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '147',
    ),
    longDesc = 
u"""
147
""",
)

entry(
    index = 135,
    label = "CH + CH3 <=> C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '148',
    ),
    longDesc = 
u"""
148
""",
)

entry(
    index = 136,
    label = "CH + C2H3 <=> CH2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '149',
    ),
    longDesc = 
u"""
149
""",
)

entry(
    index = 137,
    label = "CH + HCCO <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '150',
    ),
    longDesc = 
u"""
150
""",
)

entry(
    index = 138,
    label = "CH2 + CH2 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3330.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '151',
    ),
    longDesc = 
u"""
151
""",
)

entry(
    index = 139,
    label = "CH2 + CH2 <=> C2H2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3330.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '152',
    ),
    longDesc = 
u"""
152
""",
)

entry(
    index = 140,
    label = "CH2 + CH3 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '153',
    ),
    longDesc = 
u"""
153
""",
)

entry(
    index = 141,
    label = "CH2 + C2H3 <=> C2H2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '154',
    ),
    longDesc = 
u"""
154
""",
)

entry(
    index = 142,
    label = "CH2 + O <=> CO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '155',
    ),
    longDesc = 
u"""
155
""",
)

entry(
    index = 143,
    label = "CH2 + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '156',
    ),
    longDesc = 
u"""
156
""",
)

entry(
    index = 144,
    label = "CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '157',
    ),
    longDesc = 
u"""
157
""",
)

entry(
    index = 145,
    label = "CH2 + HCO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '158',
    ),
    longDesc = 
u"""
158
""",
)

entry(
    index = 146,
    label = "CH2 + HCCO <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '159',
    ),
    longDesc = 
u"""
159
""",
)

entry(
    index = 147,
    label = "CH2 + HCCO <=> C2H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8370.51, 'J/mol'),
        T0 = (1, 'K'),
        comment = '160',
    ),
    longDesc = 
u"""
160
""",
)

entry(
    index = 148,
    label = "CH2(S) <=> CH2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.51e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 0.48, 'O=C=O': 1.5, 'CC': 1.44, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, 'C=C': 1.6, 'C#C': 3.2, '[Ar]': 0.2},
        comment = '161',
    ),
    longDesc = 
u"""
161
""",
)

entry(
    index = 149,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '162',
    ),
    longDesc = 
u"""
162
""",
)

entry(
    index = 150,
    label = "CH3 + OH <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11640.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '163',
    ),
    longDesc = 
u"""
163
""",
)

entry(
    index = 151,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '164',
    ),
    longDesc = 
u"""
164
""",
)

entry(
    index = 152,
    label = "CH3 + HCO <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '165',
    ),
    longDesc = 
u"""
165
""",
)

entry(
    index = 153,
    label = "CH3 <=> CH2 + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.91e+16, 'cm^3/(mol*s)'), n=0, Ea=(379162, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.4},
        comment = '166',
    ),
    longDesc = 
u"""
166
""",
)

entry(
    index = 154,
    label = "C2H + C2H3 <=> C2H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '167',
    ),
    longDesc = 
u"""
167
""",
)

entry(
    index = 155,
    label = "C2H + O <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '168',
    ),
    longDesc = 
u"""
168
""",
)

entry(
    index = 156,
    label = "C2H + OH <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '169',
    ),
    longDesc = 
u"""
169
""",
)

entry(
    index = 157,
    label = "C2H + OH <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '170',
    ),
    longDesc = 
u"""
170
""",
)

entry(
    index = 158,
    label = "C2H3 + O <=> CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '171',
    ),
    longDesc = 
u"""
171
""",
)

entry(
    index = 159,
    label = "C2H3 + OH <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '172',
    ),
    longDesc = 
u"""
172
""",
)

entry(
    index = 160,
    label = "C2H5 + O <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.62e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '173',
    ),
    longDesc = 
u"""
173
""",
)

entry(
    index = 161,
    label = "H2CCCH + O <=> C2H2 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '174',
    ),
    longDesc = 
u"""
174
""",
)

entry(
    index = 162,
    label = "H2CCCH + OH <=> C3H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '175',
    ),
    longDesc = 
u"""
175
""",
)

entry(
    index = 163,
    label = "H2CCCCH <=> C4H2 + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.12e+16, 'cm^3/(mol*s)'), n=0, Ea=(194631, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.2},
        comment = '176',
    ),
    longDesc = 
u"""
176
""",
)

entry(
    index = 164,
    label = "O + CH3O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '177',
    ),
    longDesc = 
u"""
177
""",
)

entry(
    index = 165,
    label = "O + CH2OH <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '178',
    ),
    longDesc = 
u"""
178
""",
)

entry(
    index = 166,
    label = "OH + CH3O <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '179',
    ),
    longDesc = 
u"""
179
""",
)

entry(
    index = 167,
    label = "OH + CH2OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '180',
    ),
    longDesc = 
u"""
180
""",
)

entry(
    index = 168,
    label = "HCO + HCO <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '181',
    ),
    longDesc = 
u"""
181
""",
)

entry(
    index = 169,
    label = "CH3O <=> CH2O + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.55e+14, 'cm^3/(mol*s)'), n=0, Ea=(56463.2, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.2},
        comment = '182',
    ),
    longDesc = 
u"""
182
""",
)

entry(
    index = 170,
    label = "CH2OH <=> CH2O + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.26e+16, 'cm^3/(mol*s)'), n=0, Ea=(125607, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.2},
        comment = '183',
    ),
    longDesc = 
u"""
183
""",
)

entry(
    index = 171,
    label = "HCCO + HCCO <=> C2H2 + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '184',
    ),
    longDesc = 
u"""
184
""",
)

entry(
    index = 172,
    label = "CH3 + O2 <=> CH3O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (114740, 'J/mol'),
        T0 = (1, 'K'),
        comment = '185',
    ),
    longDesc = 
u"""
185
""",
)

entry(
    index = 173,
    label = "CH3 + H <=> CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62358.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '186',
    ),
    longDesc = 
u"""
186
""",
)

entry(
    index = 174,
    label = "CH3 + OH <=> CH3O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+12, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (57369.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '187',
    ),
    longDesc = 
u"""
187
""",
)

entry(
    index = 175,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.2e+41, 'cm^6/(mol^2*s)'), n=-7, Ea=(11474, 'J/mol'), T0=(1, 'K')),
        alpha = 0.62,
        T3 = (73, 'K'),
        T1 = (1180, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[O][O]': 0.4, 'N#N': 1, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '188',
    ),
    longDesc = 
u"""
188
""",
)

entry(
    index = 176,
    label = "H + CH3 <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.4e+16, 'cm^3/(mol*s)'),
            n = -0.5,
            Ea = (2186.71, 'J/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.47e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (10143.7, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.2},
        comment = '189',
    ),
    longDesc = 
u"""
189
""",
)

entry(
    index = 177,
    label = "CH3 + C2H <=> H2CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '190',
    ),
    longDesc = 
u"""
190
""",
)

entry(
    index = 178,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.48e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (104887, 'J/mol'),
        T0 = (1, 'K'),
        comment = '191',
    ),
    longDesc = 
u"""
191
""",
)

entry(
    index = 179,
    label = "C2H + H <=> C2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '192',
    ),
    longDesc = 
u"""
192
""",
)

entry(
    index = 180,
    label = "C2H3 + O2 <=> C2H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+14, 'cm^3/(mol*s)'),
        n = -0.833,
        Ea = (10630.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '193',
    ),
    longDesc = 
u"""
193
""",
)

entry(
    index = 181,
    label = "C2H3 + O2 <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1039.31, 'J/mol'),
        T0 = (1, 'K'),
        comment = '194',
    ),
    longDesc = 
u"""
194
""",
)

entry(
    index = 182,
    label = "C2H2 + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0002192, 'cm^3/(mol*s)'),
        n = 4.5,
        Ea = (-4157.24, 'J/mol'),
        T0 = (1, 'K'),
        comment = '195',
    ),
    longDesc = 
u"""
195
""",
)

entry(
    index = 183,
    label = "C2H2 + HO2 => CH2 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.09e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (33041.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '196',
    ),
    longDesc = 
u"""
196
""",
)

entry(
    index = 184,
    label = "C2H2 + CH2 <=> H2CCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (27520.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '197',
    ),
    longDesc = 
u"""
197
""",
)

entry(
    index = 185,
    label = "C2H2 + HCCO <=> CO + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12471.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '198',
    ),
    longDesc = 
u"""
198
""",
)

entry(
    index = 186,
    label = "C2H2 + C2H2 <=> C4H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (177514, 'J/mol'),
        T0 = (1, 'K'),
        comment = '199',
    ),
    longDesc = 
u"""
199
""",
)

entry(
    index = 187,
    label = "CH2CO + O2 <=> CH2O + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+08, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '200',
    ),
    longDesc = 
u"""
200
""",
)

entry(
    index = 188,
    label = "CH3CO + H <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '201',
    ),
    longDesc = 
u"""
201
""",
)

entry(
    index = 189,
    label = "CH3CO + H <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '202',
    ),
    longDesc = 
u"""
202
""",
)

entry(
    index = 190,
    label = "CH3CO + O <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '203',
    ),
    longDesc = 
u"""
203
""",
)

entry(
    index = 191,
    label = "CH3CO + O <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '204',
    ),
    longDesc = 
u"""
204
""",
)

entry(
    index = 192,
    label = "CH3CO + OH <=> CH2CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '205',
    ),
    longDesc = 
u"""
205
""",
)

entry(
    index = 193,
    label = "CH3CO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.8e+13, 's^-1'), n=0, Ea=(71088.7, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.1e+15, 'cm^3/(mol*s)'), n=0, Ea=(58201.3, 'J/mol'), T0=(1, 'K')),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[C-]#[O+]': 2, '[H][H]': 2, 'O=C=O': 3, 'O': 5},
        comment = '206',
    ),
    longDesc = 
u"""
206
""",
)

entry(
    index = 194,
    label = "CH2HCO <=> CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (184110, 'J/mol'),
        T0 = (1, 'K'),
        comment = '207',
    ),
    longDesc = 
u"""
207
""",
)

entry(
    index = 195,
    label = "CH2HCO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2e+16, 'cm^3/(mol*s)'), n=0, Ea=(174604, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'[C-]#[O+]': 2, '[H][H]': 2, 'O=C=O': 3, 'O': 5},
        comment = '208',
    ),
    longDesc = 
u"""
208
""",
)

entry(
    index = 196,
    label = "CH2HCO + O2 <=> CH2O + OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6235.85, 'J/mol'),
        T0 = (1, 'K'),
        comment = '209',
    ),
    longDesc = 
u"""
209
""",
)

entry(
    index = 197,
    label = "CH2HCO + H <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '210',
    ),
    longDesc = 
u"""
210
""",
)

entry(
    index = 198,
    label = "CH2HCO + H <=> CH3CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '211',
    ),
    longDesc = 
u"""
211
""",
)

entry(
    index = 199,
    label = "CH2HCO + O <=> CH2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '212',
    ),
    longDesc = 
u"""
212
""",
)

entry(
    index = 200,
    label = "CH2HCO + OH <=> CH2CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '213',
    ),
    longDesc = 
u"""
213
""",
)

entry(
    index = 201,
    label = "CH2HCO + OH <=> CH2OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '214',
    ),
    longDesc = 
u"""
214
""",
)

entry(
    index = 202,
    label = "CH2HCO + CH3 <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '215',
    ),
    longDesc = 
u"""
215
""",
)

entry(
    index = 203,
    label = "CH2HCO + CH2 <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '216',
    ),
    longDesc = 
u"""
216
""",
)

entry(
    index = 204,
    label = "CH2HCO + CH <=> C2H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '217',
    ),
    longDesc = 
u"""
217
""",
)

entry(
    index = 205,
    label = "CH3CHO + H <=> H2 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (18375, 'J/mol'),
        T0 = (1, 'K'),
        comment = '218',
    ),
    longDesc = 
u"""
218
""",
)

entry(
    index = 206,
    label = "CH3CHO + HO2 <=> H2O2 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (49886.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '219',
    ),
    longDesc = 
u"""
219
""",
)

entry(
    index = 207,
    label = "CH3CHO + CH3 <=> CH4 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.01e-06, 'cm^3/(mol*s)'),
        n = 5.6,
        Ea = (10226.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '220',
    ),
    longDesc = 
u"""
220
""",
)

entry(
    index = 208,
    label = "CH3CHO + OH <=> CH3CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (-4614.53, 'J/mol'),
        T0 = (1, 'K'),
        comment = '221',
    ),
    longDesc = 
u"""
221
""",
)

entry(
    index = 209,
    label = "CH3CHO + O <=> CH3CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7483.02, 'J/mol'),
        T0 = (1, 'K'),
        comment = '222',
    ),
    longDesc = 
u"""
222
""",
)

entry(
    index = 210,
    label = "CH3CHO + O2 <=> CH3CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (162132, 'J/mol'),
        T0 = (1, 'K'),
        comment = '223',
    ),
    longDesc = 
u"""
223
""",
)

entry(
    index = 211,
    label = "CH3CHO <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.1e+15, 's^-1'),
        n = 0,
        Ea = (337900, 'J/mol'),
        T0 = (1, 'K'),
        comment = '224',
    ),
    longDesc = 
u"""
224
""",
)

entry(
    index = 212,
    label = "C2H3 + O2 <=> CH2HCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)'),
        n = -0.611,
        Ea = (21879.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '225',
    ),
    longDesc = 
u"""
225
""",
)

entry(
    index = 213,
    label = "C2H3 + HO2 => CH3 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '226',
    ),
    longDesc = 
u"""
226
""",
)

entry(
    index = 214,
    label = "C2H3 + CH2 <=> C3H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '227',
    ),
    longDesc = 
u"""
227
""",
)

entry(
    index = 215,
    label = "C2H3 + C2H3 <=> H2CCCH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '228',
    ),
    longDesc = 
u"""
228
""",
)

entry(
    index = 216,
    label = "C2H3 + C2H3 <=> C2H2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '229',
    ),
    longDesc = 
u"""
229
""",
)

entry(
    index = 217,
    label = "C2H3 + C2H3 <=> i-C4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '230',
    ),
    longDesc = 
u"""
230
""",
)

entry(
    index = 218,
    label = "C2H3 + C2H3 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.94e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '231',
    ),
    longDesc = 
u"""
231
""",
)

entry(
    index = 219,
    label = "C2H3 + CH2O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5420, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (24369.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '232',
    ),
    longDesc = 
u"""
232
""",
)

entry(
    index = 220,
    label = "C2H3 + C2H5 <=> C3H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+32, 'cm^3/(mol*s)'),
        n = -5.22,
        Ea = (81955.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '233',
    ),
    longDesc = 
u"""
233
""",
)

entry(
    index = 221,
    label = "C2H3 + H2O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2469.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '234',
    ),
    longDesc = 
u"""
234
""",
)

entry(
    index = 222,
    label = "C2H3 + HCO <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '235',
    ),
    longDesc = 
u"""
235
""",
)

entry(
    index = 223,
    label = "C2H3 + CH3 <=> C2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.92e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '236',
    ),
    longDesc = 
u"""
236
""",
)

entry(
    index = 224,
    label = "C2H4 + O2 <=> CH2HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (153818, 'J/mol'),
        T0 = (1, 'K'),
        comment = '237',
    ),
    longDesc = 
u"""
237
""",
)

entry(
    index = 225,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (239457, 'J/mol'),
        T0 = (1, 'K'),
        comment = '238',
    ),
    longDesc = 
u"""
238
""",
)

entry(
    index = 226,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (235, 'cm^3/(mol*s)'),
        n = 3.63,
        Ea = (47143.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '239',
    ),
    longDesc = 
u"""
239
""",
)

entry(
    index = 227,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (500000, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (18590.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '240',
    ),
    longDesc = 
u"""
240
""",
)

entry(
    index = 228,
    label = "C2H4 + CH2 <=> C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '241',
    ),
    longDesc = 
u"""
241
""",
)

entry(
    index = 229,
    label = "C2H4 + C2H <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '242',
    ),
    longDesc = 
u"""
242
""",
)

entry(
    index = 230,
    label = "C2H4 + C2H3 <=> C4H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30597.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '243',
    ),
    longDesc = 
u"""
243
""",
)

entry(
    index = 231,
    label = "C2H6 + O2 <=> C2H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (212019, 'J/mol'),
        T0 = (1, 'K'),
        comment = '244',
    ),
    longDesc = 
u"""
244
""",
)

entry(
    index = 232,
    label = "C2H6 + CH2 <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (32052.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '245',
    ),
    longDesc = 
u"""
245
""",
)

entry(
    index = 233,
    label = "C2H6 + C2H3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41572.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '246',
    ),
    longDesc = 
u"""
246
""",
)

entry(
    index = 234,
    label = "C3H2 + O2 <=> C2H2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '247',
    ),
    longDesc = 
u"""
247
""",
)

entry(
    index = 235,
    label = "C3H2 + O <=> C2H + H + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '248',
    ),
    longDesc = 
u"""
248
""",
)

entry(
    index = 236,
    label = "C3H2 + OH <=> C2H2 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '249',
    ),
    longDesc = 
u"""
249
""",
)

entry(
    index = 237,
    label = "C3H2 + CH3 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '250',
    ),
    longDesc = 
u"""
250
""",
)

entry(
    index = 238,
    label = "H2CCCH + O2 <=> CO2 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11997.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '251',
    ),
    longDesc = 
u"""
251
""",
)

entry(
    index = 239,
    label = "H2CCCH + O2 <=> CO + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11997.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '252',
    ),
    longDesc = 
u"""
252
""",
)

entry(
    index = 240,
    label = "H2CCCH + O <=> CH2O + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '253',
    ),
    longDesc = 
u"""
253
""",
)

entry(
    index = 241,
    label = "H2CCCH + H <=> C3H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '254',
    ),
    longDesc = 
u"""
254
""",
)

entry(
    index = 242,
    label = "H2CCCH + OH <=> HCO + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '255',
    ),
    longDesc = 
u"""
255
""",
)

entry(
    index = 243,
    label = "H2CCCH + CH <=> H2CCCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '256',
    ),
    longDesc = 
u"""
256
""",
)

entry(
    index = 244,
    label = "H2CCCH + CH3 <=> C4H6",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.6e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (37706.1, 'J/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = '257',
    ),
    longDesc = 
u"""
257
""",
)

entry(
    index = 245,
    label = "H2CCCH + H <=> C3H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(9e+15, 'cm^6/(mol^2*s)'), n=1, Ea=(0, 'J/mol'), T0=(1, 'K')),
        alpha = 0.5,
        T3 = (1e+30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {},
        comment = '258',
    ),
    longDesc = 
u"""
258
""",
)

entry(
    index = 246,
    label = "C3H4 + O2 <=> H2CCCH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (212019, 'J/mol'),
        T0 = (1, 'K'),
        comment = '259',
    ),
    longDesc = 
u"""
259
""",
)

entry(
    index = 247,
    label = "C3H4 + O <=> HCCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8314.47, 'J/mol'),
        T0 = (1, 'K'),
        comment = '260',
    ),
    longDesc = 
u"""
260
""",
)

entry(
    index = 248,
    label = "C3H4 + O <=> OH + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (31595, 'J/mol'),
        T0 = (1, 'K'),
        comment = '261',
    ),
    longDesc = 
u"""
261
""",
)

entry(
    index = 249,
    label = "C3H4 + O <=> C2H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.011, 'cm^3/(mol*s)'),
        n = 4.6,
        Ea = (-17643.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '262',
    ),
    longDesc = 
u"""
262
""",
)

entry(
    index = 250,
    label = "C3H4 + O <=> CO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6651.58, 'J/mol'),
        T0 = (1, 'K'),
        comment = '263',
    ),
    longDesc = 
u"""
263
""",
)

entry(
    index = 251,
    label = "C3H4 + H <=> CH3 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9977.37, 'J/mol'),
        T0 = (1, 'K'),
        comment = '264',
    ),
    longDesc = 
u"""
264
""",
)

entry(
    index = 252,
    label = "C3H4 + H <=> C3H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(3e+24, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'J/mol'), T0=(1, 'K')),
        alpha = 0.8,
        T3 = (1e+15, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {},
        comment = '265',
    ),
    longDesc = 
u"""
265
""",
)

entry(
    index = 253,
    label = "C3H4 + HO2 <=> H2CCCH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9600, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (56538.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '266',
    ),
    longDesc = 
u"""
266
""",
)

entry(
    index = 254,
    label = "C3H4 + H <=> H2CCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '267',
    ),
    longDesc = 
u"""
267
""",
)

entry(
    index = 255,
    label = "C3H4 + OH <=> CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3325.79, 'J/mol'),
        T0 = (1, 'K'),
        comment = '268',
    ),
    longDesc = 
u"""
268
""",
)

entry(
    index = 256,
    label = "C3H4 + OH <=> H2CCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (415.724, 'J/mol'),
        T0 = (1, 'K'),
        comment = '269',
    ),
    longDesc = 
u"""
269
""",
)

entry(
    index = 257,
    label = "C3H4 + CH3 <=> H2CCCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (32010.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '270',
    ),
    longDesc = 
u"""
270
""",
)

entry(
    index = 258,
    label = "C3H4 + C2H <=> H2CCCH + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '271',
    ),
    longDesc = 
u"""
271
""",
)

entry(
    index = 259,
    label = "C3H4 + C2H3 <=> H2CCCH + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (19539, 'J/mol'),
        T0 = (1, 'K'),
        comment = '272',
    ),
    longDesc = 
u"""
272
""",
)

entry(
    index = 260,
    label = "C3H4 + C2H5 <=> H2CCCH + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (27437.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '273',
    ),
    longDesc = 
u"""
273
""",
)

entry(
    index = 261,
    label = "C3H5 + O2 <=> CO + CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (78571.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '274',
    ),
    longDesc = 
u"""
274
""",
)

entry(
    index = 262,
    label = "C3H5 + O2 <=> C3H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (94785, 'J/mol'),
        T0 = (1, 'K'),
        comment = '275',
    ),
    longDesc = 
u"""
275
""",
)

entry(
    index = 263,
    label = "C3H5 + O <=> CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '276',
    ),
    longDesc = 
u"""
276
""",
)

entry(
    index = 264,
    label = "C3H5 + O => C2H4 + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '277',
    ),
    longDesc = 
u"""
277
""",
)

entry(
    index = 265,
    label = "CH3 + C2H3 <=> C3H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+24, 'cm^3/(mol*s)'),
        n = -2.83,
        Ea = (77905.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '278',
    ),
    longDesc = 
u"""
278
""",
)

entry(
    index = 266,
    label = "C3H5 + H <=> C3H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '279',
    ),
    longDesc = 
u"""
279
""",
)

entry(
    index = 267,
    label = "C3H5 + OH <=> CH2O + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '280',
    ),
    longDesc = 
u"""
280
""",
)

entry(
    index = 268,
    label = "C3H5 + OH <=> C3H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '281',
    ),
    longDesc = 
u"""
281
""",
)

entry(
    index = 269,
    label = "C3H5 + HO2 <=> OH + HCO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '282',
    ),
    longDesc = 
u"""
282
""",
)

entry(
    index = 270,
    label = "C3H5 + HO2 => C2H3 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.25e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '283',
    ),
    longDesc = 
u"""
283
""",
)

entry(
    index = 271,
    label = "C3H5 + C2H3 <=> C3H4 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '284',
    ),
    longDesc = 
u"""
284
""",
)

entry(
    index = 272,
    label = "C3H5 + C2H5 <=> C3H4 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-550.418, 'J/mol'),
        T0 = (1, 'K'),
        comment = '285',
    ),
    longDesc = 
u"""
285
""",
)

entry(
    index = 273,
    label = "C3H5 + C2H5 <=> C2H4 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-548.755, 'J/mol'),
        T0 = (1, 'K'),
        comment = '286',
    ),
    longDesc = 
u"""
286
""",
)

entry(
    index = 274,
    label = "C3H5 + C3H4 <=> H2CCCH + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (32010.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '287',
    ),
    longDesc = 
u"""
287
""",
)

entry(
    index = 275,
    label = "C3H5 + C3H5 <=> C3H4 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1097.51, 'J/mol'),
        T0 = (1, 'K'),
        comment = '288',
    ),
    longDesc = 
u"""
288
""",
)

entry(
    index = 276,
    label = "C3H5 + CH2O <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (76119, 'J/mol'),
        T0 = (1, 'K'),
        comment = '289',
    ),
    longDesc = 
u"""
289
""",
)

entry(
    index = 277,
    label = "C3H5 + C2H3 <=> C3H6 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '290',
    ),
    longDesc = 
u"""
290
""",
)

entry(
    index = 278,
    label = "CH3 + C2H3 <=> C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.27e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (40881.1, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000, 'K'),
        T2 = (10140, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '291',
    ),
    longDesc = 
u"""
291
""",
)

entry(
    index = 279,
    label = "C3H5 + H <=> C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.67e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.33e+60, 'cm^6/(mol^2*s)'),
            n = -12,
            Ea = (24971.9, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.02,
        T3 = (1096.6, 'K'),
        T1 = (1096.6, 'K'),
        T2 = (6859.5, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '292',
    ),
    longDesc = 
u"""
292
""",
)

entry(
    index = 280,
    label = "C3H6 <=> C3H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 's^-1'),
        n = 0,
        Ea = (332579, 'J/mol'),
        T0 = (1, 'K'),
        comment = '293',
    ),
    longDesc = 
u"""
293
""",
)

entry(
    index = 281,
    label = "C3H6 <=> C2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+12, 's^-1'),
        n = 0,
        Ea = (291007, 'J/mol'),
        T0 = (1, 'K'),
        comment = '294',
    ),
    longDesc = 
u"""
294
""",
)

entry(
    index = 282,
    label = "C3H6 + O2 <=> C3H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1080, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (149494, 'J/mol'),
        T0 = (1, 'K'),
        comment = '295',
    ),
    longDesc = 
u"""
295
""",
)

entry(
    index = 283,
    label = "C3H6 + O <=> CH3 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.11e+06, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (-2610.74, 'J/mol'),
        T0 = (1, 'K'),
        comment = '296',
    ),
    longDesc = 
u"""
296
""",
)

entry(
    index = 284,
    label = "C3H6 + O <=> CH2CO + CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (1368.31, 'J/mol'),
        T0 = (1, 'K'),
        comment = '297',
    ),
    longDesc = 
u"""
297
""",
)

entry(
    index = 285,
    label = "C3H6 + O <=> C3H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (24604.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '298',
    ),
    longDesc = 
u"""
298
""",
)

entry(
    index = 286,
    label = "C3H6 + O <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (67600, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (-4739.25, 'J/mol'),
        T0 = (1, 'K'),
        comment = '299',
    ),
    longDesc = 
u"""
299
""",
)

entry(
    index = 287,
    label = "C3H6 + O <=> C2H4 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (67600, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (-4739.25, 'J/mol'),
        T0 = (1, 'K'),
        comment = '300',
    ),
    longDesc = 
u"""
300
""",
)

entry(
    index = 288,
    label = "C3H6 + H <=> C3H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18483.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '301',
    ),
    longDesc = 
u"""
301
""",
)

entry(
    index = 289,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (46062.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '302',
    ),
    longDesc = 
u"""
302
""",
)

entry(
    index = 290,
    label = "C3H6 + OH <=> C3H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.12e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1255.49, 'J/mol'),
        T0 = (1, 'K'),
        comment = '303',
    ),
    longDesc = 
u"""
303
""",
)

entry(
    index = 291,
    label = "C3H6 + OH <=> C2H5 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '304',
    ),
    longDesc = 
u"""
304
""",
)

entry(
    index = 292,
    label = "C3H6 + HO2 <=> C3H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9640, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (58226.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '305',
    ),
    longDesc = 
u"""
305
""",
)

entry(
    index = 293,
    label = "C3H6 + CH3 <=> C3H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.21, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (23771.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '306',
    ),
    longDesc = 
u"""
306
""",
)

entry(
    index = 294,
    label = "C3H6 + CH2 <=> C3H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (25774.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '307',
    ),
    longDesc = 
u"""
307
""",
)

entry(
    index = 295,
    label = "C3H6 + C2H <=> C3H4 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '308',
    ),
    longDesc = 
u"""
308
""",
)

entry(
    index = 296,
    label = "C3H6 + C2H3 <=> C3H5 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.02e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60778.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '309',
    ),
    longDesc = 
u"""
309
""",
)

entry(
    index = 297,
    label = "C3H6 + C2H5 <=> C3H5 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41073.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '310',
    ),
    longDesc = 
u"""
310
""",
)

entry(
    index = 298,
    label = "CH3 + OH <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.595e+44, 'cm^6/(mol^2*s)'), n=-8.2, Ea=(0, 'J/mol'), T0=(1, 'K')),
        alpha = 0.82,
        T3 = (200, 'K'),
        T1 = (1438, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = '311',
    ),
    longDesc = 
u"""
311
""",
)

entry(
    index = 299,
    label = "CH2O + H <=> CH2OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.4e+11, 'cm^3/(mol*s)'), n=0.5, Ea=(14966, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.27e+32, 'cm^6/(mol^2*s)'),
            n = -4.82,
            Ea = (27146.8, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7187,
        T3 = (103, 'K'),
        T1 = (1291, 'K'),
        T2 = (4160, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = '312',
    ),
    longDesc = 
u"""
312
""",
)

entry(
    index = 300,
    label = "CH2O + H <=> CH3O",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.08e+11, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (10808.8, 'J/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (23114.2, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.758,
        T3 = (94, 'K'),
        T1 = (1555, 'K'),
        T2 = (4200, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = '313',
    ),
    longDesc = 
u"""
313
""",
)

entry(
    index = 301,
    label = "CH2OH + H <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.06e+12, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (357.522, 'J/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.36e+31, 'cm^6/(mol^2*s)'),
            n = -4.65,
            Ea = (21118.8, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.61,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = '314',
    ),
    longDesc = 
u"""
314
""",
)

entry(
    index = 302,
    label = "CH3O + H <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.43e+12, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (207.862, 'J/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.66e+41, 'cm^6/(mol^2*s)'),
            n = -7.44,
            Ea = (117068, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = '315',
    ),
    longDesc = 
u"""
315
""",
)

entry(
    index = 303,
    label = "CH3O + H <=> H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.15e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (6751.35, 'J/mol'),
        T0 = (1, 'K'),
        comment = '316',
    ),
    longDesc = 
u"""
316
""",
)

entry(
    index = 304,
    label = "CH2OH + H <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.28e+13, 'cm^3/(mol*s)'),
        n = -0.1,
        Ea = (2535.91, 'J/mol'),
        T0 = (1, 'K'),
        comment = '317',
    ),
    longDesc = 
u"""
317
""",
)

entry(
    index = 305,
    label = "CH3O + H <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+14, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (4448.24, 'J/mol'),
        T0 = (1, 'K'),
        comment = '318',
    ),
    longDesc = 
u"""
318
""",
)

entry(
    index = 306,
    label = "CH3OH + H <=> CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+09, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (18790.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '319',
    ),
    longDesc = 
u"""
319
""",
)

entry(
    index = 307,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+09, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (18790.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '320',
    ),
    longDesc = 
u"""
320
""",
)

entry(
    index = 308,
    label = "CH3OH + OH <=> CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+06, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (-1197.28, 'J/mol'),
        T0 = (1, 'K'),
        comment = '321',
    ),
    longDesc = 
u"""
321
""",
)

entry(
    index = 309,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (-1197.28, 'J/mol'),
        T0 = (1, 'K'),
        comment = '322',
    ),
    longDesc = 
u"""
322
""",
)

entry(
    index = 310,
    label = "CH3OH + CH2(S) <=> CH2OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '323',
    ),
    longDesc = 
u"""
323
""",
)

entry(
    index = 311,
    label = "CH3OH + CH2 <=> CH2OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31.9, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (29932.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '324',
    ),
    longDesc = 
u"""
324
""",
)

entry(
    index = 312,
    label = "CH3OH + CH2 <=> CH3O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14.4, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (28684.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '325',
    ),
    longDesc = 
u"""
325
""",
)

entry(
    index = 313,
    label = "CH3OH + CH3 <=> CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20, 'cm^3/(mol*s)'),
        n = 3.45,
        Ea = (33424.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '326',
    ),
    longDesc = 
u"""
326
""",
)

entry(
    index = 314,
    label = "CH3OH + CH3 <=> CH3O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10, 'cm^3/(mol*s)'),
        n = 3.45,
        Ea = (33424.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '327',
    ),
    longDesc = 
u"""
327
""",
)

entry(
    index = 315,
    label = "CH3OH + C2H <=> CH2OH + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '328',
    ),
    longDesc = 
u"""
328
""",
)

entry(
    index = 316,
    label = "CH3OH + C2H <=> CH3O + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '329',
    ),
    longDesc = 
u"""
329
""",
)

entry(
    index = 317,
    label = "CH3OH + C2H3 <=> CH2OH + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31.9, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (29932.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '330',
    ),
    longDesc = 
u"""
330
""",
)

entry(
    index = 318,
    label = "CH3OH + C2H3 <=> CH3O + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14.4, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (28684.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '331',
    ),
    longDesc = 
u"""
331
""",
)

entry(
    index = 319,
    label = "CH3O + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12471.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '332',
    ),
    longDesc = 
u"""
332
""",
)

entry(
    index = 320,
    label = "CH3O + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '333',
    ),
    longDesc = 
u"""
333
""",
)

entry(
    index = 321,
    label = "CH3O + CH2O <=> CH3OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12471.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '334',
    ),
    longDesc = 
u"""
334
""",
)

entry(
    index = 322,
    label = "CH2OH + CH2 <=> C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '335',
    ),
    longDesc = 
u"""
335
""",
)

entry(
    index = 323,
    label = "CH2OH + CH2 <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '336',
    ),
    longDesc = 
u"""
336
""",
)

entry(
    index = 324,
    label = "CH2OH + CH3 <=> CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '337',
    ),
    longDesc = 
u"""
337
""",
)

entry(
    index = 325,
    label = "CH2OH + C2H <=> CH2O + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '338',
    ),
    longDesc = 
u"""
338
""",
)

entry(
    index = 326,
    label = "CH2OH + C2H2 <=> CH2O + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (37415.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '339',
    ),
    longDesc = 
u"""
339
""",
)

entry(
    index = 327,
    label = "CH2OH + C2H3 <=> CH2O + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '340',
    ),
    longDesc = 
u"""
340
""",
)

entry(
    index = 328,
    label = "CH2OH + C2H5 <=> CH2O + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '341',
    ),
    longDesc = 
u"""
341
""",
)

entry(
    index = 329,
    label = "CH2OH + HCO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '342',
    ),
    longDesc = 
u"""
342
""",
)

entry(
    index = 330,
    label = "CH2OH + CH2OH <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '343',
    ),
    longDesc = 
u"""
343
""",
)

entry(
    index = 331,
    label = "CH3O + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '344',
    ),
    longDesc = 
u"""
344
""",
)

entry(
    index = 332,
    label = "CH2OH + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '345',
    ),
    longDesc = 
u"""
345
""",
)

entry(
    index = 333,
    label = "CH2OH + CH2O <=> CH3OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5500, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (24527.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '346',
    ),
    longDesc = 
u"""
346
""",
)

entry(
    index = 334,
    label = "CH2OH + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '347',
    ),
    longDesc = 
u"""
347
""",
)

entry(
    index = 335,
    label = "CH2OH + C2H5 <=> CH3OH + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '348',
    ),
    longDesc = 
u"""
348
""",
)

entry(
    index = 336,
    label = "CH3O + CO <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.57e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (49388, 'J/mol'),
        T0 = (1, 'K'),
        comment = '349',
    ),
    longDesc = 
u"""
349
""",
)

entry(
    index = 337,
    label = "CH3O + CH3 <=> CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '350',
    ),
    longDesc = 
u"""
350
""",
)

entry(
    index = 338,
    label = "CH3O + C2H5 <=> CH2O + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '351',
    ),
    longDesc = 
u"""
351
""",
)

entry(
    index = 339,
    label = "CH3O + C2H3 <=> CH2O + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '352',
    ),
    longDesc = 
u"""
352
""",
)

entry(
    index = 340,
    label = "CH3OH <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7e+15, 'cm^3/(mol*s)'), n=0, Ea=(278019, 'J/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '353',
    ),
    longDesc = 
u"""
353
""",
)

entry(
    index = 341,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (388000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (12901.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '354',
    ),
    longDesc = 
u"""
354
""",
)

entry(
    index = 342,
    label = "CH3OH + O <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19592.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '355',
    ),
    longDesc = 
u"""
355
""",
)

entry(
    index = 343,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+06, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (-1197.28, 'J/mol'),
        T0 = (1, 'K'),
        comment = '356\nRxn 356 commented out because reverse rate coefficient is above Z',
    ),
    longDesc = 
u"""
356
Rxn 356 commented out because reverse rate coefficient is above Z
""",
)

entry(
    index = 344,
    label = "CH3CHO + OH <=> CH2HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2594.36, 'J/mol'),
        T0 = (1, 'K'),
        comment = '357\nC2H5O2H = C2H5O+OH 6.460E+14 0.0000 21700.00\n358\nC2H5+HO2 = C2H5O+OH 3.240E+13 0.0000 0.00\n359\nC2H5O = CH3+CH2O 1.000E+15 0.0000 10900.00\n360\nC2H5O+O2 = CH3CHO+HO2 1.820E+11 0.0000 468.04\n361',
    ),
    longDesc = 
u"""
357
C2H5O2H = C2H5O+OH 6.460E+14 0.0000 21700.00
358
C2H5+HO2 = C2H5O+OH 3.240E+13 0.0000 0.00
359
C2H5O = CH3+CH2O 1.000E+15 0.0000 10900.00
360
C2H5O+O2 = CH3CHO+HO2 1.820E+11 0.0000 468.04
361
""",
)

entry(
    index = 345,
    label = "CH3CHO + O <=> CH2HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.72e+13, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (14896.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '362',
    ),
    longDesc = 
u"""
362
""",
)

entry(
    index = 346,
    label = "CH3CHO + H <=> CH2HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.85e+12, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (22428.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '363',
    ),
    longDesc = 
u"""
363
""",
)

entry(
    index = 347,
    label = "CH3CHO + CH3 <=> CH2HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24.5, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (23976.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '364',
    ),
    longDesc = 
u"""
364
""",
)

entry(
    index = 348,
    label = "CH3CHO + HO2 <=> CH2HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.32e+11, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (62348.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '365',
    ),
    longDesc = 
u"""
365
""",
)

entry(
    index = 349,
    label = "C2H5OH <=> CH3 + CH2OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6e+23, 's^-1'), n=-1.68, Ea=(376679, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.88e+85, 'cm^3/(mol*s)'),
            n = -18.81,
            Ea = (477791, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (200, 'K'),
        T1 = (890, 'K'),
        T2 = (4600, 'K'),
        efficiencies = {'[C-]#[O+]': 2, '[H][H]': 2, 'O=C=O': 3, 'O': 5},
        comment = '366',
    ),
    longDesc = 
u"""
366
""",
)

entry(
    index = 350,
    label = "C2H5OH <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.79e+13, 's^-1'), n=0.09, Ea=(274948, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.57e+83, 'cm^3/(mol*s)'),
            n = -18.85,
            Ea = (359401, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (350, 'K'),
        T1 = (800, 'K'),
        T2 = (3800, 'K'),
        efficiencies = {'O': 6},
        comment = '367',
    ),
    longDesc = 
u"""
367
""",
)

entry(
    index = 351,
    label = "C2H5OH <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.25e+23, 's^-1'), n=-1.54, Ea=(401930, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.85e+85, 'cm^3/(mol*s)'),
            n = -18.81,
            Ea = (477791, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (300, 'K'),
        T1 = (900, 'K'),
        T2 = (5000, 'K'),
        efficiencies = {'[C-]#[O+]': 2, '[H][H]': 2, 'O=C=O': 3, 'O': 5},
        comment = '368',
    ),
    longDesc = 
u"""
368
""",
)

entry(
    index = 352,
    label = "C2H5OH + OH <=> CH2CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (3000.28, 'J/mol'),
        T0 = (1, 'K'),
        comment = '369',
    ),
    longDesc = 
u"""
369
""",
)

entry(
    index = 353,
    label = "C2H5OH + OH <=> CH3CHOH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.09e+10, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-1590.06, 'J/mol'),
        T0 = (1, 'K'),
        comment = '370',
    ),
    longDesc = 
u"""
370
""",
)

entry(
    index = 354,
    label = "C2H5OH + H <=> CH2CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.5e+06, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (21340.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '371\nC2H5OH+OH = CH3CH2O+H2O 1.050E+10 0.8000 360.85\n372',
    ),
    longDesc = 
u"""
371
C2H5OH+OH = CH3CH2O+H2O 1.050E+10 0.8000 360.85
372
""",
)

entry(
    index = 355,
    label = "C2H5OH + H <=> CH3CHOH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.29e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (11842, 'J/mol'),
        T0 = (1, 'K'),
        comment = '373',
    ),
    longDesc = 
u"""
373
""",
)

entry(
    index = 356,
    label = "C2H5OH + O <=> CH2CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.41e+07, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (22847, 'J/mol'),
        T0 = (1, 'K'),
        comment = '374\nC2H5OH+H = CH3CH2O+H2 7.500E+06 1.6000 1529.94\n375',
    ),
    longDesc = 
u"""
374
C2H5OH+H = CH3CH2O+H2 7.500E+06 1.6000 1529.94
375
""",
)

entry(
    index = 357,
    label = "C2H5OH + O <=> CH3CHOH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7615.64, 'J/mol'),
        T0 = (1, 'K'),
        comment = '376',
    ),
    longDesc = 
u"""
376
""",
)

entry(
    index = 358,
    label = "C2H5OH + CH3 <=> CH2CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (219, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (40254.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '377\nC2H5OH+O = CH3CH2O+OH 1.580E+07 2.0000 2239.56\n378',
    ),
    longDesc = 
u"""
377
C2H5OH+O = CH3CH2O+OH 1.580E+07 2.0000 2239.56
378
""",
)

entry(
    index = 359,
    label = "C2H5OH + CH3 <=> CH3CHOH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (728, 'cm^3/(mol*s)'),
        n = 3,
        Ea = (33266.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '379',
    ),
    longDesc = 
u"""
379
""",
)

entry(
    index = 360,
    label = "C2H5OH + HO2 <=> CH3CHOH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8200, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (45191.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '380\nC2H5OH+CH3 = CH3CH2O+CH4 1.450E+02 3.0000 3850.03\n381',
    ),
    longDesc = 
u"""
380
C2H5OH+CH3 = CH3CH2O+CH4 1.450E+02 3.0000 3850.03
381
""",
)

entry(
    index = 361,
    label = "C2H5OH + HO2 <=> CH2CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24300, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (66114.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '382',
    ),
    longDesc = 
u"""
382
""",
)

entry(
    index = 362,
    label = "C2H4 + OH <=> CH2CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-9958.99, 'J/mol'),
        T0 = (1, 'K'),
        comment = '383\nC2H5OH+HO2 = CH3CH2O+H2O2 3.800E+12 0.0000 12078.51\n384',
    ),
    longDesc = 
u"""
383
C2H5OH+HO2 = CH3CH2O+H2O2 3.800E+12 0.0000 12078.51
384
""",
)

entry(
    index = 363,
    label = "CH3CHOH + O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (21005.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '385\nC2H5+HO2 = CH3CH2O+OH 4.000E+13 0.0000 0.00\n386\nCH3CH2O+M = CH3CHO+H+M 4.000E+06 1.4200 10300.60\n387\nCH3CH2O+M = CH3+CH2O+M 1.600E+14 -0.2200 13700.75\n388\nCH3CH2O+O2 = CH3CHO+HO2 4.000E+10 0.0000 553.60\n389\nCH3CH2O+CO = C2H5+CO2 4.680E+02 3.2000 2707.60\n390\nCH3CH2O+H = CH3+CH2OH 3.000E+13 0.0000 0.00\n391\nCH3CH2O+H = C2H4+H2O 3.000E+13 0.0000 0.00\n392\nCH3CH2O+OH = CH3CHO+H2O 1.000E+13 0.0000 0.00\n393',
    ),
    longDesc = 
u"""
385
C2H5+HO2 = CH3CH2O+OH 4.000E+13 0.0000 0.00
386
CH3CH2O+M = CH3CHO+H+M 4.000E+06 1.4200 10300.60
387
CH3CH2O+M = CH3+CH2O+M 1.600E+14 -0.2200 13700.75
388
CH3CH2O+O2 = CH3CHO+HO2 4.000E+10 0.0000 553.60
389
CH3CH2O+CO = C2H5+CO2 4.680E+02 3.2000 2707.60
390
CH3CH2O+H = CH3+CH2OH 3.000E+13 0.0000 0.00
391
CH3CH2O+H = C2H4+H2O 3.000E+13 0.0000 0.00
392
CH3CH2O+OH = CH3CHO+H2O 1.000E+13 0.0000 0.00
393
""",
)

entry(
    index = 364,
    label = "CH3CHOH + O <=> CH3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '394',
    ),
    longDesc = 
u"""
394
""",
)

entry(
    index = 365,
    label = "CH3CHOH + H <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '395',
    ),
    longDesc = 
u"""
395
""",
)

entry(
    index = 366,
    label = "CH3CHOH + H <=> CH3 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '396',
    ),
    longDesc = 
u"""
396
""",
)

entry(
    index = 367,
    label = "CH3CHOH + HO2 <=> CH3CHO + OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '397',
    ),
    longDesc = 
u"""
397
""",
)

entry(
    index = 368,
    label = "CH3CHOH + OH <=> CH3CHO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '398',
    ),
    longDesc = 
u"""
398
""",
)

entry(
    index = 369,
    label = "CH3CHOH <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(104611, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '399',
    ),
    longDesc = 
u"""
399
""",
)

entry(
    index = 370,
    label = "C2H2 + O2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+15, 'cm^3/(mol*s)'),
        n = -0.54,
        Ea = (187192, 'J/mol'),
        T0 = (1, 'K'),
        comment = '400',
    ),
    longDesc = 
u"""
400
""",
)

entry(
    index = 371,
    label = "C2H4 + OH <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24866.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '401',
    ),
    longDesc = 
u"""
401
""",
)

entry(
    index = 372,
    label = "C2H4 + OH <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24866.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '402',
    ),
    longDesc = 
u"""
402
""",
)

entry(
    index = 373,
    label = "C2H2 + CH3 <=> C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.06e+11, 'cm^3/(mol*s)'),
        n = 0.28,
        Ea = (32426.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '403',
    ),
    longDesc = 
u"""
403
""",
)

entry(
    index = 374,
    label = "CH4 + CH3 <=> CH4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60512.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '404',
    ),
    longDesc = 
u"""
404
""",
)

entry(
    index = 375,
    label = "CH4 + CH3 <=> C2H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (167004, 'J/mol'),
        T0 = (1, 'K'),
        comment = '405',
    ),
    longDesc = 
u"""
405
""",
)

entry(
    index = 376,
    label = "CH4 + CH3 <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (96456.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '406',
    ),
    longDesc = 
u"""
406
""",
)

entry(
    index = 377,
    label = "C2H + C2H6 <=> C2H2 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+12, 'cm^3/(mol*s)'),
        n = 0.28,
        Ea = (-515.497, 'J/mol'),
        T0 = (1, 'K'),
        comment = '407',
    ),
    longDesc = 
u"""
407
""",
)

entry(
    index = 378,
    label = "C2H2 + O <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+07, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (9229.06, 'J/mol'),
        T0 = (1, 'K'),
        comment = '408',
    ),
    longDesc = 
u"""
408
""",
)

entry(
    index = 379,
    label = "C2H2 + O <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18873.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '409',
    ),
    longDesc = 
u"""
409
""",
)

entry(
    index = 380,
    label = "C3H8 <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (352534, 'J/mol'),
        T0 = (1, 'K'),
        comment = '410',
    ),
    longDesc = 
u"""
410
""",
)

entry(
    index = 381,
    label = "C4H <=> C4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1'),
        n = 0,
        Ea = (482239, 'J/mol'),
        T0 = (1, 'K'),
        comment = '411',
    ),
    longDesc = 
u"""
411
""",
)

entry(
    index = 382,
    label = "C4H + H <=> C4H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3e+13, 'cm^6/(mol^2*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '412',
    ),
    longDesc = 
u"""
412
""",
)

entry(
    index = 383,
    label = "C4H2 + H <=> H2CCCCH",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.1e+30, 'cm^3/(mol*s)'),
        n = -4.92,
        Ea = (44898.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '413',
    ),
    longDesc = 
u"""
413
""",
)

entry(
    index = 384,
    label = "C4H2 + H2 <=> C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (222828, 'J/mol'),
        T0 = (1, 'K'),
        comment = '414',
    ),
    longDesc = 
u"""
414
""",
)

entry(
    index = 385,
    label = "C2H2 + C2H <=> H2CCCCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.17e+36, 'cm^3/(mol*s)'),
        n = -7.3,
        Ea = (36500.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '415',
    ),
    longDesc = 
u"""
415
""",
)

entry(
    index = 386,
    label = "C3H2 + CH2 <=> H2CCCCH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '416',
    ),
    longDesc = 
u"""
416
""",
)

entry(
    index = 387,
    label = "H2CCCCH + H <=> C4H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '417',
    ),
    longDesc = 
u"""
417
""",
)

entry(
    index = 388,
    label = "H2CCCCH + O <=> CH2CO + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '418',
    ),
    longDesc = 
u"""
418
""",
)

entry(
    index = 389,
    label = "H2CCCCH + OH <=> C4H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '419',
    ),
    longDesc = 
u"""
419
""",
)

entry(
    index = 390,
    label = "H2CCCCH + O2 <=> CH2CO + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '420',
    ),
    longDesc = 
u"""
420
""",
)

entry(
    index = 391,
    label = "H2CCCCH + H2 <=> C2H2 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (83144.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '421',
    ),
    longDesc = 
u"""
421
""",
)

entry(
    index = 392,
    label = "H2CCCCH + CH2 <=> C3H4 + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '422',
    ),
    longDesc = 
u"""
422
""",
)

entry(
    index = 393,
    label = "H2CCCCH + C2H3 <=> H2CCCH + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '423',
    ),
    longDesc = 
u"""
423
""",
)

entry(
    index = 394,
    label = "C4H4 <=> C2H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+13, 's^-1'),
        n = 0,
        Ea = (320689, 'J/mol'),
        T0 = (1, 'K'),
        comment = '424',
    ),
    longDesc = 
u"""
424
""",
)

entry(
    index = 395,
    label = "C4H4 <=> H2CCCCH + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.1e+20, 'cm^3/(mol*s)'), n=0, Ea=(412720, 'J/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '425',
    ),
    longDesc = 
u"""
425
""",
)

entry(
    index = 396,
    label = "C4H4 + O <=> HCO + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+08, 'cm^3/(mol*s)'),
        n = 1.44,
        Ea = (2298.95, 'J/mol'),
        T0 = (1, 'K'),
        comment = '426',
    ),
    longDesc = 
u"""
426
""",
)

entry(
    index = 397,
    label = "C4H4 + H <=> H2CCCCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (24943.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '427',
    ),
    longDesc = 
u"""
427
""",
)

entry(
    index = 398,
    label = "H2CCCH + CH2 <=> H + C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '428',
    ),
    longDesc = 
u"""
428
""",
)

entry(
    index = 399,
    label = "C2H3 + C2H2 <=> H + C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20786.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '429',
    ),
    longDesc = 
u"""
429
""",
)

entry(
    index = 400,
    label = "C4H4 + O <=> C3H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7649.31, 'J/mol'),
        T0 = (1, 'K'),
        comment = '430',
    ),
    longDesc = 
u"""
430
""",
)

entry(
    index = 401,
    label = "C4H4 + OH <=> H2CCCCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (21001.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '431',
    ),
    longDesc = 
u"""
431
""",
)

entry(
    index = 402,
    label = "C4H4 + C2H <=> C4H2 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '432',
    ),
    longDesc = 
u"""
432
""",
)

entry(
    index = 403,
    label = "C4H4 + C2H <=> H2CCCCH + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '433',
    ),
    longDesc = 
u"""
433
""",
)

entry(
    index = 404,
    label = "C4H4 + C2H3 <=> H2CCCCH + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (67762.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '434',
    ),
    longDesc = 
u"""
434
""",
)

entry(
    index = 405,
    label = "i-C4H5 <=> C2H3 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (182503, 'J/mol'),
        T0 = (1, 'K'),
        comment = '435',
    ),
    longDesc = 
u"""
435
""",
)

entry(
    index = 406,
    label = "i-C4H5 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(207872, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2e+15, 'cm^3/(mol*s)'), n=0, Ea=(174604, 'J/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '436',
    ),
    longDesc = 
u"""
436
""",
)

entry(
    index = 407,
    label = "i-C4H5 + O2 <=> C4H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12471.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '437',
    ),
    longDesc = 
u"""
437
""",
)

entry(
    index = 408,
    label = "i-C4H5 + O2 <=> CH2CO + CH2HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+17, 'cm^3/(mol*s)'),
        n = -1.8,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '438',
    ),
    longDesc = 
u"""
438
""",
)

entry(
    index = 409,
    label = "i-C4H5 + H <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '439',
    ),
    longDesc = 
u"""
439
""",
)

entry(
    index = 410,
    label = "i-C4H5 + H <=> C4H6",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+15, 'cm^6/(mol^2*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '440',
    ),
    longDesc = 
u"""
440
""",
)

entry(
    index = 411,
    label = "i-C4H5 + H <=> H2CCCH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8314.47, 'J/mol'),
        T0 = (1, 'K'),
        comment = '441',
    ),
    longDesc = 
u"""
441
""",
)

entry(
    index = 412,
    label = "i-C4H5 + OH <=> C4H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (4180.52, 'J/mol'),
        T0 = (1, 'K'),
        comment = '442',
    ),
    longDesc = 
u"""
442
""",
)

entry(
    index = 413,
    label = "i-C4H5 + C2H <=> H2CCCH + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '443',
    ),
    longDesc = 
u"""
443
""",
)

entry(
    index = 414,
    label = "C4H6 <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+15, 's^-1'),
        n = 0,
        Ea = (390780, 'J/mol'),
        T0 = (1, 'K'),
        comment = '444',
    ),
    longDesc = 
u"""
444
""",
)

entry(
    index = 415,
    label = "C4H6 <=> C2H2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (307635, 'J/mol'),
        T0 = (1, 'K'),
        comment = '445',
    ),
    longDesc = 
u"""
445
""",
)

entry(
    index = 416,
    label = "C4H6 <=> H2CCCH + CH3",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (2e+15, 's^-1'),
        n = 0,
        Ea = (311793, 'J/mol'),
        T0 = (1, 'K'),
        comment = '446',
    ),
    longDesc = 
u"""
446
""",
)

entry(
    index = 417,
    label = "C4H6 + O2 <=> i-C4H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (236131, 'J/mol'),
        T0 = (1, 'K'),
        comment = '447',
    ),
    longDesc = 
u"""
447
""",
)

entry(
    index = 418,
    label = "C4H6 + O <=> i-C4H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.11e+08, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (19501.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '448',
    ),
    longDesc = 
u"""
448
""",
)

entry(
    index = 419,
    label = "C4H6 + O <=> C3H5 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (3658.37, 'J/mol'),
        T0 = (1, 'K'),
        comment = '449',
    ),
    longDesc = 
u"""
449
""",
)

entry(
    index = 420,
    label = "C4H6 + H <=> C3H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8663.68, 'J/mol'),
        T0 = (1, 'K'),
        comment = '450',
    ),
    longDesc = 
u"""
450
""",
)

entry(
    index = 421,
    label = "C4H6 + H <=> i-C4H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (660000, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (38550, 'J/mol'),
        T0 = (1, 'K'),
        comment = '451',
    ),
    longDesc = 
u"""
451
""",
)

entry(
    index = 422,
    label = "C4H6 + OH <=> i-C4H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1679.52, 'J/mol'),
        T0 = (1, 'K'),
        comment = '452',
    ),
    longDesc = 
u"""
452
""",
)

entry(
    index = 423,
    label = "C4H6 + OH <=> C2H5 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '453',
    ),
    longDesc = 
u"""
453
""",
)

entry(
    index = 424,
    label = "C4H6 + OH <=> CH3CHO + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3325.79, 'J/mol'),
        T0 = (1, 'K'),
        comment = '454',
    ),
    longDesc = 
u"""
454
""",
)

entry(
    index = 425,
    label = "C4H6 + CH3 <=> i-C4H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (64936, 'J/mol'),
        T0 = (1, 'K'),
        comment = '455',
    ),
    longDesc = 
u"""
455
""",
)

entry(
    index = 426,
    label = "C4H6 + C2H3 <=> i-C4H5 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (82978.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '456',
    ),
    longDesc = 
u"""
456
""",
)

entry(
    index = 427,
    label = "C4H6 + H2CCCH <=> i-C4H5 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (81731.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '457',
    ),
    longDesc = 
u"""
457
""",
)

entry(
    index = 428,
    label = "nC4H7 <=> C4H6 + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(206199, 'J/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '458',
    ),
    longDesc = 
u"""
458
""",
)

entry(
    index = 429,
    label = "nC4H7 <=> C2H4 + C2H3",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(154649, 'J/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '459',
    ),
    longDesc = 
u"""
459
""",
)

entry(
    index = 430,
    label = "nC4H7 <=> C3H4 + CH3",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(135526, 'J/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '460',
    ),
    longDesc = 
u"""
460
""",
)

entry(
    index = 431,
    label = "nC4H7 + O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '461',
    ),
    longDesc = 
u"""
461
""",
)

entry(
    index = 432,
    label = "nC4H7 + H <=> C4H6 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '462',
    ),
    longDesc = 
u"""
462
""",
)

entry(
    index = 433,
    label = "nC4H7 + CH3 <=> C4H6 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '463',
    ),
    longDesc = 
u"""
463
""",
)

entry(
    index = 434,
    label = "nC4H7 + C2H3 <=> C4H6 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '464',
    ),
    longDesc = 
u"""
464
""",
)

entry(
    index = 435,
    label = "nC4H7 + C2H5 <=> C4H6 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '465',
    ),
    longDesc = 
u"""
465
""",
)

entry(
    index = 436,
    label = "nC4H7 + C2H5 <=> C4H8 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '466',
    ),
    longDesc = 
u"""
466
""",
)

entry(
    index = 437,
    label = "nC4H7 + C3H5 <=> C4H6 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '467',
    ),
    longDesc = 
u"""
467
""",
)

entry(
    index = 438,
    label = "H2CCCH + C2H3 <=> C5H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+40, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (119812, 'J/mol'),
        T0 = (1, 'K'),
        comment = '468',
    ),
    longDesc = 
u"""
468
""",
)

entry(
    index = 439,
    label = "H2CCCH + C2H2 <=> C5H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+55, 'cm^3/(mol*s)'),
        n = -12.5,
        Ea = (17493.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '469',
    ),
    longDesc = 
u"""
469
""",
)

entry(
    index = 440,
    label = "C5H5 + O2 <=> CH2CO + C2H2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+19, 'cm^3/(mol*s)'),
        n = -2.48,
        Ea = (45563.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '470',
    ),
    longDesc = 
u"""
470
""",
)

entry(
    index = 441,
    label = "C5H6 + O2 <=> C5H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (104762, 'J/mol'),
        T0 = (1, 'K'),
        comment = '471',
    ),
    longDesc = 
u"""
471
""",
)

entry(
    index = 442,
    label = "C5H5 + O <=> i-C4H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '472',
    ),
    longDesc = 
u"""
472
""",
)

entry(
    index = 443,
    label = "C5H6 + H <=> C5H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9453.55, 'J/mol'),
        T0 = (1, 'K'),
        comment = '473',
    ),
    longDesc = 
u"""
473
""",
)

entry(
    index = 444,
    label = "C5H6 + H <=> C3H5 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (51549.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '474',
    ),
    longDesc = 
u"""
474
""",
)

entry(
    index = 445,
    label = "C5H5 + H <=> C5H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '475',
    ),
    longDesc = 
u"""
475
""",
)

entry(
    index = 446,
    label = "C5H5 + OH <=> CH2O + C2H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (324264, 'J/mol'),
        T0 = (1, 'K'),
        comment = '476',
    ),
    longDesc = 
u"""
476
""",
)

entry(
    index = 447,
    label = "C5H6 + OH <=> C5H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-1870.76, 'J/mol'),
        T0 = (1, 'K'),
        comment = '477',
    ),
    longDesc = 
u"""
477
""",
)

entry(
    index = 448,
    label = "C5H6 + HO2 <=> C5H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (48781, 'J/mol'),
        T0 = (1, 'K'),
        comment = '478',
    ),
    longDesc = 
u"""
478
""",
)

entry(
    index = 449,
    label = "C5H6 + C2H3 <=> C5H5 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '479',
    ),
    longDesc = 
u"""
479
""",
)

entry(
    index = 450,
    label = "C6H5O <=> C5H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.4e+11, 's^-1'),
        n = 0,
        Ea = (183750, 'J/mol'),
        T0 = (1, 'K'),
        comment = '480',
    ),
    longDesc = 
u"""
480
""",
)

entry(
    index = 451,
    label = "C6H5O + O <=> C5H5 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '481',
    ),
    longDesc = 
u"""
481
""",
)

entry(
    index = 452,
    label = "C6H5O + H <=> C5H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '482',
    ),
    longDesc = 
u"""
482
""",
)

entry(
    index = 453,
    label = "C6H5O + H <=> C6H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '483',
    ),
    longDesc = 
u"""
483
""",
)

entry(
    index = 454,
    label = "C6H5OH <=> C5H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0,
        Ea = (254423, 'J/mol'),
        T0 = (1, 'K'),
        comment = '484',
    ),
    longDesc = 
u"""
484
""",
)

entry(
    index = 455,
    label = "C6H5OH + O <=> C6H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (29932.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '485',
    ),
    longDesc = 
u"""
485
""",
)

entry(
    index = 456,
    label = "C6H5OH + H <=> C6H5O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24943.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '486',
    ),
    longDesc = 
u"""
486
""",
)

entry(
    index = 457,
    label = "C6H5OH + OH <=> C6H5O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '487',
    ),
    longDesc = 
u"""
487
""",
)

entry(
    index = 458,
    label = "C6H5OH + C2H3 <=> C6H5O + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '488',
    ),
    longDesc = 
u"""
488
""",
)

entry(
    index = 459,
    label = "H2CCCH + H2CCCH <=> A1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+36, 'cm^3/(mol*s)'),
        n = -7.18,
        Ea = (35203.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '489',
    ),
    longDesc = 
u"""
489
""",
)

entry(
    index = 460,
    label = "H2CCCH + H2CCCH <=> A1- + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+35, 'cm^3/(mol*s)'),
        n = -7.18,
        Ea = (35203.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '490',
    ),
    longDesc = 
u"""
490
""",
)

entry(
    index = 461,
    label = "H2CCCCH + C2H3 <=> A1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '491',
    ),
    longDesc = 
u"""
491
""",
)

entry(
    index = 462,
    label = "H2CCCCH + C2H3 <=> A1- + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '492',
    ),
    longDesc = 
u"""
492
""",
)

entry(
    index = 463,
    label = "H2CCCH + C3H4 <=> A1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41572.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '493',
    ),
    longDesc = 
u"""
493
""",
)

entry(
    index = 464,
    label = "C2H3 + C4H4 <=> A1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10393.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '494',
    ),
    longDesc = 
u"""
494
""",
)

entry(
    index = 465,
    label = "H2CCCCH + C2H2 <=> A1-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (61942.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '495',
    ),
    longDesc = 
u"""
495
""",
)

entry(
    index = 466,
    label = "C4H4 + C2H2 <=> A1- + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (124717, 'J/mol'),
        T0 = (1, 'K'),
        comment = '496',
    ),
    longDesc = 
u"""
496
""",
)

entry(
    index = 467,
    label = "i-C4H5 + C2H2 <=> A1 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (22449.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '497',
    ),
    longDesc = 
u"""
497
""",
)

entry(
    index = 468,
    label = "i-C4H5 + C2H3 <=> A1 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e-13, 'cm^3/(mol*s)'),
        n = 7.07,
        Ea = (-14966, 'J/mol'),
        T0 = (1, 'K'),
        comment = '498',
    ),
    longDesc = 
u"""
498
""",
)

entry(
    index = 469,
    label = "i-C4H5 + C2H <=> A1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '499',
    ),
    longDesc = 
u"""
499
""",
)

entry(
    index = 470,
    label = "i-C4H5 + C2H <=> A1- + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '500',
    ),
    longDesc = 
u"""
500
""",
)

entry(
    index = 471,
    label = "C5H5 + CH3 <=> A1 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+18, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (249434, 'J/mol'),
        T0 = (1, 'K'),
        comment = '501',
    ),
    longDesc = 
u"""
501
""",
)

entry(
    index = 472,
    label = "C5H6 + C2H3 <=> A1 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.12e+67, 'cm^3/(mol*s)'),
        n = -16.08,
        Ea = (177265, 'J/mol'),
        T0 = (1, 'K'),
        comment = '502',
    ),
    longDesc = 
u"""
502
""",
)

entry(
    index = 473,
    label = "A1 <=> A1- + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+14, 's^-1'),
        n = 0,
        Ea = (449480, 'J/mol'),
        T0 = (1, 'K'),
        comment = '503',
    ),
    longDesc = 
u"""
503
""",
)

entry(
    index = 474,
    label = "A1 <=> C4H4 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+14, 's^-1'),
        n = 0,
        Ea = (449480, 'J/mol'),
        T0 = (1, 'K'),
        comment = '504',
    ),
    longDesc = 
u"""
504
""",
)

entry(
    index = 475,
    label = "A1 + O2 <=> A1- + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (261906, 'J/mol'),
        T0 = (1, 'K'),
        comment = '505',
    ),
    longDesc = 
u"""
505
""",
)

entry(
    index = 476,
    label = "A1 + O <=> A1- + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (61527.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '506',
    ),
    longDesc = 
u"""
506
""",
)

entry(
    index = 477,
    label = "A1 + O <=> C6H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18957, 'J/mol'),
        T0 = (1, 'K'),
        comment = '507',
    ),
    longDesc = 
u"""
507
""",
)

entry(
    index = 478,
    label = "A1 + O <=> C6H5O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18957, 'J/mol'),
        T0 = (1, 'K'),
        comment = '508',
    ),
    longDesc = 
u"""
508
""",
)

entry(
    index = 479,
    label = "A1 + H <=> A1- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (67014.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '509',
    ),
    longDesc = 
u"""
509
""",
)

entry(
    index = 480,
    label = "A1 + OH <=> C6H5OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (43900.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '510',
    ),
    longDesc = 
u"""
510
""",
)

entry(
    index = 481,
    label = "A1 + OH <=> A1- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18790.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '511',
    ),
    longDesc = 
u"""
511
""",
)

entry(
    index = 482,
    label = "A1 + CH3 <=> A1- + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62608, 'J/mol'),
        T0 = (1, 'K'),
        comment = '512',
    ),
    longDesc = 
u"""
512
""",
)

entry(
    index = 483,
    label = "A1 + C2H <=> A1- + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '513',
    ),
    longDesc = 
u"""
513
""",
)

entry(
    index = 484,
    label = "A1 + C4H <=> A1- + C4H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '514',
    ),
    longDesc = 
u"""
514
""",
)

entry(
    index = 485,
    label = "A1 + C6H <=> A1- + C6H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '515',
    ),
    longDesc = 
u"""
515
""",
)

entry(
    index = 486,
    label = "A1 + C8H <=> A1- + C8H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '516',
    ),
    longDesc = 
u"""
516
""",
)

entry(
    index = 487,
    label = "A1- + O2 <=> C6H5O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (25359.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '517',
    ),
    longDesc = 
u"""
517
""",
)

entry(
    index = 488,
    label = "A1- + O <=> C5H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '518',
    ),
    longDesc = 
u"""
518
""",
)

entry(
    index = 489,
    label = "A1- + OH <=> C6H5O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '519',
    ),
    longDesc = 
u"""
519
""",
)

entry(
    index = 490,
    label = "A1- + C6H5OH <=> C6H5O + A1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.91e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18291.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '520',
    ),
    longDesc = 
u"""
520
""",
)

entry(
    index = 491,
    label = "i-C4H5 + C3H4 <=> C7H8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15381.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '521',
    ),
    longDesc = 
u"""
521
""",
)

entry(
    index = 492,
    label = "i-C4H5 + H2CCCH <=> C7H7 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+35, 'cm^3/(mol*s)'),
        n = -7.18,
        Ea = (35203.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '522',
    ),
    longDesc = 
u"""
522
""",
)

entry(
    index = 493,
    label = "A1 + CH2 <=> C7H8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36334.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '523',
    ),
    longDesc = 
u"""
523
""",
)

entry(
    index = 494,
    label = "A1 + CH2(S) <=> C7H8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36334.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '524',
    ),
    longDesc = 
u"""
524
""",
)

entry(
    index = 495,
    label = "C7H8 <=> A1- + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 's^-1'),
        n = 0,
        Ea = (414892, 'J/mol'),
        T0 = (1, 'K'),
        comment = '525',
    ),
    longDesc = 
u"""
525
""",
)

entry(
    index = 496,
    label = "i-C4H5 + H2CCCH <=> C7H8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+36, 'cm^3/(mol*s)'),
        n = -7.18,
        Ea = (35203.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '526',
    ),
    longDesc = 
u"""
526
""",
)

entry(
    index = 497,
    label = "C7H8 + O2 <=> C7H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (172110, 'J/mol'),
        T0 = (1, 'K'),
        comment = '527',
    ),
    longDesc = 
u"""
527
""",
)

entry(
    index = 498,
    label = "C7H8 + O <=> C7H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '528',
    ),
    longDesc = 
u"""
528
""",
)

entry(
    index = 499,
    label = "C7H8 + H <=> A1 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (21201.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '529',
    ),
    longDesc = 
u"""
529
""",
)

entry(
    index = 500,
    label = "C7H8 + H <=> C7H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (34089.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '530',
    ),
    longDesc = 
u"""
530
""",
)

entry(
    index = 501,
    label = "C7H8 + OH <=> C7H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.18e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3658.37, 'J/mol'),
        T0 = (1, 'K'),
        comment = '531',
    ),
    longDesc = 
u"""
531
""",
)

entry(
    index = 502,
    label = "C7H8 + HO2 <=> C7H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62192.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '532',
    ),
    longDesc = 
u"""
532
""",
)

entry(
    index = 503,
    label = "C7H8 + CH3 <=> C7H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46477.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '533',
    ),
    longDesc = 
u"""
533
""",
)

entry(
    index = 504,
    label = "C7H8 + C2H3 <=> C7H7 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (33923, 'J/mol'),
        T0 = (1, 'K'),
        comment = '534',
    ),
    longDesc = 
u"""
534
""",
)

entry(
    index = 505,
    label = "C7H8 + H2CCCH <=> C7H7 + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (63023.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '535',
    ),
    longDesc = 
u"""
535
""",
)

entry(
    index = 506,
    label = "C7H8 + C3H5 <=> C7H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62192.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '536',
    ),
    longDesc = 
u"""
536
""",
)

entry(
    index = 507,
    label = "C7H8 + C5H5 <=> C7H7 + C5H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46394.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '537',
    ),
    longDesc = 
u"""
537
""",
)

entry(
    index = 508,
    label = "C7H8 + A1- <=> C7H7 + A1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46527.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '538',
    ),
    longDesc = 
u"""
538
""",
)

entry(
    index = 509,
    label = "A1- + CH3 <=> C7H7 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '539',
    ),
    longDesc = 
u"""
539
""",
)

entry(
    index = 510,
    label = "C7H7 <=> C4H4 + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1'),
        n = 0,
        Ea = (351702, 'J/mol'),
        T0 = (1, 'K'),
        comment = '540',
    ),
    longDesc = 
u"""
540
""",
)

entry(
    index = 511,
    label = "C7H7 <=> C5H5 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.1e+13, 's^-1'),
        n = 0,
        Ea = (291007, 'J/mol'),
        T0 = (1, 'K'),
        comment = '541',
    ),
    longDesc = 
u"""
541
""",
)

entry(
    index = 512,
    label = "C7H7 + O <=> A1 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '542',
    ),
    longDesc = 
u"""
542
""",
)

entry(
    index = 513,
    label = "C7H7 + O <=> A1- + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '543',
    ),
    longDesc = 
u"""
543
""",
)

entry(
    index = 514,
    label = "C7H7 + H <=> C7H8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '544',
    ),
    longDesc = 
u"""
544
""",
)

entry(
    index = 515,
    label = "C7H7 + HO2 <=> A1 + HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '545',
    ),
    longDesc = 
u"""
545
""",
)

entry(
    index = 516,
    label = "C7H7 + HO2 <=> A1- + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.17e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '546',
    ),
    longDesc = 
u"""
546
""",
)

entry(
    index = 517,
    label = "C7H7 + H + OH <=> A1 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^6/(mol^2*s)'),
        n = 0,
        Ea = (21551.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '547',
    ),
    longDesc = 
u"""
547
""",
)

entry(
    index = 518,
    label = "i-C4H5 + C4H2 <=> A1C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7483.02, 'J/mol'),
        T0 = (1, 'K'),
        comment = '548',
    ),
    longDesc = 
u"""
548
""",
)

entry(
    index = 519,
    label = "A1C2H- + H <=> A1C2H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.6e+75, 'cm^6/(mol^2*s)'),
            n = -16.3,
            Ea = (58201.3, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (0.1, 'K'),
        T1 = (584.9, 'K'),
        T2 = (6113, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = '549',
    ),
    longDesc = 
u"""
549
""",
)

entry(
    index = 520,
    label = "H2CCCCH + C4H2 <=> A1C2H-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+70, 'cm^3/(mol*s)'),
        n = -17.77,
        Ea = (130205, 'J/mol'),
        T0 = (1, 'K'),
        comment = '550',
    ),
    longDesc = 
u"""
550
""",
)

entry(
    index = 521,
    label = "A1- + C4H2 <=> A1C2H + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (91459.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '551',
    ),
    longDesc = 
u"""
551
""",
)

entry(
    index = 522,
    label = "A1- + C2H3 <=> A1C2H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26606.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '552',
    ),
    longDesc = 
u"""
552
""",
)

entry(
    index = 523,
    label = "A1- + C4H4 <=> A1C2H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5656.83, 'J/mol'),
        T0 = (1, 'K'),
        comment = '553',
    ),
    longDesc = 
u"""
553
""",
)

entry(
    index = 524,
    label = "A1 + C2H <=> A1C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '554',
    ),
    longDesc = 
u"""
554
""",
)

entry(
    index = 525,
    label = "A1- + C2H <=> A1C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (2494.34, 'J/mol'),
        T0 = (1, 'K'),
        comment = '555',
    ),
    longDesc = 
u"""
555
""",
)

entry(
    index = 526,
    label = "A1C2H + O <=> A1C2H- + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (34089.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '556',
    ),
    longDesc = 
u"""
556
""",
)

entry(
    index = 527,
    label = "A1C2H + O <=> A1- + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (7898.75, 'J/mol'),
        T0 = (1, 'K'),
        comment = '557',
    ),
    longDesc = 
u"""
557
""",
)

entry(
    index = 528,
    label = "A1C2H + O <=> C6H5O + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18790.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '558',
    ),
    longDesc = 
u"""
558
""",
)

entry(
    index = 529,
    label = "A1C2H + H <=> A1C2H- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40591.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '559',
    ),
    longDesc = 
u"""
559
""",
)

entry(
    index = 530,
    label = "A1C2H + H <=> A1- + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40591.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '560',
    ),
    longDesc = 
u"""
560
""",
)

entry(
    index = 531,
    label = "A1C2H + H <=> n-C8H7",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (3e+43, 'cm^3/(mol*s)'),
        n = -9.22,
        Ea = (63289.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '561',
    ),
    longDesc = 
u"""
561
""",
)

entry(
    index = 532,
    label = "A1C2H + OH <=> A1C2H- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19123.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '562',
    ),
    longDesc = 
u"""
562
""",
)

entry(
    index = 533,
    label = "A1C2H + OH <=> A1- + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000218, 'cm^3/(mol*s)'),
        n = 4.5,
        Ea = (-4157.24, 'J/mol'),
        T0 = (1, 'K'),
        comment = '563',
    ),
    longDesc = 
u"""
563
""",
)

entry(
    index = 534,
    label = "A1C2H + OH <=> A1 + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2440, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (46344.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '564',
    ),
    longDesc = 
u"""
564
""",
)

entry(
    index = 535,
    label = "A1C2H + C2H <=> A1C2H- + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '565',
    ),
    longDesc = 
u"""
565
""",
)

entry(
    index = 536,
    label = "C4H4 + C4H4 <=> A1C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+20, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (168202, 'J/mol'),
        T0 = (1, 'K'),
        comment = '566',
    ),
    longDesc = 
u"""
566
""",
)

entry(
    index = 537,
    label = "i-C4H5 + C4H4 <=> A1C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2494.34, 'J/mol'),
        T0 = (1, 'K'),
        comment = '567',
    ),
    longDesc = 
u"""
567
""",
)

entry(
    index = 538,
    label = "C5H5 + H2CCCH <=> A1C2H3* + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+35, 'cm^3/(mol*s)'),
        n = -7.18,
        Ea = (35203.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '568\nRxn 568 commented out because reverse rate coefficient is above Z',
    ),
    longDesc = 
u"""
568
Rxn 568 commented out because reverse rate coefficient is above Z
""",
)

entry(
    index = 539,
    label = "A1 + C2H3 <=> A1C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26606.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '569',
    ),
    longDesc = 
u"""
569
""",
)

entry(
    index = 540,
    label = "A1- + C2H3 <=> A1C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+26, 'cm^3/(mol*s)'),
        n = -4,
        Ea = (22033.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '570',
    ),
    longDesc = 
u"""
570
""",
)

entry(
    index = 541,
    label = "A1- + C2H4 <=> A1C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (25733.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '571',
    ),
    longDesc = 
u"""
571
""",
)

entry(
    index = 542,
    label = "A1- + C4H4 <=> A1C2H3 + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (83144.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '572',
    ),
    longDesc = 
u"""
572
""",
)

entry(
    index = 543,
    label = "A1- + C4H6 <=> A1C2H3 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7961.44, 'J/mol'),
        T0 = (1, 'K'),
        comment = '573',
    ),
    longDesc = 
u"""
573
""",
)

entry(
    index = 544,
    label = "C7H7 + CH2 <=> A1C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '574',
    ),
    longDesc = 
u"""
574
""",
)

entry(
    index = 545,
    label = "A1C2H3 + H <=> n-C8H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.65e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (50884.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '575',
    ),
    longDesc = 
u"""
575
""",
)

entry(
    index = 546,
    label = "A1C2H3 + H <=> A1C2H3* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (303, 'cm^3/(mol*s)'),
        n = 3.3,
        Ea = (23862.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '576',
    ),
    longDesc = 
u"""
576
""",
)

entry(
    index = 547,
    label = "A1C2H3 + O <=> A1- + CH2HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (3741.51, 'J/mol'),
        T0 = (1, 'K'),
        comment = '577',
    ),
    longDesc = 
u"""
577
""",
)

entry(
    index = 548,
    label = "A1C2H3 + O <=> A1- + CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.92e+07, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (914.592, 'J/mol'),
        T0 = (1, 'K'),
        comment = '578',
    ),
    longDesc = 
u"""
578
""",
)

entry(
    index = 549,
    label = "A1C2H3 + O <=> C2H3 + C6H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18832.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '579',
    ),
    longDesc = 
u"""
579
""",
)

entry(
    index = 550,
    label = "A1C2H3 + O <=> n-C8H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.55e+06, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (15631.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '580',
    ),
    longDesc = 
u"""
580
""",
)

entry(
    index = 551,
    label = "A1C2H3 + OH <=> n-C8H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (14259.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '581',
    ),
    longDesc = 
u"""
581
""",
)

entry(
    index = 552,
    label = "A1C2H3 + OH => C6H5O + C2H4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (44066.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '582',
    ),
    longDesc = 
u"""
582
""",
)

entry(
    index = 553,
    label = "A1C2H3 + OH <=> A1C2H3* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+08, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (6092.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '583',
    ),
    longDesc = 
u"""
583
""",
)

entry(
    index = 554,
    label = "A1C2H3 + OH <=> C7H7 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '584',
    ),
    longDesc = 
u"""
584
""",
)

entry(
    index = 555,
    label = "A1C2H3 + O2 <=> C6H5O + CH2HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (31251.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '585',
    ),
    longDesc = 
u"""
585
""",
)

entry(
    index = 556,
    label = "A1C2H3* + O2 <=> C6H5O + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (31251.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '586',
    ),
    longDesc = 
u"""
586
""",
)

entry(
    index = 557,
    label = "A1C2H3* + H <=> A1C2H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.6e+75, 'cm^6/(mol^2*s)'),
            n = -16.3,
            Ea = (58201.3, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (0.1, 'K'),
        T1 = (584.9, 'K'),
        T2 = (6113, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = '587',
    ),
    longDesc = 
u"""
587
""",
)

entry(
    index = 558,
    label = "C5H5 + H2CCCH <=> n-C8H7 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+35, 'cm^3/(mol*s)'),
        n = -7.18,
        Ea = (35203.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '588\nRxn 588 commented out because k>Z for T<1400 K',
    ),
    longDesc = 
u"""
588
Rxn 588 commented out because k>Z for T<1400 K
""",
)

entry(
    index = 559,
    label = "A1 + C2H <=> n-C8H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+38, 'cm^3/(mol*s)'),
        n = -8.02,
        Ea = (68178.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '589',
    ),
    longDesc = 
u"""
589
""",
)

entry(
    index = 560,
    label = "A1- + C2H2 <=> n-C8H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (48872.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '590',
    ),
    longDesc = 
u"""
590
""",
)

entry(
    index = 561,
    label = "A1- + C2H3 <=> n-C8H7 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.4, 'cm^3/(mol*s)'),
        n = 4.14,
        Ea = (96589.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '591',
    ),
    longDesc = 
u"""
591
""",
)

entry(
    index = 562,
    label = "n-C8H7 <=> A1C2H + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2e+17, 'cm^3/(mol*s)'), n=0, Ea=(166289, 'J/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '592',
    ),
    longDesc = 
u"""
592
""",
)

entry(
    index = 563,
    label = "n-C8H7 + H <=> A1C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10060.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '593',
    ),
    longDesc = 
u"""
593
""",
)

entry(
    index = 564,
    label = "n-C8H7 + H <=> A1C2H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '594',
    ),
    longDesc = 
u"""
594
""",
)

entry(
    index = 565,
    label = "n-C8H7 + OH <=> A1C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '595',
    ),
    longDesc = 
u"""
595
""",
)

entry(
    index = 566,
    label = "C5H5 + C4H4 <=> INDENE + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41821.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '596',
    ),
    longDesc = 
u"""
596
""",
)

entry(
    index = 567,
    label = "A1- + H2CCCH <=> INDENE",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.86e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (56954.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '597',
    ),
    longDesc = 
u"""
597
""",
)

entry(
    index = 568,
    label = "C4H6 + A1- <=> INDENE + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1164.03, 'J/mol'),
        T0 = (1, 'K'),
        comment = '598',
    ),
    longDesc = 
u"""
598
""",
)

entry(
    index = 569,
    label = "i-C4H5 + A1 <=> INDENE + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1164.03, 'J/mol'),
        T0 = (1, 'K'),
        comment = '599',
    ),
    longDesc = 
u"""
599
""",
)

entry(
    index = 570,
    label = "A1- + C3H4 <=> INDENE + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (138020, 'J/mol'),
        T0 = (1, 'K'),
        comment = '600',
    ),
    longDesc = 
u"""
600
""",
)

entry(
    index = 571,
    label = "INDENE <=> INDENYL + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+15, 's^-1'),
        n = 0,
        Ea = (322602, 'J/mol'),
        T0 = (1, 'K'),
        comment = '601',
    ),
    longDesc = 
u"""
601
""",
)

entry(
    index = 572,
    label = "INDENE + O <=> INDENYL + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '602',
    ),
    longDesc = 
u"""
602
""",
)

entry(
    index = 573,
    label = "INDENE + O <=> C7H7 + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16628.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '603',
    ),
    longDesc = 
u"""
603
""",
)

entry(
    index = 574,
    label = "INDENE + H <=> INDENYL + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '604',
    ),
    longDesc = 
u"""
604
""",
)

entry(
    index = 575,
    label = "C7H7 + C2H2 <=> INDENE + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41821.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '605',
    ),
    longDesc = 
u"""
605
""",
)

entry(
    index = 576,
    label = "INDENE + H <=> A1C2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (191233, 'J/mol'),
        T0 = (1, 'K'),
        comment = '606',
    ),
    longDesc = 
u"""
606
""",
)

entry(
    index = 577,
    label = "INDENE + H <=> A1 + H2CCCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (203705, 'J/mol'),
        T0 = (1, 'K'),
        comment = '607',
    ),
    longDesc = 
u"""
607
""",
)

entry(
    index = 578,
    label = "INDENE + OH <=> C7H7 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41572.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '608',
    ),
    longDesc = 
u"""
608
""",
)

entry(
    index = 579,
    label = "INDENE + OH <=> INDENYL + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '609',
    ),
    longDesc = 
u"""
609
""",
)

entry(
    index = 580,
    label = "INDENE + CH3 <=> INDENYL + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (58201.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '610',
    ),
    longDesc = 
u"""
610
""",
)

entry(
    index = 581,
    label = "INDENE + H2CCCH <=> INDENYL + C3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (23032.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '611',
    ),
    longDesc = 
u"""
611
""",
)

entry(
    index = 582,
    label = "INDENE + A1- <=> INDENYL + A1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24943.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '612',
    ),
    longDesc = 
u"""
612
""",
)

entry(
    index = 583,
    label = "INDENE + C7H7 <=> INDENYL + C7H8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (29100.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '613',
    ),
    longDesc = 
u"""
613
""",
)

entry(
    index = 584,
    label = "C5H5 + C4H2 <=> INDENYL",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41821.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '614',
    ),
    longDesc = 
u"""
614
""",
)

entry(
    index = 585,
    label = "INDENYL => C2H2 + C4H2 + H2CCCH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (311793, 'J/mol'),
        T0 = (1, 'K'),
        comment = '615',
    ),
    longDesc = 
u"""
615
""",
)

entry(
    index = 586,
    label = "INDENYL + O <=> n-C8H7 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '616',
    ),
    longDesc = 
u"""
616
""",
)

entry(
    index = 587,
    label = "INDENYL + O <=> A1C2H3* + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '617',
    ),
    longDesc = 
u"""
617
""",
)

entry(
    index = 588,
    label = "INDENYL + HO2 => n-C8H7 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '618',
    ),
    longDesc = 
u"""
618
""",
)

entry(
    index = 589,
    label = "INDENYL + HO2 => A1C2H + CO + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '619',
    ),
    longDesc = 
u"""
619
""",
)

entry(
    index = 590,
    label = "INDENYL + HO2 => A1C2H3* + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '620',
    ),
    longDesc = 
u"""
620
""",
)

entry(
    index = 591,
    label = "A1- + A1 <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+23, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (61942.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '621',
    ),
    longDesc = 
u"""
621
""",
)

entry(
    index = 592,
    label = "INDENYL + H2CCCH => P2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (58201.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '622',
    ),
    longDesc = 
u"""
622
""",
)

entry(
    index = 593,
    label = "INDENE + H2CCCH => P2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.55e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (215445, 'J/mol'),
        T0 = (1, 'K'),
        comment = '623',
    ),
    longDesc = 
u"""
623
""",
)

entry(
    index = 594,
    label = "A1- + A1- <=> P2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+19, 'cm^3/(mol*s)'),
        n = -2.05,
        Ea = (12056, 'J/mol'),
        T0 = (1, 'K'),
        comment = '624',
    ),
    longDesc = 
u"""
624
""",
)

entry(
    index = 595,
    label = "A1- + A1- <=> P2- + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.23, 'cm^3/(mol*s)'),
        n = 4.62,
        Ea = (120560, 'J/mol'),
        T0 = (1, 'K'),
        comment = '625',
    ),
    longDesc = 
u"""
625
""",
)

entry(
    index = 596,
    label = "P2 <=> P2- + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+19, 's^-1'),
        n = -2.72,
        Ea = (476419, 'J/mol'),
        T0 = (1, 'K'),
        comment = '626',
    ),
    longDesc = 
u"""
626
""",
)

entry(
    index = 597,
    label = "P2 <=> INDENE + C3H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 's^-1'),
        n = 0,
        Ea = (457296, 'J/mol'),
        T0 = (1, 'K'),
        comment = '627',
    ),
    longDesc = 
u"""
627
""",
)

entry(
    index = 598,
    label = "P2- + O2 <=> A2 + HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30763.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '628',
    ),
    longDesc = 
u"""
628
""",
)

entry(
    index = 599,
    label = "P2 + H <=> P2- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66515.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '629',
    ),
    longDesc = 
u"""
629
""",
)

entry(
    index = 600,
    label = "P2 + OH <=> P2- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+08, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (6402.14, 'J/mol'),
        T0 = (1, 'K'),
        comment = '630',
    ),
    longDesc = 
u"""
630
""",
)

entry(
    index = 601,
    label = "i-C4H5 + A1 => A2 + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12500, 'J/mol'),
        T0 = (1, 'K'),
        comment = '631',
    ),
    longDesc = 
u"""
631
""",
)

entry(
    index = 602,
    label = "C4H6 + A1- => A2 + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12500, 'J/mol'),
        T0 = (1, 'K'),
        comment = '632',
    ),
    longDesc = 
u"""
632
""",
)

entry(
    index = 603,
    label = "A1- + H2CCCCH <=> A2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.18e+23, 'cm^3/(mol*s)'),
        n = -3.2,
        Ea = (17709.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '633',
    ),
    longDesc = 
u"""
633
""",
)

entry(
    index = 604,
    label = "A1- + H2CCCCH <=> A2- + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-10, 'cm^3/(mol*s)'),
        n = 7.1,
        Ea = (6536.75, 'J/mol'),
        T0 = (1, 'K'),
        comment = '634',
    ),
    longDesc = 
u"""
634
""",
)

entry(
    index = 605,
    label = "A1- + C4H4 <=> A2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+33, 'cm^3/(mol*s)'),
        n = -5.7,
        Ea = (106010, 'J/mol'),
        T0 = (1, 'K'),
        comment = '635',
    ),
    longDesc = 
u"""
635
""",
)

entry(
    index = 606,
    label = "C7H7 + H2CCCH => A2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (582.013, 'J/mol'),
        T0 = (1, 'K'),
        comment = '636',
    ),
    longDesc = 
u"""
636
""",
)

entry(
    index = 607,
    label = "A1C2H- + C2H2 <=> A2-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (42403.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '637',
    ),
    longDesc = 
u"""
637
""",
)

entry(
    index = 608,
    label = "A1C2H3* + C2H2 <=> A2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (27437.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '638',
    ),
    longDesc = 
u"""
638
""",
)

entry(
    index = 609,
    label = "n-C8H7 + C2H2 <=> A2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (22449.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '639',
    ),
    longDesc = 
u"""
639
""",
)

entry(
    index = 610,
    label = "INDENYL + CH3 <=> A2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+18, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (303478, 'J/mol'),
        T0 = (1, 'K'),
        comment = '640\nRxn 640 commented out because k>Z for T>2000 K',
    ),
    longDesc = 
u"""
640
Rxn 640 commented out because k>Z for T>2000 K
""",
)

entry(
    index = 611,
    label = "INDENE + CH2 => A2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36334.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '641',
    ),
    longDesc = 
u"""
641
""",
)

entry(
    index = 612,
    label = "INDENE + CH2(S) <=> A2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36334.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '642',
    ),
    longDesc = 
u"""
642
""",
)

entry(
    index = 613,
    label = "A2 + O <=> CH2CO + A1C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18832.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '643',
    ),
    longDesc = 
u"""
643
""",
)

entry(
    index = 614,
    label = "A2 + O => INDENYL + CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.6e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (183692, 'J/mol'),
        T0 = (1, 'K'),
        comment = '644',
    ),
    longDesc = 
u"""
644
""",
)

entry(
    index = 615,
    label = "A2 + O <=> n-C8H7 + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (174604, 'J/mol'),
        T0 = (1, 'K'),
        comment = '645',
    ),
    longDesc = 
u"""
645
""",
)

entry(
    index = 616,
    label = "A2 + O <=> A1C2H3* + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (174604, 'J/mol'),
        T0 = (1, 'K'),
        comment = '646',
    ),
    longDesc = 
u"""
646
""",
)

entry(
    index = 617,
    label = "A2 + O <=> A2- + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (61527.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '647',
    ),
    longDesc = 
u"""
647
""",
)

entry(
    index = 618,
    label = "A2 + H <=> A2- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66515.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '648',
    ),
    longDesc = 
u"""
648
""",
)

entry(
    index = 619,
    label = "A2 + OH <=> A2- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19123.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '649',
    ),
    longDesc = 
u"""
649
""",
)

entry(
    index = 620,
    label = "A2 + OH => A1C2H + CH2CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (44066.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '650',
    ),
    longDesc = 
u"""
650
""",
)

entry(
    index = 621,
    label = "A2 + CH3 <=> A2- + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62608, 'J/mol'),
        T0 = (1, 'K'),
        comment = '651',
    ),
    longDesc = 
u"""
651
""",
)

entry(
    index = 622,
    label = "A2 + C2H <=> A2- + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66515.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '652',
    ),
    longDesc = 
u"""
652
""",
)

entry(
    index = 623,
    label = "A2 + C2H <=> A2C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '653',
    ),
    longDesc = 
u"""
653
""",
)

entry(
    index = 624,
    label = "A2- + O2 => A1C2H + HCO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30763.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '654',
    ),
    longDesc = 
u"""
654
""",
)

entry(
    index = 625,
    label = "A2- + O => INDENYL + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '655',
    ),
    longDesc = 
u"""
655
""",
)

entry(
    index = 626,
    label = "A2- + H <=> A2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '656',
    ),
    longDesc = 
u"""
656
""",
)

entry(
    index = 627,
    label = "A2- + HO2 => INDENYL + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '657',
    ),
    longDesc = 
u"""
657
""",
)

entry(
    index = 628,
    label = "A2- + C2H2 <=> A2C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+24, 'cm^3/(mol*s)'),
        n = -3.06,
        Ea = (93953.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '658',
    ),
    longDesc = 
u"""
658
""",
)

entry(
    index = 629,
    label = "A2C2H + H <=> A2C2H* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66515.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '659',
    ),
    longDesc = 
u"""
659
""",
)

entry(
    index = 630,
    label = "A2C2H + OH <=> A2- + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000218, 'cm^3/(mol*s)'),
        n = 4.5,
        Ea = (-4157.24, 'J/mol'),
        T0 = (1, 'K'),
        comment = '660',
    ),
    longDesc = 
u"""
660
""",
)

entry(
    index = 631,
    label = "A2C2H + OH <=> A2C2H* + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19123.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '661',
    ),
    longDesc = 
u"""
661
""",
)

entry(
    index = 632,
    label = "INDENYL + H2CCCH => A2C2H + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '662',
    ),
    longDesc = 
u"""
662
""",
)

entry(
    index = 633,
    label = "A2 + CH2 <=> A2CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36334.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '663',
    ),
    longDesc = 
u"""
663
""",
)

entry(
    index = 634,
    label = "A2 + CH2(S) <=> A2CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36334.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '664',
    ),
    longDesc = 
u"""
664
""",
)

entry(
    index = 635,
    label = "A2CH3 <=> A2- + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (405746, 'J/mol'),
        T0 = (1, 'K'),
        comment = '665',
    ),
    longDesc = 
u"""
665
""",
)

entry(
    index = 636,
    label = "A2CH3 <=> A2CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.81e+15, 's^-1'),
        n = 0,
        Ea = (371657, 'J/mol'),
        T0 = (1, 'K'),
        comment = '666',
    ),
    longDesc = 
u"""
666
""",
)

entry(
    index = 637,
    label = "A2CH3 + O2 <=> A2CH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (173008, 'J/mol'),
        T0 = (1, 'K'),
        comment = '667',
    ),
    longDesc = 
u"""
667
""",
)

entry(
    index = 638,
    label = "A2CH3 + O <=> A2CH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5379.46, 'J/mol'),
        T0 = (1, 'K'),
        comment = '668',
    ),
    longDesc = 
u"""
668
""",
)

entry(
    index = 639,
    label = "A2CH3 + H <=> A2CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (398, 'cm^3/(mol*s)'),
        n = 3.44,
        Ea = (12970.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '669',
    ),
    longDesc = 
u"""
669
""",
)

entry(
    index = 640,
    label = "A2CH3 + H <=> A2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (21201.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '670',
    ),
    longDesc = 
u"""
670
""",
)

entry(
    index = 641,
    label = "A2CH3 + OH <=> A2CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.19e+08, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3658.37, 'J/mol'),
        T0 = (1, 'K'),
        comment = '671',
    ),
    longDesc = 
u"""
671
""",
)

entry(
    index = 642,
    label = "A2CH3 + HO2 <=> A2CH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (58201.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '672',
    ),
    longDesc = 
u"""
672
""",
)

entry(
    index = 643,
    label = "A2CH3 + CH3 <=> A2CH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (45729.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '673',
    ),
    longDesc = 
u"""
673
""",
)

entry(
    index = 644,
    label = "A2CH2 + O <=> A2- + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '674',
    ),
    longDesc = 
u"""
674
""",
)

entry(
    index = 645,
    label = "A2CH2 + HO2 <=> A2- + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '675',
    ),
    longDesc = 
u"""
675
""",
)

entry(
    index = 646,
    label = "A2CH2 + CH2 <=> A2C2H + H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '676',
    ),
    longDesc = 
u"""
676
""",
)

entry(
    index = 647,
    label = "A2CH2 + H2CCCH <=> A3 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (58201.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '677',
    ),
    longDesc = 
u"""
677
""",
)

entry(
    index = 648,
    label = "A1C2H- + C4H4 <=> A2R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (27437.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '678',
    ),
    longDesc = 
u"""
678
""",
)

entry(
    index = 649,
    label = "A1C2H3* + C4H2 <=> A2R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (22449.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '679',
    ),
    longDesc = 
u"""
679
""",
)

entry(
    index = 650,
    label = "n-C8H7 + C4H2 <=> A2R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (22449.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '680',
    ),
    longDesc = 
u"""
680
""",
)

entry(
    index = 651,
    label = "INDENYL + H2CCCH => A2R5 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40643.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '681',
    ),
    longDesc = 
u"""
681
""",
)

entry(
    index = 652,
    label = "INDENE + H2CCCH => A2R5 + H + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.55e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (215445, 'J/mol'),
        T0 = (1, 'K'),
        comment = '682',
    ),
    longDesc = 
u"""
682
""",
)

entry(
    index = 653,
    label = "INDENYL + H2CCCH <=> A2R5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '683',
    ),
    longDesc = 
u"""
683
""",
)

entry(
    index = 654,
    label = "A2- + C2H2 <=> A2R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+31, 'cm^3/(mol*s)'),
        n = -5.26,
        Ea = (87302, 'J/mol'),
        T0 = (1, 'K'),
        comment = '684',
    ),
    longDesc = 
u"""
684
""",
)

entry(
    index = 655,
    label = "A2C2H* + H <=> A2R5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '685',
    ),
    longDesc = 
u"""
685
""",
)

entry(
    index = 656,
    label = "A2C2H + H <=> A2R5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+37, 'cm^3/(mol*s)'),
        n = -7.03,
        Ea = (96032.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '686',
    ),
    longDesc = 
u"""
686
""",
)

entry(
    index = 657,
    label = "A2R5- + H <=> A2R5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.6e+75, 'cm^6/(mol^2*s)'),
            n = -16.3,
            Ea = (29.1007, 'J/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (0.1, 'K'),
        T1 = (585, 'K'),
        T2 = (6113, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.2},
        comment = '687',
    ),
    longDesc = 
u"""
687
""",
)

entry(
    index = 658,
    label = "A2R5 <=> A1C2H + C4H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+16, 's^-1'),
        n = 0,
        Ea = (482239, 'J/mol'),
        T0 = (1, 'K'),
        comment = '688',
    ),
    longDesc = 
u"""
688
""",
)

entry(
    index = 659,
    label = "A2R5 + O <=> A2R5- + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (61527.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '689',
    ),
    longDesc = 
u"""
689
""",
)

entry(
    index = 660,
    label = "A2R5 + O => A2- + HCCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (61527.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '690',
    ),
    longDesc = 
u"""
690
""",
)

entry(
    index = 661,
    label = "A2R5 + H <=> A2R5- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66515.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '691',
    ),
    longDesc = 
u"""
691
""",
)

entry(
    index = 662,
    label = "A2R5 + OH <=> A2R5- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+08, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (6027.99, 'J/mol'),
        T0 = (1, 'K'),
        comment = '692',
    ),
    longDesc = 
u"""
692
""",
)

entry(
    index = 663,
    label = "A2R5 + OH <=> A2- + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41572.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '693',
    ),
    longDesc = 
u"""
693
""",
)

entry(
    index = 664,
    label = "A1C2H + A1- <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+23, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '694',
    ),
    longDesc = 
u"""
694
""",
)

entry(
    index = 665,
    label = "A1C2H- + A1 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+23, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '695',
    ),
    longDesc = 
u"""
695
""",
)

entry(
    index = 666,
    label = "A2- + C4H4 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+33, 'cm^3/(mol*s)'),
        n = -5.7,
        Ea = (106010, 'J/mol'),
        T0 = (1, 'K'),
        comment = '696',
    ),
    longDesc = 
u"""
696
""",
)

entry(
    index = 667,
    label = "A2- + C4H2 <=> A3-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+33, 'cm^3/(mol*s)'),
        n = -5.7,
        Ea = (106010, 'J/mol'),
        T0 = (1, 'K'),
        comment = '697',
    ),
    longDesc = 
u"""
697
""",
)

entry(
    index = 668,
    label = "P2- + C2H2 <=> A3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.64e+06, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (30181.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '698',
    ),
    longDesc = 
u"""
698
""",
)

entry(
    index = 669,
    label = "A2C2H* + C2H2 <=> A3-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+62, 'cm^3/(mol*s)'),
        n = -14.56,
        Ea = (137605, 'J/mol'),
        T0 = (1, 'K'),
        comment = '699',
    ),
    longDesc = 
u"""
699
""",
)

entry(
    index = 670,
    label = "A2R5- + C2H2 <=> A3-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+37, 'cm^3/(mol*s)'),
        n = -8.02,
        Ea = (68178.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '700',
    ),
    longDesc = 
u"""
700
""",
)

entry(
    index = 671,
    label = "A2R5 + C2H2 => A3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (27650, 'cm^3/(mol*s)'),
        n = 2.45,
        Ea = (121682, 'J/mol'),
        T0 = (1, 'K'),
        comment = '701',
    ),
    longDesc = 
u"""
701
""",
)

entry(
    index = 672,
    label = "A2 + C4H2 => A3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (27650, 'cm^3/(mol*s)'),
        n = 2.45,
        Ea = (121682, 'J/mol'),
        T0 = (1, 'K'),
        comment = '702',
    ),
    longDesc = 
u"""
702
""",
)

entry(
    index = 673,
    label = "A3 + O <=> A2C2H + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22989.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '703',
    ),
    longDesc = 
u"""
703
""",
)

entry(
    index = 674,
    label = "A3 + O <=> A3- + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (61527.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '704',
    ),
    longDesc = 
u"""
704
""",
)

entry(
    index = 675,
    label = "A3 + O => HCCO + P2-",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (174604, 'J/mol'),
        T0 = (1, 'K'),
        comment = '705',
    ),
    longDesc = 
u"""
705
""",
)

entry(
    index = 676,
    label = "A3 + H <=> A3- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66515.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '706',
    ),
    longDesc = 
u"""
706
""",
)

entry(
    index = 677,
    label = "A3 + OH <=> A3- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+12, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (6260.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '707\nRxn 707 commented out because k>Z for T>2000 K',
    ),
    longDesc = 
u"""
707
Rxn 707 commented out because k>Z for T>2000 K
""",
)

entry(
    index = 678,
    label = "A3 + OH => A2C2H + CH2CO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41572.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '708',
    ),
    longDesc = 
u"""
708
""",
)

entry(
    index = 679,
    label = "A3 + OH <=> CH2CO + P2-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (133032, 'J/mol'),
        T0 = (1, 'K'),
        comment = '709',
    ),
    longDesc = 
u"""
709
""",
)

entry(
    index = 680,
    label = "A3 + CH3 <=> A3- + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62608, 'J/mol'),
        T0 = (1, 'K'),
        comment = '710',
    ),
    longDesc = 
u"""
710
""",
)

entry(
    index = 681,
    label = "A3 + C2H <=> A3C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '711',
    ),
    longDesc = 
u"""
711
""",
)

entry(
    index = 682,
    label = "A3C2H + H <=> A3C2H* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (303, 'cm^3/(mol*s)'),
        n = 3.3,
        Ea = (23862.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '712',
    ),
    longDesc = 
u"""
712
""",
)

entry(
    index = 683,
    label = "A3C2H + OH <=> A3- + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000218, 'cm^3/(mol*s)'),
        n = 4.5,
        Ea = (-4157.24, 'J/mol'),
        T0 = (1, 'K'),
        comment = '713',
    ),
    longDesc = 
u"""
713
""",
)

entry(
    index = 684,
    label = "A3- + O2 => CO + HCO + A2R5",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30763.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '714',
    ),
    longDesc = 
u"""
714
""",
)

entry(
    index = 685,
    label = "A3- + H <=> A3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '715',
    ),
    longDesc = 
u"""
715
""",
)

entry(
    index = 686,
    label = "A3- + C2H2 <=> A3C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+26, 'cm^3/(mol*s)'),
        n = -3.44,
        Ea = (125549, 'J/mol'),
        T0 = (1, 'K'),
        comment = '716',
    ),
    longDesc = 
u"""
716
""",
)

entry(
    index = 687,
    label = "A3 + CH2 <=> A3CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (29898.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '717',
    ),
    longDesc = 
u"""
717
""",
)

entry(
    index = 688,
    label = "A3 + CH2(S) <=> A3CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (29898.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '718',
    ),
    longDesc = 
u"""
718
""",
)

entry(
    index = 689,
    label = "A3CH2 + H <=> A3- + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (405746, 'J/mol'),
        T0 = (1, 'K'),
        comment = '719',
    ),
    longDesc = 
u"""
719
""",
)

entry(
    index = 690,
    label = "A3CH3 <=> A3CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.81e+15, 's^-1'),
        n = 0,
        Ea = (371657, 'J/mol'),
        T0 = (1, 'K'),
        comment = '720',
    ),
    longDesc = 
u"""
720
""",
)

entry(
    index = 691,
    label = "A3CH3 + O2 <=> A3CH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (173008, 'J/mol'),
        T0 = (1, 'K'),
        comment = '721',
    ),
    longDesc = 
u"""
721
""",
)

entry(
    index = 692,
    label = "A3CH3 + O <=> A3CH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5342.05, 'J/mol'),
        T0 = (1, 'K'),
        comment = '722',
    ),
    longDesc = 
u"""
722
""",
)

entry(
    index = 693,
    label = "A3CH2 + O <=> A3- + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '723',
    ),
    longDesc = 
u"""
723
""",
)

entry(
    index = 694,
    label = "A3CH3 + H <=> A3CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (34920.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '724',
    ),
    longDesc = 
u"""
724
""",
)

entry(
    index = 695,
    label = "A3CH3 + H <=> A3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (21201.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '725',
    ),
    longDesc = 
u"""
725
""",
)

entry(
    index = 696,
    label = "A3CH3 + OH <=> A3CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10601, 'J/mol'),
        T0 = (1, 'K'),
        comment = '726',
    ),
    longDesc = 
u"""
726
""",
)

entry(
    index = 697,
    label = "A3CH3 + HO2 <=> A3CH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (58201.3, 'J/mol'),
        T0 = (1, 'K'),
        comment = '727',
    ),
    longDesc = 
u"""
727
""",
)

entry(
    index = 698,
    label = "A3CH3 + CH3 <=> A3CH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (45729.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '728',
    ),
    longDesc = 
u"""
728
""",
)

entry(
    index = 699,
    label = "A3CH2 + HO2 => A3- + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '729',
    ),
    longDesc = 
u"""
729
""",
)

entry(
    index = 700,
    label = "A3CH2 + CH2 <=> A4 + H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '730',
    ),
    longDesc = 
u"""
730
""",
)

entry(
    index = 701,
    label = "C4H2 + A2R5 => A4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (500, 'cm^3/(mol*s)'),
        n = 2.2313,
        Ea = (-4732.35, 'J/mol'),
        T0 = (1, 'K'),
        comment = '731',
    ),
    longDesc = 
u"""
731
""",
)

entry(
    index = 702,
    label = "A1C2H + A1C2H- <=> A4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '732',
    ),
    longDesc = 
u"""
732
""",
)

entry(
    index = 703,
    label = "n-C8H7 + A1C2H => A4 + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.1e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '733',
    ),
    longDesc = 
u"""
733
""",
)

entry(
    index = 704,
    label = "A1C2H3* + A1C2H => A4 + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.1e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '734',
    ),
    longDesc = 
u"""
734
""",
)

entry(
    index = 705,
    label = "INDENYL + C7H7 => A4 + H2 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.3e+37, 'cm^3/(mol*s)'),
        n = -6.3,
        Ea = (187325, 'J/mol'),
        T0 = (1, 'K'),
        comment = '735',
    ),
    longDesc = 
u"""
735
""",
)

entry(
    index = 706,
    label = "INDENYL + INDENYL => A4 + C2H2 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.3e+36, 'cm^3/(mol*s)'),
        n = -6.3,
        Ea = (187325, 'J/mol'),
        T0 = (1, 'K'),
        comment = '736',
    ),
    longDesc = 
u"""
736
""",
)

entry(
    index = 707,
    label = "A2 + C6H <=> A4-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+37, 'cm^3/(mol*s)'),
        n = -8.02,
        Ea = (68178.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '737',
    ),
    longDesc = 
u"""
737
""",
)

entry(
    index = 708,
    label = "A2 + A1- <=> A4 + H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20786.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '738',
    ),
    longDesc = 
u"""
738
""",
)

entry(
    index = 709,
    label = "A2- + A1 <=> A4 + H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20786.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '739',
    ),
    longDesc = 
u"""
739
""",
)

entry(
    index = 710,
    label = "A2- + A1- => A4 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.3e+37, 'cm^3/(mol*s)'),
        n = -6.3,
        Ea = (187325, 'J/mol'),
        T0 = (1, 'K'),
        comment = '740',
    ),
    longDesc = 
u"""
740
""",
)

entry(
    index = 711,
    label = "A2- + C6H2 <=> A4-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+37, 'cm^3/(mol*s)'),
        n = -8.02,
        Ea = (68178.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '741',
    ),
    longDesc = 
u"""
741
""",
)

entry(
    index = 712,
    label = "A2C2H* + C4H4 <=> A4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+33, 'cm^3/(mol*s)'),
        n = -5.7,
        Ea = (106010, 'J/mol'),
        T0 = (1, 'K'),
        comment = '742',
    ),
    longDesc = 
u"""
742
""",
)

entry(
    index = 713,
    label = "A2R5- + C4H2 => A4-",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7e+37, 'cm^3/(mol*s)'),
        n = -8.02,
        Ea = (68178.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '743',
    ),
    longDesc = 
u"""
743
""",
)

entry(
    index = 714,
    label = "A2R5- + H2CCCCH <=> A4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.4e+23, 'cm^3/(mol*s)'),
        n = -3.2,
        Ea = (17709.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '744',
    ),
    longDesc = 
u"""
744
""",
)

entry(
    index = 715,
    label = "A3- + C2H2 <=> A4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+24, 'cm^3/(mol*s)'),
        n = -3.36,
        Ea = (73998.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '745',
    ),
    longDesc = 
u"""
745
""",
)

entry(
    index = 716,
    label = "A3C2H + H <=> A4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+38, 'cm^3/(mol*s)'),
        n = -7.39,
        Ea = (86470.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '746',
    ),
    longDesc = 
u"""
746
""",
)

entry(
    index = 717,
    label = "A4 + O <=> A3- + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (174604, 'J/mol'),
        T0 = (1, 'K'),
        comment = '747',
    ),
    longDesc = 
u"""
747
""",
)

entry(
    index = 718,
    label = "A4 + H <=> A4- + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66515.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '748',
    ),
    longDesc = 
u"""
748
""",
)

entry(
    index = 719,
    label = "A4 + OH <=> A4- + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (6092.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '749',
    ),
    longDesc = 
u"""
749
""",
)

entry(
    index = 720,
    label = "A4 + OH <=> A3- + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (174604, 'J/mol'),
        T0 = (1, 'K'),
        comment = '750',
    ),
    longDesc = 
u"""
750
""",
)

entry(
    index = 721,
    label = "A4 + CH3 <=> A4- + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (303, 'cm^3/(mol*s)'),
        n = 3.3,
        Ea = (23862.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '751',
    ),
    longDesc = 
u"""
751
""",
)

entry(
    index = 722,
    label = "A4- + O2 <=> CO + CO + A3-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30763.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '752',
    ),
    longDesc = 
u"""
752
""",
)

entry(
    index = 723,
    label = "A4- + H <=> A4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '753',
    ),
    longDesc = 
u"""
753
""",
)

entry(
    index = 724,
    label = "A4- + C2H2 <=> A4C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+26, 'cm^3/(mol*s)'),
        n = -3.44,
        Ea = (125549, 'J/mol'),
        T0 = (1, 'K'),
        comment = '754',
    ),
    longDesc = 
u"""
754
""",
)

entry(
    index = 725,
    label = "A4C2H + H <=> A4C2H* + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (66515.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '755',
    ),
    longDesc = 
u"""
755
""",
)

entry(
    index = 726,
    label = "A4C2H + H <=> BGHIF + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+37, 'cm^3/(mol*s)'),
        n = -7.03,
        Ea = (96032.2, 'J/mol'),
        T0 = (1, 'K'),
        comment = '756',
    ),
    longDesc = 
u"""
756
""",
)

entry(
    index = 727,
    label = "A4C2H* + H <=> BGHIF",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '757',
    ),
    longDesc = 
u"""
757
""",
)

entry(
    index = 728,
    label = "P2 + C6H <=> C18H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+37, 'cm^3/(mol*s)'),
        n = -8.02,
        Ea = (68178.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '758',
    ),
    longDesc = 
u"""
758
""",
)

entry(
    index = 729,
    label = "P2- + C6H2 <=> BGHIF + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '759',
    ),
    longDesc = 
u"""
759
""",
)

entry(
    index = 730,
    label = "P2- + C6H2 <=> C18H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+37, 'cm^3/(mol*s)'),
        n = -8.02,
        Ea = (68178.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '760',
    ),
    longDesc = 
u"""
760
""",
)

entry(
    index = 731,
    label = "A3- + C4H4 <=> C18H12 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+33, 'cm^3/(mol*s)'),
        n = -5.7,
        Ea = (106010, 'J/mol'),
        T0 = (1, 'K'),
        comment = '761',
    ),
    longDesc = 
u"""
761
""",
)

entry(
    index = 732,
    label = "A3C2H* + C2H2 <=> BGHIF + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (27437.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '762',
    ),
    longDesc = 
u"""
762
""",
)

entry(
    index = 733,
    label = "A2R5 + C6H2 => BGHIF",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (241.3, 'cm^3/(mol*s)'),
        n = 2.2313,
        Ea = (-4730.93, 'J/mol'),
        T0 = (1, 'K'),
        comment = '763',
    ),
    longDesc = 
u"""
763
""",
)

entry(
    index = 734,
    label = "A1C2H- + A2 => BGHIF + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.1e+25, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '764',
    ),
    longDesc = 
u"""
764
""",
)

entry(
    index = 735,
    label = "A1C2H + A2- => BGHIF + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.1e+25, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '765',
    ),
    longDesc = 
u"""
765
""",
)

entry(
    index = 736,
    label = "INDENE + INDENYL => C18H12 + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.1e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '766',
    ),
    longDesc = 
u"""
766
""",
)

entry(
    index = 737,
    label = "INDENYL + INDENYL => BGHIF + H2 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.3e+38, 'cm^3/(mol*s)'),
        n = -6.3,
        Ea = (187325, 'J/mol'),
        T0 = (1, 'K'),
        comment = '767',
    ),
    longDesc = 
u"""
767
""",
)

entry(
    index = 738,
    label = "A2 + C8H2 => BGHIF",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (241.3, 'cm^3/(mol*s)'),
        n = 2.2313,
        Ea = (-4731.77, 'J/mol'),
        T0 = (1, 'K'),
        comment = '768',
    ),
    longDesc = 
u"""
768
""",
)

entry(
    index = 739,
    label = "A2C2H + A1- <=> C18H12 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '769',
    ),
    longDesc = 
u"""
769
""",
)

entry(
    index = 740,
    label = "A2C2H* + A1 <=> C18H12 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '770',
    ),
    longDesc = 
u"""
770
""",
)

entry(
    index = 741,
    label = "A2R5- + A1 => BGHIF + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.1e+25, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '771',
    ),
    longDesc = 
u"""
771
""",
)

entry(
    index = 742,
    label = "A3C2H* + C4H4 <=> BAPYR + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+33, 'cm^3/(mol*s)'),
        n = -5.7,
        Ea = (106010, 'J/mol'),
        T0 = (1, 'K'),
        comment = '772',
    ),
    longDesc = 
u"""
772
""",
)

entry(
    index = 743,
    label = "A4- + C4H4 <=> BAPYR + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+33, 'cm^3/(mol*s)'),
        n = -5.7,
        Ea = (106010, 'J/mol'),
        T0 = (1, 'K'),
        comment = '773',
    ),
    longDesc = 
u"""
773
""",
)

entry(
    index = 744,
    label = "A4C2H* + C2H2 <=> BAPYR*S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+37, 'cm^3/(mol*s)'),
        n = -8.02,
        Ea = (68178.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '774',
    ),
    longDesc = 
u"""
774
""",
)

entry(
    index = 745,
    label = "BAPYR*S + H <=> BAPYR",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '775',
    ),
    longDesc = 
u"""
775
""",
)

entry(
    index = 746,
    label = "P2 + A1C2H- => BAPYR + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.1e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '776',
    ),
    longDesc = 
u"""
776
""",
)

entry(
    index = 747,
    label = "P2- + A1C2H3* => BAPYR + H2 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.3e+38, 'cm^3/(mol*s)'),
        n = -6.3,
        Ea = (187325, 'J/mol'),
        T0 = (1, 'K'),
        comment = '777',
    ),
    longDesc = 
u"""
777
""",
)

entry(
    index = 748,
    label = "P2- + n-C8H7 => BAPYR + H2 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.3e+38, 'cm^3/(mol*s)'),
        n = -6.3,
        Ea = (187325, 'J/mol'),
        T0 = (1, 'K'),
        comment = '778',
    ),
    longDesc = 
u"""
778
""",
)

entry(
    index = 749,
    label = "A2R5- + A1C2H- <=> BAPYR",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.3e+38, 'cm^3/(mol*s)'),
        n = -6.3,
        Ea = (187325, 'J/mol'),
        T0 = (1, 'K'),
        comment = '779',
    ),
    longDesc = 
u"""
779
""",
)

entry(
    index = 750,
    label = "A2R5 + A1C2H- <=> BAPYR + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+25, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '780',
    ),
    longDesc = 
u"""
780
""",
)

entry(
    index = 751,
    label = "A2R5- + A1C2H <=> BAPYR + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+25, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (66598.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '781',
    ),
    longDesc = 
u"""
781
""",
)

entry(
    index = 752,
    label = "C18H11 + O2 => HCO + CO + A4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30763.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '782',
    ),
    longDesc = 
u"""
782
""",
)

entry(
    index = 753,
    label = "C18H11 + H <=> BGHIF + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '783',
    ),
    longDesc = 
u"""
783
""",
)

entry(
    index = 754,
    label = "C18H11 + C2H => BAPYR",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.24e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (2910.07, 'J/mol'),
        T0 = (1, 'K'),
        comment = '784',
    ),
    longDesc = 
u"""
784
""",
)

entry(
    index = 755,
    label = "C18H11 + C2H2 <=> BAPYR + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+24, 'cm^3/(mol*s)'),
        n = -3.36,
        Ea = (73998.8, 'J/mol'),
        T0 = (1, 'K'),
        comment = '785',
    ),
    longDesc = 
u"""
785
""",
)

entry(
    index = 756,
    label = "C18H12 + O <=> C18H11 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (61527.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '786',
    ),
    longDesc = 
u"""
786
""",
)

entry(
    index = 757,
    label = "C18H12 + H <=> C18H11 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (303, 'cm^3/(mol*s)'),
        n = 3.3,
        Ea = (23862.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '787',
    ),
    longDesc = 
u"""
787
""",
)

entry(
    index = 758,
    label = "C18H12 + OH <=> C18H11 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (6092.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '788',
    ),
    longDesc = 
u"""
788
""",
)

entry(
    index = 759,
    label = "BGHIF + O <=> HCCO + A4-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (61527.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '789',
    ),
    longDesc = 
u"""
789
""",
)

entry(
    index = 760,
    label = "BGHIF + OH <=> CH2CO + A4-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (44066.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '790',
    ),
    longDesc = 
u"""
790
""",
)

entry(
    index = 761,
    label = "BAPYR*S + O2 => HCO + CO + BGHIF",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30763.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '791',
    ),
    longDesc = 
u"""
791
""",
)

entry(
    index = 762,
    label = "C4H2 + A4 => BAPYR",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (600, 'cm^3/(mol*s)'),
        n = 2.2313,
        Ea = (-4732.35, 'J/mol'),
        T0 = (1, 'K'),
        comment = '792',
    ),
    longDesc = 
u"""
792
""",
)

entry(
    index = 763,
    label = "BAPYR + O <=> HCCO + C18H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (174604, 'J/mol'),
        T0 = (1, 'K'),
        comment = '793',
    ),
    longDesc = 
u"""
793
""",
)

entry(
    index = 764,
    label = "BAPYR + OH => CH2CO + C18H11",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (44066.7, 'J/mol'),
        T0 = (1, 'K'),
        comment = '794',
    ),
    longDesc = 
u"""
794
""",
)

entry(
    index = 765,
    label = "C4H + C2H2 <=> C6H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+13, 'cm^3/(mol*s)'),
        n = 0.28,
        Ea = (-307.635, 'J/mol'),
        T0 = (1, 'K'),
        comment = '795',
    ),
    longDesc = 
u"""
795
""",
)

entry(
    index = 766,
    label = "C3H2 + C3H2 => C6H2 + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (353365, 'J/mol'),
        T0 = (1, 'K'),
        comment = '796',
    ),
    longDesc = 
u"""
796
""",
)

entry(
    index = 767,
    label = "C6H + C2H2 <=> C8H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+13, 'cm^3/(mol*s)'),
        n = 0.28,
        Ea = (-307.635, 'J/mol'),
        T0 = (1, 'K'),
        comment = '797',
    ),
    longDesc = 
u"""
797
""",
)

entry(
    index = 768,
    label = "C2H + C6H2 <=> C8H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+13, 'cm^3/(mol*s)'),
        n = 0.28,
        Ea = (-307.635, 'J/mol'),
        T0 = (1, 'K'),
        comment = '798',
    ),
    longDesc = 
u"""
798
""",
)

entry(
    index = 769,
    label = "C4H2 + C2H <=> C4H + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '799',
    ),
    longDesc = 
u"""
799
""",
)

entry(
    index = 770,
    label = "C4H2 + C2H <=> H + C6H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+13, 'cm^3/(mol*s)'),
        n = 0.28,
        Ea = (-307.635, 'J/mol'),
        T0 = (1, 'K'),
        comment = '800',
    ),
    longDesc = 
u"""
800
""",
)

entry(
    index = 771,
    label = "C4H2 + C4H2 => C8H2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.51e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (232805, 'J/mol'),
        T0 = (1, 'K'),
        comment = '801',
    ),
    longDesc = 
u"""
801
""",
)

entry(
    index = 772,
    label = "C4H2 + C4H2 <=> C8H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (174604, 'J/mol'),
        T0 = (1, 'K'),
        comment = '802',
    ),
    longDesc = 
u"""
802
""",
)

entry(
    index = 773,
    label = "C6H2 <=> C6H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.14e+17, 'cm^3/(mol*s)'), n=0, Ea=(565384, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.35},
        comment = '803',
    ),
    longDesc = 
u"""
803
""",
)

entry(
    index = 774,
    label = "C6H2 + H <=> C6H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.7e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (166289, 'J/mol'),
        T0 = (1, 'K'),
        comment = '804',
    ),
    longDesc = 
u"""
804
""",
)

entry(
    index = 775,
    label = "C6H2 + OH <=> C6H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62357.5, 'J/mol'),
        T0 = (1, 'K'),
        comment = '805',
    ),
    longDesc = 
u"""
805
""",
)

entry(
    index = 776,
    label = "C6H2 + C2H <=> C4H + C4H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '806',
    ),
    longDesc = 
u"""
806
""",
)

entry(
    index = 777,
    label = "C8H2 <=> C8H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.14e+17, 'cm^3/(mol*s)'), n=0, Ea=(565384, 'J/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3, 'O=C=O': 1.5, 'CC': 3, 'O': 6.5, '[O][O]': 0.4, '[C-]#[O+]': 0.75, '[Ar]': 0.35},
        comment = '807',
    ),
    longDesc = 
u"""
807
""",
)

entry(
    index = 778,
    label = "C8H2 + H <=> C8H + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.7e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (108088, 'J/mol'),
        T0 = (1, 'K'),
        comment = '808',
    ),
    longDesc = 
u"""
808
""",
)

entry(
    index = 779,
    label = "C8H2 + OH <=> C8H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (54043.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '809',
    ),
    longDesc = 
u"""
809
""",
)

entry(
    index = 780,
    label = "C5H5 + C5H5 <=> A2 + H + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3e+16, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (196429, 'J/mol'),
                T0 = (1, 'K'),
                comment = '810',
            ),
            Arrhenius(
                A = (453000, 'cm^3/(mol*s)'),
                n = 1.83,
                Ea = (150001, 'J/mol'),
                T0 = (1, 'K'),
                comment = '811',
            ),
        ],
    ),
)

entry(
    index = 781,
    label = "C5H5 + H2CCCH <=> A1C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (34704.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '812',
    ),
    longDesc = 
u"""
812
""",
)

entry(
    index = 782,
    label = "C5H5 + H2CCCCH <=> INDENE",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (34704.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '813',
    ),
    longDesc = 
u"""
813
""",
)

entry(
    index = 783,
    label = "C5H5 + C5H5 <=> INDENYL + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40000.9, 'J/mol'),
        T0 = (1, 'K'),
        comment = '814',
    ),
    longDesc = 
u"""
814
""",
)

entry(
    index = 784,
    label = "C5H6 + CH3 <=> C5H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1, 'cm^3/(mol*s)'),
        n = 4,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        comment = '815',
    ),
    longDesc = 
u"""
815
""",
)

entry(
    index = 785,
    label = "C5H5 + C5H6 <=> INDENE + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.63e+13, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (249201, 'J/mol'),
        T0 = (1, 'K'),
        comment = '816',
    ),
    longDesc = 
u"""
816
""",
)

entry(
    index = 786,
    label = "n-C8H7 + A1C2H- => A4 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3e+17, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196429, 'J/mol'),
        T0 = (1, 'K'),
        comment = '817',
    ),
    longDesc = 
u"""
817
""",
)

entry(
    index = 787,
    label = "INDENYL + C5H5 => A3 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3e+17, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196429, 'J/mol'),
        T0 = (1, 'K'),
        comment = '818',
    ),
    longDesc = 
u"""
818
""",
)

entry(
    index = 788,
    label = "INDENYL + INDENYL => C18H12 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6e+17, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196429, 'J/mol'),
        T0 = (1, 'K'),
        comment = '819',
    ),
    longDesc = 
u"""
819
""",
)

entry(
    index = 789,
    label = "A1C2H3* + A1C2H- <=> A4 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+17, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196429, 'J/mol'),
        T0 = (1, 'K'),
        comment = '820',
    ),
    longDesc = 
u"""
820
""",
)

entry(
    index = 790,
    label = "A2C2H* + n-C8H7 <=> BAPYR + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+17, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196429, 'J/mol'),
        T0 = (1, 'K'),
        comment = '821',
    ),
    longDesc = 
u"""
821
""",
)

entry(
    index = 791,
    label = "A2C2H* + A1C2H3* <=> BAPYR + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+17, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196429, 'J/mol'),
        T0 = (1, 'K'),
        comment = '822',
    ),
    longDesc = 
u"""
822
""",
)

entry(
    index = 792,
    label = "A2R5- + A1- => BGHIF + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6e+17, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196429, 'J/mol'),
        T0 = (1, 'K'),
        comment = '823',
    ),
    longDesc = 
u"""
823
""",
)

entry(
    index = 793,
    label = "P2- + A1C2H- => BAPYR + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6e+17, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196429, 'J/mol'),
        T0 = (1, 'K'),
        comment = '824',
    ),
    longDesc = 
u"""
824
""",
)

entry(
    index = 794,
    label = "A1C2H3 + CH3 <=> A1C2H3* + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62608, 'J/mol'),
        T0 = (1, 'K'),
        comment = '825',
    ),
    longDesc = 
u"""
825
""",
)

entry(
    index = 795,
    label = "A2R5 + CH3 <=> A2R5- + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62608, 'J/mol'),
        T0 = (1, 'K'),
        comment = '826',
    ),
    longDesc = 
u"""
826
""",
)

entry(
    index = 796,
    label = "P2 + CH3 <=> P2- + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62608, 'J/mol'),
        T0 = (1, 'K'),
        comment = '827',
    ),
    longDesc = 
u"""
827
""",
)

entry(
    index = 797,
    label = "A1 + O <=> C5H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+16, 'cm^3/(mol*s)'),
        n = -0.77,
        Ea = (63564.1, 'J/mol'),
        T0 = (1, 'K'),
        comment = '828',
    ),
    longDesc = 
u"""
828
""",
)

entry(
    index = 798,
    label = "A2R5 + OH => A2 + HCCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (176, 'cm^3/(mol*s)'),
        n = 3.25,
        Ea = (23240.6, 'J/mol'),
        T0 = (1, 'K'),
        comment = '829',
    ),
    longDesc = 
u"""
829
""",
)

entry(
    index = 799,
    label = "A1C2H3* + CH3 <=> INDENE + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+18, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (303478, 'J/mol'),
        T0 = (1, 'K'),
        comment = '830',
    ),
    longDesc = 
u"""
830
""",
)

entry(
    index = 800,
    label = "C7H7 + CH3 <=> A1C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+26, 'cm^3/(mol*s)'),
        n = -4,
        Ea = (22033.4, 'J/mol'),
        T0 = (1, 'K'),
        comment = '831',
    ),
    longDesc = 
u"""
831
""",
)

