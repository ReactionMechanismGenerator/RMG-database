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

entry(
    index = 78,
    label = "C7H9-7 <=> C7H9-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.21e+11, 's^-1'), n=0.34, Ea=(21.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C3
Taken from entry: prod_13 <=> prod_14
""",
)

entry(
    index = 79,
    label = "C7H9-9 <=> C7H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.9e+10, 's^-1'), n=0.33, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C3
Taken from entry: prod_16 <=> prod_17
""",
)

entry(
    index = 80,
    label = "C10H7-3 <=> C10H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.926e+10, 's^-1'), n=0.198, Ea=(5.455, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene',
        journal = 'Proceedings of the Combustion Institute',
        volume = '36(1)',
        pages = '919-926',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP
Taken from entry: W1 <=> W2
""",
)

entry(
    index = 81,
    label = "C10H9-28 <=> C10H9-27",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.953e+11, 's^-1'), n=0.387, Ea=(32.996, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene',
        journal = 'Proceedings of the Combustion Institute',
        volume = '36(1)',
        pages = '919-926',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP
Taken from entry: W3 <=> W11
""",
)

entry(
    index = 82,
    label = "C10H9-29 <=> C10H9-30",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.076e+11, 's^-1'), n=0.228, Ea=(6.982, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = u'Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene',
        journal = 'Proceedings of the Combustion Institute',
        volume = '36(1)',
        pages = '919-926',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP
Taken from entry: W3 <=> W4
""",
)

entry(
    index = 83,
    label = "C6H7-7 <=> C6H7-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.18e+11, 's^-1'), n=0.17, Ea=(4.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: Fulvene_H
Taken from entry: C5H5CH2-1 <=> biring1
""",
)

entry(
    index = 84,
    label = "C6H7-9 <=> C6H7-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.51e+11, 's^-1'), n=0.41, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: Fulvene_H
Taken from entry: biring1 <=> cyC6H7
""",
)

entry(
    index = 85,
    label = "C10H9-31 <=> C10H9-32",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.89e+11, 's^-1'), n=0.12, Ea=(9.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: naphthalene_H
Taken from entry: adducta <=> prod1
""",
)

entry(
    index = 86,
    label = "C10H9-33 <=> C10H9-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.73e+11, 's^-1'), n=0.31, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: naphthalene_H
Taken from entry: prod1 <=> prod2
""",
)

entry(
    index = 87,
    label = "C10H9-35 <=> C10H9-36",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(4.14e+11, 's^-1'), n=0.34, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: naphthalene_H
Taken from entry: prod2 <=> prod3
""",
)

entry(
    index = 88,
    label = "C10H9-37 <=> C10H9-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.79e+11, 's^-1'), n=0.33, Ea=(10.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: naphthalene_H
Taken from entry: prod3 <=> prod4
""",
)

entry(
    index = 89,
    label = "C10H9-39 <=> C10H9-30",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.42e+11, 's^-1'), n=0.22, Ea=(4.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: naphthalene_H
Taken from entry: prod5 <=> prod4
""",
)

entry(
    index = 90,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.89e+11, 's^-1'), n=0.29, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: adductd <=> pdt7
""",
)

entry(
    index = 91,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.51e+11, 's^-1'), n=0.58, Ea=(29.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt7 <=> pdt8
""",
)

entry(
    index = 92,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.39e+10, 's^-1'), n=0.91, Ea=(36.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt8 <=> pdt9
""",
)

entry(
    index = 93,
    label = "C10H11-9 <=> C10H11-10",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.25e+09, 's^-1'), n=0.76, Ea=(6.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt9 <=> pdt10bis
""",
)

entry(
    index = 94,
    label = "C10H11-11 <=> C10H11-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.43e+11, 's^-1'), n=0.21, Ea=(8.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: adducte <=> pdt7
""",
)

entry(
    index = 95,
    label = "C10H11-13 <=> C10H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.76e+10, 's^-1'), n=0.78, Ea=(24.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt10bis <=> pdt12
""",
)

