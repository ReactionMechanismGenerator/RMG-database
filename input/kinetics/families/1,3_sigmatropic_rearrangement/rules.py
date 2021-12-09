#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.11403e+20,'s^-1'), n=-1.91643, w0=(671167,'J/mol'), E0=(227910,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2489853322397734, var=103.35155747037187, Tref=1000.0, N=24, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 24 training reactions at node Root
    Total Standard Deviation in ln(k): 21.006122624958927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root
Total Standard Deviation in ln(k): 21.006122624958927""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root
Total Standard Deviation in ln(k): 21.006122624958927
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.26563e-22,'s^-1'), n=10.0023, w0=(636417,'J/mol'), E0=(45254.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4448894413899516, var=25.919851613271362, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
    Total Standard Deviation in ln(k): 13.836790993424374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 13.836790993424374""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 13.836790993424374
""",
)

entry(
    index = 3,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.047e+66,'s^-1'), n=-14.5812, w0=(654062,'J/mol'), E0=(401059,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5126184551256572, var=267.3876986170645, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 36.58196427792415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 36.58196427792415""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 36.58196427792415
""",
)

entry(
    index = 4,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.42921e+12,'s^-1'), n=0.272588, w0=(705700,'J/mol'), E0=(162073,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0169552558958688, var=18.84203515518181, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 8.744637519563351"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 8.744637519563351""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 8.744637519563351
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.95709e-15,'s^-1'), n=7.94274, w0=(624125,'J/mol'), E0=(36543.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8896120741680805, var=1.6673814255816741, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 4.823862973780159"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 4.823862973780159""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 4.823862973780159
""",
)

entry(
    index = 6,
    label = "Root_Ext-2R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.29289e-37,'s^-1'), n=14.1215, w0=(661000,'J/mol'), E0=(16586.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.725930562005685, var=31.20912802912534, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 33.12392731476194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 33.12392731476194""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 33.12392731476194
""",
)

