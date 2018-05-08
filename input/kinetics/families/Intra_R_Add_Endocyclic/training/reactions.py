#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""


entry(
    index = 1,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+10, 's^-1'), n=0.51, Ea=(30.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addD <=> product8
""",
)

entry(
    index = 2,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.03e+10, 's^-1'), n=1.1, Ea=(37, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product4 <=> product16
""",
)

entry(
    index = 3,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39e+11, 's^-1'), n=0.26, Ea=(26.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product22 <=> product25
""",
)



entry(
    index = 4,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+09, 's^-1'), n=0.63, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_1 <=> prod_2
""",
)

entry(
    index = 5,
    label = "C7H11 <=> C7H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+11, 's^-1'), n=0.2, Ea=(27.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_6 <=> prod_4
""",
)

entry(
    index = 6,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.53e+07, 's^-1'), n=1.05, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_7 <=> prod_8
""",
)

entry(
    index = 7,
    label = "C7H11-3 <=> C7H11-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+10, 's^-1'), n=0.2, Ea=(9.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_10 <=> prod_11
""",
)

entry(
    index = 8,
    label = "C6H9-5 <=> C6H9-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.47e+07, 's^-1'), n=0.85, Ea=(10.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_19 <=> prod_2
""",
)

entry(
    index = 9,
    label = "C7H11-5 <=> C7H11-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+11, 's^-1'), n=0.27, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_20 <=> prod_4
""",
)

entry(
    index = 10,
    label = "C5H7 <=> C5H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+09, 's^-1'), n=0.62, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_21 <=> prod_22
""",
)

entry(
    index = 11,
    label = "C5H5 <=> C5H5-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.88e+10, 's^-1'), n=0.31, Ea=(12.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_23 <=> prod_24
""",
)

entry(
    index = 12,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.05e+11, 's^-1'), n=0.12, Ea=(12.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_25 <=> prod_26
""",
)

entry(
    index = 13,
    label = "C6H7-3 <=> C6H7-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+11, 's^-1'), n=0.1, Ea=(11.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_27 <=> prod_28
""",
)

entry(
    index = 14,
    label = "C6H7-5 <=> C6H7-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.47e+11, 's^-1'), n=0.15, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_29 <=> prod_30
""",
)

entry(
    index = 15,
    label = "C_CCCJ <=> cyclobutyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.60e+07, 's^-1'),
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCJC <=> 3-methylcyclobutyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCJCC <=> 3-ethylcyclobutyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.00e+07, 's^-1'),
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
	rank = 3,
    referenceType = "theory",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 18,
    label = "CC_CCCJ <=> 2-methylcyclobutyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling" Trans conformation of pentenyl.
""",
)

entry(
    index = 19,
    label = "C_CC(C)CJ <=> 2-methylcyclobutyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_C(C)CCJ <=> 1-methylcyclobutyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.82e+08, 's^-1'),
        n = 0.91,
        Ea = (30.0, 'kcal/mol', '+|-', 1),
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CC(C)(C)CJ <=> 2,2-dimethylcyclobutyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCJ(C)C <=> 3,3-dimethylcyclobutyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_C(C)CCJC <=> 1,3-dimethylcyclobutyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "CC(C)_CCCJ <=> 2,2-dimethylcyclobutyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCCJ <=> cyclopentyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCCJC <=> 3-methylcyclopentyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCCJ(C)C <=> 3,3-dimethylcyclopentyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 28,
    label = "CC_CCCCJ <=> 2-methylcyclopentyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling" Trans conformation of hexenyl.
""",
)

entry(
    index = 29,
    label = "C_CCC(C)CJ <=> 3-methylcyclopentyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CC(C)CCJ <=> 2-methylcyclopentyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_C(C)CCCJ <=> 1-methylcyclopentyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.23e+07, 's^-1'),
        n = 1.00,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCC(C)(C)CJ <=> 3,3-dimethylcyclopentyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CC(C)(C)CCJ <=> 2,2-dimethylcyclopentyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.60e+08, 's^-1'),
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
	rank = 3,
    referenceType = "theory",
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
    label = "CC(C)_CCCCJ <=> 2,2-dimethylcyclopentyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.90e+06, 's^-1'),
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCCCJ <=> cyclohexyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCCCJC <=> 3-methylcyclohexyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.87e+05, 's^-1'),
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCCCJ(C)C <=> 3,3-dimethylcyclohexyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.30e+04, 's^-1'),
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
	rank = 3,
    referenceType = "theory",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 38,
    label = "CC_CCCCCJ <=> 2-methylcyclohexyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling" Trans conformation of heptenyl.
