#!/usr/bin/env python
# encoding: utf-8

name = "Cl_Abstraction/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.23264e+11,'m^3/(mol*s)'), n=-1.51065, w0=(331617,'J/mol'), E0=(86258.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2207527151441772, var=9.400169842575828, Tref=1000.0, N=464, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 464 training reactions at node Root
    Total Standard Deviation in ln(k): 6.701111949709109"""),
    rank = 11,
    shortDesc = """BM rule fitted to 464 training reactions at node Root
Total Standard Deviation in ln(k): 6.701111949709109""",
    longDesc = 
"""
BM rule fitted to 464 training reactions at node Root
Total Standard Deviation in ln(k): 6.701111949709109
""",
)

entry(
    index = 2,
    label = "Root_3R->H",
    kinetics = ArrheniusBM(A=(2051.98,'m^3/(mol*s)'), n=1.35725, w0=(375737,'J/mol'), E0=(65546.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.021264975340439366, var=1.4166129901551003, Tref=1000.0, N=78, data_mean=0.0, correlation='Root_3R->H',), comment="""BM rule fitted to 78 training reactions at node Root_3R->H
    Total Standard Deviation in ln(k): 2.439496394027913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 78 training reactions at node Root_3R->H
Total Standard Deviation in ln(k): 2.439496394027913""",
    longDesc = 
"""
BM rule fitted to 78 training reactions at node Root_3R->H
Total Standard Deviation in ln(k): 2.439496394027913
""",
)

entry(
    index = 3,
    label = "Root_N-3R->H",
    kinetics = ArrheniusBM(A=(7.58241e+09,'m^3/(mol*s)'), n=-0.994622, w0=(322701,'J/mol'), E0=(82121.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19866070474170566, var=9.555654490051728, Tref=1000.0, N=386, data_mean=0.0, correlation='Root_N-3R->H',), comment="""BM rule fitted to 386 training reactions at node Root_N-3R->H
    Total Standard Deviation in ln(k): 6.696229010948411"""),
    rank = 11,
    shortDesc = """BM rule fitted to 386 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 6.696229010948411""",
    longDesc = 
"""
BM rule fitted to 386 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 6.696229010948411
""",
)

entry(
    index = 4,
    label = "Root_3R->H_1R->C",
    kinetics = ArrheniusBM(A=(7.46526e-07,'m^3/(mol*s)'), n=4.15001, w0=(377500,'J/mol'), E0=(42651.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12344030733613352, var=1.1554202393680173, Tref=1000.0, N=73, data_mean=0.0, correlation='Root_3R->H_1R->C',), comment="""BM rule fitted to 73 training reactions at node Root_3R->H_1R->C
    Total Standard Deviation in ln(k): 2.4650507997473308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 73 training reactions at node Root_3R->H_1R->C
Total Standard Deviation in ln(k): 2.4650507997473308""",
    longDesc = 
"""
BM rule fitted to 73 training reactions at node Root_3R->H_1R->C
Total Standard Deviation in ln(k): 2.4650507997473308
""",
)

entry(
    index = 5,
    label = "Root_3R->H_N-1R->C",
    kinetics = ArrheniusBM(A=(8.85,'m^3/(mol*s)'), n=2.24777, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0371460646733894, var=2.49313979339776, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_N-1R->C',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_N-1R->C
    Total Standard Deviation in ln(k): 3.2587442602142214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_N-1R->C
Total Standard Deviation in ln(k): 3.2587442602142214""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_N-1R->C
Total Standard Deviation in ln(k): 3.2587442602142214
""",
)

