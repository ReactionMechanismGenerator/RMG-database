#!/usr/bin/env python
# encoding: utf-8

name = "F_Abstraction/rules"
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
    kinetics = ArrheniusBM(A=(6.43922e+32,'m^3/(mol*s)'), n=-7.31291, w0=(412.907,'kJ/mol'), E0=(253.536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.04818949699181, var=16.01440004749627, Tref=1000.0, N=242, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 242 training reactions at node Root
    Total Standard Deviation in ln(k): 10.656189985300852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 242 training reactions at node Root
Total Standard Deviation in ln(k): 10.656189985300852""",
    longDesc = 
"""
BM rule fitted to 242 training reactions at node Root
Total Standard Deviation in ln(k): 10.656189985300852
""",
)

entry(
    index = 2,
    label = "Root_1R->O",
    kinetics = ArrheniusBM(A=(1.73627e-08,'m^3/(mol*s)'), n=4.3161, w0=(337.688,'kJ/mol'), E0=(90.7442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23610417283857973, var=5.66670635196425, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_1R->O',), comment="""BM rule fitted to 64 training reactions at node Root_1R->O
    Total Standard Deviation in ln(k): 5.365467299987469"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.365467299987469""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.365467299987469
""",
)

entry(
    index = 3,
    label = "Root_N-1R->O",
    kinetics = ArrheniusBM(A=(4.85612e+32,'m^3/(mol*s)'), n=-7.27856, w0=(439.952,'kJ/mol'), E0=(257.474,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0493413696649951, var=15.733461158370503, Tref=1000.0, N=178, data_mean=0.0, correlation='Root_N-1R->O',), comment="""BM rule fitted to 178 training reactions at node Root_N-1R->O
    Total Standard Deviation in ln(k): 10.588403433672402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 178 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 10.588403433672402""",
    longDesc = 
"""
BM rule fitted to 178 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 10.588403433672402
""",
)

entry(
    index = 4,
    label = "Root_1R->O_3R->O",
    kinetics = ArrheniusBM(A=(0.00293908,'m^3/(mol*s)'), n=3.25836, w0=(228.093,'kJ/mol'), E0=(115.523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.036535856505909785, var=0.6058215571692247, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
    Total Standard Deviation in ln(k): 1.6521749543090176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.6521749543090176""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.6521749543090176
""",
)

entry(
    index = 5,
    label = "Root_1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(47406,'m^3/(mol*s)'), n=0.687846, w0=(354.214,'kJ/mol'), E0=(142.706,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20423147366122954, var=4.909942095159391, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_1R->O_N-3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
    Total Standard Deviation in ln(k): 4.9553144040035155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.9553144040035155""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.9553144040035155
""",
)

entry(
    index = 6,
    label = "Root_N-1R->O_3R->O",
    kinetics = ArrheniusBM(A=(1.08789e-08,'m^3/(mol*s)'), n=4.64827, w0=(515.412,'kJ/mol'), E0=(79.3551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23100484609731578, var=5.175507343849098, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
    Total Standard Deviation in ln(k): 5.141134647519817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.141134647519817""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.141134647519817
""",
)

entry(
    index = 7,
    label = "Root_N-1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(4.69918e+18,'m^3/(mol*s)'), n=-3.32677, w0=(479.308,'kJ/mol'), E0=(227.108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6972087088863522, var=12.189859232374713, Tref=1000.0, N=122, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O',), comment="""BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
    Total Standard Deviation in ln(k): 8.751108496561763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.751108496561763""",
    longDesc = 
"""
BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.751108496561763
""",
)

entry(
    index = 8,
    label = "Root_1R->O_3R->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.0549439,'m^3/(mol*s)'), n=2.89629, w0=(222,'kJ/mol'), E0=(116.204,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1862381768289538, var=5.7079287555470515, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
    Total Standard Deviation in ln(k): 7.770065024599618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.770065024599618""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.770065024599618
""",
)

entry(
    index = 9,
    label = "Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R",
    kinetics = Arrhenius(A=(3.88038e-05,'m^3/(mol*s)'), n=3.96851, Ea=(195.567,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R->O_3R->O_1O-u0",
    kinetics = Arrhenius(A=(1.72685e-05,'m^3/(mol*s)'), n=3.8992, Ea=(122.263,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R->O_3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.140122,'m^3/(mol*s)'), n=2.30265, w0=(266.604,'kJ/mol'), E0=(120.185,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31081505617104455, var=1.141349567679423, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 2.9226802855070133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.9226802855070133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.9226802855070133
""",
)

entry(
    index = 12,
    label = "Root_1R->O_N-3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(109.524,'m^3/(mol*s)'), n=1.45616, w0=(354.37,'kJ/mol'), E0=(125.848,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1527041277575061, var=3.1500117744590552, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0',), comment="""BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
    Total Standard Deviation in ln(k): 3.941737161367701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 3.941737161367701""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 3.941737161367701
""",
)

entry(
    index = 13,
    label = "Root_1R->O_N-3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(1.37179e-18,'m^3/(mol*s)'), n=7.09652, w0=(353.5,'kJ/mol'), E0=(54.6033,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7639757994951839, var=9.458690911152807, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 8.08509687146734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 8.08509687146734""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 8.08509687146734
""",
)

entry(
    index = 14,
    label = "Root_N-1R->O_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(7.7204e-09,'m^3/(mol*s)'), n=4.6122, w0=(540.177,'kJ/mol'), E0=(50.4049,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5013391970742386, var=2.33840575380903, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 4.325256370810569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.325256370810569""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.325256370810569
""",
)

entry(
    index = 15,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0",
    kinetics = ArrheniusBM(A=(0.766208,'m^3/(mol*s)'), n=2.53618, w0=(490.667,'kJ/mol'), E0=(114.491,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1190895280294681, var=11.646509767556543, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0
    Total Standard Deviation in ln(k): 7.140775933958206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 7.140775933958206""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 7.140775933958206
""",
)

entry(
    index = 16,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0",
    kinetics = ArrheniusBM(A=(6.96523e+08,'m^3/(mol*s)'), n=-0.222866, w0=(523.611,'kJ/mol'), E0=(166.533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8973197826099661, var=7.901609184693302, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0
    Total Standard Deviation in ln(k): 7.88984274858564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 7.88984274858564""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 7.88984274858564
""",
)

entry(
    index = 17,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F",
    kinetics = ArrheniusBM(A=(0.22677,'m^3/(mol*s)'), n=2.32228, w0=(326.667,'kJ/mol'), E0=(102.334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1879357665720745, var=1.369894418289326, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F
    Total Standard Deviation in ln(k): 2.818592246814058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F
Total Standard Deviation in ln(k): 2.818592246814058""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F
Total Standard Deviation in ln(k): 2.818592246814058
""",
)

entry(
    index = 18,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F",
    kinetics = ArrheniusBM(A=(5.55463e+12,'m^3/(mol*s)'), n=-1.63065, w0=(487.203,'kJ/mol'), E0=(213.839,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5446126889956594, var=11.926723216894985, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F',), comment="""BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F
    Total Standard Deviation in ln(k): 8.291743875649352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F
Total Standard Deviation in ln(k): 8.291743875649352""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F
Total Standard Deviation in ln(k): 8.291743875649352
""",
)

entry(
    index = 19,
    label = "Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R",
    kinetics = Arrhenius(A=(0.0487535,'m^3/(mol*s)'), n=3.06244, Ea=(13.9612,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.00501058,'m^3/(mol*s)'), n=3.19467, w0=(223.463,'kJ/mol'), E0=(113.815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.311672949735077, var=4.981622398262161, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 7.770138832350765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.770138832350765""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.770138832350765
""",
)

entry(
    index = 21,
    label = "Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C",
    kinetics = Arrhenius(A=(0.0779944,'m^3/(mol*s)'), n=2.62416, Ea=(75.5635,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C",
    kinetics = Arrhenius(A=(0.0730252,'m^3/(mol*s)'), n=2.39118, Ea=(139.927,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C",
    kinetics = Arrhenius(A=(0.00111026,'m^3/(mol*s)'), n=2.89721, Ea=(154.45,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1",
    kinetics = ArrheniusBM(A=(406.972,'m^3/(mol*s)'), n=1.27384, w0=(354.611,'kJ/mol'), E0=(126.452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12337916957327523, var=4.075617970353137, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1',), comment="""BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
    Total Standard Deviation in ln(k): 4.357189128003137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.357189128003137""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.357189128003137
""",
)

entry(
    index = 25,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(1.18901e-06,'m^3/(mol*s)'), n=3.82331, w0=(353.5,'kJ/mol'), E0=(67.7625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021250960290257536, var=1.160438535287788, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
    Total Standard Deviation in ln(k): 2.2129682250876446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.2129682250876446""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.2129682250876446
""",
)

entry(
    index = 26,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(5.93743e-18,'m^3/(mol*s)'), n=6.85017, w0=(353.5,'kJ/mol'), E0=(11.3479,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.802122904494715, var=27.265915047861213, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 14.996026877040006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 14.996026877040006""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 14.996026877040006
""",
)

entry(
    index = 27,
    label = "Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1",
    kinetics = Arrhenius(A=(0.00154,'m^3/(mol*s)'), n=2.64, Ea=(25.9,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1",
    kinetics = Arrhenius(A=(0.000996795,'m^3/(mol*s)'), n=2.97758, Ea=(41.2332,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O",
    kinetics = ArrheniusBM(A=(8.23395e-08,'m^3/(mol*s)'), n=4.30203, w0=(561.883,'kJ/mol'), E0=(63.9494,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5147020638655608, var=7.4933052547676855, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
    Total Standard Deviation in ln(k): 6.780963474537326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 6.780963474537326""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 6.780963474537326
""",
)

entry(
    index = 30,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(3.98033e-09,'m^3/(mol*s)'), n=4.72384, w0=(518.471,'kJ/mol'), E0=(83.1722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3446449708800382, var=3.6252288440001754, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
    Total Standard Deviation in ln(k): 4.682964487011335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.682964487011335""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.682964487011335
""",
)

entry(
    index = 31,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(0.571764,'m^3/(mol*s)'), n=2.57006, w0=(496.863,'kJ/mol'), E0=(113.768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14239373642661407, var=12.846794452379962, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 7.54322991568724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 7.54322991568724""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 7.54322991568724
""",
)

entry(
    index = 32,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_3O-u1",
    kinetics = Arrhenius(A=(0.00127734,'m^3/(mol*s)'), n=3.49913, Ea=(277.414,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_N-3O-u1",
    kinetics = Arrhenius(A=(3.71371e-05,'m^3/(mol*s)'), n=3.67929, Ea=(267.55,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(0.0236604,'m^3/(mol*s)'), n=2.67129, w0=(529.245,'kJ/mol'), E0=(85.7434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.322091280394907, var=9.928114922276562, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 12.15110217827353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 12.15110217827353""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 12.15110217827353
""",
)

entry(
    index = 35,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_3O-u1",
    kinetics = Arrhenius(A=(0.00226498,'m^3/(mol*s)'), n=3.15133, Ea=(325.669,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_N-3O-u1",
    kinetics = Arrhenius(A=(0.000137082,'m^3/(mol*s)'), n=3.52572, Ea=(323.852,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->H",
    kinetics = Arrhenius(A=(29364.6,'m^3/(mol*s)'), n=0.785655, Ea=(4.07732,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(0.0789065,'m^3/(mol*s)'), n=2.39473, w0=(320,'kJ/mol'), E0=(92.9853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0451538352851925, var=0.6729740932766688, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H
    Total Standard Deviation in ln(k): 1.758036232483167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 1.758036232483167""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 1.758036232483167
""",
)

entry(
    index = 39,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H",
    kinetics = ArrheniusBM(A=(5.91798,'m^3/(mol*s)'), n=2.07168, w0=(518.487,'kJ/mol'), E0=(170.135,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5360484000563462, var=5.12709775354663, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H
    Total Standard Deviation in ln(k): 5.8861960642712905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 5.8861960642712905""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 5.8861960642712905
""",
)

entry(
    index = 40,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(3.07605e+15,'m^3/(mol*s)'), n=-2.4981, w0=(481.457,'kJ/mol'), E0=(224.749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5033430109758089, var=10.506319115634556, Tref=1000.0, N=98, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H',), comment="""BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H
    Total Standard Deviation in ln(k): 7.762719479295406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 7.762719479295406""",
    longDesc = 
"""
BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 7.762719479295406
""",
)

entry(
    index = 41,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1",
    kinetics = Arrhenius(A=(0.0049864,'m^3/(mol*s)'), n=3.19625, Ea=(104.62,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1",
    kinetics = Arrhenius(A=(0.640932,'m^3/(mol*s)'), n=2.39839, Ea=(106.019,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.0547067,'m^3/(mol*s)'), n=2.33633, w0=(353.5,'kJ/mol'), E0=(109.325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08422798392250552, var=3.8779576365560193, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 4.159458797274196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.159458797274196""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.159458797274196
""",
)

entry(
    index = 44,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H",
    kinetics = Arrhenius(A=(1.04105,'m^3/(mol*s)'), n=2.3137, Ea=(11.5771,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(5.15234e-10,'m^3/(mol*s)'), n=4.89163, w0=(353.5,'kJ/mol'), E0=(58.1422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10970346547979189, var=4.5306024224849795, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H
    Total Standard Deviation in ln(k): 4.5427579245945235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H
Total Standard Deviation in ln(k): 4.5427579245945235""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H
Total Standard Deviation in ln(k): 4.5427579245945235
""",
)

entry(
    index = 46,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000245593,'m^3/(mol*s)'), n=3.10149, w0=(353.5,'kJ/mol'), E0=(62.672,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.1830706132536193, var=15.116406717583448, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 13.279476631319277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 13.279476631319277""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 13.279476631319277
""",
)

entry(
    index = 47,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R",
    kinetics = Arrhenius(A=(0.000178698,'m^3/(mol*s)'), n=3.25898, Ea=(11.1651,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH",
    kinetics = ArrheniusBM(A=(3.90045e-15,'m^3/(mol*s)'), n=6.03878, w0=(353.5,'kJ/mol'), E0=(34.618,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5485816973790718, var=10.759039383055262, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
    Total Standard Deviation in ln(k): 10.466635233706075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 10.466635233706075""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 10.466635233706075
""",
)

entry(
    index = 49,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH",
    kinetics = Arrhenius(A=(0.00171,'m^3/(mol*s)'), n=2.75, Ea=(107.2,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0",
    kinetics = ArrheniusBM(A=(4.41303e-05,'m^3/(mol*s)'), n=3.55634, w0=(557.262,'kJ/mol'), E0=(65.4651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9528843815998222, var=1.1171014805169428, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0
    Total Standard Deviation in ln(k): 4.513046940762661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 4.513046940762661""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 4.513046940762661
""",
)

entry(
    index = 51,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0",
    kinetics = ArrheniusBM(A=(2.50334e-06,'m^3/(mol*s)'), n=3.83443, w0=(574.203,'kJ/mol'), E0=(118.551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2005573809318135, var=11.86437695635573, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0
    Total Standard Deviation in ln(k): 9.921726645802522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 9.921726645802522""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 9.921726645802522
""",
)

entry(
    index = 52,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->H",
    kinetics = Arrhenius(A=(0.000687874,'m^3/(mol*s)'), n=2.99039, Ea=(395.881,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H",
    kinetics = ArrheniusBM(A=(0.585926,'m^3/(mol*s)'), n=2.41445, w0=(510.387,'kJ/mol'), E0=(120.299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22022232765485947, var=2.011855538891816, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H
    Total Standard Deviation in ln(k): 3.3968365300850287"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H
Total Standard Deviation in ln(k): 3.3968365300850287""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H
Total Standard Deviation in ln(k): 3.3968365300850287
""",
)

entry(
    index = 54,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi",
    kinetics = Arrhenius(A=(1.72013,'m^3/(mol*s)'), n=2.4493, Ea=(387.834,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi",
    kinetics = ArrheniusBM(A=(0.784243,'m^3/(mol*s)'), n=2.53072, w0=(491.84,'kJ/mol'), E0=(114.194,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1438385054438113, var=12.83284583777136, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi
    Total Standard Deviation in ln(k): 7.542958066314379"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi
Total Standard Deviation in ln(k): 7.542958066314379""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi
Total Standard Deviation in ln(k): 7.542958066314379
""",
)

entry(
    index = 56,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi",
    kinetics = ArrheniusBM(A=(0.0260557,'m^3/(mol*s)'), n=2.65832, w0=(515.452,'kJ/mol'), E0=(85.7434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.1978997929656545, var=15.097901431897137, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi
    Total Standard Deviation in ln(k): 15.824526349775374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi
Total Standard Deviation in ln(k): 15.824526349775374""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi
Total Standard Deviation in ln(k): 15.824526349775374
""",
)

entry(
    index = 57,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H-1BrCClFHILiNPSSi",
    kinetics = Arrhenius(A=(0.0387235,'m^3/(mol*s)'), n=2.8378, Ea=(400.231,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H-1BrCClFHILiNPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H-1BrCClFHILiNPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H-1BrCClFHILiNPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H-1BrCClFHILiNPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R",
    kinetics = ArrheniusBM(A=(0.0108084,'m^3/(mol*s)'), n=2.63211, w0=(320,'kJ/mol'), E0=(83.1131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.383282743962665, var=1.3861367681049666, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R
    Total Standard Deviation in ln(k): 3.3232829744829577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R
Total Standard Deviation in ln(k): 3.3232829744829577""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R
Total Standard Deviation in ln(k): 3.3232829744829577
""",
)

entry(
    index = 59,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->Cl",
    kinetics = Arrhenius(A=(650.29,'m^3/(mol*s)'), n=1.25799, Ea=(20.8614,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl",
    kinetics = ArrheniusBM(A=(1.34124e-10,'m^3/(mol*s)'), n=5.13941, w0=(525,'kJ/mol'), E0=(146.582,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3445190667762157, var=3.489677179536383, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl
    Total Standard Deviation in ln(k): 4.610606773996444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl
Total Standard Deviation in ln(k): 4.610606773996444""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl
Total Standard Deviation in ln(k): 4.610606773996444
""",
)

entry(
    index = 61,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C",
    kinetics = ArrheniusBM(A=(1.45625e-09,'m^3/(mol*s)'), n=4.44899, w0=(492.473,'kJ/mol'), E0=(168.477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1256329403256705, var=4.8578818815099165, Tref=1000.0, N=91, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C',), comment="""BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C
    Total Standard Deviation in ln(k): 4.734217684510595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 4.734217684510595""",
    longDesc = 
"""
BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 4.734217684510595
""",
)

entry(
    index = 62,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C",
    kinetics = ArrheniusBM(A=(32.6623,'m^3/(mol*s)'), n=1.76557, w0=(539.512,'kJ/mol'), E0=(103.419,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.665542150176209, var=15.67713131893077, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C
    Total Standard Deviation in ln(k): 9.609836157140156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 9.609836157140156""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 9.609836157140156
""",
)

entry(
    index = 63,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.89739e-06,'m^3/(mol*s)'), n=3.34803, w0=(353.5,'kJ/mol'), E0=(99.0058,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.8654383217508355, var=15.298175950309576, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
    Total Standard Deviation in ln(k): 15.040690570850948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.040690570850948""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.040690570850948
""",
)

entry(
    index = 64,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000271622,'m^3/(mol*s)'), n=3.0151, w0=(353.5,'kJ/mol'), E0=(96.5972,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.045748116811703855, var=4.578545239213166, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl',), comment="""BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.404584008506034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.404584008506034""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.404584008506034
""",
)

entry(
    index = 65,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.0397432,'m^3/(mol*s)'), n=2.50094, w0=(353.5,'kJ/mol'), E0=(107.939,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1272720655839468, var=0.09203473210116113, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R
    Total Standard Deviation in ln(k): 0.9279600834827265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R
Total Standard Deviation in ln(k): 0.9279600834827265""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R
Total Standard Deviation in ln(k): 0.9279600834827265
""",
)

entry(
    index = 66,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000340767,'m^3/(mol*s)'), n=3.06, w0=(353.5,'kJ/mol'), E0=(73.6425,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.911279558709082, var=69.36738782868656, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 31.549315589108073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.549315589108073""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.549315589108073
""",
)

entry(
    index = 67,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R",
    kinetics = Arrhenius(A=(1.85866e-05,'m^3/(mol*s)'), n=3.19173, Ea=(8.44927,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(9.97946e-13,'m^3/(mol*s)'), n=5.64084, w0=(353.5,'kJ/mol'), E0=(76.2913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3932029317723997, var=0.317756380140982, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 7.143139526837676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 7.143139526837676""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 7.143139526837676
""",
)

entry(
    index = 69,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C",
    kinetics = Arrhenius(A=(1.07293e-05,'m^3/(mol*s)'), n=3.59914, Ea=(12.1564,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O",
    kinetics = ArrheniusBM(A=(0.000485831,'m^3/(mol*s)'), n=2.91263, w0=(353.5,'kJ/mol'), E0=(110.441,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.042120305071763, var=1.2597325164130675, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
    Total Standard Deviation in ln(k): 12.406151841613536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
Total Standard Deviation in ln(k): 12.406151841613536""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
Total Standard Deviation in ln(k): 12.406151841613536
""",
)

entry(
    index = 71,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.1396e-10,'m^3/(mol*s)'), n=4.67699, w0=(353.5,'kJ/mol'), E0=(116.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20417718568769003, var=1.670403691693797, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
    Total Standard Deviation in ln(k): 3.104009776116423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
Total Standard Deviation in ln(k): 3.104009776116423""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
Total Standard Deviation in ln(k): 3.104009776116423
""",
)

entry(
    index = 72,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(4.77673e-05,'m^3/(mol*s)'), n=3.54518, w0=(563.607,'kJ/mol'), E0=(65.4269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9774283099766633, var=1.1881724381599277, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 4.641077872778306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 4.641077872778306""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 4.641077872778306
""",
)

entry(
    index = 73,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(1.40359e+11,'m^3/(mol*s)'), n=-1.04937, w0=(579.378,'kJ/mol'), E0=(161.116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5064640674944558, var=48.49142268922335, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 17.745215271568103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 17.745215271568103""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 17.745215271568103
""",
)

entry(
    index = 74,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(0.000404315,'m^3/(mol*s)'), n=3.30562, w0=(469.209,'kJ/mol'), E0=(107.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7861741455299677, var=4.617205676741829, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 6.283023326732462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 6.283023326732462""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 6.283023326732462
""",
)

entry(
    index = 75,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(451.851,'m^3/(mol*s)'), n=1.63275, w0=(537.839,'kJ/mol'), E0=(131.285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03209642899834627, var=0.5085948848383809, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 1.5103379279677207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 1.5103379279677207""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 1.5103379279677207
""",
)

entry(
    index = 76,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F",
    kinetics = ArrheniusBM(A=(2045.42,'m^3/(mol*s)'), n=1.59852, w0=(517.754,'kJ/mol'), E0=(143.073,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27455683002721026, var=1.9643423958919766, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F
    Total Standard Deviation in ln(k): 3.4995777244711923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.4995777244711923""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.4995777244711923
""",
)

entry(
    index = 77,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F",
    kinetics = ArrheniusBM(A=(14890.4,'m^3/(mol*s)'), n=1.28715, w0=(477.032,'kJ/mol'), E0=(123.908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07451362387249603, var=23.862399428646498, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F
    Total Standard Deviation in ln(k): 9.980181610671092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 9.980181610671092""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 9.980181610671092
""",
)

entry(
    index = 78,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O",
    kinetics = ArrheniusBM(A=(0.13755,'m^3/(mol*s)'), n=2.45159, w0=(530.964,'kJ/mol'), E0=(97.1831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.9105072835905106, var=13.059589713401982, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O
    Total Standard Deviation in ln(k): 14.55755488685779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O
Total Standard Deviation in ln(k): 14.55755488685779""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O
Total Standard Deviation in ln(k): 14.55755488685779
""",
)

entry(
    index = 79,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O",
    kinetics = ArrheniusBM(A=(2.81439e+17,'m^3/(mol*s)'), n=-2.60285, w0=(484.427,'kJ/mol'), E0=(161.571,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03682186198244248, var=30.920478343061166, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O
    Total Standard Deviation in ln(k): 11.240084243475062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O
Total Standard Deviation in ln(k): 11.240084243475062""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O
Total Standard Deviation in ln(k): 11.240084243475062
""",
)

entry(
    index = 80,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R",
    kinetics = ArrheniusBM(A=(0.0823982,'m^3/(mol*s)'), n=2.3774, w0=(320,'kJ/mol'), E0=(92.9853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03260278366730891, var=0.34757708322546954, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R
    Total Standard Deviation in ln(k): 1.263821505684412"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R
Total Standard Deviation in ln(k): 1.263821505684412""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R
Total Standard Deviation in ln(k): 1.263821505684412
""",
)

entry(
    index = 81,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R",
    kinetics = ArrheniusBM(A=(9.20796e-11,'m^3/(mol*s)'), n=5.18603, w0=(525,'kJ/mol'), E0=(146.384,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34373226423795106, var=3.4570780795466924, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R
    Total Standard Deviation in ln(k): 4.591096820014237"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R
Total Standard Deviation in ln(k): 4.591096820014237""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R
Total Standard Deviation in ln(k): 4.591096820014237
""",
)

entry(
    index = 82,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1",
    kinetics = ArrheniusBM(A=(1.36111e-09,'m^3/(mol*s)'), n=4.45713, w0=(493,'kJ/mol'), E0=(168.418,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.126451270693599, var=4.838110290240033, Tref=1000.0, N=85, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1',), comment="""BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
    Total Standard Deviation in ln(k): 4.727272854146328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
Total Standard Deviation in ln(k): 4.727272854146328""",
    longDesc = 
"""
BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
Total Standard Deviation in ln(k): 4.727272854146328
""",
)

entry(
    index = 83,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(1.81911e-05,'m^3/(mol*s)'), n=3.64993, w0=(485,'kJ/mol'), E0=(159.215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04751140728636986, var=12.866475774271212, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
    Total Standard Deviation in ln(k): 7.31033406633724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
Total Standard Deviation in ln(k): 7.31033406633724""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
Total Standard Deviation in ln(k): 7.31033406633724
""",
)

entry(
    index = 84,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H",
    kinetics = ArrheniusBM(A=(19406.8,'m^3/(mol*s)'), n=0.69086, w0=(569.378,'kJ/mol'), E0=(123.771,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2857695948365695, var=0.5959251139749165, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H
    Total Standard Deviation in ln(k): 4.778155891484378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H
Total Standard Deviation in ln(k): 4.778155891484378""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H
Total Standard Deviation in ln(k): 4.778155891484378
""",
)

entry(
    index = 85,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H",
    kinetics = ArrheniusBM(A=(6.271e+08,'m^3/(mol*s)'), n=0.020209, w0=(527.566,'kJ/mol'), E0=(132.796,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6947050627228968, var=2.073509385268082, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H
    Total Standard Deviation in ln(k): 4.632245542223378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H
Total Standard Deviation in ln(k): 4.632245542223378""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H
Total Standard Deviation in ln(k): 4.632245542223378
""",
)

entry(
    index = 86,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.41898e-06,'m^3/(mol*s)'), n=3.52361, w0=(353.5,'kJ/mol'), E0=(95.7533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.9663733357086106, var=2.9412824458163045, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
    Total Standard Deviation in ln(k): 8.37879075485405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 8.37879075485405""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 8.37879075485405
""",
)

entry(
    index = 87,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R",
    kinetics = Arrhenius(A=(2.40529e-06,'m^3/(mol*s)'), n=3.70283, Ea=(50.5842,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R",
    kinetics = ArrheniusBM(A=(1.9965e-05,'m^3/(mol*s)'), n=3.06368, w0=(353.5,'kJ/mol'), E0=(93.4586,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10951819585566452, var=0.8144638996168477, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
    Total Standard Deviation in ln(k): 2.084397716377234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 2.084397716377234""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 2.084397716377234
""",
)

entry(
    index = 89,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi",
    kinetics = Arrhenius(A=(0.00502134,'m^3/(mol*s)'), n=2.89121, Ea=(50.3342,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.24392e-07,'m^3/(mol*s)'), n=4.02029, w0=(353.5,'kJ/mol'), E0=(65.9793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19713230138189716, var=4.026634705433563, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 4.518104178962187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 4.518104178962187""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 4.518104178962187
""",
)

entry(
    index = 91,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C",
    kinetics = Arrhenius(A=(0.000476496,'m^3/(mol*s)'), n=3.27616, Ea=(30.5726,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0280362,'m^3/(mol*s)'), n=2.53741, w0=(353.5,'kJ/mol'), E0=(106.354,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.6984218191879847, var=1.5602719802605556, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 9.284085893220507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 9.284085893220507""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 9.284085893220507
""",
)

entry(
    index = 93,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000290035,'m^3/(mol*s)'), n=3.07816, w0=(353.5,'kJ/mol'), E0=(80.7316,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.425857212197383, var=60.29990428029078, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 29.200178968532555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 29.200178968532555""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 29.200178968532555
""",
)

entry(
    index = 94,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C",
    kinetics = Arrhenius(A=(1.59848e-08,'m^3/(mol*s)'), n=4.6762, Ea=(-44.8077,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH",
    kinetics = Arrhenius(A=(3.03844e-05,'m^3/(mol*s)'), n=3.46112, Ea=(17.8464,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH",
    kinetics = Arrhenius(A=(9.84034e-05,'m^3/(mol*s)'), n=3.38442, Ea=(21.95,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1",
    kinetics = Arrhenius(A=(0.000576508,'m^3/(mol*s)'), n=2.8908, Ea=(21.561,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1",
    kinetics = Arrhenius(A=(0.0988204,'m^3/(mol*s)'), n=2.35704, Ea=(32.5918,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C",
    kinetics = Arrhenius(A=(5.27678,'m^3/(mol*s)'), n=1.68981, Ea=(39.1096,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C",
    kinetics = ArrheniusBM(A=(9.09828e-11,'m^3/(mol*s)'), n=4.70447, w0=(353.5,'kJ/mol'), E0=(116.607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1871734324497998, var=1.7010604808675707, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C
    Total Standard Deviation in ln(k): 3.084954904056692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 3.084954904056692""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 3.084954904056692
""",
)

entry(
    index = 101,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(5.8091e-05,'m^3/(mol*s)'), n=3.43326, w0=(593.173,'kJ/mol'), E0=(71.2223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7203058223558416, var=2.3274035039767025, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 7.380766200912349"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.380766200912349""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.380766200912349
""",
)

entry(
    index = 102,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(0.00525089,'m^3/(mol*s)'), n=2.97505, w0=(541.433,'kJ/mol'), E0=(97.973,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.6359766129238684, var=12.43993759303567, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 13.693816715906316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 13.693816715906316""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 13.693816715906316
""",
)

entry(
    index = 103,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Ext-1BrCClFHILiNPSSi-R",
    kinetics = Arrhenius(A=(0.000115787,'m^3/(mol*s)'), n=3.43806, Ea=(384.463,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R",
    kinetics = ArrheniusBM(A=(0.000412488,'m^3/(mol*s)'), n=3.30263, w0=(467.648,'kJ/mol'), E0=(107.49,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7858605351653043, var=4.64174620882118, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R
    Total Standard Deviation in ln(k): 6.293667972185655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R
Total Standard Deviation in ln(k): 6.293667972185655""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R
Total Standard Deviation in ln(k): 6.293667972185655
""",
)

entry(
    index = 105,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R",
    kinetics = ArrheniusBM(A=(2.74409,'m^3/(mol*s)'), n=2.28954, w0=(551.184,'kJ/mol'), E0=(122.143,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.050074560616604945, var=0.6119798148530418, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R
    Total Standard Deviation in ln(k): 1.6941024640679827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R
Total Standard Deviation in ln(k): 1.6941024640679827""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R
Total Standard Deviation in ln(k): 1.6941024640679827
""",
)

entry(
    index = 106,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(349205,'m^3/(mol*s)'), n=0.964701, w0=(531.114,'kJ/mol'), E0=(153.144,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4131243359884633, var=2.324664242104322, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 4.094590275244876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 4.094590275244876""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 4.094590275244876
""",
)

entry(
    index = 107,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_3O-u1",
    kinetics = Arrhenius(A=(0.150831,'m^3/(mol*s)'), n=2.7069, Ea=(309.92,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_N-3O-u1",
    kinetics = Arrhenius(A=(0.00138537,'m^3/(mol*s)'), n=3.40706, Ea=(311.856,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(7.34706e+06,'m^3/(mol*s)'), n=0.500473, w0=(523.911,'kJ/mol'), E0=(194.873,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.32318766780312097, var=173.1436760225006, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
    Total Standard Deviation in ln(k): 27.191149486445777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 27.191149486445777""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 27.191149486445777
""",
)

entry(
    index = 110,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.71804e+08,'m^3/(mol*s)'), n=0.124959, w0=(450.988,'kJ/mol'), E0=(130.399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4956045532959031, var=17.280282255833804, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
    Total Standard Deviation in ln(k): 9.578832855203533"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.578832855203533""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.578832855203533
""",
)

entry(
    index = 111,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(0.0305183,'m^3/(mol*s)'), n=2.6347, w0=(545.982,'kJ/mol'), E0=(85.5715,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9445157623872901, var=21.350498904769942, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 11.636354379594744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.636354379594744""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.636354379594744
""",
)

entry(
    index = 112,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_3O-u1",
    kinetics = Arrhenius(A=(0.00474579,'m^3/(mol*s)'), n=2.96408, Ea=(334.468,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_N-3O-u1",
    kinetics = Arrhenius(A=(1.32859,'m^3/(mol*s)'), n=2.43214, Ea=(338.639,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O_Ext-1BrCClFHILiNPSSi-R",
    kinetics = Arrhenius(A=(0.0952393,'m^3/(mol*s)'), n=2.75763, Ea=(322.353,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O",
    kinetics = Arrhenius(A=(0.00466877,'m^3/(mol*s)'), n=2.7407, Ea=(1.59476,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(0.367477,'m^3/(mol*s)'), n=2.16709, w0=(320,'kJ/mol'), E0=(90.9595,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4269663786227196, var=1.0392454131872333, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O
    Total Standard Deviation in ln(k): 3.116474681977859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.116474681977859""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.116474681977859
""",
)

entry(
    index = 117,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F",
    kinetics = ArrheniusBM(A=(2.79268e-11,'m^3/(mol*s)'), n=5.28536, w0=(525,'kJ/mol'), E0=(147.697,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37644661954639425, var=3.584967747684189, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F
    Total Standard Deviation in ln(k): 4.741613390255667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F
Total Standard Deviation in ln(k): 4.741613390255667""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F
Total Standard Deviation in ln(k): 4.741613390255667
""",
)

entry(
    index = 118,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.84312e-15,'m^3/(mol*s)'), n=6.60345, w0=(525,'kJ/mol'), E0=(130.484,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15234348232618908, var=2.925375888215434, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.8116173693958872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.8116173693958872""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.8116173693958872
""",
)

entry(
    index = 119,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H",
    kinetics = ArrheniusBM(A=(1.18582e-13,'m^3/(mol*s)'), n=5.3127, w0=(525,'kJ/mol'), E0=(148.575,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3702934613959977, var=9.118774873168077, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H
    Total Standard Deviation in ln(k): 6.98414609560603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H
Total Standard Deviation in ln(k): 6.98414609560603""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H
Total Standard Deviation in ln(k): 6.98414609560603
""",
)

entry(
    index = 120,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H",
    kinetics = ArrheniusBM(A=(1.04239e-06,'m^3/(mol*s)'), n=3.76371, w0=(485,'kJ/mol'), E0=(179.665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007412700752238956, var=3.2119615291974384, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H
    Total Standard Deviation in ln(k): 3.6115002815264687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H
Total Standard Deviation in ln(k): 3.6115002815264687""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H
Total Standard Deviation in ln(k): 3.6115002815264687
""",
)

entry(
    index = 121,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.24207e-07,'m^3/(mol*s)'), n=4.41751, w0=(485,'kJ/mol'), E0=(146.158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05122312198697959, var=0.1080714617878249, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.7877424158271108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.7877424158271108""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.7877424158271108
""",
)

entry(
    index = 122,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(2.19996e-06,'m^3/(mol*s)'), n=3.79688, w0=(485,'kJ/mol'), E0=(176.429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.35451023191418146, var=33.37437654867911, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 12.472196123677367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 12.472196123677367""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 12.472196123677367
""",
)

entry(
    index = 123,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = Arrhenius(A=(1.71492e-09,'m^3/(mol*s)'), n=4.37345, Ea=(38.987,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl",
    kinetics = Arrhenius(A=(1580.64,'m^3/(mol*s)'), n=1.06012, Ea=(335.653,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl",
    kinetics = Arrhenius(A=(10572.3,'m^3/(mol*s)'), n=0.709227, Ea=(414.376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(95937.8,'m^3/(mol*s)'), n=1.12113, w0=(537.677,'kJ/mol'), E0=(112.975,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0977951336059821, var=3.7627866438389534, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 6.647045009245518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R
Total Standard Deviation in ln(k): 6.647045009245518""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R
Total Standard Deviation in ln(k): 6.647045009245518
""",
)

entry(
    index = 127,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C",
    kinetics = Arrhenius(A=(8.19658e-06,'m^3/(mol*s)'), n=3.30549, Ea=(14.6127,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C",
    kinetics = Arrhenius(A=(9.46969e-05,'m^3/(mol*s)'), n=2.97971, Ea=(38.0472,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi",
    kinetics = ArrheniusBM(A=(1.9354e-06,'m^3/(mol*s)'), n=3.35153, w0=(353.5,'kJ/mol'), E0=(87.5501,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08060586971265142, var=0.2695473539050901, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
    Total Standard Deviation in ln(k): 1.24334466727196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 1.24334466727196""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 1.24334466727196
""",
)

entry(
    index = 130,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi",
    kinetics = Arrhenius(A=(2.22405e-05,'m^3/(mol*s)'), n=3.55361, Ea=(69.3276,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi",
    kinetics = ArrheniusBM(A=(2.61514e-08,'m^3/(mol*s)'), n=4.20257, w0=(353.5,'kJ/mol'), E0=(71.2531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.300877549879919, var=5.772145186621324, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi',), comment="""BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
    Total Standard Deviation in ln(k): 5.572407733441556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 5.572407733441556""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 5.572407733441556
""",
)

entry(
    index = 132,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi",
    kinetics = ArrheniusBM(A=(1.28376e-06,'m^3/(mol*s)'), n=3.80533, w0=(353.5,'kJ/mol'), E0=(91.2355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3011986818268108, var=0.7480616783873952, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
    Total Standard Deviation in ln(k): 2.49068718109164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 2.49068718109164""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 2.49068718109164
""",
)

entry(
    index = 133,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(0.000849095,'m^3/(mol*s)'), n=3.17369, Ea=(16.5921,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(0.01745,'m^3/(mol*s)'), n=2.59, Ea=(14.5,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(5.31199e+07,'m^3/(mol*s)'), n=0.114184, w0=(353.5,'kJ/mol'), E0=(73.8142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.4098110634336707, var=2.112126178257914, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 8.968314390866402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 8.968314390866402""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 8.968314390866402
""",
)

entry(
    index = 136,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C",
    kinetics = Arrhenius(A=(3.4878e-05,'m^3/(mol*s)'), n=3.33904, Ea=(-1.9829,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(2.37398e-06,'m^3/(mol*s)'), n=3.44245, w0=(353.5,'kJ/mol'), E0=(138.84,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08173554125667754, var=1.4686956063042604, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.6348991561565605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.6348991561565605""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.6348991561565605
""",
)

entry(
    index = 138,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C",
    kinetics = ArrheniusBM(A=(4.62436e-05,'m^3/(mol*s)'), n=3.71297, w0=(617.272,'kJ/mol'), E0=(142.63,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.9915745234073474, var=0.016786657397153654, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C
    Total Standard Deviation in ln(k): 5.2636962484484116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C
Total Standard Deviation in ln(k): 5.2636962484484116""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C
Total Standard Deviation in ln(k): 5.2636962484484116
""",
)

entry(
    index = 139,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C",
    kinetics = Arrhenius(A=(6.89986e-05,'m^3/(mol*s)'), n=3.39582, Ea=(363.722,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-1BrCClFHILiNPSSi-R",
    kinetics = Arrhenius(A=(0.000536923,'m^3/(mol*s)'), n=3.25677, Ea=(343.511,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-5R!H-R",
    kinetics = Arrhenius(A=(5.69582e-06,'m^3/(mol*s)'), n=3.94767, Ea=(359.86,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->Cl",
    kinetics = Arrhenius(A=(6.65995e-06,'m^3/(mol*s)'), n=3.94804, Ea=(353.81,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->Cl",
    kinetics = Arrhenius(A=(5.27349e-06,'m^3/(mol*s)'), n=3.9638, Ea=(356.126,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3954.34,'m^3/(mol*s)'), n=1.23637, w0=(483.897,'kJ/mol'), E0=(135.861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6118504557319827, var=15.600511792102608, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C
    Total Standard Deviation in ln(k): 9.455511707019546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C
Total Standard Deviation in ln(k): 9.455511707019546""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C
Total Standard Deviation in ln(k): 9.455511707019546
""",
)

entry(
    index = 145,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->C",
    kinetics = Arrhenius(A=(4.6139e-06,'m^3/(mol*s)'), n=3.99356, Ea=(285.397,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R",
    kinetics = ArrheniusBM(A=(1473.32,'m^3/(mol*s)'), n=1.53069, w0=(572.376,'kJ/mol'), E0=(138.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18234139013393258, var=1.1314026178879222, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R
    Total Standard Deviation in ln(k): 2.5905290008300557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R
Total Standard Deviation in ln(k): 2.5905290008300557""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R
Total Standard Deviation in ln(k): 2.5905290008300557
""",
)

entry(
    index = 147,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->O",
    kinetics = Arrhenius(A=(0.0215072,'m^3/(mol*s)'), n=2.81865, Ea=(345.137,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->O",
    kinetics = Arrhenius(A=(0.0117015,'m^3/(mol*s)'), n=2.97295, Ea=(341.858,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O",
    kinetics = ArrheniusBM(A=(129.46,'m^3/(mol*s)'), n=1.91437, w0=(516.197,'kJ/mol'), E0=(146.91,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.500881504287154, var=1.8436248984566281, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O
    Total Standard Deviation in ln(k): 14.03077978236402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 14.03077978236402""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 14.03077978236402
""",
)

entry(
    index = 150,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(3599.34,'m^3/(mol*s)'), n=1.55064, w0=(538.572,'kJ/mol'), E0=(143.431,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3651980542804876, var=3.113032748976634, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O
    Total Standard Deviation in ln(k): 4.454695234230703"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.454695234230703""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.454695234230703
""",
)

entry(
    index = 151,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-4CClO-R",
    kinetics = Arrhenius(A=(0.000377996,'m^3/(mol*s)'), n=3.50982, Ea=(274.491,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-4CClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-4CClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-4CClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-4CClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(0.311697,'m^3/(mol*s)'), n=2.70001, w0=(525.579,'kJ/mol'), E0=(134.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.613045669712701, var=1.0567151485671513, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 11.138804719055184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.138804719055184""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.138804719055184
""",
)

entry(
    index = 153,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1",
    kinetics = Arrhenius(A=(0.293027,'m^3/(mol*s)'), n=2.5626, Ea=(315.7,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1",
    kinetics = Arrhenius(A=(0.00232171,'m^3/(mol*s)'), n=3.27276, Ea=(391.736,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(179181,'m^3/(mol*s)'), n=1.15682, w0=(445.564,'kJ/mol'), E0=(90.6944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.762092353517561, var=55.1409848301664, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 24.339049801163583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 24.339049801163583""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 24.339049801163583
""",
)

entry(
    index = 156,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(0.0016621,'m^3/(mol*s)'), n=3.0107, w0=(454.917,'kJ/mol'), E0=(95.1685,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012700588622072123, var=0.38467076258227556, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 1.2752844453945393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 1.2752844453945393""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 1.2752844453945393
""",
)

entry(
    index = 157,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1",
    kinetics = Arrhenius(A=(0.00100398,'m^3/(mol*s)'), n=3.43964, Ea=(291.755,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_5R!H->C",
    kinetics = Arrhenius(A=(0.00878609,'m^3/(mol*s)'), n=2.78929, Ea=(385.041,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_N-5R!H->C",
    kinetics = Arrhenius(A=(0.0446012,'m^3/(mol*s)'), n=2.65475, Ea=(354.674,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R",
    kinetics = Arrhenius(A=(0.00965,'m^3/(mol*s)'), n=2.58, Ea=(-2.9,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R",
    kinetics = ArrheniusBM(A=(2.32389e-06,'m^3/(mol*s)'), n=3.87693, w0=(525,'kJ/mol'), E0=(162.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40405999795608166, var=4.002554801517662, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R
    Total Standard Deviation in ln(k): 5.025976500973894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R
Total Standard Deviation in ln(k): 5.025976500973894""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R
Total Standard Deviation in ln(k): 5.025976500973894
""",
)

entry(
    index = 162,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(2.9666e-18,'m^3/(mol*s)'), n=7.56742, w0=(525,'kJ/mol'), E0=(130.52,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.395582393445104, var=0.043976089626396805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi
    Total Standard Deviation in ln(k): 1.4143281155208571"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.4143281155208571""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.4143281155208571
""",
)

entry(
    index = 163,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(3.80103e-14,'m^3/(mol*s)'), n=6.17941, w0=(525,'kJ/mol'), E0=(131.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11673683874616232, var=4.662208891084248, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.621962446416388"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.621962446416388""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.621962446416388
""",
)

entry(
    index = 164,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.19034e-14,'m^3/(mol*s)'), n=5.39126, w0=(525,'kJ/mol'), E0=(148.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3840324545830174, var=9.046687911063866, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R
    Total Standard Deviation in ln(k): 6.9946902006784315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.9946902006784315""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.9946902006784315
""",
)

entry(
    index = 165,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.424e-07,'m^3/(mol*s)'), n=3.77581, w0=(485,'kJ/mol'), E0=(179.648,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014576582766849186, var=3.282066559332953, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 3.668497812886519"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R
Total Standard Deviation in ln(k): 3.668497812886519""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R
Total Standard Deviation in ln(k): 3.668497812886519
""",
)

entry(
    index = 166,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(4.97708e-05,'m^3/(mol*s)'), n=3.41316, w0=(485,'kJ/mol'), E0=(181.191,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27402816800655555, var=0.9608410816184075, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.653604457873284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.653604457873284""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.653604457873284
""",
)

entry(
    index = 167,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(1.04396e-05,'m^3/(mol*s)'), n=3.41775, w0=(485,'kJ/mol'), E0=(178.695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23338912873570206, var=0.33630969359875873, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 1.748995111163405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.748995111163405""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.748995111163405
""",
)

entry(
    index = 168,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(7.83905e-10,'m^3/(mol*s)'), n=5.14485, w0=(485,'kJ/mol'), E0=(139.646,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06543906391629399, var=0.010784333405783839, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 0.3726067755455739"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 0.3726067755455739""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 0.3726067755455739
""",
)

entry(
    index = 169,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O",
    kinetics = Arrhenius(A=(8.68377e-05,'m^3/(mol*s)'), n=3.62888, Ea=(113.847,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    kinetics = Arrhenius(A=(2.08267e-06,'m^3/(mol*s)'), n=3.44277, Ea=(150.042,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    kinetics = Arrhenius(A=(4.03653e-08,'m^3/(mol*s)'), n=4.6553, Ea=(145.869,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.37932e+06,'m^3/(mol*s)'), n=0.66935, w0=(551.845,'kJ/mol'), E0=(122.424,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3871896484001986, var=3.3833944450647446, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 7.172911964232999"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.172911964232999""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.172911964232999
""",
)

entry(
    index = 173,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-4BrCFILiNOPSSi-R",
    kinetics = Arrhenius(A=(8.83229e-06,'m^3/(mol*s)'), n=3.59735, Ea=(26.6715,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-4BrCFILiNOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-4BrCFILiNOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R",
    kinetics = ArrheniusBM(A=(2.62839e-06,'m^3/(mol*s)'), n=3.30957, w0=(353.5,'kJ/mol'), E0=(87.9188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.7981402070946664, var=5.079888294401149, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R
    Total Standard Deviation in ln(k): 14.061459558289352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 14.061459558289352""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 14.061459558289352
""",
)

entry(
    index = 175,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(1.50169e-06,'m^3/(mol*s)'), n=3.68796, w0=(353.5,'kJ/mol'), E0=(71.2531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4125518008092134, var=13.999319270310522, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 8.537411758835901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 8.537411758835901""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 8.537411758835901
""",
)

entry(
    index = 176,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000699968,'m^3/(mol*s)'), n=2.91672, w0=(353.5,'kJ/mol'), E0=(109.953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02044856676778577, var=0.4203584512130511, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 1.3511494225008729"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 1.3511494225008729""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 1.3511494225008729
""",
)

entry(
    index = 177,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(1.07246e-05,'m^3/(mol*s)'), n=3.56773, w0=(353.5,'kJ/mol'), E0=(105.004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.8326103930978597, var=0.1747598363939161, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 5.442613920297297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 5.442613920297297""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 5.442613920297297
""",
)

entry(
    index = 178,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(7.08191e-06,'m^3/(mol*s)'), n=3.53568, w0=(353.5,'kJ/mol'), E0=(71.7831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23723961574868335, var=1.8951358372293035, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 3.355876584738528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 3.355876584738528""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 3.355876584738528
""",
)

entry(
    index = 179,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R",
    kinetics = Arrhenius(A=(0.654199,'m^3/(mol*s)'), n=2.29326, Ea=(-20.2924,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = Arrhenius(A=(0.000214,'m^3/(mol*s)'), n=2.82, Ea=(37,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O",
    kinetics = Arrhenius(A=(0.000778,'m^3/(mol*s)'), n=2.78, Ea=(45.3,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O",
    kinetics = Arrhenius(A=(0.000591,'m^3/(mol*s)'), n=2.76, Ea=(32.1,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C_Ext-1BrCClFHILiNPSSi-R",
    kinetics = Arrhenius(A=(8.38302e-05,'m^3/(mol*s)'), n=3.60203, Ea=(402.485,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C_Ext-5C-R",
    kinetics = Arrhenius(A=(1.37515e-06,'m^3/(mol*s)'), n=3.75034, Ea=(292.69,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_4BrCClFILiNPSSi->C_Ext-1CClF-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_Ext-1CClF-R",
    kinetics = Arrhenius(A=(2.05616,'m^3/(mol*s)'), n=2.3798, Ea=(393.249,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_Ext-1CClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_Ext-1CClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_Ext-1CClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_Ext-1CClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_5R!H->O",
    kinetics = Arrhenius(A=(0.285485,'m^3/(mol*s)'), n=2.54097, Ea=(361.717,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_N-5R!H->O",
    kinetics = Arrhenius(A=(0.340714,'m^3/(mol*s)'), n=2.59484, Ea=(375.342,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->H_N-4BrCClFILiNPSSi->C_Ext-1CClF-R_Ext-1CClF-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_3O-u1",
    kinetics = Arrhenius(A=(4.84958,'m^3/(mol*s)'), n=2.26492, Ea=(330.08,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_N-3O-u1",
    kinetics = Arrhenius(A=(0.0378484,'m^3/(mol*s)'), n=2.98508, Ea=(334.916,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(115363,'m^3/(mol*s)'), n=1.12249, w0=(546.832,'kJ/mol'), E0=(148.702,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.1868485869910725, var=5.694860985883006, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 12.791238571809323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 12.791238571809323""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 12.791238571809323
""",
)

entry(
    index = 191,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_3O-u1",
    kinetics = Arrhenius(A=(4.39416,'m^3/(mol*s)'), n=2.31879, Ea=(345.504,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_N-3O-u1",
    kinetics = Arrhenius(A=(0.0372336,'m^3/(mol*s)'), n=3.03896, Ea=(345.74,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_3O-u1",
    kinetics = Arrhenius(A=(0.0379121,'m^3/(mol*s)'), n=2.90824, Ea=(340.726,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-3O-u1",
    kinetics = Arrhenius(A=(7.30096,'m^3/(mol*s)'), n=2.36151, Ea=(340.16,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C",
    kinetics = ArrheniusBM(A=(756.715,'m^3/(mol*s)'), n=1.83816, w0=(441.629,'kJ/mol'), E0=(74.3855,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2850752845041122, var=6.8214777909349396, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C
    Total Standard Deviation in ln(k): 5.952228402375098"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C
Total Standard Deviation in ln(k): 5.952228402375098""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C
Total Standard Deviation in ln(k): 5.952228402375098
""",
)

entry(
    index = 196,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-4CClO->C",
    kinetics = Arrhenius(A=(0.0308105,'m^3/(mol*s)'), n=2.88761, Ea=(284.829,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-4CClO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-4CClO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-4CClO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_N-4CClO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_4CClO->Cl",
    kinetics = Arrhenius(A=(0.00381903,'m^3/(mol*s)'), n=3.24993, Ea=(296.719,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_4CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_4CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl",
    kinetics = ArrheniusBM(A=(0.00138831,'m^3/(mol*s)'), n=3.03137, w0=(451.849,'kJ/mol'), E0=(94.5326,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2340709293031898, var=0.368401769276447, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl
    Total Standard Deviation in ln(k): 1.804914107994061"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.804914107994061""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.804914107994061
""",
)

entry(
    index = 199,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F",
    kinetics = ArrheniusBM(A=(5.97564e-06,'m^3/(mol*s)'), n=3.74007, w0=(525,'kJ/mol'), E0=(165.942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4150244031115669, var=3.608170756711941, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F
    Total Standard Deviation in ln(k): 4.850806367961699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F
Total Standard Deviation in ln(k): 4.850806367961699""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F
Total Standard Deviation in ln(k): 4.850806367961699
""",
)

entry(
    index = 200,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5.86193e-10,'m^3/(mol*s)'), n=4.99656, w0=(525,'kJ/mol'), E0=(142.536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.942309401540616, var=6.107335727119699, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F
    Total Standard Deviation in ln(k): 7.321918240717532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.321918240717532""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.321918240717532
""",
)

entry(
    index = 201,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_Ext-1CH-R",
    kinetics = Arrhenius(A=(2.80067e-20,'m^3/(mol*s)'), n=8.17077, Ea=(92.4857,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_Ext-1CH-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_Ext-1CH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_Ext-1CH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_Ext-1CH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_4BrCClILiNOPSSi->C",
    kinetics = Arrhenius(A=(5.18265e-09,'m^3/(mol*s)'), n=4.74784, Ea=(92.3732,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_4BrCClILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_4BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_4BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_4BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(4.38288e-15,'m^3/(mol*s)'), n=6.43501, w0=(525,'kJ/mol'), E0=(132.023,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10674425072183095, var=6.3647074770912955, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 5.325821840291846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 5.325821840291846""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 5.325821840291846
""",
)

entry(
    index = 204,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.07764e-15,'m^3/(mol*s)'), n=5.8779, w0=(525,'kJ/mol'), E0=(145.919,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.42368027563824207, var=0.07431184928331434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 1.6110180930707172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.6110180930707172""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.6110180930707172
""",
)

entry(
    index = 205,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.86208e-13,'m^3/(mol*s)'), n=5.16672, w0=(525,'kJ/mol'), E0=(149.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.36564992667144414, var=11.275525272071992, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 7.650428134761871"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.650428134761871""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.650428134761871
""",
)

entry(
    index = 206,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0",
    kinetics = ArrheniusBM(A=(8.64117e-07,'m^3/(mol*s)'), n=3.78655, w0=(485,'kJ/mol'), E0=(179.584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.013163609070124531, var=3.267380385706902, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0',), comment="""BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0
    Total Standard Deviation in ln(k): 3.6568127953385603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.6568127953385603""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.6568127953385603
""",
)

entry(
    index = 207,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0",
    kinetics = ArrheniusBM(A=(226.688,'m^3/(mol*s)'), n=1.41927, w0=(485,'kJ/mol'), E0=(172.862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47620234355768565, var=9.700063729749633, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0
    Total Standard Deviation in ln(k): 7.440220726891817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.440220726891817""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.440220726891817
""",
)

entry(
    index = 208,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.8148e-05,'m^3/(mol*s)'), n=3.38383, w0=(485,'kJ/mol'), E0=(179.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2149616755423776, var=2.1237975861441516, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.974219057081745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.974219057081745""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.974219057081745
""",
)

entry(
    index = 209,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->C",
    kinetics = Arrhenius(A=(3.70857e-08,'m^3/(mol*s)'), n=4.36701, Ea=(151.162,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C",
    kinetics = Arrhenius(A=(3.95e-05,'m^3/(mol*s)'), n=3.43, Ea=(162.6,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.48449e-05,'m^3/(mol*s)'), n=3.39528, w0=(485,'kJ/mol'), E0=(181.012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28400779759955946, var=0.7833768206762775, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.487949921251478"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.487949921251478""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.487949921251478
""",
)

entry(
    index = 212,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.26291e-08,'m^3/(mol*s)'), n=4.37484, w0=(485,'kJ/mol'), E0=(173.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24436438432484842, var=0.014235358056965935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 0.8531698562865659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562865659""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562865659
""",
)

entry(
    index = 213,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.972e-05,'m^3/(mol*s)'), n=3.28397, w0=(485,'kJ/mol'), E0=(175.447,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1309384567838479, var=3.765453001855312, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.731697260808542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808542""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808542
""",
)

entry(
    index = 214,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C",
    kinetics = Arrhenius(A=(1.10332e-07,'m^3/(mol*s)'), n=4.39237, Ea=(82.6735,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C",
    kinetics = Arrhenius(A=(4.88042e-12,'m^3/(mol*s)'), n=5.91377, Ea=(84.5653,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = Arrhenius(A=(363.313,'m^3/(mol*s)'), n=1.87359, Ea=(383.25,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O",
    kinetics = Arrhenius(A=(14.1008,'m^3/(mol*s)'), n=2.18545, Ea=(351.113,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O",
    kinetics = Arrhenius(A=(71.772,'m^3/(mol*s)'), n=2.09863, Ea=(369.342,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_6R!H->C",
    kinetics = Arrhenius(A=(3.20903e-06,'m^3/(mol*s)'), n=3.28294, Ea=(7.36724,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_N-6R!H->C",
    kinetics = Arrhenius(A=(0.000106385,'m^3/(mol*s)'), n=3.20001, Ea=(29.559,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(5.43645e-05,'m^3/(mol*s)'), n=3.30995, w0=(353.5,'kJ/mol'), E0=(54.0853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.022278827634059497, var=14.297730921184465, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 7.6363494845055735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.6363494845055735""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.6363494845055735
""",
)

entry(
    index = 222,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R",
    kinetics = Arrhenius(A=(0.000106567,'m^3/(mol*s)'), n=3.23582, Ea=(26.4898,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(5.62416e-08,'m^3/(mol*s)'), n=4.11181, w0=(353.5,'kJ/mol'), E0=(79.5433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06842685732619386, var=0.9569025378983865, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 2.132986602032815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 2.132986602032815""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 2.132986602032815
""",
)

entry(
    index = 224,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_4FO->O",
    kinetics = Arrhenius(A=(0.000118485,'m^3/(mol*s)'), n=3.29853, Ea=(18.3298,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(0.0008528,'m^3/(mol*s)'), n=2.86905, w0=(353.5,'kJ/mol'), E0=(110.115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06865433287569553, var=0.3243580944239947, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 1.3142439578429428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 1.3142439578429428""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 1.3142439578429428
""",
)

entry(
    index = 226,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->C",
    kinetics = Arrhenius(A=(2.82278e-05,'m^3/(mol*s)'), n=3.44719, Ea=(10.5481,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->C",
    kinetics = Arrhenius(A=(0.000485841,'m^3/(mol*s)'), n=3.11646, Ea=(24.7919,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000246125,'m^3/(mol*s)'), n=3.06199, w0=(353.5,'kJ/mol'), E0=(76.3786,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4570344334553054, var=5.187466670680603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 5.714314495703311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 5.714314495703311""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 5.714314495703311
""",
)

entry(
    index = 229,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_3O-u1",
    kinetics = Arrhenius(A=(34.915,'m^3/(mol*s)'), n=2.08375, Ea=(350.612,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_N-3O-u1",
    kinetics = Arrhenius(A=(0.129776,'m^3/(mol*s)'), n=2.87392, Ea=(363.248,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C_Ext-1BrCClFHILiNPSSi-R",
    kinetics = Arrhenius(A=(335.275,'m^3/(mol*s)'), n=1.93926, Ea=(285.888,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(0.00207323,'m^3/(mol*s)'), n=3.1934, w0=(458.749,'kJ/mol'), E0=(120.394,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.5576159077772016, var=0.1089186653459663, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
    Total Standard Deviation in ln(k): 9.600352705303365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 9.600352705303365""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 9.600352705303365
""",
)

entry(
    index = 233,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C",
    kinetics = Arrhenius(A=(0.00108931,'m^3/(mol*s)'), n=3.05784, Ea=(278.107,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C",
    kinetics = Arrhenius(A=(0.00678858,'m^3/(mol*s)'), n=3.1372, Ea=(304.788,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R",
    kinetics = ArrheniusBM(A=(6.65295e-06,'m^3/(mol*s)'), n=3.72603, w0=(525,'kJ/mol'), E0=(166.297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41260525469106635, var=3.7669443542444627, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R
    Total Standard Deviation in ln(k): 4.927610261596007"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R
Total Standard Deviation in ln(k): 4.927610261596007""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R
Total Standard Deviation in ln(k): 4.927610261596007
""",
)

entry(
    index = 236,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClILiNOPSSi->C",
    kinetics = Arrhenius(A=(1.84865e-10,'m^3/(mol*s)'), n=5.13872, Ea=(109.875,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClILiNOPSSi->C",
    kinetics = Arrhenius(A=(6.15e-07,'m^3/(mol*s)'), n=4.14, Ea=(134.9,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_Ext-1CH-R",
    kinetics = Arrhenius(A=(7.71142e-12,'m^3/(mol*s)'), n=5.47558, Ea=(94.535,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_Ext-1CH-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_Ext-1CH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_Ext-1CH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_Ext-1CH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_4ClO->Cl",
    kinetics = Arrhenius(A=(3.57367e-11,'m^3/(mol*s)'), n=5.32561, Ea=(91.9755,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_N-4ClO->Cl",
    kinetics = Arrhenius(A=(3.31829e-08,'m^3/(mol*s)'), n=4.48236, Ea=(100.723,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_N-4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_N-4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIILiLiNNOOPPSSSiSi=1BrBrCCCCClClHHIILiLiNNOOPPSSSiSi_N-4BrCClILiNOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = Arrhenius(A=(1.14861e-16,'m^3/(mol*s)'), n=6.26453, Ea=(226.951,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R",
    kinetics = ArrheniusBM(A=(1.72885e-13,'m^3/(mol*s)'), n=5.12494, w0=(525,'kJ/mol'), E0=(157.534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5026459121417589, var=13.964931867927021, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
    Total Standard Deviation in ln(k): 8.75456080601361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 8.75456080601361""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 8.75456080601361
""",
)

entry(
    index = 243,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.08155e-09,'m^3/(mol*s)'), n=4.21534, w0=(525,'kJ/mol'), E0=(162.625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4865493331260655, var=9.40905345250733, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 7.371846310105829"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.371846310105829""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.371846310105829
""",
)

entry(
    index = 244,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C",
    kinetics = Arrhenius(A=(8.646e-12,'m^3/(mol*s)'), n=4.97681, Ea=(192.02,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(4.63342e-27,'m^3/(mol*s)'), n=9.35066, w0=(525,'kJ/mol'), E0=(96.8823,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43792551417774783, var=0.5664277340248023, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 2.6091069159789475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.6091069159789475""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.6091069159789475
""",
)

entry(
    index = 246,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.40719e-05,'m^3/(mol*s)'), n=3.45455, w0=(485,'kJ/mol'), E0=(188.572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09857246156252143, var=6.096048878875923, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 5.1973960845408405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.1973960845408405""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.1973960845408405
""",
)

entry(
    index = 247,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(7.98997e-08,'m^3/(mol*s)'), n=4.06507, w0=(485,'kJ/mol'), E0=(170.994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06281027432772715, var=0.5772293018171644, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 1.6809244244070463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.6809244244070463""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.6809244244070463
""",
)

entry(
    index = 248,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(6.93639e-07,'m^3/(mol*s)'), n=3.84128, w0=(485,'kJ/mol'), E0=(181.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.176144747222762, var=1.3084767616509505, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 2.7357645156060055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.7357645156060055""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.7357645156060055
""",
)

entry(
    index = 249,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(86.3165,'m^3/(mol*s)'), n=1.5824, w0=(485,'kJ/mol'), E0=(174.861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.403955761195503, var=13.200384990895312, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 8.29863467980091"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.29863467980091""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.29863467980091
""",
)

entry(
    index = 250,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C",
    kinetics = Arrhenius(A=(1.28573e-06,'m^3/(mol*s)'), n=3.56699, Ea=(285.117,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C",
    kinetics = Arrhenius(A=(4.362e-07,'m^3/(mol*s)'), n=3.96684, Ea=(150.338,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C",
    kinetics = Arrhenius(A=(8.35e-05,'m^3/(mol*s)'), n=3.36, Ea=(157.1,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(3.34e-05,'m^3/(mol*s)'), n=3.35, Ea=(144.6,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(6.36303e-10,'m^3/(mol*s)'), n=4.82658, w0=(485,'kJ/mol'), E0=(166.608,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47458481579291606, var=0.005426392301836482, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 1.3401010657982133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.3401010657982133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.3401010657982133
""",
)

entry(
    index = 255,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C",
    kinetics = Arrhenius(A=(1.35e-05,'m^3/(mol*s)'), n=3.34, Ea=(146.4,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R",
    kinetics = Arrhenius(A=(2.894e-08,'m^3/(mol*s)'), n=4.35365, Ea=(170.388,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O",
    kinetics = Arrhenius(A=(7.33269e-08,'m^3/(mol*s)'), n=4.23045, Ea=(159.023,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O",
    kinetics = Arrhenius(A=(2.43e-05,'m^3/(mol*s)'), n=3.25, Ea=(157.6,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = Arrhenius(A=(0.000166381,'m^3/(mol*s)'), n=3.31384, Ea=(-1.84829,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH",
    kinetics = ArrheniusBM(A=(3.84196e-06,'m^3/(mol*s)'), n=3.49798, w0=(353.5,'kJ/mol'), E0=(56.4557,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.6652033095404635, var=4.32018186703623, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 10.863342046260296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 10.863342046260296""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 10.863342046260296
""",
)

entry(
    index = 261,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH",
    kinetics = ArrheniusBM(A=(8.83137e-13,'m^3/(mol*s)'), n=5.47481, w0=(353.5,'kJ/mol'), E0=(67.1992,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.7638179571249575, var=0.19982645905099033, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 7.8404219534236415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.8404219534236415""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.8404219534236415
""",
)

entry(
    index = 262,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000211362,'m^3/(mol*s)'), n=3.09043, w0=(353.5,'kJ/mol'), E0=(111.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003810689331870926, var=1.0722665147753083, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.085483833267909"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.085483833267909""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.085483833267909
""",
)

entry(
    index = 263,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.296927,'m^3/(mol*s)'), n=2.14524, w0=(353.5,'kJ/mol'), E0=(124.445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006604251724122879, var=0.21187080335441666, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 0.9393616409403694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R
Total Standard Deviation in ln(k): 0.9393616409403694""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R
Total Standard Deviation in ln(k): 0.9393616409403694
""",
)

entry(
    index = 264,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->O",
    kinetics = Arrhenius(A=(0.00357,'m^3/(mol*s)'), n=2.6, Ea=(0.3,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->O",
    kinetics = Arrhenius(A=(0.02065,'m^3/(mol*s)'), n=2.64, Ea=(7.3,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R",
    kinetics = Arrhenius(A=(0.00185843,'m^3/(mol*s)'), n=3.22261, Ea=(297.595,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.42162e-06,'m^3/(mol*s)'), n=3.86841, w0=(525,'kJ/mol'), E0=(163.125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41486137507992005, var=5.691383862058191, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C
    Total Standard Deviation in ln(k): 5.824985845539739"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C
Total Standard Deviation in ln(k): 5.824985845539739""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C
Total Standard Deviation in ln(k): 5.824985845539739
""",
)

entry(
    index = 268,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00402118,'m^3/(mol*s)'), n=3.10034, w0=(525,'kJ/mol'), E0=(178.333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08508954654125657, var=0.39720517041394754, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.477261380280157"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.477261380280157""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.477261380280157
""",
)

entry(
    index = 269,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.45642e-12,'m^3/(mol*s)'), n=4.72226, w0=(525,'kJ/mol'), E0=(161.06,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.552880753523329, var=8.701294257574109, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R
    Total Standard Deviation in ln(k): 7.302706392117452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.302706392117452""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.302706392117452
""",
)

entry(
    index = 270,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C",
    kinetics = Arrhenius(A=(1.65359e-14,'m^3/(mol*s)'), n=5.65246, Ea=(171.372,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(1.76419e-08,'m^3/(mol*s)'), n=3.82916, w0=(525,'kJ/mol'), E0=(174.017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12119846539817775, var=1.139948657052627, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 2.4449418854080007"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.4449418854080007""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.4449418854080007
""",
)

entry(
    index = 272,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(3.11488e-10,'m^3/(mol*s)'), n=4.50478, w0=(525,'kJ/mol'), E0=(139.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6312385292942005, var=0.5298110164818906, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 3.0452353951331945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 3.0452353951331945""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 3.0452353951331945
""",
)

entry(
    index = 273,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O",
    kinetics = Arrhenius(A=(5.00048e-45,'m^3/(mol*s)'), n=14.5269, Ea=(79.3637,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.00181e-06,'m^3/(mol*s)'), n=3.59463, w0=(485,'kJ/mol'), E0=(184.963,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07127627324154742, var=7.21234588559805, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 5.562964763302266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.562964763302266""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.562964763302266
""",
)

entry(
    index = 275,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000112376,'m^3/(mol*s)'), n=3.34717, w0=(485,'kJ/mol'), E0=(193.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11649474195978293, var=6.5424633726299035, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 5.420459756312148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.420459756312148""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.420459756312148
""",
)

entry(
    index = 276,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F",
    kinetics = ArrheniusBM(A=(8.07218e-08,'m^3/(mol*s)'), n=4.09577, w0=(485,'kJ/mol'), E0=(171.561,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16555179720872834, var=1.1972657121953412, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
    Total Standard Deviation in ln(k): 2.6095331486906606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.6095331486906606""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.6095331486906606
""",
)

entry(
    index = 277,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(8.39473e-08,'m^3/(mol*s)'), n=4.02792, w0=(485,'kJ/mol'), E0=(170.508,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028020101044750674, var=0.06812965697886879, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
    Total Standard Deviation in ln(k): 0.5936713651043162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.5936713651043162""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.5936713651043162
""",
)

entry(
    index = 278,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C",
    kinetics = Arrhenius(A=(5.7299e-06,'m^3/(mol*s)'), n=3.76087, Ea=(211.861,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.78269e-07,'m^3/(mol*s)'), n=3.84344, w0=(485,'kJ/mol'), E0=(181.257,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1884418879326034, var=1.3243873239876631, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.780561869534053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.780561869534053""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.780561869534053
""",
)

entry(
    index = 280,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(18908.3,'m^3/(mol*s)'), n=0.817442, w0=(485,'kJ/mol'), E0=(176.149,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5132947172742112, var=34.97086510588117, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 13.144920498055807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.144920498055807""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.144920498055807
""",
)

entry(
    index = 281,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0158687,'m^3/(mol*s)'), n=2.79423, w0=(485,'kJ/mol'), E0=(172.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1575084340451626, var=8.568385324107183, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.263971138772191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772191""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772191
""",
)

entry(
    index = 282,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C",
    kinetics = Arrhenius(A=(3.19591e-10,'m^3/(mol*s)'), n=4.92231, Ea=(157.168,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C",
    kinetics = Arrhenius(A=(1.29256e-09,'m^3/(mol*s)'), n=4.72835, Ea=(149.894,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R",
    kinetics = Arrhenius(A=(4.11983e-05,'m^3/(mol*s)'), n=3.20075, Ea=(2.44607,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R",
    kinetics = Arrhenius(A=(0.00425626,'m^3/(mol*s)'), n=2.65728, Ea=(22.5481,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = Arrhenius(A=(0.00442,'m^3/(mol*s)'), n=2.67, Ea=(13.7,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O",
    kinetics = Arrhenius(A=(0.00765,'m^3/(mol*s)'), n=2.68, Ea=(18.8,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O",
    kinetics = Arrhenius(A=(0.00705,'m^3/(mol*s)'), n=2.66, Ea=(8.4,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = Arrhenius(A=(0.00175,'m^3/(mol*s)'), n=2.74, Ea=(8.1,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O",
    kinetics = Arrhenius(A=(0.00303,'m^3/(mol*s)'), n=2.77, Ea=(24.2,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O",
    kinetics = Arrhenius(A=(0.00212,'m^3/(mol*s)'), n=2.75, Ea=(15.6,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 292,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.00141278,'m^3/(mol*s)'), n=2.88157, w0=(525,'kJ/mol'), E0=(171.476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4221087960189235, var=24.145273027082244, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 10.911409976907715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 10.911409976907715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 10.911409976907715
""",
)

entry(
    index = 293,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.10667e-09,'m^3/(mol*s)'), n=4.67467, w0=(525,'kJ/mol'), E0=(156.356,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44384033024294384, var=1.188073194800202, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 3.3003132932249364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.3003132932249364""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.3003132932249364
""",
)

entry(
    index = 294,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.77849e-10,'m^3/(mol*s)'), n=3.79891, w0=(525,'kJ/mol'), E0=(168.767,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5227374995623407, var=47.320468367744056, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 15.10395824533181"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 15.10395824533181""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 15.10395824533181
""",
)

entry(
    index = 295,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.55352e-15,'m^3/(mol*s)'), n=5.47489, w0=(525,'kJ/mol'), E0=(154.848,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5382351976252426, var=1.1878227718063405, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.537256022316191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.537256022316191""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.537256022316191
""",
)

entry(
    index = 296,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O",
    kinetics = Arrhenius(A=(7.33133e-11,'m^3/(mol*s)'), n=4.61882, Ea=(195.681,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(1.95847e-08,'m^3/(mol*s)'), n=3.80315, w0=(525,'kJ/mol'), E0=(174.726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2723399473454678, var=0.5147314131167012, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 2.1225640895005102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 2.1225640895005102""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 2.1225640895005102
""",
)

entry(
    index = 298,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C",
    kinetics = Arrhenius(A=(1.10502e-10,'m^3/(mol*s)'), n=4.61742, Ea=(180.926,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C",
    kinetics = Arrhenius(A=(2.93442e-08,'m^3/(mol*s)'), n=4.04113, Ea=(190.261,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.58885e-06,'m^3/(mol*s)'), n=3.55742, w0=(485,'kJ/mol'), E0=(187.883,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05890870646334806, var=7.350701149170821, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 5.583284951983616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.583284951983616""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.583284951983616
""",
)

entry(
    index = 301,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C",
    kinetics = Arrhenius(A=(2.5027e-05,'m^3/(mol*s)'), n=3.59925, Ea=(209.739,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(1.59331e-06,'m^3/(mol*s)'), n=3.65749, w0=(485,'kJ/mol'), E0=(166.464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.1815956678024997, var=7.038092673642991, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 10.799838793496141"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.799838793496141""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.799838793496141
""",
)

entry(
    index = 303,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O",
    kinetics = ArrheniusBM(A=(0.16179,'m^3/(mol*s)'), n=2.43247, w0=(485,'kJ/mol'), E0=(190.562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28945350093143324, var=26.5743380003777, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
    Total Standard Deviation in ln(k): 11.061740288205169"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.061740288205169""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.061740288205169
""",
)

entry(
    index = 304,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(7.52261e-05,'m^3/(mol*s)'), n=3.39773, w0=(485,'kJ/mol'), E0=(193.259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09250282281970519, var=6.906895224575801, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
    Total Standard Deviation in ln(k): 5.5010579230533825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.5010579230533825""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.5010579230533825
""",
)

entry(
    index = 305,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.17542e-08,'m^3/(mol*s)'), n=4.12767, w0=(485,'kJ/mol'), E0=(171.42,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17797987717937938, var=1.2172290038287283, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 2.6589717772888206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.6589717772888206""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.6589717772888206
""",
)

entry(
    index = 306,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.34352e-08,'m^3/(mol*s)'), n=4.02818, w0=(485,'kJ/mol'), E0=(170.502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02698394495821771, var=0.06263505310594787, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 0.5695238252203216"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.5695238252203216""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.5695238252203216
""",
)

entry(
    index = 307,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C",
    kinetics = ArrheniusBM(A=(3.39606e-06,'m^3/(mol*s)'), n=3.80021, w0=(485,'kJ/mol'), E0=(174.472,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24993611629262338, var=0.04764147309766617, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
    Total Standard Deviation in ln(k): 1.0655522483929938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 1.0655522483929938""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 1.0655522483929938
""",
)

entry(
    index = 308,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C",
    kinetics = Arrhenius(A=(5.29538e-06,'m^3/(mol*s)'), n=3.74, Ea=(187.567,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.22395e-07,'m^3/(mol*s)'), n=3.97282, w0=(485,'kJ/mol'), E0=(180.817,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7406507997356162, var=2.81042003707395, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.221731173538159"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.221731173538159""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.221731173538159
""",
)

entry(
    index = 310,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00920803,'m^3/(mol*s)'), n=2.80941, w0=(485,'kJ/mol'), E0=(151.694,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.33265691981176637, var=4.254857720679769, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.971049889141976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.971049889141976""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.971049889141976
""",
)

entry(
    index = 311,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R",
    kinetics = Arrhenius(A=(1.71639e-05,'m^3/(mol*s)'), n=3.56319, Ea=(226.133,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(0.104833,'m^3/(mol*s)'), n=2.12, Ea=(147.266,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(0.001275,'m^3/(mol*s)'), n=3.12, Ea=(147.53,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C",
    kinetics = Arrhenius(A=(5.44367e-08,'m^3/(mol*s)'), n=2.98637, Ea=(209.666,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(6.71872e-09,'m^3/(mol*s)'), n=3.87148, Ea=(192.37,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.84546e-08,'m^3/(mol*s)'), n=3.73033, w0=(525,'kJ/mol'), E0=(177.279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7733021379689909, var=0.39722531548050655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 3.2064707849564407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.2064707849564407""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.2064707849564407
""",
)

entry(
    index = 317,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.68724e-05,'m^3/(mol*s)'), n=2.95314, w0=(485,'kJ/mol'), E0=(193.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0030046029818375135, var=14.743691214756588, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
    Total Standard Deviation in ln(k): 7.705233678445695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445695""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445695
""",
)

entry(
    index = 318,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.9682e-07,'m^3/(mol*s)'), n=3.83775, w0=(485,'kJ/mol'), E0=(185.213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07754259038300716, var=1.754056370544968, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 2.849917667314168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.849917667314168""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.849917667314168
""",
)

entry(
    index = 319,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R",
    kinetics = Arrhenius(A=(1.5333e-06,'m^3/(mol*s)'), n=3.65941, Ea=(175.65,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C",
    kinetics = Arrhenius(A=(1.21333e-05,'m^3/(mol*s)'), n=3.66599, Ea=(177.696,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C",
    kinetics = Arrhenius(A=(3.38922e-05,'m^3/(mol*s)'), n=3.5758, Ea=(187.056,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R",
    kinetics = Arrhenius(A=(0.00331206,'m^3/(mol*s)'), n=2.81802, Ea=(200.76,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.13873e-05,'m^3/(mol*s)'), n=3.55176, w0=(485,'kJ/mol'), E0=(193.142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027783554758651855, var=7.287454925482304, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 5.4816477011311795"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.4816477011311795""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.4816477011311795
""",
)

entry(
    index = 324,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R",
    kinetics = Arrhenius(A=(0.839925,'m^3/(mol*s)'), n=2.36463, Ea=(229.198,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.73445e-08,'m^3/(mol*s)'), n=4.20668, w0=(485,'kJ/mol'), E0=(169.253,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16996404036331322, var=1.1819907871117477, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.6065812692632426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.6065812692632426""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.6065812692632426
""",
)

entry(
    index = 326,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.84572e-07,'m^3/(mol*s)'), n=3.87954, w0=(485,'kJ/mol'), E0=(178.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9426493910441892, var=6.577083256780421, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 7.509774247558587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.509774247558587""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.509774247558587
""",
)

entry(
    index = 327,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C",
    kinetics = ArrheniusBM(A=(1.00712e-07,'m^3/(mol*s)'), n=4.01588, w0=(485,'kJ/mol'), E0=(170.299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10014952065474524, var=0.022957013107904888, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C
    Total Standard Deviation in ln(k): 0.5553808381252342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C
Total Standard Deviation in ln(k): 0.5553808381252342""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C
Total Standard Deviation in ln(k): 0.5553808381252342
""",
)

entry(
    index = 328,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C",
    kinetics = ArrheniusBM(A=(6.28296e-08,'m^3/(mol*s)'), n=4.04865, w0=(485,'kJ/mol'), E0=(170.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07071074193098331, var=0.23643662576607224, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C
    Total Standard Deviation in ln(k): 1.1524625889586742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C
Total Standard Deviation in ln(k): 1.1524625889586742""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C
Total Standard Deviation in ln(k): 1.1524625889586742
""",
)

entry(
    index = 329,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R",
    kinetics = Arrhenius(A=(4.51365e-06,'m^3/(mol*s)'), n=3.78897, Ea=(180.153,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(3.63e-05,'m^3/(mol*s)'), n=3.37, Ea=(183.4,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C",
    kinetics = Arrhenius(A=(3.56033e-08,'m^3/(mol*s)'), n=4.21745, Ea=(194.395,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(2.58576e-05,'m^3/(mol*s)'), n=3.2457, Ea=(188.78,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C",
    kinetics = Arrhenius(A=(4.47723e-05,'m^3/(mol*s)'), n=3.46134, Ea=(198.066,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(3.5032e-05,'m^3/(mol*s)'), n=3.5135, Ea=(211.783,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R",
    kinetics = Arrhenius(A=(0.000145249,'m^3/(mol*s)'), n=2.84864, Ea=(208.333,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O",
    kinetics = Arrhenius(A=(2.47232e-06,'m^3/(mol*s)'), n=3.97637, Ea=(171.25,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.86926e-07,'m^3/(mol*s)'), n=3.84755, w0=(485,'kJ/mol'), E0=(182.435,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09600916266032529, var=2.0878678233755616, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O
    Total Standard Deviation in ln(k): 3.1379622064188184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.1379622064188184""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.1379622064188184
""",
)

entry(
    index = 338,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.50053e-05,'m^3/(mol*s)'), n=3.79284, w0=(485,'kJ/mol'), E0=(187.083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00508873172663061, var=2.137679493011145, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
    Total Standard Deviation in ln(k): 2.9438698940949557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 2.9438698940949557""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 2.9438698940949557
""",
)

entry(
    index = 339,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(7.70507e-06,'m^3/(mol*s)'), n=3.51763, w0=(485,'kJ/mol'), E0=(196.685,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04959392142573586, var=1.7912645505918179, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 2.8077078165690104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8077078165690104""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8077078165690104
""",
)

entry(
    index = 340,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.63939e-08,'m^3/(mol*s)'), n=4.20067, w0=(485,'kJ/mol'), E0=(170.79,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22661832906730534, var=4.962422799104639, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.035240106288326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.035240106288326""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.035240106288326
""",
)

entry(
    index = 341,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.43184e-08,'m^3/(mol*s)'), n=4.29567, w0=(485,'kJ/mol'), E0=(166.374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14352505810456678, var=0.360092245132593, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 1.5636108663242028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663242028""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663242028
""",
)

entry(
    index = 342,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(5.94508e-05,'m^3/(mol*s)'), n=3.37621, w0=(485,'kJ/mol'), E0=(190.622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14501143760180207, var=0.5353198014536596, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 1.8311258333110643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.8311258333110643""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.8311258333110643
""",
)

entry(
    index = 343,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(2.46705e-07,'m^3/(mol*s)'), n=4.01497, w0=(485,'kJ/mol'), E0=(174.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8476407448011134, var=15.359050673686298, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 12.498995440909948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 12.498995440909948""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 12.498995440909948
""",
)

entry(
    index = 344,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O",
    kinetics = Arrhenius(A=(9.11574e-08,'m^3/(mol*s)'), n=4.14961, Ea=(160.609,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.04194e-07,'m^3/(mol*s)'), n=3.9712, w0=(485,'kJ/mol'), E0=(168.055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12341804119837824, var=0.03795975835473854, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O
    Total Standard Deviation in ln(k): 0.7006834123644969"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O
Total Standard Deviation in ln(k): 0.7006834123644969""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O
Total Standard Deviation in ln(k): 0.7006834123644969
""",
)

entry(
    index = 346,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.0277e-08,'m^3/(mol*s)'), n=4.09467, w0=(485,'kJ/mol'), E0=(170.981,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1344579195349329, var=0.5134742245781799, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.77436930471316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.77436930471316""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.77436930471316
""",
)

entry(
    index = 347,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C",
    kinetics = Arrhenius(A=(3.8501e-07,'m^3/(mol*s)'), n=3.92844, Ea=(168.206,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C",
    kinetics = ArrheniusBM(A=(9.19495e-07,'m^3/(mol*s)'), n=3.75122, w0=(485,'kJ/mol'), E0=(180.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1693157560012653, var=3.5159149374562633, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C
    Total Standard Deviation in ln(k): 4.18444973869373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.18444973869373""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.18444973869373
""",
)

entry(
    index = 349,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R",
    kinetics = Arrhenius(A=(2.68364e-05,'m^3/(mol*s)'), n=3.9376, Ea=(220.387,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C",
    kinetics = Arrhenius(A=(2.28891e-06,'m^3/(mol*s)'), n=3.82239, Ea=(199.241,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C",
    kinetics = Arrhenius(A=(0.00168439,'m^3/(mol*s)'), n=3.12619, Ea=(212.504,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(1.43032e-06,'m^3/(mol*s)'), n=3.73989, w0=(485,'kJ/mol'), E0=(195.288,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.029338637895191772, var=3.7318857833730514, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 3.946480316838213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 3.946480316838213""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 3.946480316838213
""",
)

entry(
    index = 353,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(0.00139188,'m^3/(mol*s)'), n=2.83127, w0=(485,'kJ/mol'), E0=(200.974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1303919235469705, var=3.223254257433352, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 3.9268037412494134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 3.9268037412494134""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 3.9268037412494134
""",
)

entry(
    index = 354,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C",
    kinetics = Arrhenius(A=(1.31087e-08,'m^3/(mol*s)'), n=4.12499, Ea=(167.866,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2.14559e-08,'m^3/(mol*s)'), n=4.27069, Ea=(171.076,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = Arrhenius(A=(3.45985e-08,'m^3/(mol*s)'), n=4.20193, Ea=(180.794,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = Arrhenius(A=(6.21207e-09,'m^3/(mol*s)'), n=4.38354, Ea=(182.296,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = Arrhenius(A=(0.0001135,'m^3/(mol*s)'), n=3.32, Ea=(190.5,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.05888e-05,'m^3/(mol*s)'), n=3.30617, w0=(485,'kJ/mol'), E0=(194.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21443168705568819, var=0.08400851638092321, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.1198299618386824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.1198299618386824""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.1198299618386824
""",
)

entry(
    index = 360,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.11391e-08,'m^3/(mol*s)'), n=3.97251, w0=(485,'kJ/mol'), E0=(166.8,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12852274226468025, var=0.13186923682206136, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R
    Total Standard Deviation in ln(k): 1.0509170317075254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.0509170317075254""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.0509170317075254
""",
)

entry(
    index = 361,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C",
    kinetics = Arrhenius(A=(4.11856e-08,'m^3/(mol*s)'), n=4.0381, Ea=(156.944,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(6.32707e-08,'m^3/(mol*s)'), n=4.09227, Ea=(155.795,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R",
    kinetics = Arrhenius(A=(6.83125e-07,'m^3/(mol*s)'), n=3.8806, Ea=(187.286,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C",
    kinetics = Arrhenius(A=(6.55056e-06,'m^3/(mol*s)'), n=3.42741, Ea=(176.063,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C",
    kinetics = Arrhenius(A=(3.50479e-07,'m^3/(mol*s)'), n=3.85832, Ea=(170.202,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C",
    kinetics = Arrhenius(A=(5.76532e-06,'m^3/(mol*s)'), n=3.58647, Ea=(216.806,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 367,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.00057e-07,'m^3/(mol*s)'), n=4.05084, Ea=(207.795,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 368,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00676355,'m^3/(mol*s)'), n=2.69434, w0=(485,'kJ/mol'), E0=(203.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19203964514781188, var=11.520881032749578, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.287068342570381"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570381""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570381
""",
)

entry(
    index = 369,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R",
    kinetics = Arrhenius(A=(2.96e-05,'m^3/(mol*s)'), n=3.23, Ea=(198.7,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(4.915e-05,'m^3/(mol*s)'), n=3.31, Ea=(175.6,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C",
    kinetics = Arrhenius(A=(7.80562e-08,'m^3/(mol*s)'), n=3.96948, Ea=(152.853,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C",
    kinetics = Arrhenius(A=(1.03271e-07,'m^3/(mol*s)'), n=3.97927, Ea=(151.975,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 373,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(0.000284922,'m^3/(mol*s)'), n=3.00496, Ea=(211.308,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

