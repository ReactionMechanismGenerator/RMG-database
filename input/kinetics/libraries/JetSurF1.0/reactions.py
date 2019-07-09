#!/usr/bin/env python
# encoding: utf-8

name = "JetSurF1.0"
shortDesc = u"JetSurF1.0"
longDesc = u"""
JetSurF - A Jet Surrogate Fuel Model
JetSurF is a detailed chemical reaction model for the combustion of jet-fuel surrogate.

B. Sirjean, E. Dames, D. A. Sheen, X.-Q. You, C. Sung, A. T. Holley, F. N. Egolfopoulos,
H. Wang, S. S. Vasu, D. F. Davidson, R. K. Hanson, H. Pitsch, C. T. Bowman, A. Kelley,
C. K. Law, W. Tsang, N. P. Cernansky, D. L. Miller, A. Violi, R. P. Lindstedt,
A high-temperature chemical kinetic model of n-alkane oxidation, JetSurF version 1.0
September 15, 2009 (http://web.stanford.edu/group/haiwanglab/JetSurF/JetSurF1.0/index.html).
 
 
The following reactions involve excited CH and OH species, which currently cannot be represented in RMG.
In order to compare RMG's predictions with experimental results of excited CH or OH,
it is advised to append the following reactions to the final Chemkin file.
Note that the model generation in RMG could have been somewhat different if these reactions were to integrated as a library.
See https://github.com/ReactionMechanismGenerator/RMG-database/issues/174 for more info.

CH* => CH                     1.90E+06 0.0 0.0
!DUPLICATE
CH* + M => CH + M             4.00E+10 0.5 0.0
!DUPLICATE
CH* + O2 => CH + O2           2.40E+12 0.5 0.0
C2H + O2 => CH* + CO2         4.50E+15 0.0 25000
H+O+M = OH* +M                3.10E+14   0.0 10000.
OH*+Ar = OH+Ar                2.17E+10  0.5   2060.
OH* +H2O = OH+H2O             5.92E+12  0.5   -861.
OH* +CO2 = OH+CO2             2.75E+12  0.5   -968.
OH* +CO = OH+CO               3.23E+12  0.5   -787.
OH* +H2 = OH+H2               2.95E+12  0.5   -444.
OH* +O2 = OH+O2               2.10E+12  0.5   -482.
OH* +OH = OH+OH               1.50E+12  0.5      0.
OH* +H = OH+H                 1.50E+12  0.5      0.
OH* +O = OH+O                 1.50E+12  0.5      0.
OH* +CH4 = OH+CH4             3.36E+12  0.5   -635.
OH* = OH                      1.40E+6   0.0      0.
"""

entry(
    index = 1,
    label = "H + O2 <=> O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.644e+16, 'cm^3/(mol*s)'),
        n = -0.6707,
        Ea = (17041, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "O + H2 <=> H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (45890, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (6260, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0 * 1.00',
    ),
    longDesc = 
u"""
GRI3.0 * 1.00
""",
)

entry(
    index = 3,
    label = "OH + H2 <=> H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.734e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0 * 1.19',
    ),
    longDesc = 
u"""
GRI3.0 * 1.19
""",
)

entry(
    index = 4,
    label = "OH + OH <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (39730, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (-2110, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0 * 0.80',
    ),
    longDesc = 
u"""
GRI3.0 * 0.80
""",
)

entry(
    index = 5,
    label = "H + H <=> H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.78e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0, 'O=C=O': 0, 'O': 0, '[Ar]': 0.63},
        comment = 'GRI3.0 * 1.11',
    ),
    longDesc = 
u"""
GRI3.0 * 1.11
""",
)

entry(
    index = 6,
    label = "H + H + H2 <=> H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+16, 'cm^6/(mol^2*s)'),
        n = -0.6,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0 * 1.78\nHE/0.63/',
    ),
    longDesc = 
u"""
GRI3.0 * 1.78
He/0.63/
""",
)

entry(
    index = 7,
    label = "H + H + H2O <=> H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.624e+19, 'cm^6/(mol^2*s)'),
        n = -1.25,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0',
    ),
    longDesc = 
u"""
GRI3.0
""",
)

entry(
    index = 8,
    label = "H + H + CO2 <=> H2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.5e+20, 'cm^6/(mol^2*s)'),
        n = -2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0 * 0.94',
    ),
    longDesc = 
u"""
GRI3.0 * 0.94
""",
)

entry(
    index = 9,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.4e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[C-]#[O+]': 1.75, '[H][H]': 2, 'O=C=O': 3.6, 'O': 6.3, '[Ar]': 0.38},
        comment = 'GRI3.0',
    ),
    longDesc = 
u"""
GRI3.0
""",
)

entry(
    index = 10,
    label = "O + H <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(9.428e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[C-]#[O+]': 1.75, '[H][H]': 2, 'O=C=O': 3.6, 'O': 12, '[Ar]': 0.7},
        comment = 'GRI3.0 * 2.00\nHE/0.38/',
    ),
    longDesc = 
u"""
GRI3.0 * 2.00
He/0.38/
""",
)

entry(
    index = 11,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.2e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[C-]#[O+]': 1.75, '[H][H]': 2.4, 'O=C=O': 3.6, 'O': 15.4, '[Ar]': 0.83},
        comment = '86TSA/HAM * 2.00\nHE/0.7/',
    ),
    longDesc = 
u"""
86TSA/HAM * 2.00
He/0.7/
""",
)

entry(
    index = 12,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.116e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.328e+19, 'cm^6/(mol^2*s)'),
            n = -1.4,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[C-]#[O+]': 1.09, '[O][O]': 0.85, 'O=C=O': 2.18, 'O': 11.89, '[Ar]': 0.4},
        comment = 'GRI3.0\nHE/0.83/',
    ),
    longDesc = 
u"""
GRI3.0
He/0.83/
""",
)

entry(
    index = 13,
    label = "H2 + O2 <=> HO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (591600, 'cm^3/(mol*s)'),
        n = 2.433,
        Ea = (53502, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '00 TROE - Based on M=N2 * 1.10\nHE/0.46/',
    ),
    longDesc = 
u"""
00 TROE - Based on M=N2 * 1.10
He/0.46/
""",
)

entry(
    index = 14,
    label = "OH + OH <=> H2O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.11e+14, 'cm^3/(mol*s)'), n=-0.37, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.01e+17, 'cm^6/(mol^2*s)'),
            n = -0.584,
            Ea = (-2293, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7346,
        T3 = (94, 'K'),
        T1 = (1756, 'K'),
        T2 = (5182, 'K'),
        efficiencies = {'[C-]#[O+]': 1.75, '[H][H]': 2, 'O=C=O': 3.6, 'O': 6, '[Ar]': 0.7},
        comment = '00MIC/SUT * 0.80',
    ),
    longDesc = 
u"""
00MIC/SUT * 0.80
""",
)

entry(
    index = 15,
    label = "HO2 + H <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (671, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88ZEL/EWI * 1.50\nFit 88ZEL/EWI and 92BAU/COB\nH2O=6xN2 88ZEL/EWI\nHE/0.7/\nReactions of HO2',
    ),
    longDesc = 
u"""
88ZEL/EWI * 1.50
Fit 88ZEL/EWI and 92BAU/COB
H2O=6xN2 88ZEL/EWI
He/0.7/
Reactions of HO2
""",
)

entry(
    index = 16,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.485e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (295, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0',
    ),
    longDesc = 
u"""
GRI3.0
""",
)

entry(
    index = 17,
    label = "HO2 + O <=> OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99MUE/KIM * 1.06',
    ),
    longDesc = 
u"""
99MUE/KIM * 1.06
""",
)

entry(
    index = 18,
    label = "HO2 + HO2 <=> O2 + H2O2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.3e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1630, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'GRI3.0 * 2.00',
            ),
            Arrhenius(
                A = (3.658e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (12000, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '90HIP/TRO',
            ),
        ],
    ),
)

entry(
    index = 19,
    label = "OH + HO2 <=> H2O + O2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.41e+18, 'cm^3/(mol*s)'),
                n = -1.76,
                Ea = (60, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '90HIP/TRO * 0.87',
            ),
            Arrhenius(
                A = (1.12e+85, 'cm^3/(mol*s)'),
                n = -22.3,
                Ea = (26900, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'Wang07',
            ),
            Arrhenius(
                A = (5.37e+70, 'cm^3/(mol*s)'),
                n = -16.72,
                Ea = (32900, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'Wang07',
            ),
            Arrhenius(
                A = (2.51e+12, 'cm^3/(mol*s)'),
                n = 2,
                Ea = (40000, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'Wang07',
            ),
            Arrhenius(
                A = (1e+136, 'cm^3/(mol*s)'),
                n = -40,
                Ea = (34800, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'Wang07',
            ),
        ],
    ),
)

entry(
    index = 20,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.05e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (5200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Wang07\nReactions of H2O2',
    ),
    longDesc = 
u"""
Wang07
Reactions of H2O2
""",
)

entry(
    index = 21,
    label = "H2O2 + H <=> OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0 * 0.50',
    ),
    longDesc = 
u"""
GRI3.0 * 0.50
""",
)

entry(
    index = 22,
    label = "H2O2 + O <=> OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.63e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 23,
    label = "H2O2 + OH <=> HO2 + H2O",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2e+12, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (427, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '86TSA/HAM',
            ),
            Arrhenius(
                A = (2.67e+41, 'cm^3/(mol*s)'),
                n = -7,
                Ea = (37600, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '95HIP/NEU',
            ),
        ],
    ),
)

entry(
    index = 24,
    label = "CO + O <=> CO2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.362e+10, 'cm^3/(mol*s)'), n=0, Ea=(2384, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.173e+24, 'cm^6/(mol^2*s)'),
            n = -2.79,
            Ea = (4191, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[C-]#[O+]': 1.75, '[H][H]': 2, 'O=C=O': 3.6, 'O': 12, '[Ar]': 0.7},
        comment = 'Refit95HIP/NEU\n2.2E14 MAX K\nReactions of CO/CO2',
    ),
    longDesc = 
u"""
Refit95HIP/NEU
2.2E14 MAX K
Reactions of CO/CO2
""",
)

entry(
    index = 25,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (70460, 'cm^3/(mol*s)'),
                n = 2.053,
                Ea = (-355.67, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '99MUE/KIM * 0.76\nHE/0.7/',
            ),
            Arrhenius(
                A = (5.757e+12, 'cm^3/(mol*s)'),
                n = -0.664,
                Ea = (331.83, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '06JOS/WANG',
            ),
        ],
    ),
)

entry(
    index = 26,
    label = "CO + O2 <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.119e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '06JOS/WANG',
    ),
    longDesc = 
u"""
06JOS/WANG
""",
)

entry(
    index = 27,
    label = "CO + HO2 <=> CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17942.6, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM * 0.44',
    ),
    longDesc = 
u"""
86TSA/HAM * 0.44
""",
)

entry(
    index = 28,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '07YOU/WANG\nReactions of HCO',
    ),
    longDesc = 
u"""
07YOU/WANG
Reactions of HCO
""",
)

entry(
    index = 29,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '02FRI/DAV * 1.00',
    ),
    longDesc = 
u"""
02FRI/DAV * 1.00
""",
)

entry(
    index = 30,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0',
    ),
    longDesc = 
u"""
GRI3.0
""",
)

entry(
    index = 31,
    label = "HCO + OH <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0',
    ),
    longDesc = 
u"""
GRI3.0
""",
)

entry(
    index = 32,
    label = "HCO <=> CO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.87e+17, 'cm^3/(mol*s)'),
            n = -1,
            Ea = (17000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[C-]#[O+]': 1.75, '[H][H]': 2, 'O=C=O': 3.6, 'O': 0},
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 33,
    label = "HCO + H2O <=> CO + H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.244e+18, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (17000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '02FRI/DAV * 2.00',
    ),
    longDesc = 
u"""
02FRI/DAV * 2.00
""",
)

entry(
    index = 34,
    label = "HCO + O2 <=> CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.204e+10, 'cm^3/(mol*s)'),
        n = 0.807,
        Ea = (-727, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '12xM * 2.00',
    ),
    longDesc = 
u"""
12xM * 2.00
""",
)

entry(
    index = 35,
    label = "CO + H2 <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.3e+07, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (79600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.07e+27, 'cm^6/(mol^2*s)'),
            n = -3.42,
            Ea = (84350, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '96HSU/MEB\n---- End of Optimized H2/O2 mechanism ----\nReactions of CO/CO2 (See the H2/CO model above for additional reactions)',
    ),
    longDesc = 
u"""
96HSU/MEB
---- End of Optimized H2/O2 mechanism ----
Reactions of CO/CO2 (See the H2/CO model above for additional reactions)
""",
)

entry(
    index = 36,
    label = "C + OH <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI\nReactions of C',
    ),
    longDesc = 
u"""
GRI
Reactions of C
""",
)

entry(
    index = 37,
    label = "C + O2 <=> CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (576, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 38,
    label = "CH + H <=> C + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI\nReactions of CH',
    ),
    longDesc = 
u"""
GRI
Reactions of CH
""",
)

entry(
    index = 39,
    label = "CH + O <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 40,
    label = "CH + OH <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 41,
    label = "CH + H2 <=> CH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.107e+08, 'cm^3/(mol*s)'),
        n = 1.79,
        Ea = (1670, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 42,
    label = "CH + H2O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.71e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-755, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 43,
    label = "CH + O2 <=> HCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 44,
    label = "CH + CO <=> HCCO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+28, 'cm^6/(mol^2*s)'),
            n = -3.74,
            Ea = (1936, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5757,
        T3 = (237, 'K'),
        T1 = (1652, 'K'),
        T2 = (5069, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 45,
    label = "CH + CO2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (690, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 46,
    label = "HCO + H <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.09e+12, 'cm^3/(mol*s)'),
            n = 0.48,
            Ea = (-260, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.35e+24, 'cm^6/(mol^2*s)'),
            n = -2.57,
            Ea = (1425, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7824,
        T3 = (271, 'K'),
        T1 = (2755, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'GRI\nReactions of HCO (See the H2/CO model above for additional reactions)',
    ),
    longDesc = 
u"""
GRI
Reactions of HCO (See the H2/CO model above for additional reactions)
""",
)

entry(
    index = 47,
    label = "CH2 + H <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.2e+27, 'cm^6/(mol^2*s)'),
            n = -3.14,
            Ea = (1230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.68,
        T3 = (78, 'K'),
        T1 = (1995, 'K'),
        T2 = (5590, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'GRI\nReactions of CH2(triplet)',
    ),
    longDesc = 
u"""
GRI
Reactions of CH2(triplet)
""",
)

entry(
    index = 48,
    label = "CH2 + O <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 49,
    label = "CH2 + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 50,
    label = "CH2 + OH <=> CH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 51,
    label = "CH2 + H2 <=> H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (500000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (7230, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 52,
    label = "CH2 + O2 <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 53,
    label = "CH2 + O2 <=> CO2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.64e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI##',
    ),
    longDesc = 
u"""
GRI##
""",
)

entry(
    index = 54,
    label = "CH2 + HO2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI##',
    ),
    longDesc = 
u"""
GRI##
""",
)

entry(
    index = 55,
    label = "CH2 + C <=> C2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 56,
    label = "CH2 + CO <=> CH2CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.1e+11, 'cm^3/(mol*s)'), n=0.5, Ea=(4510, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7095, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5907,
        T3 = (275, 'K'),
        T1 = (1226, 'K'),
        T2 = (5185, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 57,
    label = "CH2 + CH <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 58,
    label = "CH2 + CH2 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 59,
    label = "CH2(S) + N2 <=> CH2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI\nReactions of CH2(singlet)',
    ),
    longDesc = 
u"""
GRI
Reactions of CH2(singlet)
""",
)

entry(
    index = 60,
    label = "CH2(S) + Ar <=> CH2 + Ar",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 61,
    label = "CH2(S) + H <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 62,
    label = "CH2(S) + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 63,
    label = "CH2(S) + O <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 64,
    label = "CH2(S) + OH <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 65,
    label = "CH2(S) + H2 <=> CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 66,
    label = "CH2(S) + O2 <=> H + OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 67,
    label = "CH2(S) + O2 <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 68,
    label = "CH2(S) + H2O <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.7e+38, 'cm^6/(mol^2*s)'),
            n = -6.3,
            Ea = (3100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1507,
        T3 = (134, 'K'),
        T1 = (2383, 'K'),
        T2 = (7265, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 69,
    label = "CH2(S) + H2O <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 70,
    label = "CH2(S) + CO <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 71,
    label = "CH2(S) + CO2 <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 72,
    label = "CH2(S) + CO2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 73,
    label = "CH2O + H <=> CH2OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (3600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.27e+32, 'cm^6/(mol^2*s)'),
            n = -4.82,
            Ea = (6530, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7187,
        T3 = (103, 'K'),
        T1 = (1291, 'K'),
        T2 = (4160, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = 'GRI\nReactions of CH2O',
    ),
    longDesc = 
u"""
GRI
Reactions of CH2O
""",
)

entry(
    index = 74,
    label = "CH2O + H <=> CH3O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (2600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (5560, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.758,
        T3 = (94, 'K'),
        T1 = (1555, 'K'),
        T2 = (4200, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 75,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+10, 'cm^3/(mol*s)'),
        n = 1.05,
        Ea = (3275, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 76,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3540, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 77,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-447, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 78,
    label = "CH2O + O2 <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 79,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 80,
    label = "CH2O + CH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.46e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-515, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 81,
    label = "CH3 + H <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.27e+16, 'cm^3/(mol*s)'),
            n = -0.63,
            Ea = (383, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.477e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (2440, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'GRI\nReactions of CH3',
    ),
    longDesc = 
u"""
GRI
Reactions of CH3
""",
)

entry(
    index = 82,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 83,
    label = "CH3 + OH <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.7e+38, 'cm^6/(mol^2*s)'),
            n = -6.3,
            Ea = (3100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.2105,
        T3 = (83.5, 'K'),
        T1 = (5398, 'K'),
        T2 = (8370, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 84,
    label = "CH3 + OH <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5420, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 85,
    label = "CH3 + OH <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.501e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 86,
    label = "CH3 + O2 <=> O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.083e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 87,
    label = "CH3 + O2 <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 88,
    label = "CH3 + HO2 <=> CH4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 89,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.34e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 90,
    label = "CH3 + H2O2 <=> CH4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24500, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (5180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 91,
    label = "CH3 + C <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 92,
    label = "CH3 + CH <=> C2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 93,
    label = "CH3 + HCO <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.48e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 94,
    label = "CH3 + CH2O <=> CH4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3320, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 95,
    label = "CH3 + CH2 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 96,
    label = "CH3 + CH2(S) <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-570, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 97,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.12e+16, 'cm^3/(mol*s)'),
            n = -0.97,
            Ea = (620, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.77e+50, 'cm^6/(mol^2*s)'),
            n = -9.67,
            Ea = (6220, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5325,
        T3 = (151, 'K'),
        T1 = (1038, 'K'),
        T2 = (4970, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 98,
    label = "CH3 + CH3 <=> H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.99e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 99,
    label = "CH3 + HCCO <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 100,
    label = "CH3 + C2H <=> C3H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 101,
    label = "CH3O + H <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.6e+28, 'cm^6/(mol^2*s)'),
            n = -4,
            Ea = (3025, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8902,
        T3 = (144, 'K'),
        T1 = (2838, 'K'),
        T2 = (45569, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = '86TSA/HAM\nReactions of CH3O',
    ),
    longDesc = 
u"""
86TSA/HAM
Reactions of CH3O
""",
)

entry(
    index = 102,
    label = "CH3O + H <=> CH2OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+06, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 103,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 104,
    label = "CH3O + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 105,
    label = "CH3O + H <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 106,
    label = "CH3O + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 107,
    label = "CH3O + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 108,
    label = "CH3O + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3530, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 109,
    label = "CH2OH + H <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e+31, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (3300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7679,
        T3 = (338, 'K'),
        T1 = (1812, 'K'),
        T2 = (5081, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = 'GRI\nReactions of CH2OH',
    ),
    longDesc = 
u"""
GRI
Reactions of CH2OH
""",
)

entry(
    index = 110,
    label = "CH2OH + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 111,
    label = "CH2OH + H <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 112,
    label = "CH2OH + H <=> CH2(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 113,
    label = "CH2OH + O <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 114,
    label = "CH2OH + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 115,
    label = "CH2OH + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 116,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (10840, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI\nReactions of CH4',
    ),
    longDesc = 
u"""
GRI
Reactions of CH4
""",
)

entry(
    index = 117,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 118,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (3120, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 119,
    label = "CH4 + CH <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 120,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.46e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8270, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 121,
    label = "CH4 + CH2(S) <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-570, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 122,
    label = "CH4 + C2H <=> C2H2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 123,
    label = "CH3OH + H <=> CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+07, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4870, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM\nReactions of CH3OH',
    ),
    longDesc = 
u"""
86TSA/HAM
Reactions of CH3OH
""",
)

entry(
    index = 124,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4870, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 125,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (388000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (3100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 126,
    label = "CH3OH + O <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 127,
    label = "CH3OH + OH <=> CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.44e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-840, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 128,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 129,
    label = "CH3OH + CH3 <=> CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 130,
    label = "CH3OH + CH3 <=> CH3O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 131,
    label = "C2H + H <=> C2H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6464,
        T3 = (132, 'K'),
        T1 = (1315, 'K'),
        T2 = (5566, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'GRI\nReactions of C2H',
    ),
    longDesc = 
u"""
GRI
Reactions of C2H
""",
)

entry(
    index = 132,
    label = "C2H + O <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 133,
    label = "C2H + OH <=> H + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 134,
    label = "C2H + O2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 135,
    label = "C2H + H2 <=> H + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (490000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (560, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 136,
    label = "C2O + H <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI\nReactions of C2O',
    ),
    longDesc = 
u"""
GRI
Reactions of C2O
""",
)

entry(
    index = 137,
    label = "C2O + O <=> CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92MIL/MEL',
    ),
    longDesc = 
u"""
92MIL/MEL
""",
)

entry(
    index = 138,
    label = "C2O + OH <=> CO + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92MIL/MEL',
    ),
    longDesc = 
u"""
92MIL/MEL
""",
)

entry(
    index = 139,
    label = "C2O + O2 <=> CO + CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92MIL/MEL',
    ),
    longDesc = 
u"""
92MIL/MEL
""",
)

entry(
    index = 140,
    label = "HCCO + H <=> CH2(S) + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92MIL/MEL\nReactions of HCCO',
    ),
    longDesc = 
u"""
92MIL/MEL
Reactions of HCCO
""",
)

entry(
    index = 141,
    label = "HCCO + O <=> H + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 142,
    label = "HCCO + O2 <=> OH + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (854, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 143,
    label = "HCCO + CH <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 144,
    label = "HCCO + CH2 <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 145,
    label = "HCCO + HCCO <=> C2H2 + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 146,
    label = "HCCO + OH <=> C2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 147,
    label = "C2H2 <=> H2CC",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(8e+14, 's^-1'), n=-0.52, Ea=(50750, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.45e+15, 'cm^3/(mol*s)'),
            n = -0.64,
            Ea = (49700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 2.5, 'C#C': 2.5},
        comment = '92MIL/MEL\nReactions of C2H2',
    ),
    longDesc = 
u"""
92MIL/MEL
Reactions of C2H2
""",
)

entry(
    index = 148,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.86e+08, 's^-1'), n=1.62, Ea=(37048.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.565e+27, 'cm^3/(mol*s)'),
            n = -3.4,
            Ea = (35798.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1.9816,
        T3 = (5383.7, 'K'),
        T1 = (4.2932, 'K'),
        T2 = (-0.0795, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3, '[Ar]': 0.7},
        comment = '99LAS/WAN',
    ),
    longDesc = 
u"""
99LAS/WAN
""",
)

entry(
    index = 149,
    label = "C2H2 + O <=> C2H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19, 'cm^3/(mol*s)'),
        n = -1.41,
        Ea = (28950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96KNY/SLA',
    ),
    longDesc = 
u"""
96KNY/SLA
""",
)

entry(
    index = 150,
    label = "C2H2 + O <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.08e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 151,
    label = "C2H2 + O <=> HCCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.632e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI (0.2 branching ratio)',
    ),
    longDesc = 
u"""
GRI (0.2 branching ratio)
""",
)

entry(
    index = 152,
    label = "C2H2 + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000218, 'cm^3/(mol*s)'),
        n = 4.5,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI (0.8 branching ratio)',
    ),
    longDesc = 
u"""
GRI (0.8 branching ratio)
""",
)

entry(
    index = 153,
    label = "C2H2 + OH <=> HCCOH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (504000, 'cm^3/(mol*s)'),
        n = 2.3,
        Ea = (13500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 154,
    label = "C2H2 + OH <=> C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (14000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 155,
    label = "C2H2 + OH <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000483, 'cm^3/(mol*s)'),
        n = 4,
        Ea = (-2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 156,
    label = "C2H2 + HCO <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (6000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 157,
    label = "C2H2 + CH2 <=> C3H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6620, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 158,
    label = "C2H2 + CH2(S) <=> C3H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88BOH/TEM; 86FRA/BHA',
    ),
    longDesc = 
u"""
88BOH/TEM; 86FRA/BHA
""",
)

entry(
    index = 159,
    label = "C2H2 + C2H <=> C4H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 160,
    label = "C2H2 + C2H <=> nC4H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.3e+10, 'cm^3/(mol*s)'),
            n = 0.899,
            Ea = (-363, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.24e+31, 'cm^6/(mol^2*s)'),
            n = -4.718,
            Ea = (1871, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (100, 'K'),
        T1 = (5613, 'K'),
        T2 = (13387, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 2.5, 'C#C': 2.5},
        comment = '91SHI/MIC, 92KOS/FUK, 93FAR/MOR',
    ),
    longDesc = 
u"""
91SHI/MIC, 92KOS/FUK, 93FAR/MOR
""",
)

entry(
    index = 161,
    label = "C2H2 + C2H <=> iC4H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.3e+10, 'cm^3/(mol*s)'),
            n = 0.899,
            Ea = (-363, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.24e+31, 'cm^6/(mol^2*s)'),
            n = -4.718,
            Ea = (1871, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (100, 'K'),
        T1 = (5613, 'K'),
        T2 = (13387, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 2.5, 'C#C': 2.5},
        comment = '92WAN',
    ),
    longDesc = 
u"""
92WAN
""",
)

entry(
    index = 162,
    label = "C2H2 + HCCO <=> C3H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92WAN',
    ),
    longDesc = 
u"""
92WAN
""",
)

entry(
    index = 163,
    label = "C2H2 + CH3 <=> pC3H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.56e+09, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (13644, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '89MIL/BOW; 83HOM/WEL\nC2H2+CH3 = pC3H4+H                           4.50E+06     1.86    11600.0  !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
89MIL/BOW; 83HOM/WEL
C2H2+CH3 = pC3H4+H                           4.50E+06     1.86    11600.0  !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 164,
    label = "C2H2 + CH3 <=> aC3H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.14e+09, 'cm^3/(mol*s)'),
        n = 0.86,
        Ea = (22153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\nC2H2+CH3 = pC3H4+H                           2.07E+10     0.85    14415.0  !99DAV/LAW RRKM 2 atm\nC2H2+CH3 = pC3H4+H                           2.51E+11     0.56    15453.0  !99DAV/LAW RRKM 5 atm\nC2H2+CH3 = pC3H4+H                           1.10E+12     0.39    16200.0  !99DAV/LAW RRKM 10 atm\nC2H2+CH3 = pC3H4+H                           2.10E+12     0.37    18100.0  !99DAV/LAW RRKM 100 atm\nC2H2+CH3 = aC3H4+H                           2.40E+09     0.91    20700.0  !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
C2H2+CH3 = pC3H4+H                           2.07E+10     0.85    14415.0  !99DAV/LAW RRKM 2 atm
C2H2+CH3 = pC3H4+H                           2.51E+11     0.56    15453.0  !99DAV/LAW RRKM 5 atm
C2H2+CH3 = pC3H4+H                           1.10E+12     0.39    16200.0  !99DAV/LAW RRKM 10 atm
C2H2+CH3 = pC3H4+H                           2.10E+12     0.37    18100.0  !99DAV/LAW RRKM 100 atm
C2H2+CH3 = aC3H4+H                           2.40E+09     0.91    20700.0  !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 165,
    label = "C2H2 + CH3 <=> CH3CCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.99e+22, 'cm^3/(mol*s)'),
        n = -4.39,
        Ea = (18850, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\nC2H2+CH3 = aC3H4+H                           1.33E+10     0.75    22811.0  !99DAV/LAW RRKM 2 atm\nC2H2+CH3 = aC3H4+H                           9.20E+10     0.54    23950.0  !99DAV/LAW RRKM 5 atm\nC2H2+CH3 = aC3H4+H                           5.10E+11     0.35    25000.0  !99DAV/LAW RRKM 10 atm\nC2H2+CH3 = aC3H4+H                           7.30E+12     0.11    28500.0  !99DAV/LAW RRKM 100 atm\nC2H2+CH3 = CH3CCH2                           6.80E+20    -4.16    18000.0  !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
C2H2+CH3 = aC3H4+H                           1.33E+10     0.75    22811.0  !99DAV/LAW RRKM 2 atm
C2H2+CH3 = aC3H4+H                           9.20E+10     0.54    23950.0  !99DAV/LAW RRKM 5 atm
C2H2+CH3 = aC3H4+H                           5.10E+11     0.35    25000.0  !99DAV/LAW RRKM 10 atm
C2H2+CH3 = aC3H4+H                           7.30E+12     0.11    28500.0  !99DAV/LAW RRKM 100 atm
C2H2+CH3 = CH3CCH2                           6.80E+20    -4.16    18000.0  !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 166,
    label = "C2H2 + CH3 <=> CH3CHCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+35, 'cm^3/(mol*s)'),
        n = -7.76,
        Ea = (13300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\nC2H2+CH3 = CH3CCH2                           6.00E+23    -4.60    19571.0  !99DAV/LAW RRKM 2 atm\nC2H2+CH3 = CH3CCH2                           7.31E+25    -5.06    21150.0  !99DAV/LAW RRKM 5 atm\nC2H2+CH3 = CH3CCH2                           9.30E+27    -5.55    22900.0  !99DAV/LAW RRKM 10 atm\nC2H2+CH3 = CH3CCH2                           3.80E+36    -7.58    31300.0  !99DAV/LAW RRKM 100 atm\nC2H2+CH3 = CH3CHCH                           1.40E+32    -7.14    10000.0  !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
C2H2+CH3 = CH3CCH2                           6.00E+23    -4.60    19571.0  !99DAV/LAW RRKM 2 atm
C2H2+CH3 = CH3CCH2                           7.31E+25    -5.06    21150.0  !99DAV/LAW RRKM 5 atm
C2H2+CH3 = CH3CCH2                           9.30E+27    -5.55    22900.0  !99DAV/LAW RRKM 10 atm
C2H2+CH3 = CH3CCH2                           3.80E+36    -7.58    31300.0  !99DAV/LAW RRKM 100 atm
C2H2+CH3 = CH3CHCH                           1.40E+32    -7.14    10000.0  !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 167,
    label = "C2H2 + CH3 <=> aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.68e+53, 'cm^3/(mol*s)'),
        n = -12.82,
        Ea = (35730, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\nC2H2+CH3 = CH3CHCH                           2.40E+38    -8.21    17100.0  !99DAV/LAW RRKM 10 atm\nC2H2+CH3 = CH3CHCH                           1.40E+39    -8.06    20200.0  !99DAV/LAW RRKM 100 atm\nC2H2+CH3 = aC3H5                             8.20E+53    -13.32   33200.0  !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
C2H2+CH3 = CH3CHCH                           2.40E+38    -8.21    17100.0  !99DAV/LAW RRKM 10 atm
C2H2+CH3 = CH3CHCH                           1.40E+39    -8.06    20200.0  !99DAV/LAW RRKM 100 atm
C2H2+CH3 = aC3H5                             8.20E+53    -13.32   33200.0  !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 168,
    label = "H2CC + H <=> C2H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\nC2H2+CH3 = aC3H5                             3.64E+52    -12.46   36127.0  !99DAV/LAW RRKM 2 atm\nC2H2+CH3 = aC3H5                             1.04E+51    -11.89   36476.0  !99DAV/LAW RRKM 5 atm\nC2H2+CH3 = aC3H5                             4.40E+49    -11.40   36700.0  !99DAV/LAW RRKM 10 atm\nC2H2+CH3 = aC3H5                             3.80E+44     -9.63   37600.0  !99DAV/LAW RRKM 100 atm\nReactions of Vinylidene',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
C2H2+CH3 = aC3H5                             3.64E+52    -12.46   36127.0  !99DAV/LAW RRKM 2 atm
C2H2+CH3 = aC3H5                             1.04E+51    -11.89   36476.0  !99DAV/LAW RRKM 5 atm
C2H2+CH3 = aC3H5                             4.40E+49    -11.40   36700.0  !99DAV/LAW RRKM 10 atm
C2H2+CH3 = aC3H5                             3.80E+44     -9.63   37600.0  !99DAV/LAW RRKM 100 atm
Reactions of Vinylidene
""",
)

entry(
    index = 169,
    label = "H2CC + OH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 170,
    label = "H2CC + O2 <=> HCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 171,
    label = "H2CC + C2H2 <=> C4H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (350000, 'cm^3/(mol*s)'),
            n = 2.055,
            Ea = (-2400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+60, 'cm^6/(mol^2*s)'),
            n = -12.599,
            Ea = (7417, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.98,
        T3 = (56, 'K'),
        T1 = (580, 'K'),
        T2 = (4164, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
        comment = '99LAS/WAN',
    ),
    longDesc = 
u"""
99LAS/WAN
""",
)

entry(
    index = 172,
    label = "H2CC + C2H4 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99LAS/WAN',
    ),
    longDesc = 
u"""
99LAS/WAN
""",
)

entry(
    index = 173,
    label = "CH2CO + H <=> CH2CHO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (3.3e+14, 'cm^3/(mol*s)'),
            n = -0.06,
            Ea = (8500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.8e+41, 'cm^6/(mol^2*s)'),
            n = -7.64,
            Ea = (11900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.337,
        T3 = (1707, 'K'),
        T1 = (3200, 'K'),
        T2 = (4131, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3, '[Ar]': 0.7},
        comment = 'Estimated\nReactions of CH2CO/HCCOH',
    ),
    longDesc = 
u"""
Estimated
Reactions of CH2CO/HCCOH
""",
)

entry(
    index = 174,
    label = "CH2CO + H <=> HCCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'calculated RRKM',
    ),
    longDesc = 
u"""
calculated RRKM
""",
)

entry(
    index = 175,
    label = "CH2CO + H <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (2690, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 176,
    label = "CH2CO + O <=> HCCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'calculated RRKM',
    ),
    longDesc = 
u"""
calculated RRKM
""",
)

entry(
    index = 177,
    label = "CH2CO + O <=> CH2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1350, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 178,
    label = "CH2CO + OH <=> HCCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 179,
    label = "HCCOH + H <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 180,
    label = "C2H3 + H <=> C2H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.08e+12, 'cm^3/(mol*s)'),
            n = 0.27,
            Ea = (280, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3320, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (207.5, 'K'),
        T1 = (2663, 'K'),
        T2 = (6095, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3, '[Ar]': 0.7},
        comment = 'GRI\nReactions of C2H3',
    ),
    longDesc = 
u"""
GRI
Reactions of C2H3
""",
)

entry(
    index = 181,
    label = "C2H3 + H <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI1.2',
    ),
    longDesc = 
u"""
GRI1.2
""",
)

entry(
    index = 182,
    label = "C2H3 + H <=> H2CC + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 183,
    label = "C2H3 + O <=> CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 184,
    label = "C2H3 + O <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 185,
    label = "C2H3 + OH <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.011e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 186,
    label = "C2H3 + O2 <=> C2H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.34e+06, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-383.4, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 187,
    label = "C2H3 + O2 <=> CH2CHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (11, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96MEB/DIA',
    ),
    longDesc = 
u"""
96MEB/DIA
""",
)

entry(
    index = 188,
    label = "C2H3 + O2 <=> HCO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1010, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96MEB/DIA',
    ),
    longDesc = 
u"""
96MEB/DIA
""",
)

entry(
    index = 189,
    label = "C2H3 + HO2 <=> CH2CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96MEB/DIA',
    ),
    longDesc = 
u"""
96MEB/DIA
""",
)

entry(
    index = 190,
    label = "C2H3 + H2O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 191,
    label = "C2H3 + HCO <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.033e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 192,
    label = "C2H3 + HCO <=> C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 193,
    label = "C2H3 + CH3 <=> C2H2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.92e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 194,
    label = "C2H3 + CH3 <=> C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.27e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9769.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000, 'K'),
        T2 = (10139.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3, '[Ar]': 0.7},
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 195,
    label = "C2H3 + CH3 <=> aC3H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+24, 'cm^3/(mol*s)'),
        n = -2.83,
        Ea = (18618, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 196,
    label = "C2H3 + C2H2 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+18, 'cm^3/(mol*s)'),
        n = -1.68,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM\nC2H3 + C2H2 = C4H4 + H                       7.20E+13     -0.48    6100.   !   10 Torr RRKM WAN/FRE\nC2H3 + C2H2 = C4H4 + H                       5.00E+14     -0.71    6700.   !   20 Torr RRKM WAN/FRE\nC2H3 + C2H2 = C4H4 + H                       4.60E+16     -1.25    8400.   !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
86TSA/HAM
C2H3 + C2H2 = C4H4 + H                       7.20E+13     -0.48    6100.   !   10 Torr RRKM WAN/FRE
C2H3 + C2H2 = C4H4 + H                       5.00E+14     -0.71    6700.   !   20 Torr RRKM WAN/FRE
C2H3 + C2H2 = C4H4 + H                       4.60E+16     -1.25    8400.   !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 197,
    label = "C2H3 + C2H2 <=> nC4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.3e+38, 'cm^3/(mol*s)'),
        n = -8.76,
        Ea = (12000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nC2H3 + C2H2 = C4H4 + H                       4.90E+16     -1.13   11800.   ! 7600 Torr RRKM WAN/FRE\nC2H3 + C2H2 = nC4H5                          1.10E+31     -7.14    5600.   !   10 Torr RRKM WAN/FRE\nC2H3 + C2H2 = nC4H5                          1.10E+32     -7.33    6200.   !   20 Torr RRKM WAN/FRE\nC2H3 + C2H2 = nC4H5                          2.40E+31     -6.95    5600.   !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
C2H3 + C2H2 = C4H4 + H                       4.90E+16     -1.13   11800.   ! 7600 Torr RRKM WAN/FRE
C2H3 + C2H2 = nC4H5                          1.10E+31     -7.14    5600.   !   10 Torr RRKM WAN/FRE
C2H3 + C2H2 = nC4H5                          1.10E+32     -7.33    6200.   !   20 Torr RRKM WAN/FRE
C2H3 + C2H2 = nC4H5                          2.40E+31     -6.95    5600.   !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 198,
    label = "C2H3 + C2H2 <=> iC4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+46, 'cm^3/(mol*s)'),
        n = -10.98,
        Ea = (18600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nC2H3 + C2H2 = nC4H5                          8.10E+37     -8.09   13400.   ! 7600 Torr RRKM WAN/FRE\nC2H3 + C2H2 = iC4H5                          5.00E+34     -8.42    7900.   !   10 Torr RRKM WAN/FRE\nC2H3 + C2H2 = iC4H5                          2.10E+36     -8.78    9100.   !   20 Torr RRKM WAN/FRE\nC2H3 + C2H2 = iC4H5                          1.00E+37     -8.77    9800.   !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
C2H3 + C2H2 = nC4H5                          8.10E+37     -8.09   13400.   ! 7600 Torr RRKM WAN/FRE
C2H3 + C2H2 = iC4H5                          5.00E+34     -8.42    7900.   !   10 Torr RRKM WAN/FRE
C2H3 + C2H2 = iC4H5                          2.10E+36     -8.78    9100.   !   20 Torr RRKM WAN/FRE
C2H3 + C2H2 = iC4H5                          1.00E+37     -8.77    9800.   !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 199,
    label = "C2H3 + C2H3 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+42, 'cm^3/(mol*s)'),
        n = -8.84,
        Ea = (12483, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nC2H3 + C2H2 = iC4H5                          5.10E+53    -12.64   28800.   ! 7600 Torr RRKM WAN/FRE\nC2H3 + C2H3 = C4H6                           7.00E+57    -13.82   17629.   ! RRKM 20 Torr  WAN/FRE\nC2H3 + C2H3 = C4H6                           1.50E+52    -11.97   16056.   ! RRKM 90 Torr  WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
C2H3 + C2H2 = iC4H5                          5.10E+53    -12.64   28800.   ! 7600 Torr RRKM WAN/FRE
C2H3 + C2H3 = C4H6                           7.00E+57    -13.82   17629.   ! RRKM 20 Torr  WAN/FRE
C2H3 + C2H3 = C4H6                           1.50E+52    -11.97   16056.   ! RRKM 90 Torr  WAN/FRE
""",
)

entry(
    index = 200,
    label = "C2H3 + C2H3 <=> iC4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+22, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (13654, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM 760 Torr WAN/FRE\nC2H3 + C2H3 = iC4H5 + H                      1.50E+30     -4.95   12958.   ! RRKM 20 Torr  WAN/FRE\nC2H3 + C2H3 = iC4H5 + H                      7.20E+28     -4.49   14273.   ! RRKM 90 Torr  WAN/FRE',
    ),
    longDesc = 
u"""
RRKM 760 Torr WAN/FRE
C2H3 + C2H3 = iC4H5 + H                      1.50E+30     -4.95   12958.   ! RRKM 20 Torr  WAN/FRE
C2H3 + C2H3 = iC4H5 + H                      7.20E+28     -4.49   14273.   ! RRKM 90 Torr  WAN/FRE
""",
)

entry(
    index = 201,
    label = "C2H3 + C2H3 <=> nC4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+20, 'cm^3/(mol*s)'),
        n = -2.04,
        Ea = (15361, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM 760 Torr WAN/FRE\nC2H3 + C2H3 = nC4H5 + H                      1.10E+24     -3.28   12395.   ! RRKM 20 Torr  WAN/FRE\nC2H3 + C2H3 = nC4H5 + H                      4.60E+24     -3.38   14650.   ! RRKM 90 Torr  WAN/FRE',
    ),
    longDesc = 
u"""
RRKM 760 Torr WAN/FRE
C2H3 + C2H3 = nC4H5 + H                      1.10E+24     -3.28   12395.   ! RRKM 20 Torr  WAN/FRE
C2H3 + C2H3 = nC4H5 + H                      4.60E+24     -3.38   14650.   ! RRKM 90 Torr  WAN/FRE
""",
)

entry(
    index = 202,
    label = "C2H3 + C2H3 <=> C2H2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM 760 Torr WAN/FRE',
    ),
    longDesc = 
u"""
RRKM 760 Torr WAN/FRE
""",
)

entry(
    index = 203,
    label = "CH2CHO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+41, 's^-1'),
        n = -9.147,
        Ea = (46900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'NIST DB\nReactions of CH2CHO\nCH2CHO = CH3+CO                              2.340E+43  -10.099   45600.00 !RRKM 0.026 atm\nCH2CHO = CH3+CO                              7.200E+42   -9.521   47000.00 !RRKM 0.5 atm',
    ),
    longDesc = 
u"""
NIST DB
Reactions of CH2CHO
CH2CHO = CH3+CO                              2.340E+43  -10.099   45600.00 !RRKM 0.026 atm
CH2CHO = CH3+CO                              7.200E+42   -9.521   47000.00 !RRKM 0.5 atm
""",
)

entry(
    index = 204,
    label = "CH2CHO + H <=> CH3CHO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e+39, 'cm^6/(mol^2*s)'),
            n = -7.297,
            Ea = (4700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.55,
        T3 = (8900, 'K'),
        T1 = (4350, 'K'),
        T2 = (7244, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
        comment = 'RRKM 1 atm\nCH2CHO = CH3+CO                              1.200E+37   -7.456   46100.00 !RRKM 10 atm',
    ),
    longDesc = 
u"""
RRKM 1 atm
CH2CHO = CH3+CO                              1.200E+37   -7.456   46100.00 !RRKM 10 atm
""",
)

entry(
    index = 205,
    label = "CH2CHO + H <=> CH3CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Calculated RRKM',
    ),
    longDesc = 
u"""
Calculated RRKM
""",
)

entry(
    index = 206,
    label = "CH2CHO + H <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 207,
    label = "CH2CHO + H <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 208,
    label = "CH2CHO + O <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '82MIL/MIT',
    ),
    longDesc = 
u"""
82MIL/MIT
""",
)

entry(
    index = 209,
    label = "CH2CHO + OH <=> CH2CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '82MIL/MIT',
    ),
    longDesc = 
u"""
82MIL/MIT
""",
)

entry(
    index = 210,
    label = "CH2CHO + O2 <=> CH2CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '82MIL/MIT',
    ),
    longDesc = 
u"""
82MIL/MIT
""",
)

entry(
    index = 211,
    label = "CH2CHO + O2 <=> CH2O + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB',
    ),
    longDesc = 
u"""
92BAU/COB
""",
)

entry(
    index = 212,
    label = "CH3 + CO <=> CH3CO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.85e+07, 'cm^3/(mol*s)'),
            n = 1.65,
            Ea = (6150, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (7.8e+30, 'cm^6/(mol^2*s)'),
            n = -5.395,
            Ea = (8600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.258,
        T3 = (598, 'K'),
        T1 = (21002, 'K'),
        T2 = (1773, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3, '[Ar]': 0.7},
        comment = '92BAU/COB\nReactions of CH3CO',
    ),
    longDesc = 
u"""
92BAU/COB
Reactions of CH3CO
""",
)

entry(
    index = 213,
    label = "CH3CO + H <=> CH3CHO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.85e+44, 'cm^6/(mol^2*s)'),
            n = -8.569,
            Ea = (5500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (2900, 'K'),
        T1 = (2900, 'K'),
        T2 = (5132, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
        comment = 'kinf, RRKM',
    ),
    longDesc = 
u"""
kinf, RRKM
""",
)

entry(
    index = 214,
    label = "CH3CO + H <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 215,
    label = "CH3CO + O <=> CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 216,
    label = "CH3CO + O <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB',
    ),
    longDesc = 
u"""
92BAU/COB
""",
)

entry(
    index = 217,
    label = "CH3CO + OH <=> CH2CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM; 92BAU/COB',
    ),
    longDesc = 
u"""
86TSA/HAM; 92BAU/COB
""",
)

entry(
    index = 218,
    label = "CH3CO + OH <=> CH3 + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 219,
    label = "CH3CO + HO2 <=> CH3 + CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 220,
    label = "CH3CO + H2O2 <=> CH3CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8226, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 221,
    label = "CH3 + HCO <=> CH3CHO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.2e+48, 'cm^6/(mol^2*s)'),
            n = -9.588,
            Ea = (5100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6173,
        T3 = (13.076, 'K'),
        T1 = (2078, 'K'),
        T2 = (5093, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
        comment = '86TSA/HAM\nReactions of CH3CHO',
    ),
    longDesc = 
u"""
86TSA/HAM
Reactions of CH3CHO
""",
)

entry(
    index = 222,
    label = "CH3CHO + H <=> CH3CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS1, RRKM',
    ),
    longDesc = 
u"""
TS1, RRKM
""",
)

entry(
    index = 223,
    label = "CH3CHO + H <=> CH4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB',
    ),
    longDesc = 
u"""
92BAU/COB
""",
)

entry(
    index = 224,
    label = "CH3CHO + O <=> CH3CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '67LAM/CHR',
    ),
    longDesc = 
u"""
67LAM/CHR
""",
)

entry(
    index = 225,
    label = "CH3CHO + OH <=> CH3CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (-1110, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB',
    ),
    longDesc = 
u"""
92BAU/COB
""",
)

entry(
    index = 226,
    label = "CH3CHO + CH3 <=> CH3CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-06, 'cm^3/(mol*s)'),
        n = 5.6,
        Ea = (2460, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB',
    ),
    longDesc = 
u"""
92BAU/COB
""",
)

entry(
    index = 227,
    label = "CH3CHO + HCO <=> CO + HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB',
    ),
    longDesc = 
u"""
92BAU/COB
""",
)

entry(
    index = 228,
    label = "CH3CHO + O2 <=> CH3CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (39100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'NIST DB',
    ),
    longDesc = 
u"""
NIST DB
""",
)

entry(
    index = 229,
    label = "CH2OCH2 <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.63e+13, 's^-1'),
        n = 0,
        Ea = (57200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB\nReactions of CH2OCH2 (ethylene oxide)',
    ),
    longDesc = 
u"""
92BAU/COB
Reactions of CH2OCH2 (ethylene oxide)
""",
)

entry(
    index = 230,
    label = "CH2OCH2 <=> CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.26e+13, 's^-1'),
        n = 0,
        Ea = (57200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '83LIF/BEN',
    ),
    longDesc = 
u"""
83LIF/BEN
""",
)

entry(
    index = 231,
    label = "CH2OCH2 <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 's^-1'),
        n = 0,
        Ea = (57200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '83LIF/BEN',
    ),
    longDesc = 
u"""
83LIF/BEN
""",
)

entry(
    index = 232,
    label = "CH2OCH2 + H <=> CH2OCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '83LIF/BEN',
    ),
    longDesc = 
u"""
83LIF/BEN
""",
)

entry(
    index = 233,
    label = "CH2OCH2 + H <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '83LIF/BEN',
    ),
    longDesc = 
u"""
83LIF/BEN
""",
)

entry(
    index = 234,
    label = "CH2OCH2 + H <=> C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.51e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '83LIF/BEN',
    ),
    longDesc = 
u"""
83LIF/BEN
""",
)

entry(
    index = 235,
    label = "CH2OCH2 + O <=> CH2OCH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.91e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5250, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '83LIF/BEN',
    ),
    longDesc = 
u"""
83LIF/BEN
""",
)

entry(
    index = 236,
    label = "CH2OCH2 + OH <=> CH2OCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.78e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3610, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '78BOG/HAN',
    ),
    longDesc = 
u"""
78BOG/HAN
""",
)

entry(
    index = 237,
    label = "CH2OCH2 + CH3 <=> CH2OCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11830, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '84BOL/KEE',
    ),
    longDesc = 
u"""
84BOL/KEE
""",
)

entry(
    index = 238,
    label = "CH2OCH <=> CH3 + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.16e+14, 'cm^3/(mol*s)'), n=0, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '84BOL/KEE\nReactions of CH2OCH',
    ),
    longDesc = 
u"""
84BOL/KEE
Reactions of CH2OCH
""",
)

entry(
    index = 239,
    label = "CH2OCH <=> CH2CHO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '84BOL/KEE',
    ),
    longDesc = 
u"""
84BOL/KEE
""",
)

entry(
    index = 240,
    label = "CH2OCH <=> CH2CO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = '96WUR/McG',
    ),
    longDesc = 
u"""
96WUR/McG
""",
)

entry(
    index = 241,
    label = "C2H4 <=> H2 + H2CC",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(88770, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7e+50, 'cm^3/(mol*s)'),
            n = -9.31,
            Ea = (99860, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7345,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '83LIF/BEN\nReactions of C2H4',
    ),
    longDesc = 
u"""
83LIF/BEN
Reactions of C2H4
""",
)

entry(
    index = 242,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.367e+09, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1355, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.027e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.569,
        T3 = (299, 'K'),
        T1 = (9147, 'K'),
        T2 = (-152.4, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'GRI###',
    ),
    longDesc = 
u"""
GRI###
""",
)

entry(
    index = 243,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.07e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (12950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '04-MIL-KLI',
    ),
    longDesc = 
u"""
04-MIL-KLI
""",
)

entry(
    index = 244,
    label = "C2H4 + O <=> C2H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (3740, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96KNY/BEN',
    ),
    longDesc = 
u"""
96KNY/BEN
""",
)

entry(
    index = 245,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.92e+07, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (220, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '87MAH/MAR',
    ),
    longDesc = 
u"""
87MAH/MAR
""",
)

entry(
    index = 246,
    label = "C2H4 + O <=> CH2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (384000, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (220, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '87MAH/MAR',
    ),
    longDesc = 
u"""
87MAH/MAR
""",
)

entry(
    index = 247,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '87MAH/MAR',
    ),
    longDesc = 
u"""
87MAH/MAR
""",
)

entry(
    index = 248,
    label = "C2H4 + HCO <=> C2H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88LIU/MUL1',
    ),
    longDesc = 
u"""
88LIU/MUL1
""",
)

entry(
    index = 249,
    label = "C2H4 + CH <=> aC3H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 250,
    label = "C2H4 + CH <=> pC3H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 251,
    label = "C2H4 + CH2 <=> aC3H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 252,
    label = "C2H4 + CH2(S) <=> H2CC + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 253,
    label = "C2H4 + CH2(S) <=> aC3H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 254,
    label = "C2H4 + CH3 <=> C2H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (227000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (9200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 255,
    label = "C2H4 + CH3 <=> nC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 256,
    label = "C2H4 + C2H <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'KP',
    ),
    longDesc = 
u"""
KP
""",
)

entry(
    index = 257,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 258,
    label = "C2H4 + C2H3 <=> C4H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.93e+38, 'cm^3/(mol*s)'),
        n = -8.47,
        Ea = (14220, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM\nC2H4+C2H3 = C4H7                             1.21E+05     2.33    3680.0   !97WAN/FRE RRKM kinf\nC2H4+C2H3 = C4H7                             1.23E+35    -7.76    9930.0   !97WAN/FRE RRKM 0.1 atm',
    ),
    longDesc = 
u"""
86TSA/HAM
C2H4+C2H3 = C4H7                             1.21E+05     2.33    3680.0   !97WAN/FRE RRKM kinf
C2H4+C2H3 = C4H7                             1.23E+35    -7.76    9930.0   !97WAN/FRE RRKM 0.1 atm
""",
)

entry(
    index = 259,
    label = "C2H4 + HO2 <=> CH2OCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.82e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE RRKM 1 atm\nC2H4+C2H3 = C4H7                             2.99E+36    -7.40   15480.0   !97WAN/FRE RRKM 10 atm',
    ),
    longDesc = 
u"""
97WAN/FRE RRKM 1 atm
C2H4+C2H3 = C4H7                             2.99E+36    -7.40   15480.0   !97WAN/FRE RRKM 10 atm
""",
)

entry(
    index = 260,
    label = "C2H5 + H <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8422,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '92BAU/COB\nReactions of C2H5',
    ),
    longDesc = 
u"""
92BAU/COB
Reactions of C2H5
""",
)

entry(
    index = 261,
    label = "C2H5 + H <=> C2H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 262,
    label = "C2H5 + O <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.604e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 263,
    label = "C2H5 + O <=> CH3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 264,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 265,
    label = "C2H5 + HO2 <=> C2H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '90BOZ/DEA',
    ),
    longDesc = 
u"""
90BOZ/DEA
""",
)

entry(
    index = 266,
    label = "C2H5 + HO2 <=> C2H4 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 267,
    label = "C2H5 + HO2 <=> CH3 + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 268,
    label = "C2H5 + H2O2 <=> C2H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.7e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (974, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 269,
    label = "C2H5 + CH3 <=> C3H8",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.9e+14, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.8e+61, 'cm^6/(mol^2*s)'),
            n = -13.42,
            Ea = (6000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (1433.9, 'K'),
        T2 = (5328.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 270,
    label = "C2H5 + C2H3 <=> C4H81",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.55e+56, 'cm^6/(mol^2*s)'),
            n = -11.79,
            Ea = (8984.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.198,
        T3 = (2277.9, 'K'),
        T1 = (60000, 'K'),
        T2 = (5723.2, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 271,
    label = "C2H5 + C2H3 <=> aC3H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+32, 'cm^3/(mol*s)'),
        n = -5.22,
        Ea = (19747, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM\nC2H5+C2H3 = aC3H5+CH3                        8.00E+25  -3.46    11775.0    !86TSA/HAM RRKM 0.1 atm',
    ),
    longDesc = 
u"""
86TSA/HAM
C2H5+C2H3 = aC3H5+CH3                        8.00E+25  -3.46    11775.0    !86TSA/HAM RRKM 0.1 atm
""",
)

entry(
    index = 272,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM RRKM 1 atm\nC2H5+C2H3 = aC3H5+CH3                        3.90E+29  -4.24    22311.0    !86TSA/HAM RRKM 10 atm\nReactions of C2H6',
    ),
    longDesc = 
u"""
86TSA/HAM RRKM 1 atm
C2H5+C2H3 = aC3H5+CH3                        3.90E+29  -4.24    22311.0    !86TSA/HAM RRKM 10 atm
Reactions of C2H6
""",
)

entry(
    index = 273,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.98e+07, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (5690, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 274,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.54e+06, 'cm^3/(mol*s)'),
        n = 2.12,
        Ea = (870, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 275,
    label = "C2H6 + CH2(S) <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-550, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 276,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+06, 'cm^3/(mol*s)'),
        n = 1.74,
        Ea = (10450, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI',
    ),
    longDesc = 
u"""
GRI
""",
)

entry(
    index = 277,
    label = "C3H3 + H <=> pC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI\nReactions of C3H2\nC2H2 + CH = C3H2 + H                         3.00E+13    0.0        0.\nC3H2 + O = C2H2 + CO                         6.80E+13    0.0        0.\nC3H2 + OH = HCO + C2H2                       6.80E+13    0.0        0.\nC3H2 + O2 = HCCO + H + CO                    2.00E+12    0.0     1000.\nC3H2 + CH = C4H2 + H                         5.00E+13    0.0        0.\nC3H2 + CH2 = nC4H3 + H                       5.00E+13    0.0        0.\nC3H2 + CH3 = C4H4 + H                        5.00E+12    0.0        0.\nC3H2 + HCCO = nC4H3 + CO                     1.00E+13    0.0        0.\nC3H2 + H = C3H3\t                      1.00E+13    0.0        0.\nC3H3 + H = C3H2 + H2                         5.00E+13    0.0     1000.\nC3H3 + OH = C3H2 + H2O                       2.00E+13    0.0        0.\nC4H2 + O = C3H2 + CO                         2.70E+13    0.0     1720.\nC6H3 + O2 => CO + C3H2 + HCCO                5.00E+11    0.0        0.\nReactions of C3H3',
    ),
    longDesc = 
u"""
GRI
Reactions of C3H2
C2H2 + CH = C3H2 + H                         3.00E+13    0.0        0.
C3H2 + O = C2H2 + CO                         6.80E+13    0.0        0.
C3H2 + OH = HCO + C2H2                       6.80E+13    0.0        0.
C3H2 + O2 = HCCO + H + CO                    2.00E+12    0.0     1000.
C3H2 + CH = C4H2 + H                         5.00E+13    0.0        0.
C3H2 + CH2 = nC4H3 + H                       5.00E+13    0.0        0.
C3H2 + CH3 = C4H4 + H                        5.00E+12    0.0        0.
C3H2 + HCCO = nC4H3 + CO                     1.00E+13    0.0        0.
C3H2 + H = C3H3	                      1.00E+13    0.0        0.
C3H3 + H = C3H2 + H2                         5.00E+13    0.0     1000.
C3H3 + OH = C3H2 + H2O                       2.00E+13    0.0        0.
C4H2 + O = C3H2 + CO                         2.70E+13    0.0     1720.
C6H3 + O2 => CO + C3H2 + HCCO                5.00E+11    0.0        0.
Reactions of C3H3
""",
)

entry(
    index = 278,
    label = "C3H3 + H <=> aC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 279,
    label = "C3H3 + O <=> CH2O + C2H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 280,
    label = "C3H3 + O2 <=> CH2CO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2868, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '89MIL/BOW',
    ),
    longDesc = 
u"""
89MIL/BOW
""",
)

entry(
    index = 281,
    label = "C3H3 + HO2 <=> OH + CO + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88SLA/GUT',
    ),
    longDesc = 
u"""
88SLA/GUT
""",
)

entry(
    index = 282,
    label = "C3H3 + HO2 <=> aC3H4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 283,
    label = "C3H3 + HO2 <=> pC3H4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW',
    ),
    longDesc = 
u"""
99DAV/LAW
""",
)

entry(
    index = 284,
    label = "C3H3 + HCO <=> aC3H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW',
    ),
    longDesc = 
u"""
99DAV/LAW
""",
)

entry(
    index = 285,
    label = "C3H3 + HCO <=> pC3H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 286,
    label = "C3H3 + HCCO <=> C4H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 287,
    label = "C3H3 + CH <=> iC4H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 288,
    label = "C3H3 + CH2 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 289,
    label = "C3H3 + CH3 <=> C4H612",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.6e+57, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9770, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000, 'K'),
        T2 = (9769.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '92MIL/MEL',
    ),
    longDesc = 
u"""
92MIL/MEL
""",
)

entry(
    index = 290,
    label = "C3H3 + C2H2 <=> C5H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+55, 'cm^3/(mol*s)'),
        n = -12.5,
        Ea = (42025, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 291,
    label = "C3H3 + C3H3 => C6H5 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99MOS/LIN',
    ),
    longDesc = 
u"""
99MOS/LIN
""",
)

entry(
    index = 292,
    label = "C3H3 + C3H3 => C6H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 293,
    label = "C3H3 + C4H4 <=> C6H5CH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (653000, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (-4611, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 294,
    label = "C3H3 + C4H6 <=> C6H5CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (653000, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (-4611, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97JON/BAC',
    ),
    longDesc = 
u"""
97JON/BAC
""",
)

entry(
    index = 295,
    label = "aC3H4 + H <=> C3H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (5500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H3+C4H4\nReactions of aC3H4',
    ),
    longDesc = 
u"""
= C3H3+C4H4
Reactions of aC3H4
""",
)

entry(
    index = 296,
    label = "aC3H4 + H <=> CH3CHCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+29, 'cm^3/(mol*s)'),
        n = -6.09,
        Ea = (16300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW\naC3H4+H = CH3CHCH                            1.10E+30   -6.52   15200.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW
aC3H4+H = CH3CHCH                            1.10E+30   -6.52   15200.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 297,
    label = "aC3H4 + H <=> CH3CCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.46e+42, 'cm^3/(mol*s)'),
        n = -9.43,
        Ea = (11190, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\naC3H4+H = CH3CHCH                            2.60E+31   -6.23   18700.0    !99DAV/LAW RRKM 10 atm\naC3H4+H = CH3CHCH                            3.20E+31   -5.88   21500.0    !99DAV/LAW RRKM 100 atm\naC3H4+H = CH3CCH2                            9.20E+38   -8.65    7000.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
aC3H4+H = CH3CHCH                            2.60E+31   -6.23   18700.0    !99DAV/LAW RRKM 10 atm
aC3H4+H = CH3CHCH                            3.20E+31   -5.88   21500.0    !99DAV/LAW RRKM 100 atm
aC3H4+H = CH3CCH2                            9.20E+38   -8.65    7000.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 298,
    label = "aC3H4 + H <=> aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.52e+59, 'cm^3/(mol*s)'),
        n = -13.54,
        Ea = (26949, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\naC3H4+H = CH3CCH2                            8.47E+43   -9.59   12462.0    !99DAV/LAW RRKM 2 atm\naC3H4+H = CH3CCH2                            6.98E+44   -9.70   14032.0    !99DAV/LAW RRKM 5 atm\naC3H4+H = CH3CCH2                            1.50E+45   -9.69   15100.0    !99DAV/LAW RRKM 10 atm\naC3H4+H = CH3CCH2                            1.80E+43   -8.78   16800.0    !99DAV/LAW RRKM 100 atm\naC3H4+H = aC3H5                              9.60E+61  -14.67   26000.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
aC3H4+H = CH3CCH2                            8.47E+43   -9.59   12462.0    !99DAV/LAW RRKM 2 atm
aC3H4+H = CH3CCH2                            6.98E+44   -9.70   14032.0    !99DAV/LAW RRKM 5 atm
aC3H4+H = CH3CCH2                            1.50E+45   -9.69   15100.0    !99DAV/LAW RRKM 10 atm
aC3H4+H = CH3CCH2                            1.80E+43   -8.78   16800.0    !99DAV/LAW RRKM 100 atm
aC3H4+H = aC3H5                              9.60E+61  -14.67   26000.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 299,
    label = "aC3H4 + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\naC3H4+H = aC3H5                              3.78E+57  -12.98   26785.0    !99DAV/LAW RRKM 2 atm\naC3H4+H = aC3H5                              7.34E+54  -12.09   26187.0    !99DAV/LAW RRKM 5 atm\naC3H4+H = aC3H5                              2.40E+52  -11.30   25400.0    !99DAV/LAW RRKM 10 atm\naC3H4+H = aC3H5                              6.90E+41   -8.06   21300.0    !99DAV/LAW RRKM 100 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
aC3H4+H = aC3H5                              3.78E+57  -12.98   26785.0    !99DAV/LAW RRKM 2 atm
aC3H4+H = aC3H5                              7.34E+54  -12.09   26187.0    !99DAV/LAW RRKM 5 atm
aC3H4+H = aC3H5                              2.40E+52  -11.30   25400.0    !99DAV/LAW RRKM 10 atm
aC3H4+H = aC3H5                              6.90E+41   -8.06   21300.0    !99DAV/LAW RRKM 100 atm
""",
)

entry(
    index = 300,
    label = "aC3H4 + OH <=> C3H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98DAV/LAW',
    ),
    longDesc = 
u"""
98DAV/LAW
""",
)

entry(
    index = 301,
    label = "aC3H4 + CH3 <=> C3H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 302,
    label = "aC3H4 + CH3 <=> iC4H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '87WU/KER',
    ),
    longDesc = 
u"""
87WU/KER
""",
)

entry(
    index = 303,
    label = "aC3H4 + C2H <=> C2H2 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'PW P',
    ),
    longDesc = 
u"""
PW P
""",
)

entry(
    index = 304,
    label = "pC3H4 <=> cC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+44, 's^-1'),
        n = -9.92,
        Ea = (69250, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE\nReactions of pC3H4\npC3H4 = cC3H4                                1.73E+12   0.31    60015.0    !99DAV/LAW RRKM kinf\npC3H4 = cC3H4                                3.40E+46 -10.97    68900.0    !99DAV/LAW RRKM 0.1 atm\npC3H4 = cC3H4                                2.84E+45 -10.45    69284.0    !99DAV/LAW RRKM 0.4 atm',
    ),
    longDesc = 
u"""
97WAN/FRE
Reactions of pC3H4
pC3H4 = cC3H4                                1.73E+12   0.31    60015.0    !99DAV/LAW RRKM kinf
pC3H4 = cC3H4                                3.40E+46 -10.97    68900.0    !99DAV/LAW RRKM 0.1 atm
pC3H4 = cC3H4                                2.84E+45 -10.45    69284.0    !99DAV/LAW RRKM 0.4 atm
""",
)

entry(
    index = 305,
    label = "pC3H4 <=> aC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.15e+60, 's^-1'),
        n = -13.93,
        Ea = (91117, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\npC3H4 = cC3H4                                5.47E+42  -9.43    69089.0    !99DAV/LAW RRKM 2 atm\npC3H4 = cC3H4                                3.92E+40  -8.69    68706.0    !99DAV/LAW RRKM 5 atm\npC3H4 = cC3H4                                5.30E+38  -8.06    68300.0    !99DAV/LAW RRKM 10 atm\npC3H4 = cC3H4                                2.80E+31  -5.69    66400.0    !99DAV/LAW RRKM 100 atm\npC3H4 = aC3H4                                6.40E+61 -14.59    88200.0    !99DAV/LAW RRKM 0.1 atm\npC3H4 = aC3H4                                5.81E+62 -14.63    91211.0    !99DAV/LAW RRKM 0.4 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
pC3H4 = cC3H4                                5.47E+42  -9.43    69089.0    !99DAV/LAW RRKM 2 atm
pC3H4 = cC3H4                                3.92E+40  -8.69    68706.0    !99DAV/LAW RRKM 5 atm
pC3H4 = cC3H4                                5.30E+38  -8.06    68300.0    !99DAV/LAW RRKM 10 atm
pC3H4 = cC3H4                                2.80E+31  -5.69    66400.0    !99DAV/LAW RRKM 100 atm
pC3H4 = aC3H4                                6.40E+61 -14.59    88200.0    !99DAV/LAW RRKM 0.1 atm
pC3H4 = aC3H4                                5.81E+62 -14.63    91211.0    !99DAV/LAW RRKM 0.4 atm
""",
)

entry(
    index = 306,
    label = "pC3H4 + H <=> aC3H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.27e+17, 'cm^3/(mol*s)'),
        n = -0.91,
        Ea = (10079, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\npC3H4 = aC3H4                                7.64E+59 -13.59    91817.0    !99DAV/LAW RRKM 2 atm\npC3H4 = aC3H4                                3.12E+58 -13.07    92680.0    !99DAV/LAW RRKM 5 atm\npC3H4 = aC3H4                                1.90E+57 -12.62    93300.0    !99DAV/LAW RRKM 10 atm\npC3H4 = aC3H4                                1.40E+52 -10.86    95400.0    !99DAV/LAW RRKM 100 atm\npC3H4+H = aC3H4+H                            2.30E+15  -0.26     7600.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
pC3H4 = aC3H4                                7.64E+59 -13.59    91817.0    !99DAV/LAW RRKM 2 atm
pC3H4 = aC3H4                                3.12E+58 -13.07    92680.0    !99DAV/LAW RRKM 5 atm
pC3H4 = aC3H4                                1.90E+57 -12.62    93300.0    !99DAV/LAW RRKM 10 atm
pC3H4 = aC3H4                                1.40E+52 -10.86    95400.0    !99DAV/LAW RRKM 100 atm
pC3H4+H = aC3H4+H                            2.30E+15  -0.26     7600.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 307,
    label = "pC3H4 + H <=> CH3CCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+47, 'cm^3/(mol*s)'),
        n = -10.58,
        Ea = (13690, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\npC3H4+H = aC3H4+H                            1.50E+18  -1.00    10756.0    !99DAV/LAW RRKM 2 atm\npC3H4+H = aC3H4+H                            1.93E+18  -1.01    11523.0    !99DAV/LAW RRKM 5 atm\npC3H4+H = aC3H4+H                            3.10E+22  -2.18    14800.0    !99DAV/LAW RRKM 10 atm\npC3H4+H = aC3H4+H                            6.40E+27  -3.58    21200.0    !99DAV/LAW RRKM 100 atm\npC3H4+H = CH3CCH2                            4.60E+44 -10.21    10200.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
pC3H4+H = aC3H4+H                            1.50E+18  -1.00    10756.0    !99DAV/LAW RRKM 2 atm
pC3H4+H = aC3H4+H                            1.93E+18  -1.01    11523.0    !99DAV/LAW RRKM 5 atm
pC3H4+H = aC3H4+H                            3.10E+22  -2.18    14800.0    !99DAV/LAW RRKM 10 atm
pC3H4+H = aC3H4+H                            6.40E+27  -3.58    21200.0    !99DAV/LAW RRKM 100 atm
pC3H4+H = CH3CCH2                            4.60E+44 -10.21    10200.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 308,
    label = "pC3H4 + H <=> CH3CHCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.5e+28, 'cm^3/(mol*s)'),
        n = -5.74,
        Ea = (4300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\npC3H4+H = CH3CCH2                            5.04E+47 -10.61    14707.0    !99DAV/LAW RRKM 2 atm\npC3H4+H = CH3CCH2                            9.62E+47 -10.55    15910.0    !99DAV/LAW RRKM 5 atm\npC3H4+H = CH3CCH2                            7.00E+47 -10.40    16600.0    !99DAV/LAW RRKM 10 atm\npC3H4+H = CH3CCH2                            3.20E+44  -9.11    17400.0    !99DAV/LAW RRKM 100 atm\npC3H4+H = CH3CHCH                            1.00E+25 -5.00      1800.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
pC3H4+H = CH3CCH2                            5.04E+47 -10.61    14707.0    !99DAV/LAW RRKM 2 atm
pC3H4+H = CH3CCH2                            9.62E+47 -10.55    15910.0    !99DAV/LAW RRKM 5 atm
pC3H4+H = CH3CCH2                            7.00E+47 -10.40    16600.0    !99DAV/LAW RRKM 10 atm
pC3H4+H = CH3CCH2                            3.20E+44  -9.11    17400.0    !99DAV/LAW RRKM 100 atm
pC3H4+H = CH3CHCH                            1.00E+25 -5.00      1800.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 309,
    label = "pC3H4 + H <=> aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.91e+60, 'cm^3/(mol*s)'),
        n = -14.37,
        Ea = (31644, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\npC3H4+H = CH3CHCH                            1.00E+34 -6.88      8900.0    !99DAV/LAW RRKM 10 atm\npC3H4+H = CH3CHCH                            9.70E+37 -7.63     13800.0    !99DAV/LAW RRKM 100 atm\npC3H4+H = aC3H5                              1.10E+60 -14.56    28100.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
pC3H4+H = CH3CHCH                            1.00E+34 -6.88      8900.0    !99DAV/LAW RRKM 10 atm
pC3H4+H = CH3CHCH                            9.70E+37 -7.63     13800.0    !99DAV/LAW RRKM 100 atm
pC3H4+H = aC3H5                              1.10E+60 -14.56    28100.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 310,
    label = "pC3H4 + H <=> C3H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (5500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\npC3H4+H = aC3H5                              3.04E+60 -14.19    32642.0    !99DAV/LAW RRKM 2 atm\npC3H4+H = aC3H5                              9.02E+59 -13.89    33953.0    !99DAV/LAW RRKM 5 atm\npC3H4+H = aC3H5                              2.20E+59 -13.61    34900.0    !99DAV/LAW RRKM 10 atm\npC3H4+H = aC3H5                              1.60E+55 -12.07    37500.0    !99DAV/LAW RRKM 100 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
pC3H4+H = aC3H5                              3.04E+60 -14.19    32642.0    !99DAV/LAW RRKM 2 atm
pC3H4+H = aC3H5                              9.02E+59 -13.89    33953.0    !99DAV/LAW RRKM 5 atm
pC3H4+H = aC3H5                              2.20E+59 -13.61    34900.0    !99DAV/LAW RRKM 10 atm
pC3H4+H = aC3H5                              1.60E+55 -12.07    37500.0    !99DAV/LAW RRKM 100 atm
""",
)

entry(
    index = 311,
    label = "pC3H4 + C3H3 <=> aC3H4 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+06, 'cm^3/(mol*s)'),
        n = 1.74,
        Ea = (10450, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 312,
    label = "pC3H4 + O <=> HCCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2250, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 313,
    label = "pC3H4 + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2250, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96ADU/BLU#',
    ),
    longDesc = 
u"""
96ADU/BLU#
""",
)

entry(
    index = 314,
    label = "pC3H4 + OH <=> C3H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96ADU/BLU#',
    ),
    longDesc = 
u"""
96ADU/BLU#
""",
)

entry(
    index = 315,
    label = "pC3H4 + C2H <=> C2H2 + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98DAV/LAW',
    ),
    longDesc = 
u"""
98DAV/LAW
""",
)

entry(
    index = 316,
    label = "pC3H4 + CH3 <=> C3H3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 317,
    label = "cC3H4 <=> aC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.89e+41, 's^-1'),
        n = -9.17,
        Ea = (49594, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '87WU/KER\nReactions of cC3H4\ncC3H4 = aC3H4                                1.98E+12   0.56    42240.0    !99DAV/LAW RRKM kinf\ncC3H4 = aC3H4                                2.30E+39  -8.81    47800.0    !99DAV/LAW RRKM 0.1 atm\ncC3H4 = aC3H4                                7.59E+40  -9.07    48831.0    !99DAV/LAW RRKM 0.4 atm',
    ),
    longDesc = 
u"""
87WU/KER
Reactions of cC3H4
cC3H4 = aC3H4                                1.98E+12   0.56    42240.0    !99DAV/LAW RRKM kinf
cC3H4 = aC3H4                                2.30E+39  -8.81    47800.0    !99DAV/LAW RRKM 0.1 atm
cC3H4 = aC3H4                                7.59E+40  -9.07    48831.0    !99DAV/LAW RRKM 0.4 atm
""",
)

entry(
    index = 318,
    label = "aC3H5 + H <=> C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.33e+60, 'cm^6/(mol^2*s)'),
            n = -12,
            Ea = (5967.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.02,
        T3 = (1096.6, 'K'),
        T1 = (1096.6, 'K'),
        T2 = (6859.5, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '99DAV/LAW RRKM 1 atm\ncC3H4 = aC3H4                                8.81E+41  -9.15    50073.0    !99DAV/LAW RRKM 2 atm\ncC3H4 = aC3H4                                4.33E+41  -8.93    50475.0    !99DAV/LAW RRKM 5 atm\ncC3H4 = aC3H4                                7.20E+40  -8.60    50600.0    !99DAV/LAW RRKM 10 atm\ncC3H4 = aC3H4                                1.60E+35  -6.64    49500.0    !99DAV/LAW RRKM 100 atm\nReactions of allyl',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
cC3H4 = aC3H4                                8.81E+41  -9.15    50073.0    !99DAV/LAW RRKM 2 atm
cC3H4 = aC3H4                                4.33E+41  -8.93    50475.0    !99DAV/LAW RRKM 5 atm
cC3H4 = aC3H4                                7.20E+40  -8.60    50600.0    !99DAV/LAW RRKM 10 atm
cC3H4 = aC3H4                                1.60E+35  -6.64    49500.0    !99DAV/LAW RRKM 100 atm
Reactions of allyl
""",
)

entry(
    index = 319,
    label = "aC3H5 + H <=> aC3H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 320,
    label = "aC3H5 + O <=> C2H3CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 321,
    label = "aC3H5 + OH <=> C2H3CHO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+32, 'cm^3/(mol*s)'),
        n = -5.16,
        Ea = (30126, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA\naC3H5+OH = C2H3CHO+H+H                       5.30E+37  -6.71    29306.0    !91TSA RRKM 0.1 atm',
    ),
    longDesc = 
u"""
91TSA
aC3H5+OH = C2H3CHO+H+H                       5.30E+37  -6.71    29306.0    !91TSA RRKM 0.1 atm
""",
)

entry(
    index = 322,
    label = "aC3H5 + OH <=> aC3H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA RRKM 1 atm\naC3H5+OH = C2H3CHO+H+H                       1.60E+20  -1.56    26330.0    !91TSA RRKM 10 atm',
    ),
    longDesc = 
u"""
91TSA RRKM 1 atm
aC3H5+OH = C2H3CHO+H+H                       1.60E+20  -1.56    26330.0    !91TSA RRKM 10 atm
""",
)

entry(
    index = 323,
    label = "aC3H5 + O2 <=> aC3H4 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.99e+15, 'cm^3/(mol*s)'),
        n = -1.4,
        Ea = (22428, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 324,
    label = "aC3H5 + O2 <=> CH3CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.19e+15, 'cm^3/(mol*s)'),
        n = -1.01,
        Ea = (20128, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '93BOZ/DEA RRKM 1 atm\naC3H5+O2 = aC3H4+HO2                         2.18E+21  -2.85    30755.0    !93BOZ/DEA RRKM 10 atm',
    ),
    longDesc = 
u"""
93BOZ/DEA RRKM 1 atm
aC3H5+O2 = aC3H4+HO2                         2.18E+21  -2.85    30755.0    !93BOZ/DEA RRKM 10 atm
""",
)

entry(
    index = 325,
    label = "aC3H5 + O2 <=> C2H3CHO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.82e+13, 'cm^3/(mol*s)'),
        n = -0.41,
        Ea = (22859, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '93BOZ/DEA RRKM 1 atm\naC3H5+O2 = CH3CO+CH2O                        7.14E+15  -1.21    21046.0    !93BOZ/DEA RRKM 10 atm',
    ),
    longDesc = 
u"""
93BOZ/DEA RRKM 1 atm
aC3H5+O2 = CH3CO+CH2O                        7.14E+15  -1.21    21046.0    !93BOZ/DEA RRKM 10 atm
""",
)

entry(
    index = 326,
    label = "aC3H5 + HO2 <=> C3H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.66e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '93BOZ/DEA RRKM 1 atm\naC3H5+O2 = C2H3CHO+OH                        2.47E+13  -0.45    23017.0    !93BOZ/DEA RRKM 10 atm',
    ),
    longDesc = 
u"""
93BOZ/DEA RRKM 1 atm
aC3H5+O2 = C2H3CHO+OH                        2.47E+13  -0.45    23017.0    !93BOZ/DEA RRKM 10 atm
""",
)

entry(
    index = 327,
    label = "aC3H5 + HO2 <=> OH + C2H3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB',
    ),
    longDesc = 
u"""
92BAU/COB
""",
)

entry(
    index = 328,
    label = "aC3H5 + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB',
    ),
    longDesc = 
u"""
92BAU/COB
""",
)

entry(
    index = 329,
    label = "aC3H5 + CH3 <=> C4H81",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1e+14, 'cm^3/(mol*s)'),
            n = -0.32,
            Ea = (-262.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.91e+60, 'cm^6/(mol^2*s)'),
            n = -12.81,
            Ea = (6250, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.104,
        T3 = (1606, 'K'),
        T1 = (60000, 'K'),
        T2 = (6118.4, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 330,
    label = "aC3H5 + CH3 <=> aC3H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+12, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-131, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 331,
    label = "aC3H5 <=> CH3CCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.06e+56, 's^-1'),
        n = -14.08,
        Ea = (75868, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA !\naC3H5 = CH3CCH2                              3.90E+59 -15.42    75400.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
91TSA !
aC3H5 = CH3CCH2                              3.90E+59 -15.42    75400.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 332,
    label = "aC3H5 <=> CH3CHCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+51, 's^-1'),
        n = -13.02,
        Ea = (73300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\naC3H5 = CH3CCH2                              4.80E+55 -13.59    75949.0    !99DAV/LAW RRKM 2 atm\naC3H5 = CH3CCH2                              4.86E+53 -12.81    75883.0    !99DAV/LAW RRKM 5 atm\naC3H5 = CH3CCH2                              6.40E+51 -12.12    75700.0    !99DAV/LAW RRKM 10 atm\naC3H5 = CH3CCH2                              2.80E+43  -9.27    74000.0    !99DAV/LAW RRKM 100 atm\naC3H5 = CH3CHCH                              1.30E+55 -14.53    73800.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
aC3H5 = CH3CCH2                              4.80E+55 -13.59    75949.0    !99DAV/LAW RRKM 2 atm
aC3H5 = CH3CCH2                              4.86E+53 -12.81    75883.0    !99DAV/LAW RRKM 5 atm
aC3H5 = CH3CCH2                              6.40E+51 -12.12    75700.0    !99DAV/LAW RRKM 10 atm
aC3H5 = CH3CCH2                              2.80E+43  -9.27    74000.0    !99DAV/LAW RRKM 100 atm
aC3H5 = CH3CHCH                              1.30E+55 -14.53    73800.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 333,
    label = "aC3H5 + C2H2 <=> lC5H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.38e+30, 'cm^3/(mol*s)'),
        n = -6.242,
        Ea = (12824, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\naC3H5 = CH3CHCH                              9.70E+48 -11.73    73700.0    !99DAV/LAW RRKM 10 atm\naC3H5 = CH3CHCH                              4.86E+44 -9.84     73400.0    !99DAV/LAW RRKM 100 atm\naC3H5+C2H2 = C5H6+H                          3.97E+14  0.00  0  24892.0    !91TSA',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
aC3H5 = CH3CHCH                              9.70E+48 -11.73    73700.0    !99DAV/LAW RRKM 10 atm
aC3H5 = CH3CHCH                              4.86E+44 -9.84     73400.0    !99DAV/LAW RRKM 100 atm
aC3H5+C2H2 = C5H6+H                          3.97E+14  0.00  0  24892.0    !91TSA
""",
)

entry(
    index = 334,
    label = "CH3CCH2 <=> CH3CHCH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+48, 's^-1'),
        n = -12.71,
        Ea = (53900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '90DEAN\nReactions of CH3CCH2\nCH3CCH2 = CH3CHCH                            1.60E+44 -12.16    52200.0    !99DAV/LAW RRKM 0.1 atm',
    ),
    longDesc = 
u"""
90DEAN
Reactions of CH3CCH2
CH3CCH2 = CH3CHCH                            1.60E+44 -12.16    52200.0    !99DAV/LAW RRKM 0.1 atm
""",
)

entry(
    index = 335,
    label = "CH3CCH2 + H <=> pC3H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.34e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW RRKM 1 atm\nCH3CCH2 = CH3CHCH                            5.10E+52 -13.37    57200.0    !99DAV/LAW RRKM 10 atm\nCH3CCH2 = CH3CHCH                            5.80E+51 -12.43    59200.0    !99DAV/LAW RRKM 100 atm',
    ),
    longDesc = 
u"""
99DAV/LAW RRKM 1 atm
CH3CCH2 = CH3CHCH                            5.10E+52 -13.37    57200.0    !99DAV/LAW RRKM 10 atm
CH3CCH2 = CH3CHCH                            5.80E+51 -12.43    59200.0    !99DAV/LAW RRKM 100 atm
""",
)

entry(
    index = 336,
    label = "CH3CCH2 + O <=> CH3 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW',
    ),
    longDesc = 
u"""
99DAV/LAW
""",
)

entry(
    index = 337,
    label = "CH3CCH2 + OH <=> CH3 + CH2CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 338,
    label = "CH3CCH2 + O2 <=> CH3CO + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 339,
    label = "CH3CCH2 + HO2 <=> CH3 + CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW',
    ),
    longDesc = 
u"""
99DAV/LAW
""",
)

entry(
    index = 340,
    label = "CH3CCH2 + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 341,
    label = "CH3CCH2 + CH3 <=> pC3H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 342,
    label = "CH3CCH2 + CH3 <=> iC4H8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99DAV/LAW',
    ),
    longDesc = 
u"""
99DAV/LAW
""",
)

entry(
    index = 343,
    label = "CH3CHCH + H <=> pC3H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.34e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'PW P\nReactions of CH3CHCH',
    ),
    longDesc = 
u"""
PW P
Reactions of CH3CHCH
""",
)

entry(
    index = 344,
    label = "CH3CHCH + O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= CH3CCH2+H',
    ),
    longDesc = 
u"""
= CH3CCH2+H
""",
)

entry(
    index = 345,
    label = "CH3CHCH + OH <=> C2H4 + HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 346,
    label = "CH3CHCH + O2 <=> CH3CHO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 347,
    label = "CH3CHCH + HO2 <=> C2H4 + HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= CH3CCH2+O2',
    ),
    longDesc = 
u"""
= CH3CCH2+O2
""",
)

entry(
    index = 348,
    label = "CH3CHCH + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= CH3CCH2+HO2',
    ),
    longDesc = 
u"""
= CH3CCH2+HO2
""",
)

entry(
    index = 349,
    label = "CH3CHCH + CH3 <=> pC3H4 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= CH3CCH2+HCO',
    ),
    longDesc = 
u"""
= CH3CCH2+HCO
""",
)

entry(
    index = 350,
    label = "C3H6 + H <=> nC3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.33e+13, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (3260.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.26e+38, 'cm^6/(mol^2*s)'),
            n = -6.66,
            Ea = (7000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (1310, 'K'),
        T2 = (48097, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '= CH3CCH2+CH3\nReactions of C3H6',
    ),
    longDesc = 
u"""
= CH3CCH2+CH3
Reactions of C3H6
""",
)

entry(
    index = 351,
    label = "C3H6 + H <=> iC3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.33e+13, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (1559.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (8.7e+42, 'cm^6/(mol^2*s)'),
            n = -7.5,
            Ea = (4721.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (645.4, 'K'),
        T2 = (6844.3, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 352,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA\nC3H6+H = C2H4+CH3                            8.80E+16  -1.05     6461.0    !91TSA RRKM 0.1 atm',
    ),
    longDesc = 
u"""
91TSA
C3H6+H = C2H4+CH3                            8.80E+16  -1.05     6461.0    !91TSA RRKM 0.1 atm
""",
)

entry(
    index = 353,
    label = "C3H6 + H <=> aC3H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (173000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA RRKM 1 atm\nC3H6+H = C2H4+CH3                            3.30E+24  -3.04    15610.0    !91TSA RRKM 10 atm',
    ),
    longDesc = 
u"""
91TSA RRKM 1 atm
C3H6+H = C2H4+CH3                            3.30E+24  -3.04    15610.0    !91TSA RRKM 10 atm
""",
)

entry(
    index = 354,
    label = "C3H6 + H <=> CH3CCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (9790, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 355,
    label = "C3H6 + H <=> CH3CHCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (804000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (12283, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 356,
    label = "C3H6 + O <=> CH2CO + CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+07, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (327, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 357,
    label = "C3H6 + O <=> C2H3CHO + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+07, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (327, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 358,
    label = "C3H6 + O <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+07, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (-972, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 359,
    label = "C3H6 + O <=> aC3H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5880, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 360,
    label = "C3H6 + O <=> CH3CCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7630, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 361,
    label = "C3H6 + O <=> CH3CHCH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8960, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 362,
    label = "C3H6 + OH <=> aC3H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-298, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 363,
    label = "C3H6 + OH <=> CH3CCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1450, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 364,
    label = "C3H6 + OH <=> CH3CHCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.14e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2778, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 365,
    label = "C3H6 + HO2 <=> aC3H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9600, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 366,
    label = "C3H6 + CH3 <=> aC3H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (5675, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 367,
    label = "C3H6 + CH3 <=> CH3CCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.84, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (11660, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 368,
    label = "C3H6 + CH3 <=> CH3CHCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (12848, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 369,
    label = "C3H6 + C2H3 <=> C4H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 370,
    label = "C3H6 + HO2 <=> CH3CHOCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.09e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91TSA',
    ),
    longDesc = 
u"""
91TSA
""",
)

entry(
    index = 371,
    label = "C2H3CHO + H <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+11, 'cm^3/(mol*s)'),
        n = 0.454,
        Ea = (5820, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '85BAL/HIS\nReactions of C2H3CHO',
    ),
    longDesc = 
u"""
85BAL/HIS
Reactions of C2H3CHO
""",
)

entry(
    index = 372,
    label = "C2H3CHO + O <=> C2H3 + OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3540, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H4+H',
    ),
    longDesc = 
u"""
= C2H4+H
""",
)

entry(
    index = 373,
    label = "C2H3CHO + O <=> CH2O + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (220, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= CH2O+O',
    ),
    longDesc = 
u"""
= CH2O+O
""",
)

entry(
    index = 374,
    label = "C2H3CHO + OH <=> C2H3 + H2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-447, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H4+O',
    ),
    longDesc = 
u"""
= C2H4+O
""",
)

entry(
    index = 375,
    label = "C2H3CHO + CH3 <=> CH2CHCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= CH2O+OH',
    ),
    longDesc = 
u"""
= CH2O+OH
""",
)

entry(
    index = 376,
    label = "C2H3CHO + C2H3 <=> C4H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+21, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (14720, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 377,
    label = "CH2CHCO <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (27000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H4+C2H3\nReactions of CH2CHCO',
    ),
    longDesc = 
u"""
= C2H4+C2H3
Reactions of CH2CHCO
""",
)

entry(
    index = 378,
    label = "CH2CHCO + H <=> C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 379,
    label = "CH3CHOCH2 <=> CH3CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e+14, 's^-1'),
        n = 0,
        Ea = (58500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated\nReactions of CH3CHOCH2',
    ),
    longDesc = 
u"""
Estimated
Reactions of CH3CHOCH2
""",
)

entry(
    index = 380,
    label = "CH3CHOCH2 <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.45e+13, 's^-1'),
        n = 0,
        Ea = (58500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '77FLO',
    ),
    longDesc = 
u"""
77FLO
""",
)

entry(
    index = 381,
    label = "CH3CHOCH2 <=> CH3 + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.45e+13, 's^-1'),
        n = 0,
        Ea = (58800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '94LIF/TAM',
    ),
    longDesc = 
u"""
94LIF/TAM
""",
)

entry(
    index = 382,
    label = "CH3CHOCH2 <=> CH3COCH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.01e+14, 's^-1'),
        n = 0,
        Ea = (59900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '94LIF/TAM',
    ),
    longDesc = 
u"""
94LIF/TAM
""",
)

entry(
    index = 383,
    label = "CH3CHOCH2 <=> CH3 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.54e+13, 's^-1'),
        n = 0,
        Ea = (59900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '77FLO',
    ),
    longDesc = 
u"""
77FLO
""",
)

entry(
    index = 384,
    label = "iC3H7 + H <=> C3H8",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+58, 'cm^6/(mol^2*s)'),
            n = -12.08,
            Ea = (11263.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.649,
        T3 = (1213.1, 'K'),
        T1 = (1213.1, 'K'),
        T2 = (13369.7, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '94LIF/TAM\nReactions of iC3H7',
    ),
    longDesc = 
u"""
94LIF/TAM
Reactions of iC3H7
""",
)

entry(
    index = 385,
    label = "iC3H7 + H <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA\niC3H7+H = CH3+C2H5                           5.90E+23  -2.81    10009.0    !88TSA RRKM 0.1 atm',
    ),
    longDesc = 
u"""
88TSA
iC3H7+H = CH3+C2H5                           5.90E+23  -2.81    10009.0    !88TSA RRKM 0.1 atm
""",
)

entry(
    index = 386,
    label = "iC3H7 + H <=> C3H6 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA RRKM 1 atm\niC3H7+H = CH3+C2H5                           4.00E+24  -2.83    17542.0    !88TSA RRKM 10 atm',
    ),
    longDesc = 
u"""
88TSA RRKM 1 atm
iC3H7+H = CH3+C2H5                           4.00E+24  -2.83    17542.0    !88TSA RRKM 10 atm
""",
)

entry(
    index = 387,
    label = "iC3H7 + O <=> CH3CHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 388,
    label = "iC3H7 + OH <=> C3H6 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 389,
    label = "iC3H7 + O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 390,
    label = "iC3H7 + HO2 <=> CH3CHO + CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 391,
    label = "iC3H7 + HCO <=> C3H8 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 392,
    label = "iC3H7 + CH3 <=> CH4 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 393,
    label = "nC3H7 + H <=> C3H8",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '88TSA\nReactions of nC3H7',
    ),
    longDesc = 
u"""
88TSA
Reactions of nC3H7
""",
)

entry(
    index = 394,
    label = "nC3H7 + H <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12505, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA\nnC3H7+H = C2H5+CH3                           3.40E+18  -1.33     5386.0    !88TSA RRKM 0.1 atm',
    ),
    longDesc = 
u"""
88TSA
nC3H7+H = C2H5+CH3                           3.40E+18  -1.33     5386.0    !88TSA RRKM 0.1 atm
""",
)

entry(
    index = 395,
    label = "nC3H7 + H <=> C3H6 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA RRKM 1 atm\nnC3H7+H = C2H5+CH3                           3.10E+27  -3.59    19059.0    !88TSA RRKM 10 atm',
    ),
    longDesc = 
u"""
88TSA RRKM 1 atm
nC3H7+H = C2H5+CH3                           3.10E+27  -3.59    19059.0    !88TSA RRKM 10 atm
""",
)

entry(
    index = 396,
    label = "nC3H7 + O <=> C2H5 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 397,
    label = "nC3H7 + OH <=> C3H6 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 398,
    label = "nC3H7 + O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 399,
    label = "nC3H7 + HO2 <=> C2H5 + OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 400,
    label = "nC3H7 + HCO <=> C3H8 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 401,
    label = "nC3H7 + CH3 <=> CH4 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 402,
    label = "C3H8 + H <=> H2 + nC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA\nReactions of C3H8',
    ),
    longDesc = 
u"""
88TSA
Reactions of C3H8
""",
)

entry(
    index = 403,
    label = "C3H8 + H <=> H2 + iC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 404,
    label = "C3H8 + O <=> nC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (190000, 'cm^3/(mol*s)'),
        n = 2.68,
        Ea = (3716, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 405,
    label = "C3H8 + O <=> iC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (2106, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 406,
    label = "C3H8 + OH <=> nC3H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 407,
    label = "C3H8 + OH <=> iC3H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (27000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (393, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 408,
    label = "C3H8 + O2 <=> nC3H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 409,
    label = "C3H8 + O2 <=> iC3H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 410,
    label = "C3H8 + HO2 <=> nC3H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 411,
    label = "C3H8 + HO2 <=> iC3H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9640, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 412,
    label = "C3H8 + CH3 <=> CH4 + nC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 413,
    label = "C3H8 + CH3 <=> CH4 + iC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 414,
    label = "C4H2 + H <=> nC4H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+42, 'cm^3/(mol*s)'),
        n = -8.72,
        Ea = (15300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA\nReactions of C4H2\nC4H2 + H = nC4H3                             1.70E+49 -11.67   12804.0     !   20 Torr RRKM WAN/FRE\nC4H2 + H = nC4H3                             3.30E+50 -11.80   15010.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
88TSA
Reactions of C4H2
C4H2 + H = nC4H3                             1.70E+49 -11.67   12804.0     !   20 Torr RRKM WAN/FRE
C4H2 + H = nC4H3                             3.30E+50 -11.80   15010.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 415,
    label = "C4H2 + H <=> iC4H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+30, 'cm^3/(mol*s)'),
        n = -4.92,
        Ea = (10800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nC4H2 + H = iC4H3                             4.30E+45 -10.15   13250.0     !   20 Torr RRKM WAN/FRE\nC4H2 + H = iC4H3                             2.60E+46 -10.15   15500.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
C4H2 + H = iC4H3                             4.30E+45 -10.15   13250.0     !   20 Torr RRKM WAN/FRE
C4H2 + H = iC4H3                             2.60E+46 -10.15   15500.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 416,
    label = "C4H2 + OH <=> H2C4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-410, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
""",
)

entry(
    index = 417,
    label = "C4H2 + C2H <=> C6H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '84PER',
    ),
    longDesc = 
u"""
84PER
""",
)

entry(
    index = 418,
    label = "C4H2 + C2H <=> C6H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+37, 'cm^3/(mol*s)'),
        n = -7.68,
        Ea = (7100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H2 + C2H\nC4H2 + C2H = C6H3                            1.10E+30   -6.30   2790.0     !   20 Torr RRKM WAN/FRE\nC4H2 + C2H = C6H3                            1.30E+30   -6.12   2510.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
= C2H2 + C2H
C4H2 + C2H = C6H3                            1.10E+30   -6.30   2790.0     !   20 Torr RRKM WAN/FRE
C4H2 + C2H = C6H3                            1.30E+30   -6.12   2510.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 419,
    label = "H2C4O + H <=> C2H2 + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nReactions of H2C4O',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
Reactions of H2C4O
""",
)

entry(
    index = 420,
    label = "H2C4O + OH <=> CH2CO + HCCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92MIL/MEL',
    ),
    longDesc = 
u"""
92MIL/MEL
""",
)

entry(
    index = 421,
    label = "nC4H3 <=> iC4H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+43, 's^-1'),
        n = -9.49,
        Ea = (53000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92MIL/MEL\nReactions of nC4H3\nnC4H3 = iC4H3                                3.70E+61  -15.81  54890.0     !   20 Torr RRKM WAN/FRE\nnC4H3 = iC4H3                                1.00E+51  -12.45  51000.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
92MIL/MEL
Reactions of nC4H3
nC4H3 = iC4H3                                3.70E+61  -15.81  54890.0     !   20 Torr RRKM WAN/FRE
nC4H3 = iC4H3                                1.00E+51  -12.45  51000.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 422,
    label = "nC4H3 + H <=> iC4H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+20, 'cm^3/(mol*s)'),
        n = -1.67,
        Ea = (10800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nnC4H3 + H = iC4H3 + H                        2.40E+11    0.79   2410.0     !   20 Torr RRKM WAN/FRE\nnC4H3 + H = iC4H3 + H                        9.20E+11    0.63   2990.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
nC4H3 + H = iC4H3 + H                        2.40E+11    0.79   2410.0     !   20 Torr RRKM WAN/FRE
nC4H3 + H = iC4H3 + H                        9.20E+11    0.63   2990.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 423,
    label = "nC4H3 + H <=> C2H2 + H2CC",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+25, 'cm^3/(mol*s)'),
        n = -3.34,
        Ea = (10014, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nnC4H3 + H = C2H2 + H2CC                      1.60E+19   -1.60   2220.0     !   20 Torr RRKM WAN/FRE\nnC4H3 + H = C2H2 + H2CC                      1.30E+20   -1.85   2960.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
nC4H3 + H = C2H2 + H2CC                      1.60E+19   -1.60   2220.0     !   20 Torr RRKM WAN/FRE
nC4H3 + H = C2H2 + H2CC                      1.30E+20   -1.85   2960.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 424,
    label = "nC4H3 + H <=> C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+47, 'cm^3/(mol*s)'),
        n = -10.26,
        Ea = (13070, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nnC4H3 + H = C4H4                             1.10E+42   -9.65   7000.0     !   20 Torr RRKM WAN/FRE\nnC4H3 + H = C4H4                             1.10E+42   -9.65   7000.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
nC4H3 + H = C4H4                             1.10E+42   -9.65   7000.0     !   20 Torr RRKM WAN/FRE
nC4H3 + H = C4H4                             1.10E+42   -9.65   7000.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 425,
    label = "nC4H3 + H <=> C4H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
""",
)

entry(
    index = 426,
    label = "nC4H3 + OH <=> C4H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= 0.5*C2H3+H',
    ),
    longDesc = 
u"""
= 0.5*C2H3+H
""",
)

entry(
    index = 427,
    label = "nC4H3 + C2H2 <=> l-C6H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+14, 'cm^3/(mol*s)'),
        n = -0.56,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= 0.5*C2H3+OH\nnC4H3 + C2H2 = l-C6H4 + H                    1.40E+15   -0.81  10000.      !   10 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = l-C6H4 + H                    3.70E+16   -1.21  11100.      !   20 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = l-C6H4 + H                    1.80E+19   -1.95  13200.      !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
= 0.5*C2H3+OH
nC4H3 + C2H2 = l-C6H4 + H                    1.40E+15   -0.81  10000.      !   10 Torr RRKM WAN/FRE
nC4H3 + C2H2 = l-C6H4 + H                    3.70E+16   -1.21  11100.      !   20 Torr RRKM WAN/FRE
nC4H3 + C2H2 = l-C6H4 + H                    1.80E+19   -1.95  13200.      !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 428,
    label = "nC4H3 + C2H2 <=> C6H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+70, 'cm^3/(mol*s)'),
        n = -17.77,
        Ea = (31300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = l-C6H4 + H                    1.20E+17   -1.28  13700.      ! 7600 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = C6H5                          1.40E+67  -17.42  23000.      !   10 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = C6H5                          2.30E+68  -17.65  24400.      !   20 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = C6H5                          9.80E+68  -17.58  26500.      !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
nC4H3 + C2H2 = l-C6H4 + H                    1.20E+17   -1.28  13700.      ! 7600 Torr RRKM WAN/FRE
nC4H3 + C2H2 = C6H5                          1.40E+67  -17.42  23000.      !   10 Torr RRKM WAN/FRE
nC4H3 + C2H2 = C6H5                          2.30E+68  -17.65  24400.      !   20 Torr RRKM WAN/FRE
nC4H3 + C2H2 = C6H5                          9.80E+68  -17.58  26500.      !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 429,
    label = "nC4H3 + C2H2 <=> o-C6H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+46, 'cm^3/(mol*s)'),
        n = -10.01,
        Ea = (30100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = C6H5                          1.90E+63  -15.25  30600.      ! 7600 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = o-C6H4 + H                    9.20E+33   -6.57  15900.      !   10 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = o-C6H4 + H                    1.90E+36   -7.21  17900.      !   20 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = o-C6H4 + H                    3.50E+41   -8.63  23000.      !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
nC4H3 + C2H2 = C6H5                          1.90E+63  -15.25  30600.      ! 7600 Torr RRKM WAN/FRE
nC4H3 + C2H2 = o-C6H4 + H                    9.20E+33   -6.57  15900.      !   10 Torr RRKM WAN/FRE
nC4H3 + C2H2 = o-C6H4 + H                    1.90E+36   -7.21  17900.      !   20 Torr RRKM WAN/FRE
nC4H3 + C2H2 = o-C6H4 + H                    3.50E+41   -8.63  23000.      !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 430,
    label = "iC4H3 + H <=> C2H2 + H2CC",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+23, 'cm^3/(mol*s)'),
        n = -2.55,
        Ea = (10780, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nnC4H3 + C2H2 = o-C6H4 + H                    3.10E+49  -10.59  37700.      ! 7600 Torr RRKM WAN/FRE\nReactions of iC4H3\niC4H3 + H = C2H2 + H2CC                      2.40E+19   -1.60   2800.0     !   20 Torr RRKM WAN/FRE\niC4H3 + H = C2H2 + H2CC                      3.70E+22   -2.50   5140.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
nC4H3 + C2H2 = o-C6H4 + H                    3.10E+49  -10.59  37700.      ! 7600 Torr RRKM WAN/FRE
Reactions of iC4H3
iC4H3 + H = C2H2 + H2CC                      2.40E+19   -1.60   2800.0     !   20 Torr RRKM WAN/FRE
iC4H3 + H = C2H2 + H2CC                      3.70E+22   -2.50   5140.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 431,
    label = "iC4H3 + H <=> C4H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+43, 'cm^3/(mol*s)'),
        n = -9.01,
        Ea = (12120, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\niC4H3 + H = C4H4                             4.20E+44  -10.27   7890.0     !   20 Torr RRKM WAN/FRE\niC4H3 + H = C4H4                             5.30E+46  -10.68   9270.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
iC4H3 + H = C4H4                             4.20E+44  -10.27   7890.0     !   20 Torr RRKM WAN/FRE
iC4H3 + H = C4H4                             5.30E+46  -10.68   9270.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 432,
    label = "iC4H3 + H <=> C4H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
""",
)

entry(
    index = 433,
    label = "iC4H3 + OH <=> C4H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H3+H',
    ),
    longDesc = 
u"""
= C2H3+H
""",
)

entry(
    index = 434,
    label = "iC4H3 + O2 <=> HCCO + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.86e+16, 'cm^3/(mol*s)'),
        n = -1.8,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H3+OH',
    ),
    longDesc = 
u"""
= C2H3+OH
""",
)

entry(
    index = 435,
    label = "C4H4 + H <=> nC4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+51, 'cm^3/(mol*s)'),
        n = -11.92,
        Ea = (16500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '89SLA/BER\nReactions of C4H4\nC4H4 + H = nC4H5                             1.20E+51  -12.57    12300.    !   10 Torr RRKM WAN/FRE\nC4H4 + H = nC4H5                             4.20E+50  -12.34    12500.    !   20 Torr RRKM WAN/FRE\nC4H4 + H = nC4H5                             1.10E+50  -11.94    13400.    !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
89SLA/BER
Reactions of C4H4
C4H4 + H = nC4H5                             1.20E+51  -12.57    12300.    !   10 Torr RRKM WAN/FRE
C4H4 + H = nC4H5                             4.20E+50  -12.34    12500.    !   20 Torr RRKM WAN/FRE
C4H4 + H = nC4H5                             1.10E+50  -11.94    13400.    !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 436,
    label = "C4H4 + H <=> iC4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+51, 'cm^3/(mol*s)'),
        n = -11.92,
        Ea = (17700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nC4H4 + H = nC4H5                             6.20E+45  -10.08    15800.    ! 7600 Torr RRKM WAN/FRE\nC4H4 + H = iC4H5                             6.10E+53  -13.19    14200.    !   10 Torr RRKM WAN/FRE\nC4H4 + H = iC4H5                             9.60E+52  -12.85    14300.    !   20 Torr RRKM WAN/FRE\nC4H4 + H = iC4H5                             2.10E+52  -12.44    15500.    !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
C4H4 + H = nC4H5                             6.20E+45  -10.08    15800.    ! 7600 Torr RRKM WAN/FRE
C4H4 + H = iC4H5                             6.10E+53  -13.19    14200.    !   10 Torr RRKM WAN/FRE
C4H4 + H = iC4H5                             9.60E+52  -12.85    14300.    !   20 Torr RRKM WAN/FRE
C4H4 + H = iC4H5                             2.10E+52  -12.44    15500.    !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 437,
    label = "C4H4 + H <=> nC4H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665000, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nC4H4 + H = iC4H5                             1.50E+48  -10.58    18800.    ! 7600 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
C4H4 + H = iC4H5                             1.50E+48  -10.58    18800.    ! 7600 Torr RRKM WAN/FRE
""",
)

entry(
    index = 438,
    label = "C4H4 + H <=> iC4H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (333000, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (9240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 439,
    label = "C4H4 + OH <=> nC4H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 440,
    label = "C4H4 + OH <=> iC4H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 441,
    label = "C4H4 + O <=> C3H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 442,
    label = "C4H4 + C2H <=> l-C6H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C4H6+O',
    ),
    longDesc = 
u"""
= C4H6+O
""",
)

entry(
    index = 443,
    label = "nC4H5 <=> iC4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+67, 's^-1'),
        n = -16.89,
        Ea = (59100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H+C2H4\nReactions of nC4H5\nnC4H5 = iC4H5                                2.40E+60 -16.08     47500.    !   10 Torr RRKM WAN/FRE\nnC4H5 = iC4H5                                1.30E+62 -16.38     49600.    !   20 Torr RRKM WAN/FRE\nnC4H5 = iC4H5                                4.90E+66 -17.26     55400.    !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
= C2H+C2H4
Reactions of nC4H5
nC4H5 = iC4H5                                2.40E+60 -16.08     47500.    !   10 Torr RRKM WAN/FRE
nC4H5 = iC4H5                                1.30E+62 -16.38     49600.    !   20 Torr RRKM WAN/FRE
nC4H5 = iC4H5                                4.90E+66 -17.26     55400.    !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 444,
    label = "nC4H5 + H <=> iC4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+26, 'cm^3/(mol*s)'),
        n = -3.35,
        Ea = (17423, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nnC4H5 = iC4H5                                2.00E+60 -14.46     58600.    ! 7600 Torr RRKM WAN/FRE\nnC4H5 + H = iC4H5 + H                        1.00E+36  -6.26     17486.    ! RRKM 20 Torr  WAN/FRE\nnC4H5 + H = iC4H5 + H                        1.00E+34  -5.61     18476.    ! RRKM 90 Torr  WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
nC4H5 = iC4H5                                2.00E+60 -14.46     58600.    ! 7600 Torr RRKM WAN/FRE
nC4H5 + H = iC4H5 + H                        1.00E+36  -6.26     17486.    ! RRKM 20 Torr  WAN/FRE
nC4H5 + H = iC4H5 + H                        1.00E+34  -5.61     18476.    ! RRKM 90 Torr  WAN/FRE
""",
)

entry(
    index = 445,
    label = "nC4H5 + H <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM 760 Torr WAN/FRE',
    ),
    longDesc = 
u"""
RRKM 760 Torr WAN/FRE
""",
)

entry(
    index = 446,
    label = "nC4H5 + OH <=> C4H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 447,
    label = "nC4H5 + HCO <=> C4H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 448,
    label = "nC4H5 + HO2 <=> C2H3 + CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 449,
    label = "nC4H5 + H2O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 450,
    label = "nC4H5 + HO2 <=> C4H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 451,
    label = "nC4H5 + O2 <=> CH2CHCHCHO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (11, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 452,
    label = "nC4H5 + O2 <=> HCO + C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.2e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1010, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H3+O2=>CH2CHO+O',
    ),
    longDesc = 
u"""
= C2H3+O2=>CH2CHO+O
""",
)

entry(
    index = 453,
    label = "nC4H5 + C2H2 <=> C6H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+16, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (5400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H3+O2=>HCO+CH2O\nnC4H5 + C2H2 = C6H6 + H                      2.10E+15     -1.07    4800.  !   10 Torr RRKM WAN/FRE\nnC4H5 + C2H2 = C6H6 + H                      2.10E+15     -1.07    4800.  !   20 Torr RRKM WAN/FRE\nnC4H5 + C2H2 = C6H6 + H                      2.10E+15     -1.07    4800.  !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
= C2H3+O2=>HCO+CH2O
nC4H5 + C2H2 = C6H6 + H                      2.10E+15     -1.07    4800.  !   10 Torr RRKM WAN/FRE
nC4H5 + C2H2 = C6H6 + H                      2.10E+15     -1.07    4800.  !   20 Torr RRKM WAN/FRE
nC4H5 + C2H2 = C6H6 + H                      2.10E+15     -1.07    4800.  !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 454,
    label = "nC4H5 + C2H3 <=> C6H6 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e-13, 'cm^3/(mol*s)'),
        n = 7.07,
        Ea = (-3611, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM WAN/FRE\nnC4H5 + C2H2 = C6H6 + H                      1.60E+18     -1.88    7400.  ! 7600 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM WAN/FRE
nC4H5 + C2H2 = C6H6 + H                      1.60E+18     -1.88    7400.  ! 7600 Torr RRKM WAN/FRE
""",
)

entry(
    index = 455,
    label = "iC4H5 + H <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '89WES/DEA\nnC4H5+C4H4 =C6H5C2H3+H                       3.16E+11   0.0        600.    !84COL/BIT\nReactions of iC4H5',
    ),
    longDesc = 
u"""
89WES/DEA
nC4H5+C4H4 =C6H5C2H3+H                       3.16E+11   0.0        600.    !84COL/BIT
Reactions of iC4H5
""",
)

entry(
    index = 456,
    label = "iC4H5 + H <=> C3H3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 457,
    label = "iC4H5 + OH <=> C4H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 458,
    label = "iC4H5 + HCO <=> C4H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 459,
    label = "iC4H5 + HO2 <=> C4H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 460,
    label = "iC4H5 + HO2 <=> C2H3 + CH2CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 461,
    label = "iC4H5 + H2O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 462,
    label = "iC4H5 + O2 <=> CH2CO + CH2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 463,
    label = "C4H5-2 <=> iC4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+67, 's^-1'),
        n = -16.89,
        Ea = (59100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C4H5-2+O2\niC4H5+C4H4 =C6H5C2H3+H                       5.000E+14  0.0      25000.    !Estimated\nReactions of C4H5-2',
    ),
    longDesc = 
u"""
= C4H5-2+O2
iC4H5+C4H4 =C6H5C2H3+H                       5.000E+14  0.0      25000.    !Estimated
Reactions of C4H5-2
""",
)

entry(
    index = 464,
    label = "iC4H5 + H <=> C4H5-2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+26, 'cm^3/(mol*s)'),
        n = -3.35,
        Ea = (17423, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC4H5=>iC4H5',
    ),
    longDesc = 
u"""
= nC4H5=>iC4H5
""",
)

entry(
    index = 465,
    label = "C4H5-2 + HO2 <=> OH + C2H2 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC4H5+H=>iC4H5+H',
    ),
    longDesc = 
u"""
= nC4H5+H=>iC4H5+H
""",
)

entry(
    index = 466,
    label = "C4H5-2 + O2 <=> CH3CO + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 467,
    label = "C4H5-2 + C2H2 <=> C6H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (25000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92SLA/BEN',
    ),
    longDesc = 
u"""
92SLA/BEN
""",
)

entry(
    index = 468,
    label = "C4H5-2 + C2H4 <=> C5H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (25000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 469,
    label = "C4H6 <=> iC4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+36, 's^-1'),
        n = -6.27,
        Ea = (112353, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated\nReactions of 1,3-C4H6\nC4H6 = iC4H5 + H                             8.20E+51 -10.92    118409.    ! RRKM 20 Torr  WAN/FRE\nC4H6 = iC4H5 + H                             3.30E+45  -8.95    115934.    ! RRKM 90 Torr  WAN/FRE',
    ),
    longDesc = 
u"""
Estimated
Reactions of 1,3-C4H6
C4H6 = iC4H5 + H                             8.20E+51 -10.92    118409.    ! RRKM 20 Torr  WAN/FRE
C4H6 = iC4H5 + H                             3.30E+45  -8.95    115934.    ! RRKM 90 Torr  WAN/FRE
""",
)

entry(
    index = 470,
    label = "C4H6 <=> nC4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+44, 's^-1'),
        n = -8.62,
        Ea = (123608, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM 760 Torr WAN/FRE\nC4H6 = nC4H5 + H                             3.50E+61 -13.87    129677.    ! RRKM 20 Torr  WAN/FRE\nC4H6 = nC4H5 + H                             8.50E+54 -11.78    127472.    ! RRKM 90 Torr  WAN/FRE',
    ),
    longDesc = 
u"""
RRKM 760 Torr WAN/FRE
C4H6 = nC4H5 + H                             3.50E+61 -13.87    129677.    ! RRKM 20 Torr  WAN/FRE
C4H6 = nC4H5 + H                             8.50E+54 -11.78    127472.    ! RRKM 90 Torr  WAN/FRE
""",
)

entry(
    index = 471,
    label = "C4H6 <=> C4H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+15, 's^-1'),
        n = 0,
        Ea = (94700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM 760 Torr WAN/FRE',
    ),
    longDesc = 
u"""
RRKM 760 Torr WAN/FRE
""",
)

entry(
    index = 472,
    label = "C4H6 + H <=> nC4H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 473,
    label = "C4H6 + H <=> iC4H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665000, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (9240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2H4+H',
    ),
    longDesc = 
u"""
= C2H4+H
""",
)

entry(
    index = 474,
    label = "C4H6 + H <=> C2H4 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.46e+30, 'cm^3/(mol*s)'),
        n = -4.34,
        Ea = (21647, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated\nC2H4 + C2H3 = C4H6 + H                       7.40E+14  -0.66    8420.0     !   20 Torr RRKM WAN/FRE\nC2H4 + C2H3 = C4H6 + H                       1.90E+17  -1.32   10600.0     !   90 Torr RRKM WAN/FRE',
    ),
    longDesc = 
u"""
Estimated
C2H4 + C2H3 = C4H6 + H                       7.40E+14  -0.66    8420.0     !   20 Torr RRKM WAN/FRE
C2H4 + C2H3 = C4H6 + H                       1.90E+17  -1.32   10600.0     !   90 Torr RRKM WAN/FRE
""",
)

entry(
    index = 475,
    label = "C4H6 + H <=> pC3H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE 1 atm\nC4H6+H = C2H4+C2H3                           5.45E+30  -4.51     21877.    !97WAN/FRE 10 atm',
    ),
    longDesc = 
u"""
97WAN/FRE 1 atm
C4H6+H = C2H4+C2H3                           5.45E+30  -4.51     21877.    !97WAN/FRE 10 atm
""",
)

entry(
    index = 476,
    label = "C4H6 + H <=> aC3H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 477,
    label = "C4H6 + O <=> nC4H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (3740, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 478,
    label = "C4H6 + O <=> iC4H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (3740, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2h4+O',
    ),
    longDesc = 
u"""
= C2h4+O
""",
)

entry(
    index = 479,
    label = "C4H6 + O <=> CH3CHCHCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C2h4+O',
    ),
    longDesc = 
u"""
= C2h4+O
""",
)

entry(
    index = 480,
    label = "C4H6 + O <=> CH2CHCHCHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '93ADU/FON#',
    ),
    longDesc = 
u"""
93ADU/FON#
""",
)

entry(
    index = 481,
    label = "C4H6 + OH <=> nC4H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '93ADU/FON#',
    ),
    longDesc = 
u"""
93ADU/FON#
""",
)

entry(
    index = 482,
    label = "C4H6 + OH <=> iC4H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88LIU/MUL',
    ),
    longDesc = 
u"""
88LIU/MUL
""",
)

entry(
    index = 483,
    label = "C4H6 + HO2 <=> C4H6O25 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 484,
    label = "C4H6 + HO2 <=> C2H3CHOCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 485,
    label = "C4H6 + CH3 <=> nC4H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 486,
    label = "C4H6 + CH3 <=> iC4H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 487,
    label = "C4H6 + C2H3 <=> nC4H5 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 488,
    label = "C4H6 + C2H3 <=> iC4H5 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 489,
    label = "C4H6 + C3H3 <=> nC4H5 + aC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 490,
    label = "C4H6 + C3H3 <=> iC4H5 + aC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 491,
    label = "C4H6 + aC3H5 <=> nC4H5 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 492,
    label = "C4H6 + aC3H5 <=> iC4H5 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 493,
    label = "C4H6 + C2H3 <=> C6H6 + H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.62e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 494,
    label = "C4H612 <=> iC4H5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+15, 's^-1'),
        n = 0,
        Ea = (92600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '95LEU/LIN\nReactions of 1,2-C4H6',
    ),
    longDesc = 
u"""
95LEU/LIN
Reactions of 1,2-C4H6
""",
)

entry(
    index = 495,
    label = "C4H612 + H <=> C4H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '95LEU/LIN',
    ),
    longDesc = 
u"""
95LEU/LIN
""",
)

entry(
    index = 496,
    label = "C4H612 + H <=> iC4H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 497,
    label = "C4H612 + H <=> aC3H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+H',
    ),
    longDesc = 
u"""
= C3H6+H
""",
)

entry(
    index = 498,
    label = "C4H612 + H <=> pC3H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 499,
    label = "C4H612 + CH3 <=> iC4H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 500,
    label = "C4H612 + O <=> CH2CO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (327, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88KER/SIN',
    ),
    longDesc = 
u"""
88KER/SIN
""",
)

entry(
    index = 501,
    label = "C4H612 + O <=> iC4H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5880, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+O',
    ),
    longDesc = 
u"""
= C3H6+O
""",
)

entry(
    index = 502,
    label = "C4H612 + OH <=> iC4H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-298, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+O',
    ),
    longDesc = 
u"""
= C3H6+O
""",
)

entry(
    index = 503,
    label = "C4H612 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 's^-1'),
        n = 0,
        Ea = (65000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+OH',
    ),
    longDesc = 
u"""
= C3H6+OH
""",
)

entry(
    index = 504,
    label = "C4H6-2 <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 's^-1'),
        n = 0,
        Ea = (65000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG\nReactions of C4H6-2',
    ),
    longDesc = 
u"""
96HID/HIG
Reactions of C4H6-2
""",
)

entry(
    index = 505,
    label = "C4H6-2 <=> C4H612",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 's^-1'),
        n = 0,
        Ea = (67000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 506,
    label = "C4H6-2 + H <=> C4H612 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 507,
    label = "C4H6-2 + H <=> C4H5-2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (340000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 508,
    label = "C4H6-2 + H <=> CH3 + pC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (260000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+H',
    ),
    longDesc = 
u"""
= C3H6+H
""",
)

entry(
    index = 509,
    label = "C4H6-2 <=> H + C4H5-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+15, 's^-1'),
        n = 0,
        Ea = (87300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 510,
    label = "C4H6-2 + CH3 <=> C4H5-2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '96HID/HIG',
    ),
    longDesc = 
u"""
96HID/HIG
""",
)

entry(
    index = 511,
    label = "C2H3CHOCH2 <=> C4H6O23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14, 's^-1'),
        n = 0,
        Ea = (50600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated\nReactions of C4H6O isomers',
    ),
    longDesc = 
u"""
Estimated
Reactions of C4H6O isomers
""",
)

entry(
    index = 512,
    label = "C4H6O23 <=> CH3CHCHCHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.95e+13, 's^-1'),
        n = 0,
        Ea = (49400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '76CRA/LUT',
    ),
    longDesc = 
u"""
76CRA/LUT
""",
)

entry(
    index = 513,
    label = "C4H6O23 <=> C2H4 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.75e+15, 's^-1'),
        n = 0,
        Ea = (69300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '89LIF/BID',
    ),
    longDesc = 
u"""
89LIF/BID
""",
)

entry(
    index = 514,
    label = "C4H6O23 <=> C2H2 + CH2OCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (75800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '89LIF/BID',
    ),
    longDesc = 
u"""
89LIF/BID
""",
)

entry(
    index = 515,
    label = "C4H6O25 <=> C4H4O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+12, 's^-1'),
        n = 0,
        Ea = (48500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '89LIF/BID',
    ),
    longDesc = 
u"""
89LIF/BID
""",
)

entry(
    index = 516,
    label = "C4H4O <=> CO + pC3H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.78e+15, 's^-1'),
        n = 0,
        Ea = (77500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86LIF/BID1\nReactions of C4H4O',
    ),
    longDesc = 
u"""
86LIF/BID1
Reactions of C4H4O
""",
)

entry(
    index = 517,
    label = "C4H4O <=> C2H2 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+14, 's^-1'),
        n = 0,
        Ea = (77500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86LIF/BID2',
    ),
    longDesc = 
u"""
86LIF/BID2
""",
)

entry(
    index = 518,
    label = "CH3CHCHCHO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+14, 's^-1'),
        n = 0,
        Ea = (69000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86LIF/BID2\nReactions of CH3CHCHCHO',
    ),
    longDesc = 
u"""
86LIF/BID2
Reactions of CH3CHCHCHO
""",
)

entry(
    index = 519,
    label = "CH3CHCHCHO + H <=> CH2CHCHCHO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= HCCCHO=>C2H2+CO',
    ),
    longDesc = 
u"""
= HCCCHO=>C2H2+CO
""",
)

entry(
    index = 520,
    label = "CH3CHCHCHO + H <=> CH3CHCHCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+H=>aC3H5+H2',
    ),
    longDesc = 
u"""
= C3H6+H=>aC3H5+H2
""",
)

entry(
    index = 521,
    label = "CH3CHCHCHO + H <=> CH3 + C2H3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 522,
    label = "CH3CHCHCHO + H <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+H=>C2H4+CH3',
    ),
    longDesc = 
u"""
= C3H6+H=>C2H4+CH3
""",
)

entry(
    index = 523,
    label = "CH3CHCHCHO + CH3 <=> CH2CHCHCHO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (5675, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+H=>C2H4+CH3',
    ),
    longDesc = 
u"""
= C3H6+H=>C2H4+CH3
""",
)

entry(
    index = 524,
    label = "CH3CHCHCHO + CH3 <=> CH3CHCHCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (5675, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+CH3=>aC3H5+CH4',
    ),
    longDesc = 
u"""
= C3H6+CH3=>aC3H5+CH4
""",
)

entry(
    index = 525,
    label = "CH3CHCHCHO + C2H3 <=> CH2CHCHCHO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.21, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (4682, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 526,
    label = "CH3CHCHCHO + C2H3 <=> CH3CHCHCO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.11, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (4682, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=C3H6+C2H3=>aC3H5+C2H4',
    ),
    longDesc = 
u"""
=C3H6+C2H3=>aC3H5+C2H4
""",
)

entry(
    index = 527,
    label = "CH3CHCHCO <=> CH3CHCH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (30000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated\nReactions of CH3CHCHCO',
    ),
    longDesc = 
u"""
Estimated
Reactions of CH3CHCHCO
""",
)

entry(
    index = 528,
    label = "CH3CHCHCO + H <=> CH3CHCHCHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 529,
    label = "CH2CHCHCHO <=> aC3H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 's^-1'),
        n = 0,
        Ea = (25000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated\nReactions of CH2CHCHCHO',
    ),
    longDesc = 
u"""
Estimated
Reactions of CH2CHCHCHO
""",
)

entry(
    index = 530,
    label = "CH2CHCHCHO + H <=> CH3CHCHCHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 531,
    label = "C4H7 <=> C4H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.48e+53, 's^-1'),
        n = -12.3,
        Ea = (52000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated\nReactions of C4H7',
    ),
    longDesc = 
u"""
Estimated
Reactions of C4H7
""",
)

entry(
    index = 532,
    label = "C4H7 + H <=> C4H81",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '97WAN/FRE\nC4H7 = C4H6+H                                1.85E+48 -10.50     51770.0   !97WAN/FRE 10 atm',
    ),
    longDesc = 
u"""
97WAN/FRE
C4H7 = C4H6+H                                1.85E+48 -10.50     51770.0   !97WAN/FRE 10 atm
""",
)

entry(
    index = 533,
    label = "C4H7 + H <=> CH3 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+H',
    ),
    longDesc = 
u"""
= nC3H7+H
""",
)

entry(
    index = 534,
    label = "C4H7 + H <=> C4H6 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 535,
    label = "C4H7 + O2 <=> C4H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+H',
    ),
    longDesc = 
u"""
= nC3H7+H
""",
)

entry(
    index = 536,
    label = "C4H7 + HO2 <=> CH2O + OH + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 537,
    label = "C4H7 + HCO <=> C4H81 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HO2',
    ),
    longDesc = 
u"""
= nC3H7+HO2
""",
)

entry(
    index = 538,
    label = "C4H7 + CH3 <=> C4H6 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HCO',
    ),
    longDesc = 
u"""
= nC3H7+HCO
""",
)

entry(
    index = 539,
    label = "iC4H7 + H <=> iC4H8",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.33e+60, 'cm^6/(mol^2*s)'),
            n = -12,
            Ea = (5967.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.02,
        T3 = (1096.6, 'K'),
        T1 = (1096.6, 'K'),
        T2 = (6859.5, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '= nC3H7+CH3\nReaction of iC4H7 2-methylpropen-3-yl',
    ),
    longDesc = 
u"""
= nC3H7+CH3
Reaction of iC4H7 2-methylpropen-3-yl
""",
)

entry(
    index = 540,
    label = "iC4H7 + H <=> CH3CCH2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+45, 'cm^3/(mol*s)'),
        n = -8.19,
        Ea = (37890, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(aC3H5+H) TS5 600cm-1\niC4H7+H = CH3CCH2+CH3                        2.20E+51  -9.98     37730.0   ! =(aC3H5+H) TS5 0.1 atm',
    ),
    longDesc = 
u"""
=(aC3H5+H) TS5 600cm-1
iC4H7+H = CH3CCH2+CH3                        2.20E+51  -9.98     37730.0   ! =(aC3H5+H) TS5 0.1 atm
""",
)

entry(
    index = 541,
    label = "iC4H7 + O <=> CH2O + CH3CCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(aC3H5+H) TS5 1 atm\niC4H7+H = CH3CCH2+CH3                        3.40E+32  -4.46     33760.0   ! =(aC3H5+H) TS5 10 atm',
    ),
    longDesc = 
u"""
=(aC3H5+H) TS5 1 atm
iC4H7+H = CH3CCH2+CH3                        3.40E+32  -4.46     33760.0   ! =(aC3H5+H) TS5 10 atm
""",
)

entry(
    index = 542,
    label = "iC4H7 + HO2 <=> CH3CCH2 + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 543,
    label = "C4H81 + H <=> pC4H9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.33e+13, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (3260.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.26e+38, 'cm^6/(mol^2*s)'),
            n = -6.66,
            Ea = (7000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (1310, 'K'),
        T2 = (48097, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'Estimated\nReactions of 1-butene',
    ),
    longDesc = 
u"""
Estimated
Reactions of 1-butene
""",
)

entry(
    index = 544,
    label = "C4H81 + H <=> sC4H9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.33e+13, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (1559.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (8.7e+42, 'cm^6/(mol^2*s)'),
            n = -7.5,
            Ea = (4721.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (645.4, 'K'),
        T2 = (6844.3, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H6+H) TS5 600 cm-1',
    ),
    longDesc = 
u"""
=(C3H6+H) TS5 600 cm-1
""",
)

entry(
    index = 545,
    label = "C4H81 + H <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H) TS5 600 cm-1',
    ),
    longDesc = 
u"""
=(C3H6+H) TS5 600 cm-1
""",
)

entry(
    index = 546,
    label = "C4H81 + H <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C3H6+H',
    ),
    longDesc = 
u"""
= C3H6+H
""",
)

entry(
    index = 547,
    label = "C4H81 + H <=> C4H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (650000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 548,
    label = "C4H81 + O <=> nC3H7 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= (C3H8+H)/2',
    ),
    longDesc = 
u"""
= (C3H8+H)/2
""",
)

entry(
    index = 549,
    label = "C4H81 + O <=> C4H7 + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5760, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '91KO/ADU',
            ),
            Arrhenius(
                A = (2.6e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4470, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '91KO/ADU',
            ),
        ],
    ),
)

entry(
    index = 550,
    label = "C4H81 + OH <=> C4H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91KO/ADU',
    ),
    longDesc = 
u"""
91KO/ADU
""",
)

entry(
    index = 551,
    label = "C4H81 + O2 <=> C4H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+OH)',
    ),
    longDesc = 
u"""
=(C3H8+OH)
""",
)

entry(
    index = 552,
    label = "C4H81 + HO2 <=> C4H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 553,
    label = "C4H81 + CH3 <=> C4H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.45, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '89WAL',
    ),
    longDesc = 
u"""
89WAL
""",
)

entry(
    index = 554,
    label = "C4H82 + H <=> sC4H9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.33e+13, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (1559.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (8.7e+42, 'cm^6/(mol^2*s)'),
            n = -7.5,
            Ea = (4721.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (645.4, 'K'),
        T2 = (6844.3, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)\nReactions of 2-butene',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
Reactions of 2-butene
""",
)

entry(
    index = 555,
    label = "C4H82 + H <=> C4H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (340000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H=iC3H7) TS5 600cm-1',
    ),
    longDesc = 
u"""
=(C3H6+H=iC3H7) TS5 600cm-1
""",
)

entry(
    index = 556,
    label = "C4H82 + O <=> C2H4 + CH3CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (327, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)*2 TS5 k(a)',
    ),
    longDesc = 
u"""
=(C3H6+H)*2 TS5 k(a)
""",
)

entry(
    index = 557,
    label = "C4H82 + OH <=> C4H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-298, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+O)*2 TS5 k(a+b)',
    ),
    longDesc = 
u"""
=(C3H6+O)*2 TS5 k(a+b)
""",
)

entry(
    index = 558,
    label = "C4H82 + O2 <=> C4H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (53300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+OH)*2 TS5',
    ),
    longDesc = 
u"""
=(C3H6+OH)*2 TS5
""",
)

entry(
    index = 559,
    label = "C4H82 + HO2 <=> C4H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 560,
    label = "C4H82 + CH3 <=> C4H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (5675, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+HO2)*2 TS5',
    ),
    longDesc = 
u"""
=(C3H6+HO2)*2 TS5
""",
)

entry(
    index = 561,
    label = "iC4H8 + H <=> iC4H9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.33e+13, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (3260.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.26e+38, 'cm^6/(mol^2*s)'),
            n = -6.66,
            Ea = (7000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (1310, 'K'),
        T2 = (48097, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H6+CH3)*2 TS5 k(c)\nReactions of i-butene',
    ),
    longDesc = 
u"""
=(C3H6+CH3)*2 TS5 k(c)
Reactions of i-butene
""",
)

entry(
    index = 562,
    label = "iC4H8 + H <=> iC4H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6760, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H=nC3H7) TS5 600 cm-1',
    ),
    longDesc = 
u"""
=(C3H6+H=nC3H7) TS5 600 cm-1
""",
)

entry(
    index = 563,
    label = "iC4H8 + H <=> C3H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC4H10+H)*2/3 TS4\niC4H8+H = C3H6+CH3                           8.80E+16  -1.05      6461.0   ! =(iC4H8+H) TS5 0.1 atm',
    ),
    longDesc = 
u"""
=(iC4H10+H)*2/3 TS4
iC4H8+H = C3H6+CH3                           8.80E+16  -1.05      6461.0   ! =(iC4H8+H) TS5 0.1 atm
""",
)

entry(
    index = 564,
    label = "iC4H8 + O <=> CH3 + CH3 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (327, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC4H8+H) TS5 1 atm\niC4H8+H = C3H6+CH3                           3.30E+24  -3.04     15610.0   ! =(iC4H8+H) TS5 10 atm',
    ),
    longDesc = 
u"""
=(iC4H8+H) TS5 1 atm
iC4H8+H = C3H6+CH3                           3.30E+24  -3.04     15610.0   ! =(iC4H8+H) TS5 10 atm
""",
)

entry(
    index = 565,
    label = "iC4H8 + O <=> iC3H7 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+07, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (-972, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+O) TS5',
    ),
    longDesc = 
u"""
=(C3H6+O) TS5
""",
)

entry(
    index = 566,
    label = "iC4H8 + O <=> iC4H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (290000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (3640, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+O) TS5 k(c)',
    ),
    longDesc = 
u"""
=(C3H6+O) TS5 k(c)
""",
)

entry(
    index = 567,
    label = "iC4H8 + OH <=> iC4H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.53,
        Ea = (775, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC4H10+O)*2/3 TS4',
    ),
    longDesc = 
u"""
=(iC4H10+O)*2/3 TS4
""",
)

entry(
    index = 568,
    label = "iC4H8 + HO2 <=> iC4H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (15500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC4H10+OH)*2/3 TS4',
    ),
    longDesc = 
u"""
=(iC4H10+OH)*2/3 TS4
""",
)

entry(
    index = 569,
    label = "iC4H8 + O2 <=> iC4H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC4H10+HO2)*2/3 TS4',
    ),
    longDesc = 
u"""
=(iC4H10+HO2)*2/3 TS4
""",
)

entry(
    index = 570,
    label = "iC4H8 + CH3 <=> iC4H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.91, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7150, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC4H10+O2)*2/3 TS4',
    ),
    longDesc = 
u"""
=(iC4H10+O2)*2/3 TS4
""",
)

entry(
    index = 571,
    label = "C2H4 + C2H5 <=> pC4H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC4H10+CH3)*2/3 TS4\nReactions of 1-butyl',
    ),
    longDesc = 
u"""
=(iC4H10+CH3)*2/3 TS4
Reactions of 1-butyl
""",
)

entry(
    index = 572,
    label = "pC4H9 + H <=> C4H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'KP, P',
    ),
    longDesc = 
u"""
KP, P
""",
)

entry(
    index = 573,
    label = "pC4H9 + H <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12505, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H) TS3 600 cm-1\npC4H9+H = C2H5+C2H5                          3.40E+18  -1.33       5386.0  ! =(nC3H7+H) TS3 0.1 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H) TS3 600 cm-1
pC4H9+H = C2H5+C2H5                          3.40E+18  -1.33       5386.0  ! =(nC3H7+H) TS3 0.1 atm
""",
)

entry(
    index = 574,
    label = "pC4H9 + H <=> C4H81 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H) TS3 1 atm\npC4H9+H = C2H5+C2H5                          3.10E+27  -3.59      19059.0  ! =(nC3H7+H) TS3 10 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H) TS3 1 atm
pC4H9+H = C2H5+C2H5                          3.10E+27  -3.59      19059.0  ! =(nC3H7+H) TS3 10 atm
""",
)

entry(
    index = 575,
    label = "pC4H9 + O <=> nC3H7 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H) TS4',
    ),
    longDesc = 
u"""
=(nC3H7+H) TS4
""",
)

entry(
    index = 576,
    label = "pC4H9 + OH <=> C4H81 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O) TS3 ka+kb',
    ),
    longDesc = 
u"""
=(nC3H7+O) TS3 ka+kb
""",
)

entry(
    index = 577,
    label = "pC4H9 + O2 <=> C4H81 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+OH) TS3',
    ),
    longDesc = 
u"""
=(nC3H7+OH) TS3
""",
)

entry(
    index = 578,
    label = "pC4H9 + HO2 <=> nC3H7 + OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BB75',
    ),
    longDesc = 
u"""
BB75
""",
)

entry(
    index = 579,
    label = "pC4H9 + HCO <=> C4H10 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HO2) TS3 ?',
    ),
    longDesc = 
u"""
=(nC3H7+HO2) TS3 ?
""",
)

entry(
    index = 580,
    label = "pC4H9 + CH3 <=> C4H81 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HCO) TS3',
    ),
    longDesc = 
u"""
=(nC3H7+HCO) TS3
""",
)

entry(
    index = 581,
    label = "C3H6 + CH3 <=> sC4H9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(7403.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.31e+28, 'cm^6/(mol^2*s)'),
            n = -4.27,
            Ea = (1831, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.565,
        T3 = (60000, 'K'),
        T1 = (534.2, 'K'),
        T2 = (3007.2, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(nC3H7+CH3) TS3\nReactions of 2-butyl',
    ),
    longDesc = 
u"""
=(nC3H7+CH3) TS3
Reactions of 2-butyl
""",
)

entry(
    index = 582,
    label = "sC4H9 + H <=> C4H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+58, 'cm^6/(mol^2*s)'),
            n = -12.08,
            Ea = (11263.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.649,
        T3 = (1213.1, 'K'),
        T1 = (1213.1, 'K'),
        T2 = (13369.7, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'TS5 600cm-1',
    ),
    longDesc = 
u"""
TS5 600cm-1
""",
)

entry(
    index = 583,
    label = "sC4H9 + H <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H) TS3 600 cm-1\nsC4H9+H = C2H5+C2H5                          5.90E+23  -2.81     10009.0   ! =(iC3H7+H) TS3 0.1 atm',
    ),
    longDesc = 
u"""
=(iC3H7+H) TS3 600 cm-1
sC4H9+H = C2H5+C2H5                          5.90E+23  -2.81     10009.0   ! =(iC3H7+H) TS3 0.1 atm
""",
)

entry(
    index = 584,
    label = "sC4H9 + H <=> C4H81 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H) TS3 1 atm\nsC4H9+H = C2H5+C2H5                          4.00E+24  -2.83     17542.0   ! =(iC3H7+H) TS3 10 atm',
    ),
    longDesc = 
u"""
=(iC3H7+H) TS3 1 atm
sC4H9+H = C2H5+C2H5                          4.00E+24  -2.83     17542.0   ! =(iC3H7+H) TS3 10 atm
""",
)

entry(
    index = 585,
    label = "sC4H9 + H <=> C4H82 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H) TS3',
    ),
    longDesc = 
u"""
=(iC3H7+H) TS3
""",
)

entry(
    index = 586,
    label = "sC4H9 + O <=> CH3CHO + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)*2/3 TS3',
    ),
    longDesc = 
u"""
=(iC3H7+H)*2/3 TS3
""",
)

entry(
    index = 587,
    label = "sC4H9 + OH <=> C4H81 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O) TS3 ka+kb',
    ),
    longDesc = 
u"""
=(iC3H7+O) TS3 ka+kb
""",
)

entry(
    index = 588,
    label = "sC4H9 + OH <=> C4H82 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH) TS3',
    ),
    longDesc = 
u"""
=(iC3H7+OH) TS3
""",
)

entry(
    index = 589,
    label = "sC4H9 + O2 <=> C4H81 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH)*2/3 TS3',
    ),
    longDesc = 
u"""
=(iC3H7+OH)*2/3 TS3
""",
)

entry(
    index = 590,
    label = "sC4H9 + O2 <=> C4H82 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BB75',
    ),
    longDesc = 
u"""
BB75
""",
)

entry(
    index = 591,
    label = "sC4H9 + HO2 <=> CH3CHO + C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BB75',
    ),
    longDesc = 
u"""
BB75
""",
)

entry(
    index = 592,
    label = "sC4H9 + HCO <=> C4H10 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2) TS3 ?',
    ),
    longDesc = 
u"""
=(iC3H7+HO2) TS3 ?
""",
)

entry(
    index = 593,
    label = "sC4H9 + CH3 <=> CH4 + C4H81",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HCO) TS3',
    ),
    longDesc = 
u"""
=(iC3H7+HCO) TS3
""",
)

entry(
    index = 594,
    label = "sC4H9 + CH3 <=> CH4 + C4H82",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+CH3) TS3',
    ),
    longDesc = 
u"""
=(iC3H7+CH3) TS3
""",
)

entry(
    index = 595,
    label = "C3H6 + CH3 <=> iC4H9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.6e+10, 'cm^3/(mol*s)'), n=0, Ea=(8003.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.3e+28, 'cm^6/(mol^2*s)'),
            n = -4.27,
            Ea = (2431.1, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.565,
        T3 = (60000, 'K'),
        T1 = (534.2, 'K'),
        T2 = (3007.2, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(iC3H7+CH3)*2/3 TS3\nReactions of i-butyl',
    ),
    longDesc = 
u"""
=(iC3H7+CH3)*2/3 TS3
Reactions of i-butyl
""",
)

entry(
    index = 596,
    label = "iC4H9 + H <=> iC4H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.27e+56, 'cm^6/(mol^2*s)'),
            n = -11.74,
            Ea = (6430.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.506,
        T3 = (1266.6, 'K'),
        T1 = (1266.6, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'TS5 600cm-1',
    ),
    longDesc = 
u"""
TS5 600cm-1
""",
)

entry(
    index = 597,
    label = "iC4H9 + H <=> iC3H7 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+35, 'cm^3/(mol*s)'),
        n = -5.83,
        Ea = (22470, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4, 600cm-1\niC4H9+H = iC3H7+CH3                          1.10E+32  -5.04     16760.0   ! TS4 eq 0.1 atm',
    ),
    longDesc = 
u"""
TS4, 600cm-1
iC4H9+H = iC3H7+CH3                          1.10E+32  -5.04     16760.0   ! TS4 eq 0.1 atm
""",
)

entry(
    index = 598,
    label = "iC4H9 + H <=> iC4H8 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4 eq 1 atm\niC4H9+H = iC3H7+CH3                          1.35E+40  -7.02     31000.0   ! TS4 eq 10 atm',
    ),
    longDesc = 
u"""
TS4 eq 1 atm
iC4H9+H = iC3H7+CH3                          1.35E+40  -7.02     31000.0   ! TS4 eq 10 atm
""",
)

entry(
    index = 599,
    label = "iC4H9 + O <=> iC3H7 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 600,
    label = "iC4H9 + OH <=> iC4H8 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 601,
    label = "iC4H9 + O2 <=> iC4H8 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 602,
    label = "iC4H9 + HO2 <=> iC3H7 + CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 603,
    label = "iC4H9 + HCO <=> iC4H10 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4 ?',
    ),
    longDesc = 
u"""
TS4 ?
""",
)

entry(
    index = 604,
    label = "iC4H9 + CH3 <=> iC4H8 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 605,
    label = "tC4H9 <=> iC4H8 + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.3e+13, 's^-1'), n=0, Ea=(38150.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.9e+41, 'cm^3/(mol*s)'),
            n = -7.36,
            Ea = (36631.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.293,
        T3 = (649, 'K'),
        T1 = (60000, 'K'),
        T2 = (3425.9, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'TS4\nReactions of t-butyl',
    ),
    longDesc = 
u"""
TS4
Reactions of t-butyl
""",
)

entry(
    index = 606,
    label = "tC4H9 + H <=> iC4H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.47e+61, 'cm^6/(mol^2*s)'),
            n = -12.94,
            Ea = (8000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        T3 = (1456.4, 'K'),
        T1 = (1000, 'K'),
        T2 = (10000.5, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'TS4 600cm-1',
    ),
    longDesc = 
u"""
TS4 600cm-1
""",
)

entry(
    index = 607,
    label = "tC4H9 + H <=> iC3H7 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+36, 'cm^3/(mol*s)'),
        n = -6.12,
        Ea = (25640, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4, 600cm-1\ntC4H9+H = iC3H7+CH3                          2.80E+34  -5.69     20500.0   ! TS4 eq 0.1 atm',
    ),
    longDesc = 
u"""
TS4, 600cm-1
tC4H9+H = iC3H7+CH3                          2.80E+34  -5.69     20500.0   ! TS4 eq 0.1 atm
""",
)

entry(
    index = 608,
    label = "tC4H9 + H <=> iC4H8 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.42e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4 eq 1 atm\ntC4H9+H = iC3H7+CH3                          2.60E+36  -6.12     25640.0   ! TS4 eq 10 atm',
    ),
    longDesc = 
u"""
TS4 eq 1 atm
tC4H9+H = iC3H7+CH3                          2.60E+36  -6.12     25640.0   ! TS4 eq 10 atm
""",
)

entry(
    index = 609,
    label = "tC4H9 + O <=> iC4H8 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 610,
    label = "tC4H9 + O <=> CH3COCH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 611,
    label = "tC4H9 + OH <=> iC4H8 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 612,
    label = "tC4H9 + O2 <=> iC4H8 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 613,
    label = "tC4H9 + HO2 <=> CH3 + CH3COCH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 614,
    label = "tC4H9 + HCO <=> iC4H10 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 615,
    label = "tC4H9 + CH3 <=> iC4H8 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+15, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 616,
    label = "CH3COCH3 + H <=> H2 + CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 617,
    label = "CH3COCH3 + O <=> OH + CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (190000, 'cm^3/(mol*s)'),
        n = 2.68,
        Ea = (3716, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=C3H8+H',
    ),
    longDesc = 
u"""
=C3H8+H
""",
)

entry(
    index = 618,
    label = "CH3COCH3 + OH <=> H2O + CH2CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (934, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=C3H8+O',
    ),
    longDesc = 
u"""
=C3H8+O
""",
)

entry(
    index = 619,
    label = "CH3 + CH3CO <=> CH3COCH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+15, 'cm^3/(mol*s)'),
        n = -0.8,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=C3H8+OH',
    ),
    longDesc = 
u"""
=C3H8+OH
""",
)

entry(
    index = 620,
    label = "nC3H7 + CH3 <=> C4H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.93e+14, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.68e+61, 'cm^6/(mol^2*s)'),
            n = -13.24,
            Ea = (6000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (1433.9, 'K'),
        T2 = (5328.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'TS1 kinf\nReactions of n-butane\nkinf : TS3 recommendation\nko: scaled such that Pr(nC3H7+CH3) = Pr(C2H5+CH3)  500cm-1\nFc: assumed equal to Fc(C2H5+CH3)',
    ),
    longDesc = 
u"""
TS1 kinf
Reactions of n-butane
kinf : TS3 recommendation
ko: scaled such that Pr(nC3H7+CH3) = Pr(C2H5+CH3)  500cm-1
Fc: assumed equal to Fc(C2H5+CH3)
""",
)

entry(
    index = 621,
    label = "C2H5 + C2H5 <=> C4H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.88e+14, 'cm^3/(mol*s)'), n=-0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.61e+61, 'cm^6/(mol^2*s)'),
            n = -13.42,
            Ea = (6000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1000, 'K'),
        T1 = (1433.9, 'K'),
        T2 = (5328.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'kinf: -0.5 T power = CH3+C2H5, kinf(300K) = TS1 recommendation\nko: scaled such that Pr(C2H5+C2H5) = Pr(CH3+C2H5) at (T,P), 500 cm-1\nFc: assumed equal to Fc(CH3+C2H5)',
    ),
    longDesc = 
u"""
kinf: -0.5 T power = CH3+C2H5, kinf(300K) = TS1 recommendation
ko: scaled such that Pr(C2H5+C2H5) = Pr(CH3+C2H5) at (T,P), 500 cm-1
Fc: assumed equal to Fc(CH3+C2H5)
""",
)

entry(
    index = 622,
    label = "C4H10 + H <=> pC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 623,
    label = "C4H10 + H <=> sC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H scaled to BBW at 753K)',
    ),
    longDesc = 
u"""
=(C3H8+H scaled to BBW at 753K)
""",
)

entry(
    index = 624,
    label = "C4H10 + O <=> pC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H scaled to BBW at 753K)',
    ),
    longDesc = 
u"""
=(C3H8+H scaled to BBW at 753K)
""",
)

entry(
    index = 625,
    label = "C4H10 + O <=> sC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (430000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (2580, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86/CW',
    ),
    longDesc = 
u"""
86/CW
""",
)

entry(
    index = 626,
    label = "C4H10 + OH <=> pC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (954, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86/CW',
    ),
    longDesc = 
u"""
86/CW
""",
)

entry(
    index = 627,
    label = "C4H10 + OH <=> sC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91Coh',
    ),
    longDesc = 
u"""
91Coh
""",
)

entry(
    index = 628,
    label = "C4H10 + O2 <=> pC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '91Coh',
    ),
    longDesc = 
u"""
91Coh
""",
)

entry(
    index = 629,
    label = "C4H10 + O2 <=> sC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2) TS3',
    ),
    longDesc = 
u"""
=(C3H8+O2) TS3
""",
)

entry(
    index = 630,
    label = "C4H10 + HO2 <=> pC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2 TS3',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2 TS3
""",
)

entry(
    index = 631,
    label = "C4H10 + HO2 <=> sC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2) TS3',
    ),
    longDesc = 
u"""
=(C3H8+HO2) TS3
""",
)

entry(
    index = 632,
    label = "C4H10 + CH3 <=> pC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2 TS3',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2 TS3
""",
)

entry(
    index = 633,
    label = "C4H10 + CH3 <=> sC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3) TS3 see notes',
    ),
    longDesc = 
u"""
=(C3H8+CH3) TS3 see notes
""",
)

entry(
    index = 634,
    label = "iC3H7 + CH3 <=> iC4H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.4e+15, 'cm^3/(mol*s)'), n=-0.68, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.16e+61, 'cm^6/(mol^2*s)'),
            n = -13.33,
            Ea = (3903.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.931,
        T3 = (60000, 'K'),
        T1 = (1265.3, 'K'),
        T2 = (5469.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)*2 TS3 see notes\nReactions of i-butane',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2 TS3 see notes
Reactions of i-butane
""",
)

entry(
    index = 635,
    label = "iC4H10 + H <=> iC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6760, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4, 600cm-1',
    ),
    longDesc = 
u"""
TS4, 600cm-1
""",
)

entry(
    index = 636,
    label = "iC4H10 + H <=> tC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (600000, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (2580, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 637,
    label = "iC4H10 + O <=> iC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (430000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (3640, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 638,
    label = "iC4H10 + O <=> tC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (1110, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 639,
    label = "iC4H10 + OH <=> iC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+08, 'cm^3/(mol*s)'),
        n = 1.53,
        Ea = (775, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 640,
    label = "iC4H10 + OH <=> tC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.73e+10, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (64, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 641,
    label = "iC4H10 + HO2 <=> iC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (15500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 642,
    label = "iC4H10 + HO2 <=> tC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (10500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 643,
    label = "iC4H10 + O2 <=> iC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 644,
    label = "iC4H10 + O2 <=> tC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (44000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 645,
    label = "iC4H10 + CH3 <=> iC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.36, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7150, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 646,
    label = "iC4H10 + CH3 <=> tC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.9, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (4600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4',
    ),
    longDesc = 
u"""
TS4
""",
)

entry(
    index = 647,
    label = "C6H2 + H <=> C6H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+30, 'cm^3/(mol*s)'),
        n = -4.92,
        Ea = (10800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'TS4\nReactions of C6H2\nC6H2 + H = C6H3                              4.30E+45 -10.15    13250.0    !   20 Torr 97WAN/FRE\nC6H2 + H = C6H3                              2.60E+46 -10.15    15500.0    !   90 Torr 97WAN/FRE',
    ),
    longDesc = 
u"""
TS4
Reactions of C6H2
C6H2 + H = C6H3                              4.30E+45 -10.15    13250.0    !   20 Torr 97WAN/FRE
C6H2 + H = C6H3                              2.60E+46 -10.15    15500.0    !   90 Torr 97WAN/FRE
""",
)

entry(
    index = 648,
    label = "C6H3 + H <=> C4H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+23, 'cm^3/(mol*s)'),
        n = -2.55,
        Ea = (10780, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr 97WAN/FRE\nReactions of C6H3\nC6H3 + H = C4H2 + C2H2                       2.40E+19  -1.60     2800.0    !   20 Torr RRKM 97WAN/FRE\nC6H3 + H = C4H2 + C2H2                       3.70E+22  -2.50     5140.0    !   90 Torr RRKM 97WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr 97WAN/FRE
Reactions of C6H3
C6H3 + H = C4H2 + C2H2                       2.40E+19  -1.60     2800.0    !   20 Torr RRKM 97WAN/FRE
C6H3 + H = C4H2 + C2H2                       3.70E+22  -2.50     5140.0    !   90 Torr RRKM 97WAN/FRE
""",
)

entry(
    index = 649,
    label = "C6H3 + H <=> l-C6H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+43, 'cm^3/(mol*s)'),
        n = -9.01,
        Ea = (12120, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM 97WAN/FRE\nC6H3 + H = l-C6H4                            4.20E+44 -10.27     7890.0    !   20 Torr RRKM 97WAN/FRE\nC6H3 + H = l-C6H4                            5.30E+46 -10.68     9270.0    !   90 Torr RRKM 97WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM 97WAN/FRE
C6H3 + H = l-C6H4                            4.20E+44 -10.27     7890.0    !   20 Torr RRKM 97WAN/FRE
C6H3 + H = l-C6H4                            5.30E+46 -10.68     9270.0    !   90 Torr RRKM 97WAN/FRE
""",
)

entry(
    index = 650,
    label = "C6H3 + H <=> C6H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM 97WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM 97WAN/FRE
""",
)

entry(
    index = 651,
    label = "C6H3 + OH <=> C6H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
""",
)

entry(
    index = 652,
    label = "l-C6H4 + H <=> C6H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+78, 'cm^3/(mol*s)'),
        n = -19.72,
        Ea = (31400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '97WAN/FRE\nl-C6H4 + H = C6H5                            4.40E+74 -19.09    25800.     !   10 Torr RRKM 97WAN/FRE\nl-C6H4 + H = C6H5                            3.60E+77 -20.09    28100.     !   20 Torr RRKM 97WAN/FRE\nl-C6H4 + H = C6H5                            4.70E+78 -20.10    29500.     !   90 Torr RRKM 97WAN/FRE',
    ),
    longDesc = 
u"""
97WAN/FRE
l-C6H4 + H = C6H5                            4.40E+74 -19.09    25800.     !   10 Torr RRKM 97WAN/FRE
l-C6H4 + H = C6H5                            3.60E+77 -20.09    28100.     !   20 Torr RRKM 97WAN/FRE
l-C6H4 + H = C6H5                            4.70E+78 -20.10    29500.     !   90 Torr RRKM 97WAN/FRE
""",
)

entry(
    index = 653,
    label = "l-C6H4 + H <=> o-C6H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+54, 'cm^3/(mol*s)'),
        n = -11.7,
        Ea = (34500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM 97WAN/FRE\nl-C6H4 + H = C6H5                            3.90E+69 -16.63    34100.     ! 7600 Torr RRKM 97WAN/FRE\nl-C6H4 + H = o-C6H4+ H                       8.70E+45  -9.61    22300.     !   10 Torr RRKM 97WAN/FRE\nl-C6H4 + H = o-C6H4+ H                       2.20E+47  -9.98    24000.     !   20 Torr RRKM 97WAN/FRE\nl-C6H4 + H = o-C6H4+ H                       9.70E+48 -10.37    27000.     !   90 Torr RRKM 97WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM 97WAN/FRE
l-C6H4 + H = C6H5                            3.90E+69 -16.63    34100.     ! 7600 Torr RRKM 97WAN/FRE
l-C6H4 + H = o-C6H4+ H                       8.70E+45  -9.61    22300.     !   10 Torr RRKM 97WAN/FRE
l-C6H4 + H = o-C6H4+ H                       2.20E+47  -9.98    24000.     !   20 Torr RRKM 97WAN/FRE
l-C6H4 + H = o-C6H4+ H                       9.70E+48 -10.37    27000.     !   90 Torr RRKM 97WAN/FRE
""",
)

entry(
    index = 654,
    label = "l-C6H4 + H <=> C6H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (9240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '760 Torr RRKM 97WAN/FRE\nl-C6H4 + H = o-C6H4+ H                       5.70E+55 -11.98    41900.     ! 7600 Torr RRKM 97WAN/FRE',
    ),
    longDesc = 
u"""
760 Torr RRKM 97WAN/FRE
l-C6H4 + H = o-C6H4+ H                       5.70E+55 -11.98    41900.     ! 7600 Torr RRKM 97WAN/FRE
""",
)

entry(
    index = 655,
    label = "l-C6H4 + OH <=> C6H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= C4H4+H',
    ),
    longDesc = 
u"""
= C4H4+H
""",
)

entry(
    index = 656,
    label = "C4H2 + C2H2 <=> o-C6H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+78, 'cm^3/(mol*s)'),
        n = -19.31,
        Ea = (67920, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'see notes\nC4H2 + C2H2 = o-C6H4                         1.40E+07   1.453    25407     ! kinf 300-2500 K, 83 kcal/mol, rot',
    ),
    longDesc = 
u"""
see notes
C4H2 + C2H2 = o-C6H4                         1.40E+07   1.453    25407     ! kinf 300-2500 K, 83 kcal/mol, rot
""",
)

entry(
    index = 657,
    label = "o-C6H4 + OH <=> CO + C5H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '5 atm',
    ),
    longDesc = 
u"""
5 atm
""",
)

entry(
    index = 658,
    label = "C6H5 + CH3 <=> C6H5CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated\n*****************************************************************************\nThe following is the ring destruction sybmodel\n*****************************************************************************\nReactions of toluene (C6H5CH3)',
    ),
    longDesc = 
u"""
Estimated
*****************************************************************************
The following is the ring destruction sybmodel
*****************************************************************************
Reactions of toluene (C6H5CH3)
""",
)

entry(
    index = 659,
    label = "C6H5CH3 + O2 <=> C6H5CH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (42992, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99-TOK-LIN (added 5/2)',
    ),
    longDesc = 
u"""
99-TOK-LIN (added 5/2)
""",
)

entry(
    index = 660,
    label = "C6H5CH3 + OH <=> C6H5CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.62e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2770, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ENG-FIT',
    ),
    longDesc = 
u"""
98-ENG-FIT
""",
)

entry(
    index = 661,
    label = "C6H5CH3 + OH <=> C6H4CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.333e+08, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (1450, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '05-VAS-DAV',
    ),
    longDesc = 
u"""
05-VAS-DAV
""",
)

entry(
    index = 662,
    label = "C6H5CH3 + H <=> C6H5CH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.259e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8359, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '5/6 * c6h6+oh',
    ),
    longDesc = 
u"""
5/6 * c6h6+oh
""",
)

entry(
    index = 663,
    label = "C6H5CH3 + H <=> C6H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '90-HIP-REI',
    ),
    longDesc = 
u"""
90-HIP-REI
""",
)

entry(
    index = 664,
    label = "C6H5CH3 + O <=> OC6H4CH3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3795, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '01-TOK-LIN (added 5/2)',
    ),
    longDesc = 
u"""
01-TOK-LIN (added 5/2)
""",
)

entry(
    index = 665,
    label = "C6H5CH3 + CH3 <=> C6H5CH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '82-NIC-GUM',
    ),
    longDesc = 
u"""
82-NIC-GUM
""",
)

entry(
    index = 666,
    label = "C6H5CH3 + C6H5 <=> C6H5CH2 + C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.103e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '76-KER-PAR',
    ),
    longDesc = 
u"""
76-KER-PAR
""",
)

entry(
    index = 667,
    label = "C6H5CH3 + HO2 <=> C6H5CH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.975e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14069, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88-FAH-STE',
    ),
    longDesc = 
u"""
88-FAH-STE
""",
)

entry(
    index = 668,
    label = "C6H5CH3 + HO2 <=> C6H4CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.42e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28810, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '94-BAULCH',
    ),
    longDesc = 
u"""
94-BAULCH
""",
)

entry(
    index = 669,
    label = "C6H5CH2 + H <=> C6H5CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.1e+103, 'cm^6/(mol^2*s)'),
            n = -24.63,
            Ea = (14590, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.431,
        T3 = (383, 'K'),
        T1 = (152, 'K'),
        T2 = (4730, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5},
        comment = '94-BAULCH\nReactions of benzyl radical (C6H5CH2)',
    ),
    longDesc = 
u"""
94-BAULCH
Reactions of benzyl radical (C6H5CH2)
""",
)

entry(
    index = 670,
    label = "C6H5CH2 + H <=> C6H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+66, 'cm^3/(mol*s)'),
        n = -13.94,
        Ea = (64580, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'kinf (assumed, reduced from 2.6E14)\nk0 (RRKM)',
    ),
    longDesc = 
u"""
kinf (assumed, reduced from 2.6E14)
k0 (RRKM)
""",
)

entry(
    index = 671,
    label = "C6H5CH2 + O <=> C6H5CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM at 1 atm,',
    ),
    longDesc = 
u"""
RRKM at 1 atm,
""",
)

entry(
    index = 672,
    label = "C6H5CH2 + OH <=> C6H5CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(90a-HIP-REI)',
    ),
    longDesc = 
u"""
(90a-HIP-REI)
""",
)

entry(
    index = 673,
    label = "C6H5CH2 + HO2 <=> C6H5CHO + H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '90a-HIP-REI',
    ),
    longDesc = 
u"""
90a-HIP-REI
""",
)

entry(
    index = 674,
    label = "C6H5CH2 + C6H5OH <=> C6H5CH3 + C6H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '90a-HIP-REI',
    ),
    longDesc = 
u"""
90a-HIP-REI
""",
)

entry(
    index = 675,
    label = "C6H5CH2 + HOC6H4CH3 <=> C6H5CH3 + OC6H4CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est.',
    ),
    longDesc = 
u"""
92-EMD-BRE, est.
""",
)

entry(
    index = 676,
    label = "C6H5CH2OH + OH <=> C6H5CHO + H2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est.\nReactions of benzyl alcohol (C6H5CH2OH)',
    ),
    longDesc = 
u"""
92-EMD-BRE, est.
Reactions of benzyl alcohol (C6H5CH2OH)
""",
)

entry(
    index = 677,
    label = "C6H5CH2OH + H <=> C6H5CHO + H2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8235, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '90a-HIP-REI',
    ),
    longDesc = 
u"""
90a-HIP-REI
""",
)

entry(
    index = 678,
    label = "C6H5CH2OH + H <=> C6H6 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5148, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est.',
    ),
    longDesc = 
u"""
92-EMD-BRE, est.
""",
)

entry(
    index = 679,
    label = "C6H5CH2OH + C6H5 <=> C6H5CHO + C6H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est.',
    ),
    longDesc = 
u"""
92-EMD-BRE, est.
""",
)

entry(
    index = 680,
    label = "C6H5 + HCO <=> C6H5CHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est.\nReactions of benzaldehyde (C6H5CHO)',
    ),
    longDesc = 
u"""
92-EMD-BRE, est.
Reactions of benzaldehyde (C6H5CHO)
""",
)

entry(
    index = 681,
    label = "C6H5CHO <=> C6H5CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+15, 's^-1'),
        n = 0,
        Ea = (86900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est.',
    ),
    longDesc = 
u"""
Est.
""",
)

entry(
    index = 682,
    label = "C6H5CHO + O2 <=> C6H5CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (38950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '86-GRE,Eamodified',
    ),
    longDesc = 
u"""
86-GRE,Eamodified
""",
)

entry(
    index = 683,
    label = "C6H5CHO + OH <=> C6H5CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (-1110, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est. Tsang',
    ),
    longDesc = 
u"""
est. Tsang
""",
)

entry(
    index = 684,
    label = "C6H5CHO + H <=> C6H5CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est.,(CH3CHO+OH)',
    ),
    longDesc = 
u"""
est.,(CH3CHO+OH)
""",
)

entry(
    index = 685,
    label = "C6H5CHO + H <=> C6H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est.,(CH3CHO+H).',
    ),
    longDesc = 
u"""
est.,(CH3CHO+H).
""",
)

entry(
    index = 686,
    label = "C6H5CHO + O <=> C6H5CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est.,(C6H5CH3 + H = C6H6 + CH3)',
    ),
    longDesc = 
u"""
est.,(C6H5CH3 + H = C6H6 + CH3)
""",
)

entry(
    index = 687,
    label = "C6H5CHO + C6H5CH2 <=> C6H5CO + C6H5CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-06, 'cm^3/(mol*s)'),
        n = 5.6,
        Ea = (2460, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est.,(CH3CHO+O)',
    ),
    longDesc = 
u"""
est.,(CH3CHO+O)
""",
)

entry(
    index = 688,
    label = "C6H5CHO + CH3 <=> C6H5CO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-06, 'cm^3/(mol*s)'),
        n = 5.6,
        Ea = (2460, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est.(C6H5CHO + CH3)',
    ),
    longDesc = 
u"""
est.(C6H5CHO + CH3)
""",
)

entry(
    index = 689,
    label = "C6H5CHO + C6H5 <=> C6H5CO + C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.103e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est.(CH3CHO+CH3).',
    ),
    longDesc = 
u"""
est.(CH3CHO+CH3).
""",
)

entry(
    index = 690,
    label = "C6H5CO + H2O2 <=> C6H5CHO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8226, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est.(C6H5CH3+C6H5)',
    ),
    longDesc = 
u"""
est.(C6H5CH3+C6H5)
""",
)

entry(
    index = 691,
    label = "OC6H4CH3 + H <=> HOC6H4CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4e+93, 'cm^6/(mol^2*s)'),
            n = -21.84,
            Ea = (13880, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.043,
        T3 = (304.2, 'K'),
        T1 = (60000, 'K'),
        T2 = (5896.4, 'K'),
        efficiencies = {'[C-]#[O+]': 1.5, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
        comment = 'est.(CH3CO+H2O2 = CH3CHO+HO2)\nReactions of cresoxy radical (OC6H4CH3)',
    ),
    longDesc = 
u"""
est.(CH3CO+H2O2 = CH3CHO+HO2)
Reactions of cresoxy radical (OC6H4CH3)
""",
)

entry(
    index = 692,
    label = "OC6H4CH3 + H <=> C6H5O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4163, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated (C6H5O + H -> C6H5OH) / 2.5\n96-DAV-WAN, 97-WAN-FRE',
    ),
    longDesc = 
u"""
Estimated (C6H5O + H -> C6H5OH) / 2.5
96-DAV-WAN, 97-WAN-FRE
""",
)

entry(
    index = 693,
    label = "OC6H4CH3 + O <=> C6H4O2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est, =(C6H5CH3+H=C6H6+CH3)',
    ),
    longDesc = 
u"""
est, =(C6H5CH3+H=C6H6+CH3)
""",
)

entry(
    index = 694,
    label = "HOC6H4CH3 + OH <=> OC6H4CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est.\nReactions of cresol (HOC6H5CH3)',
    ),
    longDesc = 
u"""
est.
Reactions of cresol (HOC6H5CH3)
""",
)

entry(
    index = 695,
    label = "HOC6H4CH3 + H <=> OC6H4CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88-He-MAL',
    ),
    longDesc = 
u"""
88-He-MAL
""",
)

entry(
    index = 696,
    label = "HOC6H4CH3 + H <=> C6H5CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88-He-MAL',
    ),
    longDesc = 
u"""
88-He-MAL
""",
)

entry(
    index = 697,
    label = "HOC6H4CH3 + H <=> C6H5OH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5148, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88-He-MAL',
    ),
    longDesc = 
u"""
88-He-MAL
""",
)

entry(
    index = 698,
    label = "C6H5CO <=> C6H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+14, 's^-1'),
        n = 0,
        Ea = (29013, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est.\nReaction of benzoyl radical (C6H5CO)',
    ),
    longDesc = 
u"""
92-EMD-BRE, est.
Reaction of benzoyl radical (C6H5CO)
""",
)

entry(
    index = 699,
    label = "C6H5 + H <=> C6H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.6e+75, 'cm^6/(mol^2*s)'),
            n = -16.3,
            Ea = (7000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (0.1, 'K'),
        T1 = (584.9, 'K'),
        T2 = (6113, 'K'),
        efficiencies = {'[C-]#[O+]': 1.5, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
        comment = '00-NAM-LIN (rep 5/1)\nReactions of benzene (C6H6)',
    ),
    longDesc = 
u"""
00-NAM-LIN (rep 5/1)
Reactions of benzene (C6H6)
""",
)

entry(
    index = 700,
    label = "C6H6 + OH <=> C6H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (398500, 'cm^3/(mol*s)'),
        n = 2.286,
        Ea = (1058, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(HW, RRKM)',
    ),
    longDesc = 
u"""
(HW, RRKM)
""",
)

entry(
    index = 701,
    label = "C6H6 + OH <=> C6H5OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Fit,AJ',
    ),
    longDesc = 
u"""
Fit,AJ
""",
)

entry(
    index = 702,
    label = "C6H6 + O <=> C6H5O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92BAU/COB',
    ),
    longDesc = 
u"""
92BAU/COB
""",
)

entry(
    index = 703,
    label = "C6H6 + O <=> C5H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4530, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '50% split 82-NIC-GUM',
    ),
    longDesc = 
u"""
50% split 82-NIC-GUM
""",
)

entry(
    index = 704,
    label = "C6H5 + H2 <=> C6H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (57070, 'cm^3/(mol*s)'),
        n = 2.43,
        Ea = (6273, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '50% split based on McKinnon',
    ),
    longDesc = 
u"""
50% split based on McKinnon
""",
)

entry(
    index = 705,
    label = "C6H5 <=> o-C6H4 + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.3e+12, 's^-1'), n=0.616, Ea=(77313, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e+84, 'cm^3/(mol*s)'),
            n = -18.866,
            Ea = (90064, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.902,
        T3 = (696, 'K'),
        T1 = (358, 'K'),
        T2 = (3856, 'K'),
        efficiencies = {'[C-]#[O+]': 1.5, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
        comment = '97-MEB-LIN\nReactions of phenyl radical (C6H5)',
    ),
    longDesc = 
u"""
97-MEB-LIN
Reactions of phenyl radical (C6H5)
""",
)

entry(
    index = 706,
    label = "C6H5 + H <=> o-C6H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (24500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM 00-HAI-FRE',
    ),
    longDesc = 
u"""
RRKM 00-HAI-FRE
""",
)

entry(
    index = 707,
    label = "C6H5 + O2 <=> C6H5O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6120, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '01-MEB-LIN 1 atm',
    ),
    longDesc = 
u"""
01-MEB-LIN 1 atm
""",
)

entry(
    index = 708,
    label = "C6H5 + O2 <=> C6H4O2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8980, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '94-FRA-HER',
    ),
    longDesc = 
u"""
94-FRA-HER
""",
)

entry(
    index = 709,
    label = "C6H5 + O <=> C5H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '94-FRA-HER',
    ),
    longDesc = 
u"""
94-FRA-HER
""",
)

entry(
    index = 710,
    label = "C6H5 + OH <=> C6H5O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '94-FRA-HER',
    ),
    longDesc = 
u"""
94-FRA-HER
""",
)

entry(
    index = 711,
    label = "C6H5 + HO2 <=> C6H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est.',
    ),
    longDesc = 
u"""
Est.
""",
)

entry(
    index = 712,
    label = "C6H5 + HO2 <=> C6H6 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est.',
    ),
    longDesc = 
u"""
Est.
""",
)

entry(
    index = 713,
    label = "C6H5 + CH4 <=> C6H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00389, 'cm^3/(mol*s)'),
        n = 4.57,
        Ea = (5256, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated, 10/01',
    ),
    longDesc = 
u"""
Estimated, 10/01
""",
)

entry(
    index = 714,
    label = "C6H5 + C2H6 <=> C6H6 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4443, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '99-TOK-LIN (added 5/1)',
    ),
    longDesc = 
u"""
99-TOK-LIN (added 5/1)
""",
)

entry(
    index = 715,
    label = "C6H5 + CH2O <=> C6H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (85500, 'cm^3/(mol*s)'),
        n = 2.19,
        Ea = (38, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '01-PAR-LIN (added 5/2)',
    ),
    longDesc = 
u"""
01-PAR-LIN (added 5/2)
""",
)

entry(
    index = 716,
    label = "C6H4O2 <=> C5H4O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.4e+11, 's^-1'),
        n = 0,
        Ea = (59000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '00-CHO-LIN (added 5/1)\nC6H5 + C6H5 = BIPHENYL                       3.800E+31  -5.750    7950.00  !  97-WAN-FRE,  20 torr\nC6H5 + C6H5 = BIPHENYL                       6.100E+25  -4.000    5590.00  !  97-WAN-FRE,  90 torr\nC6H5 + C6H5 = BIPHENYL                       2.000E+19  -2.050    2900.00  !  97-WAN-FRE, 760 torr\nC6H6 + C6H5 = BIPHENYL+H                     5.600E+12  -0.074    7550.00  !  97-WAN-FRE,  20 torr\nC6H6 + C6H5 = BIPHENYL+H                     1.500E+14  -0.450    8915.00  !  97-WAN-FRE,  90 torr\nC6H6 + C6H5 = BIPHENYL+H                     1.100E+23  -2.920   15890.00  !  97-WAN-FRE, 760 torr\nReactions of benzoquinone (p-C6H4O2)',
    ),
    longDesc = 
u"""
00-CHO-LIN (added 5/1)
C6H5 + C6H5 = BIPHENYL                       3.800E+31  -5.750    7950.00  !  97-WAN-FRE,  20 torr
C6H5 + C6H5 = BIPHENYL                       6.100E+25  -4.000    5590.00  !  97-WAN-FRE,  90 torr
C6H5 + C6H5 = BIPHENYL                       2.000E+19  -2.050    2900.00  !  97-WAN-FRE, 760 torr
C6H6 + C6H5 = BIPHENYL+H                     5.600E+12  -0.074    7550.00  !  97-WAN-FRE,  20 torr
C6H6 + C6H5 = BIPHENYL+H                     1.500E+14  -0.450    8915.00  !  97-WAN-FRE,  90 torr
C6H6 + C6H5 = BIPHENYL+H                     1.100E+23  -2.920   15890.00  !  97-WAN-FRE, 760 torr
Reactions of benzoquinone (p-C6H4O2)
""",
)

entry(
    index = 717,
    label = "C6H4O2 + H <=> CO + C5H5O(1,3)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+09, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (3900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '94-FRA-HER',
    ),
    longDesc = 
u"""
94-FRA-HER
""",
)

# RMG does not accept a reaction with more than 3 products\reactants
#entry(
#    index = 718,
#    label = "C6H4O2 + O <=> CO + CO + C2H2 + CH2CO",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (3e+13, 'cm^3/(mol*s)'),
#        n = 0,
#        Ea = (5000, 'cal/mol'),
#        T0 = (1, 'K'),
#        comment = 'est. HW k = kinf[C6H6 + H]',
#    ),
#    longDesc = 
#u"""
#est. HW k = kinf[C6H6 + H]
#""",
#)

entry(
    index = 719,
    label = "C6H5O + H <=> C5H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est. HW, ??\nReactions of phenoxy radical (C6H5O)',
    ),
    longDesc = 
u"""
est. HW, ??
Reactions of phenoxy radical (C6H5O)
""",
)

entry(
    index = 720,
    label = "C6H5O + H <=> C5H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'added 9/25',
    ),
    longDesc = 
u"""
added 9/25
""",
)

entry(
    index = 721,
    label = "C6H5O <=> CO + C5H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.76e+54, 's^-1'),
        n = -12.06,
        Ea = (72800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'added 9/25',
    ),
    longDesc = 
u"""
added 9/25
""",
)

entry(
    index = 722,
    label = "C6H5O + O <=> C6H4O2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+10, 'cm^3/(mol*s)'),
        n = 0.47,
        Ea = (795, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'DAVIS, RRKM 1 atm (Ea reduced by 1.5 kcal/mol = change in hf,ch65O)',
    ),
    longDesc = 
u"""
DAVIS, RRKM 1 atm (Ea reduced by 1.5 kcal/mol = change in hf,ch65O)
""",
)

entry(
    index = 723,
    label = "C6H5OH <=> C5H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0,
        Ea = (60808, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'MEB-LIN-95 (added 9/23)\nReactions of phenol (C6H5OH)',
    ),
    longDesc = 
u"""
MEB-LIN-95 (added 9/23)
Reactions of phenol (C6H5OH)
""",
)

entry(
    index = 724,
    label = "C6H5OH + OH <=> C6H5O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.95e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1312, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-HOR-FRA (added 9/25)',
    ),
    longDesc = 
u"""
98-HOR-FRA (added 9/25)
""",
)

entry(
    index = 725,
    label = "C6H5OH + H <=> C6H5O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12398, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '90-KNI-KOC',
    ),
    longDesc = 
u"""
90-KNI-KOC
""",
)

entry(
    index = 726,
    label = "C6H5OH + O <=> C6H5O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7352, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88-He-MAL',
    ),
    longDesc = 
u"""
88-He-MAL
""",
)

entry(
    index = 727,
    label = "C6H5OH + C2H3 <=> C6H5O + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est. as 1/6 of CH3C6H4CH3 + O from 82-NIC-GUM',
    ),
    longDesc = 
u"""
92-EMD-BRE, est. as 1/6 of CH3C6H4CH3 + O from 82-NIC-GUM
""",
)

entry(
    index = 728,
    label = "C6H5OH + nC4H5 <=> C6H5O + C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est. from phenol + OH',
    ),
    longDesc = 
u"""
92-EMD-BRE, est. from phenol + OH
""",
)

entry(
    index = 729,
    label = "C6H5OH + C6H5 <=> C6H5O + C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.91e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est. from phenol + OH',
    ),
    longDesc = 
u"""
92-EMD-BRE, est. from phenol + OH
""",
)

entry(
    index = 730,
    label = "C5H6 + H <=> C2H2 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.74e+36, 'cm^3/(mol*s)'),
        n = -6.18,
        Ea = (32890, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '88-FAH-STE\nReactions of cyclopentadiene (C5H6)',
    ),
    longDesc = 
u"""
88-FAH-STE
Reactions of cyclopentadiene (C5H6)
""",
)

entry(
    index = 731,
    label = "C5H6 + H <=> lC5H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.27e+126, 'cm^3/(mol*s)'),
        n = -32.3,
        Ea = (82348, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ',
    ),
    longDesc = 
u"""
98-ZHO-BOZ
""",
)

entry(
    index = 732,
    label = "C5H6 + H <=> C5H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.03e+08, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (5590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '02-MOS-LIN',
    ),
    longDesc = 
u"""
02-MOS-LIN
""",
)

entry(
    index = 733,
    label = "C5H6 + O <=> C5H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47700, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (1106, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '02-MOS-LIN',
    ),
    longDesc = 
u"""
02-MOS-LIN
""",
)

entry(
    index = 734,
    label = "C5H6 + O <=> C5H5O(1,3) + H",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (8.91e+12, 'cm^3/(mol*s)'),
                n = -0.15,
                Ea = (590, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '98-ZHO-BOZ est.',
            ),
            Arrhenius(
                A = (5.6e+12, 'cm^3/(mol*s)'),
                n = -0.06,
                Ea = (200, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '98-ZHO-BOZ, C5H5O1_1',
            ),
        ],
    ),
)

entry(
    index = 735,
    label = "C5H6 + O <=> nC4H5 + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.7e+51, 'cm^3/(mol*s)'),
        n = -11.09,
        Ea = (33240, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ, C5H5O1_2',
    ),
    longDesc = 
u"""
98-ZHO-BOZ, C5H5O1_2
""",
)

entry(
    index = 736,
    label = "C5H6 + OH <=> C5H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.08e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ',
    ),
    longDesc = 
u"""
98-ZHO-BOZ
""",
)

entry(
    index = 737,
    label = "C5H6 + HO2 <=> C5H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (12900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ est.',
    ),
    longDesc = 
u"""
98-ZHO-BOZ est.
""",
)

entry(
    index = 738,
    label = "C5H6 + O2 <=> C5H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (37150, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ est.',
    ),
    longDesc = 
u"""
98-ZHO-BOZ est.
""",
)

entry(
    index = 739,
    label = "C5H6 + HCO <=> C5H5 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (16000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ est.',
    ),
    longDesc = 
u"""
98-ZHO-BOZ est.
""",
)

entry(
    index = 740,
    label = "C5H6 + CH3 <=> C5H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.18, 'cm^3/(mol*s)'),
        n = 4,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ est.',
    ),
    longDesc = 
u"""
98-ZHO-BOZ est.
""",
)

entry(
    index = 741,
    label = "C5H5 + H <=> C5H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.4e+80, 'cm^6/(mol^2*s)'),
            n = -18.28,
            Ea = (12994, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.068,
        T3 = (400.7, 'K'),
        T1 = (4135.8, 'K'),
        T2 = (5501.9, 'K'),
        efficiencies = {'[C-]#[O+]': 1.5, 'C': 2, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
        comment = '98-ZHO-BOZ est.',
    ),
    longDesc = 
u"""
98-ZHO-BOZ est.
""",
)

entry(
    index = 742,
    label = "C5H5 + O2 <=> C5H5O(2,4) + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.78e+15, 'cm^3/(mol*s)'),
        n = -0.73,
        Ea = (48740, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '92-EMD-BRE, est., 94-FRA-HER\n96-DAV-WAN, 97-WAN-FRE\nReactions of cyclopentadienyl radical (C5H5)',
    ),
    longDesc = 
u"""
92-EMD-BRE, est., 94-FRA-HER
96-DAV-WAN, 97-WAN-FRE
Reactions of cyclopentadienyl radical (C5H5)
""",
)

entry(
    index = 743,
    label = "C5H5 + O <=> C5H5O(2,4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e-12, 'cm^3/(mol*s)'),
        n = 5.87,
        Ea = (-17310, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '10/18',
    ),
    longDesc = 
u"""
10/18
""",
)

entry(
    index = 744,
    label = "C5H5 + O <=> C5H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.81e+13, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (20, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '10/18',
    ),
    longDesc = 
u"""
10/18
""",
)

entry(
    index = 745,
    label = "C5H5 + O <=> nC4H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13, 'cm^3/(mol*s)'),
        n = -0.17,
        Ea = (440, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ',
    ),
    longDesc = 
u"""
98-ZHO-BOZ
""",
)

entry(
    index = 746,
    label = "C5H5 + OH <=> C5H4OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.51e+57, 'cm^3/(mol*s)'),
        n = -12.18,
        Ea = (48350, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'ZHO-BOZ-98 added 10/08',
    ),
    longDesc = 
u"""
ZHO-BOZ-98 added 10/08
""",
)

entry(
    index = 747,
    label = "C5H5 + OH <=> C5H5O(2,4) + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.36e+51, 'cm^3/(mol*s)'),
        n = -10.46,
        Ea = (57100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ',
    ),
    longDesc = 
u"""
98-ZHO-BOZ
""",
)

entry(
    index = 748,
    label = "C5H5 + HO2 <=> C5H5O(2,4) + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.27e+29, 'cm^3/(mol*s)'),
        n = -4.69,
        Ea = (11650, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '10/18',
    ),
    longDesc = 
u"""
10/18
""",
)

entry(
    index = 749,
    label = "C5H5 + OH <=> C5H5OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (6.49e+14, 'cm^3/(mol*s)'),
                n = -0.85,
                Ea = (-2730, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '10/18',
            ),
            Arrhenius(
                A = (1.15e+43, 'cm^3/(mol*s)'),
                n = -8.76,
                Ea = (18730, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '98-ZHO-BOZ, C5H5OH',
            ),
            Arrhenius(
                A = (1.06e+59, 'cm^3/(mol*s)'),
                n = -13.08,
                Ea = (33450, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '98-ZHO-BOZ, 1-C5H5OH',
            ),
        ],
    ),
)

entry(
    index = 750,
    label = "C5H5 + O2 <=> C5H4O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0.08,
        Ea = (18000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '98-ZHO-BOZ, 2-C5H5OH',
    ),
    longDesc = 
u"""
98-ZHO-BOZ, 2-C5H5OH
""",
)

entry(
    index = 751,
    label = "C5H5OH + H <=> C5H5O(2,4) + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM 1 atm\nC5H5 + C5H5 = C10H8 + 2H                     6.430E+12   0.000    4000.00  ! 98-KER-KIE (added 5/12)\nReactions of cyclopentadienols (1,3-, 2,4- and 1,4-C5H5OH)',
    ),
    longDesc = 
u"""
RRKM 1 atm
C5H5 + C5H5 = C10H8 + 2H                     6.430E+12   0.000    4000.00  ! 98-KER-KIE (added 5/12)
Reactions of cyclopentadienols (1,3-, 2,4- and 1,4-C5H5OH)
""",
)

entry(
    index = 752,
    label = "C5H5OH + H <=> C5H4OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (1492, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'as C6H5OH + H = C6H5O + H2 + 3 kcal/mol E barrier',
    ),
    longDesc = 
u"""
as C6H5OH + H = C6H5O + H2 + 3 kcal/mol E barrier
""",
)

entry(
    index = 753,
    label = "C5H5OH + OH <=> C5H5O(2,4) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est. C5H6 + H = C5H5 + H2',
    ),
    longDesc = 
u"""
est. C5H6 + H = C5H5 + H2
""",
)

entry(
    index = 754,
    label = "C5H5OH + OH <=> C5H4OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.08e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'as C6H5OH + OH = C6H5O + H2O',
    ),
    longDesc = 
u"""
as C6H5OH + OH = C6H5O + H2O
""",
)

entry(
    index = 755,
    label = "C5H5O(2,4) + H <=> C5H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est. C5H6 + OH = C5H5 + H2O',
    ),
    longDesc = 
u"""
est. C5H6 + OH = C5H5 + H2O
""",
)

entry(
    index = 756,
    label = "C5H5O(2,4) <=> C5H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 's^-1'),
        n = 0,
        Ea = (30000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'est. HW\nReactions of C5H5O(2,4)',
    ),
    longDesc = 
u"""
est. HW
Reactions of C5H5O(2,4)
""",
)

entry(
    index = 757,
    label = "C5H5O(2,4) + O2 <=> C5H4O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(est. HW)',
    ),
    longDesc = 
u"""
(est. HW)
""",
)

entry(
    index = 758,
    label = "C5H4O + H <=> C5H5O(1,3)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(est. HW)\nReactions of C5H5O(1,3)',
    ),
    longDesc = 
u"""
(est. HW)
Reactions of C5H5O(1,3)
""",
)

entry(
    index = 759,
    label = "C5H5O(1,3) <=> c-C4H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0,
        Ea = (36000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW, see notes',
    ),
    longDesc = 
u"""
Est. HW, see notes
""",
)

entry(
    index = 760,
    label = "C5H5O(1,3) + O2 <=> C5H4O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. (very rough) from C6H5O',
    ),
    longDesc = 
u"""
Est. (very rough) from C6H5O
""",
)

entry(
    index = 761,
    label = "C5H4OH <=> C5H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+13, 's^-1'),
        n = 0,
        Ea = (48000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW\nReactions of cyclopentadienone (C5H4O)',
    ),
    longDesc = 
u"""
Est. HW
Reactions of cyclopentadienone (C5H4O)
""",
)

entry(
    index = 762,
    label = "C5H4O <=> C2H2 + C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+41, 's^-1'),
        n = -7.87,
        Ea = (98700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. EBG',
    ),
    longDesc = 
u"""
Est. EBG
""",
)

entry(
    index = 763,
    label = "C5H4O + H <=> CO + c-C4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+09, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (3900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'RRKM (10/18)',
    ),
    longDesc = 
u"""
RRKM (10/18)
""",
)

entry(
    index = 764,
    label = "C5H4O + O <=> CO + HCO + C3H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-858, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW = C6H6 + H kinf, possiblly too large',
    ),
    longDesc = 
u"""
Est. HW = C6H6 + H kinf, possiblly too large
""",
)

entry(
    index = 765,
    label = "c-C4H5 + H <=> C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW = C4H6 + O\nRactions of c-C4H5',
    ),
    longDesc = 
u"""
Est. HW = C4H6 + O
Ractions of c-C4H5
""",
)

entry(
    index = 766,
    label = "c-C4H5 + H <=> C2H4 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW, fast c-C4H6 -> C4H6 - Lifshitz',
    ),
    longDesc = 
u"""
Est. HW, fast c-C4H6 -> C4H6 - Lifshitz
""",
)

entry(
    index = 767,
    label = "c-C4H5 + O <=> CH2CHO + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW',
    ),
    longDesc = 
u"""
Est. HW
""",
)

entry(
    index = 768,
    label = "c-C4H5 + O2 <=> CH2CHO + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW',
    ),
    longDesc = 
u"""
Est. HW
""",
)

entry(
    index = 769,
    label = "c-C4H5 <=> C4H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+12, 's^-1'),
        n = 0,
        Ea = (52000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW, C3H5+O2',
    ),
    longDesc = 
u"""
Est. HW, C3H5+O2
""",
)

entry(
    index = 770,
    label = "c-C4H5 <=> C2H3 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 's^-1'),
        n = 0,
        Ea = (58000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW',
    ),
    longDesc = 
u"""
Est. HW
""",
)

entry(
    index = 771,
    label = "aC3H5 + C2H3 <=> lC5H7 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est. HW\nReactions of 1,4-pentadien-3-yl (l-C5H7)',
    ),
    longDesc = 
u"""
Est. HW
Reactions of 1,4-pentadien-3-yl (l-C5H7)
""",
)

entry(
    index = 772,
    label = "lC5H7 + O <=> C2H3CHO + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est.',
    ),
    longDesc = 
u"""
Est.
""",
)

entry(
    index = 773,
    label = "lC5H7 + OH <=> C2H3CHO + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Est.',
    ),
    longDesc = 
u"""
Est.
""",
)

entry(
    index = 774,
    label = "PXC5H9 + H <=> C5H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'Est.\nReactions of 1-penten-X-yl radicals\nPXC5H9 = C5H8-13+H                                2.48E+53  -12.30    52000.0   ! =(C4H7)\nPXC5H9 = C5H8-13+H                                1.85E+48  -10.50    51770.0   ! =(C4H7)10 atm',
    ),
    longDesc = 
u"""
Est.
Reactions of 1-penten-X-yl radicals
PXC5H9 = C5H8-13+H                                2.48E+53  -12.30    52000.0   ! =(C4H7)
PXC5H9 = C5H8-13+H                                1.85E+48  -10.50    51770.0   ! =(C4H7)10 atm
""",
)

entry(
    index = 775,
    label = "PXC5H9 + H <=> CH3 + C4H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=nC3H7+H',
    ),
    longDesc = 
u"""
=nC3H7+H
""",
)

entry(
    index = 776,
    label = "PXC5H9 + HO2 <=> CH2O + OH + C4H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated\nPXC5H9+H = C5H8-13+H2                             1.80E+12    0.00        0.0   != nC3H7+H\nPXC5H9+O2 = C5H8-13+HO2                           1.00E+11    0.00        0.0   !Estimated',
    ),
    longDesc = 
u"""
Estimated
PXC5H9+H = C5H8-13+H2                             1.80E+12    0.00        0.0   != nC3H7+H
PXC5H9+O2 = C5H8-13+HO2                           1.00E+11    0.00        0.0   !Estimated
""",
)

entry(
    index = 777,
    label = "PXC5H9 + HCO <=> C5H10 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HO2',
    ),
    longDesc = 
u"""
= nC3H7+HO2
""",
)

entry(
    index = 778,
    label = "PXC5H9 <=> C2H4 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+12, 's^-1'),
        n = -0.37,
        Ea = (25124, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HCO\nPXC5H9+CH3 = C5H8-13+CH4                          1.10E+13    0.00        0.0   != nC3H7+CH3',
    ),
    longDesc = 
u"""
= nC3H7+HCO
PXC5H9+CH3 = C5H8-13+CH4                          1.10E+13    0.00        0.0   != nC3H7+CH3
""",
)

entry(
    index = 779,
    label = "cC5H9 <=> PXC5H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.15e+12, 's^-1'),
        n = -0.3,
        Ea = (33721, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 780,
    label = "cC5H9 <=> cC5H8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.53e+11, 's^-1'),
        n = -0.55,
        Ea = (33140, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 781,
    label = "SXC5H9 <=> C5H8-13 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+08, 's^-1'),
        n = -1.35,
        Ea = (32487, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 782,
    label = "SXC5H9 <=> C3H6 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+12, 's^-1'),
        n = -0.58,
        Ea = (37797, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 783,
    label = "SXC5H9 <=> C5H8-14 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.69e-09, 's^-1'),
        n = -1.17,
        Ea = (37097, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 784,
    label = "SXC5H9 <=> CH2C4H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.52e+08, 's^-1'),
        n = -1.42,
        Ea = (14609, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 785,
    label = "CH2C4H7 <=> C4H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+11, 's^-1'),
        n = -0.41,
        Ea = (31254, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 786,
    label = "SAXC5H9 <=> CH3 + C4H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+12, 's^-1'),
        n = -0.1,
        Ea = (35891, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 787,
    label = "C5H10 <=> C2H5 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.24e+22, 's^-1'),
        n = -1.94,
        Ea = (75470, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS\nReactions of C5H10\nC5H10+H(+M) = PXC5H11(+M)                    1.33E+13    0.00     3260.7   ! =(C3H6+H) !BS\nLOW  / 6.26E+38   -6.66     7000.0   /\nTROE / 1.000  1000.0  1310.0 48097.0 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nC5H10+H(+M) = SXC5H11(+M)                    1.33E+13    0.00     1559.8   ! =(C3H6+H) !BS\nLOW  / 8.70E+42   -7.50   4721.8      /\nTROE / 1.000  1000.0   645.4  6844.3 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
Reactions of C5H10
C5H10+H(+M) = PXC5H11(+M)                    1.33E+13    0.00     3260.7   ! =(C3H6+H) !BS
LOW  / 6.26E+38   -6.66     7000.0   /
TROE / 1.000  1000.0  1310.0 48097.0 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
C5H10+H(+M) = SXC5H11(+M)                    1.33E+13    0.00     1559.8   ! =(C3H6+H) !BS
LOW  / 8.70E+42   -7.50   4721.8      /
TROE / 1.000  1000.0   645.4  6844.3 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 788,
    label = "C5H10 <=> C3H6 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.62e+06, 's^-1'),
        n = 1.81,
        Ea = (53454, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 789,
    label = "C5H10 + H <=> C2H4 + nC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 790,
    label = "C5H10 + H <=> C3H6 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)',
    ),
    longDesc = 
u"""
=(C3H6+H)
""",
)

entry(
    index = 791,
    label = "C5H10 + H <=> PXC5H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (650000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 792,
    label = "C5H10 + H <=> SXC5H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+H)',
    ),
    longDesc = 
u"""
=(C4H81+H)
""",
)

entry(
    index = 793,
    label = "C5H10 + H <=> SAXC5H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (-1900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H) !BS',
    ),
    longDesc = 
u"""
=(C3H8+H) !BS
""",
)

entry(
    index = 794,
    label = "C5H10 + O <=> pC4H9 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '05/TO-BU  !BS',
    ),
    longDesc = 
u"""
05/TO-BU  !BS
""",
)

entry(
    index = 795,
    label = "C5H10 + O <=> PXC5H9 + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5760, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '=(C4H81+O)',
            ),
            Arrhenius(
                A = (2.6e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4470, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '(C4H81+O)',
            ),
        ],
    ),
)

entry(
    index = 796,
    label = "C5H10 + OH <=> PXC5H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(C4H81+O)',
    ),
    longDesc = 
u"""
(C4H81+O)
""",
)

entry(
    index = 797,
    label = "C5H10 + O2 <=> PXC5H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+OH)',
    ),
    longDesc = 
u"""
=(C3H8+OH)
""",
)

entry(
    index = 798,
    label = "C5H10 + HO2 <=> PXC5H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 799,
    label = "C5H10 + CH3 <=> PXC5H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.45, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+HO2)',
    ),
    longDesc = 
u"""
=(C4H81+HO2)
""",
)

entry(
    index = 800,
    label = "PXC5H11 <=> C2H4 + nC3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(28366.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7.1e-35, 'cm^3/(mol*s)'),
            n = 15.411,
            Ea = (-600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -5.91,
        T3 = (333, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)\nBeta-scission Reactions of pentyl radicals',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
Beta-scission Reactions of pentyl radicals
""",
)

entry(
    index = 801,
    label = "SXC5H11 <=> C3H6 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0, Ea=(27392.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.7e-33, 'cm^3/(mol*s)'),
            n = 14.91,
            Ea = (-600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -6.53,
        T3 = (333, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '98TSA !BS',
    ),
    longDesc = 
u"""
98TSA !BS
""",
)

entry(
    index = 802,
    label = "S2XC5H11 <=> C4H81 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.8e+13, 's^-1'), n=0, Ea=(29348, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4e-39, 'cm^3/(mol*s)'),
            n = 16.782,
            Ea = (-600.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -7.03,
        T3 = (314, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '98TSA !BS',
    ),
    longDesc = 
u"""
98TSA !BS
""",
)

entry(
    index = 803,
    label = "SXC5H11 + H <=> NC5H12",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+58, 'cm^6/(mol^2*s)'),
            n = -12.08,
            Ea = (11263.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.649,
        T3 = (1213.1, 'K'),
        T1 = (1213.1, 'K'),
        T2 = (13369.7, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '98TSA !BS\nReactions of SXC5H11\nC3H6+C2H5 = SXC5H11                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS',
    ),
    longDesc = 
u"""
98TSA !BS
Reactions of SXC5H11
C3H6+C2H5 = SXC5H11                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS
""",
)

entry(
    index = 804,
    label = "SXC5H11 + H <=> nC3H7 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC5H11+H = nC3H7+C2H5                       5.90E+23   -2.81  10009.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC5H11+H = nC3H7+C2H5                       5.90E+23   -2.81  10009.0  ! =(iC3H7+H)
""",
)

entry(
    index = 805,
    label = "SXC5H11 + H <=> C5H10 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC5H11+H = nC3H7+C2H5                       4.00E+24   -2.83  17542.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC5H11+H = nC3H7+C2H5                       4.00E+24   -2.83  17542.0  ! =(iC3H7+H)
""",
)

entry(
    index = 806,
    label = "SXC5H11 + O <=> CH3CHO + nC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
""",
)

entry(
    index = 807,
    label = "SXC5H11 + OH <=> C5H10 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O)',
    ),
    longDesc = 
u"""
=(iC3H7+O)
""",
)

entry(
    index = 808,
    label = "SXC5H11 + O2 <=> C5H10 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH)',
    ),
    longDesc = 
u"""
=(iC3H7+OH)
""",
)

entry(
    index = 809,
    label = "SXC5H11 + HO2 <=> CH3CHO + nC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
""",
)

entry(
    index = 810,
    label = "SXC5H11 + HCO <=> NC5H12 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2)',
    ),
    longDesc = 
u"""
=(iC3H7+HO2)
""",
)

entry(
    index = 811,
    label = "SXC5H11 + CH3 <=> CH4 + C5H10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HCO)',
    ),
    longDesc = 
u"""
=(iC3H7+HCO)
""",
)

entry(
    index = 812,
    label = "PXC5H11 + H <=> NC5H12",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(iC3H7+CH3)\nReactions of S2XC5H11\nC4H81+CH3(+M)= S2XC5H11(+M)               1.70E+11    0.00   7403.6  ! =(C3H6+CH3) !BS\nLOW  / 2.31E+28  -4.27   1831.0      /\nTROE / 0.565 60000.0   534.2  3007.2 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nS2XC5H11+O2 = C5H10+HO2                       1.30E+11    0.00      0.0  ! =(iC3H7+O2)\nReactions of PXC5H11\nC2H4+nC3H7 = PXC5H11                         3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(iC3H7+CH3)
Reactions of S2XC5H11
C4H81+CH3(+M)= S2XC5H11(+M)               1.70E+11    0.00   7403.6  ! =(C3H6+CH3) !BS
LOW  / 2.31E+28  -4.27   1831.0      /
TROE / 0.565 60000.0   534.2  3007.2 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
S2XC5H11+O2 = C5H10+HO2                       1.30E+11    0.00      0.0  ! =(iC3H7+O2)
Reactions of PXC5H11
C2H4+nC3H7 = PXC5H11                         3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 813,
    label = "PXC5H11 + H <=> nC3H7 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12505, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)\nPXC5H11+H = nC3H7+C2H5                       3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)
PXC5H11+H = nC3H7+C2H5                       3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm
""",
)

entry(
    index = 814,
    label = "PXC5H11 + H <=> C5H10 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)  1 atm\nPXC5H11+H = nC3H7+C2H5                       3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)  1 atm
PXC5H11+H = nC3H7+C2H5                       3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm
""",
)

entry(
    index = 815,
    label = "PXC5H11 + O <=> pC4H9 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)',
    ),
    longDesc = 
u"""
=(nC3H7+H)
""",
)

entry(
    index = 816,
    label = "PXC5H11 + OH <=> C5H10 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O)',
    ),
    longDesc = 
u"""
=(nC3H7+O)
""",
)

entry(
    index = 817,
    label = "PXC5H11 + O2 <=> C5H10 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+OH)',
    ),
    longDesc = 
u"""
=(nC3H7+OH)
""",
)

entry(
    index = 818,
    label = "PXC5H11 + HO2 <=> pC4H9 + OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O2)',
    ),
    longDesc = 
u"""
=(nC3H7+O2)
""",
)

entry(
    index = 819,
    label = "PXC5H11 + HCO <=> NC5H12 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HO2)',
    ),
    longDesc = 
u"""
=(nC3H7+HO2)
""",
)

entry(
    index = 820,
    label = "PXC5H11 + CH3 <=> C5H10 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HCO)',
    ),
    longDesc = 
u"""
=(nC3H7+HCO)
""",
)

entry(
    index = 821,
    label = "pC4H9 + CH3 <=> NC5H12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+CH3)\nReactions of NC5H12',
    ),
    longDesc = 
u"""
=(nC3H7+CH3)
Reactions of NC5H12
""",
)

entry(
    index = 822,
    label = "nC3H7 + C2H5 <=> NC5H12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(CH3+C2H5)',
    ),
    longDesc = 
u"""
=(CH3+C2H5)
""",
)

entry(
    index = 823,
    label = "NC5H12 + H <=> PXC5H11 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 824,
    label = "NC5H12 + H <=> SXC5H11 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)',
    ),
    longDesc = 
u"""
=(C3H8+H)
""",
)

entry(
    index = 825,
    label = "NC5H12 + H <=> S2XC5H11 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2',
    ),
    longDesc = 
u"""
=(C3H8+H)*2
""",
)

entry(
    index = 826,
    label = "NC5H12 + O <=> PXC5H11 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5504, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)   EDames
""",
)

entry(
    index = 827,
    label = "NC5H12 + O <=> SXC5H11 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (620000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2225, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 828,
    label = "NC5H12 + O <=> S2XC5H11 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (310000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2225, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 829,
    label = "NC5H12 + OH <=> PXC5H11 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (974, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 830,
    label = "NC5H12 + OH <=> SXC5H11 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 831,
    label = "NC5H12 + OH <=> S2XC5H11 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1371, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 832,
    label = "NC5H12 + O2 <=> PXC5H11 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 833,
    label = "NC5H12 + O2 <=> SXC5H11 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 834,
    label = "NC5H12 + O2 <=> S2XC5H11 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2
""",
)

entry(
    index = 835,
    label = "NC5H12 + HO2 <=> PXC5H11 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)  EDames
""",
)

entry(
    index = 836,
    label = "NC5H12 + HO2 <=> SXC5H11 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)',
    ),
    longDesc = 
u"""
=(C3H8+HO2)
""",
)

entry(
    index = 837,
    label = "NC5H12 + HO2 <=> S2XC5H11 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9500, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2
""",
)

entry(
    index = 838,
    label = "NC5H12 + CH3 <=> PXC5H11 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2) EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2) EDames
""",
)

entry(
    index = 839,
    label = "NC5H12 + CH3 <=> SXC5H11 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
""",
)

entry(
    index = 840,
    label = "NC5H12 + CH3 <=> S2XC5H11 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2
""",
)

entry(
    index = 841,
    label = "PXC6H11 + H <=> C6H12",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3) EDames\nReactions of 1-hexen-X-yl radicals\nPXC6H11 = C6H10-13+H                              2.48E+53  -12.30  52000.0  !=(C4H7)\nPXC6H11 = C6H10-13+H                              1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm',
    ),
    longDesc = 
u"""
=(C3H8+CH3) EDames
Reactions of 1-hexen-X-yl radicals
PXC6H11 = C6H10-13+H                              2.48E+53  -12.30  52000.0  !=(C4H7)
PXC6H11 = C6H10-13+H                              1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm
""",
)

entry(
    index = 842,
    label = "PXC6H11 + H <=> CH3 + PXC5H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+H',
    ),
    longDesc = 
u"""
= nC3H7+H
""",
)

entry(
    index = 843,
    label = "PXC6H11 + HO2 <=> CH2O + OH + PXC5H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H7+H)\nPXC6H11+H = C6H10-13+H2                           1.80E+12    0.00      0.0  != nC3H7+H\nPXC6H11+O2 = C6H10-13+HO2                         1.00E+11    0.00      0.0  !=(C4H7+O2)',
    ),
    longDesc = 
u"""
=(C4H7+H)
PXC6H11+H = C6H10-13+H2                           1.80E+12    0.00      0.0  != nC3H7+H
PXC6H11+O2 = C6H10-13+HO2                         1.00E+11    0.00      0.0  !=(C4H7+O2)
""",
)

entry(
    index = 844,
    label = "PXC6H11 + HCO <=> C6H12 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HO2',
    ),
    longDesc = 
u"""
= nC3H7+HO2
""",
)

entry(
    index = 845,
    label = "cC6H11 <=> cC6H10 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.34e+11, 's^-1'),
        n = 0.69,
        Ea = (33948, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HCO\nPXC6H11+CH3 = C6H10-13+CH4                        1.10E+13    0.00      0.0  != nC3H7+CH3\nAlternative\nC2H4+aC3H5 = PXC5H9                            3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2',
    ),
    longDesc = 
u"""
= nC3H7+HCO
PXC6H11+CH3 = C6H10-13+CH4                        1.10E+13    0.00      0.0  != nC3H7+CH3
Alternative
C2H4+aC3H5 = PXC5H9                            3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2
""",
)

entry(
    index = 846,
    label = "cC5H9CH2 <=> CH2C5H8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.76e+08, 's^-1'),
        n = 1.11,
        Ea = (34616, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 847,
    label = "SAXC6H11 <=> C4H6 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39e+11, 's^-1'),
        n = 0.66,
        Ea = (32263, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 848,
    label = "PXC6H11 <=> C4H7 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+12, 's^-1'),
        n = 0.12,
        Ea = (27572, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 849,
    label = "SAXC6H11-3 <=> C5H8-13 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+13, 's^-1'),
        n = -0.21,
        Ea = (33346, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 850,
    label = "SXC6H11 <=> C3H6 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.57e+12, 's^-1'),
        n = 0.13,
        Ea = (24386, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 851,
    label = "m1C5H81 <=> aC3H5 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.37e+12, 's^-1'),
        n = 0.12,
        Ea = (23947, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 852,
    label = "cC6H11 <=> PXC6H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 's^-1'),
        n = 0.07,
        Ea = (27983, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 853,
    label = "PXC6H11 <=> cC5H9CH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.55e+08, 's^-1'),
        n = 0.36,
        Ea = (10704, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 854,
    label = "CH3cC5H83 <=> SXC6H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.59e+12, 's^-1'),
        n = 0.15,
        Ea = (32940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 855,
    label = "CH3cC5H83 <=> m1C5H81",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.55e+12, 's^-1'),
        n = 0.15,
        Ea = (32404, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 856,
    label = "PXC6H11 <=> SAXC6H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (155, 's^-1'),
        n = 2.83,
        Ea = (15566, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 857,
    label = "cC5H9CH2 <=> CH3cC5H83",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66.1, 's^-1'),
        n = 2.85,
        Ea = (21082, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 858,
    label = "PXC6H11 <=> SAXC6H11-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9330, 's^-1'),
        n = 2.38,
        Ea = (22141, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 859,
    label = "S2XC6H11 <=> C6H10-13 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13, 's^-1'),
        n = 0,
        Ea = (38000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 860,
    label = "C6H12 <=> aC3H5 + nC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+23, 's^-1'),
        n = -2.03,
        Ea = (74958, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '05/TOU-BU  !BS\nReactions of C6H12\nC6H12+H(+M) = PXC6H13(+M)                    1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS\nLOW  / 6.26E+38  -6.66   7000.0      /\nTROE / 1.000  1000.0  1310.0 48097.0 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nC6H12+H(+M) = SXC6H13(+M)                    1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS\nLOW  / 8.70E+42  -7.50   4721.8      /\nTROE / 1.000  1000.0   645.4  6844.3 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
05/TOU-BU  !BS
Reactions of C6H12
C6H12+H(+M) = PXC6H13(+M)                    1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS
LOW  / 6.26E+38  -6.66   7000.0      /
TROE / 1.000  1000.0  1310.0 48097.0 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
C6H12+H(+M) = SXC6H13(+M)                    1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS
LOW  / 8.70E+42  -7.50   4721.8      /
TROE / 1.000  1000.0   645.4  6844.3 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 861,
    label = "C6H12 <=> C3H6 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.08e+06, 's^-1'),
        n = 1.65,
        Ea = (53752, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 862,
    label = "C6H12 + H <=> C2H4 + pC4H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 863,
    label = "C6H12 + H <=> C3H6 + nC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)',
    ),
    longDesc = 
u"""
=(C3H6+H)
""",
)

entry(
    index = 864,
    label = "C6H12 + H <=> PXC6H11 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (650000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 865,
    label = "C6H12 + H <=> SXC6H11 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+H)',
    ),
    longDesc = 
u"""
=(C4H81+H)
""",
)

entry(
    index = 866,
    label = "C6H12 + H <=> S2XC6H11 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H) !BS',
    ),
    longDesc = 
u"""
=(C3H8+H) !BS
""",
)

entry(
    index = 867,
    label = "C6H12 + H <=> SAXC6H11 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (-1900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H) !BS',
    ),
    longDesc = 
u"""
=(C3H8+H) !BS
""",
)

entry(
    index = 868,
    label = "C6H12 + O <=> PXC5H11 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '05/TO-BU  !BS',
    ),
    longDesc = 
u"""
05/TO-BU  !BS
""",
)

entry(
    index = 869,
    label = "C6H12 + O <=> PXC6H11 + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5760, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '=(C4H81+O)',
            ),
            Arrhenius(
                A = (2.6e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4470, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '(C4H81+O)',
            ),
        ],
    ),
)

entry(
    index = 870,
    label = "C6H12 + OH <=> PXC6H11 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(C4H81+O)',
    ),
    longDesc = 
u"""
(C4H81+O)
""",
)

entry(
    index = 871,
    label = "C6H12 + O2 <=> PXC6H11 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+OH)',
    ),
    longDesc = 
u"""
=(C3H8+OH)
""",
)

entry(
    index = 872,
    label = "C6H12 + HO2 <=> PXC6H11 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 873,
    label = "C6H12 + CH3 <=> PXC6H11 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.45, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+HO2)',
    ),
    longDesc = 
u"""
=(C4H81+HO2)
""",
)

entry(
    index = 874,
    label = "PXC6H13 <=> C2H4 + pC4H9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.02e+12, 's^-1'), n=0.3, Ea=(27273.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7.1e-35, 'cm^3/(mol*s)'),
            n = 15.411,
            Ea = (-600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -5.91,
        T3 = (333, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)\nReactions of PXC6H13\nC2H4+pC4H9 = PXC6H13                         3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nPXC6H13+H(+M) = NC6H14(+M)                   3.60E+13    0.00      0.0  ! =(nC3H7+H)    !BS\nLOW  / 3.01E+48  -9.32   5833.6      /\nTROE / 0.498  1314.0  1314.0 50000.0 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nBeta-scission Reactions of hexyl radicals',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
Reactions of PXC6H13
C2H4+pC4H9 = PXC6H13                         3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
PXC6H13+H(+M) = NC6H14(+M)                   3.60E+13    0.00      0.0  ! =(nC3H7+H)    !BS
LOW  / 3.01E+48  -9.32   5833.6      /
TROE / 0.498  1314.0  1314.0 50000.0 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
Beta-scission Reactions of hexyl radicals
""",
)

entry(
    index = 875,
    label = "SXC6H13 <=> C3H6 + nC3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.47e+11, 's^-1'), n=0.57, Ea=(28044.5, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.7e-33, 'cm^3/(mol*s)'),
            n = 14.91,
            Ea = (-600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -6.53,
        T3 = (333, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '07TSA !B',
    ),
    longDesc = 
u"""
07TSA !B
""",
)

entry(
    index = 876,
    label = "S2XC6H13 <=> C2H5 + C4H81",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.55e+12, 's^-1'), n=0.29, Ea=(28296.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.5e-26, 'cm^3/(mol*s)'),
            n = 13.09,
            Ea = (-600.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.74,
        T3 = (308, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '07TSA !B',
    ),
    longDesc = 
u"""
07TSA !B
""",
)

entry(
    index = 877,
    label = "S2XC6H13 <=> C5H10 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.13e+10, 's^-1'), n=0.78, Ea=(29648, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4e-39, 'cm^3/(mol*s)'),
            n = 16.782,
            Ea = (-600.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -7.03,
        T3 = (314, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '07TSA !B',
    ),
    longDesc = 
u"""
07TSA !B
""",
)

entry(
    index = 878,
    label = "PXC6H13 + H <=> pC4H9 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12505, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '07TSA !B\nPXC6H13+H = pC4H9+C2H5                       3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm',
    ),
    longDesc = 
u"""
07TSA !B
PXC6H13+H = pC4H9+C2H5                       3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm
""",
)

entry(
    index = 879,
    label = "PXC6H13 + H <=> C6H12 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)  1 atm\nPXC6H13+H = pC4H9+C2H5                       3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)  1 atm
PXC6H13+H = pC4H9+C2H5                       3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm
""",
)

entry(
    index = 880,
    label = "PXC6H13 + O <=> PXC5H11 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)',
    ),
    longDesc = 
u"""
=(nC3H7+H)
""",
)

entry(
    index = 881,
    label = "PXC6H13 + OH <=> C6H12 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O)',
    ),
    longDesc = 
u"""
=(nC3H7+O)
""",
)

entry(
    index = 882,
    label = "PXC6H13 + O2 <=> C6H12 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+OH)',
    ),
    longDesc = 
u"""
=(nC3H7+OH)
""",
)

entry(
    index = 883,
    label = "PXC6H13 + HO2 <=> PXC5H11 + OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O2)',
    ),
    longDesc = 
u"""
=(nC3H7+O2)
""",
)

entry(
    index = 884,
    label = "PXC6H13 + HCO <=> NC6H14 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HO2)',
    ),
    longDesc = 
u"""
=(nC3H7+HO2)
""",
)

entry(
    index = 885,
    label = "PXC6H13 + CH3 <=> C6H12 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HCO)',
    ),
    longDesc = 
u"""
=(nC3H7+HCO)
""",
)

entry(
    index = 886,
    label = "SXC6H13 + H <=> NC6H14",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+58, 'cm^6/(mol^2*s)'),
            n = -12.08,
            Ea = (11263.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.649,
        T3 = (1213.1, 'K'),
        T1 = (1213.1, 'K'),
        T2 = (13369.7, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(nC3H7+CH3)\nReactions of SXC6H13\nC3H6+nC3H7 = SXC6H13                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!B',
    ),
    longDesc = 
u"""
=(nC3H7+CH3)
Reactions of SXC6H13
C3H6+nC3H7 = SXC6H13                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!B
""",
)

entry(
    index = 887,
    label = "SXC6H13 + H <=> pC4H9 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC6H13+H = pC4H9+C2H5                       5.90E+23   -2.81  10009.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC6H13+H = pC4H9+C2H5                       5.90E+23   -2.81  10009.0  ! =(iC3H7+H)
""",
)

entry(
    index = 888,
    label = "SXC6H13 + H <=> C6H12 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC6H13+H = pC4H9+C2H5                       4.00E+24   -2.83  17542.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC6H13+H = pC4H9+C2H5                       4.00E+24   -2.83  17542.0  ! =(iC3H7+H)
""",
)

entry(
    index = 889,
    label = "SXC6H13 + O <=> CH3CHO + pC4H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
""",
)

entry(
    index = 890,
    label = "SXC6H13 + OH <=> C6H12 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O)',
    ),
    longDesc = 
u"""
=(iC3H7+O)
""",
)

entry(
    index = 891,
    label = "SXC6H13 + O2 <=> C6H12 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH)',
    ),
    longDesc = 
u"""
=(iC3H7+OH)
""",
)

entry(
    index = 892,
    label = "SXC6H13 + HO2 <=> CH3CHO + pC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
""",
)

entry(
    index = 893,
    label = "SXC6H13 + HCO <=> NC6H14 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2)',
    ),
    longDesc = 
u"""
=(iC3H7+HO2)
""",
)

entry(
    index = 894,
    label = "SXC6H13 + CH3 <=> CH4 + C6H12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HCO)',
    ),
    longDesc = 
u"""
=(iC3H7+HCO)
""",
)

entry(
    index = 895,
    label = "S2XC6H13 + O2 <=> C6H12 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+CH3)\nReactions of S2XC6H13\nC2H5+C4H81 = S2XC6H13                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!B\nC5H10+CH3(+M)= S2XC6H13(+M)                 1.70E+11    0.00   7403.6  ! =(C3H6+CH3)   !B\nLOW  / 2.31E+28  -4.27   1831.0      /\nTROE / 0.565 60000.0   534.2  3007.2 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(iC3H7+CH3)
Reactions of S2XC6H13
C2H5+C4H81 = S2XC6H13                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!B
C5H10+CH3(+M)= S2XC6H13(+M)                 1.70E+11    0.00   7403.6  ! =(C3H6+CH3)   !B
LOW  / 2.31E+28  -4.27   1831.0      /
TROE / 0.565 60000.0   534.2  3007.2 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 896,
    label = "PXC5H11 + CH3 <=> NC6H14",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of NC6H14',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of NC6H14
""",
)

entry(
    index = 897,
    label = "pC4H9 + C2H5 <=> NC6H14",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(CH3+C2H5)',
    ),
    longDesc = 
u"""
=(CH3+C2H5)
""",
)

entry(
    index = 898,
    label = "nC3H7 + nC3H7 <=> NC6H14",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 899,
    label = "NC6H14 + H <=> PXC6H13 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 900,
    label = "NC6H14 + H <=> SXC6H13 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)',
    ),
    longDesc = 
u"""
=(C3H8+H)
""",
)

entry(
    index = 901,
    label = "NC6H14 + H <=> S2XC6H13 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2',
    ),
    longDesc = 
u"""
=(C3H8+H)*2
""",
)

entry(
    index = 902,
    label = "NC6H14 + O <=> PXC6H13 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5504, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2   EDames
""",
)

entry(
    index = 903,
    label = "NC6H14 + O <=> SXC6H13 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (350000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (2106, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 904,
    label = "NC6H14 + O <=> S2XC6H13 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (350000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (2106, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 905,
    label = "NC6H14 + OH <=> PXC6H13 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (974, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 906,
    label = "NC6H14 + OH <=> SXC6H13 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 907,
    label = "NC6H14 + OH <=> S2XC6H13 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1331, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 908,
    label = "NC6H14 + O2 <=> PXC6H13 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 909,
    label = "NC6H14 + O2 <=> SXC6H13 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 910,
    label = "NC6H14 + O2 <=> S2XC6H13 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2
""",
)

entry(
    index = 911,
    label = "NC6H14 + HO2 <=> PXC6H13 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2  EDames
""",
)

entry(
    index = 912,
    label = "NC6H14 + HO2 <=> SXC6H13 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)',
    ),
    longDesc = 
u"""
=(C3H8+HO2)
""",
)

entry(
    index = 913,
    label = "NC6H14 + HO2 <=> S2XC6H13 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2
""",
)

entry(
    index = 914,
    label = "NC6H14 + CH3 <=> PXC6H13 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2 EDames
""",
)

entry(
    index = 915,
    label = "NC6H14 + CH3 <=> SXC6H13 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
""",
)

entry(
    index = 916,
    label = "NC6H14 + CH3 <=> S2XC6H13 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2
""",
)

entry(
    index = 917,
    label = "PXC7H13 + H <=> C7H14",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)*2 EDames\nReactions of PXC7H13\nPXC7H13 = C7H12+H                              2.48E+53  -12.30  52000.0  !=(C4H7)\nPXC7H13 = C7H12+H                              1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2 EDames
Reactions of PXC7H13
PXC7H13 = C7H12+H                              2.48E+53  -12.30  52000.0  !=(C4H7)
PXC7H13 = C7H12+H                              1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm
""",
)

entry(
    index = 918,
    label = "PXC7H13 + H <=> CH3 + PXC6H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+H',
    ),
    longDesc = 
u"""
= nC3H7+H
""",
)

entry(
    index = 919,
    label = "PXC7H13 + HO2 <=> CH2O + OH + PXC6H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H7+H)\nPXC7H13+H = C7H12+H2                           1.80E+12    0.00      0.0  != nC3H7+H\nPXC7H13+O2 = C7H12+HO2                         1.00E+11    0.00      0.0  !=(C4H7+O2)',
    ),
    longDesc = 
u"""
=(C4H7+H)
PXC7H13+H = C7H12+H2                           1.80E+12    0.00      0.0  != nC3H7+H
PXC7H13+O2 = C7H12+HO2                         1.00E+11    0.00      0.0  !=(C4H7+O2)
""",
)

entry(
    index = 920,
    label = "PXC7H13 + HCO <=> C7H14 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HO2',
    ),
    longDesc = 
u"""
= nC3H7+HO2
""",
)

entry(
    index = 921,
    label = "C2H4 + PXC5H9 <=> PXC7H13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HCO\nPXC7H13+CH3 = C7H12+CH4                        1.10E+13    0.00      0.0  != nC3H7+CH3\nAlternative',
    ),
    longDesc = 
u"""
= nC3H7+HCO
PXC7H13+CH3 = C7H12+CH4                        1.10E+13    0.00      0.0  != nC3H7+CH3
Alternative
""",
)

entry(
    index = 922,
    label = "C7H14 <=> pC4H9 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+23, 's^-1'),
        n = -2.03,
        Ea = (74958, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H4+C2H5)*2\nReactions of C7H14\nC7H14+H(+M) = PXC7H15(+M)                    1.33E+13    0.00   3260.7  ! =(C3H6+H) !B\nLOW  / 6.26E+38  -6.66   7000.0      /\nTROE / 1.000  1000.0  1310.0 48097.0 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nC7H14+H(+M) = SXC7H15(+M)                    1.33E+13    0.00   1559.8  ! =(C3H6+H) !B\nLOW  / 8.70E+42  -7.50   4721.8      /\nTROE / 1.000  1000.0   645.4  6844.3 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(C2H4+C2H5)*2
Reactions of C7H14
C7H14+H(+M) = PXC7H15(+M)                    1.33E+13    0.00   3260.7  ! =(C3H6+H) !B
LOW  / 6.26E+38  -6.66   7000.0      /
TROE / 1.000  1000.0  1310.0 48097.0 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
C7H14+H(+M) = SXC7H15(+M)                    1.33E+13    0.00   1559.8  ! =(C3H6+H) !B
LOW  / 8.70E+42  -7.50   4721.8      /
TROE / 1.000  1000.0   645.4  6844.3 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 923,
    label = "C7H14 <=> C4H81 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.08e+06, 's^-1'),
        n = 1.65,
        Ea = (53752, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 924,
    label = "C7H14 + H <=> C2H4 + PXC5H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 925,
    label = "C7H14 + H <=> C3H6 + pC4H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)',
    ),
    longDesc = 
u"""
=(C3H6+H)
""",
)

entry(
    index = 926,
    label = "C7H14 + H <=> PXC7H13 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (650000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 927,
    label = "C7H14 + O <=> PXC6H13 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+H)',
    ),
    longDesc = 
u"""
=(C4H81+H)
""",
)

entry(
    index = 928,
    label = "C7H14 + O <=> PXC7H13 + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5760, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '=(C4H81+O)',
            ),
            Arrhenius(
                A = (2.6e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4470, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '(C4H81+O)',
            ),
        ],
    ),
)

entry(
    index = 929,
    label = "C7H14 + OH <=> PXC7H13 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(C4H81+O)',
    ),
    longDesc = 
u"""
(C4H81+O)
""",
)

entry(
    index = 930,
    label = "C7H14 + O2 <=> PXC7H13 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+OH)',
    ),
    longDesc = 
u"""
=(C3H8+OH)
""",
)

entry(
    index = 931,
    label = "C7H14 + HO2 <=> PXC7H13 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 932,
    label = "C7H14 + CH3 <=> PXC7H13 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.45, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+HO2)',
    ),
    longDesc = 
u"""
=(C4H81+HO2)
""",
)

entry(
    index = 933,
    label = "PXC7H15 <=> C2H4 + PXC5H11",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.94e+11, 's^-1'), n=0.33, Ea=(27210, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.8e-44, 'cm^3/(mol*s)'),
            n = 18.729,
            Ea = (-602.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -14.66,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)\nReactions of PXC7H15\nC2H4+PXC5H11 = PXC7H15                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!B\nBeta-scission Reactions of heptyl radicals',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
Reactions of PXC7H15
C2H4+PXC5H11 = PXC7H15                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!B
Beta-scission Reactions of heptyl radicals
""",
)

entry(
    index = 934,
    label = "SXC7H15 <=> pC4H9 + C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.01e+11, 's^-1'), n=0.56, Ea=(28092.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.9e-39, 'cm^3/(mol*s)'),
            n = 16.934,
            Ea = (-602.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -25.27,
        T3 = (223, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAa !B',
    ),
    longDesc = 
u"""
08TSAa !B
""",
)

entry(
    index = 935,
    label = "S2XC7H15 <=> nC3H7 + C4H81",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95e+12, 's^-1'), n=0.31, Ea=(28257.1, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2e-38, 'cm^3/(mol*s)'),
            n = 16.814,
            Ea = (-602.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -20.96,
        T3 = (221, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAa !B',
    ),
    longDesc = 
u"""
08TSAa !B
""",
)

entry(
    index = 936,
    label = "S2XC7H15 <=> C6H12 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.1e+11, 's^-1'), n=0.75, Ea=(29401.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.06e-42, 'cm^3/(mol*s)'),
            n = 18.004,
            Ea = (-602.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -20.94,
        T3 = (217, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAa !B',
    ),
    longDesc = 
u"""
08TSAa !B
""",
)

entry(
    index = 937,
    label = "S3XC7H15 <=> C2H5 + C5H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.89e+12, 's^-1'), n=0.31, Ea=(28257.1, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.1e-38, 'cm^3/(mol*s)'),
            n = 16.897,
            Ea = (-602.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -27.54,
        T3 = (224, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAa !B',
    ),
    longDesc = 
u"""
08TSAa !B
""",
)

entry(
    index = 938,
    label = "PXC7H15 + H <=> NC7H16",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAa !B',
    ),
    longDesc = 
u"""
08TSAa !B
""",
)

entry(
    index = 939,
    label = "PXC7H15 + H <=> PXC5H11 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12505, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)\nPXC7H15+H = PXC5H11+C2H5                     3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)
PXC7H15+H = PXC5H11+C2H5                     3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm
""",
)

entry(
    index = 940,
    label = "PXC7H15 + H <=> C7H14 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)  1 atm\nPXC7H15+H = PXC5H11+C2H5                     3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)  1 atm
PXC7H15+H = PXC5H11+C2H5                     3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm
""",
)

entry(
    index = 941,
    label = "PXC7H15 + O <=> PXC6H13 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)',
    ),
    longDesc = 
u"""
=(nC3H7+H)
""",
)

entry(
    index = 942,
    label = "PXC7H15 + OH <=> C7H14 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O)',
    ),
    longDesc = 
u"""
=(nC3H7+O)
""",
)

entry(
    index = 943,
    label = "PXC7H15 + O2 <=> C7H14 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+OH)',
    ),
    longDesc = 
u"""
=(nC3H7+OH)
""",
)

entry(
    index = 944,
    label = "PXC7H15 + HO2 <=> PXC6H13 + OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O2)',
    ),
    longDesc = 
u"""
=(nC3H7+O2)
""",
)

entry(
    index = 945,
    label = "PXC7H15 + HCO <=> NC7H16 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HO2)',
    ),
    longDesc = 
u"""
=(nC3H7+HO2)
""",
)

entry(
    index = 946,
    label = "PXC7H15 + CH3 <=> C7H14 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HCO)',
    ),
    longDesc = 
u"""
=(nC3H7+HCO)
""",
)

entry(
    index = 947,
    label = "SXC7H15 + H <=> PXC5H11 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+CH3)\nReactions of SXC7H15\npC4H9+C3H6 = SXC7H15                        3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !B\nSXC7H15+H(+M) = NC7H16(+M)                   2.40E+13    0.00      0.0  ! =(iC3H7+H)     !B\nLOW  / 1.70E+58 -12.08  11263.7      /\nTROE / 0.649  1213.1  1213.1 13369.7 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nSXC7H15+H = PXC5H11+C2H5                     5.90E+23   -2.81  10009.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(nC3H7+CH3)
Reactions of SXC7H15
pC4H9+C3H6 = SXC7H15                        3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !B
SXC7H15+H(+M) = NC7H16(+M)                   2.40E+13    0.00      0.0  ! =(iC3H7+H)     !B
LOW  / 1.70E+58 -12.08  11263.7      /
TROE / 0.649  1213.1  1213.1 13369.7 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
SXC7H15+H = PXC5H11+C2H5                     5.90E+23   -2.81  10009.0  ! =(iC3H7+H)
""",
)

entry(
    index = 948,
    label = "SXC7H15 + H <=> C7H14 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC7H15+H = PXC5H11+C2H5                     4.00E+24   -2.83  17542.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC7H15+H = PXC5H11+C2H5                     4.00E+24   -2.83  17542.0  ! =(iC3H7+H)
""",
)

entry(
    index = 949,
    label = "SXC7H15 + O <=> CH3CHO + PXC5H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
""",
)

entry(
    index = 950,
    label = "SXC7H15 + OH <=> C7H14 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O)',
    ),
    longDesc = 
u"""
=(iC3H7+O)
""",
)

entry(
    index = 951,
    label = "SXC7H15 + O2 <=> C7H14 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH)',
    ),
    longDesc = 
u"""
=(iC3H7+OH)
""",
)

entry(
    index = 952,
    label = "SXC7H15 + HO2 <=> CH3CHO + PXC5H11 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
""",
)

entry(
    index = 953,
    label = "SXC7H15 + HCO <=> NC7H16 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2)',
    ),
    longDesc = 
u"""
=(iC3H7+HO2)
""",
)

entry(
    index = 954,
    label = "SXC7H15 + CH3 <=> CH4 + C7H14",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HCO)',
    ),
    longDesc = 
u"""
=(iC3H7+HCO)
""",
)

entry(
    index = 955,
    label = "S2XC7H15 + O2 <=> C7H14 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+CH3)\nReactions of S2XC7H15\nnC3H7+C4H81 = S2XC7H15                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !B\nC6H12+CH3(+M)= S2XC7H15(+M)                 1.70E+11    0.00   7403.6  ! =(C3H6+CH3)    !B\nLOW  / 2.31E+28  -4.27   1831.0      /\nTROE / 0.565 60000.0   534.2  3007.2 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(iC3H7+CH3)
Reactions of S2XC7H15
nC3H7+C4H81 = S2XC7H15                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !B
C6H12+CH3(+M)= S2XC7H15(+M)                 1.70E+11    0.00   7403.6  ! =(C3H6+CH3)    !B
LOW  / 2.31E+28  -4.27   1831.0      /
TROE / 0.565 60000.0   534.2  3007.2 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 956,
    label = "S3XC7H15 + O2 <=> C7H14 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S3XC7H15\nC2H5+C5H10 = S3XC7H15                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !B',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S3XC7H15
C2H5+C5H10 = S3XC7H15                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !B
""",
)

entry(
    index = 957,
    label = "PXC6H13 + CH3 <=> NC7H16",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of NC7H16',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of NC7H16
""",
)

entry(
    index = 958,
    label = "PXC5H11 + C2H5 <=> NC7H16",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(CH3+C2H5)',
    ),
    longDesc = 
u"""
=(CH3+C2H5)
""",
)

entry(
    index = 959,
    label = "pC4H9 + nC3H7 <=> NC7H16",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 960,
    label = "NC7H16 + H <=> PXC7H15 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 961,
    label = "NC7H16 + H <=> SXC7H15 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)',
    ),
    longDesc = 
u"""
=(C3H8+H)
""",
)

entry(
    index = 962,
    label = "NC7H16 + H <=> S2XC7H15 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2',
    ),
    longDesc = 
u"""
=(C3H8+H)*2
""",
)

entry(
    index = 963,
    label = "NC7H16 + H <=> S3XC7H15 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2   EDames
""",
)

entry(
    index = 964,
    label = "NC7H16 + O <=> PXC7H15 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5504, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)     EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)     EDames
""",
)

entry(
    index = 965,
    label = "NC7H16 + O <=> SXC7H15 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (280000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1908, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 966,
    label = "NC7H16 + O <=> S2XC7H15 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (280000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1908, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 967,
    label = "NC7H16 + O <=> S3XC7H15 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (140000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1908, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 968,
    label = "NC7H16 + OH <=> PXC7H15 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (974, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 86/CW',
    ),
    longDesc = 
u"""
!B 86/CW
""",
)

entry(
    index = 969,
    label = "NC7H16 + OH <=> SXC7H15 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-595, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 970,
    label = "NC7H16 + OH <=> S2XC7H15 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1311, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 971,
    label = "NC7H16 + OH <=> S3XC7H15 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1311, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 972,
    label = "NC7H16 + O2 <=> PXC7H15 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!B 91Coh',
    ),
    longDesc = 
u"""
!B 91Coh
""",
)

entry(
    index = 973,
    label = "NC7H16 + O2 <=> SXC7H15 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 974,
    label = "NC7H16 + O2 <=> S2XC7H15 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2
""",
)

entry(
    index = 975,
    label = "NC7H16 + O2 <=> S3XC7H15 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2  EDames
""",
)

entry(
    index = 976,
    label = "NC7H16 + HO2 <=> PXC7H15 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)    EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)    EDames
""",
)

entry(
    index = 977,
    label = "NC7H16 + HO2 <=> SXC7H15 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)',
    ),
    longDesc = 
u"""
=(C3H8+HO2)
""",
)

entry(
    index = 978,
    label = "NC7H16 + HO2 <=> S2XC7H15 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2
""",
)

entry(
    index = 979,
    label = "NC7H16 + HO2 <=> S3XC7H15 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9500, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2 EDames
""",
)

entry(
    index = 980,
    label = "NC7H16 + CH3 <=> PXC7H15 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)   EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)   EDames
""",
)

entry(
    index = 981,
    label = "NC7H16 + CH3 <=> SXC7H15 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
""",
)

entry(
    index = 982,
    label = "NC7H16 + CH3 <=> S2XC7H15 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2
""",
)

entry(
    index = 983,
    label = "NC7H16 + CH3 <=> S3XC7H15 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2 EDames
""",
)

entry(
    index = 984,
    label = "PXC8H15 + H <=> C8H16",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)   EDames\nReactions of PXC8H15\nPXC8H15 = C8H14+H                              2.48E+53  -12.30  52000.0  !=(C4H7)\nPXC8H15 = C8H14+H                              1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm',
    ),
    longDesc = 
u"""
=(C3H8+CH3)   EDames
Reactions of PXC8H15
PXC8H15 = C8H14+H                              2.48E+53  -12.30  52000.0  !=(C4H7)
PXC8H15 = C8H14+H                              1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm
""",
)

entry(
    index = 985,
    label = "PXC8H15 + H <=> CH3 + PXC7H13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+H',
    ),
    longDesc = 
u"""
= nC3H7+H
""",
)

entry(
    index = 986,
    label = "PXC8H15 + HO2 <=> CH2O + OH + PXC7H13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H7+H)\nPXC8H15+H = C8H14+H2                           1.80E+12    0.00      0.0  != nC3H7+H\nPXC8H15+O2 = C8H14+HO2                         1.00E+11    0.00      0.0  !=(C4H7+O2)',
    ),
    longDesc = 
u"""
=(C4H7+H)
PXC8H15+H = C8H14+H2                           1.80E+12    0.00      0.0  != nC3H7+H
PXC8H15+O2 = C8H14+HO2                         1.00E+11    0.00      0.0  !=(C4H7+O2)
""",
)

entry(
    index = 987,
    label = "PXC8H15 + HCO <=> C8H16 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HO2',
    ),
    longDesc = 
u"""
= nC3H7+HO2
""",
)

entry(
    index = 988,
    label = "C2H4 + PXC6H11 <=> PXC8H15",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HCO\nPXC8H15+CH3 = C8H14+CH4                        1.10E+13    0.00      0.0  != nC3H7+CH3\nAlternative',
    ),
    longDesc = 
u"""
= nC3H7+HCO
PXC8H15+CH3 = C8H14+CH4                        1.10E+13    0.00      0.0  != nC3H7+CH3
Alternative
""",
)

entry(
    index = 989,
    label = "C8H16 <=> PXC5H11 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+23, 's^-1'),
        n = -2.03,
        Ea = (74958, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H4+C2H5)*2\nReactions of C8H16\nC8H16+H(+M) = PXC8H17(+M)                    1.33E+13    0.00   3260.7  ! =(C3H6+H) !B\nLOW  / 6.26E+38  -6.66   7000.0      /\nTROE / 1.000  1000.0  1310.0 48097.0 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nC8H16+H(+M) = SXC8H17(+M)                    1.33E+13    0.00   1559.8  ! =(C3H6+H) !B\nLOW  / 8.70E+42  -7.50   4721.8      /\nTROE / 1.000  1000.0   645.4  6844.3 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(C2H4+C2H5)*2
Reactions of C8H16
C8H16+H(+M) = PXC8H17(+M)                    1.33E+13    0.00   3260.7  ! =(C3H6+H) !B
LOW  / 6.26E+38  -6.66   7000.0      /
TROE / 1.000  1000.0  1310.0 48097.0 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
C8H16+H(+M) = SXC8H17(+M)                    1.33E+13    0.00   1559.8  ! =(C3H6+H) !B
LOW  / 8.70E+42  -7.50   4721.8      /
TROE / 1.000  1000.0   645.4  6844.3 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 990,
    label = "C8H16 <=> C5H10 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.08e+06, 's^-1'),
        n = 1.65,
        Ea = (53752, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 991,
    label = "C8H16 + H <=> C2H4 + PXC6H13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 992,
    label = "C8H16 + H <=> C3H6 + PXC5H11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)',
    ),
    longDesc = 
u"""
=(C3H6+H)
""",
)

entry(
    index = 993,
    label = "C8H16 + H <=> PXC8H15 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (650000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 994,
    label = "C8H16 + O <=> PXC7H15 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+H)',
    ),
    longDesc = 
u"""
=(C4H81+H)
""",
)

entry(
    index = 995,
    label = "C8H16 + O <=> PXC8H15 + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5760, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '=(C4H81+O)',
            ),
            Arrhenius(
                A = (2.6e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4470, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '(C4H81+O)',
            ),
        ],
    ),
)

entry(
    index = 996,
    label = "C8H16 + OH <=> PXC8H15 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(C4H81+O)',
    ),
    longDesc = 
u"""
(C4H81+O)
""",
)

entry(
    index = 997,
    label = "C8H16 + O2 <=> PXC8H15 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+OH)',
    ),
    longDesc = 
u"""
=(C3H8+OH)
""",
)

entry(
    index = 998,
    label = "C8H16 + HO2 <=> PXC8H15 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 999,
    label = "C8H16 + CH3 <=> PXC8H15 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.45, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+HO2)',
    ),
    longDesc = 
u"""
=(C4H81+HO2)
""",
)

entry(
    index = 1000,
    label = "PXC8H17 <=> C2H4 + PXC6H13",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.12e+11, 's^-1'), n=0.31, Ea=(27237.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.8e-57, 'cm^3/(mol*s)'),
            n = 23.463,
            Ea = (-602.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -2.46,
        T3 = (206, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)\nReactions of PXC8H17\nC2H4+PXC6H13 = PXC8H17                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!B\nBeta-scission Reactions of octyl radicals',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
Reactions of PXC8H17
C2H4+PXC6H13 = PXC8H17                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!B
Beta-scission Reactions of octyl radicals
""",
)

entry(
    index = 1001,
    label = "SXC8H17 <=> PXC5H11 + C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.03e+10, 's^-1'), n=0.84, Ea=(27820, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e-43, 'cm^3/(mol*s)'),
            n = 18.591,
            Ea = (-602.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -43.32,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAb !B',
    ),
    longDesc = 
u"""
08TSAb !B
""",
)

entry(
    index = 1002,
    label = "S2XC8H17 <=> pC4H9 + C4H81",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.04e+13, 's^-1'), n=0.04, Ea=(28493.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-43, 'cm^3/(mol*s)'),
            n = 18.43,
            Ea = (-602.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.47,
        T3 = (208, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAb !B',
    ),
    longDesc = 
u"""
08TSAb !B
""",
)

entry(
    index = 1003,
    label = "S2XC8H17 <=> C7H14 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.55e+09, 's^-1'), n=1.08, Ea=(29387.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.3e-46, 'cm^3/(mol*s)'),
            n = 19.133,
            Ea = (-602.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.36,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAb !B',
    ),
    longDesc = 
u"""
08TSAb !B
""",
)

entry(
    index = 1004,
    label = "S3XC8H17 <=> nC3H7 + C5H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAb !B',
    ),
    longDesc = 
u"""
08TSAb !B
""",
)

entry(
    index = 1005,
    label = "S3XC8H17 <=> C6H12 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.76e+09, 's^-1'), n=1.11, Ea=(27023.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.2e-43, 'cm^3/(mol*s)'),
            n = 18.276,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -30.04,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAb !B',
    ),
    longDesc = 
u"""
08TSAb !B
""",
)

entry(
    index = 1006,
    label = "PXC8H17 + H <=> NC8H18",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '08TSAb !B',
    ),
    longDesc = 
u"""
08TSAb !B
""",
)

entry(
    index = 1007,
    label = "PXC8H17 + H <=> PXC6H13 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12505, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)\nPXC8H17+H = PXC6H13+C2H5                     3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)
PXC8H17+H = PXC6H13+C2H5                     3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm
""",
)

entry(
    index = 1008,
    label = "PXC8H17 + H <=> C8H16 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)  1 atm\nPXC8H17+H = PXC6H13+C2H5                     3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)  1 atm
PXC8H17+H = PXC6H13+C2H5                     3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm
""",
)

entry(
    index = 1009,
    label = "PXC8H17 + O <=> PXC7H15 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)',
    ),
    longDesc = 
u"""
=(nC3H7+H)
""",
)

entry(
    index = 1010,
    label = "PXC8H17 + OH <=> C8H16 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O)',
    ),
    longDesc = 
u"""
=(nC3H7+O)
""",
)

entry(
    index = 1011,
    label = "PXC8H17 + O2 <=> C8H16 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+OH)',
    ),
    longDesc = 
u"""
=(nC3H7+OH)
""",
)

entry(
    index = 1012,
    label = "PXC8H17 + HO2 <=> PXC7H15 + OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O2)',
    ),
    longDesc = 
u"""
=(nC3H7+O2)
""",
)

entry(
    index = 1013,
    label = "PXC8H17 + HCO <=> NC8H18 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HO2)',
    ),
    longDesc = 
u"""
=(nC3H7+HO2)
""",
)

entry(
    index = 1014,
    label = "PXC8H17 + CH3 <=> C8H16 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HCO)',
    ),
    longDesc = 
u"""
=(nC3H7+HCO)
""",
)

entry(
    index = 1015,
    label = "SXC8H17 + H <=> NC8H18",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+58, 'cm^6/(mol^2*s)'),
            n = -12.08,
            Ea = (11263.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.649,
        T3 = (1213.1, 'K'),
        T1 = (1213.1, 'K'),
        T2 = (13369.7, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(nC3H7+CH3)\nReactions of SXC8H17\nPXC5H11+C3H6 = SXC8H17                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(nC3H7+CH3)
Reactions of SXC8H17
PXC5H11+C3H6 = SXC8H17                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 1016,
    label = "SXC8H17 + H <=> PXC6H13 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC8H17+H = PXC6H13+C2H5                     5.90E+23   -2.81  10009.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC8H17+H = PXC6H13+C2H5                     5.90E+23   -2.81  10009.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1017,
    label = "SXC8H17 + H <=> C8H16 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC8H17+H = PXC6H13+C2H5                     4.00E+24   -2.83  17542.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC8H17+H = PXC6H13+C2H5                     4.00E+24   -2.83  17542.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1018,
    label = "SXC8H17 + O <=> CH3CHO + PXC6H13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
""",
)

entry(
    index = 1019,
    label = "SXC8H17 + OH <=> C8H16 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O)',
    ),
    longDesc = 
u"""
=(iC3H7+O)
""",
)

entry(
    index = 1020,
    label = "SXC8H17 + O2 <=> C8H16 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH)',
    ),
    longDesc = 
u"""
=(iC3H7+OH)
""",
)

entry(
    index = 1021,
    label = "SXC8H17 + HO2 <=> CH3CHO + PXC6H13 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
""",
)

entry(
    index = 1022,
    label = "SXC8H17 + HCO <=> NC8H18 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2)',
    ),
    longDesc = 
u"""
=(iC3H7+HO2)
""",
)

entry(
    index = 1023,
    label = "SXC8H17 + CH3 <=> CH4 + C8H16",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HCO)',
    ),
    longDesc = 
u"""
=(iC3H7+HCO)
""",
)

entry(
    index = 1024,
    label = "S2XC8H17 + O2 <=> C8H16 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+CH3)\nReactions of S2XC8H17\npC4H9+C4H81 = S2XC8H17                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2\nC7H14+CH3(+M)= S2XC8H17(+M)                 1.70E+11    0.00   7403.6  ! =(C3H6+CH3)\nLOW  / 2.31E+28  -4.27   1831.0      /\nTROE / 0.565 60000.0   534.2  3007.2 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(iC3H7+CH3)
Reactions of S2XC8H17
pC4H9+C4H81 = S2XC8H17                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2
C7H14+CH3(+M)= S2XC8H17(+M)                 1.70E+11    0.00   7403.6  ! =(C3H6+CH3)
LOW  / 2.31E+28  -4.27   1831.0      /
TROE / 0.565 60000.0   534.2  3007.2 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 1025,
    label = "S3XC8H17 + O2 <=> C8H16 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S3XC8H17\nnC3H7+C5H10 = S3XC8H17                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2\nC6H12+C2H5 = S3XC8H17                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S3XC8H17
nC3H7+C5H10 = S3XC8H17                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2
C6H12+C2H5 = S3XC8H17                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2
""",
)

entry(
    index = 1026,
    label = "PXC7H15 + CH3 <=> NC8H18",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of NC8H18',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of NC8H18
""",
)

entry(
    index = 1027,
    label = "PXC6H13 + C2H5 <=> NC8H18",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(CH3+C2H5)',
    ),
    longDesc = 
u"""
=(CH3+C2H5)
""",
)

entry(
    index = 1028,
    label = "PXC5H11 + nC3H7 <=> NC8H18",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1029,
    label = "pC4H9 + pC4H9 <=> NC8H18",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1030,
    label = "NC8H18 + H <=> PXC8H17 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1031,
    label = "NC8H18 + H <=> SXC8H17 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)',
    ),
    longDesc = 
u"""
=(C3H8+H)
""",
)

entry(
    index = 1032,
    label = "NC8H18 + H <=> S2XC8H17 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2',
    ),
    longDesc = 
u"""
=(C3H8+H)*2
""",
)

entry(
    index = 1033,
    label = "NC8H18 + H <=> S3XC8H17 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2    EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2    EDames
""",
)

entry(
    index = 1034,
    label = "NC8H18 + O <=> PXC8H17 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5504, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2    EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2    EDames
""",
)

entry(
    index = 1035,
    label = "NC8H18 + O <=> SXC8H17 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW',
    ),
    longDesc = 
u"""
!BS 86/CW
""",
)

entry(
    index = 1036,
    label = "NC8H18 + O <=> S2XC8H17 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW',
    ),
    longDesc = 
u"""
!BS 86/CW
""",
)

entry(
    index = 1037,
    label = "NC8H18 + O <=> S3XC8H17 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW',
    ),
    longDesc = 
u"""
!BS 86/CW
""",
)

entry(
    index = 1038,
    label = "NC8H18 + OH <=> PXC8H17 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (974, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW',
    ),
    longDesc = 
u"""
!BS 86/CW
""",
)

entry(
    index = 1039,
    label = "NC8H18 + OH <=> SXC8H17 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-595.1, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1040,
    label = "NC8H18 + OH <=> S2XC8H17 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1351, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1041,
    label = "NC8H18 + OH <=> S3XC8H17 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1351, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1042,
    label = "NC8H18 + O2 <=> PXC8H17 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1043,
    label = "NC8H18 + O2 <=> SXC8H17 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 1044,
    label = "NC8H18 + O2 <=> S2XC8H17 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2
""",
)

entry(
    index = 1045,
    label = "NC8H18 + O2 <=> S3XC8H17 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2   EDames
""",
)

entry(
    index = 1046,
    label = "NC8H18 + HO2 <=> PXC8H17 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2   EDames
""",
)

entry(
    index = 1047,
    label = "NC8H18 + HO2 <=> SXC8H17 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)',
    ),
    longDesc = 
u"""
=(C3H8+HO2)
""",
)

entry(
    index = 1048,
    label = "NC8H18 + HO2 <=> S2XC8H17 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2
""",
)

entry(
    index = 1049,
    label = "NC8H18 + HO2 <=> S3XC8H17 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2  EDames
""",
)

entry(
    index = 1050,
    label = "NC8H18 + CH3 <=> PXC8H17 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2  EDames
""",
)

entry(
    index = 1051,
    label = "NC8H18 + CH3 <=> SXC8H17 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
""",
)

entry(
    index = 1052,
    label = "NC8H18 + CH3 <=> S2XC8H17 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2
""",
)

entry(
    index = 1053,
    label = "NC8H18 + CH3 <=> S3XC8H17 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2  EDames
""",
)

entry(
    index = 1054,
    label = "PXC9H17 + H <=> C9H18",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)*2  EDames\nReactions of PXC9H17\nPXC9H17 = C9H16+H                              2.48E+53  -12.30  52000.0  !=(C4H7)\nPXC9H17 = C9H16+H                              1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2  EDames
Reactions of PXC9H17
PXC9H17 = C9H16+H                              2.48E+53  -12.30  52000.0  !=(C4H7)
PXC9H17 = C9H16+H                              1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm
""",
)

entry(
    index = 1055,
    label = "PXC9H17 + H <=> CH3 + PXC8H15",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+H',
    ),
    longDesc = 
u"""
= nC3H7+H
""",
)

entry(
    index = 1056,
    label = "PXC9H17 + HO2 <=> CH2O + OH + PXC8H15",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H7+H)\nPXC9H17+H = C9H16+H2                           1.80E+12    0.00      0.0  != nC3H7+H\nPXC9H17+O2 = C9H16+HO2                         1.00E+11    0.00      0.0  !=(C4H7+O2)',
    ),
    longDesc = 
u"""
=(C4H7+H)
PXC9H17+H = C9H16+H2                           1.80E+12    0.00      0.0  != nC3H7+H
PXC9H17+O2 = C9H16+HO2                         1.00E+11    0.00      0.0  !=(C4H7+O2)
""",
)

entry(
    index = 1057,
    label = "PXC9H17 + HCO <=> C9H18 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HO2',
    ),
    longDesc = 
u"""
= nC3H7+HO2
""",
)

entry(
    index = 1058,
    label = "C2H4 + PXC7H13 <=> PXC9H17",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HCO\nPXC9H17+CH3 = C9H16+CH4                        1.10E+13    0.00      0.0  != nC3H7+CH3\nAlternative',
    ),
    longDesc = 
u"""
= nC3H7+HCO
PXC9H17+CH3 = C9H16+CH4                        1.10E+13    0.00      0.0  != nC3H7+CH3
Alternative
""",
)

entry(
    index = 1059,
    label = "C9H18 <=> PXC6H13 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+23, 's^-1'),
        n = -2.03,
        Ea = (74958, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H4+C2H5)*2\nReactions of C9H18\nC9H18+H(+M) = PXC9H19(+M)                    1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS\nLOW  / 6.26E+38  -6.66   7000.0      /\nTROE / 1.000  1000.0  1310.0 48097.0 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nC9H18+H(+M) = SXC9H19(+M)                    1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS\nLOW  / 8.70E+42  -7.50   4721.8      /\nTROE / 1.000  1000.0   645.4  6844.3 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(C2H4+C2H5)*2
Reactions of C9H18
C9H18+H(+M) = PXC9H19(+M)                    1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS
LOW  / 6.26E+38  -6.66   7000.0      /
TROE / 1.000  1000.0  1310.0 48097.0 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
C9H18+H(+M) = SXC9H19(+M)                    1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS
LOW  / 8.70E+42  -7.50   4721.8      /
TROE / 1.000  1000.0   645.4  6844.3 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 1060,
    label = "C9H18 <=> C6H12 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.08e+06, 's^-1'),
        n = 1.65,
        Ea = (53752, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 1061,
    label = "C9H18 + H <=> C2H4 + PXC7H15",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 1062,
    label = "C9H18 + H <=> C3H6 + PXC6H13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)',
    ),
    longDesc = 
u"""
=(C3H6+H)
""",
)

entry(
    index = 1063,
    label = "C9H18 + H <=> PXC9H17 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (650000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 1064,
    label = "C9H18 + O <=> PXC8H17 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+H)',
    ),
    longDesc = 
u"""
=(C4H81+H)
""",
)

entry(
    index = 1065,
    label = "C9H18 + O <=> PXC9H17 + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5760, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '=(C4H81+O)',
            ),
            Arrhenius(
                A = (2.6e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4470, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '(C4H81+O)',
            ),
        ],
    ),
)

entry(
    index = 1066,
    label = "C9H18 + OH <=> PXC9H17 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(C4H81+O)',
    ),
    longDesc = 
u"""
(C4H81+O)
""",
)

entry(
    index = 1067,
    label = "C9H18 + O2 <=> PXC9H17 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+OH)',
    ),
    longDesc = 
u"""
=(C3H8+OH)
""",
)

entry(
    index = 1068,
    label = "C9H18 + HO2 <=> PXC9H17 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 1069,
    label = "C9H18 + CH3 <=> PXC9H17 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.45, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+HO2)',
    ),
    longDesc = 
u"""
=(C4H81+HO2)
""",
)

entry(
    index = 1070,
    label = "PXC9H19 <=> C2H4 + PXC7H15",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.12e+11, 's^-1'), n=0.31, Ea=(27237.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.8e-57, 'cm^3/(mol*s)'),
            n = 23.463,
            Ea = (-602.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -2.46,
        T3 = (206, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)\nReactions of PXC9H19\nC2H4+PXC7H15 = PXC9H19                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS\nBeta-scission Reactions of nonyl radicals',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
Reactions of PXC9H19
C2H4+PXC7H15 = PXC9H19                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS
Beta-scission Reactions of nonyl radicals
""",
)

entry(
    index = 1071,
    label = "SXC9H19 <=> C3H6 + PXC6H13",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.03e+10, 's^-1'), n=0.84, Ea=(27820, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e-43, 'cm^3/(mol*s)'),
            n = 18.591,
            Ea = (-602.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -43.32,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1072,
    label = "S2XC9H19 <=> PXC5H11 + C4H81",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.04e+13, 's^-1'), n=0.04, Ea=(28493.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-43, 'cm^3/(mol*s)'),
            n = 18.43,
            Ea = (-602.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.47,
        T3 = (208, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1073,
    label = "S2XC9H19 <=> C8H16 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.55e+09, 's^-1'), n=1.08, Ea=(29387.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.3e-46, 'cm^3/(mol*s)'),
            n = 19.133,
            Ea = (-602.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.36,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1074,
    label = "S3XC9H19 <=> pC4H9 + C5H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1075,
    label = "S3XC9H19 <=> C7H14 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.76e+09, 's^-1'), n=1.11, Ea=(27023.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.2e-43, 'cm^3/(mol*s)'),
            n = 18.276,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -30.04,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1076,
    label = "S4XC9H19 <=> nC3H7 + C6H12",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.1e+12, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.2e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1077,
    label = "PXC9H19 + H <=> NC9H20",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb * 2 !BS',
    ),
    longDesc = 
u"""
From 08TSAb * 2 !BS
""",
)

entry(
    index = 1078,
    label = "PXC9H19 + H <=> PXC7H15 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12505, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)\nPXC9H19+H = PXC7H15+C2H5                     3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)
PXC9H19+H = PXC7H15+C2H5                     3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm
""",
)

entry(
    index = 1079,
    label = "PXC9H19 + H <=> C9H18 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)  1 atm\nPXC9H19+H = PXC7H15+C2H5                     3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)  1 atm
PXC9H19+H = PXC7H15+C2H5                     3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm
""",
)

entry(
    index = 1080,
    label = "PXC9H19 + O <=> PXC8H17 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)',
    ),
    longDesc = 
u"""
=(nC3H7+H)
""",
)

entry(
    index = 1081,
    label = "PXC9H19 + OH <=> C9H18 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O)',
    ),
    longDesc = 
u"""
=(nC3H7+O)
""",
)

entry(
    index = 1082,
    label = "PXC9H19 + O2 <=> C9H18 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+OH)',
    ),
    longDesc = 
u"""
=(nC3H7+OH)
""",
)

entry(
    index = 1083,
    label = "PXC9H19 + HO2 <=> PXC8H17 + OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O2)',
    ),
    longDesc = 
u"""
=(nC3H7+O2)
""",
)

entry(
    index = 1084,
    label = "PXC9H19 + HCO <=> NC9H20 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HO2)',
    ),
    longDesc = 
u"""
=(nC3H7+HO2)
""",
)

entry(
    index = 1085,
    label = "PXC9H19 + CH3 <=> C9H18 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HCO)',
    ),
    longDesc = 
u"""
=(nC3H7+HCO)
""",
)

entry(
    index = 1086,
    label = "SXC9H19 + H <=> NC9H20",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+58, 'cm^6/(mol^2*s)'),
            n = -12.08,
            Ea = (11263.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.649,
        T3 = (1213.1, 'K'),
        T1 = (1213.1, 'K'),
        T2 = (13369.7, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(nC3H7+CH3)\nReactions of SXC9H19\nC3H6+PXC6H13 = SXC9H19                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS',
    ),
    longDesc = 
u"""
=(nC3H7+CH3)
Reactions of SXC9H19
C3H6+PXC6H13 = SXC9H19                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS
""",
)

entry(
    index = 1087,
    label = "SXC9H19 + H <=> PXC7H15 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC9H19+H = PXC7H15+C2H5                     5.90E+23   -2.81  10009.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC9H19+H = PXC7H15+C2H5                     5.90E+23   -2.81  10009.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1088,
    label = "SXC9H19 + H <=> C9H18 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC9H19+H = PXC7H15+C2H5                     4.00E+24   -2.83  17542.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC9H19+H = PXC7H15+C2H5                     4.00E+24   -2.83  17542.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1089,
    label = "SXC9H19 + O <=> CH3CHO + PXC7H15",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
""",
)

entry(
    index = 1090,
    label = "SXC9H19 + OH <=> C9H18 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O)',
    ),
    longDesc = 
u"""
=(iC3H7+O)
""",
)

entry(
    index = 1091,
    label = "SXC9H19 + O2 <=> C9H18 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH)',
    ),
    longDesc = 
u"""
=(iC3H7+OH)
""",
)

entry(
    index = 1092,
    label = "SXC9H19 + HO2 <=> CH3CHO + PXC7H15 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
""",
)

entry(
    index = 1093,
    label = "SXC9H19 + HCO <=> NC9H20 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2)',
    ),
    longDesc = 
u"""
=(iC3H7+HO2)
""",
)

entry(
    index = 1094,
    label = "SXC9H19 + CH3 <=> CH4 + C9H18",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HCO)',
    ),
    longDesc = 
u"""
=(iC3H7+HCO)
""",
)

entry(
    index = 1095,
    label = "S2XC9H19 + O2 <=> C9H18 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+CH3)\nReactions of S2XC9H19\nPXC5H11+C4H81 = S2XC9H19                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nC8H16+CH3(+M)= S2XC9H19(+M)                 1.70E+11    0.00   7403.6  ! =(C3H6+CH3)!BS\nLOW  / 2.31E+28  -4.27   1831.0      /\nTROE / 0.565 60000.0   534.2  3007.2 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(iC3H7+CH3)
Reactions of S2XC9H19
PXC5H11+C4H81 = S2XC9H19                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
C8H16+CH3(+M)= S2XC9H19(+M)                 1.70E+11    0.00   7403.6  ! =(C3H6+CH3)!BS
LOW  / 2.31E+28  -4.27   1831.0      /
TROE / 0.565 60000.0   534.2  3007.2 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 1096,
    label = "S3XC9H19 + O2 <=> C9H18 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S3XC9H19\npC4H9+C5H10 = S3XC9H19                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nC7H14+C2H5 = S3XC9H19                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S3XC9H19
pC4H9+C5H10 = S3XC9H19                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
C7H14+C2H5 = S3XC9H19                       3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 1097,
    label = "S4XC9H19 + O2 <=> C9H18 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S4XC9H19\nnC3H7+C6H12 = S4XC9H19                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S4XC9H19
nC3H7+C6H12 = S4XC9H19                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 1098,
    label = "PXC8H17 + CH3 <=> NC9H20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of NC9H20',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of NC9H20
""",
)

entry(
    index = 1099,
    label = "PXC7H15 + C2H5 <=> NC9H20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(CH3+C2H5)',
    ),
    longDesc = 
u"""
=(CH3+C2H5)
""",
)

entry(
    index = 1100,
    label = "PXC6H13 + nC3H7 <=> NC9H20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1101,
    label = "PXC5H11 + pC4H9 <=> NC9H20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1102,
    label = "NC9H20 + H <=> PXC9H19 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1103,
    label = "NC9H20 + H <=> SXC9H19 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)',
    ),
    longDesc = 
u"""
=(C3H8+H)
""",
)

entry(
    index = 1104,
    label = "NC9H20 + H <=> S2XC9H19 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2',
    ),
    longDesc = 
u"""
=(C3H8+H)*2
""",
)

entry(
    index = 1105,
    label = "NC9H20 + H <=> S3XC9H19 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2   EDames
""",
)

entry(
    index = 1106,
    label = "NC9H20 + H <=> S4XC9H19 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2   EDames
""",
)

entry(
    index = 1107,
    label = "NC9H20 + O <=> PXC9H19 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5504, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)     EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)     EDames
""",
)

entry(
    index = 1108,
    label = "NC9H20 + O <=> SXC9H19 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1109,
    label = "NC9H20 + O <=> S2XC9H19 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1110,
    label = "NC9H20 + O <=> S3XC9H19 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1111,
    label = "NC9H20 + O <=> S4XC9H19 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (115000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1112,
    label = "NC9H20 + OH <=> PXC9H19 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (974, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1113,
    label = "NC9H20 + OH <=> SXC9H19 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1114,
    label = "NC9H20 + OH <=> S2XC9H19 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1371, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1115,
    label = "NC9H20 + OH <=> S3XC9H19 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1371, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1116,
    label = "NC9H20 + OH <=> S4XC9H19 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1371, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1117,
    label = "NC9H20 + O2 <=> PXC9H19 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1118,
    label = "NC9H20 + O2 <=> SXC9H19 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 1119,
    label = "NC9H20 + O2 <=> S2XC9H19 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2
""",
)

entry(
    index = 1120,
    label = "NC9H20 + O2 <=> S3XC9H19 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2  EDames
""",
)

entry(
    index = 1121,
    label = "NC9H20 + O2 <=> S4XC9H19 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2  EDames
""",
)

entry(
    index = 1122,
    label = "NC9H20 + HO2 <=> PXC9H19 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)    EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)    EDames
""",
)

entry(
    index = 1123,
    label = "NC9H20 + HO2 <=> SXC9H19 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)',
    ),
    longDesc = 
u"""
=(C3H8+HO2)
""",
)

entry(
    index = 1124,
    label = "NC9H20 + HO2 <=> S2XC9H19 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2
""",
)

entry(
    index = 1125,
    label = "NC9H20 + HO2 <=> S3XC9H19 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2 EDames
""",
)

entry(
    index = 1126,
    label = "NC9H20 + HO2 <=> S4XC9H19 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9500, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2 EDames
""",
)

entry(
    index = 1127,
    label = "NC9H20 + CH3 <=> PXC9H19 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)   EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)   EDames
""",
)

entry(
    index = 1128,
    label = "NC9H20 + CH3 <=> SXC9H19 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
""",
)

entry(
    index = 1129,
    label = "NC9H20 + CH3 <=> S2XC9H19 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2
""",
)

entry(
    index = 1130,
    label = "NC9H20 + CH3 <=> S3XC9H19 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2 EDames
""",
)

entry(
    index = 1131,
    label = "NC9H20 + CH3 <=> S4XC9H19 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2 EDames
""",
)

entry(
    index = 1132,
    label = "PXC10H19 + H <=> C10H20",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)   EDames\nReactions of PXC10H19\nPXC10H19 = C10H18+H                            2.48E+53  -12.30  52000.0  !=(C4H7)\nPXC10H19 = C10H18+H                            1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm',
    ),
    longDesc = 
u"""
=(C3H8+CH3)   EDames
Reactions of PXC10H19
PXC10H19 = C10H18+H                            2.48E+53  -12.30  52000.0  !=(C4H7)
PXC10H19 = C10H18+H                            1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm
""",
)

entry(
    index = 1133,
    label = "PXC10H19 + H <=> CH3 + PXC9H17",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+H',
    ),
    longDesc = 
u"""
= nC3H7+H
""",
)

entry(
    index = 1134,
    label = "PXC10H19 + HO2 <=> CH2O + OH + PXC9H17",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H7+H)\nPXC10H19+H = C10H18+H2                         1.80E+12    0.00      0.0  != nC3H7+H\nPXC10H19+O2 = C10H18+HO2                       1.00E+11    0.00      0.0  !=(C4H7+O2)',
    ),
    longDesc = 
u"""
=(C4H7+H)
PXC10H19+H = C10H18+H2                         1.80E+12    0.00      0.0  != nC3H7+H
PXC10H19+O2 = C10H18+HO2                       1.00E+11    0.00      0.0  !=(C4H7+O2)
""",
)

entry(
    index = 1135,
    label = "PXC10H19 + HCO <=> C10H20 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HO2',
    ),
    longDesc = 
u"""
= nC3H7+HO2
""",
)

entry(
    index = 1136,
    label = "C2H4 + PXC8H15 <=> PXC10H19",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HCO\nPXC10H19+CH3 = C10H18+CH4                      1.10E+13    0.00      0.0  != nC3H7+CH3\nAlternative',
    ),
    longDesc = 
u"""
= nC3H7+HCO
PXC10H19+CH3 = C10H18+CH4                      1.10E+13    0.00      0.0  != nC3H7+CH3
Alternative
""",
)

entry(
    index = 1137,
    label = "C10H20 <=> PXC7H15 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+23, 's^-1'),
        n = -2.03,
        Ea = (74958, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H4+C2H5)*2\nReactions of C10H20\nC10H20+H(+M) = PXC10H21(+M)                  1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS\nLOW  / 6.26E+38  -6.66   7000.0      /\nTROE / 1.000  1000.0  1310.0 48097.0 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nC10H20+H(+M) = SXC10H21(+M)                  1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS\nLOW  / 8.70E+42  -7.50   4721.8      /\nTROE / 1.000  1000.0   645.4  6844.3 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(C2H4+C2H5)*2
Reactions of C10H20
C10H20+H(+M) = PXC10H21(+M)                  1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS
LOW  / 6.26E+38  -6.66   7000.0      /
TROE / 1.000  1000.0  1310.0 48097.0 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
C10H20+H(+M) = SXC10H21(+M)                  1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS
LOW  / 8.70E+42  -7.50   4721.8      /
TROE / 1.000  1000.0   645.4  6844.3 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 1138,
    label = "C10H20 <=> C7H14 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.08e+06, 's^-1'),
        n = 1.65,
        Ea = (53752, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 1139,
    label = "C10H20 + H <=> C2H4 + PXC8H17",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 1140,
    label = "C10H20 + H <=> C3H6 + PXC7H15",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)',
    ),
    longDesc = 
u"""
=(C3H6+H)
""",
)

entry(
    index = 1141,
    label = "C10H20 + H <=> PXC10H19 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (650000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 1142,
    label = "C10H20 + O <=> PXC9H19 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+H)',
    ),
    longDesc = 
u"""
=(C4H81+H)
""",
)

entry(
    index = 1143,
    label = "C10H20 + O <=> PXC10H19 + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5760, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '=(C4H81+O)',
            ),
            Arrhenius(
                A = (2.6e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4470, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '(C4H81+O)',
            ),
        ],
    ),
)

entry(
    index = 1144,
    label = "C10H20 + OH <=> PXC10H19 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(C4H81+O)',
    ),
    longDesc = 
u"""
(C4H81+O)
""",
)

entry(
    index = 1145,
    label = "C10H20 + O2 <=> PXC10H19 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+OH)',
    ),
    longDesc = 
u"""
=(C3H8+OH)
""",
)

entry(
    index = 1146,
    label = "C10H20 + HO2 <=> PXC10H19 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 1147,
    label = "C10H20 + CH3 <=> PXC10H19 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.45, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+HO2)',
    ),
    longDesc = 
u"""
=(C4H81+HO2)
""",
)

entry(
    index = 1148,
    label = "PXC10H21 <=> C2H4 + PXC8H17",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.12e+11, 's^-1'), n=0.31, Ea=(27237.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.8e-57, 'cm^3/(mol*s)'),
            n = 23.463,
            Ea = (-602.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -2.46,
        T3 = (206, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)\nReactions of PXC10H21\nC2H4+PXC8H17 = PXC10H21                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nBeta-scission Reactions of decyl radicals',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
Reactions of PXC10H21
C2H4+PXC8H17 = PXC10H21                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
Beta-scission Reactions of decyl radicals
""",
)

entry(
    index = 1149,
    label = "SXC10H21 <=> C3H6 + PXC7H15",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.03e+10, 's^-1'), n=0.84, Ea=(27820, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e-43, 'cm^3/(mol*s)'),
            n = 18.591,
            Ea = (-602.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -43.32,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1150,
    label = "S2XC10H21 <=> PXC6H13 + C4H81",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.04e+13, 's^-1'), n=0.04, Ea=(28493.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-43, 'cm^3/(mol*s)'),
            n = 18.43,
            Ea = (-602.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.47,
        T3 = (208, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1151,
    label = "S2XC10H21 <=> C9H18 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.55e+09, 's^-1'), n=1.08, Ea=(29387.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.3e-46, 'cm^3/(mol*s)'),
            n = 19.133,
            Ea = (-602.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.36,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1152,
    label = "S3XC10H21 <=> PXC5H11 + C5H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1153,
    label = "S3XC10H21 <=> C8H16 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.76e+09, 's^-1'), n=1.11, Ea=(27023.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.2e-43, 'cm^3/(mol*s)'),
            n = 18.276,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -30.04,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1154,
    label = "S4XC10H21 <=> pC4H9 + C6H12",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1155,
    label = "S4XC10H21 <=> C7H14 + nC3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1156,
    label = "PXC10H21 + H <=> NC10H22",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1157,
    label = "PXC10H21 + H <=> PXC8H17 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12505, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)\nPXC10H21+H = PXC8H17+C2H5                    3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)
PXC10H21+H = PXC8H17+C2H5                    3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm
""",
)

entry(
    index = 1158,
    label = "PXC10H21 + H <=> C10H20 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)  1 atm\nPXC10H21+H = PXC8H17+C2H5                    3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)  1 atm
PXC10H21+H = PXC8H17+C2H5                    3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm
""",
)

entry(
    index = 1159,
    label = "PXC10H21 + O <=> PXC9H19 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)',
    ),
    longDesc = 
u"""
=(nC3H7+H)
""",
)

entry(
    index = 1160,
    label = "PXC10H21 + OH <=> C10H20 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O)',
    ),
    longDesc = 
u"""
=(nC3H7+O)
""",
)

entry(
    index = 1161,
    label = "PXC10H21 + O2 <=> C10H20 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+OH)',
    ),
    longDesc = 
u"""
=(nC3H7+OH)
""",
)

entry(
    index = 1162,
    label = "PXC10H21 + HO2 <=> PXC9H19 + OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O2)',
    ),
    longDesc = 
u"""
=(nC3H7+O2)
""",
)

entry(
    index = 1163,
    label = "PXC10H21 + HCO <=> NC10H22 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HO2)',
    ),
    longDesc = 
u"""
=(nC3H7+HO2)
""",
)

entry(
    index = 1164,
    label = "PXC10H21 + CH3 <=> C10H20 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HCO)',
    ),
    longDesc = 
u"""
=(nC3H7+HCO)
""",
)

entry(
    index = 1165,
    label = "SXC10H21 + H <=> NC10H22",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+58, 'cm^6/(mol^2*s)'),
            n = -12.08,
            Ea = (11263.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.649,
        T3 = (1213.1, 'K'),
        T1 = (1213.1, 'K'),
        T2 = (13369.7, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(nC3H7+CH3)\nReactions of SXC10H21\nC3H6+PXC7H15 = SXC10H21                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(nC3H7+CH3)
Reactions of SXC10H21
C3H6+PXC7H15 = SXC10H21                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 1166,
    label = "SXC10H21 + H <=> PXC8H17 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC10H21+H = PXC8H17+C2H5                    5.90E+23   -2.81  10009.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC10H21+H = PXC8H17+C2H5                    5.90E+23   -2.81  10009.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1167,
    label = "SXC10H21 + H <=> C10H20 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC10H21+H = PXC8H17+C2H5                    4.00E+24   -2.83  17542.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC10H21+H = PXC8H17+C2H5                    4.00E+24   -2.83  17542.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1168,
    label = "SXC10H21 + O <=> CH3CHO + PXC8H17",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
""",
)

entry(
    index = 1169,
    label = "SXC10H21 + OH <=> C10H20 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O)',
    ),
    longDesc = 
u"""
=(iC3H7+O)
""",
)

entry(
    index = 1170,
    label = "SXC10H21 + O2 <=> C10H20 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH)',
    ),
    longDesc = 
u"""
=(iC3H7+OH)
""",
)

entry(
    index = 1171,
    label = "SXC10H21 + HO2 <=> CH3CHO + PXC8H17 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
""",
)

entry(
    index = 1172,
    label = "SXC10H21 + HCO <=> NC10H22 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2)',
    ),
    longDesc = 
u"""
=(iC3H7+HO2)
""",
)

entry(
    index = 1173,
    label = "SXC10H21 + CH3 <=> CH4 + C10H20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HCO)',
    ),
    longDesc = 
u"""
=(iC3H7+HCO)
""",
)

entry(
    index = 1174,
    label = "S2XC10H21 + O2 <=> C10H20 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+CH3)\nReactions of S2XC10H21\nPXC6H13+C4H81 = S2XC10H21                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nC9H18+CH3(+M)= S2XC10H21(+M)                1.70E+11    0.00   7403.6  ! =(C3H6+CH3)!BS\nLOW  / 2.31E+28  -4.27   1831.0      /\nTROE / 0.565 60000.0   534.2  3007.2 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(iC3H7+CH3)
Reactions of S2XC10H21
PXC6H13+C4H81 = S2XC10H21                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
C9H18+CH3(+M)= S2XC10H21(+M)                1.70E+11    0.00   7403.6  ! =(C3H6+CH3)!BS
LOW  / 2.31E+28  -4.27   1831.0      /
TROE / 0.565 60000.0   534.2  3007.2 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 1175,
    label = "S3XC10H21 + O2 <=> C10H20 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S3XC10H21\nPXC5H11+C5H10 = S3XC10H21                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nC8H16+C2H5=S3XC10H21                        3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S3XC10H21
PXC5H11+C5H10 = S3XC10H21                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
C8H16+C2H5=S3XC10H21                        3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 1176,
    label = "S4XC10H21 + O2 <=> C10H20 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S4XC10H21\npC4H9+C6H12 = S4XC10H21                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nC7H14+nC3H7 = S4XC10H21                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S4XC10H21
pC4H9+C6H12 = S4XC10H21                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
C7H14+nC3H7 = S4XC10H21                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 1177,
    label = "PXC9H19 + CH3 <=> NC10H22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of NC10H22',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of NC10H22
""",
)

entry(
    index = 1178,
    label = "PXC8H17 + C2H5 <=> NC10H22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(CH3+C2H5)',
    ),
    longDesc = 
u"""
=(CH3+C2H5)
""",
)

entry(
    index = 1179,
    label = "PXC7H15 + nC3H7 <=> NC10H22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1180,
    label = "PXC6H13 + pC4H9 <=> NC10H22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1181,
    label = "PXC5H11 + PXC5H11 <=> NC10H22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1182,
    label = "NC10H22 + H <=> PXC10H21 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1183,
    label = "NC10H22 + H <=> SXC10H21 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)',
    ),
    longDesc = 
u"""
=(C3H8+H)
""",
)

entry(
    index = 1184,
    label = "NC10H22 + H <=> S2XC10H21 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2',
    ),
    longDesc = 
u"""
=(C3H8+H)*2
""",
)

entry(
    index = 1185,
    label = "NC10H22 + H <=> S3XC10H21 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2    EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2    EDames
""",
)

entry(
    index = 1186,
    label = "NC10H22 + H <=> S4XC10H21 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2    EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2    EDames
""",
)

entry(
    index = 1187,
    label = "NC10H22 + O <=> PXC10H21 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5504, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2    EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2    EDames
""",
)

entry(
    index = 1188,
    label = "NC10H22 + O <=> SXC10H21 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1189,
    label = "NC10H22 + O <=> S2XC10H21 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1190,
    label = "NC10H22 + O <=> S3XC10H21 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1191,
    label = "NC10H22 + O <=> S4XC10H21 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1192,
    label = "NC10H22 + OH <=> PXC10H21 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (974, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1193,
    label = "NC10H22 + OH <=> SXC10H21 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1194,
    label = "NC10H22 + OH <=> S2XC10H21 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1195,
    label = "NC10H22 + OH <=> S3XC10H21 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1196,
    label = "NC10H22 + OH <=> S4XC10H21 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1197,
    label = "NC10H22 + O2 <=> PXC10H21 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh',
    ),
    longDesc = 
u"""
!BS 91Coh
""",
)

entry(
    index = 1198,
    label = "NC10H22 + O2 <=> SXC10H21 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 1199,
    label = "NC10H22 + O2 <=> S2XC10H21 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2
""",
)

entry(
    index = 1200,
    label = "NC10H22 + O2 <=> S3XC10H21 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2   EDames
""",
)

entry(
    index = 1201,
    label = "NC10H22 + O2 <=> S4XC10H21 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2   EDames
""",
)

entry(
    index = 1202,
    label = "NC10H22 + HO2 <=> PXC10H21 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2   EDames
""",
)

entry(
    index = 1203,
    label = "NC10H22 + HO2 <=> SXC10H21 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)',
    ),
    longDesc = 
u"""
=(C3H8+HO2)
""",
)

entry(
    index = 1204,
    label = "NC10H22 + HO2 <=> S2XC10H21 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2
""",
)

entry(
    index = 1205,
    label = "NC10H22 + HO2 <=> S3XC10H21 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2  EDames
""",
)

entry(
    index = 1206,
    label = "NC10H22 + HO2 <=> S4XC10H21 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2  EDames
""",
)

entry(
    index = 1207,
    label = "NC10H22 + CH3 <=> PXC10H21 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2  EDames
""",
)

entry(
    index = 1208,
    label = "NC10H22 + CH3 <=> SXC10H21 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
""",
)

entry(
    index = 1209,
    label = "NC10H22 + CH3 <=> S2XC10H21 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2
""",
)

entry(
    index = 1210,
    label = "NC10H22 + CH3 <=> S3XC10H21 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2  EDames
""",
)

entry(
    index = 1211,
    label = "NC10H22 + CH3 <=> S4XC10H21 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2  EDames
""",
)

entry(
    index = 1212,
    label = "PXC11H21 + H <=> C11H22",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)*2  EDames\nReactions of PXC11H21\nPXC11H21 = C11H20+H                            2.48E+53  -12.30  52000.0  !=(C4H7)\nPXC11H21 = C11H20+H                            1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2  EDames
Reactions of PXC11H21
PXC11H21 = C11H20+H                            2.48E+53  -12.30  52000.0  !=(C4H7)
PXC11H21 = C11H20+H                            1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm
""",
)

entry(
    index = 1213,
    label = "PXC11H21 + H <=> CH3 + PXC10H19",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+H',
    ),
    longDesc = 
u"""
= nC3H7+H
""",
)

entry(
    index = 1214,
    label = "PXC11H21 + HO2 <=> CH2O + OH + PXC10H19",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H7+H)\nPXC11H21+H = C11H20+H2                         1.80E+12    0.00      0.0  != nC3H7+H\nPXC11H21+O2 = C11H20+HO2                       1.00E+11    0.00      0.0  !=(C4H7+O2)',
    ),
    longDesc = 
u"""
=(C4H7+H)
PXC11H21+H = C11H20+H2                         1.80E+12    0.00      0.0  != nC3H7+H
PXC11H21+O2 = C11H20+HO2                       1.00E+11    0.00      0.0  !=(C4H7+O2)
""",
)

entry(
    index = 1215,
    label = "PXC11H21 + HCO <=> C11H22 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HO2',
    ),
    longDesc = 
u"""
= nC3H7+HO2
""",
)

entry(
    index = 1216,
    label = "C2H4 + PXC9H17 <=> PXC11H21",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HCO\nPXC11H21+CH3 = C11H20+CH4                      1.10E+13    0.00      0.0  != nC3H7+CH3\nAlternative',
    ),
    longDesc = 
u"""
= nC3H7+HCO
PXC11H21+CH3 = C11H20+CH4                      1.10E+13    0.00      0.0  != nC3H7+CH3
Alternative
""",
)

entry(
    index = 1217,
    label = "C11H22 <=> PXC8H17 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+23, 's^-1'),
        n = -2.03,
        Ea = (74958, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H4+C2H5)*2\nReactions of C11H22\nC11H22+H(+M) = PXC11H23(+M)                  1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS\nLOW  / 6.26E+38  -6.66   7000.0      /\nTROE / 1.000  1000.0  1310.0 48097.0 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nC11H22+H(+M) = SXC11H23(+M)                  1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS\nLOW  / 8.70E+42  -7.50   4721.8      /\nTROE / 1.000  1000.0   645.4  6844.3 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(C2H4+C2H5)*2
Reactions of C11H22
C11H22+H(+M) = PXC11H23(+M)                  1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS
LOW  / 6.26E+38  -6.66   7000.0      /
TROE / 1.000  1000.0  1310.0 48097.0 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
C11H22+H(+M) = SXC11H23(+M)                  1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS
LOW  / 8.70E+42  -7.50   4721.8      /
TROE / 1.000  1000.0   645.4  6844.3 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 1218,
    label = "C11H22 <=> C8H16 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.08e+06, 's^-1'),
        n = 1.65,
        Ea = (53752, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 1219,
    label = "C11H22 + H <=> C2H4 + PXC9H19",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 1220,
    label = "C11H22 + H <=> C3H6 + PXC8H17",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)',
    ),
    longDesc = 
u"""
=(C3H6+H)
""",
)

entry(
    index = 1221,
    label = "C11H22 + H <=> PXC11H21 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (650000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 1222,
    label = "C11H22 + O <=> PXC10H21 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+H)',
    ),
    longDesc = 
u"""
=(C4H81+H)
""",
)

entry(
    index = 1223,
    label = "C11H22 + O <=> PXC11H21 + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5760, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '=(C4H81+O)',
            ),
            Arrhenius(
                A = (2.6e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4470, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '(C4H81+O)',
            ),
        ],
    ),
)

entry(
    index = 1224,
    label = "C11H22 + OH <=> PXC11H21 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(C4H81+O)',
    ),
    longDesc = 
u"""
(C4H81+O)
""",
)

entry(
    index = 1225,
    label = "C11H22 + O2 <=> PXC11H21 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+OH)',
    ),
    longDesc = 
u"""
=(C3H8+OH)
""",
)

entry(
    index = 1226,
    label = "C11H22 + HO2 <=> PXC11H21 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 1227,
    label = "C11H22 + CH3 <=> PXC11H21 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.45, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+HO2)',
    ),
    longDesc = 
u"""
=(C4H81+HO2)
""",
)

entry(
    index = 1228,
    label = "PXC11H23 <=> C2H4 + PXC9H19",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.12e+11, 's^-1'), n=0.31, Ea=(27237.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.8e-57, 'cm^3/(mol*s)'),
            n = 23.463,
            Ea = (-602.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -2.46,
        T3 = (206, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)\nReactions of PXC11H23\nC2H4+PXC9H19 = PXC11H23                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nBeta-scission Reactions of undecyl radicals',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
Reactions of PXC11H23
C2H4+PXC9H19 = PXC11H23                      3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
Beta-scission Reactions of undecyl radicals
""",
)

entry(
    index = 1229,
    label = "SXC11H23 <=> PXC8H17 + C3H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.03e+10, 's^-1'), n=0.84, Ea=(27820, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e-43, 'cm^3/(mol*s)'),
            n = 18.591,
            Ea = (-602.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -43.32,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1230,
    label = "S2XC11H23 <=> PXC7H15 + C4H81",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.04e+13, 's^-1'), n=0.04, Ea=(28493.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-43, 'cm^3/(mol*s)'),
            n = 18.43,
            Ea = (-602.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.47,
        T3 = (208, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1231,
    label = "S2XC11H23 <=> C10H20 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.55e+09, 's^-1'), n=1.08, Ea=(29387.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.3e-46, 'cm^3/(mol*s)'),
            n = 19.133,
            Ea = (-602.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.36,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1232,
    label = "S3XC11H23 <=> PXC6H13 + C5H10",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1233,
    label = "S3XC11H23 <=> C9H18 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.76e+09, 's^-1'), n=1.11, Ea=(27023.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.2e-43, 'cm^3/(mol*s)'),
            n = 18.276,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -30.04,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1234,
    label = "S4XC11H23 <=> PXC5H11 + C6H12",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1235,
    label = "S4XC11H23 <=> C8H16 + nC3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1236,
    label = "S5XC11H23 <=> pC4H9 + C7H14",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.1e+12, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.2e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1237,
    label = "PXC11H23 + H <=> NC11H24",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb * 2 !BS',
    ),
    longDesc = 
u"""
From 08TSAb * 2 !BS
""",
)

entry(
    index = 1238,
    label = "PXC11H23 + H <=> PXC9H19 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12505, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)\nPXC11H23+H = PXC9H19+C2H5                    3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)
PXC11H23+H = PXC9H19+C2H5                    3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm
""",
)

entry(
    index = 1239,
    label = "PXC11H23 + H <=> C11H22 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)  1 atm\nPXC11H23+H = PXC9H19+C2H5                    3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)  1 atm
PXC11H23+H = PXC9H19+C2H5                    3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm
""",
)

entry(
    index = 1240,
    label = "PXC11H23 + O <=> PXC10H21 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)',
    ),
    longDesc = 
u"""
=(nC3H7+H)
""",
)

entry(
    index = 1241,
    label = "PXC11H23 + OH <=> C11H22 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O)',
    ),
    longDesc = 
u"""
=(nC3H7+O)
""",
)

entry(
    index = 1242,
    label = "PXC11H23 + O2 <=> C11H22 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+OH)',
    ),
    longDesc = 
u"""
=(nC3H7+OH)
""",
)

entry(
    index = 1243,
    label = "PXC11H23 + HO2 <=> PXC10H21 + OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O2)',
    ),
    longDesc = 
u"""
=(nC3H7+O2)
""",
)

entry(
    index = 1244,
    label = "PXC11H23 + HCO <=> NC11H24 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HO2)',
    ),
    longDesc = 
u"""
=(nC3H7+HO2)
""",
)

entry(
    index = 1245,
    label = "PXC11H23 + CH3 <=> C11H22 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HCO)',
    ),
    longDesc = 
u"""
=(nC3H7+HCO)
""",
)

entry(
    index = 1246,
    label = "SXC11H23 + H <=> NC11H24",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+58, 'cm^6/(mol^2*s)'),
            n = -12.08,
            Ea = (11263.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.649,
        T3 = (1213.1, 'K'),
        T1 = (1213.1, 'K'),
        T2 = (13369.7, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(nC3H7+CH3)\nReactions of SXC11H23\nPXC8H17+C3H6 = SXC11H23                     3.00E+11    0.00   7300.0!BS',
    ),
    longDesc = 
u"""
=(nC3H7+CH3)
Reactions of SXC11H23
PXC8H17+C3H6 = SXC11H23                     3.00E+11    0.00   7300.0!BS
""",
)

entry(
    index = 1247,
    label = "SXC11H23 + H <=> PXC9H19 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC11H23+H = PXC9H19+C2H5                    5.90E+23   -2.81  10009.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC11H23+H = PXC9H19+C2H5                    5.90E+23   -2.81  10009.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1248,
    label = "SXC11H23 + H <=> C11H22 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC11H23+H = PXC9H19+C2H5                    4.00E+24   -2.83  17542.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC11H23+H = PXC9H19+C2H5                    4.00E+24   -2.83  17542.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1249,
    label = "SXC11H23 + O <=> CH3CHO + PXC9H19",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
""",
)

entry(
    index = 1250,
    label = "SXC11H23 + OH <=> C11H22 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O)',
    ),
    longDesc = 
u"""
=(iC3H7+O)
""",
)

entry(
    index = 1251,
    label = "SXC11H23 + O2 <=> C11H22 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH)',
    ),
    longDesc = 
u"""
=(iC3H7+OH)
""",
)

entry(
    index = 1252,
    label = "SXC11H23 + HO2 <=> CH3CHO + PXC9H19 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
""",
)

entry(
    index = 1253,
    label = "SXC11H23 + HCO <=> NC11H24 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2)',
    ),
    longDesc = 
u"""
=(iC3H7+HO2)
""",
)

entry(
    index = 1254,
    label = "SXC11H23 + CH3 <=> CH4 + C11H22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HCO)',
    ),
    longDesc = 
u"""
=(iC3H7+HCO)
""",
)

entry(
    index = 1255,
    label = "S2XC11H23 + O2 <=> C11H22 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+CH3)\nReactions of S2XC11H23\nPXC7H15+C4H81 = S2XC11H23                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nC10H20+CH3(+M)= S2XC11H23(+M)               1.70E+11    0.00   7403.6  ! =(C3H6+CH3)!BS\nLOW  / 2.31E+28  -4.27   1831.0      /\nTROE / 0.565 60000.0   534.2  3007.2 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(iC3H7+CH3)
Reactions of S2XC11H23
PXC7H15+C4H81 = S2XC11H23                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
C10H20+CH3(+M)= S2XC11H23(+M)               1.70E+11    0.00   7403.6  ! =(C3H6+CH3)!BS
LOW  / 2.31E+28  -4.27   1831.0      /
TROE / 0.565 60000.0   534.2  3007.2 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 1256,
    label = "S3XC11H23 + O2 <=> C11H22 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S3XC11H23\nPXC6H13+C5H10 = S3XC11H23                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS\nC9H18+C2H5=S3XC11H23                        3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S3XC11H23
PXC6H13+C5H10 = S3XC11H23                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS
C9H18+C2H5=S3XC11H23                        3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS
""",
)

entry(
    index = 1257,
    label = "S4XC11H23 + O2 <=> C11H22 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S4XC11H23\nPXC5H11+C6H12 = S4XC11H23                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS\nC8H16+nC3H7 = S4XC11H23                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S4XC11H23
PXC5H11+C6H12 = S4XC11H23                   3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS
C8H16+nC3H7 = S4XC11H23                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS
""",
)

entry(
    index = 1258,
    label = "S5XC11H23 + O2 <=> C11H22 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S5XC11H23\npC4H9+C7H14 = S5XC11H23                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S5XC11H23
pC4H9+C7H14 = S5XC11H23                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS
""",
)

entry(
    index = 1259,
    label = "PXC10H21 + CH3 <=> NC11H24",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of NC11H24',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of NC11H24
""",
)

entry(
    index = 1260,
    label = "PXC9H19 + C2H5 <=> NC11H24",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(CH3+C2H5)',
    ),
    longDesc = 
u"""
=(CH3+C2H5)
""",
)

entry(
    index = 1261,
    label = "PXC8H17 + nC3H7 <=> NC11H24",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1262,
    label = "PXC7H15 + pC4H9 <=> NC11H24",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1263,
    label = "PXC6H13 + PXC5H11 <=> NC11H24",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1264,
    label = "NC11H24 + H <=> PXC11H23 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1265,
    label = "NC11H24 + H <=> SXC11H23 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)',
    ),
    longDesc = 
u"""
=(C3H8+H)
""",
)

entry(
    index = 1266,
    label = "NC11H24 + H <=> S2XC11H23 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2',
    ),
    longDesc = 
u"""
=(C3H8+H)*2
""",
)

entry(
    index = 1267,
    label = "NC11H24 + H <=> S3XC11H23 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2   EDames
""",
)

entry(
    index = 1268,
    label = "NC11H24 + H <=> S4XC11H23 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2   EDames
""",
)

entry(
    index = 1269,
    label = "NC11H24 + H <=> S5XC11H23 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)*2   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)*2   EDames
""",
)

entry(
    index = 1270,
    label = "NC11H24 + O <=> PXC11H23 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5504, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)     EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)     EDames
""",
)

entry(
    index = 1271,
    label = "NC11H24 + O <=> SXC11H23 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1272,
    label = "NC11H24 + O <=> S2XC11H23 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1273,
    label = "NC11H24 + O <=> S3XC11H23 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1274,
    label = "NC11H24 + O <=> S4XC11H23 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1275,
    label = "NC11H24 + O <=> S5XC11H23 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (125000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1276,
    label = "NC11H24 + OH <=> PXC11H23 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (974, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1277,
    label = "NC11H24 + OH <=> SXC11H23 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1278,
    label = "NC11H24 + OH <=> S2XC11H23 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1279,
    label = "NC11H24 + OH <=> S3XC11H23 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1280,
    label = "NC11H24 + OH <=> S4XC11H23 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1281,
    label = "NC11H24 + OH <=> S5XC11H23 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1282,
    label = "NC11H24 + O2 <=> PXC11H23 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1283,
    label = "NC11H24 + O2 <=> SXC11H23 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 1284,
    label = "NC11H24 + O2 <=> S2XC11H23 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2
""",
)

entry(
    index = 1285,
    label = "NC11H24 + O2 <=> S3XC11H23 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2  EDames
""",
)

entry(
    index = 1286,
    label = "NC11H24 + O2 <=> S4XC11H23 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2  EDames
""",
)

entry(
    index = 1287,
    label = "NC11H24 + O2 <=> S5XC11H23 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)*2  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)*2  EDames
""",
)

entry(
    index = 1288,
    label = "NC11H24 + HO2 <=> PXC11H23 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)    EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)    EDames
""",
)

entry(
    index = 1289,
    label = "NC11H24 + HO2 <=> SXC11H23 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)',
    ),
    longDesc = 
u"""
=(C3H8+HO2)
""",
)

entry(
    index = 1290,
    label = "NC11H24 + HO2 <=> S2XC11H23 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2
""",
)

entry(
    index = 1291,
    label = "NC11H24 + HO2 <=> S3XC11H23 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2 EDames
""",
)

entry(
    index = 1292,
    label = "NC11H24 + HO2 <=> S4XC11H23 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2 EDames
""",
)

entry(
    index = 1293,
    label = "NC11H24 + HO2 <=> S5XC11H23 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9500, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)*2 EDames
""",
)

entry(
    index = 1294,
    label = "NC11H24 + CH3 <=> PXC11H23 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)   EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2)   EDames
""",
)

entry(
    index = 1295,
    label = "NC11H24 + CH3 <=> SXC11H23 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
""",
)

entry(
    index = 1296,
    label = "NC11H24 + CH3 <=> S2XC11H23 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2
""",
)

entry(
    index = 1297,
    label = "NC11H24 + CH3 <=> S3XC11H23 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2 EDames
""",
)

entry(
    index = 1298,
    label = "NC11H24 + CH3 <=> S4XC11H23 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2 EDames
""",
)

entry(
    index = 1299,
    label = "NC11H24 + CH3 <=> S5XC11H23 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3)*2 EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3)*2 EDames
""",
)

entry(
    index = 1300,
    label = "PXC12H23 + H <=> C12H24",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)   EDames\nReactions of PXC12H23\nPXC12H23 = C12H22+H                            2.48E+53  -12.30  52000.0  !=(C4H7)\nPXC12H23 = C12H22+H                            1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm',
    ),
    longDesc = 
u"""
=(C3H8+CH3)   EDames
Reactions of PXC12H23
PXC12H23 = C12H22+H                            2.48E+53  -12.30  52000.0  !=(C4H7)
PXC12H23 = C12H22+H                            1.85E+48  -10.50  51770.0  !=(C4H7) 10 atm
""",
)

entry(
    index = 1301,
    label = "PXC12H23 + H <=> CH3 + PXC11H21",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^3/(mol*s)'),
        n = -2,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+H',
    ),
    longDesc = 
u"""
= nC3H7+H
""",
)

entry(
    index = 1302,
    label = "PXC12H23 + HO2 <=> CH2O + OH + PXC11H21",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H7+H)\nPXC12H23+H = C12H22+H2                         1.80E+12    0.00      0.0  != nC3H7+H\nPXC12H23+O2 = C12H22+HO2                       1.00E+11    0.00      0.0  !=(C4H7+O2)',
    ),
    longDesc = 
u"""
=(C4H7+H)
PXC12H23+H = C12H22+H2                         1.80E+12    0.00      0.0  != nC3H7+H
PXC12H23+O2 = C12H22+HO2                       1.00E+11    0.00      0.0  !=(C4H7+O2)
""",
)

entry(
    index = 1303,
    label = "PXC12H23 + HCO <=> C12H24 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HO2',
    ),
    longDesc = 
u"""
= nC3H7+HO2
""",
)

entry(
    index = 1304,
    label = "C2H4 + PXC10H19 <=> PXC12H23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '= nC3H7+HCO\nPXC12H23+CH3 = C12H22+CH4                      1.10E+13    0.00      0.0  != nC3H7+CH3\nAlternative',
    ),
    longDesc = 
u"""
= nC3H7+HCO
PXC12H23+CH3 = C12H22+CH4                      1.10E+13    0.00      0.0  != nC3H7+CH3
Alternative
""",
)

entry(
    index = 1305,
    label = "C12H24 <=> PXC9H19 + aC3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+23, 's^-1'),
        n = -2.03,
        Ea = (74958, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H4+C2H5)*2\nReactions of C12H24\nC12H24+H(+M) = PXC12H25(+M)                  1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS\nLOW  / 6.26E+38  -6.66   7000.0      /\nTROE / 1.000  1000.0  1310.0 48097.0 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/\nC12H24+H(+M) = SXC12H25(+M)                  1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS\nLOW  / 8.70E+42  -7.50   4721.8      /\nTROE / 1.000  1000.0   645.4  6844.3 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(C2H4+C2H5)*2
Reactions of C12H24
C12H24+H(+M) = PXC12H25(+M)                  1.33E+13    0.00   3260.7  ! =(C3H6+H) !BS
LOW  / 6.26E+38  -6.66   7000.0      /
TROE / 1.000  1000.0  1310.0 48097.0 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
C12H24+H(+M) = SXC12H25(+M)                  1.33E+13    0.00   1559.8  ! =(C3H6+H) !BS
LOW  / 8.70E+42  -7.50   4721.8      /
TROE / 1.000  1000.0   645.4  6844.3 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 1306,
    label = "C12H24 <=> C9H18 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.08e+06, 's^-1'),
        n = 1.65,
        Ea = (53752, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 1307,
    label = "C12H24 + H <=> C2H4 + PXC10H21",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 1308,
    label = "C12H24 + H <=> C3H6 + PXC9H19",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)',
    ),
    longDesc = 
u"""
=(C3H6+H)
""",
)

entry(
    index = 1309,
    label = "C12H24 + H <=> PXC12H23 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (650000, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated',
    ),
    longDesc = 
u"""
Estimated
""",
)

entry(
    index = 1310,
    label = "C12H24 + O <=> PXC11H23 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-402, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+H)',
    ),
    longDesc = 
u"""
=(C4H81+H)
""",
)

entry(
    index = 1311,
    label = "C12H24 + O <=> PXC12H23 + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5760, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '=(C4H81+O)',
            ),
            Arrhenius(
                A = (2.6e+13, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4470, 'cal/mol'),
                T0 = (1, 'K'),
                comment = '(C4H81+O)',
            ),
        ],
    ),
)

entry(
    index = 1312,
    label = "C12H24 + OH <=> PXC12H23 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700, 'cm^3/(mol*s)'),
        n = 2.66,
        Ea = (527, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '(C4H81+O)',
    ),
    longDesc = 
u"""
(C4H81+O)
""",
)

entry(
    index = 1313,
    label = "C12H24 + O2 <=> PXC12H23 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+OH)',
    ),
    longDesc = 
u"""
=(C3H8+OH)
""",
)

entry(
    index = 1314,
    label = "C12H24 + HO2 <=> PXC12H23 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 1315,
    label = "C12H24 + CH3 <=> PXC12H23 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.45, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C4H81+HO2)',
    ),
    longDesc = 
u"""
=(C4H81+HO2)
""",
)

entry(
    index = 1316,
    label = "PXC12H25 <=> C2H4 + PXC10H21",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.12e+11, 's^-1'), n=0.31, Ea=(27237.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.8e-57, 'cm^3/(mol*s)'),
            n = 23.463,
            Ea = (-602.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -2.46,
        T3 = (206, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(C3H8+CH3)\nReactions of PXC12H25\nC2H4+PXC10H21 = PXC12H25                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nBeta-scission Reactions of dodecyl radicals',
    ),
    longDesc = 
u"""
=(C3H8+CH3)
Reactions of PXC12H25
C2H4+PXC10H21 = PXC12H25                     3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
Beta-scission Reactions of dodecyl radicals
""",
)

entry(
    index = 1317,
    label = "SXC12H25 <=> C3H6 + PXC9H19",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.03e+10, 's^-1'), n=0.84, Ea=(27820, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e-43, 'cm^3/(mol*s)'),
            n = 18.591,
            Ea = (-602.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -43.32,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1318,
    label = "S2XC12H25 <=> C4H81 + PXC8H17",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.04e+13, 's^-1'), n=0.04, Ea=(28493.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-43, 'cm^3/(mol*s)'),
            n = 18.43,
            Ea = (-602.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.47,
        T3 = (208, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1319,
    label = "S2XC12H25 <=> C11H22 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.55e+09, 's^-1'), n=1.08, Ea=(29387.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.3e-46, 'cm^3/(mol*s)'),
            n = 19.133,
            Ea = (-602.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -34.36,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1320,
    label = "S3XC12H25 <=> C5H10 + PXC7H15",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1321,
    label = "S3XC12H25 <=> C10H20 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.76e+09, 's^-1'), n=1.11, Ea=(27023.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.2e-43, 'cm^3/(mol*s)'),
            n = 18.276,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -30.04,
        T3 = (210, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1322,
    label = "S4XC12H25 <=> C6H12 + PXC6H13",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1323,
    label = "S4XC12H25 <=> C9H18 + nC3H7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1324,
    label = "S5XC12H25 <=> C7H14 + PXC5H11",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1325,
    label = "S5XC12H25 <=> C8H16 + pC4H9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.5e+11, 's^-1'), n=0.55, Ea=(28084.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.1e-43, 'cm^3/(mol*s)'),
            n = 18.418,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -32.13,
        T3 = (207, 'K'),
        T1 = (28, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1326,
    label = "PXC12H25 + H <=> NC12H26",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+48, 'cm^6/(mol^2*s)'),
            n = -9.32,
            Ea = (5833.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.498,
        T3 = (1314, 'K'),
        T1 = (1314, 'K'),
        T2 = (50000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'From 08TSAb !BS',
    ),
    longDesc = 
u"""
From 08TSAb !BS
""",
)

entry(
    index = 1327,
    label = "SXC12H25 + H <=> PXC10H21 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)\nReactions of SXC12H25\nC3H6+PXC9H19 = SXC12H25                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2  !BS\nS4XC12H25 = PXC12H25                        2.00E+11    0.00   18117.0 !\nSXC12H25+H = PXC10H21+C2H5                   5.90E+23   -2.81  10009.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(nC3H7+H)
Reactions of SXC12H25
C3H6+PXC9H19 = SXC12H25                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2  !BS
S4XC12H25 = PXC12H25                        2.00E+11    0.00   18117.0 !
SXC12H25+H = PXC10H21+C2H5                   5.90E+23   -2.81  10009.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1328,
    label = "SXC12H25 + H <=> C12H24 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC12H25+H = PXC10H21+C2H5                   4.00E+24   -2.83  17542.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC12H25+H = PXC10H21+C2H5                   4.00E+24   -2.83  17542.0  ! =(iC3H7+H)
""",
)

entry(
    index = 1329,
    label = "SXC12H25 + O <=> CH3CHO + PXC10H21",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
""",
)

entry(
    index = 1330,
    label = "SXC12H25 + OH <=> C12H24 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O)',
    ),
    longDesc = 
u"""
=(iC3H7+O)
""",
)

entry(
    index = 1331,
    label = "SXC12H25 + O2 <=> C12H24 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+OH)',
    ),
    longDesc = 
u"""
=(iC3H7+OH)
""",
)

entry(
    index = 1332,
    label = "SXC12H25 + HO2 <=> CH3CHO + PXC10H21 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
""",
)

entry(
    index = 1333,
    label = "SXC12H25 + HCO <=> NC12H26 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2)',
    ),
    longDesc = 
u"""
=(iC3H7+HO2)
""",
)

entry(
    index = 1334,
    label = "SXC12H25 + CH3 <=> CH4 + C12H24",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HCO)',
    ),
    longDesc = 
u"""
=(iC3H7+HCO)
""",
)

entry(
    index = 1335,
    label = "S2XC12H25 + O2 <=> C12H24 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+CH3)\nReactions of S2XC12H25\nC4H81+PXC8H17 = S2XC12H25                  3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS\nC11H22+CH3(+M) = S2XC12H25(+M)             1.70E+11    0.00   7403.6  ! =(C3H6+CH3) !BS\nLOW  / 2.31E+28  -4.27   1831.0      /\nTROE / 0.565 60000.0   534.2  3007.2 /\nH2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/',
    ),
    longDesc = 
u"""
=(iC3H7+CH3)
Reactions of S2XC12H25
C4H81+PXC8H17 = S2XC12H25                  3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2 !BS
C11H22+CH3(+M) = S2XC12H25(+M)             1.70E+11    0.00   7403.6  ! =(C3H6+CH3) !BS
LOW  / 2.31E+28  -4.27   1831.0      /
TROE / 0.565 60000.0   534.2  3007.2 /
H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/ Ar/0.7/
""",
)

entry(
    index = 1336,
    label = "S3XC12H25 + O2 <=> C12H24 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S3XC12H25\nC5H10+PXC7H15 = S3XC12H25                  3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nC10H20+C2H5 = S3XC12H25                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S3XC12H25
C5H10+PXC7H15 = S3XC12H25                  3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
C10H20+C2H5 = S3XC12H25                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 1337,
    label = "S4XC12H25 + O2 <=> C12H24 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S4XC12H25\nC6H12+PXC6H13 = S4XC12H25                  3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nC9H18+nC3H7 = S4XC12H25                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S4XC12H25
C6H12+PXC6H13 = S4XC12H25                  3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
C9H18+nC3H7 = S4XC12H25                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 1338,
    label = "S5XC12H25 + O2 <=> C12H24 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)\nReactions of S5XC12H25\nC7H14+PXC5H11 = S5XC12H25                  3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS\nC8H16+pC4H9 = S5XC12H25                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
Reactions of S5XC12H25
C7H14+PXC5H11 = S5XC12H25                  3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
C8H16+pC4H9 = S5XC12H25                    3.00E+11    0.00   7300.0  ! =(C2H4+C2H5)*2!BS
""",
)

entry(
    index = 1339,
    label = "PXC12H25 <=> S3XC12H25",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.13, 's^-1'), n=3.23, Ea=(16847.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.1e-44, 'cm^3/(mol*s)'),
            n = 18.749,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -20.15,
        T3 = (205, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = '=(iC3H7+O2)\nH_1,2 shift:\nPXC12H25 = SXC12H25                         3.56E+10     0.88  39000.0!BS\nPXC11H23 = SXC11H23                         3.56E+10     0.88  39000.0!BS\nPXC10H21 = SXC10H21                         3.56E+10     0.88  39000.0!BS\nPXC9H19 = SXC9H19                           3.56E+10     0.88  39000.0!BS\nPXC8H17 = SXC8H17\t\t\t     3.56E+10     0.88  39000.0!BS\nPXC7H15 = SXC7H15\t\t\t     3.56E+10     0.88  39000.0!BS\nPXC6H13 = SXC6H13\t\t\t     3.56E+10     0.88  39000.0!BS\nPXC5H11 = SXC5H11\t\t\t     3.56E+10     0.88  39000.0!BS\nH_1,3 shift:\nPXC12H25 = S2XC12H25\t                     3.80E+10     0.67  37500.0!BS\nPXC11H23 = S2XC11H23\t\t             3.80E+10     0.67  37500.0!BS\nPXC10H21 = S2XC10H21\t\t             3.80E+10     0.67  37500.0!BS\nPXC9H19 = S2XC9H19\t\t             3.80E+10     0.67  37500.0!BS\nPXC8H17 = S2XC8H17\t\t             3.80E+10     0.67  37500.0!BS\nPXC7H15 = S2XC7H15\t\t             3.80E+10     0.67  37500.0!BS\nPXC6H13 = S2XC6H13\t\t             3.80E+10     0.67  37500.0!BS\nPXC5H11 = S2XC5H11\t\t             3.80E+10     0.67  37500.0!BS\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nPrimary -> Secondary H_1,4 shift: !\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
H_1,2 shift:
PXC12H25 = SXC12H25                         3.56E+10     0.88  39000.0!BS
PXC11H23 = SXC11H23                         3.56E+10     0.88  39000.0!BS
PXC10H21 = SXC10H21                         3.56E+10     0.88  39000.0!BS
PXC9H19 = SXC9H19                           3.56E+10     0.88  39000.0!BS
PXC8H17 = SXC8H17			     3.56E+10     0.88  39000.0!BS
PXC7H15 = SXC7H15			     3.56E+10     0.88  39000.0!BS
PXC6H13 = SXC6H13			     3.56E+10     0.88  39000.0!BS
PXC5H11 = SXC5H11			     3.56E+10     0.88  39000.0!BS
H_1,3 shift:
PXC12H25 = S2XC12H25	                     3.80E+10     0.67  37500.0!BS
PXC11H23 = S2XC11H23		             3.80E+10     0.67  37500.0!BS
PXC10H21 = S2XC10H21		             3.80E+10     0.67  37500.0!BS
PXC9H19 = S2XC9H19		             3.80E+10     0.67  37500.0!BS
PXC8H17 = S2XC8H17		             3.80E+10     0.67  37500.0!BS
PXC7H15 = S2XC7H15		             3.80E+10     0.67  37500.0!BS
PXC6H13 = S2XC6H13		             3.80E+10     0.67  37500.0!BS
PXC5H11 = S2XC5H11		             3.80E+10     0.67  37500.0!BS
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Primary -> Secondary H_1,4 shift: !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""",
)

entry(
    index = 1340,
    label = "PXC11H23 <=> S3XC11H23",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.13, 's^-1'), n=3.23, Ea=(16847.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.1e-44, 'cm^3/(mol*s)'),
            n = 18.749,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -20.15,
        T3 = (205, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1341,
    label = "PXC10H21 <=> S3XC10H21",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.13, 's^-1'), n=3.23, Ea=(16847.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.1e-44, 'cm^3/(mol*s)'),
            n = 18.749,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -20.15,
        T3 = (205, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1342,
    label = "PXC9H19 <=> S3XC9H19",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.13, 's^-1'), n=3.23, Ea=(16847.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.1e-44, 'cm^3/(mol*s)'),
            n = 18.749,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -20.15,
        T3 = (205, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1343,
    label = "PXC8H17 <=> S3XC8H17",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.13, 's^-1'), n=3.23, Ea=(16847.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.1e-44, 'cm^3/(mol*s)'),
            n = 18.749,
            Ea = (-602.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -20.15,
        T3 = (205, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1344,
    label = "PXC7H15 <=> S3XC7H15",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(117, 's^-1'), n=2.85, Ea=(17247.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.9e-31, 'cm^3/(mol*s)'),
            n = 14.521,
            Ea = (-599, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -8.1,
        T3 = (259, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1345,
    label = "PXC6H13 <=> S2XC6H13",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.98, 's^-1'), n=3.2, Ea=(16557.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2e-26, 'cm^3/(mol*s)'),
            n = 12.833,
            Ea = (-600.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -10.14,
        T3 = (307, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAa',
    ),
    longDesc = 
u"""
BS 08TSAa
""",
)

entry(
    index = 1346,
    label = "PXC5H11 <=> SXC5H11",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+12, 's^-1'), n=0, Ea=(22453.1, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2e-26, 'cm^3/(mol*s)'),
            n = 12.833,
            Ea = (-600.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -10.14,
        T3 = (307, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 07TSA',
    ),
    longDesc = 
u"""
BS 07TSA
""",
)

entry(
    index = 1347,
    label = "PXC12H25 <=> S4XC12H25",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(22.9, 's^-1'), n=2.82, Ea=(10755.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.9e-38, 'cm^3/(mol*s)'),
            n = 17.215,
            Ea = (-603, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -16.33,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 98TSA\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nPrimary -> Secondary H_1,5 shift: !\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    ),
    longDesc = 
u"""
BS 98TSA
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Primary -> Secondary H_1,5 shift: !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""",
)

entry(
    index = 1348,
    label = "PXC11H23 <=> S4XC11H23",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(22.9, 's^-1'), n=2.82, Ea=(10755.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.9e-38, 'cm^3/(mol*s)'),
            n = 17.215,
            Ea = (-603, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -16.33,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1349,
    label = "PXC10H21 <=> S4XC10H21",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(22.9, 's^-1'), n=2.82, Ea=(10755.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.9e-38, 'cm^3/(mol*s)'),
            n = 17.215,
            Ea = (-603, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -16.33,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1350,
    label = "PXC9H19 <=> S4XC9H19",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(22.9, 's^-1'), n=2.82, Ea=(10755.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.9e-38, 'cm^3/(mol*s)'),
            n = 17.215,
            Ea = (-603, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -16.33,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1351,
    label = "PXC8H17 <=> S3XC8H17",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(22.9, 's^-1'), n=2.82, Ea=(10755.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.9e-38, 'cm^3/(mol*s)'),
            n = 17.215,
            Ea = (-603, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -16.33,
        T3 = (200, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1352,
    label = "PXC7H15 <=> S2XC7H15",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(676, 's^-1'), n=2.39, Ea=(10405.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.4e-26, 'cm^3/(mol*s)'),
            n = 13.202,
            Ea = (-602.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -25.39,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1353,
    label = "PXC6H13 <=> SXC6H13",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(183, 's^-1'), n=2.55, Ea=(10960.3, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.4e-26, 'cm^3/(mol*s)'),
            n = 13.087,
            Ea = (-602.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -25.38,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAa',
    ),
    longDesc = 
u"""
BS 08TSAa
""",
)

entry(
    index = 1354,
    label = "PXC12H25 <=> S5XC12H25",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(11015.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (-606.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 07TSA\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nPrimary -> Secondary H_1,6 shift !\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    ),
    longDesc = 
u"""
BS 07TSA
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Primary -> Secondary H_1,6 shift !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""",
)

entry(
    index = 1355,
    label = "PXC11H23 <=> S5XC11H23",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(11015.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (-606.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1356,
    label = "PXC10H21 <=> S4XC10H21",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(11015.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (-606.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1357,
    label = "PXC9H19 <=> S3XC9H19",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(11015.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (-606.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1358,
    label = "PXC8H17 <=> S2XC8H17",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(11015.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (-606.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1359,
    label = "PXC7H15 <=> SXC7H15",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(245, 's^-1'), n=2.51, Ea=(12502.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.3e-30, 'cm^3/(mol*s)'),
            n = 14.309,
            Ea = (-602.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -27.19,
        T3 = (220, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1360,
    label = "S3XC12H25 <=> S5XC12H25",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAa\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nSecondary -> Secondary H_1,4 shift !\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    ),
    longDesc = 
u"""
BS 08TSAa
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Secondary -> Secondary H_1,4 shift !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""",
)

entry(
    index = 1361,
    label = "S2XC12H25 <=> S5XC12H25",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1362,
    label = "SXC12H25 <=> S4XC12H25",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1363,
    label = "S3XC11H23 <=> S4XC11H23",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1364,
    label = "S2XC11H23 <=> S5XC11H23",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1365,
    label = "SXC11H23 <=> S4XC11H23",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1366,
    label = "S4XC10H21 <=> S2XC10H21",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1367,
    label = "S4XC10H21 <=> SXC10H21",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1368,
    label = "SXC9H19 <=> S4XC9H19",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1369,
    label = "S3XC9H19 <=> S2XC9H19",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1370,
    label = "SXC8H17 <=> S3XC8H17",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.41, 's^-1'), n=3.32, Ea=(16144.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e-30, 'cm^3/(mol*s)'),
            n = 14.079,
            Ea = (-606.4, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -21.93,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1371,
    label = "SXC7H15 <=> S2XC7H15",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(24.5, 's^-1'), n=3.09, Ea=(18107.5, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.3e-32, 'cm^3/(mol*s)'),
            n = 14.834,
            Ea = (-602.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -28.41,
        T3 = (219, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1372,
    label = "SXC12H25 <=> S5XC12H25",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.86, 's^-1'), n=3.27, Ea=(13197.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-27, 'cm^3/(mol*s)'),
            n = 13.481,
            Ea = (-606.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -19.7,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAa\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nSecondary -> Secondary H_1,5 shift !\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    ),
    longDesc = 
u"""
BS 08TSAa
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Secondary -> Secondary H_1,5 shift !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""",
)

entry(
    index = 1373,
    label = "S2XC12H25 <=> S5XC12H25",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.86, 's^-1'), n=3.27, Ea=(13197.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-27, 'cm^3/(mol*s)'),
            n = 13.481,
            Ea = (-606.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -19.7,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1374,
    label = "S3XC12H25 <=> S4XC12H25",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.86, 's^-1'), n=3.27, Ea=(13197.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-27, 'cm^3/(mol*s)'),
            n = 13.481,
            Ea = (-606.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -19.7,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1375,
    label = "SXC11H23 <=> S5XC11H23",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.86, 's^-1'), n=3.27, Ea=(13197.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-27, 'cm^3/(mol*s)'),
            n = 13.481,
            Ea = (-606.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -19.7,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1376,
    label = "S2XC11H23 <=> S4XC11H23",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.86, 's^-1'), n=3.27, Ea=(13197.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-27, 'cm^3/(mol*s)'),
            n = 13.481,
            Ea = (-606.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -19.7,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1377,
    label = "S2XC10H21 <=> S3XC10H21",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.86, 's^-1'), n=3.27, Ea=(13197.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-27, 'cm^3/(mol*s)'),
            n = 13.481,
            Ea = (-606.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -19.7,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1378,
    label = "SXC10H21 <=> S4XC10H21",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.86, 's^-1'), n=3.27, Ea=(13197.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-27, 'cm^3/(mol*s)'),
            n = 13.481,
            Ea = (-606.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -19.7,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1379,
    label = "SXC9H19 <=> S2XC9H19",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.86, 's^-1'), n=3.27, Ea=(13197.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-27, 'cm^3/(mol*s)'),
            n = 13.481,
            Ea = (-606.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -19.7,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1380,
    label = "SXC8H17 <=> S2XC8H17",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.86, 's^-1'), n=3.27, Ea=(13197.7, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3e-27, 'cm^3/(mol*s)'),
            n = 13.481,
            Ea = (-606.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -19.7,
        T3 = (215, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb',
    ),
    longDesc = 
u"""
BS 08TSAb
""",
)

entry(
    index = 1381,
    label = "S2XC12H25 <=> S4XC12H25",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(12865.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (1243.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS 08TSAb\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nSecondary -> Secondary H_1,6 shift !\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    ),
    longDesc = 
u"""
BS 08TSAb
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Secondary -> Secondary H_1,6 shift !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""",
)

entry(
    index = 1382,
    label = "SXC12H25 <=> S5XC12H25",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(12865.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (1243.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS Est (see notes)',
    ),
    longDesc = 
u"""
BS Est (see notes)
""",
)

entry(
    index = 1383,
    label = "S2XC11H23 <=> S3XC11H23",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(12865.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (1243.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS Est (see notes)',
    ),
    longDesc = 
u"""
BS Est (see notes)
""",
)

entry(
    index = 1384,
    label = "SXC11H23 <=> S4XC11H23",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(12865.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (1243.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS Est (see notes)',
    ),
    longDesc = 
u"""
BS Est (see notes)
""",
)

entry(
    index = 1385,
    label = "SXC10H21 <=> S3XC10H21",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(12865.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (1243.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS Est (see notes)',
    ),
    longDesc = 
u"""
BS Est (see notes)
""",
)

entry(
    index = 1386,
    label = "SXC9H19 <=> S2XC9H19",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.95, 's^-1'), n=3.08, Ea=(12865.9, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.9e-34, 'cm^3/(mol*s)'),
            n = 15.855,
            Ea = (1243.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -15.24,
        T3 = (216, 'K'),
        T1 = (28, 'K'),
        T2 = (5e+06, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
        comment = 'BS Est (see notes)',
    ),
    longDesc = 
u"""
BS Est (see notes)
""",
)

entry(
    index = 1387,
    label = "PXC11H23 + CH3 <=> NC12H26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BS Est (see notes)\nReactions of NC12H26',
    ),
    longDesc = 
u"""
BS Est (see notes)
Reactions of NC12H26
""",
)

entry(
    index = 1388,
    label = "PXC10H21 + C2H5 <=> NC12H26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(CH3+C2H5)',
    ),
    longDesc = 
u"""
=(CH3+C2H5)
""",
)

entry(
    index = 1389,
    label = "PXC9H19 + nC3H7 <=> NC12H26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1390,
    label = "PXC8H17 + pC4H9 <=> NC12H26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1391,
    label = "PXC7H15 + PXC5H11 <=> NC12H26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1392,
    label = "PXC6H13 + PXC6H13 <=> NC12H26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.4e+14, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1393,
    label = "NC12H26 + H <=> PXC12H25 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C2H5+C2H5)',
    ),
    longDesc = 
u"""
=(C2H5+C2H5)
""",
)

entry(
    index = 1394,
    label = "NC12H26 + H <=> SXC12H25 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)',
    ),
    longDesc = 
u"""
=(C3H8+H)
""",
)

entry(
    index = 1395,
    label = "NC12H26 + H <=> S2XC12H25 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)   EDames
""",
)

entry(
    index = 1396,
    label = "NC12H26 + H <=> S3XC12H25 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)   EDames
""",
)

entry(
    index = 1397,
    label = "NC12H26 + H <=> S4XC12H25 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)   EDames
""",
)

entry(
    index = 1398,
    label = "NC12H26 + H <=> S5XC12H25 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)   EDames
""",
)

entry(
    index = 1399,
    label = "NC12H26 + O <=> PXC12H25 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5504, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+H)   EDames',
    ),
    longDesc = 
u"""
=(C3H8+H)   EDames
""",
)

entry(
    index = 1400,
    label = "NC12H26 + O <=> SXC12H25 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1401,
    label = "NC12H26 + O <=> S2XC12H25 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1402,
    label = "NC12H26 + O <=> S3XC12H25 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1403,
    label = "NC12H26 + O <=> S4XC12H25 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1404,
    label = "NC12H26 + O <=> S5XC12H25 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (1768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1405,
    label = "NC12H26 + OH <=> PXC12H25 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (974, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 86/CW (octane)',
    ),
    longDesc = 
u"""
!BS 86/CW (octane)
""",
)

entry(
    index = 1406,
    label = "NC12H26 + OH <=> SXC12H25 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1407,
    label = "NC12H26 + OH <=> S2XC12H25 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1408,
    label = "NC12H26 + OH <=> S3XC12H25 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1409,
    label = "NC12H26 + OH <=> S4XC12H25 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1410,
    label = "NC12H26 + OH <=> S5XC12H25 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1391, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1411,
    label = "NC12H26 + O2 <=> PXC12H25 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '!BS 91Coh (decane)',
    ),
    longDesc = 
u"""
!BS 91Coh (decane)
""",
)

entry(
    index = 1412,
    label = "NC12H26 + O2 <=> SXC12H25 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)',
    ),
    longDesc = 
u"""
=(C3H8+O2)
""",
)

entry(
    index = 1413,
    label = "NC12H26 + O2 <=> S2XC12H25 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)  EDames
""",
)

entry(
    index = 1414,
    label = "NC12H26 + O2 <=> S3XC12H25 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)  EDames
""",
)

entry(
    index = 1415,
    label = "NC12H26 + O2 <=> S4XC12H25 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)  EDames
""",
)

entry(
    index = 1416,
    label = "NC12H26 + O2 <=> S5XC12H25 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)  EDames
""",
)

entry(
    index = 1417,
    label = "NC12H26 + HO2 <=> PXC12H25 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (16490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+O2)  EDames',
    ),
    longDesc = 
u"""
=(C3H8+O2)  EDames
""",
)

entry(
    index = 1418,
    label = "NC12H26 + HO2 <=> SXC12H25 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2)',
    ),
    longDesc = 
u"""
=(C3H8+HO2)
""",
)

entry(
    index = 1419,
    label = "NC12H26 + HO2 <=> S2XC12H25 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2) EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2) EDames
""",
)

entry(
    index = 1420,
    label = "NC12H26 + HO2 <=> S3XC12H25 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2) EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2) EDames
""",
)

entry(
    index = 1421,
    label = "NC12H26 + HO2 <=> S4XC12H25 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2) EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2) EDames
""",
)

entry(
    index = 1422,
    label = "NC12H26 + HO2 <=> S5XC12H25 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (13910, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2) EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2) EDames
""",
)

entry(
    index = 1423,
    label = "NC12H26 + CH3 <=> PXC12H25 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.903, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+HO2) EDames',
    ),
    longDesc = 
u"""
=(C3H8+HO2) EDames
""",
)

entry(
    index = 1424,
    label = "NC12H26 + CH3 <=> SXC12H25 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3) EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3) EDames
""",
)

entry(
    index = 1425,
    label = "NC12H26 + CH3 <=> S2XC12H25 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3) EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3) EDames
""",
)

entry(
    index = 1426,
    label = "NC12H26 + CH3 <=> S3XC12H25 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3) EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3) EDames
""",
)

entry(
    index = 1427,
    label = "NC12H26 + CH3 <=> S4XC12H25 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3) EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3) EDames
""",
)

entry(
    index = 1428,
    label = "NC12H26 + CH3 <=> S5XC12H25 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3) EDames',
    ),
    longDesc = 
u"""
=(C3H8+CH3) EDames
""",
)

entry(
    index = 1429,
    label = "PXC12H25 + O2 <=> PC12H25O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H8+CH3) EDames\nLow T of C12',
    ),
    longDesc = 
u"""
=(C3H8+CH3) EDames
Low T of C12
""",
)

entry(
    index = 1430,
    label = "SXC12H25 + O2 <=> PC12H25O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BS',
    ),
    longDesc = 
u"""
BS
""",
)

entry(
    index = 1431,
    label = "S2XC12H25 + O2 <=> PC12H25O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BS',
    ),
    longDesc = 
u"""
BS
""",
)

entry(
    index = 1432,
    label = "S3XC12H25 + O2 <=> PC12H25O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BS',
    ),
    longDesc = 
u"""
BS
""",
)

entry(
    index = 1433,
    label = "S4XC12H25 + O2 <=> PC12H25O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BS',
    ),
    longDesc = 
u"""
BS
""",
)

entry(
    index = 1434,
    label = "S5XC12H25 + O2 <=> PC12H25O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BS',
    ),
    longDesc = 
u"""
BS
""",
)

entry(
    index = 1435,
    label = "PC12H25O2 => P12OOHX2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (2e+12, 's^-1'),
        n = 0,
        Ea = (17017.2, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BS',
    ),
    longDesc = 
u"""
BS
""",
)

entry(
    index = 1436,
    label = "P12OOHX2 => PC12H25O2",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(12500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1437,
    label = "P12OOHX2 <=> C12H24 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+12, 's^-1'), n=0, Ea=(25573.6, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1438,
    label = "P12OOHX2 + O2 <=> SOO12OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1439,
    label = "SOO12OOH <=> OC12OOH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+12, 's^-1'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'BS',
    ),
    longDesc = 
u"""
BS
""",
)

# RMG does not accept a reaction with more than 3 products\reactants
#entry(
#    index = 1440,
#    label = "OC12OOH <=> CH2O + C2H4 + C2H4 + C2H4 + C2H4 + C2H5 + OH + CO",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(7e+14, 's^-1'), n=0, Ea=(42065, 'cal/mol'), T0=(1, 'K')),
#)