""",
)

entry(
    index = 39,
    label = "C_CCCC(C)CJ <=> 4-methylcyclohexyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCC(C)CCJ <=> 3-methylcyclohexyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CC(C)CCCJ <=> 2-methylcyclohexyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_C(C)CCCCJ <=> 1-methylcyclohexyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCC(C)(C)CJ <=> 4,4-dimethylcyclohexyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCC(C)(C)CCJ <=> 3,3-dimethylcyclohexyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.50e+07, 's^-1'),
        n = 0.70,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CC(C)(C)CCCJ <=> 2,2-dimethylcyclohexyl",
    degeneracy = 1,
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
	rank = 3,
    referenceType = "theory",
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
    label = "CC(C)_CCCCCJ <=> 2,2-dimethylcyclohexyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.44e+05, 's^-1'),
        n = 1.10,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCCCCJ <=> cycloheptyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.14e+05, 's^-1'),
        n = 1.20,
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCCCCJC <=> 3-methylcycloheptyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+04, 's^-1'),
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_CCCCCCJ(C)C <=> 3,3-dimethylcycloheptyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.54e+02, 's^-1'),
        n = 1.66,
        Ea = (4.9, 'kcal/mol', '+|-', 1),
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
	rank = 3,
    referenceType = "theory",
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
    label = "CC_CCCCCCJ <=> 2-methylcycloheptyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.10e+05, 's^-1'),
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
	rank = 3,
    referenceType = "theory",
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
    label = "C_C(C)CCCCCJ <=> 1-methylcycloheptyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.85e+05, 's^-1'),
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
	rank = 3,
    referenceType = "theory",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 52,
    label = "CC(C)_CCCCCCJ <=> 2,2-dimethylcycloheptyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.22e+04, 's^-1'),
        n = 1.36,
        Ea = (8.5, 'kcal/mol', '+|-', 1),
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
	rank = 3,
    referenceType = "theory",
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed TST with Eckart Tunnelling"
""",
)

entry(
    index = 53,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(324000, 's^-1'), n=1.64, Ea=(110.61, 'kJ/mol'), T0=(1, 'K')),
    rank = 4,
    reference = Article(
        authors = ['H. Ismail', 'J. Park', 'B. M. Wong', 'W. H. Green', 'M. C. Lin'],
        title = u'A theoretical and experimental kinetic study of phenyl radical addition to butadiene',
        journal = 'Proceedings of the Combustion Institute',
        volume = '30(1)',
        pages = '1049-1056',
        year = '2005',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at B3LYP/6-31G(d,p) level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP
Taken from entry: 4_phenyl_buten_3_yl <=> trihydronaphthalene
""",
)

entry(
    index = 54,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.57e+10, 's^-1'), n=0.43, Ea=(1.924, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W5 <=> W6
""",
)

entry(
    index = 55,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.588e+10, 's^-1'), n=0.535, Ea=(9.58, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W8 <=> W13
""",
)

entry(
    index = 56,
    label = "C10H9-5 <=> C10H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.53e+12, 's^-1'), n=0.189, Ea=(29.234, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W6 <=> W13
""",
)

entry(
    index = 57,
    label = "C10H9-7 <=> C10H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.017e+13, 's^-1'), n=0.272, Ea=(49.677, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W102 <=> W103
""",
)

entry(
    index = 58,
    label = "C10H9-9 <=> C10H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.69e+10, 's^-1'), n=0.239, Ea=(33.778, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W103 <=> W104
""",
)

entry(
    index = 59,
    label = "C10H9-11 <=> C10H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.279e+13, 's^-1'), n=0.395, Ea=(53.699, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W108 <=> W111
""",
)

entry(
    index = 60,
    label = "C10H9-13 <=> C10H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.161e+12, 's^-1'), n=0.277, Ea=(28.025, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W13 <=> W107
""",
)

entry(
    index = 61,
    label = "C10H9-15 <=> C10H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.473e+12, 's^-1'), n=0.247, Ea=(55.262, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W108 <=> W115
""",
)

entry(
    index = 62,
    label = "C10H9-17 <=> C10H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.748e+10, 's^-1'), n=0.262, Ea=(19.926, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W111 <=> W112
""",
)

