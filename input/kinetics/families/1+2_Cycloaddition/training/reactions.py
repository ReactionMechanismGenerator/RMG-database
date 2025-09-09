#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CH2 + C2H4 <=> C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.98e+12,'cm^3/(mol*s)','*|/',3.2), n=0, Ea=(22.1334,'kJ/mol'), T0=(1,'K'), Tmin=(296,'K'), Tmax=(728,'K')),
    rank = 6,
    shortDesc = """Frey et al [192]""",
    longDesc = 
"""
Converted to training reaction from rate rule: carbene;mb_db_unsub
""",
)

entry(
    index = 1,
    label = "C2H4 + O <=> C2H4O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K')),
    rank = 10,
    shortDesc = """Gaedtke et al [194]""",
    longDesc = 
"""
[194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + C2H4 --> Oxirane

Converted to training reaction from rate rule: o_atom_singlet;mb_db_unsub
""",
)

entry(
    index = 2,
    label = "C3H6-2 + O <=> C3H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.9e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K')),
    rank = 10,
    shortDesc = """Gaedtke et al [194]""",
    longDesc = 
"""
[194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + CH3CH=CH2 --> methyloxirane

Converted to training reaction from rate rule: o_atom_singlet;mb_db_monosub_Nd
""",
)

entry(
    index = 3,
    label = "C4H8 + O <=> C4H8O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.6e+12,'cm^3/(mol*s)','*|/',1.2), n=0, Ea=(0.4184,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(410,'K')),
    rank = 10,
    shortDesc = """Smith [196]""",
    longDesc = 
"""
[196] Smith, I.W.M. Trans. Faraday Soc. 1968, 64, 378.
Data derived from fitting to a complex mechanism. Excitation: flash photolysis, analysis : UV-Vis absorption. Pressure 0.13 atm

O + iso-C4H8 --> 2,2- dimethyloxirane. Original uncertainty 1.2E+12

Converted to training reaction from rate rule: o_atom_singlet;mb_db_onecdisub_Nd
""",
)

entry(
    index = 4,
    label = "C4H8-2 + O <=> C4H8O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.54e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K')),
    rank = 10,
    shortDesc = """Cvetanovic [197]""",
    longDesc = 
"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (Z)-2-C4H8 --> cis-2,3-dimethyloxirane/O + C2H4 = Oxirane --> 2.2E+01) 

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.

Converted to training reaction from rate rule: o_atom_singlet;mb_db_twocdisub_Nd
""",
)

entry(
    index = 5,
    label = "C6H12 + O <=> C6H12O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.18e+13,'cm^3/(mol*s)','*|/',1.2), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K')),
    rank = 10,
    shortDesc = """Cvetanovic [197]""",
    longDesc = 
"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (CH3)2C=C(CH3)2 --> tetramethyl-oxirane/O + iso-C4H8 --> 2,2-Dimethyloxirane = 4.18)  

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.

Converted to training reaction from rate rule: o_atom_singlet;mb_db_tetrasub_Nd
""",
)

