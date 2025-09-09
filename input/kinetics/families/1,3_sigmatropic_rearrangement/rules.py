#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.44525e+19,'s^-1'), n=-1.98438, w0=(667083,'J/mol'), E0=(310804,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.31616664944774464, var=131.71928722150497, Tref=1000.0, N=36, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 36 training reactions at node Root
    Total Standard Deviation in ln(k): 23.802537258508377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root
Total Standard Deviation in ln(k): 23.802537258508377""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root
Total Standard Deviation in ln(k): 23.802537258508377
""",
)

entry(
    index = 2,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(4.2264e+32,'s^-1'), n=-5.09791, w0=(654062,'J/mol'), E0=(349148,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17553162581720022, var=186.81115526145044, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 27.841528221120058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 27.841528221120058""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 27.841528221120058
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.13774e+14,'s^-1'), n=-0.428263, w0=(670804,'J/mol'), E0=(294717,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.29317989260212285, var=130.3593380846165, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 23.625698436963873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 23.625698436963873""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 23.625698436963873
""",
)

entry(
    index = 4,
    label = "Root_1R!H-inRing_2R!H->O",
    kinetics = ArrheniusBM(A=(2.24622e+41,'s^-1'), n=-7.64484, w0=(670125,'J/mol'), E0=(328736,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37673372247386944, var=394.09103067267483, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->O
    Total Standard Deviation in ln(k): 40.74401887829801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->O
Total Standard Deviation in ln(k): 40.74401887829801""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->O
Total Standard Deviation in ln(k): 40.74401887829801
""",
)

entry(
    index = 5,
    label = "Root_1R!H-inRing_N-2R!H->O",
    kinetics = ArrheniusBM(A=(2.37375e+29,'s^-1'), n=-4.11962, w0=(638000,'J/mol'), E0=(383569,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12006085095723382, var=88.79351309347992, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->O
    Total Standard Deviation in ln(k): 19.19234119641417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->O
Total Standard Deviation in ln(k): 19.19234119641417""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->O
Total Standard Deviation in ln(k): 19.19234119641417
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H-inRing_2R!H->N",
    kinetics = Arrhenius(A=(2.6203e+13,'s^-1'), n=0.0689932, Ea=(168.747,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-3.289723543435457e-15, var=72.89065172155334, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 17.11563065368294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 17.11563065368294""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 17.11563065368294
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(69805.3,'s^-1'), n=2.11195, w0=(677500,'J/mol'), E0=(292121,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.025251670000919324, var=103.94474513515149, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 20.50238123087499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 20.50238123087499""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 20.50238123087499
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_2R!H->O_4R!H->C",
    kinetics = ArrheniusBM(A=(1.11662e+44,'s^-1'), n=-8.43539, w0=(707000,'J/mol'), E0=(370675,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4438197857755845, var=494.56930035252196, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->O_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C
    Total Standard Deviation in ln(k): 45.69825626955423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C
Total Standard Deviation in ln(k): 45.69825626955423""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C
Total Standard Deviation in ln(k): 45.69825626955423
""",
)

entry(
    index = 9,
    label = "Root_1R!H-inRing_2R!H->O_N-4R!H->C",
    kinetics = Arrhenius(A=(3.23202e+11,'s^-1'), n=0.959257, Ea=(243.463,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->O_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.44257e+24,'s^-1'), n=-2.64378, w0=(645667,'J/mol'), E0=(390586,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.010257129349852259, var=79.0558298443144, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 17.850541912442168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 17.850541912442168""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 17.850541912442168
""",
)

entry(
    index = 11,
    label = "Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_N-5R!H->C",
    kinetics = Arrhenius(A=(3.92014e+10,'s^-1'), n=1.31782, Ea=(406.92,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C",
    kinetics = Arrhenius(A=(1.84529e+13,'s^-1'), n=0.118931, Ea=(182.261,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-4.7719066783898936e-15, var=54.82417730626182, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
    Total Standard Deviation in ln(k): 14.843730168865235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 14.843730168865235""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 14.843730168865235
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->C",
    kinetics = Arrhenius(A=(3.05043e+14,'s^-1'), n=-0.280572, Ea=(74.1506,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O",
    kinetics = ArrheniusBM(A=(3871.92,'s^-1'), n=2.44771, w0=(700500,'J/mol'), E0=(310498,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5989535375272125, var=99.03254865763193, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O
    Total Standard Deviation in ln(k): 21.45504929163672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O
Total Standard Deviation in ln(k): 21.45504929163672""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O
Total Standard Deviation in ln(k): 21.45504929163672
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O",
    kinetics = ArrheniusBM(A=(801448,'s^-1'), n=1.82748, w0=(667643,'J/mol'), E0=(277586,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.05209316202407, var=145.43120658103692, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O
    Total Standard Deviation in ln(k): 26.819525087594652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O
Total Standard Deviation in ln(k): 26.819525087594652""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O
Total Standard Deviation in ln(k): 26.819525087594652
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-1R!H-R",
    kinetics = Arrhenius(A=(1.61854e+10,'s^-1'), n=0.947053, Ea=(380.965,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_5R!H->C",
    kinetics = Arrhenius(A=(1.42792e+11,'s^-1'), n=1.12171, Ea=(360.677,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(7.48935e+10,'s^-1'), n=1.24936, Ea=(321.691,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->O_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(7.49547e+23,'s^-1'), n=-2.59726, w0=(661000,'J/mol'), E0=(404145,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22003588140388403, var=198.71575416114922, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 28.81291784350448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.81291784350448""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.81291784350448
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R",
    kinetics = Arrhenius(A=(5.24437e+12,'s^-1'), n=0.139323, Ea=(217.383,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.061113143746858e-16, var=26.820064402959662, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 10.38214039907133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.38214039907133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.38214039907133
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O",
    kinetics = ArrheniusBM(A=(6.3243e-38,'s^-1'), n=14.6823, w0=(707000,'J/mol'), E0=(9771.93,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-7.060098847191699, var=165.3314455210392, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O
    Total Standard Deviation in ln(k): 43.51608126760444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O
Total Standard Deviation in ln(k): 43.51608126760444""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O
Total Standard Deviation in ln(k): 43.51608126760444
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O",
    kinetics = ArrheniusBM(A=(3.83511e+16,'s^-1'), n=-0.852167, w0=(615000,'J/mol'), E0=(312143,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38447838081347113, var=56.60853028627362, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O
    Total Standard Deviation in ln(k): 16.0493802668064"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O
Total Standard Deviation in ln(k): 16.0493802668064""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O
Total Standard Deviation in ln(k): 16.0493802668064
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(87.8724,'s^-1'), n=2.82643, w0=(700500,'J/mol'), E0=(296620,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9109093232499327, var=212.64838865563013, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 31.52270308529138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 31.52270308529138""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 31.52270308529138
""",
)

entry(
    index = 24,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C",
    kinetics = ArrheniusBM(A=(5.30622e+06,'s^-1'), n=1.61778, w0=(661083,'J/mol'), E0=(304914,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6471711806600602, var=110.98297996862185, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C
    Total Standard Deviation in ln(k): 25.2581963419055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C
Total Standard Deviation in ln(k): 25.2581963419055""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C
Total Standard Deviation in ln(k): 25.2581963419055
""",
)

entry(
    index = 25,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C",
    kinetics = ArrheniusBM(A=(2.27249e+12,'s^-1'), n=-0.17563, w0=(707000,'J/mol'), E0=(140349,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22902927274512822, var=32.41664691073636, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C
    Total Standard Deviation in ln(k): 11.989533655349739"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C
Total Standard Deviation in ln(k): 11.989533655349739""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C
Total Standard Deviation in ln(k): 11.989533655349739
""",
)

entry(
    index = 26,
    label = "Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->O",
    kinetics = Arrhenius(A=(1.02334e+09,'s^-1'), n=1.56661, Ea=(426.407,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->O",
    kinetics = Arrhenius(A=(8.04681e+10,'s^-1'), n=1.21369, Ea=(447.107,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->O_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing",
    kinetics = Arrhenius(A=(2.72427e+12,'s^-1'), n=0.399431, Ea=(242.1,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing",
    kinetics = Arrhenius(A=(1.00957e+13,'s^-1'), n=-0.120785, Ea=(192.666,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_5R!H->N",
    kinetics = Arrhenius(A=(1.84179e+16,'s^-1'), n=-0.625332, Ea=(104.652,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N",
    kinetics = Arrhenius(A=(8.38538e+12,'s^-1'), n=0.316231, Ea=(165.869,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.061113143746858e-16, var=10.185941174285585, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N
    Total Standard Deviation in ln(k): 6.398196461102944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N
Total Standard Deviation in ln(k): 6.398196461102944""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N
Total Standard Deviation in ln(k): 6.398196461102944
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_5R!H->C",
    kinetics = Arrhenius(A=(3.6546e+12,'s^-1'), n=0.372553, Ea=(235.091,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(5.59681e+12,'s^-1'), n=0.174189, Ea=(169.578,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-3R!H->O_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.12337e+07,'s^-1'), n=1.41588, w0=(700500,'J/mol'), E0=(340735,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.42828928839650815, var=124.35966862039706, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 23.432241003693804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 23.432241003693804""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 23.432241003693804
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = Arrhenius(A=(1.575e+06,'s^-1'), n=1.45, Ea=(203.329,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br",
    kinetics = ArrheniusBM(A=(6.98407e+11,'s^-1'), n=0.40768, w0=(541000,'J/mol'), E0=(206783,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005374602454953211, var=0.05576325998062114, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br
    Total Standard Deviation in ln(k): 0.486907093004907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br
Total Standard Deviation in ln(k): 0.486907093004907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br
Total Standard Deviation in ln(k): 0.486907093004907
""",
)

entry(
    index = 37,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(1.58044e+07,'s^-1'), n=1.47587, w0=(685100,'J/mol'), E0=(308725,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.39241518342786463, var=98.21793495800205, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br
    Total Standard Deviation in ln(k): 20.853887166889216"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br
Total Standard Deviation in ln(k): 20.853887166889216""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br
Total Standard Deviation in ln(k): 20.853887166889216
""",
)

entry(
    index = 38,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C_Ext-1R!H-R",
    kinetics = Arrhenius(A=(2.75554e+14,'s^-1'), n=-0.892455, Ea=(121.354,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_N-3CN->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_2N-inRing",
    kinetics = Arrhenius(A=(8.05136e+14,'s^-1'), n=-0.0703128, Ea=(172.238,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_N-2N-inRing",
    kinetics = Arrhenius(A=(8.73327e+10,'s^-1'), n=0.702774, Ea=(159.501,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_N-2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_N-2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_3R!H->O_Ext-4C-R_N-5R!H->N_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.42803e+06,'s^-1'), n=1.60892, w0=(700500,'J/mol'), E0=(342452,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2231192844612943, var=433.45320073431793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 42.298261180180546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 42.298261180180546""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 42.298261180180546
""",
)

entry(
    index = 42,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br_Ext-2CO-R",
    kinetics = Arrhenius(A=(1.94657e+12,'s^-1'), n=0.28187, Ea=(223.254,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_4R!H->Br_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl",
    kinetics = ArrheniusBM(A=(4.21261e+11,'s^-1'), n=0.487024, w0=(583000,'J/mol'), E0=(230508,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0054459225153581665, var=0.10372712383063455, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl
    Total Standard Deviation in ln(k): 0.6593421453781982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 0.6593421453781982""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 0.6593421453781982
""",
)

entry(
    index = 44,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(3.5214e+07,'s^-1'), n=1.36938, w0=(710625,'J/mol'), E0=(311757,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3496844039937167, var=97.31486359691459, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl
    Total Standard Deviation in ln(k): 20.654974018660283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 20.654974018660283""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 20.654974018660283
""",
)

entry(
    index = 45,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = Arrhenius(A=(7.89e+07,'s^-1'), n=1.5, Ea=(485.946,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->O_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R",
    kinetics = Arrhenius(A=(1.046e+12,'s^-1'), n=0.380659, Ea=(252.531,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R",
    kinetics = Arrhenius(A=(1.69499e+12,'s^-1'), n=0.570599, Ea=(365.404,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_2CO->C",
    kinetics = Arrhenius(A=(2.11883e+10,'s^-1'), n=0.811585, Ea=(262.426,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.22434e+07,'s^-1'), n=1.41678, w0=(700500,'J/mol'), E0=(311505,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.33230618666219447, var=101.51497053367527, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C
    Total Standard Deviation in ln(k): 21.03357584335347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C
Total Standard Deviation in ln(k): 21.03357584335347""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C
Total Standard Deviation in ln(k): 21.03357584335347
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(162029,'s^-1'), n=1.90916, w0=(700500,'J/mol'), E0=(297271,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7266283156454434, var=174.1365176737815, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R
    Total Standard Deviation in ln(k): 30.79290582346446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R
Total Standard Deviation in ln(k): 30.79290582346446""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R
Total Standard Deviation in ln(k): 30.79290582346446
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O",
    kinetics = ArrheniusBM(A=(808.708,'s^-1'), n=2.38171, w0=(700500,'J/mol'), E0=(223063,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3611790105817516, var=117.41376442524758, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O
    Total Standard Deviation in ln(k): 22.630319556225114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O
Total Standard Deviation in ln(k): 22.630319556225114""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O
Total Standard Deviation in ln(k): 22.630319556225114
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(5.23426e+08,'s^-1'), n=1.09066, w0=(700500,'J/mol'), E0=(374409,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3940358245667278, var=173.63083761942787, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O
    Total Standard Deviation in ln(k): 27.40624435633584"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 27.40624435633584""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 27.40624435633584
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R",
    kinetics = Arrhenius(A=(5.4394e+08,'s^-1'), n=0.631892, Ea=(211.416,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R",
    kinetics = Arrhenius(A=(8.67544e+08,'s^-1'), n=1.19995, Ea=(366.787,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->O_3CN->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

