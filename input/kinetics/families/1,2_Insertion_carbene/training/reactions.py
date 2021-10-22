#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CH2 + C2H2 <=> CH3CCH",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.63e+07, 'cm^3/(mol*s)', '*|/', 0.25),
        n = 1.475,
        Ea = (-1.651, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 1,
    label = "CH2 + C2H4 <=> CH3CHCH2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (5.3e+12, 'cm^3/(mol*s)', '*|/', 0.25),
        n = 0.0073,
        Ea = (-1.054, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 2,
    label = "CH2 + CH3CCH_r1 <=> CH3CCCH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.03e+08, 'cm^3/(mol*s)', '*|/', 0.25),
        n = 1.249,
        Ea = (-2.214, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 3,
    label = "CH2 + CH3CCH_r2 <=> CH3CH2CCH",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (9.18e+10, 'cm^3/(mol*s)', '*|/', 0.25),
        n = 0.524,
        Ea = (-0.711, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 4,
    label = "CH2 + CH3CHCH2_r1 <=> CH3CHCHCH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.97e+13, 'cm^3/(mol*s)', '*|/', 0.25),
        n = -0.324,
        Ea = (-0.935, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 5,
    label = "CH2 + CH3CHCH2_r2 <=> CH2C(CH3)CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.13e+13, 'cm^3/(mol*s)', '*|/', 0.25),
        n = -0.274,
        Ea = (-0.686, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 6,
    label = "CH2 + CH3CHCH2_r3 <=> CH3CH2CHCH2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.87e+13, 'cm^3/(mol*s)', '*|/', 0.25),
        n = -0.146,
        Ea = (0.00284, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 7,
    label = "CH2 + CH2CCH2 <=> CH3CHCCH2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (2.8e+11, 'cm^3/(mol*s)', '*|/', 0.25),
        n = 0.465,
        Ea = (-1.742, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 8,
    label = "CH2 + CH2CHCHCH2_r1 <=> CH3CHCHCHCH2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (5.26e+11, 'cm^3/(mol*s)', '*|/', 0.25),
        n = 0.313,
        Ea = (-1.854, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 9,
    label = "CH2 + CH2CHCHCH2_r2 <=> CH2C(CH3)CHCH2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.34e+10, 'cm^3/(mol*s)', '*|/', 0.25),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 10,
    label = "CH2 + CH3CCCH3_r1 <=> CH3CH2CCCH3",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (2.96e+10, 'cm^3/(mol*s)', '*|/', 0.25),
        n = 0.797,
        Ea = (-1.174, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 11,
    label = "CH2 + benzene <=> toluene",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (6.48e+13, 'cm^3/(mol*s)', '*|/', 0.25),
        n = -0.272,
        Ea = (-1.274, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['D. Polino', 'S.J. Klippenstein', 'L.B. Harding', 'Y. Georgievskii'],
        title = 'Predictive Theory for the Addition and Insertion of Kinetics of CH2 Reacting with Unsaturated Hydrocarbons',
        journal = 'JPCA',
        volume = '117',
        pages = '12677-12692',
        year = '2013',
    ),
    referenceType = "theory",
    rank = 4,
    shortDesc = u"""VTST calculations at CCSD(T)/CBS//CASPT2/cc-pVDZ level""",
    longDesc = 
u"""
Quantum chemistry calculations at the CCSD(T)/CBS//CASPT2/cc-pVDZ level with hindered rotor corrections. A-factor error is estimated by source.
""",
)

entry(
    index = 12,
    label = "CHF_r1 + H2_r23 <=> CF_p123",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.25e+17,'cm^3/(mol*s)'), n=-2.85, Ea=(13000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 13,
    label = "CF2_r1 + H2_r23 <=> FCF_p123",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+06,'cm^3/(mol*s)'), n=-0.71, Ea=(40900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 14,
    label = "CH2Cl2 <=> CHCl + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.82e+37,'s^-1'), n=-7.43, Ea=(85730,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CH2CL2 <=> CHCL + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CH3Cl
Original entry: CH2CL2 <=> CHCL + HCL
""",
)

entry(
    index = 15,
    label = "Br2 + CF2_r1 <=> CBr2F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+09,'cm^3/(mol*s)'), n=0, Ea=(1030,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """The chemkin file reaction is CF2 + BR2 <=> CF2BR2""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF2 + BR2 <=> CF2BR2
""",
)

entry(
    index = 16,
    label = "CHClF2 <=> CF2_r1 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41e+13,'s^-1'), n=0, Ea=(53465,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """The chemkin file reaction is CHF2CL <=> CF2 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CHF2CL <=> CF2 + HCL
""",
)

entry(
    index = 17,
    label = "BrH + CF2_r1 <=> CHBrF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.14e+11,'cm^3/(mol*s)'), n=0, Ea=(9560,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """The chemkin file reaction is CF2 + HBR <=> CHF2BR""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF2 + HBR <=> CHF2BR
""",
)

entry(
    index = 18,
    label = "CF4 + CF2_r1 => C2F6",
    degeneracy = 4.0,
    reversible = False,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(51000,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """The chemkin file reaction is CF4 + CF2 => CF3-CF3""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF4 + CF2 => CF3-CF3
""",
)

entry(
    index = 19,
    label = "CH3Cl <=> CH2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+28,'s^-1'), n=-5.15, Ea=(109670,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """The chemkin file reaction is CH3CL <=> CH2(S) + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CH3CL <=> CH2(S) + HCL
""",
)

entry(
    index = 20,
    label = "CHCl3 <=> CCl2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.2e+12,'s^-1'), n=0, Ea=(51500,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """The chemkin file reaction is CHCL3 <=> CCL2 + HCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CHCL3 <=> CCL2 + HCL
""",
)

entry(
    index = 21,
    label = "Cl2 + CCl2 <=> CCl4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(6000,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """The chemkin file reaction is CCL2 + CL2 <=> CCL4""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CCL2 + CL2 <=> CCL4
""",
)

entry(
    index = 22,
    label = "Cl2 + CF2_r1 <=> CCl2F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.21e+08,'cm^3/(mol*s)'), n=0, Ea=(2110,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """The chemkin file reaction is CF2 + CL2 <=> CF2CL2""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF2 + CL2 <=> CF2CL2
""",
)

entry(
    index = 23,
    label = "CHCl3-2 + CCl2 <=> C2HCl5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.39e+11,'cm^3/(mol*s)'), n=0, Ea=(11900,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """The chemkin file reaction is CCL2 + CHCL3 <=> C2HCL5""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CCL2 + CHCL3 <=> C2HCL5
""",
)

