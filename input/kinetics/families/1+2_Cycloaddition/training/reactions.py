#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "CH2 + C2H4 <=> C3H6",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.98e+12, 'cm^3/(mol*s)', '*|/', 3.2),
        n = 0,
        alpha = 0,
        E0 = (5.29, 'kcal/mol', '+|-', 0.26),
        Tmin = (296, 'K'),
        Tmax = (728, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""Frey et al [192]""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: carbene;mb_db_unsub
""",
)

entry(
    index = 1,
    label = "O + C2H4 <=> C2H4O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (7e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""Gaedtke et al [194]""",
    longDesc = 
u"""
Taken from entry: [194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + C2H4 --> Oxirane

Converted to training reaction from rate rule: o_atom_singlet;mb_db_unsub
""",
)

entry(
    index = 2,
    label = "O + C3H6-2 <=> C3H6O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""Gaedtke et al [194]""",
    longDesc = 
u"""
Taken from entry: [194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + CH3CH=CH2 --> methyloxirane

Degeneracy not recalculated

Converted to training reaction from rate rule: o_atom_singlet;mb_db_monosub_Nd
""",
)

entry(
    index = 3,
    label = "O + C4H8 <=> C4H8O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (7.6e+12, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        alpha = 0,
        E0 = (0.1, 'kcal/mol', '+|-', 0.4),
        Tmin = (298, 'K'),
        Tmax = (410, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""Smith [196]""",
    longDesc = 
u"""
Taken from entry: [196] Smith, I.W.M. Trans. Faraday Soc. 1968, 64, 378.
Data derived from fitting to a complex mechanism. Excitation: flash photolysis, analysis : UV-Vis absorption. Pressure 0.13 atm

O + iso-C4H8 --> 2,2- dimethyloxirane. Original uncertainty 1.2E+12

Degeneracy not recalculated

Converted to training reaction from rate rule: o_atom_singlet;mb_db_onecdisub_Nd
""",
)

entry(
    index = 4,
    label = "O + C4H8-2 <=> C4H8O-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.54e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
Taken from entry: [197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (Z)-2-C4H8 --> cis-2,3-dimethyloxirane/O + C2H4 = Oxirane --> 2.2E+01) 

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.

Converted to training reaction from rate rule: o_atom_singlet;mb_db_twocdisub_Nd
""",
)

entry(
    index = 5,
    label = "O + C6H12 <=> C6H12O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.18e+13, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
Taken from entry: [197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (CH3)2C=C(CH3)2 --> tetramethyl-oxirane/O + iso-C4H8 --> 2,2-Dimethyloxirane = 4.18)  

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.

Converted to training reaction from rate rule: o_atom_singlet;mb_db_tetrasub_Nd
""",
)

entry(
    index = 6,
    label = "CH2 + C2H2 <=> C3H4",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.77e+15, 'cm^3/(mol*s)'),
        n = -0.662,
        alpha = 0,
        E0 = (0.0377, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Polino [carbene,acetylene]""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: carbene;mb_tb_unsub
""",
)

entry(
    index = 7,
    label = "CH2 + C3H4-2 <=> C4H6",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (4.5e+15, 'cm^3/(mol*s)'),
        n = -0.708,
        alpha = 0,
        E0 = (-0.0267, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Polino [carbene,propyne]""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: carbene;mb_tb_monosub_Nd
""",
)

entry(
    index = 8,
    label = "CH2 + C3H6-2 <=> C4H8-3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (5e+15, 'cm^3/(mol*s)'),
        n = -0.826,
        alpha = 0,
        E0 = (-0.09, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Polino [carbene,propene]""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: carbene;mb_db_monosub_Nd
""",
)

entry(
    index = 9,
    label = "CH2 + C3H4-3 <=> C4H6-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (6.38e+14, 'cm^3/(mol*s)'),
        n = -0.562,
        alpha = 0,
        E0 = (-0.133, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Polino [carbene,propadiene]""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: carbene;mb_db_dbSub
""",
)

entry(
    index = 10,
    label = "CH2 + C4H6-3 <=> C5H8",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (4.7e+15, 'cm^3/(mol*s)'),
        n = -0.823,
        alpha = 0,
        E0 = (0.023, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Polino [carbene,2-butyne]""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: carbene;mb_tb_disub_twoNd
""",
)

entry(
    index = 11,
    label = "CH2 + C4H6-4 <=> C5H8-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.85e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        alpha = 0,
        E0 = (-0.0672, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""Polino [carbene,1,3-butadiene]""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: carbene;mb_db_monosub_De
""",
)

