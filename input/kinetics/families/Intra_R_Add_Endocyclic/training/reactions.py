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
    label = "C6H9-7 <=> C6H9-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.041e+08, 's^-1'), n=0.7, Ea=(20.246, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_Vinyl_1_3_Butadiene""",
    longDesc = 
u"""
Taken from entry: C6H9 <=> c6-C6H9
""",
)



entry(
    index = 54,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.09e+08, 's^-1'), n=0.695, Ea=(6.499, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W4 <=> W5
""",
)

entry(
    index = 55,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.983e+12, 's^-1'), n=-0.321, Ea=(5.655, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W7 <=> W6
""",
)

entry(
    index = 56,
    label = "C10H9-5 <=> C10H9-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.323e+10, 's^-1'), n=0.901, Ea=(33.428, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W17 <=> W7
""",
)

entry(
    index = 57,
    label = "C10H9-7 <=> C10H9-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.899e+10, 's^-1'), n=0.97, Ea=(33.321, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W11 <=> W10
""",
)



entry(
    index = 58,
    label = "C10H7 <=> C10H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.948e+11, 's^-1'), n=0.045, Ea=(5395, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: A12 <=> C10H7-1
""",
)



entry(
    index = 59,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.485e+11, 's^-1'), n=0.065, Ea=(27.941, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9(2) <=> C9H9(3)
""",
)

entry(
    index = 60,
    label = "C9H9-3 <=> C9H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.565e+11, 's^-1'), n=0.009, Ea=(28.521, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9(6) <=> C9H9(3)
""",
)

entry(
    index = 61,
    label = "C9H7 <=> C9H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.534e+11, 's^-1'), n=0.102, Ea=(13.049, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H7(18) <=> C9H7(19)
""",
)



entry(
    index = 62,
    label = "C9H7-3 <=> C9H7-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.431e+11, 's^-1'), n=0.114, Ea=(15.579, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H7(22) <=> C9H7(19)
""",
)