entry(
    index = 6,
    label = "CH2 + C2H2 <=> C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.77e+15,'cm^3/(mol*s)'), n=-0.662, Ea=(0.157737,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """Polino [carbene,acetylene]""",
    longDesc = 
"""
Converted to training reaction from rate rule: carbene;mb_tb_unsub
""",
)

entry(
    index = 7,
    label = "CH2 + C3H4-2 <=> C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+15,'cm^3/(mol*s)'), n=-0.708, Ea=(-0.111713,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """Polino [carbene,propyne]""",
    longDesc = 
"""
Converted to training reaction from rate rule: carbene;mb_tb_monosub_Nd
""",
)

entry(
    index = 8,
    label = "CH2 + C3H6-2 <=> C4H8-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+15,'cm^3/(mol*s)'), n=-0.826, Ea=(-0.37656,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """Polino [carbene,propene]""",
    longDesc = 
"""
Converted to training reaction from rate rule: carbene;mb_db_monosub_Nd
""",
)

entry(
    index = 9,
    label = "CH2 + C3H4-3 <=> C4H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.276e+15,'cm^3/(mol*s)'), n=-0.562, Ea=(-0.556472,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """Polino [carbene,propadiene]""",
    longDesc = 
"""
Converted to training reaction from rate rule: carbene;mb_db_dbSub
""",
)

entry(
    index = 10,
    label = "CH2 + C4H6-3 <=> C5H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.7e+15,'cm^3/(mol*s)'), n=-0.823, Ea=(0.096232,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """Polino [carbene,2-butyne]""",
    longDesc = 
"""
Converted to training reaction from rate rule: carbene;mb_tb_disub_twoNd
""",
)

entry(
    index = 11,
    label = "CH2 + C4H6-4 <=> C5H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.7e+15,'cm^3/(mol*s)'), n=-0.7, Ea=(-0.281165,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """Polino [carbene,1,3-butadiene]""",
    longDesc = 
"""
Converted to training reaction from rate rule: carbene;mb_db_monosub_De
""",
)

entry(
    index = 12,
    label = "CF2 + C2H2F2 <=> C3H2F4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(10.1799,'cm^3/(mol*s)'), n=2.87159, Ea=(40.5376,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06608, dn = +|- 0.0084062, dEa = +|- 0.0457462 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1+2_Cycloaddition
Original entry: CF2 + CH2CF2 <=> FC1(F)CC1(F)F
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 46.330 kJ/mol

Coordinates (Angstoms):
F    -0.934462    1.059637    -0.200843
F    -0.935837    -1.070669    -0.203113
C    -0.566012    -0.006529    0.525943
C    1.462332    -0.006616    -0.635144
C    1.145769    -0.008289    0.707764
F    1.417535    1.067078    -1.368636
F    1.41614    -1.078261    -1.371548
H    1.355457    0.907116    1.240141
H    1.353729    -0.925878    1.237154
""",
)

entry(
    index = 13,
    label = "CF2 + C2H4 <=> C3H4F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(20.7011,'cm^3/(mol*s)'), n=2.98446, Ea=(43.7961,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02769, dn = +|- 0.00358817, dEa = +|- 0.0195267 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1+2_Cycloaddition
Original entry: CF2 + C2H4 <=> FC1(F)CC1
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 51.669 kJ/mol

Coordinates (Angstoms):
F    1.13937    -0.427755    -2.405891
F    1.526415    1.589949    -1.89642
C    2.09573    0.391359    -1.979214
C    1.70393    -0.104862    0.283744
C    2.88033    -0.154701    -0.412698
H    1.023432    -0.943399    0.283205
H    1.361345    0.817913    0.727979
H    3.282735    -1.104777    -0.735506
H    3.615533    0.629513    -0.29752
""",
)

entry(
    index = 14,
    label = "CCl2 + C2H4 <=> C3H4Cl2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(86.8219,'cm^3/(mol*s)'), n=2.97056, Ea=(7.89502,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02029, dn = +|- 0.00263921, dEa = +|- 0.0143625 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1+2_Cycloaddition
Original entry: CCl2 + C2H4 <=> ClC1(Cl)CC1
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 13.332 kJ/mol

Coordinates (Angstoms):
Cl    -1.300023    1.426031    -0.372885
Cl    -1.296527    -1.425679    -0.392776
C    -0.73929    -0.005277    0.479117
C    1.559199    0.005126    -0.685267
C    1.403325    -0.00398    0.650137
H    1.592075    0.932206    -1.24008
H    1.594637    -0.914481    -1.25224
H    1.431367    0.910813    1.224937
H    1.433107    -0.926539    1.212318
""",
)

