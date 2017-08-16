#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+10, 's^-1'), n=0.51, Ea=(30.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addD <=> product8
""",
)

entry(
    index = 1,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.03e+10, 's^-1'), n=1.1, Ea=(37, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product4 <=> product16
""",
)

entry(
    index = 2,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39e+11, 's^-1'), n=0.26, Ea=(26.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product22 <=> product25
""",
)

entry(
    index = 3,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e+09, 's^-1'), n=0.63, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_1 <=> prod_2
""",
)

entry(
    index = 4,
    label = "C7H11 <=> C7H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.71e+11, 's^-1'), n=0.2, Ea=(27.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_6 <=> prod_4
""",
)

entry(
    index = 5,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.53e+07, 's^-1'), n=1.05, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_7 <=> prod_8
""",
)

entry(
    index = 6,
    label = "C7H11-3 <=> C7H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.6e+10, 's^-1'), n=0.2, Ea=(9.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_10 <=> prod_11
""",
)

entry(
    index = 7,
    label = "C6H9-5 <=> C6H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.47e+07, 's^-1'), n=0.85, Ea=(10.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_19 <=> prod_2
""",
)

entry(
    index = 8,
    label = "C7H11-5 <=> C7H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+11, 's^-1'), n=0.27, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_20 <=> prod_4
""",
)

entry(
    index = 9,
    label = "C5H7 <=> C5H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.29e+09, 's^-1'), n=0.62, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_21 <=> prod_22
""",
)

entry(
    index = 10,
    label = "C5H5 <=> C5H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.88e+10, 's^-1'), n=0.31, Ea=(12.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_23 <=> prod_24
""",
)

entry(
    index = 11,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.05e+11, 's^-1'), n=0.12, Ea=(12.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_25 <=> prod_26
""",
)

entry(
    index = 12,
    label = "C6H7-3 <=> C6H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.8e+11, 's^-1'), n=0.1, Ea=(11.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_27 <=> prod_28
""",
)

entry(
    index = 13,
    label = "C6H7-5 <=> C6H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.47e+11, 's^-1'), n=0.15, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_29 <=> prod_30
""",
)

