#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Review and estimation based on experimental results""",
    longDesc = 
u"""
p. 519
R. Atkinson, D.L. Baulch, R.A. Cox, R.F. Hampson, J.A. Kerr, J. Troe,
Evaluated Kinetic Data for Combustion Modelling
Journal of Physical and Chemical Reference Data, 1992, 21, 411,
doi: 10.1063/1.555918
""",
)

entry(
    index = 1,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""FFCM-1""",
    longDesc = 
u"""
Taken from the FFCM-1 library
""",
)

entry(
    index = 2,
    label = "HCO + O2 <=> CO + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(1690, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Review and estimation based on experimental results""",
    longDesc = 
u"""
p. 1147, rxn (15,3)
W. Tsang and R. F. Hampson
Journal of Physical and Chemical Reference Data, 1986, 15, 1087
doi: 10.1063/1.555759
""",
)

entry(
    index = 3,
    label = "HCO + CH3 <=> CO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (1004, 'K'),
        Tmax = (1006, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Shock Tube""",
    longDesc = 
u"""
p. 4131, Table 1, rxn [16]
reported at 1005 K (value is anyway T-independent)
A.M. Held, K.C. Manthorne, P.D. Pacey, H.P. Reinholdt,
Canadian Journal of Chemistry, 1977, 55(23), 4128-4134
doi: 10.1139/v77-585
""",
)

entry(
    index = 4,
    label = "HCO + CH3O <=> CO + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Review and estimation based on experimental results""",
    longDesc = 
u"""
p. 1246, rxn (24,15)
W. Tsang and R. F. Hampson
Journal of Physical and Chemical Reference Data, 1986, 15, 1087
doi: 10.1063/1.555759
""",
)

entry(
    index = 5,
    label = "HCO + HCO_Y <=> CO + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)', '+|-', 9e+12),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Review and estimation based on experimental results""",
    longDesc = 
u"""
p. 1151, rxn (15,15 a)
W. Tsang and R. F. Hampson
Journal of Physical and Chemical Reference Data, 1986, 15, 1087
doi: 10.1063/1.555759
""",
)

entry(
    index = 6,
    label = "HCO + C2H3 <=> CO + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.033e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""JetSurF2.0""",
    longDesc = 
u"""
Taken from the JetSurF2.0 library
""",
)

entry(
    index = 7,
    label = "HCO + nC3H7 <=> CO + C3H8_n",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""JetSurF2.0""",
    longDesc = 
u"""
Taken from the JetSurF2.0 library
""",
)

entry(
    index = 8,
    label = "HCO + iC3H7 <=> CO + C3H8_i",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""JetSurF2.0""",
    longDesc = 
u"""
Taken from the JetSurF2.0 library
""",
)

entry(
    index = 9,
    label = "HCO + NO <=> CO + HNO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Shock Tube""",
    longDesc = 
u"""
p. 4180, Table 2, rxn 1
J. Dammeier , M. Colberg, G. Friedrichs,
Phys. Chem. Chem. Phys., 2007, 9, 4177-4188
doi: 10.1039/B704197G

[Also available from: Z.F. Xu, C.-H. Hsu, M.C. Lin, J. Chem. Phys., 2005, 122, 234308, doi: 10.1063/1.1917834
calculations done at the G2M(CC5)//B3LYP/6-311G(d, p) level of theory
T ranges: 200-500 & 500-3000 K]
""",
)

entry(
    index = 10,
    label = "HCO + NO2 <=> CO + HONO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.24e+23, 'cm^3/(mol*s)'),
        n = -3.29,
        Ea = (2355, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (1140, 'K'),
        Tmax = (1650, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Shock Tube""",
    longDesc = 
u"""
p. 463, Table II, rxn 2
C-Y. Lin, H-T. Wang, M.C. Lin, C.F. Melius,
Int. J. Chem. Kin, 1990, 22(5), 455-482
doi: 10.1002/kin.550220504
""",
)

entry(
    index = 11,
    label = "CH2OH + HCO <=> CH3OH + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1002/kin.10183""",
)

entry(
    index = 12,
    label = "C2H5 + HCO <=> C2H6 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Taken from Klippenstein_Glarborg2016, Experimental, original source: doi 10.1021/j100296a057""",
)

entry(
    index = 13,
    label = "HCO + CH2F <=> CO + CH3F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 14,
    label = "HCO + CHF2 <=> CO + CH2F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 15,
    label = "HCO + CF3 <=> CO + CHF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 16,
    label = "CF + HCO => CHF + CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 17,
    label = "HCO + F <=> CO + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 18,
    label = "[OH]_r1 + HCO <=> CO + O_p41",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST 2019 CH2F2 model""",
)

entry(
    index = 19,
    label = "HCO + H <=> H2-2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.592e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is HCO + H <=> CO + H2""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: HCO + H <=> CO + H2
""",
)

entry(
    index = 20,
    label = "HCO + OH <=> O_p41 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.02e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is HCO + OH <=> CO + H2O""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: HCO + OH <=> CO + H2O
""",
)

entry(
    index = 21,
    label = "HCO + O2 <=> HO2 + CO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.408e+10,'cm^3/(mol*s)'), n=0.807, Ea=(-727,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is HCO + O2 <=> CO + HO2""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: HCO + O2 <=> CO + HO2
""",
)

entry(
    index = 22,
    label = "HCO + CH3 <=> CH4 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.48e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3 + HCO <=> CH4 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3 + HCO <=> CH4 + CO
""",
)

entry(
    index = 23,
    label = "HCO + C3H3 <=> C3H4 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is C3H3 + HCO <=> aC3H4 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: C3H3 + HCO <=> aC3H4 + CO
""",
)

entry(
    index = 24,
    label = "HCO + C3H3-2 <=> C3H4-2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is C3H3 + HCO <=> pC3H4 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: C3H3 + HCO <=> pC3H4 + CO
""",
)

entry(
    index = 25,
    label = "HCO + C3H5 <=> C3H6 + CO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is aC3H5 + HCO <=> C3H6 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: aC3H5 + HCO <=> C3H6 + CO
""",
)

entry(
    index = 26,
    label = "HCO + C3H5-2 <=> C3H6-2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3CCH2 + HCO <=> C3H6 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3CCH2 + HCO <=> C3H6 + CO
""",
)

entry(
    index = 27,
    label = "HCO + C3H5-3 <=> C3H6-3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3CHCH + HCO <=> C3H6 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3CHCH + HCO <=> C3H6 + CO
""",
)

entry(
    index = 28,
    label = "HCO + C4H5 <=> C4H6 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is nC4H5 + HCO <=> C4H6 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: nC4H5 + HCO <=> C4H6 + CO
""",
)

entry(
    index = 29,
    label = "HCO + C4H5-2 <=> C4H6-2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is iC4H5 + HCO <=> C4H6 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: iC4H5 + HCO <=> C4H6 + CO
""",
)

entry(
    index = 30,
    label = "HCO + C4H7 <=> C4H8 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is C4H7 + HCO <=> C4H81 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: C4H7 + HCO <=> C4H81 + CO
""",
)

entry(
    index = 31,
    label = "HCO + C4H9 <=> C4H10 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is pC4H9 + HCO <=> C4H10 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: pC4H9 + HCO <=> C4H10 + CO
""",
)

entry(
    index = 32,
    label = "HCO + C4H9-2 <=> C4H10-2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is sC4H9 + HCO <=> C4H10 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: sC4H9 + HCO <=> C4H10 + CO
""",
)

entry(
    index = 33,
    label = "HCO + C4H9-3 <=> C4H10-3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is iC4H9 + HCO <=> iC4H10 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: iC4H9 + HCO <=> iC4H10 + CO
""",
)

entry(
    index = 34,
    label = "HCO + C4H9-4 <=> C4H10-4 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is tC4H9 + HCO <=> iC4H10 + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: tC4H9 + HCO <=> iC4H10 + CO
""",
)

entry(
    index = 35,
    label = "HCO + CH2F <=> CH3F-2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is HCO + CH2F <=> CO + CH3F""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: HCO + CH2F <=> CO + CH3F
""",
)

entry(
    index = 36,
    label = "HCO + CHF2 <=> CH2F2-2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is HCO + CHF2 <=> CO + CH2F2""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: HCO + CHF2 <=> CO + CH2F2
""",
)

entry(
    index = 37,
    label = "HCO + CF3 <=> CHF3-2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is HCO + CF3 <=> CO + CHF3""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: HCO + CF3 <=> CO + CHF3
""",
)

entry(
    index = 38,
    label = "HCO + CF => CHF-2 + CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CF + HCO => CHF + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CF + HCO => CHF + CO
""",
)

entry(
    index = 39,
    label = "HCO + F <=> FH + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is HCO + F <=> CO + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: HCO + F <=> CO + HF
""",
)

entry(
    index = 40,
    label = "HCO + Br <=> BrH + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is BR + HCO <=> HBR + CO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: BR + HCO <=> HBR + CO
""",
)

entry(
    index = 41,
    label = "HCO + BrO <=> BrHO + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is HCO + BRO <=> CO + BROH""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: HCO + BRO <=> CO + BROH
""",
)

