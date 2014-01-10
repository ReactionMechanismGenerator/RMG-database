#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

entry(
    index = 1,
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {2,S} {3,S}
""",
    product1 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 C 0 {1,S} {6,D}
6 *2 C 1 {5,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (50100000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.31, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (493, 'K'),
    ),
    reference = Article(
        authors = ["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals',
        journal = "J. Chem. Soc.",
        pages = """940-944""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962GAR/TRO940-944:1",
    ),
    referenceType = "",
    shortDesc = u"""Dominguez et al. (1962). Data derived from fitting a complex mechanism.""",
    longDesc = 
u"""
Dominguez et al. Data derived from fitting to a complex mechanism.
Pressure 0.01-0.32 atm. Excitation : direct photolysis, analysis : GC. 
C2H2 + Tert-C4H9 --> (CH3)3CCH=CH

Was in the rules database with rank=4. Richard moved to the training database and checked with NIST database. NIST squib: 1962GAR/TRO940-944
This is the full rate; NB the degeneracy=2 so the per-site rate is half this.
""",
    history = [
        ("2011-08-09","Richard West <rwest@mit.edu>","action","""New entry. Moved from rules to training, cross-referenced with NIST and PrIMe."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {5,D}
2 *2 C 1 {1,S}
3 *3 O 0 {1,S} {4,S}
4    O 0 {3,S}
5    O 0 {1,D}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *1 C 0 {1,D} {3,D}
3    O 0 {2,D}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+16, 's^-1', '*|/', 2.51189),
        n = -1,
        Ea = (29.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["J. W. Allen", "C. F. Goldsmith", "W. H. Green"],
        title = u'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "???",
        pages = """???-???""",
        year = "2011 (accepted)",
    ),
    referenceType = "theory",
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
""",
    history = [
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
1 C 1 {2,S}
2 O 0 {1,S}
""",
    product1 = 
"""
1 C 0 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
1 H 1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (73700000000.0, 's^-1'),
            n = 0.811,
            Ea = (39578, 'cal/mol'),
            T0 = (1000, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.5e+21, 'cm^3/(mol*s)'),
            n = -1.99,
            Ea = (24000, 'cal/mol'),
            T0 = (1000, 'K'),
        ),
        alpha = 0.844,
        T3 = (900, 'K'),
        T1 = (1, 'K'),
        T2 = (3315, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5},
        comment = 'Dames and Golden 2013',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Dames and Golden 2013
""",
    history = [
        ("Fri Jan 10 15:08:46 2014","enoch dames <enoch.dames@gmail.com>","action","""New entry. test_reaction update """),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
1 C 0 {2,S}
2 C 0 {1,S} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
1 C 0 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
1 C 1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(63100000000.0, 's^-1'), n=0.93, Ea=(17099, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.7e+25, 'cm^3/(mol*s)'), n=-3, Ea=(16533, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.426,
        T3 = (0.3, 'K'),
        T1 = (2278, 'K'),
        T2 = (100000, 'K'),
        efficiencies = {},
        comment = 'Dames 2014',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Dames 2014 IJCK
N2 bath gas. 
Rates valid between 470 - 1200 K. Uncertainties range from 1.5-3 depending on T and P (see original text).
This is a strongly dominant channel.
""",
    history = [
        ("Fri Jan 10 16:46:44 2014","enoch dames <enoch.dames@gmail.com>","action","""New entry. test_new and improved ethoxy decomp rate in N2 """),
    ],
)

entry(
    index = 4,
    label = "2014/Dames",
    reactant1 = 
"""
1 C 0 {2,S}
2 C 0 {1,S} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
1 C 0 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
1 C 1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(63100000000.0, 's^-1'), n=0.93, Ea=(17099, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.7e+25, 'cm^3/(mol*s)'), n=-3, Ea=(16533, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.426,
        T3 = (0.3, 'K'),
        T1 = (2278, 'K'),
        T2 = (100000, 'K'),
        efficiencies = {},
        comment = 'Dames 2014',
    ),
    reference = None,
    referenceType = "theory",
    shortDesc = u"""RRKM/MasterEquation calculation""",
    longDesc = 
u"""
Dames 2014 IJCK
N2 bath gas. 
Rates valid between 470 - 1200 K. Uncertainties range from 1.5-3 depending on T and P (see original text).
This is a strongly dominant channel.
""",
    history = [
        ("Fri Jan 10 16:46:44 2014","enoch dames <enoch.dames@gmail.com>","action","""New entry. test_new and improved ethoxy decomp rate in N2 """),
        ("Fri Jan 10 16:55:55 2014","enoch dames <enoch.dames@gmail.com>","action","""added labels"""),
    ],
)

entry(
    index = 5,
    label = "2014/Dames",
    reactant1 = 
"""
1 C 0 {2,S}
2 C 1 {1,S} {3,S}
3 O 0 {2,S}
""",
    product1 = 
"""
1 C 0 {2,S}
2 C 0 {1,S} {3,D}
3 O 0 {2,D}
""",
    product2 = 
"""
1 H 1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6170000000.0, 's^-1'), n=1.31, Ea=(33759, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.767e+16, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (20782, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1868,
        T3 = (65.19, 'K'),
        T1 = (2568, 'K'),
        T2 = (41226, 'K'),
        efficiencies = {},
        comment = 'Dames 2014',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Dames 2014 IJCK
N2 bath gas. Rates valid between 800 - 1500 K. Uncertainties range from 1.5-3 depending on T and P (see original text)
""",
    history = [
        ("Fri Jan 10 17:22:15 2014","enoch dames <enoch.dames@gmail.com>","action","""New entry. added reaction of CH3CHOH=CH3CHO+H"""),
    ],
)

entry(
    index = 6,
    label = "2014/Dames",
    reactant1 = 
"""
1 C 0 {2,S}
2 C 1 {1,S} {3,S}
3 O 0 {2,S}
""",
    product1 = 
"""
1 C 0 {2,D} {3,S}
2 C 0 {1,D}
3 O 0 {1,S}
""",
    product2 = 
"""
1 H 1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6360000000.0, 's^-1'), n=1.33, Ea=(35975, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (818000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (21512, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.4731,
        T3 = (10, 'K'),
        T1 = (2218, 'K'),
        T2 = (2615, 'K'),
        efficiencies = {},
        comment = 'Dames 2014',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Dames 2014 IJCK
N2 bath gas. Rates valid between 800 - 1500 K. Uncertainties range from 1.5-3 depending on T and P (see original text)
""",
    history = [
        ("Fri Jan 10 17:27:58 2014","enoch dames <enoch.dames@gmail.com>","action","""New entry. added reaction of CH3CHOH=C2H3OH+H"""),
    ],
)