entry(
    index = 96,
    label = "C10H11-15 <=> C10H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.02e+11, 's^-1'), n=0.85, Ea=(46.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: adductd <=> pdt14
""",
)

entry(
    index = 97,
    label = "C10H11-17 <=> C10H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.29e+09, 's^-1'), n=1.04, Ea=(31.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt15 <=> pdt16
""",
)

entry(
    index = 98,
    label = "C10H11-19 <=> C10H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.47e+10, 's^-1'), n=0.79, Ea=(29, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt17 <=> pdt18
""",
)

entry(
    index = 99,
    label = "C10H11-21 <=> C10H11-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.69e+11, 's^-1'), n=0.22, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt18 <=> pdt19
""",
)

entry(
    index = 100,
    label = "C10H11-23 <=> C10H11-24",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.9e+10, 's^-1'), n=0.29, Ea=(21.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt20 <=> pdt21
""",
)

entry(
    index = 101,
    label = "C10H11-25 <=> C10H11-26",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt14 <=> pdt23
""",
)

entry(
    index = 102,
    label = "C10H11-27 <=> C10H11-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.27e+10, 's^-1'), n=1.01, Ea=(40.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt23 <=> pdt9
""",
)

entry(
    index = 103,
    label = "C10H11-29 <=> C10H11-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.48e+11, 's^-1'), n=0.26, Ea=(7.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt17 <=> pdt24
""",
)

entry(
    index = 104,
    label = "C10H11-31 <=> C10H11-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.43e+12, 's^-1'), n=0.31, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt24 <=> pdt28
""",
)

entry(
    index = 105,
    label = "C10H11-33 <=> C10H11-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0.41, Ea=(32.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt25 <=> pdt32
""",
)

entry(
    index = 106,
    label = "C10H11-35 <=> C10H11-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.16e+10, 's^-1'), n=0.2, Ea=(24.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt33 <=> pdt29
""",
)

entry(
    index = 107,
    label = "C10H11-37 <=> C10H11-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=1.08, Ea=(42.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt39 <=> pdt33
""",
)

entry(
    index = 108,
    label = "C10H11-39 <=> C10H11-40",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.51e+11, 's^-1'), n=0.28, Ea=(12.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt14 <=> pdt57
""",
)

entry(
    index = 109,
    label = "C10H11-41 <=> C10H11-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.75e+11, 's^-1'), n=0.44, Ea=(18.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt57 <=> pdt12
""",
)

entry(
    index = 110,
    label = "C7H9-11 <=> C7H9-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.69e+11, 's^-1'), n=0.24, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: addA <=> product1
""",
)

entry(
    index = 111,
    label = "C7H9-13 <=> C7H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.21e+11, 's^-1'), n=0.46, Ea=(16.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product1 <=> product2
""",
)

entry(
    index = 112,
    label = "C7H9-15 <=> C7H9-16",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.52e+11, 's^-1'), n=0.16, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: addB <=> product3
""",
)

entry(
    index = 113,
    label = "C7H9-17 <=> C7H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.56e+11, 's^-1'), n=0.55, Ea=(26.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product3 <=> product4
""",
)

entry(
    index = 114,
    label = "C7H9-19 <=> C7H9-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.77e+10, 's^-1'), n=0.87, Ea=(35, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: addC <=> product16
""",
)

entry(
    index = 115,
    label = "C7H9-21 <=> C7H9-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.17e+10, 's^-1'), n=0.34, Ea=(31.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: addC <=> product6
""",
)

entry(
    index = 116,
    label = "C7H9-23 <=> C7H9-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.37e+11, 's^-1'), n=0.73, Ea=(25.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product6 <=> product5
""",
)

entry(
    index = 117,
    label = "C7H9-25 <=> C7H9-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.01e+11, 's^-1'), n=0.59, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product8 <=> product9
""",
)