entry(
    index = 7,
    label = "Root_1R!H-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(4.83039e+87,'s^-1'), n=-20.7641, w0=(638000,'J/mol'), E0=(482767,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.129184246830301, var=422.90828088074545, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 51.60167822215132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 51.60167822215132""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 51.60167822215132
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(3.57104e+57,'s^-1'), n=-12.1805, w0=(670125,'J/mol'), E0=(355647,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.427142357120706, var=535.1560083290228, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 49.96220180328063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 49.96220180328063""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 49.96220180328063
""",
)

entry(
    index = 9,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.17409e+12,'s^-1'), n=0.297212, w0=(707000,'J/mol'), E0=(161155,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025396941674194665, var=16.021570096630306, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 8.088155191452177"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.088155191452177""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.088155191452177
""",
)

entry(
    index = 10,
    label = "Root_N-1R!H-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(0.0196531,'s^-1'), n=4.11861, w0=(700500,'J/mol'), E0=(370385,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700500,'J/mol'), E0=(383041,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(7.98007e+11,'s^-1'), n=0.338845, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_Ext-2R!H-R_5R!H->C_4R!H->C",
    kinetics = ArrheniusBM(A=(1.5457e-15,'s^-1'), n=7.99283, w0=(661000,'J/mol'), E0=(66100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.92545895214582, var=0.05532539280288581, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C
    Total Standard Deviation in ln(k): 20.384754211192494"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C
Total Standard Deviation in ln(k): 20.384754211192494""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C
Total Standard Deviation in ln(k): 20.384754211192494
""",
)

entry(
    index = 14,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(7.5809e+11,'s^-1'), n=0.263048, w0=(559500,'J/mol'), E0=(131897,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-2R!H-R_N-5R!H->C_3R!H->N",
    kinetics = ArrheniusBM(A=(3.90941e+10,'s^-1'), n=0.721594, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N",
    kinetics = ArrheniusBM(A=(9.08391e+10,'s^-1'), n=0.559605, w0=(707000,'J/mol'), E0=(197781,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(2.5627e-25,'s^-1'), n=11.532, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0471320207033354, var=37.83890763345716, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N
    Total Standard Deviation in ln(k): 14.96277963690898"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 14.96277963690898""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 14.96277963690898
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_2R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.5373e+10,'s^-1'), n=1.12018, w0=(707000,'J/mol'), E0=(429584,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->C",
    kinetics = ArrheniusBM(A=(4.83275e+67,'s^-1'), n=-15.104, w0=(707000,'J/mol'), E0=(416393,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5423715033712326, var=749.7290753599457, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C
    Total Standard Deviation in ln(k): 58.76731938407889"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 58.76731938407889""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 58.76731938407889
""",
)

entry(
    index = 20,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.0435e+11,'s^-1'), n=1.01704, w0=(559500,'J/mol'), E0=(124536,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N",
    kinetics = ArrheniusBM(A=(4.6152e+12,'s^-1'), n=0.237708, w0=(707000,'J/mol'), E0=(162124,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.026486858660185405, var=26.778014476754585, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
    Total Standard Deviation in ln(k): 10.44054826608419"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
Total Standard Deviation in ln(k): 10.44054826608419""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
Total Standard Deviation in ln(k): 10.44054826608419
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N",
    kinetics = ArrheniusBM(A=(2.94384e+11,'s^-1'), n=0.35852, w0=(707000,'J/mol'), E0=(160169,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.016746619657169413, var=20.83377532884782, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
    Total Standard Deviation in ln(k): 9.19249586318171"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
Total Standard Deviation in ln(k): 9.19249586318171""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
Total Standard Deviation in ln(k): 9.19249586318171
""",
)

entry(
    index = 23,
    label = "Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->N",
    kinetics = ArrheniusBM(A=(1.00046e+12,'s^-1'), n=0.355217, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->N",
    kinetics = ArrheniusBM(A=(7.58556e+11,'s^-1'), n=0.301396, w0=(707000,'J/mol'), E0=(70700,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->C_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.08157e-17,'s^-1'), n=9.35044, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.803854354883043, var=0.32490167187561364, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 20.75037619267036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 20.75037619267036""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 20.75037619267036
""",
)

entry(
    index = 26,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.1544e+10,'s^-1'), n=1.34775, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(707000,'J/mol'), E0=(430709,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.6259e+11,'s^-1'), n=1.19107, w0=(707000,'J/mol'), E0=(70700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.23586e+11,'s^-1'), n=1.27308, w0=(707000,'J/mol'), E0=(191263,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O",
    kinetics = ArrheniusBM(A=(1.4157e+13,'s^-1'), n=0.116469, w0=(707000,'J/mol'), E0=(150200,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.024797229953593753, var=12.258043364057169, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O
    Total Standard Deviation in ln(k): 7.08118053561588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O
Total Standard Deviation in ln(k): 7.08118053561588""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O
Total Standard Deviation in ln(k): 7.08118053561588
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O",
    kinetics = ArrheniusBM(A=(2.30252e+10,'s^-1'), n=0.837267, w0=(707000,'J/mol'), E0=(195266,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N",
    kinetics = ArrheniusBM(A=(1.50036e+10,'s^-1'), n=0.759237, w0=(707000,'J/mol'), E0=(181473,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0031826932391024877, var=21.29156289472698, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N
    Total Standard Deviation in ln(k): 9.258401991518488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N
Total Standard Deviation in ln(k): 9.258401991518488""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N
Total Standard Deviation in ln(k): 9.258401991518488
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N",
    kinetics = ArrheniusBM(A=(8.99356e+09,'s^-1'), n=0.762386, w0=(707000,'J/mol'), E0=(131558,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0013555408842965467, var=1.8883622591608438, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N
    Total Standard Deviation in ln(k): 2.758266593399976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 2.758266593399976""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 2.758266593399976
""",
)

entry(
    index = 34,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.04679e+11,'s^-1'), n=1.26667, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.88231e+11,'s^-1'), n=0.661449, w0=(707000,'J/mol'), E0=(168563,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.57015e+11,'s^-1'), n=0.576299, w0=(707000,'J/mol'), E0=(133711,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.10312e+11,'s^-1'), n=0.507696, w0=(707000,'J/mol'), E0=(169853,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.85823e+11,'s^-1'), n=0.331305, w0=(707000,'J/mol'), E0=(135901,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_N-5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

