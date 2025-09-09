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
    kinetics = ArrheniusBM(A=(6.47696e+32,'m^3/(mol*s)'), n=-7.31364, w0=(412907,'J/mol'), E0=(253526,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0500599909307462, var=16.014843595246155, Tref=1000.0, N=242, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 242 training reactions at node Root
    Total Standard Deviation in ln(k): 10.661000817529402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 242 training reactions at node Root
Total Standard Deviation in ln(k): 10.661000817529402""",
    longDesc = 
"""
BM rule fitted to 242 training reactions at node Root
Total Standard Deviation in ln(k): 10.661000817529402
""",
)

entry(
    index = 2,
    label = "Root_1R->O",
    kinetics = ArrheniusBM(A=(1.24159e-07,'m^3/(mol*s)'), n=4.06955, w0=(337688,'J/mol'), E0=(94519.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22374332618359472, var=5.7652241386381435, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_1R->O',), comment="""BM rule fitted to 64 training reactions at node Root_1R->O
    Total Standard Deviation in ln(k): 5.375714730423702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.375714730423702""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.375714730423702
""",
)

entry(
    index = 3,
    label = "Root_N-1R->O",
    kinetics = ArrheniusBM(A=(4.92793e+32,'m^3/(mol*s)'), n=-7.28039, w0=(439952,'J/mol'), E0=(257473,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.051528243097407, var=15.733556930228595, Tref=1000.0, N=178, data_mean=0.0, correlation='Root_N-1R->O',), comment="""BM rule fitted to 178 training reactions at node Root_N-1R->O
    Total Standard Deviation in ln(k): 10.593922292585319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 178 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 10.593922292585319""",
    longDesc = 
"""
BM rule fitted to 178 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 10.593922292585319
""",
)

entry(
    index = 4,
    label = "Root_1R->O_3R->O",
    kinetics = ArrheniusBM(A=(0.00307209,'m^3/(mol*s)'), n=3.25285, w0=(222000,'J/mol'), E0=(115568,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.038422170979766884, var=0.6020457254883146, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
    Total Standard Deviation in ln(k): 1.652044252008594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.652044252008594""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.652044252008594
""",
)

entry(
    index = 5,
    label = "Root_1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(3.9573e-10,'m^3/(mol*s)'), n=4.72151, w0=(354214,'J/mol'), E0=(35421.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17350395239974964, var=6.758739019519006, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_1R->O_N-3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
    Total Standard Deviation in ln(k): 5.647764616714658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 5.647764616714658""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 5.647764616714658
""",
)

entry(
    index = 6,
    label = "Root_N-1R->O_3R->O",
    kinetics = ArrheniusBM(A=(1.83564e-09,'m^3/(mol*s)'), n=4.86969, w0=(354214,'J/mol'), E0=(35421.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.26979715369361473, var=4.842276971114332, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
    Total Standard Deviation in ln(k): 5.089336781234786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.089336781234786""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.089336781234786
""",
)

entry(
    index = 7,
    label = "Root_N-1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(4.71743e+18,'m^3/(mol*s)'), n=-3.32725, w0=(479308,'J/mol'), E0=(227099,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6988343734258925, var=12.190312235808559, Tref=1000.0, N=122, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O',), comment="""BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
    Total Standard Deviation in ln(k): 8.75532313524932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.75532313524932""",
    longDesc = 
"""
BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.75532313524932
""",
)

entry(
    index = 8,
    label = "Root_1R->O_3R->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.0549417,'m^3/(mol*s)'), n=2.89629, w0=(222000,'J/mol'), E0=(116198,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.18729199312897, var=5.708864139407394, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
    Total Standard Deviation in ln(k): 7.773105232081249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.773105232081249""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.773105232081249
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
    kinetics = ArrheniusBM(A=(0.199178,'m^3/(mol*s)'), n=2.25889, w0=(222000,'J/mol'), E0=(120689,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31081505617104804, var=1.1413495676794396, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 2.9226802855070377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.9226802855070377""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.9226802855070377
""",
)

entry(
    index = 12,
    label = "Root_1R->O_N-3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(6.92634e-08,'m^3/(mol*s)'), n=4.09181, w0=(354370,'J/mol'), E0=(35437,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09452272920500861, var=4.167227609027439, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0',), comment="""BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
    Total Standard Deviation in ln(k): 4.329918081232297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 4.329918081232297""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 4.329918081232297
""",
)

entry(
    index = 13,
    label = "Root_1R->O_N-3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(1.37179e-18,'m^3/(mol*s)'), n=7.09652, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7253925150214916, var=9.298452795485321, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 7.935706006288016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 7.935706006288016""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 7.935706006288016
""",
)

entry(
    index = 14,
    label = "Root_N-1R->O_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(7.85802e-09,'m^3/(mol*s)'), n=4.61, w0=(355318,'J/mol'), E0=(35531.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5588034240854249, var=1.7468321069871093, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 4.05364247454528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.05364247454528""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.05364247454528
""",
)

entry(
    index = 15,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0",
    kinetics = ArrheniusBM(A=(1.33992e-09,'m^3/(mol*s)'), n=5.04526, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.049137222088002655, var=11.742224789567535, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0
    Total Standard Deviation in ln(k): 6.993071976509428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 6.993071976509428""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 6.993071976509428
""",
)

entry(
    index = 16,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0",
    kinetics = ArrheniusBM(A=(2.36912e-11,'m^3/(mol*s)'), n=5.35509, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03797547925611948, var=29.274335063450092, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0
    Total Standard Deviation in ln(k): 10.942187719920888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 10.942187719920888""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 10.942187719920888
""",
)

entry(
    index = 17,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F",
    kinetics = ArrheniusBM(A=(0.286421,'m^3/(mol*s)'), n=2.22749, w0=(326667,'J/mol'), E0=(32666.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07982352851038943, var=2.86740995855166, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F
    Total Standard Deviation in ln(k): 3.595265409811371"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F
Total Standard Deviation in ln(k): 3.595265409811371""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F
Total Standard Deviation in ln(k): 3.595265409811371
""",
)

entry(
    index = 18,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F",
    kinetics = ArrheniusBM(A=(5.61612e+12,'m^3/(mol*s)'), n=-1.63202, w0=(487203,'J/mol'), E0=(213837,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5462357169893383, var=11.92689120026768, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F',), comment="""BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F
    Total Standard Deviation in ln(k): 8.295870591783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F
Total Standard Deviation in ln(k): 8.295870591783""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F
Total Standard Deviation in ln(k): 8.295870591783
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
    kinetics = ArrheniusBM(A=(0.00501,'m^3/(mol*s)'), n=3.19468, w0=(222000,'J/mol'), E0=(113810,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3116729497350743, var=4.981622398262143, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 7.770138832350749"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.770138832350749""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.770138832350749
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
    kinetics = ArrheniusBM(A=(3.6768e-08,'m^3/(mol*s)'), n=4.15162, w0=(354611,'J/mol'), E0=(35461.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10078592125048802, var=4.959664893550687, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1',), comment="""BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
    Total Standard Deviation in ln(k): 4.717837140225767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.717837140225767""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.717837140225767
""",
)

entry(
    index = 25,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(1.18901e-06,'m^3/(mol*s)'), n=3.82331, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.022540691608677756, var=1.1866825852192928, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
    Total Standard Deviation in ln(k): 2.240492289673071"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.240492289673071""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.240492289673071
""",
)

entry(
    index = 26,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(5.93743e-18,'m^3/(mol*s)'), n=6.85017, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6529401405341346, var=25.823241012381136, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 14.34049259087525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 14.34049259087525""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 14.34049259087525
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
    kinetics = ArrheniusBM(A=(8.38974e-08,'m^3/(mol*s)'), n=4.2997, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4247501581365868, var=6.878974091361633, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
    Total Standard Deviation in ln(k): 6.325190198995025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 6.325190198995025""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 6.325190198995025
""",
)

entry(
    index = 30,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(2.75075e-09,'m^3/(mol*s)'), n=4.74755, w0=(357136,'J/mol'), E0=(35713.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5859016260750727, var=2.1553224862804683, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
    Total Standard Deviation in ln(k): 4.415269534854463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.415269534854463""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.415269534854463
""",
)

entry(
    index = 31,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(2.32037e-09,'m^3/(mol*s)'), n=4.97438, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013453651298259362, var=12.931692919046366, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 7.242963419917438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 7.242963419917438""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 7.242963419917438
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
    kinetics = ArrheniusBM(A=(0.0231404,'m^3/(mol*s)'), n=2.67404, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9829507987758292, var=6.346959859035542, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 7.520289467415782"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 7.520289467415782""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 7.520289467415782
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
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C",
    kinetics = ArrheniusBM(A=(0.00257577,'m^3/(mol*s)'), n=2.81749, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11460147064854857, var=0.9198265095043655, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C
    Total Standard Deviation in ln(k): 2.210636416475616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 2.210636416475616""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 2.210636416475616
""",
)

entry(
    index = 38,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->C",
    kinetics = Arrhenius(A=(29364.6,'m^3/(mol*s)'), n=0.785655, Ea=(4.07732,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H",
    kinetics = ArrheniusBM(A=(5.90234,'m^3/(mol*s)'), n=2.07201, w0=(518487,'J/mol'), E0=(170124,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5369132859841977, var=5.127321894743522, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H
    Total Standard Deviation in ln(k): 5.888468366528195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 5.888468366528195""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 5.888468366528195
""",
)

entry(
    index = 40,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(3.09921e+15,'m^3/(mol*s)'), n=-2.49904, w0=(481457,'J/mol'), E0=(224742,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5051615488137885, var=10.506495721068575, Tref=1000.0, N=98, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H',), comment="""BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H
    Total Standard Deviation in ln(k): 7.767343283836953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 7.767343283836953""",
    longDesc = 
"""
BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 7.767343283836953
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
    kinetics = ArrheniusBM(A=(1.9597e-08,'m^3/(mol*s)'), n=4.18315, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08546670275270314, var=4.178216402435214, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 4.312556463038107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.312556463038107""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.312556463038107
""",
)

entry(
    index = 44,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C",
    kinetics = ArrheniusBM(A=(5.15234e-10,'m^3/(mol*s)'), n=4.89163, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2062628550795026, var=1.7584106807569755, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C
    Total Standard Deviation in ln(k): 3.176628899939157"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C
Total Standard Deviation in ln(k): 3.176628899939157""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C
Total Standard Deviation in ln(k): 3.176628899939157
""",
)

entry(
    index = 45,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C",
    kinetics = Arrhenius(A=(1.04105,'m^3/(mol*s)'), n=2.3137, Ea=(11.5771,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000245593,'m^3/(mol*s)'), n=3.10149, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3880687636183124, var=11.564223689260121, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 10.304954310909942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 10.304954310909942""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 10.304954310909942
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
    kinetics = ArrheniusBM(A=(3.90045e-15,'m^3/(mol*s)'), n=6.03878, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2939537384946425, var=9.110125558300933, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
    Total Standard Deviation in ln(k): 9.302028831540193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 9.302028831540193""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 9.302028831540193
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
    kinetics = ArrheniusBM(A=(4.49448e-05,'m^3/(mol*s)'), n=3.55407, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8134974073183621, var=0.9115435098924485, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0
    Total Standard Deviation in ln(k): 3.9579798953793475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 3.9579798953793475""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 3.9579798953793475
""",
)

entry(
    index = 51,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0",
    kinetics = ArrheniusBM(A=(5.09882e-11,'m^3/(mol*s)'), n=5.17848, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4713124203817223, var=15.388085976125996, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0
    Total Standard Deviation in ln(k): 11.560869657968997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 11.560869657968997""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0
Total Standard Deviation in ln(k): 11.560869657968997
""",
)

entry(
    index = 52,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C",
    kinetics = ArrheniusBM(A=(1.5831e-09,'m^3/(mol*s)'), n=4.8694, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45561771119422806, var=2.7803063801854284, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C
    Total Standard Deviation in ln(k): 4.487513655024877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 4.487513655024877""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 4.487513655024877
""",
)

entry(
    index = 53,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->C",
    kinetics = Arrhenius(A=(0.000687874,'m^3/(mol*s)'), n=2.99039, Ea=(395.881,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
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
    kinetics = ArrheniusBM(A=(2.39138e-09,'m^3/(mol*s)'), n=4.97062, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012664531201620735, var=12.938895581160784, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi
    Total Standard Deviation in ln(k): 7.242988096695542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi
Total Standard Deviation in ln(k): 7.242988096695542""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi
Total Standard Deviation in ln(k): 7.242988096695542
""",
)

entry(
    index = 56,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi",
    kinetics = ArrheniusBM(A=(0.0257221,'m^3/(mol*s)'), n=2.65974, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3675803242638414, var=8.38681293386402, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi
    Total Standard Deviation in ln(k): 9.241843190877676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi
Total Standard Deviation in ln(k): 9.241843190877676""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi
Total Standard Deviation in ln(k): 9.241843190877676
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
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0108084,'m^3/(mol*s)'), n=2.63211, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40107863394034476, var=1.2611536926907378, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.2590747931686406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.2590747931686406""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.2590747931686406
""",
)

entry(
    index = 59,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C",
    kinetics = ArrheniusBM(A=(1.34074e-10,'m^3/(mol*s)'), n=5.13946, w0=(525000,'J/mol'), E0=(146575,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3452957127082802, var=3.4896475956685364, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C
    Total Standard Deviation in ln(k): 4.612542271543766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C
Total Standard Deviation in ln(k): 4.612542271543766""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C
Total Standard Deviation in ln(k): 4.612542271543766
""",
)

entry(
    index = 60,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->C",
    kinetics = Arrhenius(A=(650.29,'m^3/(mol*s)'), n=1.25799, Ea=(20.8614,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C",
    kinetics = ArrheniusBM(A=(1.45706e-09,'m^3/(mol*s)'), n=4.44892, w0=(492473,'J/mol'), E0=(168467,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12439752743985773, var=4.857874440442904, Tref=1000.0, N=91, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C',), comment="""BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C
    Total Standard Deviation in ln(k): 4.731110247967088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 4.731110247967088""",
    longDesc = 
"""
BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 4.731110247967088
""",
)

entry(
    index = 62,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C",
    kinetics = ArrheniusBM(A=(0.0767251,'m^3/(mol*s)'), n=2.51885, w0=(338253,'J/mol'), E0=(33825.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.009471497707623422, var=11.892304991361218, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C
    Total Standard Deviation in ln(k): 6.9371710441639065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 6.9371710441639065""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 6.9371710441639065
""",
)

entry(
    index = 63,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(6.40008e-12,'m^3/(mol*s)'), n=5.05694, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.1132282999324854, var=16.28773362426252, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
    Total Standard Deviation in ln(k): 15.912904394737142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.912904394737142""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.912904394737142
""",
)

entry(
    index = 64,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(6.47818e-08,'m^3/(mol*s)'), n=4.053, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08114696602720062, var=4.092602571883935, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl',), comment="""BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.259502364534309"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.259502364534309""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.259502364534309
""",
)

entry(
    index = 65,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.11722e-08,'m^3/(mol*s)'), n=4.37793, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2701684927013809, var=0.3454530799266302, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R
    Total Standard Deviation in ln(k): 1.8571034960374122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R
Total Standard Deviation in ln(k): 1.8571034960374122""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R
Total Standard Deviation in ln(k): 1.8571034960374122
""",
)

entry(
    index = 66,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000340767,'m^3/(mol*s)'), n=3.06, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.911279317756785, var=69.36738496052052, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 31.549314638513938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.549314638513938""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.549314638513938
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
    kinetics = ArrheniusBM(A=(4.57091e-13,'m^3/(mol*s)'), n=5.73718, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3932029317723975, var=0.31775638014096713, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 7.143139526837644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 7.143139526837644""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 7.143139526837644
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
    kinetics = ArrheniusBM(A=(9.92129e-13,'m^3/(mol*s)'), n=5.40242, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.042120305071752, var=1.2597325164130357, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
    Total Standard Deviation in ln(k): 12.406151841613477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
Total Standard Deviation in ln(k): 12.406151841613477""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
Total Standard Deviation in ln(k): 12.406151841613477
""",
)

entry(
    index = 71,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O",
    kinetics = ArrheniusBM(A=(6.971e-19,'m^3/(mol*s)'), n=7.03026, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40128655227643495, var=0.7917787201238058, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
    Total Standard Deviation in ln(k): 2.79211000793875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
Total Standard Deviation in ln(k): 2.79211000793875""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
Total Standard Deviation in ln(k): 2.79211000793875
""",
)

entry(
    index = 72,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(4.86492e-05,'m^3/(mol*s)'), n=3.5429, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8203806609827082, var=0.9492562286798802, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 4.014466943987982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 4.014466943987982""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 4.014466943987982
""",
)

entry(
    index = 73,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(0.0370893,'m^3/(mol*s)'), n=2.5544, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5064640674944558, var=48.4914226892234, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 17.74521527156811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 17.74521527156811""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 17.74521527156811
""",
)

entry(
    index = 74,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(2.48616e-10,'m^3/(mol*s)'), n=5.08521, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6079583567502719, var=4.237502376253689, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 5.654319733043686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 5.654319733043686""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 5.654319733043686
""",
)

entry(
    index = 75,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(5.2025e-07,'m^3/(mol*s)'), n=4.19384, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.311750976793184, var=1.120581839613572, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 2.9054571121264936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 2.9054571121264936""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 2.9054571121264936
""",
)

entry(
    index = 76,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F",
    kinetics = ArrheniusBM(A=(7.27456e-12,'m^3/(mol*s)'), n=5.73835, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06350833929258697, var=2.722502416580844, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F
    Total Standard Deviation in ln(k): 3.4673830374518473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.4673830374518473""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.4673830374518473
""",
)

entry(
    index = 77,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F",
    kinetics = ArrheniusBM(A=(2.1665e-08,'m^3/(mol*s)'), n=4.67866, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.036567346713901126, var=23.03956357645449, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F
    Total Standard Deviation in ln(k): 9.714514989790505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 9.714514989790505""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 9.714514989790505
""",
)

entry(
    index = 78,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O",
    kinetics = ArrheniusBM(A=(0.0255218,'m^3/(mol*s)'), n=2.65878, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0825639883932814, var=7.283061781077924, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O
    Total Standard Deviation in ln(k): 8.130218322284835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O
Total Standard Deviation in ln(k): 8.130218322284835""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O
Total Standard Deviation in ln(k): 8.130218322284835
""",
)

entry(
    index = 79,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O",
    kinetics = ArrheniusBM(A=(0.0559805,'m^3/(mol*s)'), n=2.75535, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03682186198244248, var=30.920478343061166, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_N-4R!H->O
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
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00434898,'m^3/(mol*s)'), n=2.74217, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.33234268447166243, var=0.6712269040528758, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 2.4774800161731134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.4774800161731134""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.4774800161731134
""",
)

entry(
    index = 81,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.20448e-11,'m^3/(mol*s)'), n=5.18607, w0=(525000,'J/mol'), E0=(146376,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3445084038250166, var=3.4570441385030084, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.593028621688415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.593028621688415""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.593028621688415
""",
)

entry(
    index = 82,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1",
    kinetics = ArrheniusBM(A=(1.36186e-09,'m^3/(mol*s)'), n=4.45706, w0=(493000,'J/mol'), E0=(168408,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1252159251121607, var=4.838102558484823, Tref=1000.0, N=85, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1',), comment="""BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
    Total Standard Deviation in ln(k): 4.724165447331821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
Total Standard Deviation in ln(k): 4.724165447331821""",
    longDesc = 
"""
BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
Total Standard Deviation in ln(k): 4.724165447331821
""",
)

entry(
    index = 83,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(1.81567e-05,'m^3/(mol*s)'), n=3.65016, w0=(485000,'J/mol'), E0=(159206,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04677514853114033, var=12.86598925485542, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
    Total Standard Deviation in ln(k): 7.308348212998748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
Total Standard Deviation in ln(k): 7.308348212998748""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
Total Standard Deviation in ln(k): 7.308348212998748
""",
)

entry(
    index = 84,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C",
    kinetics = ArrheniusBM(A=(0.792201,'m^3/(mol*s)'), n=2.56975, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4073627487201191, var=2.9843526473479565, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
    Total Standard Deviation in ln(k): 4.4867602737795"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 4.4867602737795""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 4.4867602737795
""",
)

entry(
    index = 85,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C",
    kinetics = ArrheniusBM(A=(0.0113121,'m^3/(mol*s)'), n=2.47711, w0=(383885,'J/mol'), E0=(38388.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2857695948365517, var=0.5959251139747826, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
    Total Standard Deviation in ln(k): 4.77815589148416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 4.77815589148416""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 4.77815589148416
""",
)

entry(
    index = 86,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(8.68166e-12,'m^3/(mol*s)'), n=5.01731, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.9663733357086086, var=2.94128244581631, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
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
    kinetics = ArrheniusBM(A=(1.9111e-09,'m^3/(mol*s)'), n=4.21518, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.005541262532681, var=2.813618993160456, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
    Total Standard Deviation in ln(k): 5.889197268509554"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 5.889197268509554""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 5.889197268509554
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
    kinetics = ArrheniusBM(A=(1.24392e-07,'m^3/(mol*s)'), n=4.02029, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09914915495434834, var=3.180777131737125, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 3.824510031291821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 3.824510031291821""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 3.824510031291821
""",
)

entry(
    index = 91,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C",
    kinetics = Arrhenius(A=(0.000476496,'m^3/(mol*s)'), n=3.27616, Ea=(30.5726,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.94356e-08,'m^3/(mol*s)'), n=4.30209, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.698421819187984, var=1.5602719802605522, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 9.284085893220501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 9.284085893220501""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 9.284085893220501
""",
)

entry(
    index = 93,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000290035,'m^3/(mol*s)'), n=3.07816, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.427596795396312, var=58.32772836405397, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 28.947859327504517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 28.947859327504517""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 28.947859327504517
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
    kinetics = ArrheniusBM(A=(6.59723e-19,'m^3/(mol*s)'), n=7.03657, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40475763261328895, var=0.7829137400603391, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C
    Total Standard Deviation in ln(k): 2.7908169460522805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 2.7908169460522805""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 2.7908169460522805
""",
)

entry(
    index = 101,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(5.92303e-05,'m^3/(mol*s)'), n=3.43084, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7262432120854407, var=2.3471530446716447, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 7.408633072373351"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.408633072373351""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.408633072373351
""",
)

entry(
    index = 102,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(4.70704e-05,'m^3/(mol*s)'), n=3.56169, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.323200440989884, var=16.3933312351659, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 16.466657345566126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 16.466657345566126""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 16.466657345566126
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
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.56731e-10,'m^3/(mol*s)'), n=5.08072, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6063328718902272, var=4.258892694364666, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 5.660638208145669"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.660638208145669""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.660638208145669
""",
)

entry(
    index = 105,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.91695e-06,'m^3/(mol*s)'), n=4.05326, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21391053915903774, var=0.7789620327632053, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.3068193054874735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.3068193054874735""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.3068193054874735
""",
)

entry(
    index = 106,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(6.7601e-12,'m^3/(mol*s)'), n=5.75324, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.034200302726023625, var=3.800957333655942, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 3.9943707454021666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 3.9943707454021666""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 3.9943707454021666
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
    kinetics = ArrheniusBM(A=(1.57211e-26,'m^3/(mol*s)'), n=9.86078, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4798073597983304, var=201.39789185135874, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
    Total Standard Deviation in ln(k): 29.655688860172038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 29.655688860172038""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 29.655688860172038
""",
)

entry(
    index = 110,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(2.20132e-06,'m^3/(mol*s)'), n=4.10531, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2672950532644582, var=18.639659819611904, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
    Total Standard Deviation in ln(k): 9.326773144050454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.326773144050454""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.326773144050454
""",
)

entry(
    index = 111,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R",
    kinetics = ArrheniusBM(A=(0.0311503,'m^3/(mol*s)'), n=2.63215, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9445157623872364, var=21.35049890476946, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 11.636354379594504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.636354379594504""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-4R!H-1BrCClFHILiNPSSi_4R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.636354379594504
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
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O",
    kinetics = Arrhenius(A=(0.00466877,'m^3/(mol*s)'), n=2.7407, Ea=(1.59476,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(0.367477,'m^3/(mol*s)'), n=2.16709, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4269663786227196, var=1.0392454131872326, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 3.1164746819778575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.1164746819778575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.1164746819778575
""",
)

entry(
    index = 117,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(2.79237e-11,'m^3/(mol*s)'), n=5.28537, w0=(525000,'J/mol'), E0=(147690,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37729644142022806, var=3.584896636386719, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 4.74371097454957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 4.74371097454957""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 4.74371097454957
""",
)

entry(
    index = 118,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.84074e-15,'m^3/(mol*s)'), n=6.60361, w0=(525000,'J/mol'), E0=(130477,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15292343895861524, var=2.925419480284944, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.813100093988797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.813100093988797""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.813100093988797
""",
)

entry(
    index = 119,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C",
    kinetics = ArrheniusBM(A=(1.04243e-06,'m^3/(mol*s)'), n=3.76371, w0=(485000,'J/mol'), E0=(179655,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008643677353455611, var=3.211961279033082, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C
    Total Standard Deviation in ln(k): 3.614593047643713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C
Total Standard Deviation in ln(k): 3.614593047643713""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C
Total Standard Deviation in ln(k): 3.614593047643713
""",
)

entry(
    index = 120,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C",
    kinetics = ArrheniusBM(A=(1.18811e-13,'m^3/(mol*s)'), n=5.31246, w0=(525000,'J/mol'), E0=(148566,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3690049835665827, var=9.118729808909121, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C
    Total Standard Deviation in ln(k): 6.9808937555055195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C
Total Standard Deviation in ln(k): 6.9808937555055195""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C
Total Standard Deviation in ln(k): 6.9808937555055195
""",
)

entry(
    index = 121,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.24163e-07,'m^3/(mol*s)'), n=4.41753, w0=(485000,'J/mol'), E0=(146152,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05057556960482193, var=0.10803949586257557, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.7860179253224522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.7860179253224522""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.7860179253224522
""",
)

entry(
    index = 122,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(2.1997e-06,'m^3/(mol*s)'), n=3.79689, w0=(485000,'J/mol'), E0=(176420,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.35451023191418146, var=33.3743765486795, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 12.472196123677433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 12.472196123677433""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 12.472196123677433
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
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.13251,'m^3/(mol*s)'), n=2.32287, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0384295923050715, var=4.174659521896346, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.705190992971417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.705190992971417""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.705190992971417
""",
)

entry(
    index = 125,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->Cl",
    kinetics = Arrhenius(A=(1580.64,'m^3/(mol*s)'), n=1.06012, Ea=(335.653,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->Cl",
    kinetics = Arrhenius(A=(10572.3,'m^3/(mol*s)'), n=0.709227, Ea=(414.376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
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
    kinetics = ArrheniusBM(A=(2.52511e-09,'m^3/(mol*s)'), n=4.17798, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07947616098846677, var=0.21670084334867099, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
    Total Standard Deviation in ln(k): 1.1329158357559586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 1.1329158357559586""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 1.1329158357559586
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
    kinetics = ArrheniusBM(A=(2.26019e-07,'m^3/(mol*s)'), n=3.92012, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1181981591872006, var=5.077875618161782, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi',), comment="""BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
    Total Standard Deviation in ln(k): 4.814478817415484"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 4.814478817415484""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 4.814478817415484
""",
)

entry(
    index = 132,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi",
    kinetics = ArrheniusBM(A=(2.20239e-08,'m^3/(mol*s)'), n=4.31068, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14664741715471388, var=0.7362767439690774, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
    Total Standard Deviation in ln(k): 2.088655252813506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 2.088655252813506""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi
Total Standard Deviation in ln(k): 2.088655252813506
""",
)

entry(
    index = 133,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(0.000849095,'m^3/(mol*s)'), n=3.17369, Ea=(16.5921,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(0.01745,'m^3/(mol*s)'), n=2.59, Ea=(14.5,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(5.31202e+07,'m^3/(mol*s)'), n=0.114184, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.409811063433669, var=2.1121261782578697, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 8.968314390866366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 8.968314390866366""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 8.968314390866366
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
    kinetics = ArrheniusBM(A=(1.52693e-19,'m^3/(mol*s)'), n=7.22205, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.42027930036268396, var=1.1088623300935554, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 3.1670149432692702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 3.1670149432692702""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 3.1670149432692702
""",
)

entry(
    index = 138,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C",
    kinetics = ArrheniusBM(A=(6.84972e-14,'m^3/(mol*s)'), n=6.24271, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.9915745234073474, var=0.016786657397154188, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C
    Total Standard Deviation in ln(k): 5.263696248448416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C
Total Standard Deviation in ln(k): 5.263696248448416""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C
Total Standard Deviation in ln(k): 5.263696248448416
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
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C",
    kinetics = Arrhenius(A=(5.27349e-06,'m^3/(mol*s)'), n=3.9638, Ea=(356.126,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C",
    kinetics = Arrhenius(A=(6.65995e-06,'m^3/(mol*s)'), n=3.94804, Ea=(353.81,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-5R!H=1BrBrBrCCCClClClFFFHHHIIILiLiLiNNNPPPSSSSiSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.39163e-09,'m^3/(mol*s)'), n=4.80449, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6118504557319647, var=15.600511792102418, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 9.455511707019454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 9.455511707019454""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 9.455511707019454
""",
)

entry(
    index = 145,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(4.6139e-06,'m^3/(mol*s)'), n=3.99356, Ea=(285.397,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.15642e-07,'m^3/(mol*s)'), n=4.18289, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09961166593940578, var=2.17191883283887, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.204745128808868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.204745128808868""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.204745128808868
""",
)

entry(
    index = 147,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->O",
    kinetics = Arrhenius(A=(0.0215072,'m^3/(mol*s)'), n=2.81865, Ea=(345.137,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->O",
    kinetics = Arrhenius(A=(0.0117015,'m^3/(mol*s)'), n=2.97295, Ea=(341.858,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O",
    kinetics = ArrheniusBM(A=(2.95817e-15,'m^3/(mol*s)'), n=6.68228, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.500881504287118, var=1.8436248984570236, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O
    Total Standard Deviation in ln(k): 14.030779782364222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 14.030779782364222""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 14.030779782364222
""",
)

entry(
    index = 150,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(3.2316e-10,'m^3/(mol*s)'), n=5.28873, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09079029865426554, var=3.952887815418673, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O
    Total Standard Deviation in ln(k): 4.213904682938074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.213904682938074""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.213904682938074
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
    kinetics = ArrheniusBM(A=(4.1614e-13,'m^3/(mol*s)'), n=6.10222, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.613045669712701, var=1.0567151485671573, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 11.138804719055187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.138804719055187""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 11.138804719055187
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
    kinetics = ArrheniusBM(A=(98.5977,'m^3/(mol*s)'), n=2.09069, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.25562235166291, var=76.38067481151892, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 30.725671612414004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 30.725671612414004""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 30.725671612414004
""",
)

entry(
    index = 156,
    label = "Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(1.26046e-08,'m^3/(mol*s)'), n=4.47769, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3136422526376453, var=0.6125561160051448, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 2.3570710998879676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 2.3570710998879676""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 2.3570710998879676
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
    label = "Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R",
    kinetics = Arrhenius(A=(0.00965,'m^3/(mol*s)'), n=2.58, Ea=(-2.9,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHILiNPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.32363e-06,'m^3/(mol*s)'), n=3.87695, w0=(525000,'J/mol'), E0=(162527,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40501075270893755, var=4.002522635978417, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 5.028349216278372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.028349216278372""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.028349216278372
""",
)

entry(
    index = 162,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(2.96661e-18,'m^3/(mol*s)'), n=7.56742, w0=(525000,'J/mol'), E0=(130514,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3955823934451051, var=0.04397608962639776, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 1.4143281155208647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.4143281155208647""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.4143281155208647
""",
)

entry(
    index = 163,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(3.7984e-14,'m^3/(mol*s)'), n=6.1795, w0=(525000,'J/mol'), E0=(131769,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11731167884064622, var=4.662246159983312, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 4.623424069485684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.623424069485684""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.623424069485684
""",
)

entry(
    index = 164,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.42487e-07,'m^3/(mol*s)'), n=3.7758, w0=(485000,'J/mol'), E0=(179637,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01581346117502535, var=3.2820662363240642, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.671605368862638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.671605368862638""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.671605368862638
""",
)

entry(
    index = 165,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(4.97707e-05,'m^3/(mol*s)'), n=3.41316, w0=(485000,'J/mol'), E0=(181182,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27293962943213335, var=0.9607960757425561, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.6508234132668904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.6508234132668904""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.6508234132668904
""",
)

entry(
    index = 166,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(1.04377e-05,'m^3/(mol*s)'), n=3.41777, w0=(485000,'J/mol'), E0=(178686,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23236678604832017, var=0.3363104982246206, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 1.746427801700129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.746427801700129""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.746427801700129
""",
)

entry(
    index = 167,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.2026e-14,'m^3/(mol*s)'), n=5.39101, w0=(525000,'J/mol'), E0=(148164,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.38275009856801273, var=9.04663850613767, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 6.991451735970476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.991451735970476""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.991451735970476
""",
)

entry(
    index = 168,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(7.83903e-10,'m^3/(mol*s)'), n=5.14485, w0=(485000,'J/mol'), E0=(139641,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06543906391629854, var=0.010784333405798239, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 0.3726067755457244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 0.3726067755457244""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 0.3726067755457244
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
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.38025,'m^3/(mol*s)'), n=2.3884, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2801712339214502, var=4.590911247311203, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 7.511938579670093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.511938579670093""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.511938579670093
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
    kinetics = ArrheniusBM(A=(3.00315e-09,'m^3/(mol*s)'), n=4.15252, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.798140207094654, var=5.079888294401087, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R
    Total Standard Deviation in ln(k): 14.061459558289293"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 14.061459558289293""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 14.061459558289293
""",
)

entry(
    index = 175,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(9.46787e-07,'m^3/(mol*s)'), n=3.74324, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.049350133556677715, var=11.202137544055145, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 6.833762317716111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 6.833762317716111""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 6.833762317716111
""",
)

entry(
    index = 176,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(7.79807e-09,'m^3/(mol*s)'), n=4.33585, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15486845091199464, var=0.5615130183559228, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 1.8913483485925853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 1.8913483485925853""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 1.8913483485925853
""",
)

entry(
    index = 177,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(1.39804e-09,'m^3/(mol*s)'), n=4.6808, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.8326103930978574, var=0.17475983639391765, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 5.442613920297295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 5.442613920297295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 5.442613920297295
""",
)

entry(
    index = 178,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(7.08191e-06,'m^3/(mol*s)'), n=3.53568, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08265982558405777, var=1.180358822837767, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 2.385718792936555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.385718792936555""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.385718792936555
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
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R",
    kinetics = Arrhenius(A=(1.37515e-06,'m^3/(mol*s)'), n=3.75034, Ea=(292.69,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_4BrCClFILiNPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = Arrhenius(A=(2.05616,'m^3/(mol*s)'), n=2.3798, Ea=(393.249,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O",
    kinetics = Arrhenius(A=(0.285485,'m^3/(mol*s)'), n=2.54097, Ea=(361.717,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O",
    kinetics = Arrhenius(A=(0.340714,'m^3/(mol*s)'), n=2.59484, Ea=(375.342,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHILiNPSSi->C_N-4BrCClFILiNPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O
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
    kinetics = ArrheniusBM(A=(1.12178e-09,'m^3/(mol*s)'), n=5.13717, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.1868485869910574, var=5.694860985882942, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R
    Total Standard Deviation in ln(k): 12.79123857180926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 12.79123857180926""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_4R!H->F_Ext-1BrCClFHILiNPSSi-R_N-5R!H->O_Ext-1BrCClFHILiNPSSi-R
Total Standard Deviation in ln(k): 12.79123857180926
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
    kinetics = ArrheniusBM(A=(131.695,'m^3/(mol*s)'), n=2.05573, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28507528450428055, var=6.821477790933631, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C
    Total Standard Deviation in ln(k): 5.9522284023750185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C
Total Standard Deviation in ln(k): 5.9522284023750185""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_Ext-1BrCClFHILiNPSSi-R_4CClO->C
Total Standard Deviation in ln(k): 5.9522284023750185
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
    kinetics = ArrheniusBM(A=(1.45602e-08,'m^3/(mol*s)'), n=4.45802, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11050425909143742, var=0.5200883806443982, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl
    Total Standard Deviation in ln(k): 1.7234067620951001"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.7234067620951001""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.7234067620951001
""",
)

entry(
    index = 199,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(5.97442e-06,'m^3/(mol*s)'), n=3.7401, w0=(525000,'J/mol'), E0=(165933,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4160068741681061, var=3.608169143060094, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 4.853274036687226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 4.853274036687226""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 4.853274036687226
""",
)

entry(
    index = 200,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5.86193e-10,'m^3/(mol*s)'), n=4.99656, w0=(525000,'J/mol'), E0=(142529,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9423094015406155, var=6.107335727119696, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 7.3219182407175305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.3219182407175305""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.3219182407175305
""",
)

entry(
    index = 201,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_Ext-1C-R",
    kinetics = Arrhenius(A=(2.80067e-20,'m^3/(mol*s)'), n=8.17077, Ea=(92.4857,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_4BrCClILiNOPSSi->C",
    kinetics = Arrhenius(A=(5.18265e-09,'m^3/(mol*s)'), n=4.74784, Ea=(92.3732,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_4BrCClILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_4BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_4BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_4BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(4.37791e-15,'m^3/(mol*s)'), n=6.43515, w0=(525000,'J/mol'), E0=(132017,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3336639168085958, var=7.324792426608593, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 6.264037476124818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 6.264037476124818""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 6.264037476124818
""",
)

entry(
    index = 204,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0",
    kinetics = ArrheniusBM(A=(8.6417e-07,'m^3/(mol*s)'), n=3.78654, w0=(485000,'J/mol'), E0=(179573,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014399211682271911, var=3.26737977395334, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0',), comment="""BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0
    Total Standard Deviation in ln(k): 3.6599169852774525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.6599169852774525""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.6599169852774525
""",
)

entry(
    index = 205,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0",
    kinetics = ArrheniusBM(A=(228.591,'m^3/(mol*s)'), n=1.41823, w0=(485000,'J/mol'), E0=(172857,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4779045289067694, var=9.699901474267332, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0
    Total Standard Deviation in ln(k): 7.44444535401821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.44444535401821""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.44444535401821
""",
)

entry(
    index = 206,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.81477e-05,'m^3/(mol*s)'), n=3.38383, w0=(485000,'J/mol'), E0=(179384,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2149616755423849, var=2.1237975861441685, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.9742190570817755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.9742190570817755""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.9742190570817755
""",
)

entry(
    index = 207,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C",
    kinetics = Arrhenius(A=(3.70857e-08,'m^3/(mol*s)'), n=4.36701, Ea=(151.162,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C",
    kinetics = Arrhenius(A=(3.95e-05,'m^3/(mol*s)'), n=3.43, Ea=(162.6,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.48443e-05,'m^3/(mol*s)'), n=3.39528, w0=(485000,'J/mol'), E0=(181004,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28301429677414974, var=0.7833694466991995, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.4854453369072624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.4854453369072624""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.4854453369072624
""",
)

entry(
    index = 210,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.26291e-08,'m^3/(mol*s)'), n=4.37484, w0=(485000,'J/mol'), E0=(173733,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24436438432485383, var=0.014235358056972649, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 0.8531698562866359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562866359""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562866359
""",
)

entry(
    index = 211,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.97199e-05,'m^3/(mol*s)'), n=3.28397, w0=(485000,'J/mol'), E0=(175438,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1309384567838492, var=3.765453001855297, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.731697260808538"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808538""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808538
""",
)

entry(
    index = 212,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.07774e-15,'m^3/(mol*s)'), n=5.87789, w0=(525000,'J/mol'), E0=(145906,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.42368027563824734, var=0.07431184928327957, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 1.6110180930706026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.6110180930706026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.6110180930706026
""",
)

entry(
    index = 213,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.867e-13,'m^3/(mol*s)'), n=5.16656, w0=(525000,'J/mol'), E0=(149730,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.36440541170633217, var=11.275511280738879, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 7.647297036187546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.647297036187546""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.647297036187546
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
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = Arrhenius(A=(363.313,'m^3/(mol*s)'), n=1.87359, Ea=(383.25,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O",
    kinetics = Arrhenius(A=(14.1008,'m^3/(mol*s)'), n=2.18545, Ea=(351.113,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O",
    kinetics = Arrhenius(A=(71.772,'m^3/(mol*s)'), n=2.09863, Ea=(369.342,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O
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
    kinetics = ArrheniusBM(A=(5.43644e-05,'m^3/(mol*s)'), n=3.30995, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.022278827677990505, var=14.297730918703746, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 7.636349483958339"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.636349483958339""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.636349483958339
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
    kinetics = ArrheniusBM(A=(5.62416e-08,'m^3/(mol*s)'), n=4.11181, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13804191344216082, var=0.559755399725918, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 1.8467176701639496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 1.8467176701639496""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 1.8467176701639496
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
    kinetics = ArrheniusBM(A=(1.14789e-09,'m^3/(mol*s)'), n=4.55116, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17138137621640787, var=0.45073726449468876, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 1.7765248460869265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 1.7765248460869265""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 1.7765248460869265
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
    kinetics = ArrheniusBM(A=(0.000246125,'m^3/(mol*s)'), n=3.06199, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.45703443345530537, var=5.187466670680611, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 5.714314495703316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 5.714314495703316""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_N-Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 5.714314495703316
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
    kinetics = ArrheniusBM(A=(6.92154e-15,'m^3/(mol*s)'), n=6.48156, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.557615907777201, var=0.10891866534596795, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
    Total Standard Deviation in ln(k): 9.600352705303369"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 9.600352705303369""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHILiNPSSi-u0_Ext-1BrCClFHILiNPSSi-R_N-Sp-4R!H#1BrBrBrBrCCCCClClClClFFFFHHHHIIIILiLiLiLiNNNNPPPPSSSSSiSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHILiNOOPSSi=1BrBrCCCCClClClClFFHHIILiLiNNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 9.600352705303369
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
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.6515e-06,'m^3/(mol*s)'), n=3.72606, w0=(525000,'J/mol'), E0=(166288,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41358967924443424, var=3.7669428611427964, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.930082919002328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.930082919002328""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.930082919002328
""",
)

entry(
    index = 236,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClILiNOPSSi->C",
    kinetics = Arrhenius(A=(1.84865e-10,'m^3/(mol*s)'), n=5.13872, Ea=(109.875,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClILiNOPSSi->C",
    kinetics = Arrhenius(A=(6.15e-07,'m^3/(mol*s)'), n=4.14, Ea=(134.9,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_Ext-1C-R",
    kinetics = Arrhenius(A=(7.71142e-12,'m^3/(mol*s)'), n=5.47558, Ea=(94.535,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_4ClO->Cl",
    kinetics = Arrhenius(A=(3.57367e-11,'m^3/(mol*s)'), n=5.32561, Ea=(91.9755,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_N-4ClO->Cl",
    kinetics = Arrhenius(A=(3.31829e-08,'m^3/(mol*s)'), n=4.48236, Ea=(100.723,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_N-4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_N-4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIILiLiNNOOPPSSSiSi=1C_N-4BrCClILiNOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.40738e-05,'m^3/(mol*s)'), n=3.45454, w0=(485000,'J/mol'), E0=(188561,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0998962525064304, var=6.0960568074569235, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 5.2007254112705485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.2007254112705485""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.2007254112705485
""",
)

entry(
    index = 242,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(7.98978e-08,'m^3/(mol*s)'), n=4.06507, w0=(485000,'J/mol'), E0=(170985,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.061667757903041034, var=0.57723420944871, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 1.6780602548863075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.6780602548863075""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.6780602548863075
""",
)

entry(
    index = 243,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(6.93677e-07,'m^3/(mol*s)'), n=3.84128, w0=(485000,'J/mol'), E0=(181259,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17482047820953117, var=1.3084956852577916, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 2.732453788887294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.732453788887294""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.732453788887294
""",
)

entry(
    index = 244,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(86.5108,'m^3/(mol*s)'), n=1.58212, w0=(485000,'J/mol'), E0=(174850,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40550489441967746, var=13.200509779856521, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 8.302561402099661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.302561402099661""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.302561402099661
""",
)

entry(
    index = 245,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C",
    kinetics = Arrhenius(A=(1.28573e-06,'m^3/(mol*s)'), n=3.56699, Ea=(285.117,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C",
    kinetics = Arrhenius(A=(4.362e-07,'m^3/(mol*s)'), n=3.96684, Ea=(150.338,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C",
    kinetics = Arrhenius(A=(8.35e-05,'m^3/(mol*s)'), n=3.36, Ea=(157.1,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(3.34e-05,'m^3/(mol*s)'), n=3.35, Ea=(144.6,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(6.36293e-10,'m^3/(mol*s)'), n=4.82658, w0=(485000,'J/mol'), E0=(166599,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4745848157929178, var=0.005426392301846511, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 1.340101065798354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.340101065798354""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.340101065798354
""",
)

entry(
    index = 250,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C",
    kinetics = Arrhenius(A=(1.35e-05,'m^3/(mol*s)'), n=3.34, Ea=(146.4,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R",
    kinetics = Arrhenius(A=(2.894e-08,'m^3/(mol*s)'), n=4.35365, Ea=(170.388,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O",
    kinetics = Arrhenius(A=(7.33269e-08,'m^3/(mol*s)'), n=4.23045, Ea=(159.023,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O",
    kinetics = Arrhenius(A=(2.43e-05,'m^3/(mol*s)'), n=3.25, Ea=(157.6,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = Arrhenius(A=(1.14861e-16,'m^3/(mol*s)'), n=6.26453, Ea=(226.951,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R",
    kinetics = ArrheniusBM(A=(1.7293e-13,'m^3/(mol*s)'), n=5.12491, w0=(525000,'J/mol'), E0=(157523,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5013726110787028, var=13.96489584596274, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
    Total Standard Deviation in ln(k): 8.751351894928552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 8.751351894928552""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R
Total Standard Deviation in ln(k): 8.751351894928552
""",
)

entry(
    index = 256,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.08243e-09,'m^3/(mol*s)'), n=4.21524, w0=(525000,'J/mol'), E0=(162615,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.485292598479842, var=9.408855115100442, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 7.368623872542479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.368623872542479""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.368623872542479
""",
)

entry(
    index = 257,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C",
    kinetics = Arrhenius(A=(8.646e-12,'m^3/(mol*s)'), n=4.97681, Ea=(192.02,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(4.63361e-27,'m^3/(mol*s)'), n=9.35066, w0=(525000,'J/mol'), E0=(96874.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43700832665140077, var=0.5670635276126303, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 2.6076489677869423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.6076489677869423""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.6076489677869423
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
    kinetics = ArrheniusBM(A=(3.84196e-06,'m^3/(mol*s)'), n=3.49798, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.665203309540455, var=4.3201818670361956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 10.863342046260257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 10.863342046260257""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 10.863342046260257
""",
)

entry(
    index = 261,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH",
    kinetics = ArrheniusBM(A=(8.83138e-13,'m^3/(mol*s)'), n=5.47481, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.7638179571249553, var=0.19982645905098143, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 7.8404219534236175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.8404219534236175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_4BrCFILiNOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.8404219534236175
""",
)

entry(
    index = 262,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(1.81081e-08,'m^3/(mol*s)'), n=4.25573, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15025719955355346, var=0.8459446173470252, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.2213907035622658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.2213907035622658""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.2213907035622658
""",
)

entry(
    index = 263,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(7.38731e-10,'m^3/(mol*s)'), n=4.61046, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17597359401558216, var=0.8657986150496749, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.3075166194974868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.3075166194974868""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIILiLiLiNNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIILiLiLiNNNOOOPPPSSSSiSiSi_Sp-4BrCFILiNOPSSi-3BrCCClFFHILiNOPSSi_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.3075166194974868
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
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.42134e-06,'m^3/(mol*s)'), n=3.86844, w0=(525000,'J/mol'), E0=(163117,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41580743737409864, var=5.691333204676779, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 5.8273416020629565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 5.8273416020629565""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 5.8273416020629565
""",
)

entry(
    index = 268,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00402118,'m^3/(mol*s)'), n=3.10034, w0=(525000,'J/mol'), E0=(178323,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08508954654125812, var=0.39720517041394404, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.477261380280155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.477261380280155""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.477261380280155
""",
)

entry(
    index = 269,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.00165e-06,'m^3/(mol*s)'), n=3.59464, w0=(485000,'J/mol'), E0=(184952,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07250102782170646, var=7.212308675703701, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 5.5660281478605915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.5660281478605915""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.5660281478605915
""",
)

entry(
    index = 270,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000112402,'m^3/(mol*s)'), n=3.34714, w0=(485000,'J/mol'), E0=(193035,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11795421658362171, var=6.542481672455338, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 5.424133949364235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.424133949364235""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.424133949364235
""",
)

entry(
    index = 271,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F",
    kinetics = ArrheniusBM(A=(8.07231e-08,'m^3/(mol*s)'), n=4.09577, w0=(485000,'J/mol'), E0=(171551,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16433669165202913, var=1.1972750490415756, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
    Total Standard Deviation in ln(k): 2.606488672902054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.606488672902054""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.606488672902054
""",
)

entry(
    index = 272,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(8.39451e-08,'m^3/(mol*s)'), n=4.02792, w0=(485000,'J/mol'), E0=(170499,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.029092896180799535, var=0.06812993170645934, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
    Total Standard Deviation in ln(k): 0.5963678852903638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.5963678852903638""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.5963678852903638
""",
)

entry(
    index = 273,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C",
    kinetics = Arrhenius(A=(5.7299e-06,'m^3/(mol*s)'), n=3.76087, Ea=(211.861,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.78303e-07,'m^3/(mol*s)'), n=3.84344, w0=(485000,'J/mol'), E0=(181246,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1871194940764309, var=1.3244079947262366, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.7772572761037058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.7772572761037058""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.7772572761037058
""",
)

entry(
    index = 275,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(18997,'m^3/(mol*s)'), n=0.816859, w0=(485000,'J/mol'), E0=(176141,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5147737260969624, var=34.971339017284336, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 13.14871692909517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.14871692909517""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.14871692909517
""",
)

entry(
    index = 276,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0158947,'m^3/(mol*s)'), n=2.79402, w0=(485000,'J/mol'), E0=(172338,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15750843404516243, var=8.568385324107172, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.263971138772187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772187""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772187
""",
)

entry(
    index = 277,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C",
    kinetics = Arrhenius(A=(3.19591e-10,'m^3/(mol*s)'), n=4.92231, Ea=(157.168,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C",
    kinetics = Arrhenius(A=(1.29256e-09,'m^3/(mol*s)'), n=4.72835, Ea=(149.894,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.45546e-12,'m^3/(mol*s)'), n=4.72234, w0=(525000,'J/mol'), E0=(161049,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5516054794795432, var=8.701153406633509, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R
    Total Standard Deviation in ln(k): 7.299454323345523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.299454323345523""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.299454323345523
""",
)

entry(
    index = 280,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C",
    kinetics = Arrhenius(A=(1.65359e-14,'m^3/(mol*s)'), n=5.65246, Ea=(171.372,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(1.76438e-08,'m^3/(mol*s)'), n=3.82915, w0=(525000,'J/mol'), E0=(174006,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11993050856267691, var=1.1399188131592315, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C
    Total Standard Deviation in ln(k): 2.44172804585589"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.44172804585589""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C
Total Standard Deviation in ln(k): 2.44172804585589
""",
)

entry(
    index = 282,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(3.11507e-10,'m^3/(mol*s)'), n=4.50477, w0=(525000,'J/mol'), E0=(139938,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6312385292942253, var=0.5298110164819458, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 3.045235395133333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 3.045235395133333""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 3.045235395133333
""",
)

entry(
    index = 283,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O",
    kinetics = Arrhenius(A=(5.00048e-45,'m^3/(mol*s)'), n=14.5269, Ea=(79.3637,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_N-4FO->O
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
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.00141237,'m^3/(mol*s)'), n=2.8816, w0=(525000,'J/mol'), E0=(171467,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4221087960189235, var=24.145273027082244, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 10.911409976907715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 10.911409976907715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 10.911409976907715
""",
)

entry(
    index = 293,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.10667e-09,'m^3/(mol*s)'), n=4.67467, w0=(525000,'J/mol'), E0=(156348,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44384033024294384, var=1.1880731948002066, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 3.300313293224941"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.300313293224941""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.300313293224941
""",
)

entry(
    index = 294,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.5887e-06,'m^3/(mol*s)'), n=3.55743, w0=(485000,'J/mol'), E0=(187873,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06013887095373207, var=7.3506571663082205, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 5.586359556555985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.586359556555985""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.586359556555985
""",
)

entry(
    index = 295,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C",
    kinetics = Arrhenius(A=(2.5027e-05,'m^3/(mol*s)'), n=3.59925, Ea=(209.739,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(1.59331e-06,'m^3/(mol*s)'), n=3.65749, w0=(485000,'J/mol'), E0=(166454,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.1828431129345716, var=7.038275073340396, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 10.803041993865104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.803041993865104""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.803041993865104
""",
)

entry(
    index = 297,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O",
    kinetics = ArrheniusBM(A=(0.161805,'m^3/(mol*s)'), n=2.43246, w0=(485000,'J/mol'), E0=(190550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.289453500931442, var=26.57433800037729, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
    Total Standard Deviation in ln(k): 11.06174028820511"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.06174028820511""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.06174028820511
""",
)

entry(
    index = 298,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(7.52431e-05,'m^3/(mol*s)'), n=3.3977, w0=(485000,'J/mol'), E0=(193247,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09396692101335095, var=6.90691438934566, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
    Total Standard Deviation in ln(k): 5.504743871251022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.504743871251022""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.504743871251022
""",
)

entry(
    index = 299,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.17552e-08,'m^3/(mol*s)'), n=4.12767, w0=(485000,'J/mol'), E0=(171410,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17676832783233234, var=1.2172388419303009, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 2.655936621676801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.655936621676801""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.655936621676801
""",
)

entry(
    index = 300,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.34329e-08,'m^3/(mol*s)'), n=4.02818, w0=(485000,'J/mol'), E0=(170493,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028056319435529276, var=0.062635345862288, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 0.5722194059850624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.5722194059850624""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.5722194059850624
""",
)

entry(
    index = 301,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C",
    kinetics = ArrheniusBM(A=(3.39606e-06,'m^3/(mol*s)'), n=3.80021, w0=(485000,'J/mol'), E0=(174462,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2499361162926234, var=0.047641473097666344, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
    Total Standard Deviation in ln(k): 1.0655522483929947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 1.0655522483929947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 1.0655522483929947
""",
)

entry(
    index = 302,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C",
    kinetics = Arrhenius(A=(5.29538e-06,'m^3/(mol*s)'), n=3.74, Ea=(187.567,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.22404e-07,'m^3/(mol*s)'), n=3.97282, w0=(485000,'J/mol'), E0=(180806,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7393695614252405, var=2.81054508868293, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.21858675153661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.21858675153661""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.21858675153661
""",
)

entry(
    index = 304,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0092216,'m^3/(mol*s)'), n=2.80922, w0=(485000,'J/mol'), E0=(151683,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.33265691981176637, var=4.25485772067976, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.971049889141971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.971049889141971""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.971049889141971
""",
)

entry(
    index = 305,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R",
    kinetics = Arrhenius(A=(1.71639e-05,'m^3/(mol*s)'), n=3.56319, Ea=(226.133,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.77086e-10,'m^3/(mol*s)'), n=3.799, w0=(525000,'J/mol'), E0=(168754,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5227374995623466, var=47.32046836774436, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 15.103958245331869"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 15.103958245331869""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 15.103958245331869
""",
)

entry(
    index = 307,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.55352e-15,'m^3/(mol*s)'), n=5.47489, w0=(525000,'J/mol'), E0=(154838,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5382351976252426, var=1.1878227718065575, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.5372560223163907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.5372560223163907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.5372560223163907
""",
)

entry(
    index = 308,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O",
    kinetics = Arrhenius(A=(7.33133e-11,'m^3/(mol*s)'), n=4.61882, Ea=(195.681,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(1.95851e-08,'m^3/(mol*s)'), n=3.80315, w0=(525000,'J/mol'), E0=(174715,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27112014202881796, var=0.5146851543055032, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 2.1194346210204436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 2.1194346210204436""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 2.1194346210204436
""",
)

entry(
    index = 310,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C",
    kinetics = Arrhenius(A=(1.10502e-10,'m^3/(mol*s)'), n=4.61742, Ea=(180.926,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C",
    kinetics = Arrhenius(A=(2.93442e-08,'m^3/(mol*s)'), n=4.04113, Ea=(190.261,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFILiNOPSSi->C_4FO->O_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(0.104833,'m^3/(mol*s)'), n=2.12, Ea=(147.266,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(0.001275,'m^3/(mol*s)'), n=3.12, Ea=(147.53,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.68723e-05,'m^3/(mol*s)'), n=2.95314, w0=(485000,'J/mol'), E0=(193710,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003004602981835939, var=14.743691214756439, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
    Total Standard Deviation in ln(k): 7.705233678445651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445651""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445651
""",
)

entry(
    index = 315,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.96738e-07,'m^3/(mol*s)'), n=3.83776, w0=(485000,'J/mol'), E0=(185203,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07873236803044407, var=1.7540342494307302, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 2.85289031614716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.85289031614716""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.85289031614716
""",
)

entry(
    index = 316,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R",
    kinetics = Arrhenius(A=(1.5333e-06,'m^3/(mol*s)'), n=3.65941, Ea=(175.65,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C",
    kinetics = Arrhenius(A=(1.21333e-05,'m^3/(mol*s)'), n=3.66599, Ea=(177.696,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 318,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C",
    kinetics = Arrhenius(A=(3.38922e-05,'m^3/(mol*s)'), n=3.5758, Ea=(187.056,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R",
    kinetics = Arrhenius(A=(0.00331206,'m^3/(mol*s)'), n=2.81802, Ea=(200.76,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.13904e-05,'m^3/(mol*s)'), n=3.55174, w0=(485000,'J/mol'), E0=(193130,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.029234580826764514, var=7.287478571292758, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 5.485302275239592"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.485302275239592""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.485302275239592
""",
)

entry(
    index = 321,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R",
    kinetics = Arrhenius(A=(0.839925,'m^3/(mol*s)'), n=2.36463, Ea=(229.198,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.73459e-08,'m^3/(mol*s)'), n=4.20668, w0=(485000,'J/mol'), E0=(169243,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1687503557079864, var=1.182015404971815, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.6035545073055824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.6035545073055824""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.6035545073055824
""",
)

entry(
    index = 323,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.8448e-07,'m^3/(mol*s)'), n=3.87956, w0=(485000,'J/mol'), E0=(178077,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9414292247845112, var=6.576990579197837, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 7.506672280009452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.506672280009452""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.506672280009452
""",
)

entry(
    index = 324,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C",
    kinetics = ArrheniusBM(A=(1.00712e-07,'m^3/(mol*s)'), n=4.01588, w0=(485000,'J/mol'), E0=(170290,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10121089927251038, var=0.022957521836780116, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C
    Total Standard Deviation in ln(k): 0.5580509841004793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C
Total Standard Deviation in ln(k): 0.5580509841004793""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C
Total Standard Deviation in ln(k): 0.5580509841004793
""",
)

entry(
    index = 325,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C",
    kinetics = ArrheniusBM(A=(6.28254e-08,'m^3/(mol*s)'), n=4.04866, w0=(485000,'J/mol'), E0=(170729,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06962334785444124, var=0.2364469489169405, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C
    Total Standard Deviation in ln(k): 1.1497517233085692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C
Total Standard Deviation in ln(k): 1.1497517233085692""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C
Total Standard Deviation in ln(k): 1.1497517233085692
""",
)

entry(
    index = 326,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R",
    kinetics = Arrhenius(A=(4.51365e-06,'m^3/(mol*s)'), n=3.78897, Ea=(180.153,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 327,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(3.63e-05,'m^3/(mol*s)'), n=3.37, Ea=(183.4,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C",
    kinetics = Arrhenius(A=(3.56033e-08,'m^3/(mol*s)'), n=4.21745, Ea=(194.395,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(2.58576e-05,'m^3/(mol*s)'), n=3.2457, Ea=(188.78,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C",
    kinetics = Arrhenius(A=(4.47723e-05,'m^3/(mol*s)'), n=3.46134, Ea=(198.066,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(3.5032e-05,'m^3/(mol*s)'), n=3.5135, Ea=(211.783,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C",
    kinetics = Arrhenius(A=(5.44367e-08,'m^3/(mol*s)'), n=2.98637, Ea=(209.666,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(6.71872e-09,'m^3/(mol*s)'), n=3.87148, Ea=(192.37,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-4BrCFILiNOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.84546e-08,'m^3/(mol*s)'), n=3.73033, w0=(525000,'J/mol'), E0=(177268,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7733021379689362, var=0.3972253154803849, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 3.20647078495611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.20647078495611""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFILiNOPSSi->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.20647078495611
""",
)

entry(
    index = 335,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R",
    kinetics = Arrhenius(A=(0.000145249,'m^3/(mol*s)'), n=2.84864, Ea=(208.333,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O",
    kinetics = Arrhenius(A=(2.47232e-06,'m^3/(mol*s)'), n=3.97637, Ea=(171.25,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.86868e-07,'m^3/(mol*s)'), n=3.84756, w0=(485000,'J/mol'), E0=(182425,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09720191356503283, var=2.0878264080310385, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O
    Total Standard Deviation in ln(k): 3.1409303377701763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.1409303377701763""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.1409303377701763
""",
)

entry(
    index = 338,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.50059e-05,'m^3/(mol*s)'), n=3.79283, w0=(485000,'J/mol'), E0=(187071,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006525647083063791, var=2.1379077683223744, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
    Total Standard Deviation in ln(k): 2.9476367301167716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 2.9476367301167716""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 2.9476367301167716
""",
)

entry(
    index = 339,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(7.70594e-06,'m^3/(mol*s)'), n=3.51762, w0=(485000,'J/mol'), E0=(196673,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.051044128206725894, var=1.791325848414104, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 2.8113974602086755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8113974602086755""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8113974602086755
""",
)

entry(
    index = 340,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.6394e-08,'m^3/(mol*s)'), n=4.20067, w0=(485000,'J/mol'), E0=(170780,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22661832906730342, var=4.962422799104257, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.035240106288149"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.035240106288149""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.035240106288149
""",
)

entry(
    index = 341,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.43184e-08,'m^3/(mol*s)'), n=4.29567, w0=(485000,'J/mol'), E0=(166364,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1435250581045705, var=0.36009224513264615, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 1.5636108663243007"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663243007""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663243007
""",
)

entry(
    index = 342,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(5.94509e-05,'m^3/(mol*s)'), n=3.37621, w0=(485000,'J/mol'), E0=(190611,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14501143760180213, var=0.5353198014536561, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 1.8311258333110598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.8311258333110598""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.8311258333110598
""",
)

entry(
    index = 343,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(2.46664e-07,'m^3/(mol*s)'), n=4.015, w0=(485000,'J/mol'), E0=(174920,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8464453142362636, var=15.358982914588138, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 12.495974515953652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 12.495974515953652""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 12.495974515953652
""",
)

entry(
    index = 344,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O",
    kinetics = Arrhenius(A=(9.11574e-08,'m^3/(mol*s)'), n=4.14961, Ea=(160.609,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.04194e-07,'m^3/(mol*s)'), n=3.9712, w0=(485000,'J/mol'), E0=(168046,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12446773206423278, var=0.037958477710098464, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O
    Total Standard Deviation in ln(k): 0.7033142379330838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O
Total Standard Deviation in ln(k): 0.7033142379330838""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O
Total Standard Deviation in ln(k): 0.7033142379330838
""",
)

entry(
    index = 346,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.02747e-08,'m^3/(mol*s)'), n=4.09468, w0=(485000,'J/mol'), E0=(170972,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.134457919534933, var=0.5134742245781816, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.7743693047131623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.7743693047131623""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.7743693047131623
""",
)

entry(
    index = 347,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C",
    kinetics = Arrhenius(A=(3.8501e-07,'m^3/(mol*s)'), n=3.92844, Ea=(168.206,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C",
    kinetics = ArrheniusBM(A=(9.19464e-07,'m^3/(mol*s)'), n=3.75122, w0=(485000,'J/mol'), E0=(180112,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1705285014275157, var=3.515806757001901, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C
    Total Standard Deviation in ln(k): 4.18743900685402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.18743900685402""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.18743900685402
""",
)

entry(
    index = 349,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R",
    kinetics = Arrhenius(A=(2.68364e-05,'m^3/(mol*s)'), n=3.9376, Ea=(220.387,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C",
    kinetics = Arrhenius(A=(2.28891e-06,'m^3/(mol*s)'), n=3.82239, Ea=(199.241,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C",
    kinetics = Arrhenius(A=(0.00168439,'m^3/(mol*s)'), n=3.12619, Ea=(212.504,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(1.43048e-06,'m^3/(mol*s)'), n=3.73988, w0=(485000,'J/mol'), E0=(195276,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.029338637895189975, var=3.7318857833729955, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 3.9464803168381795"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 3.9464803168381795""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 3.9464803168381795
""",
)

entry(
    index = 353,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(0.00139208,'m^3/(mol*s)'), n=2.83125, w0=(485000,'J/mol'), E0=(200963,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13183536540997565, var=3.223334108219495, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 3.9304750612568586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 3.9304750612568586""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 3.9304750612568586
""",
)

entry(
    index = 354,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C",
    kinetics = Arrhenius(A=(1.31087e-08,'m^3/(mol*s)'), n=4.12499, Ea=(167.866,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2.14559e-08,'m^3/(mol*s)'), n=4.27069, Ea=(171.076,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = Arrhenius(A=(3.45985e-08,'m^3/(mol*s)'), n=4.20193, Ea=(180.794,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = Arrhenius(A=(6.21207e-09,'m^3/(mol*s)'), n=4.38354, Ea=(182.296,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = Arrhenius(A=(0.0001135,'m^3/(mol*s)'), n=3.32, Ea=(190.5,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.05887e-05,'m^3/(mol*s)'), n=3.30617, w0=(485000,'J/mol'), E0=(194239,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21443168705568819, var=0.08400851638092321, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.1198299618386824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.1198299618386824""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.1198299618386824
""",
)

entry(
    index = 360,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.11393e-08,'m^3/(mol*s)'), n=3.97251, w0=(485000,'J/mol'), E0=(166791,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12852274226468013, var=0.13186923682206084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R
    Total Standard Deviation in ln(k): 1.0509170317075238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.0509170317075238""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.0509170317075238
""",
)

entry(
    index = 361,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C",
    kinetics = Arrhenius(A=(4.11856e-08,'m^3/(mol*s)'), n=4.0381, Ea=(156.944,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(6.32707e-08,'m^3/(mol*s)'), n=4.09227, Ea=(155.795,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R",
    kinetics = Arrhenius(A=(6.83125e-07,'m^3/(mol*s)'), n=3.8806, Ea=(187.286,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C",
    kinetics = Arrhenius(A=(6.55056e-06,'m^3/(mol*s)'), n=3.42741, Ea=(176.063,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C",
    kinetics = Arrhenius(A=(3.50479e-07,'m^3/(mol*s)'), n=3.85832, Ea=(170.202,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C",
    kinetics = Arrhenius(A=(5.76532e-06,'m^3/(mol*s)'), n=3.58647, Ea=(216.806,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 367,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.00057e-07,'m^3/(mol*s)'), n=4.05084, Ea=(207.795,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFILiNPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 368,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00676459,'m^3/(mol*s)'), n=2.69433, w0=(485000,'J/mol'), E0=(203145,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1920396451478082, var=11.520881032749767, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.287068342570428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570428""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570428
""",
)

entry(
    index = 369,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R",
    kinetics = Arrhenius(A=(2.96e-05,'m^3/(mol*s)'), n=3.23, Ea=(198.7,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(4.915e-05,'m^3/(mol*s)'), n=3.31, Ea=(175.6,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIILiLiNNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C",
    kinetics = Arrhenius(A=(7.80562e-08,'m^3/(mol*s)'), n=3.96948, Ea=(152.853,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C",
    kinetics = Arrhenius(A=(1.03271e-07,'m^3/(mol*s)'), n=3.97927, Ea=(151.975,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->C_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 373,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(0.000284922,'m^3/(mol*s)'), n=3.00496, Ea=(211.308,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHILiNPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFILiNPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