entry(
    index = 15,
    label = "CF2 + C2F4 <=> C3F6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.10298,'cm^3/(mol*s)'), n=3.07477, Ea=(21.6954,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00921, dn = +|- 0.00120384, dEa = +|- 0.00655125 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1+2_Cycloaddition
Original entry: CF2 + CF2CF2 <=> FC1(F)C(F)(F)C1(F)F
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 27.482 kJ/mol

Coordinates (Angstoms):
F    -1.037731    1.037959    -0.208358
F    -1.026004    -1.058063    -0.199201
C    -0.668218    -0.00491    0.509442
C    1.509632    0.002738    -0.655919
C    1.244797    0.005764    0.682605
F    1.444742    1.087849    -1.367818
F    1.456488    -1.087722    -1.360587
F    1.435478    1.109765    1.3669
F    1.446996    -1.0922    1.373924
""",
)

entry(
    index = 16,
    label = "CBr2 + C2H4 <=> C3H4Br2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(145.611,'cm^3/(mol*s)'), n=2.95653, Ea=(-0.108502,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0219, dn = +|- 0.00284573, dEa = +|- 0.0154864 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1+2_Cycloaddition
Original entry: CBr2 + C2H4 <=> BrC1(Br)CC1
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 4.605 kJ/mol

Coordinates (Angstoms):
Br    -1.395119    1.571209    -0.413669
Br    -1.394421    -1.566739    -0.44214
C    -0.78974    -0.006163    0.511653
C    1.589777    0.004359    -0.674032
C    1.467834    -0.00445    0.659804
H    1.616426    0.931252    -1.229997
H    1.620555    -0.915194    -1.241831
H    1.479333    0.912309    1.232597
H    1.483225    -0.928362    1.220876
""",
)

entry(
    index = 17,
    label = "CF2 + CH2O <=> C2H2F2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(48.1575,'cm^3/(mol*s)'), n=2.76922, Ea=(37.8393,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09911, dn = +|- 0.0124151, dEa = +|- 0.0675623 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/1+2_Cycloaddition
Original entry: CF2 + CH2O <=> FC1(F)CO1
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 45.923 kJ/mol

Coordinates (Angstoms):
F    -1.065525    1.039756    -0.149065
F    -1.065472    -1.039826    -0.148937
C    -0.563356    1.3e-05    0.421949
O    1.438367    3e-05    -0.594004
C    1.289254    5.2e-05    0.64322
H    1.412955    0.922013    1.229339
H    1.412967    -0.921889    1.229368
""",
)

entry(
    index = 18,
    label = "C2F2O2 <=> CF2O + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.58e+12,'s^-1'), n=0.3, Ea=(9852.72,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: c_F2COC(O) <=> CF2O+CO
""",
)

entry(
    index = 19,
    label = "C2F2O2-2 <=> CO2 + CF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.17e+13,'s^-1'), n=0.33, Ea=(19504.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: c_F2COC(O) <=> CF2+CO2
""",
)

entry(
    index = 20,
    label = "C3F4O2 <=> C2F4O + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.29e+12,'s^-1'), n=0.31, Ea=(15935.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3-c_FCOC(O) <=> CF3CFO+CO
""",
)

entry(
    index = 21,
    label = "C3F4O2-2 <=> CO2 + C2F4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.81e+12,'s^-1'), n=0.64, Ea=(32162.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3-c_FCOC(O) <=> CF3CF+CO2
""",
)

entry(
    index = 22,
    label = "C4F6O2 <=> C3F6O + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.74e+12,'s^-1'), n=0.27, Ea=(15958.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5-c_FCOC(O) <=> C2F5CFO+CO
""",
)

entry(
    index = 23,
    label = "C4F6O2-2 <=> CO2 + C3F6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.9e+08,'s^-1'), n=1.39, Ea=(64235.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5-c_FCOC(O) <=> C2F5CF+CO2
""",
)

entry(
    index = 24,
    label = "C5F8O2 <=> C4F8O + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.67e+12,'s^-1'), n=0.24, Ea=(16106.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7-c_FCOC(O) <=> C3F7CFO+CO
""",
)

