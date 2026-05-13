#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftC/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.68145e+12,'s^-1'), n=0.116389, w0=(368.569,'kJ/mol'), E0=(188.558,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05582194602018226, var=22.847189733569515, Tref=1000.0, N=14, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 14 training reactions at node Root
    Total Standard Deviation in ln(k): 9.722636019102342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 9.722636019102342""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 9.722636019102342
""",
)

entry(
    index = 2,
    label = "Root_2C-inRing",
    kinetics = ArrheniusBM(A=(5.38641e+08,'s^-1'), n=1.08691, w0=(346,'kJ/mol'), E0=(115.355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007608366987764202, var=6.88408757744791, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_2C-inRing
    Total Standard Deviation in ln(k): 5.279049142836315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2C-inRing
Total Standard Deviation in ln(k): 5.279049142836315""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2C-inRing
Total Standard Deviation in ln(k): 5.279049142836315
""",
)

entry(
    index = 3,
    label = "Root_N-2C-inRing",
    kinetics = ArrheniusBM(A=(3.45748e+17,'s^-1'), n=-1.25212, w0=(391.525,'kJ/mol'), E0=(211.611,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1846592434436917, var=16.77948271462324, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2C-inRing',), comment="""BM rule fitted to 12 training reactions at node Root_N-2C-inRing
    Total Standard Deviation in ln(k): 8.675917513936373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2C-inRing
Total Standard Deviation in ln(k): 8.675917513936373""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2C-inRing
Total Standard Deviation in ln(k): 8.675917513936373
""",
)

entry(
    index = 4,
    label = "Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = Arrhenius(A=(8.889e+11,'s^-1'), n=0.232, Ea=(122.75,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-2C-inRing_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.75708e+12,'s^-1'), n=0.345999, w0=(382.125,'kJ/mol'), E0=(181.165,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04576079032223387, var=17.727071816315462, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2C-inRing_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-2C-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 8.555619072122909"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 8.555619072122909""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 8.555619072122909
""",
)

entry(
    index = 6,
    label = "Root_N-2C-inRing_1C-inRing",
    kinetics = ArrheniusBM(A=(4.44736e+07,'s^-1'), n=1.49129, w0=(383.714,'kJ/mol'), E0=(193.132,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027547669081808165, var=16.593348419636637, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2C-inRing_1C-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_N-2C-inRing_1C-inRing
    Total Standard Deviation in ln(k): 8.235490340647598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2C-inRing_1C-inRing
Total Standard Deviation in ln(k): 8.235490340647598""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2C-inRing_1C-inRing
Total Standard Deviation in ln(k): 8.235490340647598
""",
)

entry(
    index = 7,
    label = "Root_N-2C-inRing_N-1C-inRing",
    kinetics = ArrheniusBM(A=(1.95134e+07,'s^-1'), n=1.79273, w0=(433.756,'kJ/mol'), E0=(199.509,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23977934772360482, var=108.52657903952432, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_N-1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_N-1C-inRing
    Total Standard Deviation in ln(k): 21.487007027148238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_N-1C-inRing
Total Standard Deviation in ln(k): 21.487007027148238""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_N-1C-inRing
Total Standard Deviation in ln(k): 21.487007027148238
""",
)

entry(
    index = 8,
    label = "Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(6.1205e+11,'s^-1'), n=0.578508, w0=(460.169,'kJ/mol'), E0=(180.091,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22848919410076524, var=54.94541948095504, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 15.43422780949594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 15.43422780949594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 15.43422780949594
""",
)

entry(
    index = 9,
    label = "Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(5.04408e+12,'s^-1'), n=0.113495, w0=(346,'kJ/mol'), E0=(182.274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13912340030690926, var=54.94667511828915, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 15.2098604334124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 15.2098604334124""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 15.2098604334124
""",
)

entry(
    index = 10,
    label = "Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.97261e+09,'s^-1'), n=1.14551, w0=(407.375,'kJ/mol'), E0=(194.274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1426124172105378, var=6.491897820154725, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 5.466227842354289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.466227842354289""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.466227842354289
""",
)

entry(
    index = 11,
    label = "Root_N-2C-inRing_1C-inRing_3C-inRing",
    kinetics = ArrheniusBM(A=(1.58519e+10,'s^-1'), n=0.904494, w0=(371.686,'kJ/mol'), E0=(194.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1288354106222728, var=6.491898261086161, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_1C-inRing_3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_3C-inRing
    Total Standard Deviation in ln(k): 5.431612421376553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_3C-inRing
Total Standard Deviation in ln(k): 5.431612421376553""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_3C-inRing
Total Standard Deviation in ln(k): 5.431612421376553
""",
)

entry(
    index = 12,
    label = "Root_N-2C-inRing_1C-inRing_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.40598e+07,'s^-1'), n=1.29727, w0=(372.082,'kJ/mol'), E0=(200.574,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2017904400447535, var=108.52685434044393, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_1C-inRing_N-3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_N-3C-inRing
    Total Standard Deviation in ln(k): 21.391583999413584"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 21.391583999413584""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 21.391583999413584
""",
)