entry(
    index = 6,
    label = "Root_N-3R->H_1R->H",
    kinetics = ArrheniusBM(A=(517.174,'m^3/(mol*s)'), n=1.06849, w0=(375616,'J/mol'), E0=(78038,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06768869673353681, var=3.1436532829805284, Tref=1000.0, N=73, data_mean=0.0, correlation='Root_N-3R->H_1R->H',), comment="""BM rule fitted to 73 training reactions at node Root_N-3R->H_1R->H
    Total Standard Deviation in ln(k): 3.724537657393341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 73 training reactions at node Root_N-3R->H_1R->H
Total Standard Deviation in ln(k): 3.724537657393341""",
    longDesc = 
"""
BM rule fitted to 73 training reactions at node Root_N-3R->H_1R->H
Total Standard Deviation in ln(k): 3.724537657393341
""",
)

entry(
    index = 7,
    label = "Root_N-3R->H_N-1R->H",
    kinetics = ArrheniusBM(A=(8.73332e+16,'m^3/(mol*s)'), n=-3.0675, w0=(310360,'J/mol'), E0=(94527.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3126959480100204, var=10.113764902544617, Tref=1000.0, N=313, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H',), comment="""BM rule fitted to 313 training reactions at node Root_N-3R->H_N-1R->H
    Total Standard Deviation in ln(k): 7.16115597349631"""),
    rank = 11,
    shortDesc = """BM rule fitted to 313 training reactions at node Root_N-3R->H_N-1R->H
Total Standard Deviation in ln(k): 7.16115597349631""",
    longDesc = 
"""
BM rule fitted to 313 training reactions at node Root_N-3R->H_N-1R->H
Total Standard Deviation in ln(k): 7.16115597349631
""",
)

entry(
    index = 8,
    label = "Root_3R->H_1R->C_1C-u0",
    kinetics = ArrheniusBM(A=(1.48913e-07,'m^3/(mol*s)'), n=4.37039, w0=(377500,'J/mol'), E0=(40634.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13439982238542433, var=0.8781504845739581, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0',), comment="""BM rule fitted to 65 training reactions at node Root_3R->H_1R->C_1C-u0
    Total Standard Deviation in ln(k): 2.2163188988359974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_3R->H_1R->C_1C-u0
Total Standard Deviation in ln(k): 2.2163188988359974""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_3R->H_1R->C_1C-u0
Total Standard Deviation in ln(k): 2.2163188988359974
""",
)

entry(
    index = 9,
    label = "Root_3R->H_1R->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(8.57449e-21,'m^3/(mol*s)'), n=8.21027, w0=(377500,'J/mol'), E0=(3830.17,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.39536360992613273, var=1.2807108859294063, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0',), comment="""BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_N-1C-u0
    Total Standard Deviation in ln(k): 3.2621044731922826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_N-1C-u0
Total Standard Deviation in ln(k): 3.2621044731922826""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_N-1C-u0
Total Standard Deviation in ln(k): 3.2621044731922826
""",
)

entry(
    index = 10,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0",
    kinetics = ArrheniusBM(A=(48.4284,'m^3/(mol*s)'), n=2.08043, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022845712994763158, var=0.4263642689185543, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0
    Total Standard Deviation in ln(k): 1.3664246296001894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0
Total Standard Deviation in ln(k): 1.3664246296001894""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0
Total Standard Deviation in ln(k): 1.3664246296001894
""",
)

entry(
    index = 11,
    label = "Root_3R->H_N-1R->C_N-1BrClFHO-u0",
    kinetics = ArrheniusBM(A=(5996.23,'m^3/(mol*s)'), n=1.20842, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-1R->C_N-1BrClFHO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_N-1BrClFHO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_N-1BrClFHO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_N-1BrClFHO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.16061e-17,'m^3/(mol*s)'), n=6.88425, w0=(377500,'J/mol'), E0=(26650.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23369028879605863, var=1.1422848164415893, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 68 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 2.729776778565254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.729776778565254""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.729776778565254
""",
)

entry(
    index = 13,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0013899,'m^3/(mol*s)'), n=3.22037, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06812500328699421, var=2.334365244605693, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 3.2341288324948474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.2341288324948474""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.2341288324948474
""",
)

entry(
    index = 14,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C",
    kinetics = ArrheniusBM(A=(4.61801e+18,'m^3/(mol*s)'), n=-3.56299, w0=(319125,'J/mol'), E0=(101739,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.34356952338514407, var=9.715932749711873, Tref=1000.0, N=226, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C',), comment="""BM rule fitted to 226 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C
    Total Standard Deviation in ln(k): 7.112077629493091"""),
    rank = 11,
    shortDesc = """BM rule fitted to 226 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C
Total Standard Deviation in ln(k): 7.112077629493091""",
    longDesc = 
"""
BM rule fitted to 226 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C
Total Standard Deviation in ln(k): 7.112077629493091
""",
)

entry(
    index = 15,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C",
    kinetics = ArrheniusBM(A=(1.61683e+06,'m^3/(mol*s)'), n=0.0653341, w0=(287590,'J/mol'), E0=(60073.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1257641727650251, var=10.27938290041031, Tref=1000.0, N=87, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C',), comment="""BM rule fitted to 87 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C
    Total Standard Deviation in ln(k): 6.743467086989992"""),
    rank = 11,
    shortDesc = """BM rule fitted to 87 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C
Total Standard Deviation in ln(k): 6.743467086989992""",
    longDesc = 
"""
BM rule fitted to 87 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C
Total Standard Deviation in ln(k): 6.743467086989992
""",
)

entry(
    index = 16,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.39589e-07,'m^3/(mol*s)'), n=4.3781, w0=(377500,'J/mol'), E0=(40440.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13491134996643814, var=0.8913871131680193, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 64 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 2.231709774900501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.231709774900501""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.231709774900501
""",
)

entry(
    index = 17,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.52071e-20,'m^3/(mol*s)'), n=7.98835, w0=(377500,'J/mol'), E0=(-4013.05,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.46502376790797956, var=0.5928579397729297, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 2.711992682531702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.711992682531702""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.711992682531702
""",
)

entry(
    index = 18,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R",
    kinetics = ArrheniusBM(A=(17.8513,'m^3/(mol*s)'), n=2.20559, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.029257265796347316, var=0.5901362934183971, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R
    Total Standard Deviation in ln(k): 1.6135547983543979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R
Total Standard Deviation in ln(k): 1.6135547983543979""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R
Total Standard Deviation in ln(k): 1.6135547983543979
""",
)

entry(
    index = 19,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1",
    kinetics = ArrheniusBM(A=(5.80951e-17,'m^3/(mol*s)'), n=6.65866, w0=(377500,'J/mol'), E0=(28867.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22120956798864808, var=1.1075974739919268, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1',), comment="""BM rule fitted to 65 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1
    Total Standard Deviation in ln(k): 2.665635384961141"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1
Total Standard Deviation in ln(k): 2.665635384961141""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1
Total Standard Deviation in ln(k): 2.665635384961141
""",
)

entry(
    index = 20,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(0.00318409,'m^3/(mol*s)'), n=2.92164, w0=(377500,'J/mol'), E0=(67270.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010105404464754518, var=2.119307810216056, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1
    Total Standard Deviation in ln(k): 2.9438522336227497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1
Total Standard Deviation in ln(k): 2.9438522336227497""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1
Total Standard Deviation in ln(k): 2.9438522336227497
""",
)

entry(
    index = 21,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R",
    kinetics = ArrheniusBM(A=(0.000213318,'m^3/(mol*s)'), n=3.47976, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06887581201262677, var=4.341998568827702, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R
    Total Standard Deviation in ln(k): 4.3504140684858195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R
Total Standard Deviation in ln(k): 4.3504140684858195""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R
Total Standard Deviation in ln(k): 4.3504140684858195
""",
)

entry(
    index = 22,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1",
    kinetics = ArrheniusBM(A=(188.748,'m^3/(mol*s)'), n=1.64016, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1",
    kinetics = ArrheniusBM(A=(26.7577,'m^3/(mol*s)'), n=1.79078, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0",
    kinetics = ArrheniusBM(A=(1.87448e+14,'m^3/(mol*s)'), n=-2.2759, w0=(319419,'J/mol'), E0=(93182.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2741152728475844, var=9.32859608864046, Tref=1000.0, N=213, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0',), comment="""BM rule fitted to 213 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0
    Total Standard Deviation in ln(k): 6.811744172560566"""),
    rank = 11,
    shortDesc = """BM rule fitted to 213 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0
Total Standard Deviation in ln(k): 6.811744172560566""",
    longDesc = 
"""
BM rule fitted to 213 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0
Total Standard Deviation in ln(k): 6.811744172560566
""",
)

entry(
    index = 25,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(3.36993e+40,'m^3/(mol*s)'), n=-9.85127, w0=(314308,'J/mol'), E0=(139568,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6597821362178538, var=13.408268051693932, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0
    Total Standard Deviation in ln(k): 8.99854303512776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0
Total Standard Deviation in ln(k): 8.99854303512776""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0
Total Standard Deviation in ln(k): 8.99854303512776
""",
)

entry(
    index = 26,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.70746e+11,'m^3/(mol*s)'), n=-1.61299, w0=(293620,'J/mol'), E0=(76906.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23136605785137682, var=6.705468608317395, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 64 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.77256711723601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.77256711723601""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.77256711723601
""",
)

entry(
    index = 27,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1",
    kinetics = ArrheniusBM(A=(6.46274e-05,'m^3/(mol*s)'), n=3.37203, w0=(269156,'J/mol'), E0=(8202.03,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08975645446466793, var=2.823803455321718, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1
    Total Standard Deviation in ln(k): 3.5943109236529653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 3.5943109236529653""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 3.5943109236529653
""",
)

entry(
    index = 28,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1",
    kinetics = ArrheniusBM(A=(0.0150053,'m^3/(mol*s)'), n=2.79294, w0=(273380,'J/mol'), E0=(8599.52,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17111441500871052, var=1.1674674987261746, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1
    Total Standard Deviation in ln(k): 2.596040137982911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 2.596040137982911""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 2.596040137982911
""",
)

entry(
    index = 29,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(3.63089e-05,'m^3/(mol*s)'), n=3.645, w0=(377500,'J/mol'), E0=(46313.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09477328167133711, var=0.7668418964341546, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 56 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 1.9936604939403595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.9936604939403595""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.9936604939403595
""",
)

entry(
    index = 30,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.32676e-17,'m^3/(mol*s)'), n=7.44338, w0=(377500,'J/mol'), E0=(19760.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.32363855066638103, var=1.8319139044865154, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 3.5265353111679203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.5265353111679203""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.5265353111679203
""",
)

entry(
    index = 31,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(1.37478e-18,'m^3/(mol*s)'), n=7.566, w0=(377500,'J/mol'), E0=(5968.78,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13907657185504704, var=3.4263512300213925, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 4.060284603815113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 4.060284603815113""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 4.060284603815113
""",
)

entry(
    index = 32,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.26292e-19,'m^3/(mol*s)'), n=7.85869, w0=(377500,'J/mol'), E0=(20211.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1576409641331833, var=1.866047464358928, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 3.1346180556813854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.1346180556813854""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.1346180556813854
""",
)

entry(
    index = 33,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(82.9217,'m^3/(mol*s)'), n=1.97896, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.26468343389694526, var=0.849830612725389, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.5131240001728306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.5131240001728306""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.5131240001728306
""",
)

entry(
    index = 34,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.73126e-17,'m^3/(mol*s)'), n=6.65818, w0=(377500,'J/mol'), E0=(28867.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22026743067603313, var=1.1083751274685085, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R',), comment="""BM rule fitted to 64 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 2.664008741352372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 2.664008741352372""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 2.664008741352372
""",
)

entry(
    index = 35,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0018077,'m^3/(mol*s)'), n=2.92944, w0=(377500,'J/mol'), E0=(66574.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3849888927152672e-05, var=2.9728619478262157, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 3.4565968727046825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 3.4565968727046825""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 3.4565968727046825
""",
)

entry(
    index = 36,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.85979e-05,'m^3/(mol*s)'), n=3.67629, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.4244870208168512, var=8.649035411570846, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 9.474887110430211"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 9.474887110430211""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 9.474887110430211
""",
)

entry(
    index = 37,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(26964.2,'m^3/(mol*s)'), n=0.497401, w0=(326761,'J/mol'), E0=(79095.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1327520644782505, var=5.611915398848727, Tref=1000.0, N=115, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 115 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.082661379537618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 115 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.082661379537618""",
    longDesc = 
"""
BM rule fitted to 115 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.082661379537618
""",
)

entry(
    index = 38,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(5.47804e+11,'m^3/(mol*s)'), n=-1.31631, w0=(299500,'J/mol'), E0=(71494.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19087991795079023, var=2.8272731383793506, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O',), comment="""BM rule fitted to 50 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O
    Total Standard Deviation in ln(k): 3.8504590049363068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O
Total Standard Deviation in ln(k): 3.8504590049363068""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O
Total Standard Deviation in ln(k): 3.8504590049363068
""",
)

entry(
    index = 39,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(6.55399e+06,'m^3/(mol*s)'), n=0.0267102, w0=(322579,'J/mol'), E0=(78408.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14522166770857795, var=7.025227563283947, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O',), comment="""BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O
    Total Standard Deviation in ln(k): 5.6784581230145434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O
Total Standard Deviation in ln(k): 5.6784581230145434""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O
Total Standard Deviation in ln(k): 5.6784581230145434
""",
)

entry(
    index = 40,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.74717e+44,'m^3/(mol*s)'), n=-10.9342, w0=(316000,'J/mol'), E0=(143792,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7114557853948641, var=10.607710545647816, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 8.316895334473458"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.316895334473458""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.316895334473458
""",
)

entry(
    index = 41,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.176969,'m^3/(mol*s)'), n=1.82892, w0=(327000,'J/mol'), E0=(78683.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.180615,'m^3/(mol*s)'), n=2.22706, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5296657784779342, var=0.3625135915117447, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 2.5378515183881425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.5378515183881425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.5378515183881425
""",
)

entry(
    index = 43,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.01895e+13,'m^3/(mol*s)'), n=-2.08714, w0=(298116,'J/mol'), E0=(81443.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2606317456661369, var=5.554844714491549, Tref=1000.0, N=54, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 54 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 5.379757216681677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 54 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 5.379757216681677""",
    longDesc = 
"""
BM rule fitted to 54 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 5.379757216681677
""",
)

entry(
    index = 44,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00215987,'m^3/(mol*s)'), n=2.88286, w0=(269342,'J/mol'), E0=(24552.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.089637168765086, var=3.5529609363020307, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 4.0040042167732475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.0040042167732475""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.0040042167732475
""",
)

entry(
    index = 45,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(0.00689478,'m^3/(mol*s)'), n=2.76337, w0=(269526,'J/mol'), E0=(17664.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.026695899895133816, var=2.363589862815284, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0
    Total Standard Deviation in ln(k): 3.1491490324803997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0
Total Standard Deviation in ln(k): 3.1491490324803997""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0
Total Standard Deviation in ln(k): 3.1491490324803997
""",
)

entry(
    index = 46,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(1.57122e-17,'m^3/(mol*s)'), n=7.12288, w0=(268230,'J/mol'), E0=(-23557.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.795057843230961, var=2.476045630533532, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 10.17730038081239"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0
Total Standard Deviation in ln(k): 10.17730038081239""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0
Total Standard Deviation in ln(k): 10.17730038081239
""",
)

entry(
    index = 47,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br",
    kinetics = ArrheniusBM(A=(8949.92,'m^3/(mol*s)'), n=1.08089, w0=(245420,'J/mol'), E0=(43308,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br",
    kinetics = ArrheniusBM(A=(0.10514,'m^3/(mol*s)'), n=2.54361, w0=(276875,'J/mol'), E0=(10694.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.021569978385952957, var=0.6595272106809102, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br
    Total Standard Deviation in ln(k): 1.6822669558307568"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br
Total Standard Deviation in ln(k): 1.6822669558307568""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br
Total Standard Deviation in ln(k): 1.6822669558307568
""",
)

entry(
    index = 49,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(6.08146e-08,'m^3/(mol*s)'), n=4.47766, w0=(377500,'J/mol'), E0=(36922.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13410297587026623, var=0.8429575388571694, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 35 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 2.1775439357387993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 2.1775439357387993""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 2.1775439357387993
""",
)

entry(
    index = 50,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.2037,'m^3/(mol*s)'), n=2.1387, w0=(377500,'J/mol'), E0=(60236.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03145473163038932, var=0.6152804767056035, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 1.6515424992261136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 1.6515424992261136""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 1.6515424992261136
""",
)

entry(
    index = 51,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(6.10154e-15,'m^3/(mol*s)'), n=6.58711, w0=(377500,'J/mol'), E0=(26848.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03414571955190233, var=1.0786998487111124, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C',), comment="""BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C
    Total Standard Deviation in ln(k): 2.167920660300313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C
Total Standard Deviation in ln(k): 2.167920660300313""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C
Total Standard Deviation in ln(k): 2.167920660300313
""",
)

entry(
    index = 52,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(0.00117184,'m^3/(mol*s)'), n=3.76336, w0=(377500,'J/mol'), E0=(56536.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1459.52,'m^3/(mol*s)'), n=1.33971, w0=(377500,'J/mol'), E0=(47356.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010539352418119617, var=0.8800779872505192, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 1.907172314893019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.907172314893019""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.907172314893019
""",
)

entry(
    index = 54,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R",
    kinetics = ArrheniusBM(A=(23.5467,'m^3/(mol*s)'), n=1.8421, w0=(377500,'J/mol'), E0=(70516.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(42.4593,'m^3/(mol*s)'), n=1.81356, w0=(377500,'J/mol'), E0=(84789.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1437.58,'m^3/(mol*s)'), n=1.62878, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(686.74,'m^3/(mol*s)'), n=1.69184, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.9654e-16,'m^3/(mol*s)'), n=6.35867, w0=(377500,'J/mol'), E0=(30405.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20644068573601915, var=1.4582213847955519, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 2.9395498737373496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 2.9395498737373496""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 2.9395498737373496
""",
)

entry(
    index = 59,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.89724e-16,'m^3/(mol*s)'), n=6.48417, w0=(377500,'J/mol'), E0=(32845.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20653404277666482, var=0.9691475015065592, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 36 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 2.4924970053840427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 2.4924970053840427""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 2.4924970053840427
""",
)

entry(
    index = 60,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.00118183,'m^3/(mol*s)'), n=2.92126, w0=(377500,'J/mol'), E0=(57174.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000796126,'m^3/(mol*s)'), n=2.83903, w0=(377500,'J/mol'), E0=(59376.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.0048769,'m^3/(mol*s)'), n=3.00364, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.0011727,'m^3/(mol*s)'), n=2.96521, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.164995,'m^3/(mol*s)'), n=1.95686, w0=(327000,'J/mol'), E0=(68257.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05524205513082842, var=6.077406677218294, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl',), comment="""BM rule fitted to 50 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl
    Total Standard Deviation in ln(k): 5.080951593105803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.080951593105803""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.080951593105803
""",
)

entry(
    index = 65,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.82986e+07,'m^3/(mol*s)'), n=-0.276617, w0=(326577,'J/mol'), E0=(84987.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17148853171779782, var=5.035225132141483, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl',), comment="""BM rule fitted to 65 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.929362358467084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.929362358467084""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.929362358467084
""",
)

entry(
    index = 66,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.1218e+10,'m^3/(mol*s)'), n=-1.05135, w0=(299500,'J/mol'), E0=(68925,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17697335840291994, var=2.7163371452624165, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 3.748723529571859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.748723529571859""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.748723529571859
""",
)

entry(
    index = 67,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1",
    kinetics = ArrheniusBM(A=(0.0967719,'m^3/(mol*s)'), n=2.92787, w0=(299500,'J/mol'), E0=(28316.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(10.5404,'m^3/(mol*s)'), n=2.14943, w0=(299500,'J/mol'), E0=(69107.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F",
    kinetics = ArrheniusBM(A=(1430.74,'m^3/(mol*s)'), n=1.46983, w0=(288770,'J/mol'), E0=(23196.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F",
    kinetics = ArrheniusBM(A=(1.40468e+07,'m^3/(mol*s)'), n=-0.0771526, w0=(323298,'J/mol'), E0=(80202.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15228200046856405, var=5.619877508276971, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F',), comment="""BM rule fitted to 47 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F
    Total Standard Deviation in ln(k): 5.1350993652311745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F
Total Standard Deviation in ln(k): 5.1350993652311745""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F
Total Standard Deviation in ln(k): 5.1350993652311745
""",
)

entry(
    index = 71,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.09006e+21,'m^3/(mol*s)'), n=-4.10814, w0=(327000,'J/mol'), E0=(106777,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.39843966580876133, var=8.026128845913885, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 6.680604023483769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.680604023483769""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.680604023483769
""",
)

entry(
    index = 72,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.78113e+14,'m^3/(mol*s)'), n=-2.10909, w0=(299500,'J/mol'), E0=(7592.47,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6747394411670511, var=18.21361337277451, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 10.251015343457274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 10.251015343457274""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 10.251015343457274
""",
)

entry(
    index = 73,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.01606,'m^3/(mol*s)'), n=2.58252, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(5.81832,'m^3/(mol*s)'), n=1.87825, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(102962,'m^3/(mol*s)'), n=0.387056, w0=(296732,'J/mol'), E0=(57291.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14167952907987863, var=2.9986685059745675, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0',), comment="""BM rule fitted to 27 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0
    Total Standard Deviation in ln(k): 3.8275110820727924"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0
Total Standard Deviation in ln(k): 3.8275110820727924""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0
Total Standard Deviation in ln(k): 3.8275110820727924
""",
)

entry(
    index = 76,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(3.16054e+12,'m^3/(mol*s)'), n=-2.05419, w0=(299500,'J/mol'), E0=(85707.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23301877320014874, var=4.46252865739887, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0',), comment="""BM rule fitted to 27 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 4.820416613224259"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 4.820416613224259""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 4.820416613224259
""",
)

entry(
    index = 77,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.00169657,'m^3/(mol*s)'), n=3.02018, w0=(272000,'J/mol'), E0=(15214.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008044831746981432, var=2.107299637979286, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.930395047845308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.930395047845308""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.930395047845308
""",
)

entry(
    index = 78,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C",
    kinetics = ArrheniusBM(A=(15.7503,'m^3/(mol*s)'), n=1.49986, w0=(272000,'J/mol'), E0=(32952.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15082079723906588, var=0.10949075809424502, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C
    Total Standard Deviation in ln(k): 1.0423012896301798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C
Total Standard Deviation in ln(k): 1.0423012896301798""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C
Total Standard Deviation in ln(k): 1.0423012896301798
""",
)

entry(
    index = 79,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.62829e-06,'m^3/(mol*s)'), n=3.6289, w0=(263140,'J/mol'), E0=(3104.65,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06405698985694609, var=1.2498944744388731, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.4022145552736376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C
Total Standard Deviation in ln(k): 2.4022145552736376""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C
Total Standard Deviation in ln(k): 2.4022145552736376
""",
)

entry(
    index = 80,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000600926,'m^3/(mol*s)'), n=3.23718, w0=(299500,'J/mol'), E0=(9179.27,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3123315256373949, var=8.00254642399521, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 6.455902004335112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.455902004335112""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.455902004335112
""",
)

entry(
    index = 81,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00225141,'m^3/(mol*s)'), n=2.86789, w0=(262032,'J/mol'), E0=(14124.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06110218493841438, var=2.3996353664799237, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 3.2590093689224884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.2590093689224884""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.2590093689224884
""",
)

entry(
    index = 82,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.3609e+06,'m^3/(mol*s)'), n=0.498188, w0=(245420,'J/mol'), E0=(45386.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(2.05451e-06,'m^3/(mol*s)'), n=3.77469, w0=(275833,'J/mol'), E0=(-16777.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9077434363744121, var=3.9247362195243802, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br
    Total Standard Deviation in ln(k): 8.76489525838352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br
Total Standard Deviation in ln(k): 8.76489525838352""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br
Total Standard Deviation in ln(k): 8.76489525838352
""",
)

entry(
    index = 84,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0",
    kinetics = ArrheniusBM(A=(0.20598,'m^3/(mol*s)'), n=2.46326, w0=(273643,'J/mol'), E0=(11830.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009474708677514798, var=0.8190969158363606, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0
    Total Standard Deviation in ln(k): 1.838170697139568"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0
Total Standard Deviation in ln(k): 1.838170697139568""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0
Total Standard Deviation in ln(k): 1.838170697139568
""",
)

entry(
    index = 85,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0",
    kinetics = ArrheniusBM(A=(49.4221,'m^3/(mol*s)'), n=1.71189, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.17049e-08,'m^3/(mol*s)'), n=4.55762, w0=(377500,'J/mol'), E0=(34223.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13426658503067163, var=0.9006342995840816, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 26 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.2398819890467667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.2398819890467667""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.2398819890467667
""",
)

entry(
    index = 87,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.23199e-06,'m^3/(mol*s)'), n=3.99061, w0=(377500,'J/mol'), E0=(45751.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03897143226106023, var=1.1629123330457478, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.2597926649509614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.2597926649509614""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.2597926649509614
""",
)

entry(
    index = 88,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl",
    kinetics = ArrheniusBM(A=(0.362172,'m^3/(mol*s)'), n=2.4567, w0=(377500,'J/mol'), E0=(55239.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.062007753513043135, var=0.7061173955954871, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl
    Total Standard Deviation in ln(k): 1.8403931329483507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl
Total Standard Deviation in ln(k): 1.8403931329483507""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl
Total Standard Deviation in ln(k): 1.8403931329483507
""",
)

entry(
    index = 89,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl",
    kinetics = ArrheniusBM(A=(0.0894054,'m^3/(mol*s)'), n=2.63193, w0=(377500,'J/mol'), E0=(60991.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.035294545988984176, var=0.18430096202496207, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl
    Total Standard Deviation in ln(k): 0.949318304399477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl
Total Standard Deviation in ln(k): 0.949318304399477""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl
Total Standard Deviation in ln(k): 0.949318304399477
""",
)

entry(
    index = 90,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C",
    kinetics = ArrheniusBM(A=(5.38121e-15,'m^3/(mol*s)'), n=6.61062, w0=(377500,'J/mol'), E0=(27035.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16653125687949763, var=2.0935374493929637, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C
    Total Standard Deviation in ln(k): 3.3190837854503874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C
Total Standard Deviation in ln(k): 3.3190837854503874""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C
Total Standard Deviation in ln(k): 3.3190837854503874
""",
)

entry(
    index = 91,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(24.0657,'m^3/(mol*s)'), n=1.94769, w0=(377500,'J/mol'), E0=(68769.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(36.3215,'m^3/(mol*s)'), n=1.83646, w0=(377500,'J/mol'), E0=(51038.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(882.183,'m^3/(mol*s)'), n=1.42825, w0=(377500,'J/mol'), E0=(45417.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0022107214661341293, var=0.2475890620304536, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 1.0030771140320058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.0030771140320058""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.0030771140320058
""",
)

entry(
    index = 94,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.29342e-16,'m^3/(mol*s)'), n=6.39365, w0=(377500,'J/mol'), E0=(29982.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2040904284946623, var=1.3569998914609664, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 27 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 2.848112694791506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 2.848112694791506""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 2.848112694791506
""",
)

entry(
    index = 95,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.68513e-12,'m^3/(mol*s)'), n=5.34811, w0=(377500,'J/mol'), E0=(42714.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18210347168275715, var=1.0777946785520311, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 2.5388000345078594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.5388000345078594""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.5388000345078594
""",
)

entry(
    index = 96,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(7.95839e-19,'m^3/(mol*s)'), n=7.27706, w0=(377500,'J/mol'), E0=(28584.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014470819766070014, var=2.0514931400152165, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 2.9077477883199156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.9077477883199156""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.9077477883199156
""",
)

entry(
    index = 97,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.00155005,'m^3/(mol*s)'), n=2.60838, w0=(327000,'J/mol'), E0=(63941.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02130050241462552, var=4.8187694607096745, Tref=1000.0, N=43, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 43 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 4.454252297070465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 43 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.454252297070465""",
    longDesc = 
"""
BM rule fitted to 43 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.454252297070465
""",
)

entry(
    index = 98,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(11366,'m^3/(mol*s)'), n=0.145241, w0=(327000,'J/mol'), E0=(77335.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10568852141797813, var=14.04571793145985, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 7.778818436354915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 7.778818436354915""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 7.778818436354915
""",
)

entry(
    index = 99,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1",
    kinetics = ArrheniusBM(A=(158296,'m^3/(mol*s)'), n=0.299108, w0=(326549,'J/mol'), E0=(80466.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13742808095739545, var=4.531928063925258, Tref=1000.0, N=61, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1',), comment="""BM rule fitted to 61 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1
    Total Standard Deviation in ln(k): 4.613041990591716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 61 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 4.613041990591716""",
    longDesc = 
"""
BM rule fitted to 61 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 4.613041990591716
""",
)

entry(
    index = 100,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1",
    kinetics = ArrheniusBM(A=(7.72355e+07,'m^3/(mol*s)'), n=0.0549246, w0=(327000,'J/mol'), E0=(90315.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6566357587282334, var=13.644551177166184, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1
    Total Standard Deviation in ln(k): 9.055035592949093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 9.055035592949093""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 9.055035592949093
""",
)

entry(
    index = 101,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(4.57625e+12,'m^3/(mol*s)'), n=-1.60312, w0=(299500,'J/mol'), E0=(71132.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2045060816374969, var=2.819725251632908, Tref=1000.0, N=33, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 33 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 3.8801930462076024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 3.8801930462076024""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 3.8801930462076024
""",
)

entry(
    index = 102,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.91777e+11,'m^3/(mol*s)'), n=-1.19931, w0=(299500,'J/mol'), E0=(74560.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19252184508705078, var=2.549175684987757, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 15 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 3.6845109555864783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.6845109555864783""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.6845109555864783
""",
)

entry(
    index = 103,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.09997e+07,'m^3/(mol*s)'), n=-0.130793, w0=(323217,'J/mol'), E0=(80305.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15584943350954938, var=5.737456907322806, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R',), comment="""BM rule fitted to 46 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R
    Total Standard Deviation in ln(k): 5.193521253303043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.193521253303043""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.193521253303043
""",
)

entry(
    index = 104,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.13946e+21,'m^3/(mol*s)'), n=-4.04791, w0=(327000,'J/mol'), E0=(106860,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3748916911876865, var=10.618664007825155, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 7.4746271055215985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.4746271055215985""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.4746271055215985
""",
)

entry(
    index = 105,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(0.171123,'m^3/(mol*s)'), n=2.55484, w0=(327000,'J/mol'), E0=(52803.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(157.231,'m^3/(mol*s)'), n=1.7152, w0=(299500,'J/mol'), E0=(57523.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.977703,'m^3/(mol*s)'), n=2.24188, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(3.76314e+12,'m^3/(mol*s)'), n=-1.56684, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0942170328911507, var=3.7511290089229687, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 9.14458897962611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 9.14458897962611""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 9.14458897962611
""",
)

entry(
    index = 109,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.22348e+08,'m^3/(mol*s)'), n=-0.663436, w0=(297500,'J/mol'), E0=(71021.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20468923608628456, var=1.5187761375918958, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.984902725610864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.984902725610864""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.984902725610864
""",
)

entry(
    index = 110,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(8.52327,'m^3/(mol*s)'), n=1.81506, w0=(295500,'J/mol'), E0=(47285.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.346965268982822, var=2.6002591973091786, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 4.10447133872876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C
Total Standard Deviation in ln(k): 4.10447133872876""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C
Total Standard Deviation in ln(k): 4.10447133872876
""",
)

entry(
    index = 111,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(2.91651e-05,'m^3/(mol*s)'), n=3.20275, w0=(296651,'J/mol'), E0=(23652,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002365370392681771, var=1.9396360165083455, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C',), comment="""BM rule fitted to 15 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.7979540408718493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.7979540408718493""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.7979540408718493
""",
)

entry(
    index = 112,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1",
    kinetics = ArrheniusBM(A=(1.04412e+08,'m^3/(mol*s)'), n=-0.752047, w0=(299500,'J/mol'), E0=(76346.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16488944306323813, var=3.68839335434195, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1',), comment="""BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1
    Total Standard Deviation in ln(k): 4.264426954406092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1
Total Standard Deviation in ln(k): 4.264426954406092""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1
Total Standard Deviation in ln(k): 4.264426954406092
""",
)

entry(
    index = 113,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1",
    kinetics = ArrheniusBM(A=(0.254715,'m^3/(mol*s)'), n=2.28881, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(7929.14,'m^3/(mol*s)'), n=1.02276, w0=(272000,'J/mol'), E0=(29393.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7335912828451596, var=5.7724248067406805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 9.17230764197859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 9.17230764197859""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 9.17230764197859
""",
)

entry(
    index = 115,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.00015294,'m^3/(mol*s)'), n=3.32595, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06385783340243101, var=3.9122969846358115, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 4.125718027994882"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 4.125718027994882""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 4.125718027994882
""",
)

entry(
    index = 116,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(0.0129879,'m^3/(mol*s)'), n=2.36842, w0=(272000,'J/mol'), E0=(24049.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(785.274,'m^3/(mol*s)'), n=1.03345, w0=(272000,'J/mol'), E0=(38997.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O",
    kinetics = ArrheniusBM(A=(1.358e-06,'m^3/(mol*s)'), n=3.83886, w0=(258710,'J/mol'), E0=(799.149,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16790098169506443, var=2.3964144310069533, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O
    Total Standard Deviation in ln(k): 3.525263168790169"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O
Total Standard Deviation in ln(k): 3.525263168790169""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O
Total Standard Deviation in ln(k): 3.525263168790169
""",
)

entry(
    index = 119,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O",
    kinetics = ArrheniusBM(A=(0.00123036,'m^3/(mol*s)'), n=2.89569, w0=(272000,'J/mol'), E0=(19743.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R",
    kinetics = ArrheniusBM(A=(0.00549393,'m^3/(mol*s)'), n=2.84052, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R",
    kinetics = ArrheniusBM(A=(0.0749143,'m^3/(mol*s)'), n=2.36147, w0=(267570,'J/mol'), E0=(19648.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12838896908857245, var=2.7880004364418514, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R
    Total Standard Deviation in ln(k): 3.6699529490570875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 3.6699529490570875""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 3.6699529490570875
""",
)

entry(
    index = 122,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O",
    kinetics = ArrheniusBM(A=(49.219,'m^3/(mol*s)'), n=1.86416, w0=(245420,'J/mol'), E0=(27617.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(8.50529,'m^3/(mol*s)'), n=1.86514, w0=(245420,'J/mol'), E0=(27755,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl",
    kinetics = ArrheniusBM(A=(1.50923e+06,'m^3/(mol*s)'), n=0.331641, w0=(256000,'J/mol'), E0=(25641.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl",
    kinetics = ArrheniusBM(A=(2.22531e-08,'m^3/(mol*s)'), n=4.32748, w0=(285750,'J/mol'), E0=(-13432,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0120234484097612, var=64.58445550449544, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl
    Total Standard Deviation in ln(k): 18.653716578820646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl
Total Standard Deviation in ln(k): 18.653716578820646""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl
Total Standard Deviation in ln(k): 18.653716578820646
""",
)

entry(
    index = 126,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00519164,'m^3/(mol*s)'), n=2.99789, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.13258,'m^3/(mol*s)'), n=2.50951, w0=(269333,'J/mol'), E0=(10681.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014549359240975385, var=0.8605148669014032, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 1.8962274346626746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.8962274346626746""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.8962274346626746
""",
)

entry(
    index = 128,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.08791e-08,'m^3/(mol*s)'), n=4.63911, w0=(377500,'J/mol'), E0=(28191.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14352225001220972, var=0.7983393514729089, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 15 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.1518362083261118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.1518362083261118""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.1518362083261118
""",
)

entry(
    index = 129,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(62588.4,'m^3/(mol*s)'), n=0.861102, w0=(377500,'J/mol'), E0=(71956.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05529491621869825, var=1.635329736913831, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 2.7025874000011445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 2.7025874000011445""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 2.7025874000011445
""",
)

entry(
    index = 130,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.14537e-12,'m^3/(mol*s)'), n=5.89691, w0=(377500,'J/mol'), E0=(24322.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03693105844281619, var=0.8178012519049005, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 1.9057209332495346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.9057209332495346""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.9057209332495346
""",
)

entry(
    index = 131,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.65086e-08,'m^3/(mol*s)'), n=4.44563, w0=(377500,'J/mol'), E0=(45296.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.032846077257453574, var=2.733305672521222, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 3.3968986065278073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 3.3968986065278073""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 3.3968986065278073
""",
)

entry(
    index = 132,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(506.9,'m^3/(mol*s)'), n=1.55272, w0=(377500,'J/mol'), E0=(62096.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02095073137499071, var=0.42805599807247446, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 1.3642577712306554"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.3642577712306554""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.3642577712306554
""",
)

entry(
    index = 133,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.599359,'m^3/(mol*s)'), n=2.39082, w0=(377500,'J/mol'), E0=(55318.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.058251253632978596, var=0.744302654197764, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R',), comment="""BM rule fitted to 13 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 1.8759045638370222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 1.8759045638370222""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 1.8759045638370222
""",
)

entry(
    index = 134,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O",
    kinetics = ArrheniusBM(A=(28.207,'m^3/(mol*s)'), n=1.91432, w0=(377500,'J/mol'), E0=(63639.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O",
    kinetics = ArrheniusBM(A=(0.0235816,'m^3/(mol*s)'), n=2.80751, w0=(377500,'J/mol'), E0=(60694.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04471268766163932, var=0.1501725916524168, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O',), comment="""BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O
    Total Standard Deviation in ln(k): 0.8892205495260386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O
Total Standard Deviation in ln(k): 0.8892205495260386""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O
Total Standard Deviation in ln(k): 0.8892205495260386
""",
)

entry(
    index = 136,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(23993.5,'m^3/(mol*s)'), n=0.953042, w0=(377500,'J/mol'), E0=(67258.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(4.07503e-16,'m^3/(mol*s)'), n=6.9826, w0=(377500,'J/mol'), E0=(24677,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.28774936454598665, var=2.4496801164788433, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 3.8606902334659385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F
Total Standard Deviation in ln(k): 3.8606902334659385""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F
Total Standard Deviation in ln(k): 3.8606902334659385
""",
)

entry(
    index = 138,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(34.0466,'m^3/(mol*s)'), n=1.832, w0=(377500,'J/mol'), E0=(40068.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(82.3604,'m^3/(mol*s)'), n=1.89796, w0=(377500,'J/mol'), E0=(54231.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.80088e-15,'m^3/(mol*s)'), n=6.00109, w0=(377500,'J/mol'), E0=(12231.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18710233001578955, var=2.456532139297762, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.612193420257354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.612193420257354""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.612193420257354
""",
)

entry(
    index = 141,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(5.27282e-12,'m^3/(mol*s)'), n=5.16746, w0=(377500,'J/mol'), E0=(44216.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.154996717640678, var=0.937074636375146, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.330074977407665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.330074977407665""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.330074977407665
""",
)

entry(
    index = 142,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000188534,'m^3/(mol*s)'), n=2.90765, w0=(377500,'J/mol'), E0=(62604.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.019625222809309492, var=0.9359553608847592, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 1.988786264572879"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 1.988786264572879""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 1.988786264572879
""",
)

entry(
    index = 143,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.00140232,'m^3/(mol*s)'), n=2.68536, w0=(377500,'J/mol'), E0=(73853.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0016955639991539163, var=3.276663888684693, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 3.633142965994664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 3.633142965994664""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 3.633142965994664
""",
)

entry(
    index = 144,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(8.82597e-06,'m^3/(mol*s)'), n=3.4053, w0=(377500,'J/mol'), E0=(56937.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04621996279228595, var=0.5914972600738666, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 1.6579494348262642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 1.6579494348262642""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 1.6579494348262642
""",
)

entry(
    index = 145,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C",
    kinetics = ArrheniusBM(A=(6.76422e-18,'m^3/(mol*s)'), n=6.97124, w0=(377500,'J/mol'), E0=(31252.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03821160552119061, var=1.8042965246585392, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C
    Total Standard Deviation in ln(k): 2.788851514095702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C
Total Standard Deviation in ln(k): 2.788851514095702""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C
Total Standard Deviation in ln(k): 2.788851514095702
""",
)

entry(
    index = 146,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C",
    kinetics = ArrheniusBM(A=(9.64471e-05,'m^3/(mol*s)'), n=3.30977, w0=(377500,'J/mol'), E0=(57127.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(225.294,'m^3/(mol*s)'), n=0.984493, w0=(327000,'J/mol'), E0=(72587.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10683682977877071, var=4.932969478713925, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl',), comment="""BM rule fitted to 23 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl
    Total Standard Deviation in ln(k): 4.721008836382942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.721008836382942""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.721008836382942
""",
)

entry(
    index = 148,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.21685e-06,'m^3/(mol*s)'), n=3.63851, w0=(327000,'J/mol'), E0=(60102.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02931979013159395, var=4.9212850471294995, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl',), comment="""BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.520966004397923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.520966004397923""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.520966004397923
""",
)

entry(
    index = 149,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.00138208,'m^3/(mol*s)'), n=2.70635, w0=(327000,'J/mol'), E0=(62525.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(955216,'m^3/(mol*s)'), n=-0.519537, w0=(327000,'J/mol'), E0=(81900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1068663824620386, var=13.114399306410846, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 7.528417729886166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.528417729886166""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.528417729886166
""",
)

entry(
    index = 151,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(11908.1,'m^3/(mol*s)'), n=0.612248, w0=(326500,'J/mol'), E0=(78006.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12073699036529997, var=4.590655837923661, Tref=1000.0, N=55, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 55 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.598667727010517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 55 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.598667727010517""",
    longDesc = 
"""
BM rule fitted to 55 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.598667727010517
""",
)

entry(
    index = 152,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1778,'m^3/(mol*s)'), n=1.04811, w0=(327000,'J/mol'), E0=(77596.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04989109265909885, var=5.419035808554763, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.792141723446247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.792141723446247""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.792141723446247
""",
)

entry(
    index = 153,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(3.31301e-26,'m^3/(mol*s)'), n=9.87585, w0=(327000,'J/mol'), E0=(4804.69,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6170013636793144, var=6.63688849715294, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 6.7148851163181495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 6.7148851163181495""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 6.7148851163181495
""",
)

entry(
    index = 154,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(0.000854975,'m^3/(mol*s)'), n=3.28947, w0=(327000,'J/mol'), E0=(42838.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.50197e+13,'m^3/(mol*s)'), n=-1.7517, w0=(299500,'J/mol'), E0=(71104.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21158097278730756, var=3.148410572845195, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.088764508703126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.088764508703126""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.088764508703126
""",
)

entry(
    index = 156,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.92516e+16,'m^3/(mol*s)'), n=-2.7478, w0=(299500,'J/mol'), E0=(82217.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23030987885994278, var=3.794273718383914, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 4.483670555086223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.483670555086223""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.483670555086223
""",
)

entry(
    index = 157,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.16794e+13,'m^3/(mol*s)'), n=-1.84136, w0=(299500,'J/mol'), E0=(74982.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24175774598428448, var=3.7513412400848316, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.490278497850596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.490278497850596""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.490278497850596
""",
)

entry(
    index = 158,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(9.29659e+14,'m^3/(mol*s)'), n=-2.23186, w0=(299500,'J/mol'), E0=(91582.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24576098008118513, var=4.236790672619611, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 4.743929504292122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.743929504292122""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.743929504292122
""",
)

entry(
    index = 159,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(9.66016e+10,'m^3/(mol*s)'), n=-1.13183, w0=(299500,'J/mol'), E0=(70783.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1896173367810115, var=2.6657469376783642, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 3.7495795432108716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 3.7495795432108716""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 3.7495795432108716
""",
)

entry(
    index = 160,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(6162.87,'m^3/(mol*s)'), n=0.894691, w0=(321780,'J/mol'), E0=(69243.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09812047308308564, var=7.638979571269701, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 5.787361786152755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.787361786152755""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.787361786152755
""",
)

entry(
    index = 161,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(6.10749e+09,'m^3/(mol*s)'), n=-0.836214, w0=(324929,'J/mol'), E0=(89820.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18669856338787943, var=4.153296183747187, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.554669253118066"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.554669253118066""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.554669253118066
""",
)

entry(
    index = 162,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O",
    kinetics = ArrheniusBM(A=(1.39543e+19,'m^3/(mol*s)'), n=-3.47206, w0=(327000,'J/mol'), E0=(91807.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5352246413685504, var=11.15051032067538, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O
    Total Standard Deviation in ln(k): 8.03907305143576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 8.03907305143576""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 8.03907305143576
""",
)

entry(
    index = 163,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O",
    kinetics = ArrheniusBM(A=(86.872,'m^3/(mol*s)'), n=1.58191, w0=(327000,'J/mol'), E0=(83090.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.019437028169395205, var=22.281750390558173, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O
    Total Standard Deviation in ln(k): 9.511897801800835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 9.511897801800835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 9.511897801800835
""",
)

entry(
    index = 164,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(52.7701,'m^3/(mol*s)'), n=1.64048, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O",
    kinetics = ArrheniusBM(A=(2.06632e+07,'m^3/(mol*s)'), n=-0.380265, w0=(299500,'J/mol'), E0=(71598.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2038967053365674, var=1.6431026281693228, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O
    Total Standard Deviation in ln(k): 3.082044166494217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O
Total Standard Deviation in ln(k): 3.082044166494217""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O
Total Standard Deviation in ln(k): 3.082044166494217
""",
)

entry(
    index = 166,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(0.0786025,'m^3/(mol*s)'), n=1.58787, w0=(283500,'J/mol'), E0=(30657.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O",
    kinetics = ArrheniusBM(A=(498.909,'m^3/(mol*s)'), n=1.25837, w0=(299500,'J/mol'), E0=(54948.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18359167328198975, var=0.32157756714061736, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O
    Total Standard Deviation in ln(k): 1.5981269622483416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O
Total Standard Deviation in ln(k): 1.5981269622483416""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O
Total Standard Deviation in ln(k): 1.5981269622483416
""",
)

entry(
    index = 168,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(0.0708355,'m^3/(mol*s)'), n=2.5177, w0=(283500,'J/mol'), E0=(25332.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl",
    kinetics = ArrheniusBM(A=(1.37533e+14,'m^3/(mol*s)'), n=-2.36761, w0=(283500,'J/mol'), E0=(61837,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.036605612162127724, var=35.529751535247414, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl
    Total Standard Deviation in ln(k): 12.041565827887531"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl
Total Standard Deviation in ln(k): 12.041565827887531""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl
Total Standard Deviation in ln(k): 12.041565827887531
""",
)

entry(
    index = 170,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl",
    kinetics = ArrheniusBM(A=(6.6918e-06,'m^3/(mol*s)'), n=3.40293, w0=(298675,'J/mol'), E0=(22007.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07302722741032097, var=1.423866257990027, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl
    Total Standard Deviation in ln(k): 2.5756530119058967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl
Total Standard Deviation in ln(k): 2.5756530119058967""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl
Total Standard Deviation in ln(k): 2.5756530119058967
""",
)

entry(
    index = 171,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl",
    kinetics = ArrheniusBM(A=(722872,'m^3/(mol*s)'), n=-0.145075, w0=(299500,'J/mol'), E0=(71773,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12874496568226584, var=4.560970750031809, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl
    Total Standard Deviation in ln(k): 4.604878119834457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl
Total Standard Deviation in ln(k): 4.604878119834457""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl
Total Standard Deviation in ln(k): 4.604878119834457
""",
)

entry(
    index = 172,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.41344e+07,'m^3/(mol*s)'), n=-0.438974, w0=(299500,'J/mol'), E0=(74269.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14739842763176467, var=2.98421779433991, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl
    Total Standard Deviation in ln(k): 3.8335053406688644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.8335053406688644""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.8335053406688644
""",
)

entry(
    index = 173,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(1.22259e-06,'m^3/(mol*s)'), n=3.71504, w0=(272000,'J/mol'), E0=(9138.78,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(0.116915,'m^3/(mol*s)'), n=2.38628, w0=(272000,'J/mol'), E0=(16092.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(0.0844782,'m^3/(mol*s)'), n=2.28559, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(0.0214236,'m^3/(mol*s)'), n=2.72353, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7890304190583937, var=1.5320421056336533, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 4.463863134149878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 4.463863134149878""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 4.463863134149878
""",
)

entry(
    index = 177,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O",
    kinetics = ArrheniusBM(A=(2.78249e-05,'m^3/(mol*s)'), n=3.31769, w0=(272000,'J/mol'), E0=(24287.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(0.0133585,'m^3/(mol*s)'), n=2.57468, w0=(245420,'J/mol'), E0=(20506.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O",
    kinetics = ArrheniusBM(A=(0.0254004,'m^3/(mol*s)'), n=2.46704, w0=(272000,'J/mol'), E0=(16643.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09081708548127386, var=3.0497208798012556, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O
    Total Standard Deviation in ln(k): 3.729142722519516"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O
Total Standard Deviation in ln(k): 3.729142722519516""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O
Total Standard Deviation in ln(k): 3.729142722519516
""",
)

entry(
    index = 180,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O",
    kinetics = ArrheniusBM(A=(80.5994,'m^3/(mol*s)'), n=1.63822, w0=(245420,'J/mol'), E0=(36490,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C",
    kinetics = ArrheniusBM(A=(90.1146,'m^3/(mol*s)'), n=1.48177, w0=(299500,'J/mol'), E0=(72259.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C",
    kinetics = ArrheniusBM(A=(3523.39,'m^3/(mol*s)'), n=0.999173, w0=(272000,'J/mol'), E0=(16637.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O",
    kinetics = ArrheniusBM(A=(0.114153,'m^3/(mol*s)'), n=2.53269, w0=(272000,'J/mol'), E0=(7320.03,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2602400411964976, var=1.2590481146524588, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O
    Total Standard Deviation in ln(k): 2.903328818343582"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O
Total Standard Deviation in ln(k): 2.903328818343582""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O
Total Standard Deviation in ln(k): 2.903328818343582
""",
)

entry(
    index = 184,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O",
    kinetics = ArrheniusBM(A=(8060.2,'m^3/(mol*s)'), n=1.07817, w0=(256000,'J/mol'), E0=(22060.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.91146e+06,'m^3/(mol*s)'), n=0.268206, w0=(377500,'J/mol'), E0=(59785.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06898561852044642, var=2.262328549630402, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.188660553263694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.188660553263694""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.188660553263694
""",
)

entry(
    index = 186,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(2.03826,'m^3/(mol*s)'), n=2.22329, w0=(377500,'J/mol'), E0=(53462,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002975362359582955, var=0.13126976798935627, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 0.7338147588531938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 0.7338147588531938""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 0.7338147588531938
""",
)

entry(
    index = 187,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5.75771e-09,'m^3/(mol*s)'), n=4.79859, w0=(377500,'J/mol'), E0=(15032.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20565025331844292, var=0.6459667027964928, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 2.1279559336357616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.1279559336357616""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.1279559336357616
""",
)

entry(
    index = 188,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.66274e+06,'m^3/(mol*s)'), n=0.31572, w0=(377500,'J/mol'), E0=(77041.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08306616507898022, var=1.742178091348737, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R
    Total Standard Deviation in ln(k): 2.85479074365178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 2.85479074365178""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 2.85479074365178
""",
)

entry(
    index = 189,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C",
    kinetics = ArrheniusBM(A=(1.26212e-13,'m^3/(mol*s)'), n=6.2072, w0=(377500,'J/mol'), E0=(21815,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12122725566309941, var=1.5688041731621998, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C
    Total Standard Deviation in ln(k): 2.815560131366684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C
Total Standard Deviation in ln(k): 2.815560131366684""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C
Total Standard Deviation in ln(k): 2.815560131366684
""",
)

entry(
    index = 190,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C",
    kinetics = ArrheniusBM(A=(3.70472e-07,'m^3/(mol*s)'), n=4.24843, w0=(377500,'J/mol'), E0=(39295.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013333098236407387, var=1.1198824346926088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C
    Total Standard Deviation in ln(k): 2.1550010758633493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C
Total Standard Deviation in ln(k): 2.1550010758633493""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C
Total Standard Deviation in ln(k): 2.1550010758633493
""",
)

entry(
    index = 191,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(0.000841691,'m^3/(mol*s)'), n=3.26914, w0=(377500,'J/mol'), E0=(54177.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11311278676282382, var=4.206300468817086, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C
    Total Standard Deviation in ln(k): 4.395767746915374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C
Total Standard Deviation in ln(k): 4.395767746915374""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C
Total Standard Deviation in ln(k): 4.395767746915374
""",
)

entry(
    index = 192,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(43.2043,'m^3/(mol*s)'), n=1.91844, w0=(377500,'J/mol'), E0=(75232.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(263.628,'m^3/(mol*s)'), n=1.64143, w0=(377500,'J/mol'), E0=(58677.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0013066185853155743, var=0.9337790332488703, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.9405034270870185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.9405034270870185""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.9405034270870185
""",
)

entry(
    index = 194,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(21.2149,'m^3/(mol*s)'), n=2.00716, w0=(377500,'J/mol'), E0=(66917.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(28.5031,'m^3/(mol*s)'), n=1.97907, w0=(377500,'J/mol'), E0=(63968.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(52708.5,'m^3/(mol*s)'), n=0.95248, w0=(377500,'J/mol'), E0=(66974.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0033010312613124095, var=0.22987552446591225, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 0.969471017267569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.969471017267569""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.969471017267569
""",
)

entry(
    index = 197,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.34934e-08,'m^3/(mol*s)'), n=4.65812, w0=(377500,'J/mol'), E0=(36636,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13463534192978543, var=0.7884190010629424, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.1183433988919913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.1183433988919913""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.1183433988919913
""",
)

entry(
    index = 198,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br",
    kinetics = ArrheniusBM(A=(48.3102,'m^3/(mol*s)'), n=1.84106, w0=(377500,'J/mol'), E0=(72219.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00045951926176135454, var=0.26341720991250145, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br
    Total Standard Deviation in ln(k): 1.030068536907337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br
Total Standard Deviation in ln(k): 1.030068536907337""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br
Total Standard Deviation in ln(k): 1.030068536907337
""",
)

entry(
    index = 199,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br",
    kinetics = ArrheniusBM(A=(17.156,'m^3/(mol*s)'), n=1.95116, w0=(377500,'J/mol'), E0=(65289.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.47473131806419e-05, var=0.1214838260736045, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br
    Total Standard Deviation in ln(k): 0.6989287960646976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br
Total Standard Deviation in ln(k): 0.6989287960646976""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br
Total Standard Deviation in ln(k): 0.6989287960646976
""",
)

entry(
    index = 200,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C",
    kinetics = ArrheniusBM(A=(144.067,'m^3/(mol*s)'), n=1.76784, w0=(377500,'J/mol'), E0=(61265,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0038281147633589816, var=0.9019768259174188, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C
    Total Standard Deviation in ln(k): 1.9135646089170832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C
Total Standard Deviation in ln(k): 1.9135646089170832""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C
Total Standard Deviation in ln(k): 1.9135646089170832
""",
)

entry(
    index = 201,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C",
    kinetics = ArrheniusBM(A=(30.5257,'m^3/(mol*s)'), n=2.04125, w0=(377500,'J/mol'), E0=(93315.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.64137e-15,'m^3/(mol*s)'), n=6.03979, w0=(377500,'J/mol'), E0=(17534.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21245567989005293, var=2.8789278987654576, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 3.9353231871021883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 3.9353231871021883""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 3.9353231871021883
""",
)

entry(
    index = 203,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(0.000702801,'m^3/(mol*s)'), n=2.76707, w0=(377500,'J/mol'), E0=(67149.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006329136195630499, var=1.3909593248943513, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 2.380265625192914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.380265625192914""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.380265625192914
""",
)

entry(
    index = 204,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(8.95214e-11,'m^3/(mol*s)'), n=4.7684, w0=(377500,'J/mol'), E0=(43316.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03628723582529306, var=0.2864713349387636, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 1.1641686557520263"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 1.1641686557520263""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 1.1641686557520263
""",
)

entry(
    index = 205,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi",
    kinetics = ArrheniusBM(A=(2.86532e-08,'m^3/(mol*s)'), n=4.0304, w0=(377500,'J/mol'), E0=(53408.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06459010161268612, var=0.9300844695170757, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
    Total Standard Deviation in ln(k): 2.095670979129165"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 2.095670979129165""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 2.095670979129165
""",
)

entry(
    index = 206,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi",
    kinetics = ArrheniusBM(A=(1.68075,'m^3/(mol*s)'), n=1.83046, w0=(377500,'J/mol'), E0=(72496.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000500117,'m^3/(mol*s)'), n=2.74152, w0=(377500,'J/mol'), E0=(61169.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F",
    kinetics = ArrheniusBM(A=(0.00112937,'m^3/(mol*s)'), n=2.75893, w0=(377500,'J/mol'), E0=(66188.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009004570774582756, var=0.08073191876992687, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F
    Total Standard Deviation in ln(k): 0.5922372011427575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F
Total Standard Deviation in ln(k): 0.5922372011427575""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F
Total Standard Deviation in ln(k): 0.5922372011427575
""",
)

entry(
    index = 209,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F",
    kinetics = ArrheniusBM(A=(0.000324127,'m^3/(mol*s)'), n=2.95636, w0=(377500,'J/mol'), E0=(57206.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0006490855268967592, var=0.448105693627869, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F
    Total Standard Deviation in ln(k): 1.3436145051785067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F
Total Standard Deviation in ln(k): 1.3436145051785067""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F
Total Standard Deviation in ln(k): 1.3436145051785067
""",
)

entry(
    index = 210,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(8.41249e-19,'m^3/(mol*s)'), n=7.2254, w0=(377500,'J/mol'), E0=(29201.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13099921464636163, var=1.8442944898792286, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.0516703060356147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.0516703060356147""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.0516703060356147
""",
)

entry(
    index = 211,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0259115,'m^3/(mol*s)'), n=2.33049, w0=(377500,'J/mol'), E0=(61792.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(366.299,'m^3/(mol*s)'), n=0.916553, w0=(327000,'J/mol'), E0=(73270.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11047040505053281, var=5.122195722886658, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 4.814734063194315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.814734063194315""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.814734063194315
""",
)

entry(
    index = 213,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(117214,'m^3/(mol*s)'), n=0.110404, w0=(327000,'J/mol'), E0=(73986.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0005607884507079853, var=39.749150430562956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 12.640647685955308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 12.640647685955308""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 12.640647685955308
""",
)

entry(
    index = 214,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.0554e-06,'m^3/(mol*s)'), n=3.59767, w0=(327000,'J/mol'), E0=(59530.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03057398140750648, var=4.704942828754961, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.425265883905166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.425265883905166""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.425265883905166
""",
)

entry(
    index = 215,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(9.83347e-07,'m^3/(mol*s)'), n=4.00094, w0=(327000,'J/mol'), E0=(62442.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.021445085621872584, var=3.8748521801912013, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.000131799815043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.000131799815043""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.000131799815043
""",
)

entry(
    index = 216,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.53987e-08,'m^3/(mol*s)'), n=3.58104, w0=(327000,'J/mol'), E0=(50814.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0009632298488913212, var=17.75701662293015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 8.450188402258629"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 8.450188402258629""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 8.450188402258629
""",
)

entry(
    index = 217,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1.5435e+12,'m^3/(mol*s)'), n=-2.41311, w0=(327000,'J/mol'), E0=(97012.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12751868818031306, var=28.994771781934414, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 11.115254302306761"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 11.115254302306761""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 11.115254302306761
""",
)

entry(
    index = 218,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(1.78101,'m^3/(mol*s)'), n=1.82901, w0=(327000,'J/mol'), E0=(67926.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0647174724807686, var=3.6225396657723055, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F',), comment="""BM rule fitted to 29 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 3.9782130763678434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F
Total Standard Deviation in ln(k): 3.9782130763678434""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F
Total Standard Deviation in ln(k): 3.9782130763678434
""",
)

entry(
    index = 219,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(4.24011e+07,'m^3/(mol*s)'), n=-0.533601, w0=(325942,'J/mol'), E0=(87788.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1579990028862138, var=4.409430671013229, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F',), comment="""BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 4.606654322166015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.606654322166015""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.606654322166015
""",
)

entry(
    index = 220,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.11937e+08,'m^3/(mol*s)'), n=-0.562766, w0=(327000,'J/mol'), E0=(87940.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15817733257171987, var=6.059066948781727, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 5.332120367617018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.332120367617018""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.332120367617018
""",
)

entry(
    index = 221,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000296645,'m^3/(mol*s)'), n=3.33465, w0=(327000,'J/mol'), E0=(67625.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.65487e-38,'m^3/(mol*s)'), n=13.4974, w0=(327000,'J/mol'), E0=(-16709.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06661951038906799, var=19.34471207690335, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 8.984736603149146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.984736603149146""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.984736603149146
""",
)

entry(
    index = 223,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.21196e-06,'m^3/(mol*s)'), n=3.85925, w0=(327000,'J/mol'), E0=(61730.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.926428,'m^3/(mol*s)'), n=2.16368, w0=(299500,'J/mol'), E0=(16602.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09593389252858672, var=0.7947813293060015, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 2.0282714608586576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 2.0282714608586576""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 2.0282714608586576
""",
)

entry(
    index = 225,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(9.70669e+11,'m^3/(mol*s)'), n=-1.40887, w0=(299500,'J/mol'), E0=(69499.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18651956848690546, var=3.511965692339225, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 18 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 4.225563641361109"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 4.225563641361109""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 4.225563641361109
""",
)

entry(
    index = 226,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(2.57496e+15,'m^3/(mol*s)'), n=-2.49451, w0=(299500,'J/mol'), E0=(74924.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3895354003863016, var=9.079003891136244, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C
    Total Standard Deviation in ln(k): 7.019276695908444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 7.019276695908444""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 7.019276695908444
""",
)

entry(
    index = 227,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(8.08352e+18,'m^3/(mol*s)'), n=-3.40939, w0=(299500,'J/mol'), E0=(92961.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.032267005243502234, var=8.014132026958464, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 5.756325993783535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 5.756325993783535""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 5.756325993783535
""",
)

entry(
    index = 228,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.187594,'m^3/(mol*s)'), n=2.42669, w0=(299500,'J/mol'), E0=(42098.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(3.3758e+14,'m^3/(mol*s)'), n=-2.14635, w0=(299500,'J/mol'), E0=(77428.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2455578683853529, var=5.0259603838097835, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 5.111325735679105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 5.111325735679105""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 5.111325735679105
""",
)

entry(
    index = 230,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1",
    kinetics = ArrheniusBM(A=(1.31503e+18,'m^3/(mol*s)'), n=-3.05557, w0=(299500,'J/mol'), E0=(98579.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.22393609072918771, var=17.247557790330102, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1
    Total Standard Deviation in ln(k): 8.88835418264951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1
Total Standard Deviation in ln(k): 8.88835418264951""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1
Total Standard Deviation in ln(k): 8.88835418264951
""",
)

entry(
    index = 231,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.98544e+16,'m^3/(mol*s)'), n=-2.73076, w0=(299500,'J/mol'), E0=(94557.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0301459369916237, var=22.241369207330592, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1
    Total Standard Deviation in ln(k): 12.04278858758272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1
Total Standard Deviation in ln(k): 12.04278858758272""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1
Total Standard Deviation in ln(k): 12.04278858758272
""",
)

entry(
    index = 232,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.33002e+11,'m^3/(mol*s)'), n=-1.35405, w0=(299500,'J/mol'), E0=(71262.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2067751495373023, var=4.237950174851678, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.6465397685352485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 4.6465397685352485""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 4.6465397685352485
""",
)

entry(
    index = 233,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.96772e+09,'m^3/(mol*s)'), n=-0.656033, w0=(299500,'J/mol'), E0=(65507.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07592908147866317, var=4.608376756792764, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 4.494367463306099"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.494367463306099""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.494367463306099
""",
)

entry(
    index = 234,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0599532,'m^3/(mol*s)'), n=2.51396, w0=(299500,'J/mol'), E0=(51142.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.75053e+12,'m^3/(mol*s)'), n=-1.68113, w0=(299500,'J/mol'), E0=(77618.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.016102156177829823, var=16.746931777266713, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 8.24443809468803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.24443809468803""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.24443809468803
""",
)

entry(
    index = 236,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8844.6,'m^3/(mol*s)'), n=0.841545, w0=(321562,'J/mol'), E0=(69016.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1001696239143631, var=7.990335230806462, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 5.918503406064323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.918503406064323""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.918503406064323
""",
)

entry(
    index = 237,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C",
    kinetics = ArrheniusBM(A=(725.803,'m^3/(mol*s)'), n=1.0218, w0=(327000,'J/mol'), E0=(54101.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C",
    kinetics = ArrheniusBM(A=(8.26735e+08,'m^3/(mol*s)'), n=-0.572937, w0=(324825,'J/mol'), E0=(88680.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16693093827241923, var=4.514835823116425, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C',), comment="""BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
    Total Standard Deviation in ln(k): 4.679114234610594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 4.679114234610594""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 4.679114234610594
""",
)

entry(
    index = 239,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3541.93,'m^3/(mol*s)'), n=1.13226, w0=(327000,'J/mol'), E0=(42355.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4922815922106995, var=0.0675906456998819, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 1.758083478257886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.758083478257886""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.758083478257886
""",
)

entry(
    index = 240,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.011895,'m^3/(mol*s)'), n=2.70774, w0=(327000,'J/mol'), E0=(88319.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(1.29067e+07,'m^3/(mol*s)'), n=-0.349034, w0=(299500,'J/mol'), E0=(68114,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.206993799688753, var=1.929037274525198, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 3.3044571892051415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C
Total Standard Deviation in ln(k): 3.3044571892051415""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C
Total Standard Deviation in ln(k): 3.3044571892051415
""",
)

entry(
    index = 242,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(0.00255885,'m^3/(mol*s)'), n=2.71007, w0=(299500,'J/mol'), E0=(66939.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000330289,'m^3/(mol*s)'), n=3.11442, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1023.11,'m^3/(mol*s)'), n=1.14376, w0=(299500,'J/mol'), E0=(54640.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08954634623061489, var=2.3591707485291096, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C
    Total Standard Deviation in ln(k): 3.3041821604826875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C
Total Standard Deviation in ln(k): 3.3041821604826875""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C
Total Standard Deviation in ln(k): 3.3041821604826875
""",
)

entry(
    index = 245,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F",
    kinetics = ArrheniusBM(A=(0.0201449,'m^3/(mol*s)'), n=2.57076, w0=(283500,'J/mol'), E0=(21371,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F",
    kinetics = ArrheniusBM(A=(0.263742,'m^3/(mol*s)'), n=1.61124, w0=(283500,'J/mol'), E0=(23360.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F",
    kinetics = ArrheniusBM(A=(2.57795e-05,'m^3/(mol*s)'), n=3.21224, w0=(299500,'J/mol'), E0=(25655.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0661661831414553, var=0.2506603564918515, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F
    Total Standard Deviation in ln(k): 1.1699371967765075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F
Total Standard Deviation in ln(k): 1.1699371967765075""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F
Total Standard Deviation in ln(k): 1.1699371967765075
""",
)

entry(
    index = 248,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F",
    kinetics = ArrheniusBM(A=(3.93289e-06,'m^3/(mol*s)'), n=3.4855, w0=(298159,'J/mol'), E0=(22262.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16177749076002598, var=2.7517340612649095, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F
    Total Standard Deviation in ln(k): 3.7320011241174615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 3.7320011241174615""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 3.7320011241174615
""",
)

entry(
    index = 249,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.363995,'m^3/(mol*s)'), n=1.58261, w0=(299500,'J/mol'), E0=(62022.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025334381594396455, var=2.2657468228388518, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.0812612303089155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.0812612303089155""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.0812612303089155
""",
)

entry(
    index = 250,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(116.243,'m^3/(mol*s)'), n=1.04438, w0=(299500,'J/mol'), E0=(61427.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0777946218744535, var=4.991848883757391, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.6745323732290975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.6745323732290975""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.6745323732290975
""",
)

entry(
    index = 251,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C",
    kinetics = ArrheniusBM(A=(72.8353,'m^3/(mol*s)'), n=1.22977, w0=(299500,'J/mol'), E0=(60676.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08338956629706909, var=1.3476248744469534, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C
    Total Standard Deviation in ln(k): 2.536763269535293"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C
Total Standard Deviation in ln(k): 2.536763269535293""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C
Total Standard Deviation in ln(k): 2.536763269535293
""",
)

entry(
    index = 252,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C",
    kinetics = ArrheniusBM(A=(8.87507,'m^3/(mol*s)'), n=1.16946, w0=(299500,'J/mol'), E0=(62411.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0005014666844774744, var=0.891994937425714, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C
    Total Standard Deviation in ln(k): 1.89464170548072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C
Total Standard Deviation in ln(k): 1.89464170548072""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C
Total Standard Deviation in ln(k): 1.89464170548072
""",
)

entry(
    index = 253,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(8.86035e-05,'m^3/(mol*s)'), n=3.31017, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(6.08473,'m^3/(mol*s)'), n=1.89139, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1219.29,'m^3/(mol*s)'), n=1.09228, w0=(272000,'J/mol'), E0=(21277.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1913114745269135, var=0.5675406765016174, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.503518007673117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.503518007673117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.503518007673117
""",
)

entry(
    index = 256,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0597365,'m^3/(mol*s)'), n=2.3895, w0=(272000,'J/mol'), E0=(29395.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.3625e-06,'m^3/(mol*s)'), n=3.69896, w0=(272000,'J/mol'), E0=(10235.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6066750992718065, var=8.593307038198269, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl
    Total Standard Deviation in ln(k): 7.401058457119929"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.401058457119929""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.401058457119929
""",
)

entry(
    index = 258,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.351516,'m^3/(mol*s)'), n=2.39226, w0=(272000,'J/mol'), E0=(23076,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023041261703404602, var=2.1401451567308634, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R
    Total Standard Deviation in ln(k): 2.990666666404452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R
Total Standard Deviation in ln(k): 2.990666666404452""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R
Total Standard Deviation in ln(k): 2.990666666404452
""",
)

entry(
    index = 259,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(64.768,'m^3/(mol*s)'), n=1.81809, w0=(377500,'J/mol'), E0=(59372.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(620936,'m^3/(mol*s)'), n=0.62293, w0=(377500,'J/mol'), E0=(54425.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0005192183537101806, var=3.0794519637078803, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 3.519287324884224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.519287324884224""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.519287324884224
""",
)

entry(
    index = 261,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R",
    kinetics = ArrheniusBM(A=(65.426,'m^3/(mol*s)'), n=1.83086, w0=(377500,'J/mol'), E0=(62155.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O",
    kinetics = ArrheniusBM(A=(0.0378161,'m^3/(mol*s)'), n=2.74125, w0=(377500,'J/mol'), E0=(41846.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.023680740226199763, var=0.19008211131011138, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O
    Total Standard Deviation in ln(k): 0.9335319102518352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O
Total Standard Deviation in ln(k): 0.9335319102518352""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O
Total Standard Deviation in ln(k): 0.9335319102518352
""",
)

entry(
    index = 263,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O",
    kinetics = ArrheniusBM(A=(2.61617e-05,'m^3/(mol*s)'), n=3.67953, w0=(377500,'J/mol'), E0=(49632.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02377539428597138, var=0.873311909685643, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O',), comment="""BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O
    Total Standard Deviation in ln(k): 1.9331853339617282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O
Total Standard Deviation in ln(k): 1.9331853339617282""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O
Total Standard Deviation in ln(k): 1.9331853339617282
""",
)

entry(
    index = 264,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(14.8684,'m^3/(mol*s)'), n=1.9007, w0=(377500,'J/mol'), E0=(71831,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.908204622138397e-05, var=0.004456003875672238, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 0.13397114162889823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 0.13397114162889823""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 0.13397114162889823
""",
)

entry(
    index = 265,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(524.975,'m^3/(mol*s)'), n=1.47174, w0=(377500,'J/mol'), E0=(60323.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003149700317788727, var=0.29128720082488474, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.089889976746263"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.089889976746263""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.089889976746263
""",
)

entry(
    index = 266,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C",
    kinetics = ArrheniusBM(A=(1.44504e-13,'m^3/(mol*s)'), n=6.19832, w0=(377500,'J/mol'), E0=(8946.89,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07018555899382649, var=2.314011270609315, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C
    Total Standard Deviation in ln(k): 3.2259234742034044"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C
Total Standard Deviation in ln(k): 3.2259234742034044""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C
Total Standard Deviation in ln(k): 3.2259234742034044
""",
)

entry(
    index = 267,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C",
    kinetics = ArrheniusBM(A=(43.7292,'m^3/(mol*s)'), n=1.85998, w0=(377500,'J/mol'), E0=(56644.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 268,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C",
    kinetics = ArrheniusBM(A=(45.5028,'m^3/(mol*s)'), n=1.93983, w0=(377500,'J/mol'), E0=(59994.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C",
    kinetics = ArrheniusBM(A=(68.8575,'m^3/(mol*s)'), n=1.80771, w0=(377500,'J/mol'), E0=(62251.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.49482e-13,'m^3/(mol*s)'), n=6.20421, w0=(377500,'J/mol'), E0=(16272.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008244183909516404, var=11.52065940282592, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R
    Total Standard Deviation in ln(k): 6.825205250517261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R
Total Standard Deviation in ln(k): 6.825205250517261""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R
Total Standard Deviation in ln(k): 6.825205250517261
""",
)

entry(
    index = 271,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(34.7298,'m^3/(mol*s)'), n=1.98737, w0=(377500,'J/mol'), E0=(59053.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8767.63,'m^3/(mol*s)'), n=1.18687, w0=(377500,'J/mol'), E0=(63346.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8496842976118266, var=2.198267000793379, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 5.107216434720141"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.107216434720141""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.107216434720141
""",
)

entry(
    index = 273,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(318.428,'m^3/(mol*s)'), n=1.54984, w0=(377500,'J/mol'), E0=(57380.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011733064123095561, var=1.4148880597504876, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.4140937358243337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.4140937358243337""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.4140937358243337
""",
)

entry(
    index = 274,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00796311,'m^3/(mol*s)'), n=2.96059, w0=(377500,'J/mol'), E0=(56085.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10929920813184171, var=0.5562842067702486, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 1.7698420108438244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.7698420108438244""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.7698420108438244
""",
)

entry(
    index = 275,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(71.139,'m^3/(mol*s)'), n=1.83301, w0=(377500,'J/mol'), E0=(73695.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 276,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(11.7668,'m^3/(mol*s)'), n=1.99796, w0=(377500,'J/mol'), E0=(64561,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0003466035739259883, var=0.22277634877564198, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 0.9470895710421666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 0.9470895710421666""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 0.9470895710421666
""",
)

entry(
    index = 277,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(84.0213,'m^3/(mol*s)'), n=1.80109, w0=(377500,'J/mol'), E0=(61440.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012592436659483893, var=0.3541022035015281, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 1.196111353749668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.196111353749668""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.196111353749668
""",
)

entry(
    index = 278,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(100.122,'m^3/(mol*s)'), n=1.85066, w0=(377500,'J/mol'), E0=(60272.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00031043362799039134, var=4.024393182409867, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.022457023872945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.022457023872945""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.022457023872945
""",
)

entry(
    index = 279,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(0.000241839,'m^3/(mol*s)'), n=2.71215, w0=(377500,'J/mol'), E0=(46191.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(1.08171e-08,'m^3/(mol*s)'), n=4.02663, w0=(377500,'J/mol'), E0=(59950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1347507805078687, var=3.1469027492292554, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 3.894871933916145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 3.894871933916145""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 3.894871933916145
""",
)

entry(
    index = 281,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.371209,'m^3/(mol*s)'), n=1.87014, w0=(377500,'J/mol'), E0=(74840,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.046645032474836014, var=0.9675748276974954, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 2.089163880932612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.089163880932612""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.089163880932612
""",
)

entry(
    index = 282,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.00173745,'m^3/(mol*s)'), n=2.69634, w0=(377500,'J/mol'), E0=(63809.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00016159748633279227, var=0.3338780567189362, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 1.158785696695627"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 1.158785696695627""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 1.158785696695627
""",
)

entry(
    index = 283,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.00330492,'m^3/(mol*s)'), n=2.62035, w0=(377500,'J/mol'), E0=(69385.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010444592997049295, var=2.28109926366191, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 3.0304374945678423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 3.0304374945678423""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 3.0304374945678423
""",
)

entry(
    index = 284,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00550838,'m^3/(mol*s)'), n=2.44854, w0=(377500,'J/mol'), E0=(59231,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0041865438883804725, var=0.1617016605554352, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 0.8166659306943025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.8166659306943025""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.8166659306943025
""",
)

entry(
    index = 285,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00111823,'m^3/(mol*s)'), n=2.56187, w0=(377500,'J/mol'), E0=(58876.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl",
    kinetics = ArrheniusBM(A=(5.35812e-06,'m^3/(mol*s)'), n=3.32429, w0=(377500,'J/mol'), E0=(58307,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.018157015485602404, var=1.0586975266186027, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl
    Total Standard Deviation in ln(k): 2.1083532718078715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl
Total Standard Deviation in ln(k): 2.1083532718078715""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl
Total Standard Deviation in ln(k): 2.1083532718078715
""",
)

entry(
    index = 287,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.64357e-06,'m^3/(mol*s)'), n=3.57624, w0=(377500,'J/mol'), E0=(58582.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04640008445522524, var=1.0836002758701861, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.2034346125080644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.2034346125080644""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.2034346125080644
""",
)

entry(
    index = 288,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0010759,'m^3/(mol*s)'), n=2.77566, w0=(377500,'J/mol'), E0=(65989.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009177287293078696, var=0.028438358688296892, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R
    Total Standard Deviation in ln(k): 0.361130549982178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.361130549982178""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.361130549982178
""",
)

entry(
    index = 289,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0322278,'m^3/(mol*s)'), n=2.36183, w0=(377500,'J/mol'), E0=(60197.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.039402674941999734, var=0.6369004936865642, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R
    Total Standard Deviation in ln(k): 1.6989014886916176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R
Total Standard Deviation in ln(k): 1.6989014886916176""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R
Total Standard Deviation in ln(k): 1.6989014886916176
""",
)

entry(
    index = 290,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C",
    kinetics = ArrheniusBM(A=(0.00593802,'m^3/(mol*s)'), n=2.48442, w0=(377500,'J/mol'), E0=(57607.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.0174812,'m^3/(mol*s)'), n=2.32835, w0=(377500,'J/mol'), E0=(56215.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 292,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(0.0114951,'m^3/(mol*s)'), n=2.42703, w0=(377500,'J/mol'), E0=(62239.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0065274743355576625, var=0.9999209284489792, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C
    Total Standard Deviation in ln(k): 2.021056506356637"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 2.021056506356637""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 2.021056506356637
""",
)

entry(
    index = 293,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(0.287756,'m^3/(mol*s)'), n=2.01677, w0=(377500,'J/mol'), E0=(90165.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F",
    kinetics = ArrheniusBM(A=(0.000223254,'m^3/(mol*s)'), n=3.0128, w0=(327000,'J/mol'), E0=(57292.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006282779934434974, var=1.0685907656962395, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F
    Total Standard Deviation in ln(k): 2.0881339343442447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F
Total Standard Deviation in ln(k): 2.0881339343442447""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F
Total Standard Deviation in ln(k): 2.0881339343442447
""",
)

entry(
    index = 295,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(489552,'m^3/(mol*s)'), n=-0.0724467, w0=(327000,'J/mol'), E0=(80618.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16187402305147108, var=4.728345412085818, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F',), comment="""BM rule fitted to 16 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F
    Total Standard Deviation in ln(k): 4.765966749840817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F
Total Standard Deviation in ln(k): 4.765966749840817""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F
Total Standard Deviation in ln(k): 4.765966749840817
""",
)

entry(
    index = 296,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00021109,'m^3/(mol*s)'), n=3.01699, w0=(327000,'J/mol'), E0=(55770.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.53329e-08,'m^3/(mol*s)'), n=3.96109, w0=(327000,'J/mol'), E0=(54387,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05547706368830271, var=6.545884448065274, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.268489492730077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.268489492730077""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.268489492730077
""",
)

entry(
    index = 298,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000214944,'m^3/(mol*s)'), n=2.96092, w0=(327000,'J/mol'), E0=(60937.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003695616901324604, var=0.7252351574251228, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R
    Total Standard Deviation in ln(k): 1.7165326891231023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R
Total Standard Deviation in ln(k): 1.7165326891231023""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R
Total Standard Deviation in ln(k): 1.7165326891231023
""",
)

entry(
    index = 299,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000111183,'m^3/(mol*s)'), n=3.16652, w0=(327000,'J/mol'), E0=(75191.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.183951666246189e-05, var=0.016449742049071927, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 0.25730090154310165"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.25730090154310165""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.25730090154310165
""",
)

entry(
    index = 300,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.74342e-08,'m^3/(mol*s)'), n=4.2645, w0=(327000,'J/mol'), E0=(60940.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.57108e-05,'m^3/(mol*s)'), n=3.73131, w0=(327000,'J/mol'), E0=(66025.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010167881383970705, var=8.894128256807447, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 5.981281195803567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.981281195803567""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.981281195803567
""",
)

entry(
    index = 302,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.92682e-06,'m^3/(mol*s)'), n=3.60349, w0=(327000,'J/mol'), E0=(58382.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(5.07841e-05,'m^3/(mol*s)'), n=2.8807, w0=(327000,'J/mol'), E0=(61037.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00171439,'m^3/(mol*s)'), n=1.9068, w0=(327000,'J/mol'), E0=(59129,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C",
    kinetics = ArrheniusBM(A=(0.00560159,'m^3/(mol*s)'), n=1.54256, w0=(327000,'J/mol'), E0=(66015.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0047473589637304255, var=1.5043842744682212, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C
    Total Standard Deviation in ln(k): 2.470802644300532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C
Total Standard Deviation in ln(k): 2.470802644300532""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C
Total Standard Deviation in ln(k): 2.470802644300532
""",
)

entry(
    index = 306,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C",
    kinetics = ArrheniusBM(A=(7.21671e-05,'m^3/(mol*s)'), n=3.03858, w0=(327000,'J/mol'), E0=(65441.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(11.9669,'m^3/(mol*s)'), n=1.55709, w0=(327000,'J/mol'), E0=(69178.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07904268229904748, var=3.7873463133006475, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R',), comment="""BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.100035809190126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.100035809190126""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.100035809190126
""",
)

entry(
    index = 308,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br",
    kinetics = ArrheniusBM(A=(1.43701e-06,'m^3/(mol*s)'), n=3.70864, w0=(327000,'J/mol'), E0=(56670.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br",
    kinetics = ArrheniusBM(A=(0.0013868,'m^3/(mol*s)'), n=3.03795, w0=(327000,'J/mol'), E0=(65151.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.395783359025404e-06, var=5.053759431991071, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br
    Total Standard Deviation in ln(k): 4.506776930258356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br
Total Standard Deviation in ln(k): 4.506776930258356""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br
Total Standard Deviation in ln(k): 4.506776930258356
""",
)

entry(
    index = 310,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00288807,'m^3/(mol*s)'), n=2.45122, w0=(327000,'J/mol'), E0=(67260.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01732965311860244, var=3.442014724156741, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 3.7628601793281518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.7628601793281518""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.7628601793281518
""",
)

entry(
    index = 311,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00311851,'m^3/(mol*s)'), n=2.95174, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(4.86852e+09,'m^3/(mol*s)'), n=-0.821925, w0=(327000,'J/mol'), E0=(94589.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14414194563316668, var=8.675179977403488, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi
    Total Standard Deviation in ln(k): 6.2668439233947595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi
Total Standard Deviation in ln(k): 6.2668439233947595""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi
Total Standard Deviation in ln(k): 6.2668439233947595
""",
)

entry(
    index = 313,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(1565.77,'m^3/(mol*s)'), n=0.653508, w0=(327000,'J/mol'), E0=(57810,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(9.79469e-05,'m^3/(mol*s)'), n=3.46572, w0=(327000,'J/mol'), E0=(77684.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl",
    kinetics = ArrheniusBM(A=(1.74981,'m^3/(mol*s)'), n=2.26956, w0=(299500,'J/mol'), E0=(37672.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(618.116,'m^3/(mol*s)'), n=1.30893, w0=(299500,'J/mol'), E0=(36712.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003038371646634461, var=1.3523287104698158, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl
    Total Standard Deviation in ln(k): 2.3389338844578536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl
Total Standard Deviation in ln(k): 2.3389338844578536""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl
Total Standard Deviation in ln(k): 2.3389338844578536
""",
)

entry(
    index = 317,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(9.81808e+06,'m^3/(mol*s)'), n=0.00915098, w0=(299500,'J/mol'), E0=(61462.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11111470769706903, var=3.081758780500183, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R
    Total Standard Deviation in ln(k): 3.798482852196422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R
Total Standard Deviation in ln(k): 3.798482852196422""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R
Total Standard Deviation in ln(k): 3.798482852196422
""",
)

entry(
    index = 318,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C",
    kinetics = ArrheniusBM(A=(2.52746e+17,'m^3/(mol*s)'), n=-2.94374, w0=(299500,'J/mol'), E0=(75732.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2211199036338823, var=5.5143806239174955, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C
    Total Standard Deviation in ln(k): 5.263240571693213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C
Total Standard Deviation in ln(k): 5.263240571693213""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C
Total Standard Deviation in ln(k): 5.263240571693213
""",
)

entry(
    index = 319,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C",
    kinetics = ArrheniusBM(A=(9.3956e+09,'m^3/(mol*s)'), n=-0.739273, w0=(299500,'J/mol'), E0=(63896.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6104772147164502, var=10.805992107240732, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C
    Total Standard Deviation in ln(k): 8.123921494357152"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C
Total Standard Deviation in ln(k): 8.123921494357152""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C
Total Standard Deviation in ln(k): 8.123921494357152
""",
)

entry(
    index = 320,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.92534e+14,'m^3/(mol*s)'), n=-2.3367, w0=(299500,'J/mol'), E0=(73048.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14026699017356756, var=13.938862807549027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R
    Total Standard Deviation in ln(k): 7.837065227879554"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 7.837065227879554""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 7.837065227879554
""",
)

entry(
    index = 321,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(71.082,'m^3/(mol*s)'), n=1.78047, w0=(299500,'J/mol'), E0=(70716,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1",
    kinetics = ArrheniusBM(A=(1.67749,'m^3/(mol*s)'), n=2.41807, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1",
    kinetics = ArrheniusBM(A=(40.6724,'m^3/(mol*s)'), n=1.5243, w0=(299500,'J/mol'), E0=(50479.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1",
    kinetics = ArrheniusBM(A=(0.00212116,'m^3/(mol*s)'), n=2.9814, w0=(299500,'J/mol'), E0=(10321.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07687478480206693, var=0.775349125305861, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1
    Total Standard Deviation in ln(k): 1.95840036768154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1
Total Standard Deviation in ln(k): 1.95840036768154""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1
Total Standard Deviation in ln(k): 1.95840036768154
""",
)

entry(
    index = 325,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1",
    kinetics = ArrheniusBM(A=(6769.81,'m^3/(mol*s)'), n=0.887292, w0=(299500,'J/mol'), E0=(63390.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.003778940356615353, var=2.6589120191492643, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1
    Total Standard Deviation in ln(k): 3.278450057002987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1
Total Standard Deviation in ln(k): 3.278450057002987""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1
Total Standard Deviation in ln(k): 3.278450057002987
""",
)

entry(
    index = 326,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.13444,'m^3/(mol*s)'), n=2.35273, w0=(299500,'J/mol'), E0=(46537.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 327,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(50.2678,'m^3/(mol*s)'), n=1.51875, w0=(299500,'J/mol'), E0=(67395.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.96517e+08,'m^3/(mol*s)'), n=-0.35908, w0=(299500,'J/mol'), E0=(63002.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1668904046578665, var=1.3203205406318375, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.7228675114938508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.7228675114938508""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.7228675114938508
""",
)

entry(
    index = 329,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.95329e+14,'m^3/(mol*s)'), n=-2.33311, w0=(299500,'J/mol'), E0=(79385.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0984661244457889, var=18.061639955065257, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 8.767323556621033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.767323556621033""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.767323556621033
""",
)

entry(
    index = 330,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.316045,'m^3/(mol*s)'), n=2.33519, w0=(299500,'J/mol'), E0=(38132.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.0284258,'m^3/(mol*s)'), n=2.56818, w0=(299500,'J/mol'), E0=(46869,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.0415779,'m^3/(mol*s)'), n=2.65327, w0=(299500,'J/mol'), E0=(45024.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00435304,'m^3/(mol*s)'), n=2.58838, w0=(299500,'J/mol'), E0=(46985.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(13899.3,'m^3/(mol*s)'), n=0.768725, w0=(316125,'J/mol'), E0=(60581.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07470821060213943, var=13.065911389966415, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 7.434184830241345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 7.434184830241345""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 7.434184830241345
""",
)

entry(
    index = 335,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(7.2595e-08,'m^3/(mol*s)'), n=4.13373, w0=(327000,'J/mol'), E0=(54792.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05809522364590576, var=2.98500081390869, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 3.6095797448911116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 3.6095797448911116""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 3.6095797448911116
""",
)

entry(
    index = 336,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00963475,'m^3/(mol*s)'), n=2.576, w0=(327000,'J/mol'), E0=(67940.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010475052241760001, var=1.4079108247177574, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.4050460148448516"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.4050460148448516""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.4050460148448516
""",
)

entry(
    index = 337,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.78434e+17,'m^3/(mol*s)'), n=-2.97996, w0=(320786,'J/mol'), E0=(103502,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2205723362936119, var=9.383771329527304, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 6.6952951765202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 6.6952951765202""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 6.6952951765202
""",
)

entry(
    index = 338,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0111464,'m^3/(mol*s)'), n=2.7136, w0=(327000,'J/mol'), E0=(23557.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0343304,'m^3/(mol*s)'), n=2.71102, w0=(327000,'J/mol'), E0=(39616.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(689018,'m^3/(mol*s)'), n=0.0162562, w0=(299500,'J/mol'), E0=(66999,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19563393898648063, var=6.602091346774926, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 5.64261614412096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.64261614412096""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.64261614412096
""",
)

entry(
    index = 341,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.08671e-06,'m^3/(mol*s)'), n=3.48783, w0=(299500,'J/mol'), E0=(21990.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000102465,'m^3/(mol*s)'), n=3.10435, w0=(299500,'J/mol'), E0=(30363.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000506611,'m^3/(mol*s)'), n=3.06943, w0=(299500,'J/mol'), E0=(35204.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000195765,'m^3/(mol*s)'), n=2.96441, w0=(299500,'J/mol'), E0=(29381.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.028929522391603308, var=0.09224729462518909, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 0.6815701858591555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6815701858591555""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6815701858591555
""",
)

entry(
    index = 345,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.34555e-05,'m^3/(mol*s)'), n=3.14313, w0=(299500,'J/mol'), E0=(32720.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 346,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C",
    kinetics = ArrheniusBM(A=(0.00122456,'m^3/(mol*s)'), n=2.76919, w0=(299500,'J/mol'), E0=(12380,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7002253211393781, var=0.15813103416886778, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C
    Total Standard Deviation in ln(k): 2.5565569001887103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C
Total Standard Deviation in ln(k): 2.5565569001887103""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C
Total Standard Deviation in ln(k): 2.5565569001887103
""",
)

entry(
    index = 347,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C",
    kinetics = ArrheniusBM(A=(5.75202e-08,'m^3/(mol*s)'), n=4.00082, w0=(297712,'J/mol'), E0=(1462.92,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3435472705189543, var=2.6794121962535344, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C
    Total Standard Deviation in ln(k): 4.144716933198208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C
Total Standard Deviation in ln(k): 4.144716933198208""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C
Total Standard Deviation in ln(k): 4.144716933198208
""",
)

entry(
    index = 348,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.876719,'m^3/(mol*s)'), n=1.48331, w0=(299500,'J/mol'), E0=(62975.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03320468577562097, var=3.0158899730781634, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 3.5649155241091224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 3.5649155241091224""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 3.5649155241091224
""",
)

entry(
    index = 349,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(41816.3,'m^3/(mol*s)'), n=0.258408, w0=(299500,'J/mol'), E0=(69793.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09454136027924473, var=8.846855734974584, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 6.200357846770421"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 6.200357846770421""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 6.200357846770421
""",
)

entry(
    index = 350,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00107019,'m^3/(mol*s)'), n=2.65069, w0=(299500,'J/mol'), E0=(43430.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012862768896435055, var=0.6207633877547286, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 1.6118199930881558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 1.6118199930881558""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 1.6118199930881558
""",
)

entry(
    index = 351,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.210425,'m^3/(mol*s)'), n=1.63892, w0=(299500,'J/mol'), E0=(45062.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.776813,'m^3/(mol*s)'), n=1.65286, w0=(299500,'J/mol'), E0=(61098.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 353,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0541297,'m^3/(mol*s)'), n=2.12015, w0=(299500,'J/mol'), E0=(59526.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04559190981117677, var=0.21127001927066036, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.0360113445017183"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.0360113445017183""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.0360113445017183
""",
)

entry(
    index = 354,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(0.0780684,'m^3/(mol*s)'), n=2.10772, w0=(299500,'J/mol'), E0=(48216.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01476789479809785, var=2.41747152497532, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C
    Total Standard Deviation in ln(k): 3.1541115130655846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C
Total Standard Deviation in ln(k): 3.1541115130655846""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C
Total Standard Deviation in ln(k): 3.1541115130655846
""",
)

entry(
    index = 355,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(0.00285547,'m^3/(mol*s)'), n=2.56268, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O",
    kinetics = ArrheniusBM(A=(0.589857,'m^3/(mol*s)'), n=1.65372, w0=(299500,'J/mol'), E0=(62918.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O",
    kinetics = ArrheniusBM(A=(0.00147361,'m^3/(mol*s)'), n=2.19756, w0=(299500,'J/mol'), E0=(51118.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001162160510718151, var=0.41603330090534907, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O
    Total Standard Deviation in ln(k): 1.2959870262281012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O
Total Standard Deviation in ln(k): 1.2959870262281012""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O
Total Standard Deviation in ln(k): 1.2959870262281012
""",
)

entry(
    index = 358,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.0422576,'m^3/(mol*s)'), n=2.34082, w0=(272000,'J/mol'), E0=(9146.63,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.0898359,'m^3/(mol*s)'), n=2.42885, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 360,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C",
    kinetics = ArrheniusBM(A=(0.0703235,'m^3/(mol*s)'), n=2.34313, w0=(272000,'J/mol'), E0=(24215.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.0290111,'m^3/(mol*s)'), n=2.3822, w0=(272000,'J/mol'), E0=(42231.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.557574,'m^3/(mol*s)'), n=2.34801, w0=(272000,'J/mol'), E0=(11792.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21574915992104426, var=1.689255616422526, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.147664895369954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.147664895369954""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.147664895369954
""",
)

entry(
    index = 363,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(209.185,'m^3/(mol*s)'), n=1.80526, w0=(377500,'J/mol'), E0=(50373.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C",
    kinetics = ArrheniusBM(A=(107.671,'m^3/(mol*s)'), n=1.76176, w0=(377500,'J/mol'), E0=(53308.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C",
    kinetics = ArrheniusBM(A=(117.661,'m^3/(mol*s)'), n=1.76471, w0=(377500,'J/mol'), E0=(57664.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C",
    kinetics = ArrheniusBM(A=(58.4325,'m^3/(mol*s)'), n=1.86734, w0=(377500,'J/mol'), E0=(74737.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 367,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C",
    kinetics = ArrheniusBM(A=(1.04948e-08,'m^3/(mol*s)'), n=4.71651, w0=(377500,'J/mol'), E0=(-11287.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1620646789285346, var=0.6450039702023322, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C',), comment="""BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C
    Total Standard Deviation in ln(k): 2.0172433115911486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C
Total Standard Deviation in ln(k): 2.0172433115911486""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C
Total Standard Deviation in ln(k): 2.0172433115911486
""",
)

entry(
    index = 368,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(18.9529,'m^3/(mol*s)'), n=1.91362, w0=(377500,'J/mol'), E0=(74860.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 369,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(36.5503,'m^3/(mol*s)'), n=1.87317, w0=(377500,'J/mol'), E0=(59649.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.30759e-14,'m^3/(mol*s)'), n=6.43612, w0=(377500,'J/mol'), E0=(6235.65,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.049126174459264274, var=7.49383343868113, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 5.611368212732325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.611368212732325""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.611368212732325
""",
)

entry(
    index = 371,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(14.0202,'m^3/(mol*s)'), n=1.96824, w0=(377500,'J/mol'), E0=(67621.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(179.007,'m^3/(mol*s)'), n=1.73491, w0=(377500,'J/mol'), E0=(37750,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 373,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(120.578,'m^3/(mol*s)'), n=1.77539, w0=(377500,'J/mol'), E0=(62355.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 374,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(581.884,'m^3/(mol*s)'), n=1.45485, w0=(377500,'J/mol'), E0=(56776.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013218093267935757, var=2.15491873926047, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 2.97609050909299"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 2.97609050909299""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 2.97609050909299
""",
)

entry(
    index = 375,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.196087,'m^3/(mol*s)'), n=2.57658, w0=(377500,'J/mol'), E0=(57344.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013966389053329734, var=0.4769159352116721, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.419543440223081"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.419543440223081""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.419543440223081
""",
)

entry(
    index = 376,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C",
    kinetics = ArrheniusBM(A=(6.55978e-13,'m^3/(mol*s)'), n=5.97055, w0=(377500,'J/mol'), E0=(22760.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.016825194303694023, var=2.7127031637611507, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
    Total Standard Deviation in ln(k): 3.3441303377736964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
Total Standard Deviation in ln(k): 3.3441303377736964""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
Total Standard Deviation in ln(k): 3.3441303377736964
""",
)

entry(
    index = 377,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C",
    kinetics = ArrheniusBM(A=(67.2815,'m^3/(mol*s)'), n=1.83026, w0=(377500,'J/mol'), E0=(70397.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 378,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(73.4575,'m^3/(mol*s)'), n=1.82774, w0=(377500,'J/mol'), E0=(67496.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 379,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(52.0663,'m^3/(mol*s)'), n=1.89167, w0=(377500,'J/mol'), E0=(74133.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 380,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(34.4569,'m^3/(mol*s)'), n=1.89428, w0=(377500,'J/mol'), E0=(68302.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 381,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(74.2968,'m^3/(mol*s)'), n=1.88465, w0=(377500,'J/mol'), E0=(63514.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 382,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(57.7168,'m^3/(mol*s)'), n=1.89866, w0=(377500,'J/mol'), E0=(65778.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 383,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(126.882,'m^3/(mol*s)'), n=1.93859, w0=(377500,'J/mol'), E0=(61460,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 384,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(9.86912e-17,'m^3/(mol*s)'), n=6.43199, w0=(377500,'J/mol'), E0=(-23549.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20339589693159627, var=2.801299549831148, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 3.866386751221151"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 3.866386751221151""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 3.866386751221151
""",
)

entry(
    index = 385,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.47693e-06,'m^3/(mol*s)'), n=3.10583, w0=(377500,'J/mol'), E0=(35868.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 386,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000185734,'m^3/(mol*s)'), n=2.71297, w0=(377500,'J/mol'), E0=(37750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 387,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.645356,'m^3/(mol*s)'), n=1.78934, w0=(377500,'J/mol'), E0=(74105.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07688712987796288, var=1.7078949076358743, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 2.813100914136679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.813100914136679""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.813100914136679
""",
)

entry(
    index = 388,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.97108e-05,'m^3/(mol*s)'), n=2.90057, w0=(377500,'J/mol'), E0=(64016,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00033355,'m^3/(mol*s)'), n=2.63731, w0=(377500,'J/mol'), E0=(49336.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00028866,'m^3/(mol*s)'), n=2.74158, w0=(377500,'J/mol'), E0=(50356.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 391,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00141842,'m^3/(mol*s)'), n=2.67769, w0=(377500,'J/mol'), E0=(68414.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005146716086813761, var=4.865896230803715, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R
    Total Standard Deviation in ln(k): 4.435131759770366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.435131759770366""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.435131759770366
""",
)

entry(
    index = 392,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C",
    kinetics = ArrheniusBM(A=(0.00296538,'m^3/(mol*s)'), n=2.42542, w0=(377500,'J/mol'), E0=(54201.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 393,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C",
    kinetics = ArrheniusBM(A=(5.4353e-05,'m^3/(mol*s)'), n=3.2139, w0=(377500,'J/mol'), E0=(58723.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 394,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.00795104,'m^3/(mol*s)'), n=2.37976, w0=(377500,'J/mol'), E0=(58468.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0029666907561632172, var=0.23934870810448683, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 0.9882361018672746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.9882361018672746""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.9882361018672746
""",
)

entry(
    index = 395,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.38442e-06,'m^3/(mol*s)'), n=3.32881, w0=(377500,'J/mol'), E0=(58154,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02234276367191037, var=1.8084903542496438, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 2.752107799571482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 2.752107799571482""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 2.752107799571482
""",
)

entry(
    index = 396,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.00427636,'m^3/(mol*s)'), n=2.49556, w0=(377500,'J/mol'), E0=(64799.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.021504564696054083, var=1.8855331929087173, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 2.806827898684325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.806827898684325""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.806827898684325
""",
)

entry(
    index = 397,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.0538026,'m^3/(mol*s)'), n=2.18986, w0=(377500,'J/mol'), E0=(55498.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 398,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.1618e-05,'m^3/(mol*s)'), n=3.06026, w0=(377500,'J/mol'), E0=(48013.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 399,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C",
    kinetics = ArrheniusBM(A=(0.0046457,'m^3/(mol*s)'), n=2.46618, w0=(377500,'J/mol'), E0=(67524.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 400,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C",
    kinetics = ArrheniusBM(A=(0.000850733,'m^3/(mol*s)'), n=2.60501, w0=(377500,'J/mol'), E0=(57681.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 401,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.0014796,'m^3/(mol*s)'), n=2.7223, w0=(377500,'J/mol'), E0=(66026.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00018832264319449838, var=0.08733201769548907, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F
    Total Standard Deviation in ln(k): 0.5929123037745985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 0.5929123037745985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 0.5929123037745985
""",
)

entry(
    index = 402,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.000440121,'m^3/(mol*s)'), n=2.90314, w0=(377500,'J/mol'), E0=(65398.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.016445454809353, var=0.07448762433871525, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 0.5884609752313108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 0.5884609752313108""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 0.5884609752313108
""",
)

entry(
    index = 403,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.193819,'m^3/(mol*s)'), n=2.12119, w0=(377500,'J/mol'), E0=(61123,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.048934453760816135, var=0.994609095494404, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.122274996199205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.122274996199205""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.122274996199205
""",
)

entry(
    index = 404,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.00199999,'m^3/(mol*s)'), n=2.61593, w0=(377500,'J/mol'), E0=(51114.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00817698,'m^3/(mol*s)'), n=2.52239, w0=(377500,'J/mol'), E0=(61553,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0020595381092611605, var=1.5684528412515595, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.515862575529665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R
Total Standard Deviation in ln(k): 2.515862575529665""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R
Total Standard Deviation in ln(k): 2.515862575529665
""",
)

entry(
    index = 406,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F",
    kinetics = ArrheniusBM(A=(9.05162,'m^3/(mol*s)'), n=1.36072, w0=(377500,'J/mol'), E0=(60730.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 407,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.00498304,'m^3/(mol*s)'), n=2.40441, w0=(377500,'J/mol'), E0=(59258.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 408,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000163473,'m^3/(mol*s)'), n=3.00273, w0=(327000,'J/mol'), E0=(56991.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0041362367332316114, var=0.4176411592695972, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 1.30595585056726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 1.30595585056726""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 1.30595585056726
""",
)

entry(
    index = 409,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(7.99212e+08,'m^3/(mol*s)'), n=-0.92296, w0=(327000,'J/mol'), E0=(81449.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19878686166044093, var=9.108222497007953, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 6.549721227853546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.549721227853546""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.549721227853546
""",
)

entry(
    index = 410,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(0.0708442,'m^3/(mol*s)'), n=1.90476, w0=(327000,'J/mol'), E0=(69001.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06919303534960755, var=2.942289576271743, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 3.612594662868285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 3.612594662868285""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 3.612594662868285
""",
)

entry(
    index = 411,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.55759e-07,'m^3/(mol*s)'), n=3.32068, w0=(327000,'J/mol'), E0=(59143,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 412,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(9.81457e-05,'m^3/(mol*s)'), n=3.18096, w0=(327000,'J/mol'), E0=(65771.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0005667364245684885, var=0.7364344330579138, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 1.7218025645289186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.7218025645289186""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.7218025645289186
""",
)

entry(
    index = 413,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(9.47164e-05,'m^3/(mol*s)'), n=2.93355, w0=(327000,'J/mol'), E0=(59404.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0013877744269917447, var=7.064085874733603, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 5.3317415429975785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 5.3317415429975785""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 5.3317415429975785
""",
)

entry(
    index = 414,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(6.70266e-07,'m^3/(mol*s)'), n=3.70279, w0=(327000,'J/mol'), E0=(53075.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 415,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.26481e-07,'m^3/(mol*s)'), n=3.88187, w0=(327000,'J/mol'), E0=(67376.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 416,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(4.78552e-08,'m^3/(mol*s)'), n=4.56733, w0=(327000,'J/mol'), E0=(57012.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 417,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0989309,'m^3/(mol*s)'), n=1.11534, w0=(327000,'J/mol'), E0=(61819.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 418,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0246274,'m^3/(mol*s)'), n=2.41869, w0=(327000,'J/mol'), E0=(60667.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.037388666409569574, var=2.776227954081066, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.4342342760511633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.4342342760511633""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.4342342760511633
""",
)

entry(
    index = 419,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0111426,'m^3/(mol*s)'), n=2.37373, w0=(327000,'J/mol'), E0=(66274.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027034236350043574, var=3.9934659584963574, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.074119277768116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.074119277768116""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.074119277768116
""",
)

entry(
    index = 420,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.91371e-05,'m^3/(mol*s)'), n=3.55919, w0=(327000,'J/mol'), E0=(56381.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 421,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.96396,'m^3/(mol*s)'), n=1.14461, w0=(327000,'J/mol'), E0=(65812.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07459030924954256, var=5.2367649311182, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.775044370763584"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.775044370763584""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.775044370763584
""",
)

entry(
    index = 422,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(1.89935e-05,'m^3/(mol*s)'), n=3.24194, w0=(327000,'J/mol'), E0=(70374.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013271229292477107, var=2.6884219960299403, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 3.3203902495944444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 3.3203902495944444""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 3.3203902495944444
""",
)

entry(
    index = 423,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br",
    kinetics = ArrheniusBM(A=(4.79164e-05,'m^3/(mol*s)'), n=3.22155, w0=(327000,'J/mol'), E0=(73744.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 424,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br",
    kinetics = ArrheniusBM(A=(0.00314625,'m^3/(mol*s)'), n=2.729, w0=(327000,'J/mol'), E0=(72045.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007061887251767618, var=0.5493886460284599, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br
    Total Standard Deviation in ln(k): 1.5036682291522498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br
Total Standard Deviation in ln(k): 1.5036682291522498""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br
Total Standard Deviation in ln(k): 1.5036682291522498
""",
)

entry(
    index = 425,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.76802e+13,'m^3/(mol*s)'), n=-2.06176, w0=(327000,'J/mol'), E0=(101212,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20562581603515095, var=15.763892354573805, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R
    Total Standard Deviation in ln(k): 8.47620152659888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R
Total Standard Deviation in ln(k): 8.47620152659888""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R
Total Standard Deviation in ln(k): 8.47620152659888
""",
)

entry(
    index = 426,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C",
    kinetics = ArrheniusBM(A=(3.56063,'m^3/(mol*s)'), n=2.01448, w0=(299500,'J/mol'), E0=(39325.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 427,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C",
    kinetics = ArrheniusBM(A=(1.57474,'m^3/(mol*s)'), n=2.23169, w0=(299500,'J/mol'), E0=(37513.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 428,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(4.89453e+09,'m^3/(mol*s)'), n=-0.85018, w0=(299500,'J/mol'), E0=(68542.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1683424007002336, var=2.6891432174839047, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl
    Total Standard Deviation in ln(k): 3.7104571857570456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl
Total Standard Deviation in ln(k): 3.7104571857570456""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl
Total Standard Deviation in ln(k): 3.7104571857570456
""",
)

entry(
    index = 429,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(5.3191e+07,'m^3/(mol*s)'), n=-0.164172, w0=(299500,'J/mol'), E0=(62303.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11322603213444594, var=4.477300189464976, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 4.526433132248803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 4.526433132248803""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 4.526433132248803
""",
)

entry(
    index = 430,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C",
    kinetics = ArrheniusBM(A=(7.87113e+14,'m^3/(mol*s)'), n=-2.08655, w0=(299500,'J/mol'), E0=(66840.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.241653770328508, var=10.75104638083491, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C
    Total Standard Deviation in ln(k): 7.180453681931535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C
Total Standard Deviation in ln(k): 7.180453681931535""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C
Total Standard Deviation in ln(k): 7.180453681931535
""",
)

entry(
    index = 431,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(4.2896e+07,'m^3/(mol*s)'), n=-0.181883, w0=(299500,'J/mol'), E0=(57720.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03742160884200184, var=4.503136422525098, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C
    Total Standard Deviation in ln(k): 4.348191212016156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C
Total Standard Deviation in ln(k): 4.348191212016156""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C
Total Standard Deviation in ln(k): 4.348191212016156
""",
)

entry(
    index = 432,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1",
    kinetics = ArrheniusBM(A=(1.34085e-05,'m^3/(mol*s)'), n=3.63224, w0=(299500,'J/mol'), E0=(-15932.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.053073385070242805, var=8.422429074796872, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1
    Total Standard Deviation in ln(k): 5.951376386956211"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1
Total Standard Deviation in ln(k): 5.951376386956211""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1
Total Standard Deviation in ln(k): 5.951376386956211
""",
)

entry(
    index = 433,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.10817e+13,'m^3/(mol*s)'), n=-1.66962, w0=(299500,'J/mol'), E0=(76423.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04485846229948748, var=21.961954554774923, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1
    Total Standard Deviation in ln(k): 9.507616667371517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1
Total Standard Deviation in ln(k): 9.507616667371517""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1
Total Standard Deviation in ln(k): 9.507616667371517
""",
)

entry(
    index = 434,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.057352,'m^3/(mol*s)'), n=2.53406, w0=(299500,'J/mol'), E0=(37077.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 435,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(215.121,'m^3/(mol*s)'), n=1.19164, w0=(299500,'J/mol'), E0=(53663.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 436,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O",
    kinetics = ArrheniusBM(A=(0.0073974,'m^3/(mol*s)'), n=2.79522, w0=(299500,'J/mol'), E0=(-5207.91,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00628541020401013, var=2.4129450672143276, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O
    Total Standard Deviation in ln(k): 3.129879239464793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O
Total Standard Deviation in ln(k): 3.129879239464793""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O
Total Standard Deviation in ln(k): 3.129879239464793
""",
)

entry(
    index = 437,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O",
    kinetics = ArrheniusBM(A=(0.446215,'m^3/(mol*s)'), n=2.42573, w0=(299500,'J/mol'), E0=(38886.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 438,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O",
    kinetics = ArrheniusBM(A=(208.569,'m^3/(mol*s)'), n=1.5036, w0=(299500,'J/mol'), E0=(65386.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 439,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O",
    kinetics = ArrheniusBM(A=(33.1951,'m^3/(mol*s)'), n=1.53476, w0=(299500,'J/mol'), E0=(61327.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 440,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.186883,'m^3/(mol*s)'), n=2.60235, w0=(299500,'J/mol'), E0=(41199.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 441,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.99217e+07,'m^3/(mol*s)'), n=0.0920123, w0=(299500,'J/mol'), E0=(61095,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13393234935575554, var=1.9607681083711497, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 3.143692442858543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 3.143692442858543""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 3.143692442858543
""",
)

entry(
    index = 442,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.558006,'m^3/(mol*s)'), n=2.23525, w0=(299500,'J/mol'), E0=(44792.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 443,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(34.7818,'m^3/(mol*s)'), n=1.42177, w0=(299500,'J/mol'), E0=(59767.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 444,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(23676,'m^3/(mol*s)'), n=0.689867, w0=(315136,'J/mol'), E0=(59743.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07224407338963691, var=14.518161969528013, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 7.820100878605934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 7.820100878605934""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 7.820100878605934
""",
)

entry(
    index = 445,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.90905e-11,'m^3/(mol*s)'), n=5.10745, w0=(327000,'J/mol'), E0=(48483.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2418145222164146, var=4.425407795329621, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 4.824865842510102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 4.824865842510102""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 4.824865842510102
""",
)

entry(
    index = 446,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000188015,'m^3/(mol*s)'), n=3.18635, w0=(327000,'J/mol'), E0=(60447.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0032007629276661616, var=1.0299911987240895, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.04261731692462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.04261731692462""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.04261731692462
""",
)

entry(
    index = 447,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C",
    kinetics = ArrheniusBM(A=(0.000141709,'m^3/(mol*s)'), n=3.34347, w0=(327000,'J/mol'), E0=(67808.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010803452893020033, var=0.09744382221526766, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C
    Total Standard Deviation in ln(k): 0.6285123978481912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C
Total Standard Deviation in ln(k): 0.6285123978481912""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C
Total Standard Deviation in ln(k): 0.6285123978481912
""",
)

entry(
    index = 448,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(0.000303344,'m^3/(mol*s)'), n=2.9787, w0=(327000,'J/mol'), E0=(64217.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.015777799752177843, var=1.3809568105004677, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 2.3954894723671676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 2.3954894723671676""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 2.3954894723671676
""",
)

entry(
    index = 449,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C",
    kinetics = ArrheniusBM(A=(0.000127332,'m^3/(mol*s)'), n=3.32351, w0=(327000,'J/mol'), E0=(63946.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011853097761675832, var=1.5826400416612756, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C
    Total Standard Deviation in ln(k): 2.5517989688825007"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C
Total Standard Deviation in ln(k): 2.5517989688825007""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C
Total Standard Deviation in ln(k): 2.5517989688825007
""",
)

entry(
    index = 450,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C",
    kinetics = ArrheniusBM(A=(1130.32,'m^3/(mol*s)'), n=1.6362, w0=(283500,'J/mol'), E0=(42748,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 451,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.64552e-12,'m^3/(mol*s)'), n=5.08844, w0=(299500,'J/mol'), E0=(10451,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12298135103417608, var=2.1269294907247347, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.2327032713844672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.2327032713844672""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.2327032713844672
""",
)

entry(
    index = 452,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00117601,'m^3/(mol*s)'), n=2.72514, w0=(299500,'J/mol'), E0=(31090.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03507905107009192, var=0.18495333722780122, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 0.9502987273201745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 0.9502987273201745""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 0.9502987273201745
""",
)

entry(
    index = 453,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.47383e-08,'m^3/(mol*s)'), n=4.03904, w0=(299500,'J/mol'), E0=(21110.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 454,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O",
    kinetics = ArrheniusBM(A=(1.50953e+07,'m^3/(mol*s)'), n=-0.202874, w0=(299500,'J/mol'), E0=(61583.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009391703132074774, var=19.544209976885266, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O
    Total Standard Deviation in ln(k): 8.886297255606834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O
Total Standard Deviation in ln(k): 8.886297255606834""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O
Total Standard Deviation in ln(k): 8.886297255606834
""",
)

entry(
    index = 455,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O",
    kinetics = ArrheniusBM(A=(1.96676e-07,'m^3/(mol*s)'), n=3.78178, w0=(296818,'J/mol'), E0=(-5182.09,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6715222174120079, var=0.09247513080522006, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O
    Total Standard Deviation in ln(k): 2.296876154378071"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O
Total Standard Deviation in ln(k): 2.296876154378071""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O
Total Standard Deviation in ln(k): 2.296876154378071
""",
)

entry(
    index = 456,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.42264,'m^3/(mol*s)'), n=1.33562, w0=(299500,'J/mol'), E0=(65555.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04702374548669442, var=8.49320032522501, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 5.9605687547180555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.9605687547180555""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.9605687547180555
""",
)

entry(
    index = 457,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.027169,'m^3/(mol*s)'), n=1.73665, w0=(299500,'J/mol'), E0=(50092.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 458,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.0567875,'m^3/(mol*s)'), n=1.80944, w0=(299500,'J/mol'), E0=(58017.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 459,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(0.0159833,'m^3/(mol*s)'), n=2.03281, w0=(299500,'J/mol'), E0=(54087.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09924910259451426, var=8.093824075404298, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 5.952770108291853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.952770108291853""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.952770108291853
""",
)

entry(
    index = 460,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(0.00205139,'m^3/(mol*s)'), n=2.91659, w0=(299500,'J/mol'), E0=(57268.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 461,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.0245699,'m^3/(mol*s)'), n=2.26037, w0=(299500,'J/mol'), E0=(44801.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0046254217501974304, var=0.3458674362593308, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 1.1906162920370769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.1906162920370769""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.1906162920370769
""",
)

entry(
    index = 462,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.000495128,'m^3/(mol*s)'), n=2.66142, w0=(299500,'J/mol'), E0=(41881.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 463,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000430651,'m^3/(mol*s)'), n=2.78666, w0=(299500,'J/mol'), E0=(58984,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 464,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.112234,'m^3/(mol*s)'), n=2.09111, w0=(299500,'J/mol'), E0=(45715.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010344159293620139, var=2.805686560641288, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.3839584440519825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.3839584440519825""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.3839584440519825
""",
)

entry(
    index = 465,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0547955,'m^3/(mol*s)'), n=1.74792, w0=(299500,'J/mol'), E0=(53685.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 466,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(220.761,'m^3/(mol*s)'), n=1.59458, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 467,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(47.5838,'m^3/(mol*s)'), n=1.77045, w0=(272000,'J/mol'), E0=(13727.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11354911717072118, var=0.0006155904837598917, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 0.3350389637946271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.3350389637946271""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.3350389637946271
""",
)

entry(
    index = 468,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.56317e-09,'m^3/(mol*s)'), n=4.84597, w0=(377500,'J/mol'), E0=(6269.66,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16923099446050444, var=0.42989422923808795, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R',), comment="""BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.7396345156971387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.7396345156971387""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.7396345156971387
""",
)

entry(
    index = 469,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(30.3495,'m^3/(mol*s)'), n=1.95189, w0=(377500,'J/mol'), E0=(78264.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 470,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2771.65,'m^3/(mol*s)'), n=1.35855, w0=(377500,'J/mol'), E0=(58239.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0011516249778903095, var=6.154159275731674, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 4.9761557157172875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.9761557157172875""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.9761557157172875
""",
)

entry(
    index = 471,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(24.8273,'m^3/(mol*s)'), n=1.88378, w0=(377500,'J/mol'), E0=(61645.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 472,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(17440.8,'m^3/(mol*s)'), n=0.915521, w0=(377500,'J/mol'), E0=(60370.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 473,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O",
    kinetics = ArrheniusBM(A=(185.874,'m^3/(mol*s)'), n=1.75948, w0=(377500,'J/mol'), E0=(71729.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 474,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O",
    kinetics = ArrheniusBM(A=(84.18,'m^3/(mol*s)'), n=1.82792, w0=(377500,'J/mol'), E0=(63716.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 475,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O",
    kinetics = ArrheniusBM(A=(52.0355,'m^3/(mol*s)'), n=1.85451, w0=(377500,'J/mol'), E0=(76275.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 476,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O",
    kinetics = ArrheniusBM(A=(40.2856,'m^3/(mol*s)'), n=1.90639, w0=(377500,'J/mol'), E0=(65898.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 477,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(6.6831e-18,'m^3/(mol*s)'), n=6.77359, w0=(377500,'J/mol'), E0=(-25245,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22209298624590354, var=2.623546206583656, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 3.8051650801685306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 3.8051650801685306""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 3.8051650801685306
""",
)

entry(
    index = 478,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.00141887,'m^3/(mol*s)'), n=2.48484, w0=(377500,'J/mol'), E0=(65659.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 479,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000115063,'m^3/(mol*s)'), n=2.71663, w0=(377500,'J/mol'), E0=(44852.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 480,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O",
    kinetics = ArrheniusBM(A=(3.86512e-05,'m^3/(mol*s)'), n=3.18148, w0=(377500,'J/mol'), E0=(59686.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012246755359862062, var=3.6963106529154115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O
    Total Standard Deviation in ln(k): 3.8850326370188215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O
Total Standard Deviation in ln(k): 3.8850326370188215""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O
Total Standard Deviation in ln(k): 3.8850326370188215
""",
)

entry(
    index = 481,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O",
    kinetics = ArrheniusBM(A=(3.24197e-07,'m^3/(mol*s)'), n=3.47473, w0=(377500,'J/mol'), E0=(54197.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 482,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.004014,'m^3/(mol*s)'), n=2.48483, w0=(377500,'J/mol'), E0=(58218,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004263454747417353, var=1.5635386634433621, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 2.5174638042457773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 2.5174638042457773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 2.5174638042457773
""",
)

entry(
    index = 483,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.000869642,'m^3/(mol*s)'), n=2.59617, w0=(377500,'J/mol'), E0=(52044.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 484,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.312416,'m^3/(mol*s)'), n=1.69659, w0=(377500,'J/mol'), E0=(49915.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 485,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00346267,'m^3/(mol*s)'), n=2.45062, w0=(377500,'J/mol'), E0=(60623.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025666391813760008, var=1.4357686729071073, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 2.466633460161851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.466633460161851""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.466633460161851
""",
)

entry(
    index = 486,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.000166848,'m^3/(mol*s)'), n=2.71783, w0=(377500,'J/mol'), E0=(56997.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 487,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(7.19971e-05,'m^3/(mol*s)'), n=3.05189, w0=(377500,'J/mol'), E0=(58434.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0026625192547315023, var=2.1691094933399926, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 2.9592429152632334"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 2.9592429152632334""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 2.9592429152632334
""",
)

entry(
    index = 488,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000554304,'m^3/(mol*s)'), n=2.72146, w0=(377500,'J/mol'), E0=(55665.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 489,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.04932e-06,'m^3/(mol*s)'), n=3.26105, w0=(377500,'J/mol'), E0=(41974.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 490,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C",
    kinetics = ArrheniusBM(A=(52.6319,'m^3/(mol*s)'), n=1.37633, w0=(377500,'J/mol'), E0=(66897.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07771694622863495, var=1.14627050650708, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C
    Total Standard Deviation in ln(k): 2.341618737598739"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C
Total Standard Deviation in ln(k): 2.341618737598739""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C
Total Standard Deviation in ln(k): 2.341618737598739
""",
)

entry(
    index = 491,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C",
    kinetics = ArrheniusBM(A=(8.88686e-05,'m^3/(mol*s)'), n=3.02721, w0=(377500,'J/mol'), E0=(42645.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 492,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00335891,'m^3/(mol*s)'), n=2.58664, w0=(377500,'J/mol'), E0=(61882.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0015265106518631804, var=0.025371659229652257, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 0.32315935349922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 0.32315935349922""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 0.32315935349922
""",
)

entry(
    index = 493,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0235932,'m^3/(mol*s)'), n=2.3902, w0=(377500,'J/mol'), E0=(54542.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 494,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.14379e-05,'m^3/(mol*s)'), n=3.22757, w0=(327000,'J/mol'), E0=(60388.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 495,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.50944e-06,'m^3/(mol*s)'), n=3.29154, w0=(327000,'J/mol'), E0=(41347.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 496,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.97135e-06,'m^3/(mol*s)'), n=3.55842, w0=(327000,'J/mol'), E0=(56449.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 497,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.10313e+11,'m^3/(mol*s)'), n=-1.73732, w0=(327000,'J/mol'), E0=(86267.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16970762460859162, var=9.223631066282126, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 6.514867991754647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 6.514867991754647""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 6.514867991754647
""",
)

entry(
    index = 498,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(69.4029,'m^3/(mol*s)'), n=1.03123, w0=(327000,'J/mol'), E0=(74361.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1267130345163794, var=5.737890490630677, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 5.120495660066896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.120495660066896""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.120495660066896
""",
)

entry(
    index = 499,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C",
    kinetics = ArrheniusBM(A=(8.70581e-05,'m^3/(mol*s)'), n=2.78977, w0=(327000,'J/mol'), E0=(66038.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01598606041054954, var=3.4905854283770563, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
    Total Standard Deviation in ln(k): 3.785634275336158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
Total Standard Deviation in ln(k): 3.785634275336158""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
Total Standard Deviation in ln(k): 3.785634275336158
""",
)

entry(
    index = 500,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C",
    kinetics = ArrheniusBM(A=(2.65851e-05,'m^3/(mol*s)'), n=2.68716, w0=(327000,'J/mol'), E0=(46503.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 501,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C",
    kinetics = ArrheniusBM(A=(5.6833e-08,'m^3/(mol*s)'), n=4.04124, w0=(327000,'J/mol'), E0=(55605.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 502,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.19448e-05,'m^3/(mol*s)'), n=3.35979, w0=(327000,'J/mol'), E0=(61032.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 503,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F",
    kinetics = ArrheniusBM(A=(0.00082385,'m^3/(mol*s)'), n=2.68492, w0=(327000,'J/mol'), E0=(60060.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013639845513329722, var=6.65702229363011, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F
    Total Standard Deviation in ln(k): 5.206729232782531"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F
Total Standard Deviation in ln(k): 5.206729232782531""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F
Total Standard Deviation in ln(k): 5.206729232782531
""",
)

entry(
    index = 504,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F",
    kinetics = ArrheniusBM(A=(8.51382e-08,'m^3/(mol*s)'), n=3.50006, w0=(327000,'J/mol'), E0=(56984.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 505,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(8.64884e-07,'m^3/(mol*s)'), n=3.81209, w0=(327000,'J/mol'), E0=(51809.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.040416048844219385, var=1.6183821905418572, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 2.6518846445795092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.6518846445795092""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.6518846445795092
""",
)

entry(
    index = 506,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(8.22643e-05,'m^3/(mol*s)'), n=3.18139, w0=(327000,'J/mol'), E0=(53718.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004491684296420335, var=0.06842548686099835, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 0.5356895686626414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 0.5356895686626414""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 0.5356895686626414
""",
)

entry(
    index = 507,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000758851,'m^3/(mol*s)'), n=2.6134, w0=(327000,'J/mol'), E0=(56903.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013326294221134611, var=11.66409188397504, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 6.880201384684057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 6.880201384684057""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 6.880201384684057
""",
)

entry(
    index = 508,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(6.07137e-05,'m^3/(mol*s)'), n=3.23507, w0=(327000,'J/mol'), E0=(62094.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0017943508312125444, var=1.8155054532096786, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 2.705702368806504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 2.705702368806504""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 2.705702368806504
""",
)

entry(
    index = 509,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.00631513,'m^3/(mol*s)'), n=2.38245, w0=(327000,'J/mol'), E0=(65613.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01915347299479003, var=4.586430142145006, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 4.341455389246147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 4.341455389246147""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 4.341455389246147
""",
)

entry(
    index = 510,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.59038,'m^3/(mol*s)'), n=1.43836, w0=(327000,'J/mol'), E0=(59099,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06684288139738132, var=4.004366603873951, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.179604967025601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.179604967025601""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.179604967025601
""",
)

entry(
    index = 511,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00751368,'m^3/(mol*s)'), n=1.99102, w0=(327000,'J/mol'), E0=(61357.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02214310399640412, var=11.414691157707741, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.828760650145386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.828760650145386""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.828760650145386
""",
)

entry(
    index = 512,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C",
    kinetics = ArrheniusBM(A=(0.00178376,'m^3/(mol*s)'), n=2.34747, w0=(327000,'J/mol'), E0=(66060.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 513,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C",
    kinetics = ArrheniusBM(A=(0.00204844,'m^3/(mol*s)'), n=2.00995, w0=(327000,'J/mol'), E0=(73933.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 514,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00092309,'m^3/(mol*s)'), n=2.85351, w0=(327000,'J/mol'), E0=(73155.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0048783426610703225, var=0.39556529395673684, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C
    Total Standard Deviation in ln(k): 1.273114855948801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C
Total Standard Deviation in ln(k): 1.273114855948801""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C
Total Standard Deviation in ln(k): 1.273114855948801
""",
)

entry(
    index = 515,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.62705e-06,'m^3/(mol*s)'), n=3.21493, w0=(327000,'J/mol'), E0=(70401.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005705093171151363, var=4.244091390269874, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.144327761179358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.144327761179358""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.144327761179358
""",
)

entry(
    index = 516,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C",
    kinetics = ArrheniusBM(A=(0.0152471,'m^3/(mol*s)'), n=2.47636, w0=(327000,'J/mol'), E0=(72659,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01325755230977195, var=0.11457385808383035, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C
    Total Standard Deviation in ln(k): 0.7118884060066712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C
Total Standard Deviation in ln(k): 0.7118884060066712""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C
Total Standard Deviation in ln(k): 0.7118884060066712
""",
)

entry(
    index = 517,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C",
    kinetics = ArrheniusBM(A=(7.07718e-05,'m^3/(mol*s)'), n=3.38784, w0=(327000,'J/mol'), E0=(70126.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 518,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00423821,'m^3/(mol*s)'), n=2.23356, w0=(327000,'J/mol'), E0=(67079.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 519,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.6121,'m^3/(mol*s)'), n=2.01077, w0=(327000,'J/mol'), E0=(72876.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008426724208837088, var=0.4944011300536491, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 1.4307753539470824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.4307753539470824""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.4307753539470824
""",
)

entry(
    index = 520,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(2.68906e+11,'m^3/(mol*s)'), n=-1.42097, w0=(299500,'J/mol'), E0=(68353.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5316007770156629, var=7.77830872230957, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R
    Total Standard Deviation in ln(k): 6.9268101819187935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R
Total Standard Deviation in ln(k): 6.9268101819187935""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R
Total Standard Deviation in ln(k): 6.9268101819187935
""",
)

entry(
    index = 521,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C",
    kinetics = ArrheniusBM(A=(19.9098,'m^3/(mol*s)'), n=1.76121, w0=(299500,'J/mol'), E0=(36353.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3707181430981072e-16, var=0.0031729214271064565, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C
    Total Standard Deviation in ln(k): 0.11292410266393599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C
Total Standard Deviation in ln(k): 0.11292410266393599""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C
Total Standard Deviation in ln(k): 0.11292410266393599
""",
)

entry(
    index = 522,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.0846e+07,'m^3/(mol*s)'), n=-0.200472, w0=(299500,'J/mol'), E0=(67937.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10094688934033727, var=4.9928017519875025, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C
    Total Standard Deviation in ln(k): 4.7331313722433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C
Total Standard Deviation in ln(k): 4.7331313722433""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C
Total Standard Deviation in ln(k): 4.7331313722433
""",
)

entry(
    index = 523,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(1.57952,'m^3/(mol*s)'), n=2.43229, w0=(299500,'J/mol'), E0=(29816.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 524,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(398.23,'m^3/(mol*s)'), n=1.63639, w0=(299500,'J/mol'), E0=(54798.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 525,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O",
    kinetics = ArrheniusBM(A=(4.69543,'m^3/(mol*s)'), n=2.03929, w0=(299500,'J/mol'), E0=(45777.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 526,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O",
    kinetics = ArrheniusBM(A=(6674.28,'m^3/(mol*s)'), n=0.996546, w0=(299500,'J/mol'), E0=(59537.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 527,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O",
    kinetics = ArrheniusBM(A=(0.157359,'m^3/(mol*s)'), n=2.34331, w0=(299500,'J/mol'), E0=(34188.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 528,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O",
    kinetics = ArrheniusBM(A=(4.54705,'m^3/(mol*s)'), n=2.29539, w0=(299500,'J/mol'), E0=(43737.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 529,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O",
    kinetics = ArrheniusBM(A=(290.458,'m^3/(mol*s)'), n=1.65322, w0=(299500,'J/mol'), E0=(51387.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 530,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O",
    kinetics = ArrheniusBM(A=(244.231,'m^3/(mol*s)'), n=1.41374, w0=(299500,'J/mol'), E0=(64203,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 531,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C",
    kinetics = ArrheniusBM(A=(0.176621,'m^3/(mol*s)'), n=2.47253, w0=(299500,'J/mol'), E0=(43850.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 532,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C",
    kinetics = ArrheniusBM(A=(0.722892,'m^3/(mol*s)'), n=2.37337, w0=(299500,'J/mol'), E0=(39683.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 533,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(26.7714,'m^3/(mol*s)'), n=1.82744, w0=(299500,'J/mol'), E0=(46180.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 534,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R",
    kinetics = ArrheniusBM(A=(48.9307,'m^3/(mol*s)'), n=1.947, w0=(299500,'J/mol'), E0=(69755.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 535,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(1.84584e+17,'m^3/(mol*s)'), n=-2.71954, w0=(305250,'J/mol'), E0=(77669.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09670136353310002, var=81.99922959941304, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F
    Total Standard Deviation in ln(k): 18.396531197686027"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F
Total Standard Deviation in ln(k): 18.396531197686027""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F
Total Standard Deviation in ln(k): 18.396531197686027
""",
)

entry(
    index = 536,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(0.0183448,'m^3/(mol*s)'), n=2.40872, w0=(317333,'J/mol'), E0=(48736,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12262372124177995, var=10.312728099511025, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 6.745993081913186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F
Total Standard Deviation in ln(k): 6.745993081913186""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F
Total Standard Deviation in ln(k): 6.745993081913186
""",
)

entry(
    index = 537,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.59132e-28,'m^3/(mol*s)'), n=10.0565, w0=(327000,'J/mol'), E0=(6106.78,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12427451511698356, var=11.008776079220768, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.963853404542852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.963853404542852""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.963853404542852
""",
)

entry(
    index = 538,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(6.19596e-05,'m^3/(mol*s)'), n=3.36562, w0=(327000,'J/mol'), E0=(65231.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010531440489724964, var=1.5165851534632764, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 2.4714715622218555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 2.4714715622218555""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 2.4714715622218555
""",
)

entry(
    index = 539,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.00472731,'m^3/(mol*s)'), n=2.8542, w0=(327000,'J/mol'), E0=(75064.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 540,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.0378904,'m^3/(mol*s)'), n=2.66351, w0=(327000,'J/mol'), E0=(68135,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 541,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C",
    kinetics = ArrheniusBM(A=(4.31904e-05,'m^3/(mol*s)'), n=3.35456, w0=(327000,'J/mol'), E0=(59370.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011532587001041648, var=1.563168874424618, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
    Total Standard Deviation in ln(k): 2.5354315050104765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
Total Standard Deviation in ln(k): 2.5354315050104765""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
Total Standard Deviation in ln(k): 2.5354315050104765
""",
)

entry(
    index = 542,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C",
    kinetics = ArrheniusBM(A=(0.0090139,'m^3/(mol*s)'), n=2.78658, w0=(327000,'J/mol'), E0=(65454.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 543,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00717719,'m^3/(mol*s)'), n=2.80408, w0=(327000,'J/mol'), E0=(70434.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 544,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.000185212,'m^3/(mol*s)'), n=3.05362, w0=(327000,'J/mol'), E0=(64817.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.018784091115384365, var=2.07480876421275, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.9348560046460626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R
Total Standard Deviation in ln(k): 2.9348560046460626""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R
Total Standard Deviation in ln(k): 2.9348560046460626
""",
)

entry(
    index = 545,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00666669,'m^3/(mol*s)'), n=2.45517, w0=(327000,'J/mol'), E0=(57089.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.758164782697057e-05, var=0.009391293821763817, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.19437067251157095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.19437067251157095""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.19437067251157095
""",
)

entry(
    index = 546,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.92936e-05,'m^3/(mol*s)'), n=3.40391, w0=(327000,'J/mol'), E0=(57708,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011835072555620416, var=2.7751872901510297, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.3694031563702156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.3694031563702156""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.3694031563702156
""",
)

entry(
    index = 547,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C",
    kinetics = ArrheniusBM(A=(0.000590108,'m^3/(mol*s)'), n=3.10871, w0=(327000,'J/mol'), E0=(72444.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0005762316498945033, var=0.5137139763873364, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C
    Total Standard Deviation in ln(k): 1.4383184892420449"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C
Total Standard Deviation in ln(k): 1.4383184892420449""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C
Total Standard Deviation in ln(k): 1.4383184892420449
""",
)

entry(
    index = 548,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C",
    kinetics = ArrheniusBM(A=(0.0105112,'m^3/(mol*s)'), n=2.86655, w0=(327000,'J/mol'), E0=(71590.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 549,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.02649e-14,'m^3/(mol*s)'), n=5.47731, w0=(299500,'J/mol'), E0=(5343.85,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10327277343801901, var=5.117461924800162, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.794552510548998"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.794552510548998""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.794552510548998
""",
)

entry(
    index = 550,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(4.60523e-05,'m^3/(mol*s)'), n=3.14472, w0=(299500,'J/mol'), E0=(22767.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 551,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(4.26272e-05,'m^3/(mol*s)'), n=3.13411, w0=(299500,'J/mol'), E0=(24203.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07391047925475314, var=0.10655074060176453, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 0.840092569576954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 0.840092569576954""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 0.840092569576954
""",
)

entry(
    index = 552,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.20565e-06,'m^3/(mol*s)'), n=3.17637, w0=(299500,'J/mol'), E0=(23479.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 553,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O",
    kinetics = ArrheniusBM(A=(1.12386e-09,'m^3/(mol*s)'), n=4.51687, w0=(299500,'J/mol'), E0=(9672.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012780955507016026, var=0.2726412336191488, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O
    Total Standard Deviation in ln(k): 1.0788865473568694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O
Total Standard Deviation in ln(k): 1.0788865473568694""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O
Total Standard Deviation in ln(k): 1.0788865473568694
""",
)

entry(
    index = 554,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O",
    kinetics = ArrheniusBM(A=(0.00135502,'m^3/(mol*s)'), n=2.64458, w0=(288770,'J/mol'), E0=(11892.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 555,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(7.25794e-05,'m^3/(mol*s)'), n=2.83709, w0=(299500,'J/mol'), E0=(53785.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002181999163932156, var=3.940713576849172, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 3.9851282481050263"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 3.9851282481050263""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 3.9851282481050263
""",
)

entry(
    index = 556,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(0.00890658,'m^3/(mol*s)'), n=1.76738, w0=(299500,'J/mol'), E0=(58819.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 557,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C",
    kinetics = ArrheniusBM(A=(1.69473e-12,'m^3/(mol*s)'), n=4.91954, w0=(299500,'J/mol'), E0=(6177.65,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1534907768906506, var=3.2327755144969657, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C
    Total Standard Deviation in ln(k): 3.9901530070465836"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C
Total Standard Deviation in ln(k): 3.9901530070465836""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C
Total Standard Deviation in ln(k): 3.9901530070465836
""",
)

entry(
    index = 558,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(12.64,'m^3/(mol*s)'), n=1.16704, w0=(299500,'J/mol'), E0=(72538,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004236215765055897, var=30.91165747769297, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C
    Total Standard Deviation in ln(k): 11.156620581340114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C
Total Standard Deviation in ln(k): 11.156620581340114""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C
Total Standard Deviation in ln(k): 11.156620581340114
""",
)

entry(
    index = 559,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C",
    kinetics = ArrheniusBM(A=(0.00054819,'m^3/(mol*s)'), n=2.65512, w0=(299500,'J/mol'), E0=(36457.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 560,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C",
    kinetics = ArrheniusBM(A=(4.61982,'m^3/(mol*s)'), n=1.59815, w0=(299500,'J/mol'), E0=(48938,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 561,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000447245,'m^3/(mol*s)'), n=2.63852, w0=(299500,'J/mol'), E0=(32744.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 562,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(153.79,'m^3/(mol*s)'), n=1.59378, w0=(272000,'J/mol'), E0=(16090.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 563,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(234.788,'m^3/(mol*s)'), n=1.5918, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 564,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.44069e-10,'m^3/(mol*s)'), n=5.1577, w0=(377500,'J/mol'), E0=(26342.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18057989634763746, var=0.2351099251571485, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 1.4257769865158252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 1.4257769865158252""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 1.4257769865158252
""",
)

entry(
    index = 565,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(41.157,'m^3/(mol*s)'), n=1.86255, w0=(377500,'J/mol'), E0=(59848.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 566,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(163.845,'m^3/(mol*s)'), n=1.8839, w0=(377500,'J/mol'), E0=(57829.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 567,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C",
    kinetics = ArrheniusBM(A=(9.73123e-07,'m^3/(mol*s)'), n=3.44059, w0=(377500,'J/mol'), E0=(63842.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17465372727007103, var=0.041649242317018935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C
    Total Standard Deviation in ln(k): 0.8479577219916961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 0.8479577219916961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 0.8479577219916961
""",
)

entry(
    index = 568,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.3526e-20,'m^3/(mol*s)'), n=7.3285, w0=(377500,'J/mol'), E0=(1435.77,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03416737245189578, var=5.421781891473801, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C
    Total Standard Deviation in ln(k): 4.7538171804015334"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.7538171804015334""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.7538171804015334
""",
)

entry(
    index = 569,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C",
    kinetics = ArrheniusBM(A=(6.12995e-05,'m^3/(mol*s)'), n=2.9629, w0=(377500,'J/mol'), E0=(37681.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 570,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.0131926,'m^3/(mol*s)'), n=2.28677, w0=(377500,'J/mol'), E0=(62877.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 571,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.0035867,'m^3/(mol*s)'), n=2.3426, w0=(377500,'J/mol'), E0=(52313.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 572,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000395983,'m^3/(mol*s)'), n=2.7051, w0=(377500,'J/mol'), E0=(46914.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 573,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.014512,'m^3/(mol*s)'), n=2.23618, w0=(377500,'J/mol'), E0=(63759.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017288378696116016, var=0.9247898788284611, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 1.9713115919329525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 1.9713115919329525""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 1.9713115919329525
""",
)

entry(
    index = 574,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000173475,'m^3/(mol*s)'), n=2.83304, w0=(377500,'J/mol'), E0=(46337,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 575,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C",
    kinetics = ArrheniusBM(A=(0.00129363,'m^3/(mol*s)'), n=2.78526, w0=(377500,'J/mol'), E0=(57233.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009442785061186669, var=2.622079199560084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C
    Total Standard Deviation in ln(k): 3.269960113794612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C
Total Standard Deviation in ln(k): 3.269960113794612""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C
Total Standard Deviation in ln(k): 3.269960113794612
""",
)

entry(
    index = 576,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C",
    kinetics = ArrheniusBM(A=(0.0443652,'m^3/(mol*s)'), n=2.13654, w0=(377500,'J/mol'), E0=(55189,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 577,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(0.0343176,'m^3/(mol*s)'), n=2.1924, w0=(377500,'J/mol'), E0=(57920.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 578,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.0395088,'m^3/(mol*s)'), n=2.19468, w0=(377500,'J/mol'), E0=(60231.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 579,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.61542e+11,'m^3/(mol*s)'), n=-1.82653, w0=(327000,'J/mol'), E0=(85717.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08933987895480945, var=28.997990045243558, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.019926714717096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.019926714717096""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.019926714717096
""",
)

entry(
    index = 580,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(3.65285e-05,'m^3/(mol*s)'), n=2.3486, w0=(327000,'J/mol'), E0=(36625.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 581,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(2.58609e-06,'m^3/(mol*s)'), n=3.6814, w0=(327000,'J/mol'), E0=(58662.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 582,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R",
    kinetics = ArrheniusBM(A=(12110.6,'m^3/(mol*s)'), n=0.263079, w0=(327000,'J/mol'), E0=(80194,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13249860811733777, var=10.351919138919147, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R
    Total Standard Deviation in ln(k): 6.783025586967024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R
Total Standard Deviation in ln(k): 6.783025586967024""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R
Total Standard Deviation in ln(k): 6.783025586967024
""",
)

entry(
    index = 583,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.07553e-07,'m^3/(mol*s)'), n=3.64601, w0=(327000,'J/mol'), E0=(55969.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 584,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(4.99796e-08,'m^3/(mol*s)'), n=3.80643, w0=(327000,'J/mol'), E0=(57983.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.043936944444036966, var=2.2145488249803615, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R
    Total Standard Deviation in ln(k): 3.093712819383289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R
Total Standard Deviation in ln(k): 3.093712819383289""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R
Total Standard Deviation in ln(k): 3.093712819383289
""",
)

entry(
    index = 585,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000306951,'m^3/(mol*s)'), n=2.72173, w0=(327000,'J/mol'), E0=(58367.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005285904319878661, var=8.000020612674026, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R
    Total Standard Deviation in ln(k): 5.683535542394534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.683535542394534""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.683535542394534
""",
)

entry(
    index = 586,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C",
    kinetics = ArrheniusBM(A=(4.11859e-07,'m^3/(mol*s)'), n=3.98655, w0=(327000,'J/mol'), E0=(51657.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 587,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C",
    kinetics = ArrheniusBM(A=(5.5308e-07,'m^3/(mol*s)'), n=3.71151, w0=(327000,'J/mol'), E0=(52252.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 588,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(9.20334e-05,'m^3/(mol*s)'), n=3.18628, w0=(327000,'J/mol'), E0=(57638.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 589,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(1.69419e-08,'m^3/(mol*s)'), n=4.32008, w0=(327000,'J/mol'), E0=(47886.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19250416686639124, var=2.085933304659664, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 3.3790696673601297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
Total Standard Deviation in ln(k): 3.3790696673601297""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
Total Standard Deviation in ln(k): 3.3790696673601297
""",
)

entry(
    index = 590,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.000570337,'m^3/(mol*s)'), n=2.91943, w0=(327000,'J/mol'), E0=(54032.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 591,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(0.00164798,'m^3/(mol*s)'), n=2.87921, w0=(327000,'J/mol'), E0=(62421,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 592,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.06492e-05,'m^3/(mol*s)'), n=3.25636, w0=(327000,'J/mol'), E0=(53125.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.3821454089912284e-05, var=0.9929280368368195, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 1.997769023588688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.997769023588688""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.997769023588688
""",
)

entry(
    index = 593,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0210199,'m^3/(mol*s)'), n=1.85566, w0=(327000,'J/mol'), E0=(62838,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 594,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.02819e-05,'m^3/(mol*s)'), n=3.37214, w0=(327000,'J/mol'), E0=(58104.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0007130791688094451, var=3.9019001153060513, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 3.961790537728531"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R
Total Standard Deviation in ln(k): 3.961790537728531""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R
Total Standard Deviation in ln(k): 3.961790537728531
""",
)

entry(
    index = 595,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R",
    kinetics = ArrheniusBM(A=(0.000171298,'m^3/(mol*s)'), n=3.19295, w0=(327000,'J/mol'), E0=(64742.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 596,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O",
    kinetics = ArrheniusBM(A=(0.00289119,'m^3/(mol*s)'), n=2.26603, w0=(327000,'J/mol'), E0=(70925.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 597,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O",
    kinetics = ArrheniusBM(A=(0.00307903,'m^3/(mol*s)'), n=2.45333, w0=(327000,'J/mol'), E0=(63609.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017723535669233077, var=4.466167154415403, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O
    Total Standard Deviation in ln(k): 4.2811999214841405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O
Total Standard Deviation in ln(k): 4.2811999214841405""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O
Total Standard Deviation in ln(k): 4.2811999214841405
""",
)

entry(
    index = 598,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0986609,'m^3/(mol*s)'), n=1.8044, w0=(327000,'J/mol'), E0=(53668.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07580719568033695, var=5.81780778180466, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.025917853647733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.025917853647733""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.025917853647733
""",
)

entry(
    index = 599,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C",
    kinetics = ArrheniusBM(A=(0.00177736,'m^3/(mol*s)'), n=1.98145, w0=(327000,'J/mol'), E0=(49732,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 600,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C",
    kinetics = ArrheniusBM(A=(0.00038912,'m^3/(mol*s)'), n=2.85908, w0=(327000,'J/mol'), E0=(70168.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 601,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(1.83044e-06,'m^3/(mol*s)'), n=2.67848, w0=(327000,'J/mol'), E0=(43863.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 602,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.54685e-09,'m^3/(mol*s)'), n=4.29667, w0=(327000,'J/mol'), E0=(53487.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 603,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(0.00129677,'m^3/(mol*s)'), n=2.78265, w0=(327000,'J/mol'), E0=(72995.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002643884290401819, var=0.07815466629399853, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 0.567089792640773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 0.567089792640773""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 0.567089792640773
""",
)

entry(
    index = 604,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.98204e-06,'m^3/(mol*s)'), n=3.27477, w0=(327000,'J/mol'), E0=(60498,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 605,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(5.29539e-07,'m^3/(mol*s)'), n=3.59832, w0=(327000,'J/mol'), E0=(71695.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00040626289392602447, var=14.496820689555653, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 7.63398755400886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 7.63398755400886""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 7.63398755400886
""",
)

entry(
    index = 606,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0346373,'m^3/(mol*s)'), n=2.32146, w0=(327000,'J/mol'), E0=(70188.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010097809568683471, var=0.1940036508253936, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R
    Total Standard Deviation in ln(k): 0.9083738962553685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 0.9083738962553685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 0.9083738962553685
""",
)

entry(
    index = 607,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00151048,'m^3/(mol*s)'), n=3.07958, w0=(327000,'J/mol'), E0=(65111.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 608,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(3.57521e+12,'m^3/(mol*s)'), n=-1.76616, w0=(299500,'J/mol'), E0=(72858.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09394774172035059, var=16.293133926427753, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R
    Total Standard Deviation in ln(k): 8.328113493182295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R
Total Standard Deviation in ln(k): 8.328113493182295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R
Total Standard Deviation in ln(k): 8.328113493182295
""",
)

entry(
    index = 609,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(101.399,'m^3/(mol*s)'), n=1.7102, w0=(299500,'J/mol'), E0=(47698,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 610,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(36.3899,'m^3/(mol*s)'), n=1.93252, w0=(299500,'J/mol'), E0=(55682.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 611,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(16652.4,'m^3/(mol*s)'), n=0.786827, w0=(299500,'J/mol'), E0=(62121.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04830961544580788, var=3.745848924473886, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 4.001384451277161"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 4.001384451277161""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 4.001384451277161
""",
)

entry(
    index = 612,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C",
    kinetics = ArrheniusBM(A=(0.0228759,'m^3/(mol*s)'), n=2.75, w0=(327000,'J/mol'), E0=(57517.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 613,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C",
    kinetics = ArrheniusBM(A=(8392.38,'m^3/(mol*s)'), n=1.46983, w0=(283500,'J/mol'), E0=(35138.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 614,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1.09971e-07,'m^3/(mol*s)'), n=4.16644, w0=(305250,'J/mol'), E0=(-14241.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1379759395160391, var=9.09718208213581, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 6.393261983830748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.393261983830748""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.393261983830748
""",
)

entry(
    index = 615,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(0.250839,'m^3/(mol*s)'), n=2.00671, w0=(320786,'J/mol'), E0=(55701.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006269284540063562, var=6.563414043678486, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 5.1517150188351675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 5.1517150188351675""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 5.1517150188351675
""",
)

entry(
    index = 616,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(8.80195e-07,'m^3/(mol*s)'), n=3.37306, w0=(327000,'J/mol'), E0=(55867.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0008480383458855596, var=3.7810410593732318, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 3.900317905232883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 3.900317905232883""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 3.900317905232883
""",
)

entry(
    index = 617,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.12103e-05,'m^3/(mol*s)'), n=3.55656, w0=(327000,'J/mol'), E0=(54850.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010550932663279564, var=8.377310107518321, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 5.805072646711127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.805072646711127""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.805072646711127
""",
)

entry(
    index = 618,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.0056062,'m^3/(mol*s)'), n=2.84217, w0=(327000,'J/mol'), E0=(76231.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 619,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.0141769,'m^3/(mol*s)'), n=2.76355, w0=(327000,'J/mol'), E0=(72170.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 620,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000308032,'m^3/(mol*s)'), n=3.12036, w0=(327000,'J/mol'), E0=(58242.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002724272561366101, var=0.11796843023677352, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.6954018930454385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.6954018930454385""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.6954018930454385
""",
)

entry(
    index = 621,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00433022,'m^3/(mol*s)'), n=2.75792, w0=(327000,'J/mol'), E0=(67824.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.003794796451540874, var=0.09709865513668728, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 0.6342232878302797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 0.6342232878302797""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 0.6342232878302797
""",
)

entry(
    index = 622,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000193888,'m^3/(mol*s)'), n=2.86662, w0=(327000,'J/mol'), E0=(64503.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00563682575007647, var=4.143579817895739, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.09495849471426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.09495849471426""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.09495849471426
""",
)

entry(
    index = 623,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(712.895,'m^3/(mol*s)'), n=1.00111, w0=(327000,'J/mol'), E0=(70088.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 624,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.64202e-06,'m^3/(mol*s)'), n=3.71674, w0=(327000,'J/mol'), E0=(54192.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0001977039584887095, var=8.501950863184254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.845924328998689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.845924328998689""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.845924328998689
""",
)

entry(
    index = 625,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O",
    kinetics = ArrheniusBM(A=(0.00435666,'m^3/(mol*s)'), n=2.88851, w0=(327000,'J/mol'), E0=(74278.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 626,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O",
    kinetics = ArrheniusBM(A=(0.00300542,'m^3/(mol*s)'), n=2.90586, w0=(327000,'J/mol'), E0=(76408.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 627,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1.19048e-05,'m^3/(mol*s)'), n=3.22184, w0=(299500,'J/mol'), E0=(43911.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 628,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(4.36525e-10,'m^3/(mol*s)'), n=4.21502, w0=(299500,'J/mol'), E0=(25416.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 629,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.59217e-05,'m^3/(mol*s)'), n=3.15405, w0=(299500,'J/mol'), E0=(21908.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 630,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.99305e-05,'m^3/(mol*s)'), n=3.20569, w0=(299500,'J/mol'), E0=(25726.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 631,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.83254e-09,'m^3/(mol*s)'), n=4.50432, w0=(299500,'J/mol'), E0=(20889.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.028706574397867606, var=0.5980395059914608, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 1.6224491301401553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.6224491301401553""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.6224491301401553
""",
)

entry(
    index = 632,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(0.000148664,'m^3/(mol*s)'), n=2.72935, w0=(299500,'J/mol'), E0=(47367.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 633,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000155428,'m^3/(mol*s)'), n=2.723, w0=(299500,'J/mol'), E0=(39728.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.102974334933584e-16, var=0.003172921427113525, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 0.1129241026640637"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 0.1129241026640637""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 0.1129241026640637
""",
)

entry(
    index = 634,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000685288,'m^3/(mol*s)'), n=2.02041, w0=(299500,'J/mol'), E0=(56243.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 635,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(2.64842e-08,'m^3/(mol*s)'), n=4.57508, w0=(377500,'J/mol'), E0=(15523.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03518532554626563, var=1.58707421770653, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F
    Total Standard Deviation in ln(k): 2.613953227969315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F
Total Standard Deviation in ln(k): 2.613953227969315""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F
Total Standard Deviation in ln(k): 2.613953227969315
""",
)

entry(
    index = 636,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(79.4924,'m^3/(mol*s)'), n=1.76076, w0=(377500,'J/mol'), E0=(75939,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006750489460972829, var=0.06403051856409375, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 0.5242442511938121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F
Total Standard Deviation in ln(k): 0.5242442511938121""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F
Total Standard Deviation in ln(k): 0.5242442511938121
""",
)

entry(
    index = 637,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F",
    kinetics = ArrheniusBM(A=(5.75008e-06,'m^3/(mol*s)'), n=2.92375, w0=(377500,'J/mol'), E0=(32112.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 638,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F",
    kinetics = ArrheniusBM(A=(0.000248607,'m^3/(mol*s)'), n=2.66431, w0=(377500,'J/mol'), E0=(67327.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 639,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.78339e-07,'m^3/(mol*s)'), n=3.46567, w0=(377500,'J/mol'), E0=(77732.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0004519259199117045, var=10.005908102454773, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 6.342536894862765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 6.342536894862765""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 6.342536894862765
""",
)

entry(
    index = 640,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.96843e-08,'m^3/(mol*s)'), n=3.73603, w0=(377500,'J/mol'), E0=(30759.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 641,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(0.818423,'m^3/(mol*s)'), n=1.69085, w0=(377500,'J/mol'), E0=(66491.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3827297029648272, var=1.685859935181887, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C
    Total Standard Deviation in ln(k): 3.5645938576406637"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.5645938576406637""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.5645938576406637
""",
)

entry(
    index = 642,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.12514e-05,'m^3/(mol*s)'), n=3.03612, w0=(377500,'J/mol'), E0=(34909.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 643,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(0.0013649,'m^3/(mol*s)'), n=2.67622, w0=(327000,'J/mol'), E0=(49069.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 644,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(0.110345,'m^3/(mol*s)'), n=1.80649, w0=(327000,'J/mol'), E0=(68051.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 645,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F",
    kinetics = ArrheniusBM(A=(8.17278e-07,'m^3/(mol*s)'), n=3.58113, w0=(327000,'J/mol'), E0=(64263.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 646,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F",
    kinetics = ArrheniusBM(A=(160.629,'m^3/(mol*s)'), n=0.642602, w0=(327000,'J/mol'), E0=(72396.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029370515222430518, var=24.88808021333458, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F
    Total Standard Deviation in ln(k): 10.075008531374321"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F
Total Standard Deviation in ln(k): 10.075008531374321""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F
Total Standard Deviation in ln(k): 10.075008531374321
""",
)

entry(
    index = 647,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(3.04724e-08,'m^3/(mol*s)'), n=3.71219, w0=(327000,'J/mol'), E0=(55256,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.016570749078643345, var=1.8633735828544047, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 2.778207536023226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl
Total Standard Deviation in ln(k): 2.778207536023226""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl
Total Standard Deviation in ln(k): 2.778207536023226
""",
)

entry(
    index = 648,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(6.53341e-06,'m^3/(mol*s)'), n=3.33791, w0=(327000,'J/mol'), E0=(64698.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03328743602254748, var=0.8403473565795473, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 1.921386677149056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 1.921386677149056""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 1.921386677149056
""",
)

entry(
    index = 649,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00149133,'m^3/(mol*s)'), n=2.80796, w0=(327000,'J/mol'), E0=(58360.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002322934276283307, var=4.411666556463115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.216575582860994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.216575582860994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.216575582860994
""",
)

entry(
    index = 650,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br",
    kinetics = ArrheniusBM(A=(5.12823e-06,'m^3/(mol*s)'), n=3.42232, w0=(327000,'J/mol'), E0=(62742.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 651,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br",
    kinetics = ArrheniusBM(A=(0.00542015,'m^3/(mol*s)'), n=2.0913, w0=(327000,'J/mol'), E0=(58500.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.016413724337212214, var=11.6716607525227, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br
    Total Standard Deviation in ln(k): 6.890179815800676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br
Total Standard Deviation in ln(k): 6.890179815800676""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br
Total Standard Deviation in ln(k): 6.890179815800676
""",
)

entry(
    index = 652,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(48967,'m^3/(mol*s)'), n=0.373136, w0=(327000,'J/mol'), E0=(67986,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017424829531510613, var=17.654047863650653, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
    Total Standard Deviation in ln(k): 8.467020284778199"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
Total Standard Deviation in ln(k): 8.467020284778199""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
Total Standard Deviation in ln(k): 8.467020284778199
""",
)

entry(
    index = 653,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.00565e-23,'m^3/(mol*s)'), n=8.82169, w0=(327000,'J/mol'), E0=(13069.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09108038846321016, var=0.6695343574187396, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
    Total Standard Deviation in ln(k): 1.8692212605140481"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
Total Standard Deviation in ln(k): 1.8692212605140481""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
Total Standard Deviation in ln(k): 1.8692212605140481
""",
)

entry(
    index = 654,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000243866,'m^3/(mol*s)'), n=2.90704, w0=(327000,'J/mol'), E0=(56571.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 655,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.0001815,'m^3/(mol*s)'), n=3.18568, w0=(327000,'J/mol'), E0=(59822.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 656,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.00785663,'m^3/(mol*s)'), n=2.37051, w0=(327000,'J/mol'), E0=(66410,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.021652696522710443, var=6.165882157185942, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.032400404400853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.032400404400853""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.032400404400853
""",
)

entry(
    index = 657,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0148734,'m^3/(mol*s)'), n=1.93367, w0=(327000,'J/mol'), E0=(59102,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 658,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C",
    kinetics = ArrheniusBM(A=(0.44422,'m^3/(mol*s)'), n=1.5117, w0=(327000,'J/mol'), E0=(49175.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.622923090604055, var=15.571922682899414, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C
    Total Standard Deviation in ln(k): 9.476073723510169"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 9.476073723510169""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 9.476073723510169
""",
)

entry(
    index = 659,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C",
    kinetics = ArrheniusBM(A=(0.000909656,'m^3/(mol*s)'), n=2.73905, w0=(327000,'J/mol'), E0=(68521,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 660,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00260953,'m^3/(mol*s)'), n=2.65495, w0=(327000,'J/mol'), E0=(71095.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.9391920276294965e-05, var=0.2249185057685291, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.9508309642395009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.9508309642395009""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.9508309642395009
""",
)

entry(
    index = 661,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(3.85859e-07,'m^3/(mol*s)'), n=3.30296, w0=(327000,'J/mol'), E0=(63102.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 662,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(0.00677928,'m^3/(mol*s)'), n=2.48293, w0=(327000,'J/mol'), E0=(67336.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001192022212344225, var=0.027990430190122446, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 0.3383940404409132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 0.3383940404409132""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 0.3383940404409132
""",
)

entry(
    index = 663,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(0.000183421,'m^3/(mol*s)'), n=3.08609, w0=(327000,'J/mol'), E0=(67923.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 664,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.211482,'m^3/(mol*s)'), n=2.3853, w0=(299500,'J/mol'), E0=(45837.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 665,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(12635,'m^3/(mol*s)'), n=0.772422, w0=(299500,'J/mol'), E0=(69890.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 666,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.884495,'m^3/(mol*s)'), n=2.14222, w0=(299500,'J/mol'), E0=(52012.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002473234318821272, var=0.07159205682116299, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 0.5426149471895118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.5426149471895118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.5426149471895118
""",
)

entry(
    index = 667,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1036.11,'m^3/(mol*s)'), n=1.05979, w0=(299500,'J/mol'), E0=(67700.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 668,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C",
    kinetics = ArrheniusBM(A=(0.0287048,'m^3/(mol*s)'), n=2.77954, w0=(327000,'J/mol'), E0=(55345.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 669,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C",
    kinetics = ArrheniusBM(A=(212391,'m^3/(mol*s)'), n=0.469006, w0=(283500,'J/mol'), E0=(34182.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 670,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R",
    kinetics = ArrheniusBM(A=(9.18494e-08,'m^3/(mol*s)'), n=4.00135, w0=(318300,'J/mol'), E0=(39736.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.31276825817144494, var=6.397011022933673, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R
    Total Standard Deviation in ln(k): 5.85628862227067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R
Total Standard Deviation in ln(k): 5.85628862227067""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R
Total Standard Deviation in ln(k): 5.85628862227067
""",
)

entry(
    index = 671,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C",
    kinetics = ArrheniusBM(A=(0.602197,'m^3/(mol*s)'), n=1.79841, w0=(327000,'J/mol'), E0=(72113.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 672,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C",
    kinetics = ArrheniusBM(A=(0.21934,'m^3/(mol*s)'), n=1.76817, w0=(327000,'J/mol'), E0=(54768,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 673,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.168083,'m^3/(mol*s)'), n=1.8024, w0=(327000,'J/mol'), E0=(72414.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 674,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.00416182,'m^3/(mol*s)'), n=2.75776, w0=(327000,'J/mol'), E0=(66704.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 675,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.0184071,'m^3/(mol*s)'), n=2.76105, w0=(327000,'J/mol'), E0=(62189.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 676,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O",
    kinetics = ArrheniusBM(A=(0.0117959,'m^3/(mol*s)'), n=2.7472, w0=(327000,'J/mol'), E0=(66187.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 677,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O",
    kinetics = ArrheniusBM(A=(0.00615345,'m^3/(mol*s)'), n=2.71255, w0=(327000,'J/mol'), E0=(60748.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 678,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0098082,'m^3/(mol*s)'), n=2.63859, w0=(327000,'J/mol'), E0=(67310.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0016498340392406717, var=0.17325397997015607, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 0.8385920076273257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 0.8385920076273257""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 0.8385920076273257
""",
)

entry(
    index = 679,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.58899,'m^3/(mol*s)'), n=2.05761, w0=(327000,'J/mol'), E0=(70663.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 680,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.24293e-05,'m^3/(mol*s)'), n=3.13493, w0=(327000,'J/mol'), E0=(66034.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0004017641776887628, var=14.112966075722639, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 7.532243398836198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.532243398836198""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.532243398836198
""",
)

entry(
    index = 681,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br",
    kinetics = ArrheniusBM(A=(0.00779837,'m^3/(mol*s)'), n=2.71484, w0=(327000,'J/mol'), E0=(65133.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 682,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br",
    kinetics = ArrheniusBM(A=(0.147314,'m^3/(mol*s)'), n=2.58017, w0=(327000,'J/mol'), E0=(64687.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 683,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.02363e-05,'m^3/(mol*s)'), n=3.27282, w0=(299500,'J/mol'), E0=(34631.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 684,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000151446,'m^3/(mol*s)'), n=2.66819, w0=(299500,'J/mol'), E0=(35825.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 685,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C",
    kinetics = ArrheniusBM(A=(46.947,'m^3/(mol*s)'), n=1.75719, w0=(377500,'J/mol'), E0=(58353.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 686,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C",
    kinetics = ArrheniusBM(A=(131.082,'m^3/(mol*s)'), n=1.7963, w0=(377500,'J/mol'), E0=(82861.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 687,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C",
    kinetics = ArrheniusBM(A=(81.3833,'m^3/(mol*s)'), n=1.79753, w0=(377500,'J/mol'), E0=(80678,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 688,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C",
    kinetics = ArrheniusBM(A=(92.576,'m^3/(mol*s)'), n=1.74555, w0=(377500,'J/mol'), E0=(75558.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00043017316604630377, var=0.060884837498802906, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C
    Total Standard Deviation in ln(k): 0.4957462722811417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C
Total Standard Deviation in ln(k): 0.4957462722811417""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C
Total Standard Deviation in ln(k): 0.4957462722811417
""",
)

entry(
    index = 689,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F",
    kinetics = ArrheniusBM(A=(5.0283e-06,'m^3/(mol*s)'), n=3.08625, w0=(377500,'J/mol'), E0=(64514,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 690,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F",
    kinetics = ArrheniusBM(A=(2.16928e-07,'m^3/(mol*s)'), n=3.17306, w0=(377500,'J/mol'), E0=(60720.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 691,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000694859,'m^3/(mol*s)'), n=2.4156, w0=(377500,'J/mol'), E0=(52535.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 692,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R",
    kinetics = ArrheniusBM(A=(0.00017113,'m^3/(mol*s)'), n=2.22654, w0=(327000,'J/mol'), E0=(64469.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 693,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R",
    kinetics = ArrheniusBM(A=(4.30603e-10,'m^3/(mol*s)'), n=4.2585, w0=(327000,'J/mol'), E0=(54994.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 694,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.68385e-08,'m^3/(mol*s)'), n=4.14292, w0=(327000,'J/mol'), E0=(58612.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 695,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br",
    kinetics = ArrheniusBM(A=(4.48911e-05,'m^3/(mol*s)'), n=3.19144, w0=(327000,'J/mol'), E0=(57601.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 696,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br",
    kinetics = ArrheniusBM(A=(0.000113941,'m^3/(mol*s)'), n=3.20363, w0=(327000,'J/mol'), E0=(53677.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 697,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C",
    kinetics = ArrheniusBM(A=(1.8714e-07,'m^3/(mol*s)'), n=3.7897, w0=(327000,'J/mol'), E0=(48918.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 698,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00123785,'m^3/(mol*s)'), n=2.06524, w0=(327000,'J/mol'), E0=(55767.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00217726397182622, var=0.011102202987407347, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C
    Total Standard Deviation in ln(k): 0.21670341720437988"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C
Total Standard Deviation in ln(k): 0.21670341720437988""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C
Total Standard Deviation in ln(k): 0.21670341720437988
""",
)

entry(
    index = 699,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.69523e-06,'m^3/(mol*s)'), n=3.1208, w0=(327000,'J/mol'), E0=(49362.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 700,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(9.80673e-05,'m^3/(mol*s)'), n=3.09159, w0=(327000,'J/mol'), E0=(44930.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 701,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.19327e-23,'m^3/(mol*s)'), n=8.71176, w0=(327000,'J/mol'), E0=(12605.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21062193305203852, var=0.9466580687919577, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.4797349936631594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.4797349936631594""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.4797349936631594
""",
)

entry(
    index = 702,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(0.000169094,'m^3/(mol*s)'), n=3.20047, w0=(327000,'J/mol'), E0=(59735.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 703,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(0.00031634,'m^3/(mol*s)'), n=2.69819, w0=(327000,'J/mol'), E0=(64357.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00042300009736377073, var=3.8370015898923895, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 3.927991179688995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
Total Standard Deviation in ln(k): 3.927991179688995""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
Total Standard Deviation in ln(k): 3.927991179688995
""",
)

entry(
    index = 704,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F",
    kinetics = ArrheniusBM(A=(67749.1,'m^3/(mol*s)'), n=0.0635332, w0=(327000,'J/mol'), E0=(62027.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009251539627005093, var=36.60222126377477, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F
    Total Standard Deviation in ln(k): 12.151846111405472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F
Total Standard Deviation in ln(k): 12.151846111405472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F
Total Standard Deviation in ln(k): 12.151846111405472
""",
)

entry(
    index = 705,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.00897965,'m^3/(mol*s)'), n=1.86068, w0=(327000,'J/mol'), E0=(41582.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 706,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(9.26597e-06,'m^3/(mol*s)'), n=3.28359, w0=(327000,'J/mol'), E0=(61704.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 707,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.46418e-07,'m^3/(mol*s)'), n=3.44684, w0=(327000,'J/mol'), E0=(49408.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 708,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(0.128823,'m^3/(mol*s)'), n=2.44703, w0=(299500,'J/mol'), E0=(52763.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 709,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C",
    kinetics = ArrheniusBM(A=(0.0950297,'m^3/(mol*s)'), n=2.23434, w0=(327000,'J/mol'), E0=(60928,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025810795774380422, var=1.9645965740273679, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C
    Total Standard Deviation in ln(k): 2.874769467170316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C
Total Standard Deviation in ln(k): 2.874769467170316""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C
Total Standard Deviation in ln(k): 2.874769467170316
""",
)

entry(
    index = 710,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C",
    kinetics = ArrheniusBM(A=(1.71214e+06,'m^3/(mol*s)'), n=0.133752, w0=(283500,'J/mol'), E0=(44105.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 711,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0320252,'m^3/(mol*s)'), n=2.41998, w0=(327000,'J/mol'), E0=(63533.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0240540358455134e-05, var=0.22556492885482587, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.952173243971634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.952173243971634""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.952173243971634
""",
)

entry(
    index = 712,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.21039,'m^3/(mol*s)'), n=1.87409, w0=(327000,'J/mol'), E0=(75354.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 713,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(134.809,'m^3/(mol*s)'), n=1.77494, w0=(377500,'J/mol'), E0=(80872.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 714,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C",
    kinetics = ArrheniusBM(A=(0.000113403,'m^3/(mol*s)'), n=2.24537, w0=(327000,'J/mol'), E0=(45871.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 715,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C",
    kinetics = ArrheniusBM(A=(6.47964e-05,'m^3/(mol*s)'), n=2.51178, w0=(327000,'J/mol'), E0=(57229.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 716,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(2.59266e-10,'m^3/(mol*s)'), n=4.91929, w0=(327000,'J/mol'), E0=(47373.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04950991903578138, var=0.9251149149221315, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 2.0526090012833413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl
Total Standard Deviation in ln(k): 2.0526090012833413""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl
Total Standard Deviation in ln(k): 2.0526090012833413
""",
)

entry(
    index = 717,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000250735,'m^3/(mol*s)'), n=3.18369, w0=(327000,'J/mol'), E0=(53802,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 718,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(7.4482e-05,'m^3/(mol*s)'), n=2.91197, w0=(327000,'J/mol'), E0=(61793.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0032305823749292505, var=5.695912041414659, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
    Total Standard Deviation in ln(k): 4.7926398188971575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
Total Standard Deviation in ln(k): 4.7926398188971575""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
Total Standard Deviation in ln(k): 4.7926398188971575
""",
)

entry(
    index = 719,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0200628,'m^3/(mol*s)'), n=2.08964, w0=(327000,'J/mol'), E0=(72419.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 720,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F",
    kinetics = ArrheniusBM(A=(0.00843525,'m^3/(mol*s)'), n=1.82185, w0=(327000,'J/mol'), E0=(49437.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 721,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F",
    kinetics = ArrheniusBM(A=(0.000319131,'m^3/(mol*s)'), n=2.84493, w0=(327000,'J/mol'), E0=(45294.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 722,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R",
    kinetics = ArrheniusBM(A=(0.000729546,'m^3/(mol*s)'), n=3.08162, w0=(327000,'J/mol'), E0=(63181.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00012636295401745456, var=0.049515701782837096, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R
    Total Standard Deviation in ln(k): 0.44641362804307605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R
Total Standard Deviation in ln(k): 0.44641362804307605""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R
Total Standard Deviation in ln(k): 0.44641362804307605
""",
)

entry(
    index = 723,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C",
    kinetics = ArrheniusBM(A=(0.00133416,'m^3/(mol*s)'), n=2.78212, w0=(327000,'J/mol'), E0=(57697.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 724,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C",
    kinetics = ArrheniusBM(A=(0.208167,'m^3/(mol*s)'), n=1.78944, w0=(327000,'J/mol'), E0=(53867.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 725,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(18.7578,'m^3/(mol*s)'), n=1.67817, w0=(327000,'J/mol'), E0=(75299.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 726,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.1699e-10,'m^3/(mol*s)'), n=5.02603, w0=(327000,'J/mol'), E0=(48371,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.056982599919405415, var=1.3994413331237787, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 2.514733569206707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.514733569206707""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.514733569206707
""",
)

entry(
    index = 727,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000135758,'m^3/(mol*s)'), n=2.72245, w0=(327000,'J/mol'), E0=(61722.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004965174766263925, var=8.329021544654031, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.798149619022849"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.798149619022849""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.798149619022849
""",
)

entry(
    index = 728,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F",
    kinetics = ArrheniusBM(A=(0.0167469,'m^3/(mol*s)'), n=2.76768, w0=(327000,'J/mol'), E0=(71015.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 729,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(0.0102091,'m^3/(mol*s)'), n=2.77509, w0=(327000,'J/mol'), E0=(68497.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 730,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(0.00016077,'m^3/(mol*s)'), n=3.1849, w0=(327000,'J/mol'), E0=(67813.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 731,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(0.0001693,'m^3/(mol*s)'), n=3.21727, w0=(327000,'J/mol'), E0=(59814.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 732,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(0.000306394,'m^3/(mol*s)'), n=3.18453, w0=(327000,'J/mol'), E0=(60721.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 733,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000241094,'m^3/(mol*s)'), n=2.88397, w0=(327000,'J/mol'), E0=(67374.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

