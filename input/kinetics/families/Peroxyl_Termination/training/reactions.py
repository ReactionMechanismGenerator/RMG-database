#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Termination/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CH3O2 + CH3O2-2 <=> CH2O + O2 + CH4O",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2e+11, 'cm^3/(mol*s)'),
        n = -0.55,
        Ea = (-1600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc =
u"""
Taken from entry CH3OO + CH3OO <=> CH3OH + CH2O + O2
which is based on experimental data from Baulch et al. in JPCRD (2005)
(https://doi.org/10.1063/1.1748524).
""",
)

entry(
    index = 2,
    label = "C2H5O2 + C2H5O2-2 <=> C2H4O + O2 + C2H6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.3e+09, 'cm^3/(mol*s)'), n=0, Ea=(-850, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc =
u"""
Taken from entry CH3CH2OO + CH3CH2OO <=> CH3CHO + CH3CH2OH + O2
which is based on a fitted expression combining rates from Fenter et al. in J. Phys. Chem. 1993
(https://doi.org/10.1021/j100116a016) with a branching ratio from Lightfoot et al.
in Atmos. Environ. A 1992 (https://doi.org/10.1016/0960-1686(92)90423-I).
""",
)

entry(
    index = 3,
    label = "CH3O2 + C2H3O3 <=> CH2O + O2 + C2H4O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Experimental rate from Atkinson et al. (2006)""",
    longDesc =
u"""
Based on the experimental rates from Atkinson et al. in Atmos. Chem. Phys. (2006)
(https://doi.org/10.5194/acp-6-3625-2006).
""",
)

entry(
    index = 4,
    label = "Me2CHO2 + Me2CHO2-2 <=> Me2CO + Me2CHOH + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(10.3, 'kJ/mol'), T0=(1, 'K'), Tmin=(210, 'K'),
                         Tmax=(300, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
""",
)

entry(
    index = 5,
    label = "Me2CHO2 + Me2CHO2-2 <=> Me2CO + Me2CHOH + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.2e+10, 'cm^3/(mol*s)'), n=0, Ea=(10.3, 'kJ/mol'), T0=(1, 'K'), Tmin=(210, 'K'),
                         Tmax=(300, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
""",
)

entry(
    index = 6,
    label = "C4H9CH2O2 + C4H9CH2O2-2 <=> C4H9CHO + C4H9CH2OH + O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.0e+12, 'cm^3/(mol*s)'), n=0, Ea=(9.1, 'kJ/mol'), T0=(1, 'K'), Tmin=(253, 'K'),
                         Tmax=(303, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
""",
)

entry(
    index = 7,
    label = "CH3CHO2C3H7 + CH3CHO2C3H7-2 <=> CH3COC3H7 + CH3CHOHC3H7 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.0e+10, 'cm^3/(mol*s)'), n=0, Ea=(6.9, 'kJ/mol'), T0=(1, 'K'), Tmin=(253, 'K'),
                         Tmax=(303, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
""",
)

entry(
    index = 8,
    label = "CH3CHO2C4H9 + CH3CHO2C4H9-2 <=> CH3COC4H9 + CH3CHOHC4H9 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.9e+10, 'cm^3/(mol*s)'), n=0, Ea=(8.4, 'kJ/mol'), T0=(1, 'K'), Tmin=(283, 'K'),
                         Tmax=(320, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
T range: 283-320K
""",
)

entry(
    index = 9,
    label = "cyclohexaneOO + cyclohexaneOO-2 <=> cyclohexanone + cyclohexanol + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.9e+10, 'cm^3/(mol*s)'), n=0, Ea=(5.4, 'kJ/mol'), T0=(1, 'K'), Tmin=(285, 'K'),
                         Tmax=(333, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
T range: 285-333K
""",
)

entry(
    index = 10,
    label = "Me2CdCCHOOMe + Me2CdCCHOOMe-2 <=> Me2CdCCOMe + Me2CdCCHOHMe + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(5.0, 'kJ/mol'), T0=(1, 'K'), Tmin=(313, 'K'),
                         Tmax=(333, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
T range: 313-333K
""",
)

entry(
    index = 11,
    label = "cyclohexeneOO + cyclohexeneOO-2 <=> cyclohexenone + cyclohexenol + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(8.3, 'kJ/mol'), T0=(1, 'K'), Tmin=(282, 'K'),
                         Tmax=(319, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
T range: 282-319K
""",
)

entry(
    index = 12,
    label = "benzylCCHO2 + benzylCCHO2-2 <=> benzylCCO + benzylCCHOH + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(9.4, 'kJ/mol'), T0=(1, 'K'), Tmin=(323, 'K'),
                         Tmax=(353, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
T range: 323-353K
""",
)

entry(
    index = 13,
    label = "tetralinOO + tetralinOO-2 <=> tetralinone + tetralinol + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(18.0, 'kJ/mol'), T0=(1, 'K'), Tmin=(286, 'K'),
                         Tmax=(323, 'K')),
    rank = 1,
    shortDesc = u"""Table 2.9 from Denisov et al. (1999)""",
    longDesc =
u"""
Based on Table 2.9 (experimental rates) from Handbook of Antioxidants: Bond Dissociation Energies, Rate Constants, 
Activation Energies, and Enthalpies of Reactions, Second Edition by Evgeny T. Denisov, Taissa Denisova (1999).
ISBN 9780849390043 - CAT# 9004
https://www.crcpress.com/Handbook-of-Antioxidants-Bond-Dissociation-Energies-Rate-Constants-Activation/Denisov-Denisova/p/book/9780849390043
T range: 286-323K
""",
)
