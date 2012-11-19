#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 576,
    label = "elec_def;multiplebond",
    group1 = "OR{carbene, me_carbene, dime_carbene, ph_carbene, o_atom}",
    group2 = 
"""
1 *1 {Cd,CO} 0 {2,D}
2 *2 {Cd,O}  0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 577,
    label = "carbene;mb_db_unsub",
    group1 = 
"""
1 *3 C {2S,2T} {2,S} {3,S}
2    H 0       {1,S}
3    H 0       {1,S}
""",
    group2 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1980000000000.0, 'cm^3/(mol*s)', '*|/', 3.2),
        n = 0,
        alpha = 0,
        E0 = (5.29, 'kcal/mol', '+|-', 0.26),
        Tmin = (296, 'K'),
        Tmax = (728, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Frey et al [192]""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 579,
    label = "o_atom;mb_db_unsub",
    group1 = 
"""
1 *3 O {2S,2T}
""",
    group2 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Gaedtke et al [194]""",
    longDesc = 
u"""
[194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + C2H4 --> Oxirane
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 580,
    label = "o_atom;mb_db_monosub_Nd",
    group1 = 
"""
1 *3 O {2S,2T}
""",
    group2 = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Gaedtke et al [194]""",
    longDesc = 
u"""
[194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + CH3CH=CH2 --> methyloxirane
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 581,
    label = "o_atom;mb_db_monosub_Nd",
    group1 = 
"""
1 *3 O {2S,2T}
""",
    group2 = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (4200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (275, 'K'),
        Tmax = (360, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Herbrechtsmeier et al [195]""",
    longDesc = 
u"""
[195] Herbrechtsmeier, P. Reactions of O(3P) Atoms with Unsaturated C3 Hydrocarbons. In Combust. Inst. European Symp., 1973; pp13.
Absolute values measured directly. Excitation: discharge, analysis :GC, Pressure 0.01 atm. O + CH3CH=CH2 --> methyloxirane
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 582,
    label = "o_atom;mb_db_monosub_Nd",
    group1 = 
"""
1 *3 O {2S,2T}
""",
    group2 = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1900000000000.0, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        alpha = 0,
        E0 = (0.8, 'kcal/mol', '+|-', 0.4),
        Tmin = (298, 'K'),
        Tmax = (410, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Smith [196]""",
    longDesc = 
u"""
[196] Smith, I.W.M. Trans. Faraday Soc. 1968, 64, 378.
Data derived from fitting to a complex mechanism. Excitation: flash photolysis, analysis : UV-Vis absorption. Pressure 0.13 atm

O + 1-C4H8 --> ethyloxirane. Original uncertainty 3.0E+11
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 583,
    label = "o_atom;mb_db_onecdisub_Nd",
    group1 = 
"""
1 *3 O {2S,2T}
""",
    group2 = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (7600000000000.0, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        alpha = 0,
        E0 = (0.1, 'kcal/mol', '+|-', 0.4),
        Tmin = (298, 'K'),
        Tmax = (410, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Smith [196]""",
    longDesc = 
u"""
[196] Smith, I.W.M. Trans. Faraday Soc. 1968, 64, 378.
Data derived from fitting to a complex mechanism. Excitation: flash photolysis, analysis : UV-Vis absorption. Pressure 0.13 atm

O + iso-C4H8 --> 2,2- dimethyloxirane. Original uncertainty 1.2E+12
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 584,
    label = "o_atom;mb_db_twocdisub_Nd",
    group1 = 
"""
1 *3 O {2S,2T}
""",
    group2 = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (15400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (Z)-2-C4H8 --> cis-2,3-dimethyloxirane/O + C2H4 = Oxirane --> 2.2E+01) 

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 585,
    label = "o_atom;mb_db_tetrasub_Nd",
    group1 = 
"""
1 *3 O {2S,2T}
""",
    group2 = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cd     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (31800000000000.0, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (CH3)2C=C(CH3)2 --> tetramethyl-oxirane/O + iso-C4H8 --> 2,2-Dimethyloxirane = 4.18)  

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

