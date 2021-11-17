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
    index = 13,
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
    index = 14,
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
    index = 15,
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
    index = 16,
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
    index = 17,
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
    index = 18,
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
    index = 19,
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

entry(
    index = 20,
    label = "CHCl + ClH <=> CH2Cl2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29.3293,'cm^3/(mol*s)'), n=3.0651, Ea=(82.8573,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.27975, dn = +|- 0.0324069, dEa = +|- 0.176357 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1,2_Insertion_carbene
Original entry: [CH]Cl + Cl <=> ClCCl
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 99.093 kJ/mol

Cl    -1.532894    -0.103313    -0.016505
H    -0.090402    1.672669    0.658359
C    -0.171809    0.989845    -0.209741
Cl    1.529308    -0.088202    -0.0154
H    0.547547    0.450051    0.923357
""",
)

entry(
    index = 21,
    label = "CHCl + H2_r23 <=> CH3Cl-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39739e+06,'cm^3/(mol*s)'), n=2.08325, Ea=(9.93074,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18262, dn = +|- 0.0220362, dEa = +|- 0.11992 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1,2_Insertion_carbene
Original entry: [CH]Cl + [H][H] <=> CCl
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 19.586 kJ/mol

Cl    -1.140263    -0.231728    0.139039
H    0.773484    0.766065    0.812477
C    0.424494    0.433777    -0.180209
H    1.555152    -1.088451    0.370826
H    1.492213    -0.788943    -0.344024
""",
)

entry(
    index = 22,
    label = "CF2_r1 + CF4_r23 <=> FC(F)(F)C(F)(F)F_p123",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(5.34327,'cm^3/(mol*s)'), n=3.3552, Ea=(272.197,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1212, dn = +|- 0.0150298, dEa = +|- 0.0817915 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1,2_Insertion_carbene
Original entry: F[C]F + FC(F)(F)F <=> FC(F)(F)C(F)(F)F
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 279.045 kJ/mol

F    0.145393    -1.101329    -0.717923
F    1.830989    0.486732    -0.972091
F    1.839973    -0.632008    0.810651
F    -0.937617    1.217267    -0.5759
F    -1.923556    -0.619567    -0.405348
F    -0.928867    0.033717    1.314709
C    1.104489    0.095507    0.028512
C    -0.841664    0.045031    0.00564
""",
)

entry(
    index = 23,
    label = "CHBr + BrH <=> CH2Br2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(582.952,'cm^3/(mol*s)'), n=2.73661, Ea=(52.1718,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04122, dn = +|- 0.00530686, dEa = +|- 0.0288798 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1,2_Insertion_carbene
Original entry: [CH]Br + Br <=> BrCBr
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 63.705 kJ/mol

Br    -1.364172    -0.79887    -0.158316
H    0.006571    1.036603    0.840387
C    -0.392723    0.866056    -0.178953
Br    1.503832    0.575119    -1.286218
H    0.906462    0.136491    0.09662
""",
)

entry(
    index = 24,
    label = "CF2_r1 + FH <=> CHF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00398081,'cm^3/(mol*s)'), n=4.16158, Ea=(55.7474,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 3.20446, dn = +|- 0.152998, dEa = +|- 0.832608 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1,2_Insertion_carbene
Original entry: F[C]F + F <=> FC(F)F
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 83.554 kJ/mol

F    -1.173077    -0.391031    0.028581
F    -0.437426    1.397459    0.811619
C    -0.33304    0.554819    -0.141255
F    1.395651    -0.254871    0.084683
H    0.713632    0.379043    -0.723127
""",
)

entry(
    index = 25,
    label = "CHF_r1 + FH <=> CH2F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9488.44,'cm^3/(mol*s)'), n=2.40423, Ea=(-1.8086,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.15696, dn = +|- 0.019155, dEa = +|- 0.104241 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1,2_Insertion_carbene
Original entry: [CH]F + F <=> FCF
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 10.871 kJ/mol

F    1.040784    -0.424239    -0.070737
H    -0.890091    -0.255937    -0.100793
C    0.016789    0.310713    -0.33722
F    -0.097871    1.714272    1.053627
H    0.061969    1.563821    -0.063856
""",
)

entry(
    index = 26,
    label = "CHF_r1 + H2_r23 <=> CF_p123",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.13948e+06,'cm^3/(mol*s)'), n=1.96174, Ea=(10.3842,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.23287, dn = +|- 0.0275038, dEa = +|- 0.149675 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1,2_Insertion_carbene
Original entry: [CH]F + [H][H] <=> CF
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 20.698 kJ/mol

F    -1.192549    -0.408095    0.055992
H    -0.234984    1.111644    0.760794
C    -0.504484    0.687358    -0.232742
H    1.203766    -0.016631    0.056779
H    0.923371    0.192935    -0.648684
""",
)

entry(
    index = 27,
    label = "CF2_r1 + H2_r23 <=> FCF_p123",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00326413,'cm^3/(mol*s)'), n=4.30786, Ea=(109.478,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 6.37258, dn = +|- 0.243316, dEa = +|- 1.32412 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1,2_Insertion_carbene
Original entry: F[C]F + [H][H] <=> FCF
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 143.899 kJ/mol

F    -0.128793    -1.084934    -0.216679
F    -0.095222    1.059355    -0.146325
C    0.391577    -0.040297    0.416646
H    -0.625432    -0.063401    1.611109
H    0.32886    -0.078592    1.611489
""",
)

entry(
    index = 28,
    label = "CHBr + H2_r23 <=> CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.50896e+06,'cm^3/(mol*s)'), n=2.11145, Ea=(7.35429,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17058, dn = +|- 0.0206925, dEa = +|- 0.112608 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1,2_Insertion_carbene
Original entry: [CH]Br + [H][H] <=> CBr
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 16.373 kJ/mol

Br    -1.272767    -0.236652    0.148971
H    0.785723    0.774036    0.814768
C    0.45292    0.467056    -0.192011
H    1.594591    -1.111476    0.36596
H    1.544614    -0.802244    -0.339578
""",
)