entry(
    index = 14,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.6e+07, 's^-1'),
        n = 1.08,
        Ea = (30.4, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 15,
    label = "C_CCCJC <=> 3-methylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.02e+07, 's^-1'),
        n = 1.34,
        Ea = (30.1, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 16,
    label = "C_CCCJCC <=> 3-ethylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+07, 's^-1'),
        n = 1.34,
        Ea = (29.4, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 17,
    label = "CC_CCCJ <=> 2-methylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.61e+08, 's^-1'),
        n = 0.96,
        Ea = (29.4, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling" Trans conformation of pentenyl.
""",
)

entry(
    index = 18,
    label = "C_CC(C)CJ <=> 2-methylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+08, 's^-1'),
        n = 1.02,
        Ea = (29.7, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 19,
    label = "C_C(C)CCJ <=> 1-methylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.82e+08, 's^-1'),
        n = 0.91,
        Ea = (30, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 20,
    label = "C_CC(C)(C)CJ <=> 2,2-dimethylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.41e+08, 's^-1'),
        n = 0.96,
        Ea = (29.3, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 21,
    label = "C_CCCJ(C)C <=> 3,3-dimethylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.02e+06, 's^-1'),
        n = 1.58,
        Ea = (29.7, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 22,
    label = "C_C(C)CCJC <=> 1,3-dimethylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.71e+08, 's^-1'),
        n = 0.99,
        Ea = (29.7, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 23,
    label = "CC(C)_CCCJ <=> 2,2-dimethylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.15e+07, 's^-1'),
        n = 1.24,
        Ea = (30.9, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 24,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.65e+07, 's^-1'),
        n = 1.02,
        Ea = (14.2, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 25,
    label = "C_CCCCJC <=> 3-methylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.64e+06, 's^-1'),
        n = 1.15,
        Ea = (13.9, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 26,
    label = "C_CCCCJ(C)C <=> 3,3-dimethylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.07e+06, 's^-1'),
        n = 1.38,
        Ea = (12.2, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 27,
    label = "CC_CCCCJ <=> 2-methylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.94e+07, 's^-1'),
        n = 0.93,
        Ea = (13.9, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling" Trans conformation of hexenyl.
""",
)

entry(
    index = 28,
    label = "C_CCC(C)CJ <=> 3-methylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.65e+07, 's^-1'),
        n = 0.83,
        Ea = (13.4, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 29,
    label = "C_CC(C)CCJ <=> 2-methylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.25e+07, 's^-1'),
        n = 0.83,
        Ea = (14.1, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 30,
    label = "C_C(C)CCCJ <=> 1-methylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.23e+07, 's^-1'),
        n = 1,
        Ea = (13.5, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 31,
    label = "C_CCC(C)(C)CJ <=> 3,3-dimethylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38e+08, 's^-1'),
        n = 0.75,
        Ea = (12.6, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 32,
    label = "C_CC(C)(C)CCJ <=> 2,2-dimethylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.6e+08, 's^-1'),
        n = 0.76,
        Ea = (13.4, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 33,
    label = "CC(C)_CCCCJ <=> 2,2-dimethylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.9e+06, 's^-1'),
        n = 1.13,
        Ea = (15.6, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 34,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+06, 's^-1'),
        n = 1.08,
        Ea = (6.7, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 35,
    label = "C_CCCCCJC <=> 3-methylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (487000, 's^-1'),
        n = 1.17,
        Ea = (6.3, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 36,
    label = "C_CCCCCJ(C)C <=> 3,3-dimethylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (33000, 's^-1'),
        n = 1.42,
        Ea = (4.7, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 37,
    label = "CC_CCCCCJ <=> 2-methylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.26e+06, 's^-1'),
        n = 1.02,
        Ea = (6.3, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling" Trans conformation of heptenyl.
""",
)

entry(
    index = 38,
    label = "C_CCCC(C)CJ <=> 4-methylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+06, 's^-1'),
        n = 1.05,
        Ea = (5.8, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 39,
    label = "C_CCC(C)CCJ <=> 3-methylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.32e+06, 's^-1'),
        n = 0.84,
        Ea = (5.9, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 40,
    label = "C_CC(C)CCCJ <=> 2-methylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.24e+07, 's^-1'),
        n = 0.79,
        Ea = (6.2, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 41,
    label = "C_C(C)CCCCJ <=> 1-methylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.46e+06, 's^-1'),
        n = 1.02,
        Ea = (6.1, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 42,
    label = "C_CCCC(C)(C)CJ <=> 4,4-dimethylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.19e+07, 's^-1'),
        n = 0.78,
        Ea = (6.2, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 43,
    label = "C_CCC(C)(C)CCJ <=> 3,3-dimethylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.5e+07, 's^-1'),
        n = 0.7,
        Ea = (6.3, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 44,
    label = "C_CC(C)(C)CCCJ <=> 2,2-dimethylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.85e+07, 's^-1'),
        n = 0.63,
        Ea = (6.3, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 45,
    label = "CC(C)_CCCCCJ <=> 2,2-dimethylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (344000, 's^-1'),
        n = 1.1,
        Ea = (7.7, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 46,
    label = "C_CCCCCCJ <=> cycloheptyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (114000, 's^-1'),
        n = 1.2,
        Ea = (6.5, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 47,
    label = "C_CCCCCCJC <=> 3-methylcycloheptyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (21100, 's^-1'),
        n = 1.34,
        Ea = (6.4, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 48,
    label = "C_CCCCCCJ(C)C <=> 3,3-dimethylcycloheptyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(554, 's^-1'), n=1.66, Ea=(4.9, 'kcal/mol', '+|-', 1), T0=(1, 'K')),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 49,
    label = "CC_CCCCCCJ <=> 2-methylcycloheptyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (110000, 's^-1'),
        n = 1.18,
        Ea = (6.5, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 50,
    label = "C_C(C)CCCCCJ <=> 1-methylcycloheptyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (185000, 's^-1'),
        n = 1.07,
        Ea = (6.4, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["K. Wang", "S. Villano", "A. Dean"],
        title = u'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = "J. Phys. Chem. A",
        volume = "119(28)",
        pages = """7205-7221""",
        year = "2015",
    ),
    referenceType = "theory",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 51,
    label = "C5H7-3 <=> C5H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.02676e+11, 's^-1'),
        n = 0.55665,
        Ea = (157.071, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SD_D;doublebond_intra_pri_2H;radadd_intra_cs2H
""",
)

entry(
    index = 52,
    label = "C5H7-5 <=> C5H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.05e+08, 's^-1'),
        n = 1.192,
        Ea = (225.936, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R3_D;doublebond_intra_pri_HDe;radadd_intra_cs2H
""",
)

entry(
    index = 53,
    label = "C3H3 <=> C3H3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.05e+08, 's^-1'),
        n = 1.192,
        Ea = (225.936, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3_T;triplebond_intra_H;radadd_intra_cs2H
""",
)

entry(
    index = 54,
    label = "C5H7-3 <=> C5H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0.19,
        Ea = (125.52, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Guess""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SM;multiplebond_intra;radadd_intra
""",
)

entry(
    index = 55,
    label = "C4H7S <=> C4H7S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.48e+06, 's^-1'),
        n = 1.17,
        Ea = (1.12968, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CBS-QB3, 1d-hr by CAC""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cs-R5_SS_CS;thiyl_intra_H;radadd_intra_csHNd
""",
)

entry(
    index = 56,
    label = "C6H7-7 <=> C6H7-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0.19,
        Ea = (146.44, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Guess""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMM;multiplebond_intra;radadd_intra
""",
)

entry(
    index = 57,
    label = "C5H7S <=> C5H7S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.97e+11, 's^-1'),
        n = 0.1,
        Ea = (44.7688, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""same reaction as above""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: R5_SD_D;doublebond_intra_pri_HNd;radadd_intra_S
""",
)

entry(
    index = 58,
    label = "C5H7 <=> C5H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.73e+10, 's^-1'),
        n = 0.19,
        Ea = (49.7896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""BMK/cbsb7 + 1D-HR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_DS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 59,
    label = "C6H9-7 <=> C6H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.03e+10, 's^-1'),
        n = 0.19,
        Ea = (16.736, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""BMK/cbsb7 + 1D-HR""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_DSS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 60,
    label = "C5H7 <=> C5H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.73e+10, 's^-1'),
        n = 0.19,
        Ea = (49.7896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Guess, i.e. 821""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_MS;multiplebond_intra;radadd_intra_cdsingle
""",
)

entry(
    index = 61,
    label = "C6H9-7 <=> C6H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.03e+10, 's^-1'),
        n = 0.19,
        Ea = (17.1544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Guess, i.e. 822""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_MSR;multiplebond_intra;radadd_intra_cdsingle
""",
)

entry(
    index = 62,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.06e+08, 's^-1'),
        n = 0.19,
        Ea = (39.6643, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_cs2H
""",
)

entry(
    index = 63,
    label = "C_CCCCCJC <=> 3-methylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.22e+09, 's^-1'),
        n = 0.19,
        Ea = (39.5806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csHNd
""",
)

entry(
    index = 64,
    label = "C_CCCCCJ(C)C <=> 3,3-dimethylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.57e+08, 's^-1'),
        n = 0.19,
        Ea = (41.045, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 65,
    label = "C8H13 <=> C8H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.59e+09, 's^-1'),
        n = 0.19,
        Ea = (67.8645, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csHCd
""",
)

entry(
    index = 66,
    label = "C9H15 <=> C9H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.34e+08, 's^-1'),
        n = 0.19,
        Ea = (70.877, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 67,
    label = "C8H11 <=> C8H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.29e+09, 's^-1'),
        n = 0.19,
        Ea = (54.8941, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csHCt
""",
)

entry(
    index = 68,
    label = "C9H13 <=> C9H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.16e+09, 's^-1'),
        n = 0.19,
        Ea = (58.8689, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 69,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.88e+09, 's^-1'),
        n = 0.19,
        Ea = (30.334, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 70,
    label = "CC_CCCCCJ <=> 2-methylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.92e+09, 's^-1'),
        n = 0.19,
        Ea = (41.0032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 71,
    label = "C8H15 <=> C8H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.39e+10, 's^-1'),
        n = 0.19,
        Ea = (40.9195, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 72,
    label = "C9H17 <=> C9H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.49e+09, 's^-1'),
        n = 0.19,
        Ea = (42.4258, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 73,
    label = "C9H15-3 <=> C9H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.62e+10, 's^-1'),
        n = 0.19,
        Ea = (69.2034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 74,
    label = "C10H17 <=> C10H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.59e+09, 's^-1'),
        n = 0.19,
        Ea = (72.2577, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 75,
    label = "C9H13-3 <=> C9H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.08e+09, 's^-1'),
        n = 0.19,
        Ea = (56.2748, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 76,
    label = "C10H15 <=> C10H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.27e+09, 's^-1'),
        n = 0.19,
        Ea = (60.2496, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 77,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.05e+10, 's^-1'),
        n = 0.19,
        Ea = (31.7147, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 78,
    label = "CC(C)_CCCCCJ <=> C8H15-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.19e+08, 's^-1'),
        n = 0.19,
        Ea = (48.4089, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 79,
    label = "C9H17-3 <=> C9H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.03e+09, 's^-1'),
        n = 0.19,
        Ea = (48.3252, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 80,
    label = "C10H19 <=> C10H19-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.62e+08, 's^-1'),
        n = 0.19,
        Ea = (49.7896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 81,
    label = "C10H17-3 <=> C10H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.54e+09, 's^-1'),
        n = 0.19,
        Ea = (76.609, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 82,
    label = "C11H19 <=> C11H19-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+09, 's^-1'),
        n = 0.19,
        Ea = (79.6634, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 83,
    label = "C10H15-3 <=> C10H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.76e+09, 's^-1'),
        n = 0.19,
        Ea = (63.6386, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 84,
    label = "C11H17 <=> C11H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.59e+09, 's^-1'),
        n = 0.19,
        Ea = (67.6134, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 85,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.67e+09, 's^-1'),
        n = 0.19,
        Ea = (39.0786, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 86,
    label = "C8H13-3 <=> C8H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.13e+09, 's^-1'),
        n = 0.19,
        Ea = (44.183, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 87,
    label = "C9H15-5 <=> C9H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.2e+09, 's^-1'),
        n = 0.19,
        Ea = (44.0994, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 88,
    label = "C10H17-5 <=> C10H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.06e+09, 's^-1'),
        n = 0.19,
        Ea = (45.6056, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 89,
    label = "C10H15-5 <=> C10H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.59e+09, 's^-1'),
        n = 0.19,
        Ea = (72.3832, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 90,
    label = "C11H17-3 <=> C11H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.71e+09, 's^-1'),
        n = 0.19,
        Ea = (75.4375, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 91,
    label = "C10H13 <=> C10H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.77e+09, 's^-1'),
        n = 0.19,
        Ea = (59.4546, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 92,
    label = "C11H15 <=> C11H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.29e+09, 's^-1'),
        n = 0.19,
        Ea = (63.3876, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 93,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.8e+10, 's^-1'),
        n = 0.19,
        Ea = (34.8527, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 94,
    label = "C9H15-7 <=> C9H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.07e+08, 's^-1'),
        n = 0.19,
        Ea = (54.7686, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 95,
    label = "C10H17-7 <=> C10H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.95e+09, 's^-1'),
        n = 0.19,
        Ea = (54.6849, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 96,
    label = "C11H19-3 <=> C11H19-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.4e+08, 's^-1'),
        n = 0.19,
        Ea = (56.1911, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 97,
    label = "C11H17-5 <=> C11H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.44e+09, 's^-1'),
        n = 0.19,
        Ea = (82.9687, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 98,
    label = "C12H19 <=> C12H19-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.74e+08, 's^-1'),
        n = 0.19,
        Ea = (86.023, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 99,
    label = "C11H15-3 <=> C11H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.71e+09, 's^-1'),
        n = 0.19,
        Ea = (70.0402, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 100,
    label = "C12H17 <=> C12H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.54e+09, 's^-1'),
        n = 0.19,
        Ea = (74.015, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 101,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.48e+09, 's^-1'),
        n = 0.19,
        Ea = (45.4801, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 102,
    label = "C8H11-3 <=> C8H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.96e+09, 's^-1'),
        n = 0.19,
        Ea = (42.4676, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 103,
    label = "C9H13-5 <=> C9H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.14e+10, 's^-1'),
        n = 0.19,
        Ea = (42.4258, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 104,
    label = "C10H15-7 <=> C10H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.38e+09, 's^-1'),
        n = 0.19,
        Ea = (43.8902, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 105,
    label = "C10H13-3 <=> C10H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.5e+10, 's^-1'),
        n = 0.19,
        Ea = (70.7096, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 106,
    label = "C11H15-5 <=> C11H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.08e+09, 's^-1'),
        n = 0.19,
        Ea = (73.7221, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 107,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+10, 's^-1'),
        n = 0.19,
        Ea = (57.7392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 108,
    label = "C11H13 <=> C11H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.12e+10, 's^-1'),
        n = 0.19,
        Ea = (61.714, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 109,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.71e+10, 's^-1'),
        n = 0.19,
        Ea = (33.1791, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 110,
    label = "C9H13-7 <=> C9H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.58e+08, 's^-1'),
        n = 0.19,
        Ea = (51.6306, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 111,
    label = "C10H15-9 <=> C10H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.87e+09, 's^-1'),
        n = 0.19,
        Ea = (51.5469, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 112,
    label = "C11H17-7 <=> C11H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.7e+08, 's^-1'),
        n = 0.19,
        Ea = (53.0531, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 113,
    label = "C11H15-7 <=> C11H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.19e+09, 's^-1'),
        n = 0.19,
        Ea = (79.8307, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 114,
    label = "C12H17-3 <=> C12H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.19e+08, 's^-1'),
        n = 0.19,
        Ea = (82.885, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 115,
    label = "C11H13-3 <=> C11H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.09e+09, 's^-1'),
        n = 0.19,
        Ea = (66.9022, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 116,
    label = "C12H15 <=> C12H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.8e+08, 's^-1'),
        n = 0.19,
        Ea = (70.8351, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 117,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.12e+09, 's^-1'),
        n = 0.19,
        Ea = (42.3002, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 118,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.83e+10, 's^-1'),
        n = 0.19,
        Ea = (135.185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_2H;radadd_intra_cs2H
""",
)

entry(
    index = 119,
    label = "C_CCCJC <=> 3-methylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.32e+11, 's^-1'),
        n = 0.19,
        Ea = (135.101, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_2H;radadd_intra_csHNd
""",
)

entry(
    index = 120,
    label = "C_CCCJ(C)C <=> 3,3-dimethylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.33e+10, 's^-1'),
        n = 0.19,
        Ea = (136.608, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 121,
    label = "C6H9-9 <=> C6H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.55e+11, 's^-1'),
        n = 0.19,
        Ea = (163.385, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_2H;radadd_intra_csHCd
""",
)

entry(
    index = 122,
    label = "C7H11-7 <=> C7H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.38e+10, 's^-1'),
        n = 0.19,
        Ea = (166.44, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 123,
    label = "C6H7-9 <=> C6H7-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.71e+10, 's^-1'),
        n = 0.19,
        Ea = (150.457, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_2H;radadd_intra_csHCt
""",
)

entry(
    index = 124,
    label = "C7H9-7 <=> C7H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.94e+10, 's^-1'),
        n = 0.19,
        Ea = (154.39, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 125,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.91e+11, 's^-1'),
        n = 0.19,
        Ea = (125.897, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 126,
    label = "CC_CCCJ <=> 2-methylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.14e+11, 's^-1'),
        n = 0.19,
        Ea = (136.566, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 127,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.29e+11, 's^-1'),
        n = 0.19,
        Ea = (136.482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 128,
    label = "C7H13 <=> C7H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.08e+11, 's^-1'),
        n = 0.19,
        Ea = (137.988, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 129,
    label = "C7H11-9 <=> C7H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.68e+11, 's^-1'),
        n = 0.19,
        Ea = (164.766, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 130,
    label = "C8H13-5 <=> C8H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.74e+11, 's^-1'),
        n = 0.19,
        Ea = (167.82, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 131,
    label = "C7H9-9 <=> C7H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.82e+11, 's^-1'),
        n = 0.19,
        Ea = (151.837, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 132,
    label = "C8H11-5 <=> C8H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.34e+11, 's^-1'),
        n = 0.19,
        Ea = (155.77, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 133,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.82e+12, 's^-1'),
        n = 0.19,
        Ea = (127.277, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 134,
    label = "CC(C)_CCCJ <=> C6H11-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.5e+10, 's^-1'),
        n = 0.19,
        Ea = (143.93, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 135,
    label = "C7H13-3 <=> C7H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.81e+11, 's^-1'),
        n = 0.19,
        Ea = (143.846, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 136,
    label = "C8H15-4 <=> C8H15-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.55e+10, 's^-1'),
        n = 0.19,
        Ea = (145.352, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 137,
    label = "C8H13-7 <=> C8H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.12e+11, 's^-1'),
        n = 0.19,
        Ea = (172.13, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 138,
    label = "C9H15-9 <=> C9H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.99e+10, 's^-1'),
        n = 0.19,
        Ea = (175.184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 139,
    label = "C8H11-7 <=> C8H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.05e+11, 's^-1'),
        n = 0.19,
        Ea = (159.201, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 140,
    label = "C9H13-9 <=> C9H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.48e+10, 's^-1'),
        n = 0.19,
        Ea = (163.176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 141,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.98e+11, 's^-1'),
        n = 0.19,
        Ea = (134.641, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 142,
    label = "C6H9-11 <=> C6H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.76e+10, 's^-1'),
        n = 0.19,
        Ea = (139.746, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 143,
    label = "C7H11-11 <=> C7H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.9e+11, 's^-1'),
        n = 0.19,
        Ea = (139.662, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 144,
    label = "C8H13-9 <=> C8H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.23e+11, 's^-1'),
        n = 0.19,
        Ea = (141.126, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 145,
    label = "C8H11-9 <=> C8H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.72e+11, 's^-1'),
        n = 0.19,
        Ea = (167.946, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 146,
    label = "C9H13-11 <=> C9H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.62e+11, 's^-1'),
        n = 0.19,
        Ea = (170.958, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 147,
    label = "C8H9 <=> C8H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.85e+11, 's^-1'),
        n = 0.19,
        Ea = (154.975, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 148,
    label = "C9H11 <=> C9H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.56e+11, 's^-1'),
        n = 0.19,
        Ea = (158.95, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 149,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.08e+12, 's^-1'),
        n = 0.19,
        Ea = (130.415, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 150,
    label = "C7H11-13 <=> C7H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.43e+10, 's^-1'),
        n = 0.19,
        Ea = (150.331, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 151,
    label = "C8H13-11 <=> C8H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.76e+11, 's^-1'),
        n = 0.19,
        Ea = (150.247, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 152,
    label = "C9H15-11 <=> C9H15-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.42e+10, 's^-1'),
        n = 0.19,
        Ea = (151.754, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 153,
    label = "C9H13-13 <=> C9H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.05e+11, 's^-1'),
        n = 0.19,
        Ea = (178.531, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 154,
    label = "C10H15-11 <=> C10H15-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.82e+10, 's^-1'),
        n = 0.19,
        Ea = (181.586, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 155,
    label = "C9H11-3 <=> C9H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.02e+11, 's^-1'),
        n = 0.19,
        Ea = (165.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 156,
    label = "C10H13-5 <=> C10H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.21e+10, 's^-1'),
        n = 0.19,
        Ea = (169.536, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 157,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.87e+11, 's^-1'),
        n = 0.19,
        Ea = (141.043, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 158,
    label = "C6H7-11 <=> C6H7-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.76e+11, 's^-1'),
        n = 0.19,
        Ea = (138.03, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 159,
    label = "C7H9-11 <=> C7H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28e+12, 's^-1'),
        n = 0.19,
        Ea = (137.946, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 160,
    label = "C8H11-11 <=> C8H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.21e+11, 's^-1'),
        n = 0.19,
        Ea = (139.453, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 161,
    label = "C8H9-3 <=> C8H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.49e+12, 's^-1'),
        n = 0.19,
        Ea = (166.23, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 162,
    label = "C9H11-5 <=> C9H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.23e+11, 's^-1'),
        n = 0.19,
        Ea = (169.285, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 163,
    label = "C8H7 <=> C8H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.44e+11, 's^-1'),
        n = 0.19,
        Ea = (153.302, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 164,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.69e+11, 's^-1'),
        n = 0.19,
        Ea = (157.235, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 165,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.81e+12, 's^-1'),
        n = 0.19,
        Ea = (128.742, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 166,
    label = "C7H9-13 <=> C7H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.54e+10, 's^-1'),
        n = 0.19,
        Ea = (147.193, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 167,
    label = "C8H11-13 <=> C8H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.12e+11, 's^-1'),
        n = 0.19,
        Ea = (147.109, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 168,
    label = "C9H13-15 <=> C9H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.81e+10, 's^-1'),
        n = 0.19,
        Ea = (148.574, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 169,
    label = "C9H11-7 <=> C9H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.31e+11, 's^-1'),
        n = 0.19,
        Ea = (175.393, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 170,
    label = "C10H13-7 <=> C10H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.7e+10, 's^-1'),
        n = 0.19,
        Ea = (178.406, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 171,
    label = "C9H9-3 <=> C9H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.5e+10, 's^-1'),
        n = 0.19,
        Ea = (162.423, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 172,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.85e+10, 's^-1'),
        n = 0.19,
        Ea = (166.398, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 173,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.46e+11, 's^-1'),
        n = 0.19,
        Ea = (137.863, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 174,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.86e+09, 's^-1'),
        n = 0.19,
        Ea = (67.9063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_2H;radadd_intra_cs2H
""",
)

entry(
    index = 175,
    label = "C_CCCCJC <=> 3-methylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.52e+10, 's^-1'),
        n = 0.19,
        Ea = (67.8226, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csHNd
""",
)

entry(
    index = 176,
    label = "C_CCCCJ(C)C <=> 3,3-dimethylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.84e+09, 's^-1'),
        n = 0.19,
        Ea = (69.3289, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 177,
    label = "C7H11-15 <=> C7H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.11e+10, 's^-1'),
        n = 0.19,
        Ea = (96.1065, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csHCd
""",
)

entry(
    index = 178,
    label = "C8H13-13 <=> C8H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.16e+10, 's^-1'),
        n = 0.19,
        Ea = (99.1608, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 179,
    label = "C7H9-15 <=> C7H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.05e+10, 's^-1'),
        n = 0.19,
        Ea = (83.1779, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csHCt
""",
)

entry(
    index = 180,
    label = "C8H11-15 <=> C8H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.84e+10, 's^-1'),
        n = 0.19,
        Ea = (87.1109, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 181,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.74e+10, 's^-1'),
        n = 0.19,
        Ea = (58.6178, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 182,
    label = "CC_CCCCJ <=> 2-methylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.04e+10, 's^-1'),
        n = 0.19,
        Ea = (69.287, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 183,
    label = "C7H13-5 <=> C7H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.2e+11, 's^-1'),
        n = 0.19,
        Ea = (69.2034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 184,
    label = "C8H15-6 <=> C8H15-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.53e+10, 's^-1'),
        n = 0.19,
        Ea = (70.7096, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 185,
    label = "C8H13-15 <=> C8H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.57e+11, 's^-1'),
        n = 0.19,
        Ea = (97.4872, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 186,
    label = "C9H15-13 <=> C9H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.28e+10, 's^-1'),
        n = 0.19,
        Ea = (100.542, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 187,
    label = "C8H11-17 <=> C8H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28e+11, 's^-1'),
        n = 0.19,
        Ea = (84.5586, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 188,
    label = "C9H13-17 <=> C9H13-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.15e+11, 's^-1'),
        n = 0.19,
        Ea = (88.4916, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 189,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.84e+11, 's^-1'),
        n = 0.19,
        Ea = (59.9567, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 190,
    label = "CC(C)_CCCCJ <=> C7H13-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.64e+09, 's^-1'),
        n = 0.19,
        Ea = (76.6509, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 191,
    label = "C8H15-8 <=> C8H15-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.81e+10, 's^-1'),
        n = 0.19,
        Ea = (76.5672, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 192,
    label = "C9H17-5 <=> C9H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+10, 's^-1'),
        n = 0.19,
        Ea = (78.0734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 193,
    label = "C9H15-15 <=> C9H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.62e+10, 's^-1'),
        n = 0.19,
        Ea = (104.851, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 194,
    label = "C10H17-9 <=> C10H17-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.59e+10, 's^-1'),
        n = 0.19,
        Ea = (107.905, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 195,
    label = "C9H13-19 <=> C9H13-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.8e+10, 's^-1'),
        n = 0.19,
        Ea = (91.9225, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 196,
    label = "C10H15-13 <=> C10H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.52e+10, 's^-1'),
        n = 0.19,
        Ea = (95.8554, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 197,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.06e+11, 's^-1'),
        n = 0.19,
        Ea = (67.3624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 198,
    label = "C7H11-17 <=> C7H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.8e+10, 's^-1'),
        n = 0.19,
        Ea = (72.425, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 199,
    label = "C8H13-17 <=> C8H13-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.3e+11, 's^-1'),
        n = 0.19,
        Ea = (72.3414, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 200,
    label = "C9H15-17 <=> C9H15-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.27e+10, 's^-1'),
        n = 0.19,
        Ea = (73.8476, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 201,
    label = "C9H13-21 <=> C9H13-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.52e+11, 's^-1'),
        n = 0.19,
        Ea = (100.625, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 202,
    label = "C10H15-15 <=> C10H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.3e+10, 's^-1'),
        n = 0.19,
        Ea = (103.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 203,
    label = "C9H11-9 <=> C9H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.57e+10, 's^-1'),
        n = 0.19,
        Ea = (87.6966, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 204,
    label = "C10H13-9 <=> C10H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.81e+10, 's^-1'),
        n = 0.19,
        Ea = (91.6714, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 205,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.86e+11, 's^-1'),
        n = 0.19,
        Ea = (63.1366, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 206,
    label = "C8H13-19 <=> C8H13-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.45e+09, 's^-1'),
        n = 0.19,
        Ea = (83.0524, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 207,
    label = "C9H15-19 <=> C9H15-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.67e+10, 's^-1'),
        n = 0.19,
        Ea = (82.9687, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 208,
    label = "C10H17-11 <=> C10H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.17e+10, 's^-1'),
        n = 0.19,
        Ea = (84.475, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 209,
    label = "C10H15-17 <=> C10H15-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.46e+10, 's^-1'),
        n = 0.19,
        Ea = (111.253, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 210,
    label = "C11H17-9 <=> C11H17-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.55e+10, 's^-1'),
        n = 0.19,
        Ea = (114.307, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 211,
    label = "C10H13-11 <=> C10H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.72e+10, 's^-1'),
        n = 0.19,
        Ea = (98.324, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 212,
    label = "C11H15-9 <=> C11H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.45e+10, 's^-1'),
        n = 0.19,
        Ea = (102.257, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 213,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.03e+11, 's^-1'),
        n = 0.19,
        Ea = (73.7221, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 214,
    label = "C7H9-17 <=> C7H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.69e+10, 's^-1'),
        n = 0.19,
        Ea = (70.7514, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 215,
    label = "C8H11-19 <=> C8H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.4e+11, 's^-1'),
        n = 0.19,
        Ea = (70.6678, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 216,
    label = "C9H13-23 <=> C9H13-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.53e+10, 's^-1'),
        n = 0.19,
        Ea = (72.174, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 217,
    label = "C9H11-11 <=> C9H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.97e+11, 's^-1'),
        n = 0.19,
        Ea = (98.9516, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 218,
    label = "C10H13-13 <=> C10H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.12e+11, 's^-1'),
        n = 0.19,
        Ea = (102.006, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 219,
    label = "C9H9-5 <=> C9H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.98e+11, 's^-1'),
        n = 0.19,
        Ea = (86.023, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 220,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.78e+11, 's^-1'),
        n = 0.19,
        Ea = (89.956, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 221,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.47e+11, 's^-1'),
        n = 0.19,
        Ea = (61.463, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 222,
    label = "C8H11-21 <=> C8H11-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.1e+09, 's^-1'),
        n = 0.19,
        Ea = (79.8726, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 223,
    label = "C9H13-25 <=> C9H13-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.97e+10, 's^-1'),
        n = 0.19,
        Ea = (79.7889, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 224,
    label = "C10H15-19 <=> C10H15-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.45e+09, 's^-1'),
        n = 0.19,
        Ea = (81.2951, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 225,
    label = "C10H13-15 <=> C10H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.47e+10, 's^-1'),
        n = 0.19,
        Ea = (108.073, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 226,
    label = "C11H15-11 <=> C11H15-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.82e+09, 's^-1'),
        n = 0.19,
        Ea = (111.127, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 227,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.73e+10, 's^-1'),
        n = 0.19,
        Ea = (95.1442, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 228,
    label = "C11H13-5 <=> C11H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.55e+10, 's^-1'),
        n = 0.19,
        Ea = (99.119, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 229,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.53e+10, 's^-1'),
        n = 0.19,
        Ea = (70.5841, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 230,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.31e+10, 's^-1'),
        n = 0.19,
        Ea = (99.4118, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_cs2H
""",
)

entry(
    index = 231,
    label = "C7H11-19 <=> C7H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.48e+10, 's^-1'),
        n = 0.19,
        Ea = (99.3282, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csHNd
""",
)

entry(
    index = 232,
    label = "C8H13-21 <=> C8H13-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.38e+10, 's^-1'),
        n = 0.19,
        Ea = (100.834, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 233,
    label = "C8H11-23 <=> C8H11-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.11e+11, 's^-1'),
        n = 0.19,
        Ea = (127.612, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csHCd
""",
)

entry(
    index = 234,
    label = "C9H13-27 <=> C9H13-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.14e+10, 's^-1'),
        n = 0.19,
        Ea = (130.666, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 235,
    label = "C8H9-5 <=> C8H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.52e+10, 's^-1'),
        n = 0.19,
        Ea = (114.683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csHCt
""",
)

entry(
    index = 236,
    label = "C9H11-13 <=> C9H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.97e+10, 's^-1'),
        n = 0.19,
        Ea = (118.616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 237,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.09e+11, 's^-1'),
        n = 0.19,
        Ea = (90.0815, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 238,
    label = "C7H11-21 <=> C7H11-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.19e+10, 's^-1'),
        n = 0.19,
        Ea = (100.793, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 239,
    label = "C8H13-23 <=> C8H13-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.93e+11, 's^-1'),
        n = 0.19,
        Ea = (100.709, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 240,
    label = "C9H15-21 <=> C9H15-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.49e+11, 's^-1'),
        n = 0.19,
        Ea = (102.173, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 241,
    label = "C9H13-29 <=> C9H13-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.93e+11, 's^-1'),
        n = 0.19,
        Ea = (128.993, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 242,
    label = "C10H15-21 <=> C10H15-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.96e+11, 's^-1'),
        n = 0.19,
        Ea = (132.005, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 243,
    label = "C9H11-15 <=> C9H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.45e+11, 's^-1'),
        n = 0.19,
        Ea = (116.022, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 244,
    label = "C10H13-17 <=> C10H13-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.11e+11, 's^-1'),
        n = 0.19,
        Ea = (119.997, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 245,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.3e+12, 's^-1'),
        n = 0.19,
        Ea = (91.4622, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 246,
    label = "C8H13-25 <=> C8H13-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.79e+10, 's^-1'),
        n = 0.19,
        Ea = (108.156, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 247,
    label = "C9H15-23 <=> C9H15-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.3e+11, 's^-1'),
        n = 0.19,
        Ea = (108.073, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 248,
    label = "C10H17-13 <=> C10H17-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.26e+10, 's^-1'),
        n = 0.19,
        Ea = (109.579, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 249,
    label = "C10H15-23 <=> C10H15-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.51e+11, 's^-1'),
        n = 0.19,
        Ea = (136.357, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 250,
    label = "C11H17-11 <=> C11H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.29e+10, 's^-1'),
        n = 0.19,
        Ea = (139.411, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 251,
    label = "C10H13-19 <=> C10H13-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.54e+10, 's^-1'),
        n = 0.19,
        Ea = (123.428, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 252,
    label = "C11H15-13 <=> C11H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.79e+10, 's^-1'),
        n = 0.19,
        Ea = (127.361, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 253,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.85e+11, 's^-1'),
        n = 0.19,
        Ea = (98.8261, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 254,
    label = "C8H11-25 <=> C8H11-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.84e+10, 's^-1'),
        n = 0.19,
        Ea = (103.931, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 255,
    label = "C9H13-31 <=> C9H13-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.51e+11, 's^-1'),
        n = 0.19,
        Ea = (103.847, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 256,
    label = "C10H15-25 <=> C10H15-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.8e+10, 's^-1'),
        n = 0.19,
        Ea = (105.353, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 257,
    label = "C10H13-21 <=> C10H13-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.1e+11, 's^-1'),
        n = 0.19,
        Ea = (132.131, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 258,
    label = "C11H15-15 <=> C11H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.16e+11, 's^-1'),
        n = 0.19,
        Ea = (135.185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 259,
    label = "C10H11-9 <=> C10H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.04e+11, 's^-1'),
        n = 0.19,
        Ea = (119.202, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 260,
    label = "C11H13-7 <=> C11H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.84e+11, 's^-1'),
        n = 0.19,
        Ea = (123.135, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 261,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.71e+11, 's^-1'),
        n = 0.19,
        Ea = (94.6421, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 262,
    label = "C9H13-33 <=> C9H13-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.74e+10, 's^-1'),
        n = 0.19,
        Ea = (114.558, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 263,
    label = "C10H15-27 <=> C10H15-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.26e+11, 's^-1'),
        n = 0.19,
        Ea = (114.474, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 264,
    label = "C11H17-13 <=> C11H17-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.16e+10, 's^-1'),
        n = 0.19,
        Ea = (115.939, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 265,
    label = "C11H15-17 <=> C11H15-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.47e+11, 's^-1'),
        n = 0.19,
        Ea = (142.758, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 266,
    label = "C12H17-5 <=> C12H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.16e+10, 's^-1'),
        n = 0.19,
        Ea = (145.771, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 267,
    label = "C11H13-9 <=> C11H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.32e+10, 's^-1'),
        n = 0.19,
        Ea = (129.788, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 268,
    label = "C12H15-3 <=> C12H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.59e+10, 's^-1'),
        n = 0.19,
        Ea = (133.762, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 269,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.77e+11, 's^-1'),
        n = 0.19,
        Ea = (105.228, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 270,
    label = "C8H9-7 <=> C8H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.26e+11, 's^-1'),
        n = 0.19,
        Ea = (102.257, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 271,
    label = "C9H11-17 <=> C9H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.15e+11, 's^-1'),
        n = 0.19,
        Ea = (102.173, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 272,
    label = "C10H13-23 <=> C10H13-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.3e+11, 's^-1'),
        n = 0.19,
        Ea = (103.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 273,
    label = "C10H11-11 <=> C10H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.07e+12, 's^-1'),
        n = 0.19,
        Ea = (130.457, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 274,
    label = "C11H13-11 <=> C11H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.03e+11, 's^-1'),
        n = 0.19,
        Ea = (133.511, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 275,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.32e+11, 's^-1'),
        n = 0.19,
        Ea = (117.529, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 276,
    label = "C11H11 <=> C11H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.79e+11, 's^-1'),
        n = 0.19,
        Ea = (121.462, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 277,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+12, 's^-1'),
        n = 0.19,
        Ea = (92.9266, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 278,
    label = "C9H11-19 <=> C9H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+10, 's^-1'),
        n = 0.19,
        Ea = (111.378, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 279,
    label = "C10H13-25 <=> C10H13-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8e+10, 's^-1'),
        n = 0.19,
        Ea = (111.294, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 280,
    label = "C11H15-19 <=> C11H15-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+10, 's^-1'),
        n = 0.19,
        Ea = (112.801, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 281,
    label = "C11H13-13 <=> C11H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.35e+10, 's^-1'),
        n = 0.19,
        Ea = (139.578, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 282,
    label = "C12H15-5 <=> C12H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.65e+10, 's^-1'),
        n = 0.19,
        Ea = (142.633, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 283,
    label = "C11H11-3 <=> C11H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.65e+10, 's^-1'),
        n = 0.19,
        Ea = (126.65, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 284,
    label = "C12H13 <=> C12H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.19e+10, 's^-1'),
        n = 0.19,
        Ea = (130.583, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 285,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.76e+11, 's^-1'),
        n = 0.19,
        Ea = (102.09, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 286,
    label = "C_C(C)CCCCJ <=> 1-methylcyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.83e+08, 's^-1'),
        n = 0.19,
        Ea = (37.9489, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_cs2H
""",
)

entry(
    index = 287,
    label = "C8H15-10 <=> C8H15-11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.77e+09, 's^-1'),
        n = 0.19,
        Ea = (37.8652, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csHNd
""",
)

entry(
    index = 288,
    label = "C9H17-7 <=> C9H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.97e+08, 's^-1'),
        n = 0.19,
        Ea = (39.3714, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 289,
    label = "C9H15-25 <=> C9H15-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.24e+09, 's^-1'),
        n = 0.19,
        Ea = (66.149, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csHCd
""",
)

entry(
    index = 290,
    label = "C10H17-15 <=> C10H17-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.18e+08, 's^-1'),
        n = 0.19,
        Ea = (69.2034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 291,
    label = "C9H13-35 <=> C9H13-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.61e+09, 's^-1'),
        n = 0.19,
        Ea = (53.2205, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csHCt
""",
)

entry(
    index = 292,
    label = "C10H15-29 <=> C10H15-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.45e+09, 's^-1'),
        n = 0.19,
        Ea = (57.1534, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 293,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.1e+09, 's^-1'),
        n = 0.19,
        Ea = (28.6604, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 294,
    label = "C8H15-12 <=> C8H15-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+09, 's^-1'),
        n = 0.19,
        Ea = (39.3296, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 295,
    label = "C9H17-9 <=> C9H17-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.74e+10, 's^-1'),
        n = 0.19,
        Ea = (39.2459, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 296,
    label = "C10H19-3 <=> C10H19-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.36e+09, 's^-1'),
        n = 0.19,
        Ea = (40.7522, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 297,
    label = "C10H17-17 <=> C10H17-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.03e+10, 's^-1'),
        n = 0.19,
        Ea = (67.5298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 298,
    label = "C11H19-5 <=> C11H19-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.74e+09, 's^-1'),
        n = 0.19,
        Ea = (70.5841, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 299,
    label = "C10H15-31 <=> C10H15-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.01e+10, 's^-1'),
        n = 0.19,
        Ea = (54.6012, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 300,
    label = "C11H17-15 <=> C11H17-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.09e+09, 's^-1'),
        n = 0.19,
        Ea = (58.5342, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 301,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.82e+10, 's^-1'),
        n = 0.19,
        Ea = (29.9993, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 302,
    label = "C9H17-11 <=> C9H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.24e+08, 's^-1'),
        n = 0.19,
        Ea = (46.6934, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 303,
    label = "C10H19-5 <=> C10H19-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.79e+09, 's^-1'),
        n = 0.19,
        Ea = (46.6098, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 304,
    label = "C11H21 <=> C11H21-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.52e+08, 's^-1'),
        n = 0.19,
        Ea = (48.116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 305,
    label = "C11H19-7 <=> C11H19-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.43e+09, 's^-1'),
        n = 0.19,
        Ea = (74.8936, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 306,
    label = "C12H21 <=> C12H21-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+09, 's^-1'),
        n = 0.19,
        Ea = (77.9479, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 307,
    label = "C11H17-17 <=> C11H17-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.21e+09, 's^-1'),
        n = 0.19,
        Ea = (61.965, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 308,
    label = "C12H19-3 <=> C12H19-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.99e+09, 's^-1'),
        n = 0.19,
        Ea = (65.898, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 309,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.34e+09, 's^-1'),
        n = 0.19,
        Ea = (37.405, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 310,
    label = "C9H15-27 <=> C9H15-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.42e+09, 's^-1'),
        n = 0.19,
        Ea = (42.4676, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 311,
    label = "C10H17-19 <=> C10H17-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.03e+10, 's^-1'),
        n = 0.19,
        Ea = (42.3839, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 312,
    label = "C11H19-9 <=> C11H19-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.58e+09, 's^-1'),
        n = 0.19,
        Ea = (43.8902, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 313,
    label = "C11H17-19 <=> C11H17-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+10, 's^-1'),
        n = 0.19,
        Ea = (70.6678, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 314,
    label = "C12H19-5 <=> C12H19-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.39e+09, 's^-1'),
        n = 0.19,
        Ea = (73.7221, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 315,
    label = "C11H15-21 <=> C11H15-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.97e+09, 's^-1'),
        n = 0.19,
        Ea = (57.7392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 316,
    label = "C12H17-7 <=> C12H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.37e+09, 's^-1'),
        n = 0.19,
        Ea = (61.6722, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 317,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.26e+10, 's^-1'),
        n = 0.19,
        Ea = (33.1791, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 318,
    label = "C10H17-21 <=> C10H17-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.08e+08, 's^-1'),
        n = 0.19,
        Ea = (53.095, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 319,
    label = "C11H19-11 <=> C11H19-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.68e+09, 's^-1'),
        n = 0.19,
        Ea = (53.0113, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 320,
    label = "C12H21-3 <=> C12H21-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.25e+08, 's^-1'),
        n = 0.19,
        Ea = (54.4757, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 321,
    label = "C12H19-7 <=> C12H19-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.3e+09, 's^-1'),
        n = 0.19,
        Ea = (81.2951, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 322,
    label = "C13H21 <=> C13H21-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.22e+09, 's^-1'),
        n = 0.19,
        Ea = (84.3494, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 323,
    label = "C12H17-9 <=> C12H17-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.14e+09, 's^-1'),
        n = 0.19,
        Ea = (68.3666, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 324,
    label = "C13H19 <=> C13H19-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.93e+09, 's^-1'),
        n = 0.19,
        Ea = (72.2995, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 325,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.1e+09, 's^-1'),
        n = 0.19,
        Ea = (43.7646, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 326,
    label = "C9H13-37 <=> C9H13-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.7e+09, 's^-1'),
        n = 0.19,
        Ea = (40.794, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 327,
    label = "C10H15-33 <=> C10H15-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.68e+10, 's^-1'),
        n = 0.19,
        Ea = (40.7103, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 328,
    label = "C11H17-21 <=> C11H17-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.72e+09, 's^-1'),
        n = 0.19,
        Ea = (42.2166, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 329,
    label = "C11H15-23 <=> C11H15-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.13e+10, 's^-1'),
        n = 0.19,
        Ea = (68.9942, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 330,
    label = "C12H17-11 <=> C12H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.86e+09, 's^-1'),
        n = 0.19,
        Ea = (72.0485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 331,
    label = "C11H13-15 <=> C11H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.56e+10, 's^-1'),
        n = 0.19,
        Ea = (56.0656, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 332,
    label = "C12H15-7 <=> C12H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.4e+10, 's^-1'),
        n = 0.19,
        Ea = (59.9986, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 333,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.89e+10, 's^-1'),
        n = 0.19,
        Ea = (31.4637, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 334,
    label = "C10H15-35 <=> C10H15-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.23e+08, 's^-1'),
        n = 0.19,
        Ea = (49.9151, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 335,
    label = "C11H17-23 <=> C11H17-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.34e+09, 's^-1'),
        n = 0.19,
        Ea = (49.8314, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 336,
    label = "C12H19-9 <=> C12H19-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.88e+08, 's^-1'),
        n = 0.19,
        Ea = (51.3377, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 337,
    label = "C12H17-13 <=> C12H17-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.73e+09, 's^-1'),
        n = 0.19,
        Ea = (78.1153, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 338,
    label = "C13H19-3 <=> C13H19-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.74e+08, 's^-1'),
        n = 0.19,
        Ea = (81.1696, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 339,
    label = "C12H15-9 <=> C12H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.36e+09, 's^-1'),
        n = 0.19,
        Ea = (65.1867, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 340,
    label = "C13H17 <=> C13H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.23e+09, 's^-1'),
        n = 0.19,
        Ea = (69.1197, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 341,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.15e+09, 's^-1'),
        n = 0.19,
        Ea = (40.6266, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 342,
    label = "C_C(C)CCJ <=> 1-methylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.29e+10, 's^-1'),
        n = 0.19,
        Ea = (133.511, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_2H;radadd_intra_cs2H
""",
)

entry(
    index = 343,
    label = "C_C(C)CCJC <=> 1,3-dimethylcyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.66e+11, 's^-1'),
        n = 0.19,
        Ea = (133.428, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csHNd
""",
)

entry(
    index = 344,
    label = "C7H13-8 <=> C7H13-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.16e+10, 's^-1'),
        n = 0.19,
        Ea = (134.892, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 345,
    label = "C7H11-23 <=> C7H11-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.94e+11, 's^-1'),
        n = 0.19,
        Ea = (161.712, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csHCd
""",
)

entry(
    index = 346,
    label = "C8H13-27 <=> C8H13-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.48e+10, 's^-1'),
        n = 0.19,
        Ea = (164.766, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 347,
    label = "C7H9-19 <=> C7H9-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.64e+10, 's^-1'),
        n = 0.19,
        Ea = (148.741, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csHCt
""",
)

entry(
    index = 348,
    label = "C8H11-27 <=> C8H11-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.67e+10, 's^-1'),
        n = 0.19,
        Ea = (152.716, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 349,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.64e+11, 's^-1'),
        n = 0.19,
        Ea = (124.181, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 350,
    label = "C6H11-4 <=> C6H11-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.43e+11, 's^-1'),
        n = 0.19,
        Ea = (134.85, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 351,
    label = "C7H13-10 <=> C7H13-11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.04e+12, 's^-1'),
        n = 0.19,
        Ea = (134.808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 352,
    label = "C8H15-14 <=> C8H15-15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.6e+11, 's^-1'),
        n = 0.19,
        Ea = (136.273, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 353,
    label = "C8H13-29 <=> C8H13-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+12, 's^-1'),
        n = 0.19,
        Ea = (163.092, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 354,
    label = "C9H15-29 <=> C9H15-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.43e+11, 's^-1'),
        n = 0.19,
        Ea = (166.105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 355,
    label = "C8H11-29 <=> C8H11-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.03e+11, 's^-1'),
        n = 0.19,
        Ea = (150.122, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 356,
    label = "C9H13-39 <=> C9H13-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.42e+11, 's^-1'),
        n = 0.19,
        Ea = (154.097, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 357,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.28e+12, 's^-1'),
        n = 0.19,
        Ea = (125.562, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 358,
    label = "C7H13-12 <=> C7H13-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.13e+10, 's^-1'),
        n = 0.19,
        Ea = (142.256, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 359,
    label = "C8H15-16 <=> C8H15-17",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.26e+11, 's^-1'),
        n = 0.19,
        Ea = (142.172, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 360,
    label = "C9H17-13 <=> C9H17-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.69e+10, 's^-1'),
        n = 0.19,
        Ea = (143.679, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 361,
    label = "C9H15-31 <=> C9H15-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.65e+11, 's^-1'),
        n = 0.19,
        Ea = (170.456, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 362,
    label = "C10H17-23 <=> C10H17-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.49e+10, 's^-1'),
        n = 0.19,
        Ea = (173.51, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 363,
    label = "C9H13-41 <=> C9H13-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.32e+11, 's^-1'),
        n = 0.19,
        Ea = (157.528, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 364,
    label = "C10H15-37 <=> C10H15-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.19e+11, 's^-1'),
        n = 0.19,
        Ea = (161.461, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 365,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.98e+11, 's^-1'),
        n = 0.19,
        Ea = (132.926, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 366,
    label = "C7H11-25 <=> C7H11-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.45e+10, 's^-1'),
        n = 0.19,
        Ea = (138.03, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 367,
    label = "C8H13-31 <=> C8H13-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.12e+11, 's^-1'),
        n = 0.19,
        Ea = (137.946, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 368,
    label = "C9H15-33 <=> C9H15-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.54e+11, 's^-1'),
        n = 0.19,
        Ea = (139.453, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 369,
    label = "C9H13-43 <=> C9H13-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.15e+11, 's^-1'),
        n = 0.19,
        Ea = (166.23, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 370,
    label = "C10H15-39 <=> C10H15-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.03e+11, 's^-1'),
        n = 0.19,
        Ea = (169.285, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 371,
    label = "C9H11-21 <=> C9H11-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.56e+11, 's^-1'),
        n = 0.19,
        Ea = (153.302, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 372,
    label = "C10H13-27 <=> C10H13-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.21e+11, 's^-1'),
        n = 0.19,
        Ea = (157.235, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 373,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.35e+12, 's^-1'),
        n = 0.19,
        Ea = (128.742, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 374,
    label = "C8H13-33 <=> C8H13-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.03e+10, 's^-1'),
        n = 0.19,
        Ea = (148.616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 375,
    label = "C9H15-35 <=> C9H15-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.2e+11, 's^-1'),
        n = 0.19,
        Ea = (148.574, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 376,
    label = "C10H17-25 <=> C10H17-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.52e+10, 's^-1'),
        n = 0.19,
        Ea = (150.038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 377,
    label = "C10H15-41 <=> C10H15-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.57e+11, 's^-1'),
        n = 0.19,
        Ea = (176.858, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 378,
    label = "C11H17-25 <=> C11H17-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.27e+10, 's^-1'),
        n = 0.19,
        Ea = (179.87, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 379,
    label = "C10H13-29 <=> C10H13-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28e+11, 's^-1'),
        n = 0.19,
        Ea = (163.887, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 380,
    label = "C11H15-25 <=> C11H15-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.15e+11, 's^-1'),
        n = 0.19,
        Ea = (167.862, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 381,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.84e+11, 's^-1'),
        n = 0.19,
        Ea = (139.327, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 382,
    label = "C7H9-21 <=> C7H9-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.21e+11, 's^-1'),
        n = 0.19,
        Ea = (136.357, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 383,
    label = "C8H11-31 <=> C8H11-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.6e+12, 's^-1'),
        n = 0.19,
        Ea = (136.273, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 384,
    label = "C9H13-45 <=> C9H13-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.01e+11, 's^-1'),
        n = 0.19,
        Ea = (137.737, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 385,
    label = "C9H11-23 <=> C9H11-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.87e+12, 's^-1'),
        n = 0.19,
        Ea = (164.557, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 386,
    label = "C10H13-31 <=> C10H13-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.29e+11, 's^-1'),
        n = 0.19,
        Ea = (167.569, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 387,
    label = "C9H9-7 <=> C9H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.3e+11, 's^-1'),
        n = 0.19,
        Ea = (151.586, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 388,
    label = "C10H11-13 <=> C10H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.37e+11, 's^-1'),
        n = 0.19,
        Ea = (155.561, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 389,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.51e+12, 's^-1'),
        n = 0.19,
        Ea = (127.026, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 390,
    label = "C8H11-33 <=> C8H11-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.93e+10, 's^-1'),
        n = 0.19,
        Ea = (145.478, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 391,
    label = "C9H13-47 <=> C9H13-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.4e+11, 's^-1'),
        n = 0.19,
        Ea = (145.394, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 392,
    label = "C10H15-43 <=> C10H15-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.51e+10, 's^-1'),
        n = 0.19,
        Ea = (146.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 393,
    label = "C10H13-33 <=> C10H13-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.63e+11, 's^-1'),
        n = 0.19,
        Ea = (173.678, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 394,
    label = "C11H15-27 <=> C11H15-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.62e+10, 's^-1'),
        n = 0.19,
        Ea = (176.732, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 395,
    label = "C10H11-15 <=> C10H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.13e+10, 's^-1'),
        n = 0.19,
        Ea = (160.749, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 396,
    label = "C11H13-17 <=> C11H13-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.31e+10, 's^-1'),
        n = 0.19,
        Ea = (164.682, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 397,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.07e+11, 's^-1'),
        n = 0.19,
        Ea = (136.189, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 398,
    label = "C_C(C)CCCJ <=> 1-methylcyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.07e+09, 's^-1'),
        n = 0.19,
        Ea = (66.1909, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_cs2H
""",
)

entry(
    index = 399,
    label = "C7H13-14 <=> C7H13-15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.4e+10, 's^-1'),
        n = 0.19,
        Ea = (66.149, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csHNd
""",
)

entry(
    index = 400,
    label = "C8H15-18 <=> C8H15-19",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+10, 's^-1'),
        n = 0.19,
        Ea = (67.6134, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 401,
    label = "C8H13-35 <=> C8H13-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.14e+10, 's^-1'),
        n = 0.19,
        Ea = (94.391, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csHCd
""",
)

entry(
    index = 402,
    label = "C9H15-37 <=> C9H15-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.46e+10, 's^-1'),
        n = 0.19,
        Ea = (97.4454, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 403,
    label = "C8H11-35 <=> C8H11-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.56e+10, 's^-1'),
        n = 0.19,
        Ea = (81.4625, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csHCt
""",
)

entry(
    index = 404,
    label = "C9H13-49 <=> C9H13-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.3e+10, 's^-1'),
        n = 0.19,
        Ea = (85.4373, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 405,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.68e+10, 's^-1'),
        n = 0.19,
        Ea = (56.9024, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 406,
    label = "C7H13-16 <=> C7H13-17",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.8e+10, 's^-1'),
        n = 0.19,
        Ea = (67.5716, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 407,
    label = "C8H15-20 <=> C8H15-21",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.75e+11, 's^-1'),
        n = 0.19,
        Ea = (67.4879, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 408,
    label = "C9H17-15 <=> C9H17-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.91e+10, 's^-1'),
        n = 0.19,
        Ea = (68.9942, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 409,
    label = "C9H15-39 <=> C9H15-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.22e+11, 's^-1'),
        n = 0.19,
        Ea = (95.7718, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 410,
    label = "C10H17-27 <=> C10H17-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.1e+10, 's^-1'),
        n = 0.19,
        Ea = (98.8261, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 411,
    label = "C9H13-51 <=> C9H13-52",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.6e+11, 's^-1'),
        n = 0.19,
        Ea = (82.8432, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 412,
    label = "C10H15-45 <=> C10H15-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.44e+11, 's^-1'),
        n = 0.19,
        Ea = (86.7762, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 413,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.05e+11, 's^-1'),
        n = 0.19,
        Ea = (58.2831, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 414,
    label = "C8H15-22 <=> C8H15-23",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.3e+09, 's^-1'),
        n = 0.19,
        Ea = (74.9354, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 415,
    label = "C9H17-17 <=> C9H17-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.01e+10, 's^-1'),
        n = 0.19,
        Ea = (74.8936, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 416,
    label = "C10H19-7 <=> C10H19-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.51e+10, 's^-1'),
        n = 0.19,
        Ea = (76.358, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 417,
    label = "C10H17-29 <=> C10H17-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.03e+10, 's^-1'),
        n = 0.19,
        Ea = (103.177, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 418,
    label = "C11H19-13 <=> C11H19-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.99e+10, 's^-1'),
        n = 0.19,
        Ea = (106.19, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 419,
    label = "C10H15-47 <=> C10H15-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.5e+10, 's^-1'),
        n = 0.19,
        Ea = (90.207, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 420,
    label = "C11H17-27 <=> C11H17-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.15e+10, 's^-1'),
        n = 0.19,
        Ea = (94.1818, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 421,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.32e+11, 's^-1'),
        n = 0.19,
        Ea = (65.647, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 422,
    label = "C8H13-37 <=> C8H13-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.25e+10, 's^-1'),
        n = 0.19,
        Ea = (70.7514, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 423,
    label = "C9H15-41 <=> C9H15-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.63e+11, 's^-1'),
        n = 0.19,
        Ea = (70.6678, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 424,
    label = "C10H17-31 <=> C10H17-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.08e+10, 's^-1'),
        n = 0.19,
        Ea = (72.1322, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 425,
    label = "C10H15-49 <=> C10H15-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.9e+11, 's^-1'),
        n = 0.19,
        Ea = (98.9516, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 426,
    label = "C11H17-29 <=> C11H17-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.38e+10, 's^-1'),
        n = 0.19,
        Ea = (102.006, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 427,
    label = "C10H13-35 <=> C10H13-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.46e+10, 's^-1'),
        n = 0.19,
        Ea = (86.023, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 428,
    label = "C11H15-29 <=> C11H15-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.52e+10, 's^-1'),
        n = 0.19,
        Ea = (89.956, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 429,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.58e+11, 's^-1'),
        n = 0.19,
        Ea = (61.4211, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 430,
    label = "C9H15-43 <=> C9H15-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.06e+09, 's^-1'),
        n = 0.19,
        Ea = (81.337, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 431,
    label = "C10H17-33 <=> C10H17-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.84e+10, 's^-1'),
        n = 0.19,
        Ea = (81.2533, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 432,
    label = "C11H19-15 <=> C11H19-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.47e+10, 's^-1'),
        n = 0.19,
        Ea = (82.7595, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 433,
    label = "C11H17-31 <=> C11H17-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.83e+10, 's^-1'),
        n = 0.19,
        Ea = (109.537, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 434,
    label = "C12H19-11 <=> C12H19-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.93e+10, 's^-1'),
        n = 0.19,
        Ea = (112.591, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 435,
    label = "C11H15-31 <=> C11H15-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.4e+10, 's^-1'),
        n = 0.19,
        Ea = (96.6086, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 436,
    label = "C12H17-15 <=> C12H17-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.06e+10, 's^-1'),
        n = 0.19,
        Ea = (100.542, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 437,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28e+11, 's^-1'),
        n = 0.19,
        Ea = (72.0485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 438,
    label = "C8H11-37 <=> C8H11-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.86e+10, 's^-1'),
        n = 0.19,
        Ea = (69.036, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 439,
    label = "C9H13-53 <=> C9H13-54",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.25e+11, 's^-1'),
        n = 0.19,
        Ea = (68.9523, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 440,
    label = "C10H15-51 <=> C10H15-52",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.07e+11, 's^-1'),
        n = 0.19,
        Ea = (70.4586, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 441,
    label = "C10H13-37 <=> C10H13-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.96e+11, 's^-1'),
        n = 0.19,
        Ea = (97.2362, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 442,
    label = "C11H15-33 <=> C11H15-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.4e+11, 's^-1'),
        n = 0.19,
        Ea = (100.29, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 443,
    label = "C10H11-17 <=> C10H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.47e+11, 's^-1'),
        n = 0.19,
        Ea = (84.3076, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 444,
    label = "C11H13-19 <=> C11H13-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.22e+11, 's^-1'),
        n = 0.19,
        Ea = (88.2824, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 445,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.34e+11, 's^-1'),
        n = 0.19,
        Ea = (59.7475, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 446,
    label = "C9H13-55 <=> C9H13-56",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.12e+09, 's^-1'),
        n = 0.19,
        Ea = (78.199, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 447,
    label = "C10H15-53 <=> C10H15-54",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.71e+10, 's^-1'),
        n = 0.19,
        Ea = (78.1153, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 448,
    label = "C11H17-33 <=> C11H17-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.32e+09, 's^-1'),
        n = 0.19,
        Ea = (79.5797, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 449,
    label = "C11H15-35 <=> C11H15-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.34e+10, 's^-1'),
        n = 0.19,
        Ea = (106.399, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 450,
    label = "C12H17-17 <=> C12H17-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.23e+10, 's^-1'),
        n = 0.19,
        Ea = (109.453, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 451,
    label = "C11H13-21 <=> C11H13-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.16e+10, 's^-1'),
        n = 0.19,
        Ea = (93.4706, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 452,
    label = "C12H15-11 <=> C12H15-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.94e+10, 's^-1'),
        n = 0.19,
        Ea = (97.4035, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 453,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.16e+10, 's^-1'),
        n = 0.19,
        Ea = (68.8686, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 454,
    label = "C7H11-27 <=> C7H11-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.64e+10, 's^-1'),
        n = 0.19,
        Ea = (97.6964, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_cs2H
""",
)

entry(
    index = 455,
    label = "C8H13-39 <=> C8H13-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.19e+11, 's^-1'),
        n = 0.19,
        Ea = (97.6127, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csHNd
""",
)

entry(
    index = 456,
    label = "C9H15-45 <=> C9H15-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.98e+10, 's^-1'),
        n = 0.19,
        Ea = (99.119, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 457,
    label = "C9H13-57 <=> C9H13-58",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.39e+11, 's^-1'),
        n = 0.19,
        Ea = (125.897, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csHCd
""",
)

entry(
    index = 458,
    label = "C10H15-55 <=> C10H15-56",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.92e+10, 's^-1'),
        n = 0.19,
        Ea = (128.951, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 459,
    label = "C9H11-25 <=> C9H11-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.9e+10, 's^-1'),
        n = 0.19,
        Ea = (112.968, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csHCt
""",
)

entry(
    index = 460,
    label = "C10H13-39 <=> C10H13-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.21e+10, 's^-1'),
        n = 0.19,
        Ea = (116.901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 461,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.61e+11, 's^-1'),
        n = 0.19,
        Ea = (88.4079, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 462,
    label = "C8H13-41 <=> C8H13-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.02e+11, 's^-1'),
        n = 0.19,
        Ea = (99.0771, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 463,
    label = "C9H15-47 <=> C9H15-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.42e+11, 's^-1'),
        n = 0.19,
        Ea = (98.9934, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 464,
    label = "C10H17-35 <=> C10H17-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.86e+11, 's^-1'),
        n = 0.19,
        Ea = (100.5, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 465,
    label = "C10H15-57 <=> C10H15-58",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.67e+11, 's^-1'),
        n = 0.19,
        Ea = (127.277, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 466,
    label = "C11H17-35 <=> C11H17-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.45e+11, 's^-1'),
        n = 0.19,
        Ea = (130.332, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 467,
    label = "C10H13-41 <=> C10H13-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.31e+11, 's^-1'),
        n = 0.19,
        Ea = (114.349, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 468,
    label = "C11H15-37 <=> C11H15-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.88e+11, 's^-1'),
        n = 0.19,
        Ea = (118.282, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 469,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.63e+12, 's^-1'),
        n = 0.19,
        Ea = (89.7886, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 470,
    label = "C9H15-49 <=> C9H15-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.24e+10, 's^-1'),
        n = 0.19,
        Ea = (106.441, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 471,
    label = "C10H17-37 <=> C10H17-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.62e+11, 's^-1'),
        n = 0.19,
        Ea = (106.357, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 472,
    label = "C11H19-17 <=> C11H19-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.07e+10, 's^-1'),
        n = 0.19,
        Ea = (107.864, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 473,
    label = "C11H17-37 <=> C11H17-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.89e+11, 's^-1'),
        n = 0.19,
        Ea = (134.641, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 474,
    label = "C12H19-13 <=> C12H19-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.36e+10, 's^-1'),
        n = 0.19,
        Ea = (137.695, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 475,
    label = "C11H15-39 <=> C11H15-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.43e+10, 's^-1'),
        n = 0.19,
        Ea = (121.713, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 476,
    label = "C12H17-19 <=> C12H17-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.49e+10, 's^-1'),
        n = 0.19,
        Ea = (125.646, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 477,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.56e+11, 's^-1'),
        n = 0.19,
        Ea = (97.1525, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 478,
    label = "C9H13-59 <=> C9H13-60",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.05e+10, 's^-1'),
        n = 0.19,
        Ea = (102.215, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 479,
    label = "C10H15-59 <=> C10H15-60",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.38e+11, 's^-1'),
        n = 0.19,
        Ea = (102.173, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 480,
    label = "C11H17-39 <=> C11H17-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+11, 's^-1'),
        n = 0.19,
        Ea = (103.638, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 481,
    label = "C11H15-41 <=> C11H15-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.12e+11, 's^-1'),
        n = 0.19,
        Ea = (130.457, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 482,
    label = "C12H17-21 <=> C12H17-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.45e+11, 's^-1'),
        n = 0.19,
        Ea = (133.47, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 483,
    label = "C11H13-23 <=> C11H13-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.55e+11, 's^-1'),
        n = 0.19,
        Ea = (117.487, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 484,
    label = "C12H15-13 <=> C12H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.29e+11, 's^-1'),
        n = 0.19,
        Ea = (121.462, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 485,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.64e+11, 's^-1'),
        n = 0.19,
        Ea = (92.9266, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 486,
    label = "C10H15-61 <=> C10H15-62",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.17e+10, 's^-1'),
        n = 0.19,
        Ea = (112.842, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 487,
    label = "C11H17-41 <=> C11H17-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.57e+11, 's^-1'),
        n = 0.19,
        Ea = (112.759, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 488,
    label = "C12H19-15 <=> C12H19-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.95e+10, 's^-1'),
        n = 0.19,
        Ea = (114.265, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 489,
    label = "C12H17-23 <=> C12H17-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.84e+11, 's^-1'),
        n = 0.19,
        Ea = (141.043, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 490,
    label = "C13H19-5 <=> C13H19-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.21e+10, 's^-1'),
        n = 0.19,
        Ea = (144.097, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 491,
    label = "C12H15-15 <=> C12H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.16e+10, 's^-1'),
        n = 0.19,
        Ea = (128.114, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 492,
    label = "C13H17-3 <=> C13H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.24e+10, 's^-1'),
        n = 0.19,
        Ea = (132.047, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 493,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.46e+11, 's^-1'),
        n = 0.19,
        Ea = (103.554, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 494,
    label = "C9H11-27 <=> C9H11-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.58e+11, 's^-1'),
        n = 0.19,
        Ea = (100.542, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 495,
    label = "C10H13-43 <=> C10H13-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.14e+12, 's^-1'),
        n = 0.19,
        Ea = (100.458, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 496,
    label = "C11H15-43 <=> C11H15-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.87e+11, 's^-1'),
        n = 0.19,
        Ea = (101.964, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 497,
    label = "C11H13-25 <=> C11H13-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.34e+12, 's^-1'),
        n = 0.19,
        Ea = (128.742, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 498,
    label = "C12H15-17 <=> C12H15-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.78e+11, 's^-1'),
        n = 0.19,
        Ea = (131.796, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 499,
    label = "C11H11-5 <=> C11H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.66e+11, 's^-1'),
        n = 0.19,
        Ea = (115.813, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 500,
    label = "C12H13-3 <=> C12H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.99e+11, 's^-1'),
        n = 0.19,
        Ea = (119.746, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 501,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.52e+12, 's^-1'),
        n = 0.19,
        Ea = (91.253, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 502,
    label = "C10H13-45 <=> C10H13-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38e+10, 's^-1'),
        n = 0.19,
        Ea = (109.663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 503,
    label = "C11H15-45 <=> C11H15-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0.19,
        Ea = (109.621, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 504,
    label = "C12H17-25 <=> C12H17-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.51e+10, 's^-1'),
        n = 0.19,
        Ea = (111.085, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 505,
    label = "C12H15-19 <=> C12H15-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.17e+11, 's^-1'),
        n = 0.19,
        Ea = (137.905, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 506,
    label = "C13H17-5 <=> C13H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.31e+10, 's^-1'),
        n = 0.19,
        Ea = (140.917, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 507,
    label = "C12H13-5 <=> C12H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.82e+10, 's^-1'),
        n = 0.19,
        Ea = (124.934, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 508,
    label = "C13H15 <=> C13H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.24e+10, 's^-1'),
        n = 0.19,
        Ea = (128.909, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 509,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.2e+11, 's^-1'),
        n = 0.19,
        Ea = (100.374, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 510,
    label = "C8H13-43 <=> C8H13-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4e+08, 's^-1'),
        n = 0.19,
        Ea = (26.3592, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_cs2H
""",
)

entry(
    index = 511,
    label = "C9H15-51 <=> C9H15-52",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.9e+09, 's^-1'),
        n = 0.19,
        Ea = (26.2755, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csHNd
""",
)

entry(
    index = 512,
    label = "C10H17-39 <=> C10H17-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.28e+08, 's^-1'),
        n = 0.19,
        Ea = (27.7399, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 513,
    label = "C10H15-63 <=> C10H15-64",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.39e+09, 's^-1'),
        n = 0.19,
        Ea = (54.5594, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csHCd
""",
)

entry(
    index = 514,
    label = "C11H17-43 <=> C11H17-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.59e+08, 's^-1'),
        n = 0.19,
        Ea = (57.6137, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 515,
    label = "C10H13-47 <=> C10H13-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.69e+09, 's^-1'),
        n = 0.19,
        Ea = (41.6308, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csHCt
""",
)

entry(
    index = 516,
    label = "C11H15-47 <=> C11H15-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.52e+09, 's^-1'),
        n = 0.19,
        Ea = (45.5638, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 517,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.38e+09, 's^-1'),
        n = 0.19,
        Ea = (17.0289, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 518,
    label = "C9H15-53 <=> C9H15-54",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.5e+09, 's^-1'),
        n = 0.19,
        Ea = (27.6981, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 519,
    label = "C10H17-41 <=> C10H17-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.81e+10, 's^-1'),
        n = 0.19,
        Ea = (27.6562, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 520,
    label = "C11H19-19 <=> C11H19-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.55e+09, 's^-1'),
        n = 0.19,
        Ea = (29.1206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 521,
    label = "C11H17-45 <=> C11H17-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.12e+10, 's^-1'),
        n = 0.19,
        Ea = (55.9401, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 522,
    label = "C12H19-17 <=> C12H19-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6e+09, 's^-1'),
        n = 0.19,
        Ea = (58.9526, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 523,
    label = "C11H15-49 <=> C11H15-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.05e+10, 's^-1'),
        n = 0.19,
        Ea = (42.9697, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 524,
    label = "C12H17-27 <=> C12H17-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.49e+09, 's^-1'),
        n = 0.19,
        Ea = (46.9445, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 525,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.99e+10, 's^-1'),
        n = 0.19,
        Ea = (18.4096, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 526,
    label = "C10H17-43 <=> C10H17-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.47e+08, 's^-1'),
        n = 0.19,
        Ea = (35.1038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 527,
    label = "C11H19-21 <=> C11H19-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.96e+09, 's^-1'),
        n = 0.19,
        Ea = (35.0201, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 528,
    label = "C12H21-5 <=> C12H21-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.95e+08, 's^-1'),
        n = 0.19,
        Ea = (36.5263, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 529,
    label = "C12H19-19 <=> C12H19-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.63e+09, 's^-1'),
        n = 0.19,
        Ea = (63.3039, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 530,
    label = "C13H21-3 <=> C13H21-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.31e+09, 's^-1'),
        n = 0.19,
        Ea = (66.3582, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 531,
    label = "C12H17-29 <=> C12H17-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.31e+09, 's^-1'),
        n = 0.19,
        Ea = (50.3754, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 532,
    label = "C13H19-7 <=> C13H19-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.07e+09, 's^-1'),
        n = 0.19,
        Ea = (54.3083, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 533,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.71e+09, 's^-1'),
        n = 0.19,
        Ea = (25.7734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 534,
    label = "C10H15-65 <=> C10H15-66",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.48e+09, 's^-1'),
        n = 0.19,
        Ea = (30.8779, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 535,
    label = "C11H17-47 <=> C11H17-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.07e+10, 's^-1'),
        n = 0.19,
        Ea = (30.7942, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 536,
    label = "C12H19-21 <=> C12H19-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.69e+09, 's^-1'),
        n = 0.19,
        Ea = (32.3005, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 537,
    label = "C12H17-31 <=> C12H17-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+10, 's^-1'),
        n = 0.19,
        Ea = (59.0781, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 538,
    label = "C13H19-9 <=> C13H19-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.54e+09, 's^-1'),
        n = 0.19,
        Ea = (62.1324, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 539,
    label = "C12H15-21 <=> C12H15-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.23e+09, 's^-1'),
        n = 0.19,
        Ea = (46.1495, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 540,
    label = "C13H17-7 <=> C13H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.61e+09, 's^-1'),
        n = 0.19,
        Ea = (50.0825, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 541,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.36e+10, 's^-1'),
        n = 0.19,
        Ea = (21.5894, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 542,
    label = "C11H17-49 <=> C11H17-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.31e+08, 's^-1'),
        n = 0.19,
        Ea = (41.4634, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 543,
    label = "C12H19-23 <=> C12H19-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.85e+09, 's^-1'),
        n = 0.19,
        Ea = (41.4216, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 544,
    label = "C13H21-5 <=> C13H21-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.66e+08, 's^-1'),
        n = 0.19,
        Ea = (42.886, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 545,
    label = "C13H19-11 <=> C13H19-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.5e+09, 's^-1'),
        n = 0.19,
        Ea = (69.7054, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 546,
    label = "C14H21 <=> C14H21-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.27e+09, 's^-1'),
        n = 0.19,
        Ea = (72.7179, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 547,
    label = "C13H17-9 <=> C13H17-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.24e+09, 's^-1'),
        n = 0.19,
        Ea = (56.735, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 548,
    label = "C14H19 <=> C14H19-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+09, 's^-1'),
        n = 0.19,
        Ea = (60.7098, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 549,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.46e+09, 's^-1'),
        n = 0.19,
        Ea = (32.175, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 550,
    label = "C10H13-49 <=> C10H13-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.86e+09, 's^-1'),
        n = 0.19,
        Ea = (29.2043, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 551,
    label = "C11H15-51 <=> C11H15-52",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.8e+10, 's^-1'),
        n = 0.19,
        Ea = (29.1206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 552,
    label = "C12H17-33 <=> C12H17-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.02e+09, 's^-1'),
        n = 0.19,
        Ea = (30.585, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 553,
    label = "C12H15-23 <=> C12H15-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.27e+10, 's^-1'),
        n = 0.19,
        Ea = (57.4045, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 554,
    label = "C13H17-11 <=> C13H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.25e+09, 's^-1'),
        n = 0.19,
        Ea = (60.417, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 555,
    label = "C12H13-7 <=> C12H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.63e+10, 's^-1'),
        n = 0.19,
        Ea = (44.4341, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 556,
    label = "C13H15-3 <=> C13H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.46e+10, 's^-1'),
        n = 0.19,
        Ea = (48.4089, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 557,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.15e+10, 's^-1'),
        n = 0.19,
        Ea = (19.874, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 558,
    label = "C11H15-53 <=> C11H15-54",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.37e+08, 's^-1'),
        n = 0.19,
        Ea = (38.3254, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 559,
    label = "C12H17-35 <=> C12H17-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.44e+09, 's^-1'),
        n = 0.19,
        Ea = (38.2418, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 560,
    label = "C13H19-13 <=> C13H19-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.14e+08, 's^-1'),
        n = 0.19,
        Ea = (39.748, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 561,
    label = "C13H17-13 <=> C13H17-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.86e+09, 's^-1'),
        n = 0.19,
        Ea = (66.5256, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 562,
    label = "C14H19-3 <=> C14H19-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.09e+08, 's^-1'),
        n = 0.19,
        Ea = (69.5799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 563,
    label = "C13H15-5 <=> C13H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.42e+09, 's^-1'),
        n = 0.19,
        Ea = (53.597, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 564,
    label = "C14H17 <=> C14H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28e+09, 's^-1'),
        n = 0.19,
        Ea = (57.53, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 565,
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.38e+09, 's^-1'),
        n = 0.19,
        Ea = (29.037, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 566,
    label = "C6H9-15 <=> C6H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.39e+10, 's^-1'),
        n = 0.19,
        Ea = (121.88, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_2H;radadd_intra_cs2H
""",
)

entry(
    index = 567,
    label = "C7H11-29 <=> C7H11-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.73e+11, 's^-1'),
        n = 0.19,
        Ea = (121.838, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csHNd
""",
)

entry(
    index = 568,
    label = "C8H13-45 <=> C8H13-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.35e+10, 's^-1'),
        n = 0.19,
        Ea = (123.302, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 569,
    label = "C8H11-39 <=> C8H11-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.02e+11, 's^-1'),
        n = 0.19,
        Ea = (150.08, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csHCd
""",
)

entry(
    index = 570,
    label = "C9H13-61 <=> C9H13-62",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.72e+10, 's^-1'),
        n = 0.19,
        Ea = (153.134, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 571,
    label = "C8H9-9 <=> C8H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.01e+11, 's^-1'),
        n = 0.19,
        Ea = (137.152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csHCt
""",
)

entry(
    index = 572,
    label = "C9H11-29 <=> C9H11-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.06e+10, 's^-1'),
        n = 0.19,
        Ea = (141.126, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 573,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.81e+11, 's^-1'),
        n = 0.19,
        Ea = (112.591, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 574,
    label = "C7H11-31 <=> C7H11-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.49e+11, 's^-1'),
        n = 0.19,
        Ea = (123.261, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 575,
    label = "C8H13-47 <=> C8H13-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.08e+12, 's^-1'),
        n = 0.19,
        Ea = (123.177, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 576,
    label = "C9H15-55 <=> C9H15-56",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.72e+11, 's^-1'),
        n = 0.19,
        Ea = (124.683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 577,
    label = "C9H13-63 <=> C9H13-64",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.26e+12, 's^-1'),
        n = 0.19,
        Ea = (151.461, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 578,
    label = "C10H15-67 <=> C10H15-68",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.58e+11, 's^-1'),
        n = 0.19,
        Ea = (154.515, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 579,
    label = "C9H11-31 <=> C9H11-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.3e+11, 's^-1'),
        n = 0.19,
        Ea = (138.532, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 580,
    label = "C10H13-51 <=> C10H13-52",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.67e+11, 's^-1'),
        n = 0.19,
        Ea = (142.465, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 581,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.38e+12, 's^-1'),
        n = 0.19,
        Ea = (113.972, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 582,
    label = "C8H13-49 <=> C8H13-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.27e+10, 's^-1'),
        n = 0.19,
        Ea = (130.666, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 583,
    label = "C9H15-57 <=> C9H15-58",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.36e+11, 's^-1'),
        n = 0.19,
        Ea = (130.583, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 584,
    label = "C10H17-45 <=> C10H17-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.94e+10, 's^-1'),
        n = 0.19,
        Ea = (132.047, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 585,
    label = "C10H15-69 <=> C10H15-70",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.76e+11, 's^-1'),
        n = 0.19,
        Ea = (158.866, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 586,
    label = "C11H17-51 <=> C11H17-52",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.82e+10, 's^-1'),
        n = 0.19,
        Ea = (161.879, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 587,
    label = "C10H13-53 <=> C10H13-54",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38e+11, 's^-1'),
        n = 0.19,
        Ea = (145.896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 588,
    label = "C11H15-55 <=> C11H15-56",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.24e+11, 's^-1'),
        n = 0.19,
        Ea = (149.871, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 589,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.2e+11, 's^-1'),
        n = 0.19,
        Ea = (121.336, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 590,
    label = "C8H11-41 <=> C8H11-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.83e+10, 's^-1'),
        n = 0.19,
        Ea = (126.44, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 591,
    label = "C9H13-65 <=> C9H13-66",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.4e+11, 's^-1'),
        n = 0.19,
        Ea = (126.357, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 592,
    label = "C10H15-71 <=> C10H15-72",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.61e+11, 's^-1'),
        n = 0.19,
        Ea = (127.821, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 593,
    label = "C10H13-55 <=> C10H13-56",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.47e+11, 's^-1'),
        n = 0.19,
        Ea = (154.641, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 594,
    label = "C11H15-57 <=> C11H15-58",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.12e+11, 's^-1'),
        n = 0.19,
        Ea = (157.695, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 595,
    label = "C10H11-19 <=> C10H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.72e+11, 's^-1'),
        n = 0.19,
        Ea = (141.712, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 596,
    label = "C11H13-27 <=> C11H13-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.35e+11, 's^-1'),
        n = 0.19,
        Ea = (145.645, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 597,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.41e+12, 's^-1'),
        n = 0.19,
        Ea = (117.11, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 598,
    label = "C9H13-67 <=> C9H13-68",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.17e+10, 's^-1'),
        n = 0.19,
        Ea = (137.026, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 599,
    label = "C10H15-73 <=> C10H15-74",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.3e+11, 's^-1'),
        n = 0.19,
        Ea = (136.942, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 600,
    label = "C11H17-53 <=> C11H17-54",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.77e+10, 's^-1'),
        n = 0.19,
        Ea = (138.449, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 601,
    label = "C11H15-59 <=> C11H15-60",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.68e+11, 's^-1'),
        n = 0.19,
        Ea = (165.226, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 602,
    label = "C12H17-37 <=> C12H17-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.6e+10, 's^-1'),
        n = 0.19,
        Ea = (168.28, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 603,
    label = "C11H13-29 <=> C11H13-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.34e+11, 's^-1'),
        n = 0.19,
        Ea = (152.298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 604,
    label = "C12H15-25 <=> C12H15-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+11, 's^-1'),
        n = 0.19,
        Ea = (156.231, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 605,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.05e+11, 's^-1'),
        n = 0.19,
        Ea = (127.738, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 606,
    label = "C8H9-11 <=> C8H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.31e+11, 's^-1'),
        n = 0.19,
        Ea = (124.725, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 607,
    label = "C9H11-33 <=> C9H11-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.67e+12, 's^-1'),
        n = 0.19,
        Ea = (124.641, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 608,
    label = "C10H13-57 <=> C10H13-58",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.19e+11, 's^-1'),
        n = 0.19,
        Ea = (126.148, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 609,
    label = "C10H11-21 <=> C10H11-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.95e+12, 's^-1'),
        n = 0.19,
        Ea = (152.925, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 610,
    label = "C11H13-31 <=> C11H13-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.52e+11, 's^-1'),
        n = 0.19,
        Ea = (155.98, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 611,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.71e+11, 's^-1'),
        n = 0.19,
        Ea = (139.997, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 612,
    label = "C11H11-7 <=> C11H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.74e+11, 's^-1'),
        n = 0.19,
        Ea = (143.971, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 613,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.67e+12, 's^-1'),
        n = 0.19,
        Ea = (115.437, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 614,
    label = "C9H11-35 <=> C9H11-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+10, 's^-1'),
        n = 0.19,
        Ea = (133.888, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 615,
    label = "C10H13-59 <=> C10H13-60",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.46e+11, 's^-1'),
        n = 0.19,
        Ea = (133.804, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 616,
    label = "C11H15-61 <=> C11H15-62",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.66e+10, 's^-1'),
        n = 0.19,
        Ea = (135.311, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 617,
    label = "C11H13-33 <=> C11H13-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.71e+11, 's^-1'),
        n = 0.19,
        Ea = (162.088, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 618,
    label = "C12H15-27 <=> C12H15-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.83e+10, 's^-1'),
        n = 0.19,
        Ea = (165.142, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 619,
    label = "C11H11-9 <=> C11H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.49e+10, 's^-1'),
        n = 0.19,
        Ea = (149.16, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 620,
    label = "C12H13-9 <=> C12H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.64e+10, 's^-1'),
        n = 0.19,
        Ea = (153.093, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 621,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.21e+11, 's^-1'),
        n = 0.19,
        Ea = (124.558, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 622,
    label = "C7H11-33 <=> C7H11-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.35e+09, 's^-1'),
        n = 0.19,
        Ea = (54.6012, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_cs2H
""",
)

entry(
    index = 623,
    label = "C8H13-51 <=> C8H13-52",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.6e+10, 's^-1'),
        n = 0.19,
        Ea = (54.5175, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csHNd
""",
)

entry(
    index = 624,
    label = "C9H15-59 <=> C9H15-60",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.15e+10, 's^-1'),
        n = 0.19,
        Ea = (56.0238, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 625,
    label = "C9H13-69 <=> C9H13-70",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.37e+10, 's^-1'),
        n = 0.19,
        Ea = (82.8014, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csHCd
""",
)

entry(
    index = 626,
    label = "C10H15-75 <=> C10H15-76",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.52e+10, 's^-1'),
        n = 0.19,
        Ea = (85.8557, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 627,
    label = "C9H11-37 <=> C9H11-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.67e+10, 's^-1'),
        n = 0.19,
        Ea = (69.8728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csHCt
""",
)

entry(
    index = 628,
    label = "C10H13-61 <=> C10H13-62",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.41e+10, 's^-1'),
        n = 0.19,
        Ea = (73.8058, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 629,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.01e+11, 's^-1'),
        n = 0.19,
        Ea = (45.3127, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 630,
    label = "C8H13-53 <=> C8H13-54",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.97e+10, 's^-1'),
        n = 0.19,
        Ea = (55.9819, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 631,
    label = "C9H15-61 <=> C9H15-62",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.88e+11, 's^-1'),
        n = 0.19,
        Ea = (55.8982, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 632,
    label = "C10H17-47 <=> C10H17-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.22e+10, 's^-1'),
        n = 0.19,
        Ea = (57.4045, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 633,
    label = "C10H15-77 <=> C10H15-78",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.36e+11, 's^-1'),
        n = 0.19,
        Ea = (84.1821, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 634,
    label = "C11H17-55 <=> C11H17-56",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.51e+10, 's^-1'),
        n = 0.19,
        Ea = (87.2364, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 635,
    label = "C10H13-63 <=> C10H13-64",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.67e+11, 's^-1'),
        n = 0.19,
        Ea = (71.2535, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 636,
    label = "C11H15-63 <=> C11H15-64",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.51e+11, 's^-1'),
        n = 0.19,
        Ea = (75.1865, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 637,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.32e+11, 's^-1'),
        n = 0.19,
        Ea = (46.6516, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 638,
    label = "C9H15-63 <=> C9H15-64",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.67e+09, 's^-1'),
        n = 0.19,
        Ea = (63.3458, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 639,
    label = "C10H17-49 <=> C10H17-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.28e+10, 's^-1'),
        n = 0.19,
        Ea = (63.2621, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 640,
    label = "C11H19-23 <=> C11H19-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.58e+10, 's^-1'),
        n = 0.19,
        Ea = (64.7683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 641,
    label = "C11H17-57 <=> C11H17-58",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.34e+10, 's^-1'),
        n = 0.19,
        Ea = (91.5459, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 642,
    label = "C12H19-25 <=> C12H19-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.08e+10, 's^-1'),
        n = 0.19,
        Ea = (94.6002, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 643,
    label = "C11H15-65 <=> C11H15-66",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.66e+10, 's^-1'),
        n = 0.19,
        Ea = (78.6174, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 644,
    label = "C12H17-39 <=> C12H17-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.29e+10, 's^-1'),
        n = 0.19,
        Ea = (82.5503, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 645,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38e+11, 's^-1'),
        n = 0.19,
        Ea = (54.0573, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 646,
    label = "C9H13-71 <=> C9H13-72",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.35e+10, 's^-1'),
        n = 0.19,
        Ea = (59.1199, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 647,
    label = "C10H15-79 <=> C10H15-80",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+11, 's^-1'),
        n = 0.19,
        Ea = (59.0781, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 648,
    label = "C11H17-59 <=> C11H17-60",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.27e+10, 's^-1'),
        n = 0.19,
        Ea = (60.5425, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 649,
    label = "C11H15-67 <=> C11H15-68",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.99e+11, 's^-1'),
        n = 0.19,
        Ea = (87.3619, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 650,
    label = "C12H17-41 <=> C12H17-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.62e+10, 's^-1'),
        n = 0.19,
        Ea = (90.3744, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 651,
    label = "C11H13-35 <=> C11H13-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.89e+10, 's^-1'),
        n = 0.19,
        Ea = (74.3915, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 652,
    label = "C12H15-29 <=> C12H15-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.9e+10, 's^-1'),
        n = 0.19,
        Ea = (78.3663, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 653,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.74e+11, 's^-1'),
        n = 0.19,
        Ea = (49.8314, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 654,
    label = "C10H15-81 <=> C10H15-82",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.42e+09, 's^-1'),
        n = 0.19,
        Ea = (69.7473, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 655,
    label = "C11H17-61 <=> C11H17-62",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.1e+10, 's^-1'),
        n = 0.19,
        Ea = (69.6636, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 656,
    label = "C12H19-27 <=> C12H19-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.53e+10, 's^-1'),
        n = 0.19,
        Ea = (71.1698, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 657,
    label = "C12H17-43 <=> C12H17-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.13e+10, 's^-1'),
        n = 0.19,
        Ea = (97.9474, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 658,
    label = "C13H19-15 <=> C13H19-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.02e+10, 's^-1'),
        n = 0.19,
        Ea = (101.002, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 659,
    label = "C12H15-31 <=> C12H15-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.55e+10, 's^-1'),
        n = 0.19,
        Ea = (85.0189, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 660,
    label = "C13H17-15 <=> C13H17-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.19e+10, 's^-1'),
        n = 0.19,
        Ea = (88.9518, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 661,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.34e+11, 's^-1'),
        n = 0.19,
        Ea = (60.417, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 662,
    label = "C9H11-39 <=> C9H11-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.12e+10, 's^-1'),
        n = 0.19,
        Ea = (57.4463, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 663,
    label = "C10H13-65 <=> C10H13-66",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.44e+11, 's^-1'),
        n = 0.19,
        Ea = (57.3626, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 664,
    label = "C11H15-69 <=> C11H15-70",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.11e+11, 's^-1'),
        n = 0.19,
        Ea = (58.8689, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 665,
    label = "C11H13-37 <=> C11H13-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.18e+11, 's^-1'),
        n = 0.19,
        Ea = (85.6465, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 666,
    label = "C12H15-33 <=> C12H15-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.47e+11, 's^-1'),
        n = 0.19,
        Ea = (88.7008, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 667,
    label = "C11H11-11 <=> C11H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.58e+11, 's^-1'),
        n = 0.19,
        Ea = (72.7179, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 668,
    label = "C12H13-11 <=> C12H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.32e+11, 's^-1'),
        n = 0.19,
        Ea = (76.6509, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 669,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.76e+11, 's^-1'),
        n = 0.19,
        Ea = (48.1578, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 670,
    label = "C10H13-67 <=> C10H13-68",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.35e+09, 's^-1'),
        n = 0.19,
        Ea = (66.5674, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 671,
    label = "C11H15-71 <=> C11H15-72",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.88e+10, 's^-1'),
        n = 0.19,
        Ea = (66.5256, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 672,
    label = "C12H17-45 <=> C12H17-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.74e+09, 's^-1'),
        n = 0.19,
        Ea = (67.99, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 673,
    label = "C12H15-35 <=> C12H15-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.53e+10, 's^-1'),
        n = 0.19,
        Ea = (94.8094, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 674,
    label = "C13H17-17 <=> C13H17-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28e+10, 's^-1'),
        n = 0.19,
        Ea = (97.8219, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 675,
    label = "C12H13-13 <=> C12H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.26e+10, 's^-1'),
        n = 0.19,
        Ea = (81.839, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 676,
    label = "C13H15-7 <=> C13H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.03e+10, 's^-1'),
        n = 0.19,
        Ea = (85.8138, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 677,
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.53e+10, 's^-1'),
        n = 0.19,
        Ea = (57.279, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 678,
    label = "C8H11-43 <=> C8H11-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.71e+10, 's^-1'),
        n = 0.19,
        Ea = (86.1067, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_cs2H
""",
)

entry(
    index = 679,
    label = "C9H13-73 <=> C9H13-74",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.24e+11, 's^-1'),
        n = 0.19,
        Ea = (86.023, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csHNd
""",
)

entry(
    index = 680,
    label = "C10H15-83 <=> C10H15-84",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.11e+10, 's^-1'),
        n = 0.19,
        Ea = (87.5293, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd
""",
)

entry(
    index = 681,
    label = "C10H13-69 <=> C10H13-70",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.45e+11, 's^-1'),
        n = 0.19,
        Ea = (114.307, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csHCd
""",
)

entry(
    index = 682,
    label = "C11H15-73 <=> C11H15-74",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.1e+10, 's^-1'),
        n = 0.19,
        Ea = (117.361, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd
""",
)

entry(
    index = 683,
    label = "C10H11-23 <=> C10H11-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.21e+10, 's^-1'),
        n = 0.19,
        Ea = (101.378, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csHCt
""",
)

entry(
    index = 684,
    label = "C11H13-39 <=> C11H13-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.49e+10, 's^-1'),
        n = 0.19,
        Ea = (105.311, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt
""",
)

entry(
    index = 685,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.72e+11, 's^-1'),
        n = 0.19,
        Ea = (76.8182, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH
""",
)

entry(
    index = 686,
    label = "C9H13-75 <=> C9H13-76",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.07e+11, 's^-1'),
        n = 0.19,
        Ea = (87.4874, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H
""",
)

entry(
    index = 687,
    label = "C10H15-85 <=> C10H15-86",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.75e+11, 's^-1'),
        n = 0.19,
        Ea = (87.4038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd
""",
)

entry(
    index = 688,
    label = "C11H17-63 <=> C11H17-64",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.95e+11, 's^-1'),
        n = 0.19,
        Ea = (88.8682, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd
""",
)

entry(
    index = 689,
    label = "C11H15-75 <=> C11H15-76",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.05e+11, 's^-1'),
        n = 0.19,
        Ea = (115.688, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd
""",
)

entry(
    index = 690,
    label = "C12H17-47 <=> C12H17-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.56e+11, 's^-1'),
        n = 0.19,
        Ea = (118.742, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd
""",
)

entry(
    index = 691,
    label = "C11H13-41 <=> C11H13-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.51e+11, 's^-1'),
        n = 0.19,
        Ea = (102.759, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt
""",
)

entry(
    index = 692,
    label = "C12H15-37 <=> C12H15-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.06e+11, 's^-1'),
        n = 0.19,
        Ea = (106.692, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt
""",
)

entry(
    index = 693,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+12, 's^-1'),
        n = 0.19,
        Ea = (78.1571, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 694,
    label = "C10H15-87 <=> C10H15-88",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.34e+10, 's^-1'),
        n = 0.19,
        Ea = (94.8513, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H
""",
)

entry(
    index = 695,
    label = "C11H17-65 <=> C11H17-66",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.69e+11, 's^-1'),
        n = 0.19,
        Ea = (94.7676, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd
""",
)

entry(
    index = 696,
    label = "C12H19-29 <=> C12H19-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.25e+10, 's^-1'),
        n = 0.19,
        Ea = (96.2738, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd
""",
)

entry(
    index = 697,
    label = "C12H17-49 <=> C12H17-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.98e+11, 's^-1'),
        n = 0.19,
        Ea = (123.051, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd
""",
)

entry(
    index = 698,
    label = "C13H19-17 <=> C13H19-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.6e+10, 's^-1'),
        n = 0.19,
        Ea = (126.106, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd
""",
)

entry(
    index = 699,
    label = "C12H15-39 <=> C12H15-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.85e+10, 's^-1'),
        n = 0.19,
        Ea = (110.123, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt
""",
)

entry(
    index = 700,
    label = "C13H17-19 <=> C13H17-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.87e+10, 's^-1'),
        n = 0.19,
        Ea = (114.056, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt
""",
)

entry(
    index = 701,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.72e+11, 's^-1'),
        n = 0.19,
        Ea = (85.5628, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH
""",
)

entry(
    index = 702,
    label = "C10H13-71 <=> C10H13-72",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.32e+10, 's^-1'),
        n = 0.19,
        Ea = (90.6254, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H
""",
)

entry(
    index = 703,
    label = "C11H15-77 <=> C11H15-78",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.58e+11, 's^-1'),
        n = 0.19,
        Ea = (90.5418, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd
""",
)

entry(
    index = 704,
    label = "C12H17-51 <=> C12H17-52",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.15e+11, 's^-1'),
        n = 0.19,
        Ea = (92.048, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd
""",
)

entry(
    index = 705,
    label = "C12H15-41 <=> C12H15-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.35e+11, 's^-1'),
        n = 0.19,
        Ea = (118.826, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd
""",
)

entry(
    index = 706,
    label = "C13H17-21 <=> C13H17-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.51e+11, 's^-1'),
        n = 0.19,
        Ea = (121.88, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd
""",
)

entry(
    index = 707,
    label = "C12H13-15 <=> C12H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.66e+11, 's^-1'),
        n = 0.19,
        Ea = (105.897, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt
""",
)

entry(
    index = 708,
    label = "C13H15-9 <=> C13H15-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+11, 's^-1'),
        n = 0.19,
        Ea = (109.83, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt
""",
)

entry(
    index = 709,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.01e+12, 's^-1'),
        n = 0.19,
        Ea = (81.337, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 710,
    label = "C11H15-79 <=> C11H15-80",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.27e+10, 's^-1'),
        n = 0.19,
        Ea = (101.253, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H
""",
)

entry(
    index = 711,
    label = "C12H17-53 <=> C12H17-54",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.64e+11, 's^-1'),
        n = 0.19,
        Ea = (101.169, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd
""",
)

entry(
    index = 712,
    label = "C13H19-19 <=> C13H19-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.13e+10, 's^-1'),
        n = 0.19,
        Ea = (102.634, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd
""",
)

entry(
    index = 713,
    label = "C13H17-23 <=> C13H17-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.92e+11, 's^-1'),
        n = 0.19,
        Ea = (129.453, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd
""",
)

entry(
    index = 714,
    label = "C14H19-5 <=> C14H19-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.44e+10, 's^-1'),
        n = 0.19,
        Ea = (132.507, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd
""",
)

entry(
    index = 715,
    label = "C13H15-11 <=> C13H15-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.57e+10, 's^-1'),
        n = 0.19,
        Ea = (116.524, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt
""",
)

entry(
    index = 716,
    label = "C14H17-3 <=> C14H17-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.61e+10, 's^-1'),
        n = 0.19,
        Ea = (120.457, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt
""",
)

entry(
    index = 717,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.62e+11, 's^-1'),
        n = 0.19,
        Ea = (91.9225, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH
""",
)

entry(
    index = 718,
    label = "C10H11-25 <=> C10H11-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.65e+11, 's^-1'),
        n = 0.19,
        Ea = (88.9518, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H
""",
)

entry(
    index = 719,
    label = "C11H13-43 <=> C11H13-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+12, 's^-1'),
        n = 0.19,
        Ea = (88.8682, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd
""",
)

entry(
    index = 720,
    label = "C12H15-43 <=> C12H15-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3e+11, 's^-1'),
        n = 0.19,
        Ea = (90.3744, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd
""",
)

entry(
    index = 721,
    label = "C12H13-17 <=> C12H13-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.4e+12, 's^-1'),
        n = 0.19,
        Ea = (117.152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd
""",
)

entry(
    index = 722,
    label = "C13H15-13 <=> C13H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.95e+11, 's^-1'),
        n = 0.19,
        Ea = (120.206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd
""",
)

entry(
    index = 723,
    label = "C12H11 <=> C12H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.95e+11, 's^-1'),
        n = 0.19,
        Ea = (104.223, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt
""",
)

entry(
    index = 724,
    label = "C13H13 <=> C13H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.26e+11, 's^-1'),
        n = 0.19,
        Ea = (108.156, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt
""",
)

entry(
    index = 725,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.63e+12, 's^-1'),
        n = 0.19,
        Ea = (79.6215, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 726,
    label = "C11H13-45 <=> C11H13-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.44e+10, 's^-1'),
        n = 0.19,
        Ea = (98.073, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H
""",
)

entry(
    index = 727,
    label = "C12H15-45 <=> C12H15-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.04e+11, 's^-1'),
        n = 0.19,
        Ea = (97.9893, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd
""",
)

entry(
    index = 728,
    label = "C13H17-25 <=> C13H17-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.62e+10, 's^-1'),
        n = 0.19,
        Ea = (99.4955, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd
""",
)

entry(
    index = 729,
    label = "C13H15-15 <=> C13H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.22e+11, 's^-1'),
        n = 0.19,
        Ea = (126.273, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd
""",
)

entry(
    index = 730,
    label = "C14H17-5 <=> C14H17-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.46e+10, 's^-1'),
        n = 0.19,
        Ea = (129.327, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd
""",
)

entry(
    index = 731,
    label = "C13H13-3 <=> C13H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.08e+10, 's^-1'),
        n = 0.19,
        Ea = (113.345, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt
""",
)

entry(
    index = 732,
    label = "C14H15 <=> C14H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.47e+10, 's^-1'),
        n = 0.19,
        Ea = (117.278, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt
""",
)

entry(
    index = 733,
    label = "C6H9-13 <=> C6H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.3e+11, 's^-1'),
        n = 0.19,
        Ea = (88.7845, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH
""",
)

entry(
    index = 734,
    label = "C9H13-77 <=> C9H13-78",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.71e+10, 's^-1'),
        n = 0.19,
        Ea = (86.1067, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R9_SDSSSD;doublebond_intra_pri_2H;radadd_intra_cs2H
""",
)

