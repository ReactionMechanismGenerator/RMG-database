#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
Sources:
[1] Characterization of the 1,1-HCl Elimination Reaction of Vibrationally Excited CD3CHFCl Molecules and Assignment of Threshold Energies for 1,1-HCl and 1,2-DCl plus 1,1-HF and 1,2-DF Elimination Reactions
    Timothy M. Brown, Matthew J. Nestler, Samuel M. Rossabi, George L. Heard, D. W. Setser, and Bert E. Holmes
    The Journal of Physical Chemistry A 2015 119 (36), 9441-9451
    DOI: 10.1021/acs.jpca.5b06638

[2] Unimolecular HBr and HF Elimination Reactions of Vibrationally Excited C2H5CH2Br and C2D5CHFBr: Identification of the 1,1-HBr Elimination Reaction from C2D5CHFBr and Search for the C2D5(F)C:HBr Adduct
    Timothy M. Brown, Blanton R. Gillespie, Mallory M. Rothrock, Anthony J. Ranieri, Melinda K. Schueneman, George L. Heard, Donald W. Setser, and Bert E. Holmes
    The Journal of Physical Chemistry A 2019 123 (41), 8776-8786
    DOI: 10.1021/acs.jpca.9b07029

[3] The Unimolecular Reactions of CF3CHF2 Studied by Chemical Activation: Assignment of Rate Constants and Threshold Energies to the 1,2-H Atom Transfer, 1,1-HF and 1,2-HF Elimination Reactions, and the Dependence of Threshold Energies on the Number of F-Atom Substituents in the Fluoroethane Molecules
    Caleb A. Smith, Blanton R. Gillespie, George L. Heard, D. W. Setser, and Bert E. Holmes
    The Journal of Physical Chemistry A 2017 121 (46), 8746-8756
    DOI: 10.1021/acs.jpca.7b06769
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    rank = 10,
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
    kinetics = Arrhenius(A=(1e13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment=""""""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier is submerged = -20.411 kJ/mol
assume barrierless

Cl    -1.713168    -0.072738    0.025808
H    -0.448144    1.711652    0.501838
C    -0.399293    0.909528    -0.247448
Cl    2.150168    -0.467838    -0.498352
H    0.984247    0.251576    -0.706437
""",
)

entry(
    index = 21,
    label = "CHCl + H2_r23 <=> CH3Cl-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39739e+06,'cm^3/(mol*s)'), n=2.08325, Ea=(9.93074,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18262, dn = +|- 0.0220362, dEa = +|- 0.11992 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
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
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
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
    kinetics = Arrhenius(A=(1e13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment=""""""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Could not locate TS with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
assuming barrierless
""",
)

entry(
    index = 24,
    label = "CF2_r1 + FH <=> CHF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00398081,'cm^3/(mol*s)'), n=4.16158, Ea=(55.7474,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 3.20446, dn = +|- 0.152998, dEa = +|- 0.832608 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
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
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
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
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
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
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
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
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 16.373 kJ/mol

Br    -1.272767    -0.236652    0.148971
H    0.785723    0.774036    0.814768
C    0.45292    0.467056    -0.192011
H    1.594591    -1.111476    0.36596
H    1.544614    -0.802244    -0.339578
""",
)

entry(
    index = 29,
    label = "C2H4ClF <=> C2H3F + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39e+15,'s^-1'), n=0, Ea=(73,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Training reaction from kinetics library: HY_elim
Original entry: CH3CHFCl <=> CH3CF + HCl
From [1]
Arrhenius form (s−1) at 1000 K
""",
)

entry(
    index = 30,
    label = "C2H4ClF-2 <=> C2H3Cl + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(75.5,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Training reaction from kinetics library: HY_elim
Original entry: CH3CHFCl_2 <=> CH3CCl + HF
From [1]
Arrhenius form (s−1) at 1000 K
""",
)

entry(
    index = 31,
    label = "C2H4BrF <=> C2H3F + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39e+15,'s^-1'), n=0, Ea=(65.8,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
""",
)

entry(
    index = 32,
    label = "C2H3BrF2 <=> C2H2F2 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39e+15,'s^-1'), n=0, Ea=(70.7,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Training reaction from kinetics library: HY_elim
Original entry: CH2FCHFBr <=> CH2FCF + HBr
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
""",
)

entry(
    index = 33,
    label = "C2H2BrF3 <=> C2HF3 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39e+15,'s^-1'), n=0, Ea=(75.5,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
""",
)

entry(
    index = 34,
    label = "C2HBrF4 <=> C2F4 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39e+15,'s^-1'), n=0, Ea=(77.3,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
""",
)

entry(
    index = 35,
    label = "C3H6BrF <=> C3H5F + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39e+15,'s^-1'), n=0, Ea=(66,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """MP2/6-311+G(2d,p)""",
    longDesc = 
"""
Ea taken from Table 3 in [2]
A factor taken for CH3CHFCl <=> CH3CF + HCl in [1]
""",
)

entry(
    index = 36,
    label = "C2H4F2 <=> C2H3F + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(74,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """experimental""",
    longDesc = 
"""
Ea taken from Table 2 in [3]
A factor taken for CH3CHFCl <=> CH3CCl + HF in [1]
""",
)

entry(
    index = 37,
    label = "C2H3F3 <=> C2H2F2 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(77,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """experimental""",
    longDesc = 
"""
Ea taken from Table 2 in [3]
A factor taken for CH3CHFCl <=> CH3CCl + HF in [1]
""",
)

entry(
    index = 38,
    label = "C2H2F4 <=> C2HF3 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(84,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """M062X/6-311G(2d,p)""",
    longDesc = 
"""
Ea taken from Table 2 in [3]
A factor taken for CH3CHFCl <=> CH3CCl + HF in [1]
""",
)

entry(
    index = 39,
    label = "C2HF5 <=> C2F4 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97e+14,'s^-1'), n=0, Ea=(85,'kcal/mol'), T0=(1,'K')),
    rank = 7,
    shortDesc = """M062X/6-311G(2d,p)""",
    longDesc = 
"""
Ea taken from Table 2 in [3]
A factor taken for CH3CHFCl <=> CH3CCl + HF in [1]
""",
)

entry(
    index = 40,
    label = "C2H3Br + CH4 <=> C3H7Br",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(11.7012,'cm^3/(mol*s)'), n=3.16987, Ea=(35.1917,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0603, dn = +|- 0.00769279, dEa = +|- 0.0418639 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 46.031 kJ/mol

Br    -0.692934    -1.755445    -0.337842
C    -0.959406    1.053029    -0.156715
C    -0.385181    -0.099815    0.60748
C    1.706166    0.224468    -0.070066
H    -2.034981    1.010395    0.033369
H    -0.586287    1.991132    0.255145
H    -0.815173    1.035815    -1.240143
H    0.872973    0.004361    0.839758
H    1.352014    0.201505    -1.09025
H    2.391433    -0.592632    0.139201
H    2.092887    1.197348    0.221323
""",
)

entry(
    index = 41,
    label = "C2H3Cl + CH4 <=> C3H7Cl",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(8.96195,'cm^3/(mol*s)'), n=3.20888, Ea=(40.549,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04063, dn = +|- 0.00523243, dEa = +|- 0.0284747 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 51.879 kJ/mol

Cl    -0.653952    -1.619534    -0.308083
C    -0.961682    1.040042    -0.159188
C    -0.385031    -0.124314    0.584529
C    1.700254    0.213937    -0.071232
H    -2.037394    0.995706    0.028271
H    -0.589834    1.97368    0.261361
H    -0.814271    1.02929    -1.242861
H    0.862495    -0.01145    0.842218
H    1.349583    0.175761    -1.092464
H    2.391295    -0.595426    0.149619
H    2.080046    1.192468    0.209091
""",
)

entry(
    index = 42,
    label = "C2H3F + CH4 <=> C3H7F",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(1.33549,'cm^3/(mol*s)'), n=3.38172, Ea=(55.0573,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07084, dn = +|- 0.008992, dEa = +|- 0.0489341 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 68.906 kJ/mol

F    1.124633    -1.241279    -0.302952
C    1.32193    1.003034    0.2504
C    1.181235    -0.002325    -0.849027
C    -0.94433    0.258106    -1.076336
H    2.35946    0.9369    0.584564
H    1.158066    2.008218    -0.13081
H    0.67833    0.815849    1.11549
H    0.226633    0.151346    -1.635444
H    -1.086597    -0.265425    -0.140502
H    -1.482804    -0.22235    -1.890876
H    -1.151495    1.320336    -1.008378
""",
)

entry(
    index = 43,
    label = "CHF_r1 + CH3Br-2 <=> C2H4BrF-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(30.1249,'cm^3/(mol*s)'), n=3.17037, Ea=(120.81,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07904, dn = +|- 0.00999483, dEa = +|- 0.0543915 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 129.617 kJ/mol

Br    -0.911553    -0.259394    0.073238
F    1.707081    -0.341313    -1.113424
H    1.501427    -0.4996    0.833006
H    0.383799    2.14802    -0.936374
H    -1.169658    2.179089    -0.015238
H    0.399801    2.238748    0.877259
C    1.335129    0.233491    0.028853
C    -0.119316    1.918099    -0.01044
""",
)

entry(
    index = 44,
    label = "CF2_r1 + CH3Br-2 <=> C2H3BrF2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.43831,'cm^3/(mol*s)'), n=3.35156, Ea=(209.26,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14968, dn = +|- 0.0183253, dEa = +|- 0.0997254 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 216.094 kJ/mol

Br    0.38892    0.005147    -2.035482
F    2.147557    1.132453    0.007161
F    2.19423    -0.967509    0.045684
H    -0.681321    0.942421    0.693655
H    -1.564558    -0.01086    -0.562074
H    -0.641569    -0.879156    0.726163
C    1.406554    0.067923    0.159177
C    -0.744952    0.019601    0.139166
""",
)

entry(
    index = 45,
    label = "CHF_r1 + CH3F <=> C2H4F2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.96165,'cm^3/(mol*s)'), n=3.30609, Ea=(133.548,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14157, dn = +|- 0.0173948, dEa = +|- 0.0946619 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 144.869 kJ/mol

F    0.637124    0.046018    0.851408
H    -1.012463    0.856211    -0.131406
F    -1.065083    -1.097492    -0.17537
H    1.714192    0.852105    -1.096544
H    2.538783    0.028743    0.290457
H    1.68179    -0.951025    -0.97474
C    -0.367715    0.019111    -0.429368
C    1.742722    -0.01056    -0.451048
""",
)

entry(
    index = 46,
    label = "CHF_r1 + CH3Cl-3 <=> C2H4ClF-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(17.8425,'cm^3/(mol*s)'), n=3.22746, Ea=(130.179,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10739, dn = +|- 0.0134011, dEa = +|- 0.0729283 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 139.785 kJ/mol

Cl    -0.988935    -0.73972    0.007959
F    1.388023    -0.044821    -1.098706
H    1.193095    -0.131316    0.854906
H    -0.858706    1.841286    -0.935807
H    -2.260688    1.223335    0.026484
H    -0.818107    1.900438    0.876109
C    0.773145    0.411898    -0.003865
C    -1.193308    1.40911    -0.00658
""",
)

entry(
    index = 47,
    label = "CF2_r1 + CH4 <=> C2H4F2-3",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(0.000267207,'cm^3/(mol*s)'), n=4.72997, Ea=(129.265,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 3.00906, dn = +|- 0.144732, dEa = +|- 0.787625 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 153.464 kJ/mol

H    0.441606    -0.239005    0.598734
F    -0.591304    -0.614218    -1.227686
F    -0.490175    1.38018    -0.427886
H    2.022439    -1.020489    -0.099551
H    1.61781    0.398106    -1.142301
H    2.106911    0.669546    0.575416
C    -0.408388    0.090654    -0.115718
C    1.641711    -0.004263    -0.137797
""",
)

entry(
    index = 48,
    label = "CF2_r1 + H2O <=> CH2F2O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.52789e-06,'cm^3/(mol*s)'), n=5.02686, Ea=(72.5674,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 3.96429, dn = +|- 0.180953, dEa = +|- 0.98474 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 103.723 kJ/mol

F    0.771481    -1.056488    -0.052798
F    0.65349    1.042089    -0.285
C    0.185362    0.01667    0.389916
O    -1.48358    -0.172316    -0.244125
H    -1.000445    0.018846    0.844749
H    -1.727239    0.690888    -0.605771
""",
)

entry(
    index = 49,
    label = "CHF_r1 + CH4 <=> C2H5F",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(111.983,'cm^3/(mol*s)'), n=3.10993, Ea=(26.3876,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0698, dn = +|- 0.00886387, dEa = +|- 0.0482369 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 38.444 kJ/mol

H    0.765696    0.255978    0.864815
H    -0.537434    -0.933964    0.10096
F    -0.928359    0.952914    -0.270049
H    1.938071    -1.005509    0.074224
H    1.261692    0.21915    -1.069208
H    2.308902    0.745727    0.285865
C    -0.470397    0.038808    0.608346
C    1.58449    0.010175    -0.058755
""",
)

entry(
    index = 50,
    label = "CF2_r1 + CH3F <=> C2H3F3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.6158,'cm^3/(mol*s)'), n=3.54561, Ea=(195.225,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20788, dn = +|- 0.0248129, dEa = +|- 0.135031 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 205.134 kJ/mol

F    0.23109    -0.011075    -1.121739
F    1.870875    1.063806    0.005076
F    1.874336    -1.048293    0.034849
H    -0.979425    0.922048    0.725225
H    -1.704603    -0.004539    -0.658058
H    -0.978849    -0.890455    0.751312
C    1.109625    0.009585    0.240378
C    -0.985158    0.007412    0.154467
""",
)

entry(
    index = 51,
    label = "CHF_r1 + H2O <=> CH3FO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.34896,'cm^3/(mol*s)'), n=3.15288, Ea=(2.84581,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0433, dn = +|- 0.00556916, dEa = +|- 0.0303072 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 19.372 kJ/mol

H    0.74012    -0.790596    -0.045987
F    0.62736    1.16595    -0.09184
C    0.281806    0.027063    0.513377
O    -1.425142    -0.253122    -0.065619
H    -0.995621    -0.078024    0.948873
H    -1.699203    0.6171    -0.384374
""",
)

entry(
    index = 52,
    label = "CF2_r1 + CH3Cl-3 <=> C2H3ClF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.42311,'cm^3/(mol*s)'), n=3.42841, Ea=(214.884,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17954, dn = +|- 0.0216936, dEa = +|- 0.118056 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 222.631 kJ/mol

Cl    0.417331    0.019598    -1.842081
F    2.145051    1.130018    -0.012663
F    2.188692    -0.973624    0.012831
H    -0.689768    0.937585    0.674142
H    -1.557579    -0.005315    -0.600844
H    -0.652749    -0.881779    0.695608
C    1.398343    0.063896    0.1357
C    -0.744462    0.019641    0.110756
""",
)

entry(
    index = 53,
    label = "CHF_r1 + C2H6 <=> C3H7F-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.7066,'cm^3/(mol*s)'), n=3.19155, Ea=(216.984,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08847, dn = +|- 0.0111371, dEa = +|- 0.0606078 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 228.586 kJ/mol

C    -0.644246    -0.043312    -0.088057
F    1.715548    -0.702246    -0.482367
H    0.989542    -0.361591    1.334637
H    0.877781    1.963655    -0.790798
H    -0.787353    1.975547    -0.238985
H    0.485569    2.104716    0.946103
C    1.384228    0.200187    0.476699
C    0.226497    1.628584    0.007684
H    -0.930332    0.129831    -1.118879
H    -1.450398    0.170656    0.604405
H    -0.328167    -1.074417    0.000369
""",
)

entry(
    index = 54,
    label = "CF2_r1 + C2H6 <=> C3H6F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.222791,'cm^3/(mol*s)'), n=3.59921, Ea=(320.496,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.26384, dn = +|- 0.0307635, dEa = +|- 0.167414 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 332.008 kJ/mol

C    -0.695038    -0.080264    -0.119021
F    1.66398    -0.643084    -0.51829
F    1.066759    -0.486589    1.54559
H    0.945151    2.01382    -0.733224
H    -0.752053    1.947025    -0.291092
H    0.450849    2.144078    0.971957
C    1.305838    0.231499    0.436189
C    0.261066    1.650533    0.025447
H    -0.964565    0.081354    -1.15545
H    -1.466846    0.212255    0.582107
H    -0.37114    -1.100917    0.051497
""",
)

entry(
    index = 55,
    label = "CHF_r1 + CH4O <=> C2H5FO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.212553,'cm^3/(mol*s)'), n=3.34134, Ea=(111.339,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16803, dn = +|- 0.0204062, dEa = +|- 0.11105 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 125.610 kJ/mol

O    -0.522371    -0.629543    -0.714935
F    0.602106    1.257353    -0.130333
H    1.269877    -0.531067    0.378677
H    -1.639961    1.036518    0.711935
H    -2.507672    -0.116727    -0.367966
H    -1.838322    -0.690112    1.207707
C    0.310205    -0.003851    0.384962
C    -1.73265    0.007182    0.393401
H    -0.363812    -0.165564    -1.559169
""",
)

entry(
    index = 56,
    label = "CF2_r1 + CH4O <=> C2H4F2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.140908,'cm^3/(mol*s)'), n=3.45227, Ea=(176.699,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12809, dn = +|- 0.0158346, dEa = +|- 0.0861712 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 188.137 kJ/mol

O    -0.766409    0.573579    -0.541623
F    0.731944    0.389058    1.088694
F    1.378619    0.096046    -0.932617
H    -1.229825    -1.118235    1.232347
H    -2.511508    -0.281334    0.264719
H    -1.554748    -1.634428    -0.475748
C    0.376699    -0.228909    -0.088206
C    -1.578529    -0.838557    0.249451
H    -0.737404    1.473838    -0.150497
""",
)

entry(
    index = 57,
    label = "CH2 + CH4O <=> C2H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(12.6474,'cm^3/(mol*s)'), n=2.95311, Ea=(59.8071,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06041, dn = +|- 0.00770604, dEa = +|- 0.041936 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 74.961 kJ/mol

O    -0.519683    -0.589358    -0.721104
H    0.655886    1.014894    0.030108
H    1.195239    -0.605699    0.525624
H    -1.701431    1.010338    0.761819
H    -2.501597    -0.135131    -0.367411
H    -1.789645    -0.731388    1.177948
C    0.327162    0.043884    0.404395
C    -1.715083    -0.003579    0.387764
H    -0.430129    -0.129371    -1.569553
""",
)

entry(
    index = 58,
    label = "CH2 + C2H6 <=> C3H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(166.864,'cm^3/(mol*s)'), n=2.82973, Ea=(154.574,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02266, dn = +|- 0.00294339, dEa = +|- 0.0160178 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 166.986 kJ/mol

C    -0.621512    -0.005564    -0.083209
H    1.577964    -0.536165    -0.330681
H    1.092178    -0.378813    1.367612
H    0.90271    1.926672    -0.757861
H    -0.78407    2.006359    -0.316048
H    0.413832    2.084953    0.950966
C    1.433109    0.177929    0.487625
C    0.194329    1.619903    -0.000424
H    -0.936603    0.084465    -1.116766
H    -1.427155    0.243513    0.598362
H    -0.346823    -1.032411    0.090493
""",
)

entry(
    index = 59,
    label = "CBr2 + H2O <=> CH2Br2O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00335251,'cm^3/(mol*s)'), n=4.20006, Ea=(44.8276,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.81103, dn = +|- 0.078026, dEa = +|- 0.424615 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 67.126 kJ/mol

Br    1.082417    -1.484033    -0.390486
Br    0.760079    1.662848    -0.291732
C    0.217249    -0.018504    0.430195
O    -1.485478    -0.200763    -0.087358
H    -1.001636    -0.133294    0.944338
H    -1.772291    0.691175    -0.330237
""",
)

entry(
    index = 60,
    label = "CBr2 + CH4 <=> C2H4Br2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(2.19874,'cm^3/(mol*s)'), n=3.52855, Ea=(62.1777,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0862, dn = +|- 0.0108628, dEa = +|- 0.0591152 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 74.539 kJ/mol

H    0.751426    0.002547    0.863152
Br    -0.959216    -1.556469    -0.399241
Br    -0.902782    1.626676    -0.392919
H    2.149728    -0.934862    0.210123
H    1.353506    -0.007995    -1.122751
H    2.179225    0.89546    0.20832
C    -0.426145    0.024243    0.539774
C    1.660376    -0.01185    -0.088449
""",
)

entry(
    index = 61,
    label = "CCl2 + CH4 <=> C2H4Cl2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(1.33592,'cm^3/(mol*s)'), n=3.60759, Ea=(71.667,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14661, dn = +|- 0.0179743, dEa = +|- 0.0978154 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 85.075 kJ/mol

H    0.726944    0.004526    0.862801
Cl    -0.91109    -1.412889    -0.367983
Cl    -0.861917    1.4788    -0.365574
H    2.134674    -0.935548    0.202243
H    1.336141    -0.004036    -1.126742
H    2.168298    0.893586    0.204938
C    -0.432773    0.024568    0.500971
C    1.645844    -0.011258    -0.092644
""",
)

entry(
    index = 62,
    label = "CCl2 + H2O <=> CH2Cl2O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00446709,'cm^3/(mol*s)'), n=4.16722, Ea=(48.7822,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.78868, dn = +|- 0.0763947, dEa = +|- 0.415737 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 71.077 kJ/mol

Cl    1.027404    -1.340558    -0.354291
Cl    0.736082    1.511108    -0.269505
C    0.25061    -0.012243    0.407489
O    -1.48699    -0.201823    -0.100577
H    -0.951324    -0.131807    0.920361
H    -1.775441    0.692753    -0.328757
""",
)

