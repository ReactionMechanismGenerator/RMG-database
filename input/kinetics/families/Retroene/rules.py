#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.10012e+10,'s^-1'), n=0.352209, w0=(1.11205e+06,'J/mol'), E0=(162219,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0315482980354495, var=11.3165183829301, Tref=1000.0, N=67, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 67 training reactions at node Root
    Total Standard Deviation in ln(k): 6.823202550259767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 67 training reactions at node Root
Total Standard Deviation in ln(k): 6.823202550259767""",
    longDesc = 
"""
BM rule fitted to 67 training reactions at node Root
Total Standard Deviation in ln(k): 6.823202550259767
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(7.08414e+11,'s^-1'), n=-0.0384258, w0=(1.04926e+06,'J/mol'), E0=(173468,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0885800887239561, var=2.933633025269101, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 31 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 3.65624353954917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.65624353954917""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.65624353954917
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(2.51696e+11,'s^-1'), n=0.0936269, w0=(1.16612e+06,'J/mol'), E0=(153183,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03495653711814081, var=24.398290288554755, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 36 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 9.990144333888548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 9.990144333888548""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 9.990144333888548
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(5.60991e+11,'s^-1'), n=-0.0273666, w0=(1.0543e+06,'J/mol'), E0=(171027,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08769201295031893, var=2.499675655451367, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C',), comment="""BM rule fitted to 27 training reactions at node Root_1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 3.3898905398944907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 3.3898905398944907""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 3.3898905398944907
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.0937e+10,'s^-1'), n=0.830793, w0=(1.01525e+06,'J/mol'), E0=(222264,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.600131383473395, var=38.10179994091674, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 21.42011538066948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 21.42011538066948""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 21.42011538066948
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.59138e+06,'s^-1'), n=1.59388, w0=(1.17869e+06,'J/mol'), E0=(147231,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21962150556401386, var=2.9313754415001467, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.984171878119655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.984171878119655""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.984171878119655
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(9.54463e+09,'s^-1'), n=0.829688, w0=(1.0865e+06,'J/mol'), E0=(100226,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(6.16445e+10,'s^-1'), n=0.126877, w0=(1.1575e+06,'J/mol'), E0=(162948,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10956172353909022, var=13.764781872707946, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 7.71303207558061"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 7.71303207558061""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 7.71303207558061
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.50265e+10,'s^-1'), n=0.582016, w0=(1.0845e+06,'J/mol'), E0=(171532,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07578885385627057, var=2.175429915116852, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.147275918033949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.147275918033949""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.147275918033949
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_2R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(2.14192e+15,'s^-1'), n=-1.36604, w0=(968000,'J/mol'), E0=(168571,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07722342872883733, var=3.2717649671082105, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 3.820197694621681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.820197694621681""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.820197694621681
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.31421e+08,'s^-1'), n=0.798496, w0=(1.0845e+06,'J/mol'), E0=(166008,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06646347756542345, var=3.684389843138008, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 4.015035432311303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 4.015035432311303""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 4.015035432311303
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_N-2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.8e+12,'s^-1'), n=0, w0=(1.0665e+06,'J/mol'), E0=(218338,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_1R!H->C_N-2R!H->C_2NOS->S",
    kinetics = ArrheniusBM(A=(5.6608e+10,'s^-1'), n=0, w0=(953500,'J/mol'), E0=(119669,'J/mol'), Tmin=(588,'K'), Tmax=(691,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_2NOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S",
    kinetics = ArrheniusBM(A=(1.18273e+11,'s^-1'), n=-0.16585, w0=(1.0205e+06,'J/mol'), E0=(160293,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.001642907944431047, var=4.049121298193099, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
    Total Standard Deviation in ln(k): 4.03814174042697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 4.03814174042697""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 4.03814174042697
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.93151e+06,'s^-1'), n=1.81611, w0=(1.1055e+06,'J/mol'), E0=(159124,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(3.62979e+09,'s^-1'), n=0.813364, w0=(1.183e+06,'J/mol'), E0=(152248,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07834185115310821, var=3.1028790984589047, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 3.728177867462698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 3.728177867462698""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 3.728177867462698
""",
)

entry(
    index = 17,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.93725e+10,'s^-1'), n=-0.00164902, w0=(1.0245e+06,'J/mol'), E0=(139223,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010065863716581231, var=81.8360764684643, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing
    Total Standard Deviation in ln(k): 18.160785079462567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing
Total Standard Deviation in ln(k): 18.160785079462567""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing
Total Standard Deviation in ln(k): 18.160785079462567
""",
)

entry(
    index = 18,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(5.0377e+09,'s^-1'), n=0.503998, w0=(1.17523e+06,'J/mol'), E0=(165380,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07023301752382041, var=14.693850144505003, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing
    Total Standard Deviation in ln(k): 7.861127261438902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.861127261438902""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.861127261438902
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.06632e+07,'s^-1'), n=1.54494, w0=(1.0845e+06,'J/mol'), E0=(175232,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03160873187820852, var=1.3512789532393483, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
    Total Standard Deviation in ln(k): 2.409813687361464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.409813687361464""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.409813687361464
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(2.11272e+10,'s^-1'), n=0.508892, w0=(1.0845e+06,'J/mol'), E0=(165988,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05946298457203635, var=2.1502413853175404, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
    Total Standard Deviation in ln(k): 3.0890881384700166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 3.0890881384700166""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 3.0890881384700166
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.48935e+16,'s^-1'), n=-1.81548, w0=(968000,'J/mol'), E0=(163551,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10791093733813462, var=3.878221135229738, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.21909782627248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.21909782627248""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.21909782627248
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.23333e+11,'s^-1'), n=0, w0=(968000,'J/mol'), E0=(182946,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.01606e+09,'s^-1'), n=0.528417, w0=(1.0845e+06,'J/mol'), E0=(162089,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0004170773678849364, var=7.571252332200875, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 5.517258674761662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.517258674761662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.517258674761662
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.72448e+06,'s^-1'), n=1.38418, w0=(1.0845e+06,'J/mol'), E0=(169437,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.023226627232403933, var=4.996815442657889, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.539654493299976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.539654493299976""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.539654493299976
""",
)

entry(
    index = 25,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N",
    kinetics = ArrheniusBM(A=(7.8141e+10,'s^-1'), n=0, w0=(974500,'J/mol'), E0=(160561,'J/mol'), Tmin=(602,'K'), Tmax=(694,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N",
    kinetics = ArrheniusBM(A=(4.1009e+10,'s^-1'), n=0, w0=(1.0665e+06,'J/mol'), E0=(167048,'J/mol'), Tmin=(725,'K'), Tmax=(810,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.585e+08,'s^-1'), n=1.03057, w0=(1.183e+06,'J/mol'), E0=(137902,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9849605138850569, var=2.175969446453559, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.431993466301682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.431993466301682""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.431993466301682
""",
)

entry(
    index = 28,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C",
    kinetics = ArrheniusBM(A=(2.72971e+09,'s^-1'), n=0.858007, w0=(1.183e+06,'J/mol'), E0=(158565,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09327428286217945, var=0.3885302816570969, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C
    Total Standard Deviation in ln(k): 1.4839529178212068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C
Total Standard Deviation in ln(k): 1.4839529178212068""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C
Total Standard Deviation in ln(k): 1.4839529178212068
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.63512e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(94204,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(550000,'s^-1'), n=0.9, w0=(1.0245e+06,'J/mol'), E0=(131295,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.97792e+06,'s^-1'), n=1.65745, w0=(1.183e+06,'J/mol'), E0=(173053,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.015698585890881855, var=0.33104774169034074, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.192903060789605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.192903060789605""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.192903060789605
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.86778e+11,'s^-1'), n=-0.20998, w0=(1.183e+06,'J/mol'), E0=(161018,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007000260714869858, var=47.42592109938536, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 13.82349346766583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.82349346766583""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.82349346766583
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C",
    kinetics = ArrheniusBM(A=(3.33333e+07,'s^-1'), n=1.2, w0=(1.0665e+06,'J/mol'), E0=(165825,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.96667e+10,'s^-1'), n=0.59, w0=(1.183e+06,'J/mol'), E0=(179850,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.17483e+06,'s^-1'), n=1.66626, w0=(1.0845e+06,'J/mol'), E0=(184882,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014692611028300074, var=6.989117524371048, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 5.336822036500276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.336822036500276""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.336822036500276
""",
)

entry(
    index = 36,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(8.9437e+07,'s^-1'), n=1.20317, w0=(1.0845e+06,'J/mol'), E0=(168361,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.289085629588869e-05, var=0.0032978926118627083, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 0.11523425074443258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.11523425074443258""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.11523425074443258
""",
)

entry(
    index = 37,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.26489e+09,'s^-1'), n=0.721231, w0=(1.0845e+06,'J/mol'), E0=(173168,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05463853673654339, var=3.498019671653633, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.8867374747822776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.8867374747822776""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.8867374747822776
""",
)

entry(
    index = 38,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.63884e+10,'s^-1'), n=0.553788, w0=(1.0845e+06,'J/mol'), E0=(159149,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0054573965212036946, var=1.5050092139275335, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 2.4730973283903155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.4730973283903155""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.4730973283903155
""",
)

entry(
    index = 39,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(11.5839,'s^-1'), n=3.09547, w0=(1.0845e+06,'J/mol'), E0=(137668,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(1.2535e+06,'s^-1'), n=1.80968, w0=(1.0845e+06,'J/mol'), E0=(155867,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.47918e+17,'s^-1'), n=-2.02819, w0=(968000,'J/mol'), E0=(156988,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11215013592975923, var=3.0170948703094664, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 3.763966312410604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.763966312410604""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.763966312410604
""",
)

entry(
    index = 42,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(21.2645,'s^-1'), n=2.97303, w0=(1.0845e+06,'J/mol'), E0=(146892,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.78363e+11,'s^-1'), n=0.169307, w0=(1.0845e+06,'J/mol'), E0=(166826,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.80655,'s^-1'), n=3.07798, w0=(1.0845e+06,'J/mol'), E0=(150022,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2419.21,'s^-1'), n=2.3826, w0=(1.0845e+06,'J/mol'), E0=(172708,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->C_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.45626e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(142579,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.47446e+08,'s^-1'), n=1.09592, w0=(1.183e+06,'J/mol'), E0=(138292,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9397855924827363, var=2.0052075611816607, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 5.200082488575585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.200082488575585""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.200082488575585
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(4.72256e+08,'s^-1'), n=1.05476, w0=(1.183e+06,'J/mol'), E0=(153718,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8089351856699499, var=2.4771942159743126, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 5.187774025217704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 5.187774025217704""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 5.187774025217704
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.77656e+09,'s^-1'), n=0.762969, w0=(1.183e+06,'J/mol'), E0=(163796,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1381107593472458, var=0.05384276569539632, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.8121915671689098"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8121915671689098""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8121915671689098
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.32388e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(156130,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.55471e+06,'s^-1'), n=1.74582, w0=(1.183e+06,'J/mol'), E0=(172104,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06042635539233208, var=0.15875309730657372, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 0.9505882960246963"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.9505882960246963""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.9505882960246963
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(9.41708e+14,'s^-1'), n=-0.896351, w0=(1.183e+06,'J/mol'), E0=(201255,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.3172441301014085e-15, var=0.04558127893527205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 0.4280063799185306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.4280063799185306""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.4280063799185306
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.7237e+13,'s^-1'), n=-0.218608, w0=(1.183e+06,'J/mol'), E0=(173278,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008485639854909011, var=0.595884305542138, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 1.5688467338498606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5688467338498606""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5688467338498606
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(58002.5,'s^-1'), n=0.286, w0=(1.183e+06,'J/mol'), E0=(125149,'J/mol'), Tmin=(500,'K'), Tmax=(1300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1708.21,'s^-1'), n=2.62955, w0=(1.0845e+06,'J/mol'), E0=(162976,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(85500.5,'s^-1'), n=2.19797, w0=(1.0845e+06,'J/mol'), E0=(186561,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(111514,'s^-1'), n=2.05353, w0=(1.0845e+06,'J/mol'), E0=(161295,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.3077e+06,'s^-1'), n=1.41637, w0=(1.0845e+06,'J/mol'), E0=(158519,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(4.85194e+07,'s^-1'), n=1.12718, w0=(1.0845e+06,'J/mol'), E0=(163383,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.023199101818381307, var=14.082287951603485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 7.581333161482922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 7.581333161482922""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 7.581333161482922
""",
)

entry(
    index = 60,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(1.86934e+11,'s^-1'), n=0.401442, w0=(1.0845e+06,'J/mol'), E0=(182171,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.021492990850914453, var=5.303057773824753, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 4.670580394351897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 4.670580394351897""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 4.670580394351897
""",
)

entry(
    index = 61,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.37571e+07,'s^-1'), n=1.37128, w0=(1.0845e+06,'J/mol'), E0=(152318,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0072034781886713035, var=1.112822940211039, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.1329027100545948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1329027100545948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1329027100545948
""",
)

entry(
    index = 62,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.35624e+13,'s^-1'), n=-0.218688, w0=(1.0845e+06,'J/mol'), E0=(165536,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00045559036986736554, var=2.308582681294396, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 3.0471433462500226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.0471433462500226""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.0471433462500226
""",
)

entry(
    index = 63,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.2474e+17,'s^-1'), n=-2.18683, w0=(968000,'J/mol'), E0=(148502,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10639571125003566, var=4.305704753171537, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 4.427189719338195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.427189719338195""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.427189719338195
""",
)

entry(
    index = 64,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.39881e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(136330,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.16921e+13,'s^-1'), n=-0.324602, w0=(1.183e+06,'J/mol'), E0=(155605,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0006121978434024415, var=0.049410262461096775, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.4471591044090268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.4471591044090268""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.4471591044090268
""",
)

entry(
    index = 66,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.81965e+13,'s^-1'), n=-0.54761, w0=(1.183e+06,'J/mol'), E0=(142581,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.011656401367828983, var=1.7600602599389328, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.6889145927230276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.6889145927230276""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.6889145927230276
""",
)

entry(
    index = 67,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.09597e+13,'s^-1'), n=-0.328822, w0=(1.183e+06,'J/mol'), E0=(160198,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0010628098785811556, var=0.16224599752348345, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.8101730807390738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8101730807390738""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8101730807390738
""",
)

entry(
    index = 68,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(165471,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.99592e+06,'s^-1'), n=1.77995, w0=(1.183e+06,'J/mol'), E0=(172186,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.045572513486908654, var=0.10435748944687856, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
    Total Standard Deviation in ln(k): 0.7621216381393935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.7621216381393935""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.7621216381393935
""",
)

entry(
    index = 70,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(193178,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(1.49982e+12,'s^-1'), n=0.105014, w0=(1.183e+06,'J/mol'), E0=(171575,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6694644050553874e-15, var=2.116729755416145, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 2.9166861328622327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.9166861328622327""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.9166861328622327
""",
)

entry(
    index = 72,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N",
    kinetics = ArrheniusBM(A=(6552.1,'s^-1'), n=2.29082, w0=(1.0845e+06,'J/mol'), E0=(167773,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N",
    kinetics = ArrheniusBM(A=(459.236,'s^-1'), n=2.68918, w0=(1.0845e+06,'J/mol'), E0=(145855,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N",
    kinetics = ArrheniusBM(A=(2.87851e+08,'s^-1'), n=1.30992, w0=(1.0845e+06,'J/mol'), E0=(187582,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N",
    kinetics = ArrheniusBM(A=(6.1395e+07,'s^-1'), n=1.36832, w0=(1.0845e+06,'J/mol'), E0=(163924,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(1017.11,'s^-1'), n=2.55399, w0=(1.0845e+06,'J/mol'), E0=(143955,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(1.65185e+07,'s^-1'), n=1.51788, w0=(1.0845e+06,'J/mol'), E0=(159604,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(2.0173e+12,'s^-1'), n=0.0499164, w0=(1.0845e+06,'J/mol'), E0=(160428,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(8.27867e+08,'s^-1'), n=1.04991, w0=(1.0845e+06,'J/mol'), E0=(162025,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.29826e+14,'s^-1'), n=-1.58523, w0=(968000,'J/mol'), E0=(118901,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0013608568101268583, var=1.6674726433047609, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.5921468035711666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.5921468035711666""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.5921468035711666
""",
)

entry(
    index = 81,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing",
    kinetics = ArrheniusBM(A=(1.25594e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(155092,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.98582e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(160232,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.32702e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(116943,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.37297e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(151179,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(3.61437e+13,'s^-1'), n=-0.487071, w0=(1.183e+06,'J/mol'), E0=(151204,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.255606157999161e-05, var=0.017017844750293856, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.2616044249499389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2616044249499389""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2616044249499389
""",
)

entry(
    index = 86,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(1.11936e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(158970,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(1.99054e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(166153,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R",
    kinetics = ArrheniusBM(A=(85171.3,'s^-1'), n=2.12989, w0=(1.183e+06,'J/mol'), E0=(165322,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6638418747586526, var=1.1683510553150969, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
    Total Standard Deviation in ln(k): 3.8348683456525428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.8348683456525428""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.8348683456525428
""",
)

entry(
    index = 89,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.16053e+06,'s^-1'), n=1.87467, w0=(1.183e+06,'J/mol'), E0=(182477,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(6.96433e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(174127,'J/mol'), Tmin=(900,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(6.5e+10,'s^-1'), n=0, w0=(968000,'J/mol'), E0=(139431,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->C_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing",
    kinetics = ArrheniusBM(A=(1.32702e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(152192,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.32702e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(151418,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_Ext-2R!H-R_N-1BrClFINOPSSi->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.94328e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(172170,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(170162,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(168938,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->N_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