entry(
    index = 118,
    label = "C7H9-27 <=> C7H9-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.56e+10, 's^-1'), n=1.17, Ea=(48.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product10 <=> product11
""",
)

entry(
    index = 119,
    label = "C7H9-29 <=> C7H9-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e+11, 's^-1'), n=0.26, Ea=(22.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product11 <=> product12
""",
)

entry(
    index = 120,
    label = "C7H9-31 <=> C7H9-32",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.98e+11, 's^-1'), n=0.06, Ea=(19.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: addB <=> product17
""",
)

entry(
    index = 121,
    label = "C7H9-33 <=> C7H9-34",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.29e+12, 's^-1'), n=0.15, Ea=(2.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product18 <=> product19
""",
)

entry(
    index = 122,
    label = "C7H9-35 <=> C7H9-36",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.58e+12, 's^-1'), n=0.31, Ea=(16, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product19 <=> product20
""",
)

entry(
    index = 123,
    label = "C7H9-37 <=> C7H9-38",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41e+11, 's^-1'), n=0.2, Ea=(46.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product21 <=> product23
""",
)

entry(
    index = 124,
    label = "C7H9-39 <=> C7H9-40",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.18e+11, 's^-1'), n=0.82, Ea=(22.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product23 <=> product24
""",
)

entry(
    index = 125,
    label = "C7H9-41 <=> C7H9-42",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.95e+10, 's^-1'), n=1.05, Ea=(39.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product25 <=> product26
""",
)

entry(
    index = 126,
    label = "C7H9-43 <=> C7H9-44",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.81e+10, 's^-1'), n=0.91, Ea=(32, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product26 <=> product11
""",
)

entry(
    index = 127,
    label = "C7H9-45 <=> C7H9-46",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.11e+10, 's^-1'), n=0.18, Ea=(66.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product22 <=> product29
""",
)

entry(
    index = 128,
    label = "C7H7 <=> C7H7-2",
    degeneracy = 7.0,
    kinetics = Arrhenius(A=(1.56e+13, 's^-1'), n=0, Ea=(43.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product33 <=> product34
""",
)

entry(
    index = 129,
    label = "C7H9-47 <=> C7H9-48",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.51e+10, 's^-1'), n=0.25, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product35 <=> product36
""",
)

entry(
    index = 130,
    label = "C7H9-49 <=> C7H9-50",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+12, 's^-1'), n=0.39, Ea=(16, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product36 <=> product37
""",
)

entry(
    index = 131,
    label = "C7H7-3 <=> C7H7-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.25e+11, 's^-1'), n=0.16, Ea=(9.81, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = u'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 132,
    label = "C7H7-5 <=> C7H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.51e+12, 's^-1'), n=0.26, Ea=(25.25, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = u'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 133,
    label = "C7H7-7 <=> C7H7-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.85e+11, 's^-1'), n=0.49, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = u'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product46 <=> BENZYL
""",
)

entry(
    index = 134,
    label = "C4H5 <=> C4H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.605e+12, 's^-1'), n=0.275, Ea=(32.899, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = u'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 135,
    label = "C4H5-3 <=> C4H5-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.631e+12, 's^-1'), n=0.216, Ea=(46.951, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = u'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 136,
    label = "C4H5-5 <=> C4H5-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.403e+13, 's^-1'), n=0.233, Ea=(17.146, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = u'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 137,
    label = "C4H5-7 <=> C4H5-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.114e+13, 's^-1'), n=0.256, Ea=(8.237, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = u'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 138,
    label = "C7H7-9 <=> C7H7-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+12, 's^-1'), n=0.14, Ea=(0.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = u'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 139,
    label = "C7H7-11 <=> C7H7-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.24e+12, 's^-1'), n=0.31, Ea=(3.62, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = u'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 140,
    label = "C7H7-13 <=> C7H7-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.98e+12, 's^-1'), n=0.5, Ea=(61, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = u'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 141,
    label = "C7H7-15 <=> C7H7-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+13, 's^-1'), n=0.15, Ea=(19.35, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = u'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)
""",
)

