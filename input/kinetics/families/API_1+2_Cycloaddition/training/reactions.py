#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CH2 + C2H4 <=> C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.98e+12, 'cm^3/(mol*s)', '*|/', 3.2),
        n = 0,
        Ea = (22.1334, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (296, 'K'),
        Tmax = (728, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Frey et al [192]""",
    longDesc = 
u"""
Converted to training reaction from rate rule: carbene;mb_db_unsub
""",
)

entry(
    index = 2,
    label = "C2H4 + O <=> C2H4O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Gaedtke et al [194]""",
    longDesc = 
u"""
[194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + C2H4 --> Oxirane

Converted to training reaction from rate rule: o_atom_singlet;mb_db_unsub
""",
)

entry(
    index = 3,
    label = "C3H6-2 + O <=> C3H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Gaedtke et al [194]""",
    longDesc = 
u"""
[194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + CH3CH=CH2 --> methyloxirane

Converted to training reaction from rate rule: o_atom_singlet;mb_db_monosub_Nd
""",
)

entry(
    index = 4,
    label = "C4H8 + O <=> C4H8O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.6e+12, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (0.4184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (410, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Smith [196]""",
    longDesc = 
u"""
[196] Smith, I.W.M. Trans. Faraday Soc. 1968, 64, 378.
Data derived from fitting to a complex mechanism. Excitation: flash photolysis, analysis : UV-Vis absorption. Pressure 0.13 atm

O + iso-C4H8 --> 2,2- dimethyloxirane. Original uncertainty 1.2E+12

Converted to training reaction from rate rule: o_atom_singlet;mb_db_onecdisub_Nd
""",
)

entry(
    index = 5,
    label = "C4H8-2 + O <=> C4H8O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.54e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (Z)-2-C4H8 --> cis-2,3-dimethyloxirane/O + C2H4 = Oxirane --> 2.2E+01) 

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.

Converted to training reaction from rate rule: o_atom_singlet;mb_db_twocdisub_Nd
""",
)

entry(
    index = 6,
    label = "C6H12 + O <=> C6H12O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.18e+13, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (CH3)2C=C(CH3)2 --> tetramethyl-oxirane/O + iso-C4H8 --> 2,2-Dimethyloxirane = 4.18)  

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.

Converted to training reaction from rate rule: o_atom_singlet;mb_db_tetrasub_Nd
""",
)

entry(
    index = 7,
    label = "CH2 + C2H2 <=> C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.77e+15, 'cm^3/(mol*s)'),
        n = -0.662,
        Ea = (0.157737, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Polino [carbene,acetylene]""",
    longDesc = 
u"""
Converted to training reaction from rate rule: carbene;mb_tb_unsub
""",
)

entry(
    index = 8,
    label = "CH2 + C3H4-2 <=> C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.5e+15, 'cm^3/(mol*s)'),
        n = -0.708,
        Ea = (-0.111713, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Polino [carbene,propyne]""",
    longDesc = 
u"""
Converted to training reaction from rate rule: carbene;mb_tb_monosub_Nd
""",
)

entry(
    index = 9,
    label = "CH2 + C3H6-2 <=> C4H8-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5e+15, 'cm^3/(mol*s)'),
        n = -0.826,
        Ea = (-0.37656, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Polino [carbene,propene]""",
    longDesc = 
u"""
Converted to training reaction from rate rule: carbene;mb_db_monosub_Nd
""",
)

entry(
    index = 10,
    label = "CH2 + C3H4-3 <=> C4H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.276e+15, 'cm^3/(mol*s)'),
        n = -0.562,
        Ea = (-0.556472, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Polino [carbene,propadiene]""",
    longDesc = 
u"""
Converted to training reaction from rate rule: carbene;mb_db_dbSub
""",
)

entry(
    index = 11,
    label = "CH2 + C4H6-3 <=> C5H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.7e+15, 'cm^3/(mol*s)'),
        n = -0.823,
        Ea = (0.096232, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Polino [carbene,2-butyne]""",
    longDesc = 
u"""
Converted to training reaction from rate rule: carbene;mb_tb_disub_twoNd
""",
)

entry(
    index = 12,
    label = "CH2 + C4H6-4 <=> C5H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.7e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-0.281165, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Polino [carbene,1,3-butadiene]""",
    longDesc = 
u"""
Converted to training reaction from rate rule: carbene;mb_db_monosub_De
""",
)