entry(
    index = 25,
    label = "C5F8O2-2 <=> CO2 + C4F8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.89e+13,'s^-1'), n=0.18, Ea=(32595.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7-c_FCOC(O) <=> C3F7CF+CO2
""",
)

entry(
    index = 26,
    label = "C4F6O3 <=> C3F6O2 + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.11e+11,'s^-1'), n=0.35, Ea=(17594.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3O-c_(CF3)COC(O) <=> CF3OC(O)CF3+CO
""",
)

entry(
    index = 27,
    label = "C4F6O3-2 <=> CO2 + C3F6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.62e+11,'s^-1'), n=0.59, Ea=(24008.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3O-c_(CF3)COC(O) <=> CF3OCCF3+CO2
""",
)

entry(
    index = 28,
    label = "C5F8O3 <=> C4F8O2 + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.51e+11,'s^-1'), n=0.39, Ea=(17285.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5O-c_(CF3)COC(O) <=> C2F5OC(O)CF3+CO
""",
)

entry(
    index = 29,
    label = "C5F8O3-2 <=> CO2 + C4F8O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.01e+13,'s^-1'), n=0.17, Ea=(24869.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5O-c_(CF3)COC(O) <=> C2F5OCCF3+CO2
""",
)

entry(
    index = 30,
    label = "C6F10O3 <=> C5F10O2 + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.46e+11,'s^-1'), n=0.45, Ea=(17288.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7O-c_(CF3)COC(O) <=> C3F7OC(O)CF3+CO
""",
)

entry(
    index = 31,
    label = "C6F10O3-2 <=> CO2 + C5F10O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.73e+13,'s^-1'), n=-0.01, Ea=(25134.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7O-c_(CF3)COC(O) <=> C3F7OCCF3+CO2
""",
)

entry(
    index = 32,
    label = "C2H2O2 <=> CH2O-2 + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.48e+12,'s^-1'), n=0.3, Ea=(28548.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: c_H2COC(O) <=> CH2O+CO
""",
)

entry(
    index = 33,
    label = "C2H2O2-2 <=> CO2 + CH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.18e+12,'s^-1'), n=0.62, Ea=(56045.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: c_H2COC(O) <=> CH2+CO2
""",
)

entry(
    index = 34,
    label = "C3H4O2 <=> C2H4O-2 + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.55e+11,'s^-1'), n=0.54, Ea=(27711.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH3-c_HCOC(O) <=> CH3CHO+CO
""",
)

entry(
    index = 35,
    label = "C3H4O2-2 <=> CO2 + C2H4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.05e+11,'s^-1'), n=0.76, Ea=(61244.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH3-c_HCOC(O) <=> CH3CH+CO2
""",
)

entry(
    index = 36,
    label = "C4H6O2 <=> C3H6O-2 + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.63e+11,'s^-1'), n=0.61, Ea=(27229,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2H5-c_HCOC(O) <=> C2H5CHO+CO
""",
)

entry(
    index = 37,
    label = "C4H6O2-2 <=> CO2 + C3H6-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.01e+11,'s^-1'), n=0.87, Ea=(61019.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2H5-c_HCOC(O) <=> C2H5CH+CO2
""",
)

entry(
    index = 38,
    label = "C4H6O3 <=> C3H6O2 + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.39e+10,'s^-1'), n=0.65, Ea=(20326.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH3O-c_(CH3)COC(O) <=> CH3OC(O)CH3+CO
""",
)

entry(
    index = 39,
    label = "C4H6O3-2 <=> CO2 + C3H6O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.11e+15,'s^-1'), n=-0.47, Ea=(16581.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH3O-c_(CH3)COC(O) <=> CH3OCCH3+CO2
""",
)

entry(
    index = 40,
    label = "C5H8O3 <=> C4H8O2 + CO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.55e+10,'s^-1'), n=0.75, Ea=(20718.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2H5O-c_(CH3)COC(O) <=> C2H5OC(O)CH3+CO
""",
)

entry(
    index = 41,
    label = "C5H8O3-2 <=> CO2 + C4H8O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.43e+14,'s^-1'), n=-0.25, Ea=(15680.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2H5O-c_(CH3)COC(O) <=> C2H5OCCH3+CO2
""",
)