entry(
    index = 63,
    label = "C10H9-19 <=> C10H9-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.998e+12, 's^-1'), n=0.237, Ea=(16.277, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W117 <=> W118
""",
)

entry(
    index = 64,
    label = "C10H7 <=> C10H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.992e+11, 's^-1'), n=0.67, Ea=(58.336, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""""",
    longDesc = 
u"""
Effective rate for an adduct of phenyl radical + diacetylene to form either benzofulvenyl or 2-naphthyl radical.
Rate-limiting step is trans-cis isomerization of the adduct, calculated by Zach Buras using CBS-QB3.
From kinetics library: First_to_Second_Aromatic_Ring/phenyl_diacetylene_effective
Taken from entry: i2_trans <=> i4
""",
)

entry(
    index = 65,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.63e+12, 's^-1'), n=-0.455, Ea=(30.695, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 66,
    label = "C9H9-3 <=> C9H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.999e+07, 's^-1'), n=0.942, Ea=(10.168, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 67,
    label = "C9H9-5 <=> C9H9-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.258e+10, 's^-1'), n=0.51, Ea=(12.883, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 68,
    label = "C9H9-7 <=> C9H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.315e+10, 's^-1'), n=0.447, Ea=(22.628, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 69,
    label = "C10H9-21 <=> C10H9-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.09e+08, 's^-1'), n=0.695, Ea=(6.499, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = u'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 70,
    label = "C10H9-23 <=> C10H9-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.983e+12, 's^-1'), n=-0.321, Ea=(5.655, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = u'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 71,
    label = "C10H9-25 <=> C10H9-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.323e+10, 's^-1'), n=0.901, Ea=(33.428, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = u'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 72,
    label = "C10H9-27 <=> C10H9-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.899e+10, 's^-1'), n=0.97, Ea=(33.321, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = u'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 73,
    label = "C10H9-29 <=> C10H9-30",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.258e+10, 's^-1'), n=0.21, Ea=(7.415, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = u'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 74,
    label = "C6H9-7 <=> C6H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.041e+08, 's^-1'), n=0.7, Ea=(20.246, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['Z. J. Buras', 'E. E. Dames', 'S. S. Merchant', 'G. Liu', 'R. M. I. Elsamra', 'W. H. Green'],
        title = u'Kinetics and Products of Vinyl + 1,3-Butadiene, a Potential Route to Benzene',
        journal = 'Journal of Physical Chemistry A',
        volume = '119(28)',
        pages = '7325-7338',
        year = '2015',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CCSD(T)-F12a/cc-pVTZ-F12//M08SO/MG3S level of theory
From kinetics library: 2015_Buras_C2H3_C4H6_highP
""",
)

entry(
    index = 75,
    label = "C9H11 <=> C9H11-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.162e+09, 's^-1'), n=0.771, Ea=(31.613, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['Z. J. Buras', 'T.-C. Chu', 'A. Jamal', 'N. W. Yee', 'J. E. Middaugh', 'W. H. Green'],
        title = u'Phenyl radical + propene: a prototypical reaction surface for aromatic-catalyzed 1,2-hydrogen-migration and subsequent resonance-stabilized radical formation',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '20',
        pages = '13191-13214 ',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP
""",
)

entry(
    index = 76,
    label = "C9H11-3 <=> C9H11-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.066e+08, 's^-1'), n=0.949, Ea=(16.873, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['Z. J. Buras', 'T.-C. Chu', 'A. Jamal', 'N. W. Yee', 'J. E. Middaugh', 'W. H. Green'],
        title = u'Phenyl radical + propene: a prototypical reaction surface for aromatic-catalyzed 1,2-hydrogen-migration and subsequent resonance-stabilized radical formation',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '20',
        pages = '13191-13214 ',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP
""",
)

entry(
    index = 77,
    label = "C9H11-5 <=> C9H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.255e+12, 's^-1'), n=0.347, Ea=(57.413, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['Z. J. Buras', 'T.-C. Chu', 'A. Jamal', 'N. W. Yee', 'J. E. Middaugh', 'W. H. Green'],
        title = u'Phenyl radical + propene: a prototypical reaction surface for aromatic-catalyzed 1,2-hydrogen-migration and subsequent resonance-stabilized radical formation',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '20',
        pages = '13191-13214 ',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP
""",
)

