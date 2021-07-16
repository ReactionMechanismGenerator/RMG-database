#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = ""
longDesc = """
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.63228e+07,'m^3/(mol*s)'), n=-0.0359247, w0=(166874,'J/mol'), E0=(-2398.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.059288395344936656, var=8.188637331114286, Tref=1000.0, N=231, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 231 training reactions at node Root
    Total Standard Deviation in ln(k): 5.885674651581886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 231 training reactions at node Root
Total Standard Deviation in ln(k): 5.885674651581886""",
    longDesc = 
"""
BM rule fitted to 231 training reactions at node Root
Total Standard Deviation in ln(k): 5.885674651581886
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(9.84084e+08,'m^3/(mol*s)'), n=-0.49351, w0=(191027,'J/mol'), E0=(19102.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21294516634903593, var=17.563460782102336, Tref=1000.0, N=94, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 94 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 8.936638805228199"""),
    rank = 11,
    shortDesc = """BM rule fitted to 94 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 8.936638805228199""",
    longDesc = 
"""
BM rule fitted to 94 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 8.936638805228199
""",
)

entry(
    index = 3,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(5.7056e+06,'m^3/(mol*s)'), n=0.157279, w0=(150303,'J/mol'), E0=(-1669.05,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.060824672931554545, var=5.167572430271839, Tref=1000.0, N=137, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 137 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 4.710048760134311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 137 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.710048760134311""",
    longDesc = 
"""
BM rule fitted to 137 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.710048760134311
""",
)

entry(
    index = 4,
    label = "Root_1R->H_2R->S",
    kinetics = ArrheniusBM(A=(1.01224e+07,'m^3/(mol*s)'), n=0.564397, w0=(181667,'J/mol'), E0=(18166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.2992478270622168, var=17.016792941748268, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_2R->S',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
    Total Standard Deviation in ln(k): 14.046820587721712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 14.046820587721712""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 14.046820587721712
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-2R->S",
    kinetics = ArrheniusBM(A=(4.63676e+09,'m^3/(mol*s)'), n=-0.851786, w0=(191335,'J/mol'), E0=(19133.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22729418165192433, var=18.82841863799078, Tref=1000.0, N=91, data_mean=0.0, correlation='Root_1R->H_N-2R->S',), comment="""BM rule fitted to 91 training reactions at node Root_1R->H_N-2R->S
    Total Standard Deviation in ln(k): 9.269982377187164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 91 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 9.269982377187164""",
    longDesc = 
"""
BM rule fitted to 91 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 9.269982377187164
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(104582,'m^3/(mol*s)'), n=0.846757, w0=(77730.8,'J/mol'), E0=(49762.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5297377864040611, var=8.98842065611257, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
    Total Standard Deviation in ln(k): 7.341334530798696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 7.341334530798696""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 7.341334530798696
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(707024,'m^3/(mol*s)'), n=0.435051, w0=(157911,'J/mol'), E0=(1576.52,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03811698323926548, var=4.728692220187523, Tref=1000.0, N=124, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N',), comment="""BM rule fitted to 124 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
    Total Standard Deviation in ln(k): 4.455179278730624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 124 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 4.455179278730624""",
    longDesc = 
"""
BM rule fitted to 124 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 4.455179278730624
""",
)

entry(
    index = 8,
    label = "Root_1R->H_2R->S_Ext-2S-R",
    kinetics = ArrheniusBM(A=(6.94752e+06,'m^3/(mol*s)'), n=1.02083, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_2R->S_Ext-2S-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing",
    kinetics = ArrheniusBM(A=(1.73764e+07,'m^3/(mol*s)'), n=0.123265, w0=(212091,'J/mol'), E0=(21209.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10067081692156987, var=4.813044730771074, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing',), comment="""BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing
    Total Standard Deviation in ln(k): 4.651060370806105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing
Total Standard Deviation in ln(k): 4.651060370806105""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing
Total Standard Deviation in ln(k): 4.651060370806105
""",
)

entry(
    index = 10,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing",
    kinetics = ArrheniusBM(A=(1.63169e+10,'m^3/(mol*s)'), n=-1.07138, w0=(188481,'J/mol'), E0=(18848.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4069695143513474, var=23.859444744355812, Tref=1000.0, N=80, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing',), comment="""BM rule fitted to 80 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing
    Total Standard Deviation in ln(k): 10.814891608777451"""),
    rank = 11,
    shortDesc = """BM rule fitted to 80 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing
Total Standard Deviation in ln(k): 10.814891608777451""",
    longDesc = 
"""
BM rule fitted to 80 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing
Total Standard Deviation in ln(k): 10.814891608777451
""",
)

entry(
    index = 11,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R",
    kinetics = ArrheniusBM(A=(198329,'m^3/(mol*s)'), n=1.03085, w0=(77250,'J/mol'), E0=(40939.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1400932990632578, var=31.198540567979997, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
    Total Standard Deviation in ln(k): 11.549572049786793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 11.549572049786793""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 11.549572049786793
""",
)

entry(
    index = 12,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(6.8848e+06,'m^3/(mol*s)'), n=0.139797, w0=(77250,'J/mol'), E0=(7725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.053315102751840954, var=1.9676215119596228, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
    Total Standard Deviation in ln(k): 2.946038184336049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.946038184336049""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.946038184336049
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S",
    kinetics = ArrheniusBM(A=(145833,'m^3/(mol*s)'), n=0.753606, w0=(145250,'J/mol'), E0=(5064.83,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013816789269955642, var=4.406776321910686, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S
    Total Standard Deviation in ln(k): 4.243120212979136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S
Total Standard Deviation in ln(k): 4.243120212979136""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S
Total Standard Deviation in ln(k): 4.243120212979136
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S",
    kinetics = ArrheniusBM(A=(2.85567e+07,'m^3/(mol*s)'), n=-0.308813, w0=(158784,'J/mol'), E0=(15878.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023009862151364042, var=3.8449690133714793, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S',), comment="""BM rule fitted to 116 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S
    Total Standard Deviation in ln(k): 3.9888170520051145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S
Total Standard Deviation in ln(k): 3.9888170520051145""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S
Total Standard Deviation in ln(k): 3.9888170520051145
""",
)

entry(
    index = 15,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(6.68844e+06,'m^3/(mol*s)'), n=0.105537, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3705566296084406, var=9.640462010212294, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 7.155567474279537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 7.155567474279537""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 7.155567474279537
""",
)

entry(
    index = 16,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(4.63064e+07,'m^3/(mol*s)'), n=0.141464, w0=(207400,'J/mol'), E0=(20740,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00871465232674572, var=0.8676704064877683, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 1.8892833304748036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.8892833304748036""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.8892833304748036
""",
)

entry(
    index = 17,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O",
    kinetics = ArrheniusBM(A=(4.55088e+06,'m^3/(mol*s)'), n=0.286905, w0=(107250,'J/mol'), E0=(10725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1312290136565373, var=5.629142580175238, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O
    Total Standard Deviation in ln(k): 7.5986811444942175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O
Total Standard Deviation in ln(k): 7.5986811444942175""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O
Total Standard Deviation in ln(k): 7.5986811444942175
""",
)

entry(
    index = 18,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O",
    kinetics = ArrheniusBM(A=(2.49133e+10,'m^3/(mol*s)'), n=-1.14161, w0=(192757,'J/mol'), E0=(19275.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.47464082266338253, var=25.743159942883494, Tref=1000.0, N=76, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O',), comment="""BM rule fitted to 76 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O
    Total Standard Deviation in ln(k): 11.364133116917897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 76 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O
Total Standard Deviation in ln(k): 11.364133116917897""",
    longDesc = 
"""
BM rule fitted to 76 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O
Total Standard Deviation in ln(k): 11.364133116917897
""",
)

entry(
    index = 19,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0",
    kinetics = ArrheniusBM(A=(1.00575e+30,'m^3/(mol*s)'), n=-7.13103, w0=(79333.3,'J/mol'), E0=(7933.33,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3449650629055383, var=32.90236135536008, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
    Total Standard Deviation in ln(k): 12.366023063582485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 12.366023063582485""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 12.366023063582485
""",
)

entry(
    index = 20,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0",
    kinetics = ArrheniusBM(A=(8.07906e+128,'m^3/(mol*s)'), n=-37.2678, w0=(71000,'J/mol'), E0=(272267,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.121789619228202, var=143.15315703134127, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
    Total Standard Deviation in ln(k): 29.31710899420356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 29.31710899420356""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 29.31710899420356
""",
)

entry(
    index = 21,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.10796e+07,'m^3/(mol*s)'), n=0.0974081, w0=(75166.7,'J/mol'), E0=(7516.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1078476173045317, var=4.129322638654681, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
    Total Standard Deviation in ln(k): 6.857305717290992"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 6.857305717290992""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 6.857305717290992
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S",
    kinetics = ArrheniusBM(A=(1.74988e+07,'m^3/(mol*s)'), n=0.493661, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.478850108957965, var=26.3269780808117, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S
    Total Standard Deviation in ln(k): 19.027089367324724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S
Total Standard Deviation in ln(k): 19.027089367324724""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S
Total Standard Deviation in ln(k): 19.027089367324724
""",
)

entry(
    index = 23,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S",
    kinetics = ArrheniusBM(A=(50703.9,'m^3/(mol*s)'), n=0.81198, w0=(156000,'J/mol'), E0=(1098.62,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0037020196255218908, var=1.1376836120834068, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S
    Total Standard Deviation in ln(k): 2.147597148225215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S
Total Standard Deviation in ln(k): 2.147597148225215""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S
Total Standard Deviation in ln(k): 2.147597148225215
""",
)

entry(
    index = 24,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br",
    kinetics = ArrheniusBM(A=(3899.18,'m^3/(mol*s)'), n=0.861126, w0=(126200,'J/mol'), E0=(12620,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02543844309653931, var=13.50470408409468, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br
    Total Standard Deviation in ln(k): 7.431065908671619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br
Total Standard Deviation in ln(k): 7.431065908671619""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br
Total Standard Deviation in ln(k): 7.431065908671619
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br",
    kinetics = ArrheniusBM(A=(2.91699e+07,'m^3/(mol*s)'), n=-0.311606, w0=(160252,'J/mol'), E0=(16025.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023165845054413613, var=3.8369195750992167, Tref=1000.0, N=111, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br',), comment="""BM rule fitted to 111 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br
    Total Standard Deviation in ln(k): 3.985092037514054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 111 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br
Total Standard Deviation in ln(k): 3.985092037514054""",
    longDesc = 
"""
BM rule fitted to 111 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br
Total Standard Deviation in ln(k): 3.985092037514054
""",
)

entry(
    index = 26,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.4769e+06,'m^3/(mol*s)'), n=-0.220906, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04719635125001107, var=0.22911507772565162, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.0781696235914124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0781696235914124""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0781696235914124
""",
)

entry(
    index = 27,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(4.4197e+06,'m^3/(mol*s)'), n=0.173431, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1097017345178382, var=0.8159359144189625, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing
    Total Standard Deviation in ln(k): 2.086493076125835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing
Total Standard Deviation in ln(k): 2.086493076125835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing
Total Standard Deviation in ln(k): 2.086493076125835
""",
)

entry(
    index = 28,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(9.42e+06,'m^3/(mol*s)'), n=0.408, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.02093e+07,'m^3/(mol*s)'), n=0.125846, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.47660747185827573, var=1.386468955460086, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.5580500164857103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.5580500164857103""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.5580500164857103
""",
)

entry(
    index = 30,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.22915e+07,'m^3/(mol*s)'), n=0.181361, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1489920501984019, var=0.10041008290210698, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.0096033162086009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009
""",
)

entry(
    index = 31,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R",
    kinetics = ArrheniusBM(A=(2.72122e+06,'m^3/(mol*s)'), n=0.322102, w0=(119333,'J/mol'), E0=(11933.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8374914607595294, var=1.6498954069319867, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R
    Total Standard Deviation in ln(k): 4.679297114514701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R
Total Standard Deviation in ln(k): 4.679297114514701""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R
Total Standard Deviation in ln(k): 4.679297114514701
""",
)

entry(
    index = 32,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_2CHN->N",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0.493, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(200,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_2CHN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_2CHN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_2CHN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_2CHN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N",
    kinetics = ArrheniusBM(A=(3.51764e+10,'m^3/(mol*s)'), n=-1.20682, w0=(194213,'J/mol'), E0=(19421.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5552373463401862, var=27.510774799494566, Tref=1000.0, N=75, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N',), comment="""BM rule fitted to 75 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N
    Total Standard Deviation in ln(k): 11.910047482904101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 75 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N
Total Standard Deviation in ln(k): 11.910047482904101""",
    longDesc = 
"""
BM rule fitted to 75 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N
Total Standard Deviation in ln(k): 11.910047482904101
""",
)

entry(
    index = 34,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C",
    kinetics = ArrheniusBM(A=(505,'m^3/(mol*s)'), n=0, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(2000,'K'), Tmax=(4000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C",
    kinetics = ArrheniusBM(A=(2.85423e+08,'m^3/(mol*s)'), n=-0.30578, w0=(78500,'J/mol'), E0=(7850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06262066178409414, var=1.5701960652574938, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
    Total Standard Deviation in ln(k): 2.669421041068438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 2.669421041068438""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 2.669421041068438
""",
)

entry(
    index = 36,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R",
    kinetics = ArrheniusBM(A=(58500,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(473,'K'), Tmax=(703,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C",
    kinetics = ArrheniusBM(A=(1.45488e+12,'m^3/(mol*s)'), n=-1.37297, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4709502203626317, var=0.4813240235668652, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
    Total Standard Deviation in ln(k): 2.5741274836274104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.5741274836274104""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.5741274836274104
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S_Ext-1S-R",
    kinetics = ArrheniusBM(A=(106000,'m^3/(mol*s)'), n=1.21, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S_Ext-1S-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S_Ext-1S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_2R->S_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R",
    kinetics = ArrheniusBM(A=(69181.1,'m^3/(mol*s)'), n=0.764865, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03639418016190122, var=1.0362331955515207, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R
    Total Standard Deviation in ln(k): 2.1321735605013337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R
Total Standard Deviation in ln(k): 2.1321735605013337""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R
Total Standard Deviation in ln(k): 2.1321735605013337
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R",
    kinetics = ArrheniusBM(A=(15562.8,'m^3/(mol*s)'), n=0.752576, w0=(134000,'J/mol'), E0=(13400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.044412336976029074, var=15.953498382267611, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R
    Total Standard Deviation in ln(k): 8.118867688719185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R
Total Standard Deviation in ln(k): 8.118867688719185""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R
Total Standard Deviation in ln(k): 8.118867688719185
""",
)

entry(
    index = 42,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(2.46361e+07,'m^3/(mol*s)'), n=-0.301707, w0=(161682,'J/mol'), E0=(16168.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.024370465007777047, var=3.8273008080874726, Tref=1000.0, N=107, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R',), comment="""BM rule fitted to 107 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R
    Total Standard Deviation in ln(k): 3.98319347976726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 107 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R
Total Standard Deviation in ln(k): 3.98319347976726""",
    longDesc = 
"""
BM rule fitted to 107 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R
Total Standard Deviation in ln(k): 3.98319347976726
""",
)

entry(
    index = 43,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C",
    kinetics = ArrheniusBM(A=(7.39762e+08,'m^3/(mol*s)'), n=-0.50372, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2591908809794792, var=0.33015705878329676, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C
    Total Standard Deviation in ln(k): 1.8031400124190624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C
Total Standard Deviation in ln(k): 1.8031400124190624""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C
Total Standard Deviation in ln(k): 1.8031400124190624
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_N-1CFO->C",
    kinetics = ArrheniusBM(A=(1.57e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_N-1CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_N-1CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.03082e+09,'m^3/(mol*s)'), n=-1.0508, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.68977e+06,'m^3/(mol*s)'), n=-0.120159, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8040217460360854, var=0.956881531786605, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 3.9811934407228455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 3.9811934407228455""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 3.9811934407228455
""",
)

entry(
    index = 47,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(249317,'m^3/(mol*s)'), n=0.611, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-2BrCFHNO-R",
    kinetics = ArrheniusBM(A=(6.44369e+06,'m^3/(mol*s)'), n=0.245, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-2BrCFHNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-2BrCFHNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-2BrCFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-2BrCFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCFHNO",
    kinetics = ArrheniusBM(A=(3.62e+07,'m^3/(mol*s)'), n=0.228, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCFHNO",
    kinetics = ArrheniusBM(A=(2.2e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1200,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_3R!H-inRing",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.61215e+06,'m^3/(mol*s)'), n=0.325758, w0=(143500,'J/mol'), E0=(14350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.573841544937113, var=0.5984327916266005, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing
    Total Standard Deviation in ln(k): 2.992644667134224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 2.992644667134224""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 2.992644667134224
""",
)

entry(
    index = 53,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R",
    kinetics = ArrheniusBM(A=(3.77918e+10,'m^3/(mol*s)'), n=-1.22055, w0=(194197,'J/mol'), E0=(19419.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5757459570375505, var=27.917547216805943, Tref=1000.0, N=71, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R',), comment="""BM rule fitted to 71 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R
    Total Standard Deviation in ln(k): 12.039028282638078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 71 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R
Total Standard Deviation in ln(k): 12.039028282638078""",
    longDesc = 
"""
BM rule fitted to 71 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R
Total Standard Deviation in ln(k): 12.039028282638078
""",
)

entry(
    index = 54,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_2CH->C",
    kinetics = ArrheniusBM(A=(5.37e+07,'m^3/(mol*s)'), n=0.15395, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0638883423777328, var=3.290805964782287, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_2CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_2CH->C
    Total Standard Deviation in ln(k): 6.309791736806655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_2CH->C
Total Standard Deviation in ln(k): 6.309791736806655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_2CH->C
Total Standard Deviation in ln(k): 6.309791736806655
""",
)

entry(
    index = 55,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_N-2CH->C",
    kinetics = ArrheniusBM(A=(30255.8,'m^3/(mol*s)'), n=0.454367, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3774142242586176, var=47.94959741791935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_N-2CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_N-2CH->C
    Total Standard Deviation in ln(k): 14.830194859219086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_N-2CH->C
Total Standard Deviation in ln(k): 14.830194859219086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_N-2CH->C
Total Standard Deviation in ln(k): 14.830194859219086
""",
)

entry(
    index = 56,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R",
    kinetics = ArrheniusBM(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(600,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N",
    kinetics = ArrheniusBM(A=(122000,'m^3/(mol*s)'), n=0.2, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N",
    kinetics = ArrheniusBM(A=(2.98483e+08,'m^3/(mol*s)'), n=-0.304134, w0=(79333.3,'J/mol'), E0=(7933.33,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009765358261953589, var=1.0633988791636333, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N
    Total Standard Deviation in ln(k): 2.091843615577922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N
Total Standard Deviation in ln(k): 2.091843615577922""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N
Total Standard Deviation in ln(k): 2.091843615577922
""",
)

entry(
    index = 59,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04415470256864107, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C
    Total Standard Deviation in ln(k): 0.11094146374030418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C
Total Standard Deviation in ln(k): 0.11094146374030418""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C
Total Standard Deviation in ln(k): 0.11094146374030418
""",
)

entry(
    index = 60,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(129687,'m^3/(mol*s)'), n=0.801692, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3723820346018363, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C
    Total Standard Deviation in ln(k): 0.9356332527684328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.83961e-10,'m^3/(mol*s)'), n=4.9034, w0=(95000,'J/mol'), E0=(9500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(6.84618,'m^3/(mol*s)'), n=1.32431, w0=(95000,'J/mol'), E0=(9500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F",
    kinetics = ArrheniusBM(A=(2.9712e+10,'m^3/(mol*s)'), n=-1.45978, w0=(168225,'J/mol'), E0=(16822.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06570190399627691, var=7.733717204167451, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F
    Total Standard Deviation in ln(k): 5.740160537976879"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F
Total Standard Deviation in ln(k): 5.740160537976879""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F
Total Standard Deviation in ln(k): 5.740160537976879
""",
)

entry(
    index = 66,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(5.30286e+06,'m^3/(mol*s)'), n=-0.0510047, w0=(160178,'J/mol'), E0=(16017.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06349078738448034, var=3.245843107836522, Tref=1000.0, N=87, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F',), comment="""BM rule fitted to 87 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F
    Total Standard Deviation in ln(k): 3.7713001214806385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 87 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.7713001214806385""",
    longDesc = 
"""
BM rule fitted to 87 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.7713001214806385
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_2R->C",
    kinetics = ArrheniusBM(A=(7.57968e+08,'m^3/(mol*s)'), n=-0.508605, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.700128153501157, var=0.7225535388437543, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_2R->C
    Total Standard Deviation in ln(k): 3.4632039141850433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_2R->C
Total Standard Deviation in ln(k): 3.4632039141850433""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_2R->C
Total Standard Deviation in ln(k): 3.4632039141850433
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_N-2R->C",
    kinetics = ArrheniusBM(A=(6.03e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_1CFO->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.54095e+09,'m^3/(mol*s)'), n=-1.00262, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCFHNO-inRing_Ext-2BrCFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_3R!H->C",
    kinetics = ArrheniusBM(A=(700000,'m^3/(mol*s)'), n=0.493, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_N-3R!H->C",
    kinetics = ArrheniusBM(A=(43950,'m^3/(mol*s)'), n=1, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(298,'K'), Tmax=(6000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_N-3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_N-3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_N-3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_2BrCFHNO->O_Ext-2O-R_N-3R!H-inRing_N-3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F",
    kinetics = ArrheniusBM(A=(2.86537e+16,'m^3/(mol*s)'), n=-3.90272, w0=(195360,'J/mol'), E0=(19536,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19995276804646034, var=36.20235316807103, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F',), comment="""BM rule fitted to 25 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F
    Total Standard Deviation in ln(k): 12.564562357137442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F
Total Standard Deviation in ln(k): 12.564562357137442""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F
Total Standard Deviation in ln(k): 12.564562357137442
""",
)

entry(
    index = 73,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(8.70966e+08,'m^3/(mol*s)'), n=-0.473625, w0=(193565,'J/mol'), E0=(19356.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2914552671219465, var=13.778918611018765, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F',), comment="""BM rule fitted to 46 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F
    Total Standard Deviation in ln(k): 8.173869417522152"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F
Total Standard Deviation in ln(k): 8.173869417522152""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F
Total Standard Deviation in ln(k): 8.173869417522152
""",
)

entry(
    index = 74,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.59771e+09,'m^3/(mol*s)'), n=-0.461068, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N",
    kinetics = ArrheniusBM(A=(5.02e+08,'m^3/(mol*s)'), n=-0.429, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(400,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(1900,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6642490346951677, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R
    Total Standard Deviation in ln(k): 1.6689674238572052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 1.6689674238572052""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 1.6689674238572052
""",
)

entry(
    index = 78,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R",
    kinetics = ArrheniusBM(A=(3940,'m^3/(mol*s)'), n=1.25, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.56988e+07,'m^3/(mol*s)'), n=-0.434435, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09907769705779038, var=11.50723402156175, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R
    Total Standard Deviation in ln(k): 7.049464259995176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 7.049464259995176""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 7.049464259995176
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C",
    kinetics = ArrheniusBM(A=(2.94908e+18,'m^3/(mol*s)'), n=-4.3177, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005409242555914756, var=4.51750936705488, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C
    Total Standard Deviation in ln(k): 4.2745418688578605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C
Total Standard Deviation in ln(k): 4.2745418688578605""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C
Total Standard Deviation in ln(k): 4.2745418688578605
""",
)

entry(
    index = 81,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_N-2R->C",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=6.37888e-08, w0=(125250,'J/mol'), E0=(12525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_N-2R->C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_N-2R->C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_N-2R->C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 82,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1",
    kinetics = ArrheniusBM(A=(105110,'m^3/(mol*s)'), n=0.349549, w0=(156895,'J/mol'), E0=(15689.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0119415375080056, var=2.701036920785913, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1
    Total Standard Deviation in ln(k): 3.3247522174269615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 3.3247522174269615""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 3.3247522174269615
""",
)

entry(
    index = 83,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1",
    kinetics = ArrheniusBM(A=(4.82592e+08,'m^3/(mol*s)'), n=-0.511824, w0=(161096,'J/mol'), E0=(16109.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009282617848909087, var=0.7620712029808074, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1
    Total Standard Deviation in ln(k): 1.7733905199261453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 1.7733905199261453""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1
Total Standard Deviation in ln(k): 1.7733905199261453
""",
)

entry(
    index = 84,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R",
    kinetics = ArrheniusBM(A=(1.35353e+17,'m^3/(mol*s)'), n=-4.12152, w0=(195435,'J/mol'), E0=(19543.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2070725385213954, var=39.97682081216169, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R',), comment="""BM rule fitted to 23 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R
    Total Standard Deviation in ln(k): 13.19566649904195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R
Total Standard Deviation in ln(k): 13.19566649904195""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R
Total Standard Deviation in ln(k): 13.19566649904195
""",
)

entry(
    index = 85,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R",
    kinetics = ArrheniusBM(A=(1.14192e+15,'m^3/(mol*s)'), n=-2.2177, w0=(186231,'J/mol'), E0=(18623.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4510032796647716, var=19.85276587057504, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R
    Total Standard Deviation in ln(k): 10.065560432171344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R
Total Standard Deviation in ln(k): 10.065560432171344""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R
Total Standard Deviation in ln(k): 10.065560432171344
""",
)

entry(
    index = 86,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing",
    kinetics = ArrheniusBM(A=(1.01846e+07,'m^3/(mol*s)'), n=0.342681, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.041780033705653176, var=0.2726914782705248, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing
    Total Standard Deviation in ln(k): 1.15184500261956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 1.15184500261956""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 1.15184500261956
""",
)

entry(
    index = 87,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing",
    kinetics = ArrheniusBM(A=(2.96241e+08,'m^3/(mol*s)'), n=-0.396761, w0=(193759,'J/mol'), E0=(19375.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7828400456634212, var=31.84624708616608, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing',), comment="""BM rule fitted to 29 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing
    Total Standard Deviation in ln(k): 15.792714657750594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 15.792714657750594""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 15.792714657750594
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R",
    kinetics = ArrheniusBM(A=(89.4,'m^3/(mol*s)'), n=1.54, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.262388,'m^3/(mol*s)'), n=1.84767, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_4R!H->O",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=1.67934e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_4R!H->O
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_4R!H->O
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_4R!H->O
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 91,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(4.29418e+11,'m^3/(mol*s)'), n=-1.66245, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10409730126885786, var=1.0795983950620833, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O
    Total Standard Deviation in ln(k): 2.3445454185992145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O
Total Standard Deviation in ln(k): 2.3445454185992145""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O
Total Standard Deviation in ln(k): 2.3445454185992145
""",
)

entry(
    index = 92,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(4.55803e+19,'m^3/(mol*s)'), n=-4.68648, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06345678090303891, var=13.852408835840915, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R
    Total Standard Deviation in ln(k): 7.620827412883078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 7.620827412883078""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 7.620827412883078
""",
)

entry(
    index = 93,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing",
    kinetics = ArrheniusBM(A=(3.5471e+06,'m^3/(mol*s)'), n=-0.0529334, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02594719581388334, var=0.43953349774332723, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing
    Total Standard Deviation in ln(k): 1.394279639884687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing
Total Standard Deviation in ln(k): 1.394279639884687""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing
Total Standard Deviation in ln(k): 1.394279639884687
""",
)

entry(
    index = 94,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing",
    kinetics = ArrheniusBM(A=(40.9293,'m^3/(mol*s)'), n=1.24752, w0=(152600,'J/mol'), E0=(15260,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12987327669238594, var=1.292644311997628, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing
    Total Standard Deviation in ln(k): 2.6055886222411524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing
Total Standard Deviation in ln(k): 2.6055886222411524""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing
Total Standard Deviation in ln(k): 2.6055886222411524
""",
)

entry(
    index = 95,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.94916e+08,'m^3/(mol*s)'), n=-0.548055, w0=(165714,'J/mol'), E0=(16571.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013509500214697812, var=0.7492514207761182, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R',), comment="""BM rule fitted to 42 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R
    Total Standard Deviation in ln(k): 1.7692283251543803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R
Total Standard Deviation in ln(k): 1.7692283251543803""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R
Total Standard Deviation in ln(k): 1.7692283251543803
""",
)

entry(
    index = 96,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_3BrCClINOPSSi->Br",
    kinetics = ArrheniusBM(A=(310000,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_3BrCClINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_3BrCClINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_3BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_3BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br",
    kinetics = ArrheniusBM(A=(5.50475e+08,'m^3/(mol*s)'), n=-0.47747, w0=(152860,'J/mol'), E0=(15286,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03989164768431995, var=0.6017476282265359, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br
    Total Standard Deviation in ln(k): 1.6553512597570494"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 1.6553512597570494""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 1.6553512597570494
""",
)

entry(
    index = 98,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.23243e+20,'m^3/(mol*s)'), n=-4.89281, w0=(195524,'J/mol'), E0=(19552.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20223811500183766, var=10.235276087405978, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C
    Total Standard Deviation in ln(k): 6.9218083266075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C
Total Standard Deviation in ln(k): 6.9218083266075""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C
Total Standard Deviation in ln(k): 6.9218083266075
""",
)

entry(
    index = 99,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.68475e-16,'m^3/(mol*s)'), n=4.33877, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.8697538460650303, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 9.722999613228719"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_N-4R!H->C
Total Standard Deviation in ln(k): 9.722999613228719""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_N-4R!H->C
Total Standard Deviation in ln(k): 9.722999613228719
""",
)

entry(
    index = 100,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing",
    kinetics = ArrheniusBM(A=(1.98784e+47,'m^3/(mol*s)'), n=-12.1693, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.575146461471214, var=0.1377894866619035, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing
    Total Standard Deviation in ln(k): 14.75206346882034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 14.75206346882034""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 14.75206346882034
""",
)

entry(
    index = 101,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing",
    kinetics = ArrheniusBM(A=(7.4637e+06,'m^3/(mol*s)'), n=0.308635, w0=(184727,'J/mol'), E0=(18472.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8930774606618942, var=8.510101731534794, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing',), comment="""BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing
    Total Standard Deviation in ln(k): 8.092142154104884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 8.092142154104884""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing
Total Standard Deviation in ln(k): 8.092142154104884
""",
)

entry(
    index = 102,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.35338e+07,'m^3/(mol*s)'), n=0.337482, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06473678945074876, var=0.16285884646625434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 0.971681599438312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.971681599438312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.971681599438312
""",
)

entry(
    index = 103,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(7.66431e+06,'m^3/(mol*s)'), n=0.347881, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17016890191634104, var=0.2974812683061607, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.520979521855843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.520979521855843""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.520979521855843
""",
)

entry(
    index = 104,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi",
    kinetics = ArrheniusBM(A=(7.23271e+07,'m^3/(mol*s)'), n=-0.170852, w0=(195933,'J/mol'), E0=(19593.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6935148369814748, var=49.44014709951868, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi',), comment="""BM rule fitted to 15 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi
    Total Standard Deviation in ln(k): 20.863656879446843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi
Total Standard Deviation in ln(k): 20.863656879446843""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi
Total Standard Deviation in ln(k): 20.863656879446843
""",
)

entry(
    index = 105,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi",
    kinetics = ArrheniusBM(A=(3.31985e+13,'m^3/(mol*s)'), n=-2.25963, w0=(191429,'J/mol'), E0=(19142.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0019045610264583096, var=10.092586346764705, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi',), comment="""BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi
    Total Standard Deviation in ln(k): 6.373594353068106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi
Total Standard Deviation in ln(k): 6.373594353068106""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi
Total Standard Deviation in ln(k): 6.373594353068106
""",
)

entry(
    index = 106,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.21643e+14,'m^3/(mol*s)'), n=-2.4333, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15129391754616475, var=1.8386561999030853, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R
    Total Standard Deviation in ln(k): 3.0984972465701626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 3.0984972465701626""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 3.0984972465701626
""",
)

entry(
    index = 107,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(8.93449,'m^3/(mol*s)'), n=1.77413, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-1CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-1CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(9.05135e+16,'m^3/(mol*s)'), n=-3.59877, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.52615920770435, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R_Ext-1CFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 6.347133687699372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 6.347133687699372""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_2R->C_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 6.347133687699372
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(27200,'m^3/(mol*s)'), n=0.504, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(252000,'m^3/(mol*s)'), n=0.34, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_2R-inRing_Ext-2R-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R",
    kinetics = ArrheniusBM(A=(39.2281,'m^3/(mol*s)'), n=1.25113, w0=(149462,'J/mol'), E0=(14946.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1702924000069968, var=1.2729812194748986, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R
    Total Standard Deviation in ln(k): 2.6897421601996387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 2.6897421601996387""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 2.6897421601996387
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(700,'K'), Tmax=(1300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(4.22639e+08,'m^3/(mol*s)'), n=-0.575127, w0=(165537,'J/mol'), E0=(16553.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0026823772414088856, var=0.4101902475823604, Tref=1000.0, N=41, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 41 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 1.2906942033807913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 41 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 1.2906942033807913""",
    longDesc = 
"""
BM rule fitted to 41 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 1.2906942033807913
""",
)

entry(
    index = 114,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_2R->F",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(77500,'J/mol'), E0=(7750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_2R->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_2R->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_2R->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_2R->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F",
    kinetics = ArrheniusBM(A=(6.68232e+08,'m^3/(mol*s)'), n=-0.516056, w0=(156000,'J/mol'), E0=(15600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03676651953981065, var=0.5673351049419127, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F
    Total Standard Deviation in ln(k): 1.6023777402903088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F
Total Standard Deviation in ln(k): 1.6023777402903088""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F
Total Standard Deviation in ln(k): 1.6023777402903088
""",
)

entry(
    index = 116,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH",
    kinetics = ArrheniusBM(A=(6.02035e+22,'m^3/(mol*s)'), n=-5.92853, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24318537331007758, var=14.29956356817709, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH',), comment="""BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH
    Total Standard Deviation in ln(k): 8.191876857479853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH
Total Standard Deviation in ln(k): 8.191876857479853""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH
Total Standard Deviation in ln(k): 8.191876857479853
""",
)

entry(
    index = 117,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH",
    kinetics = ArrheniusBM(A=(2.23161e+15,'m^3/(mol*s)'), n=-3.06618, w0=(197571,'J/mol'), E0=(19757.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13208148909312953, var=2.5627592826595587, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH
    Total Standard Deviation in ln(k): 3.5411673308089804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH
Total Standard Deviation in ln(k): 3.5411673308089804""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH
Total Standard Deviation in ln(k): 3.5411673308089804
""",
)

entry(
    index = 118,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_4R!H->C",
    kinetics = ArrheniusBM(A=(8.04193e+08,'m^3/(mol*s)'), n=-0.845814, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_N-4R!H->C",
    kinetics = ArrheniusBM(A=(8.27077e+07,'m^3/(mol*s)'), n=0.0781819, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_3BrCClINOPSSi-inRing_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=-9.86414e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 121,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(7.16126e+06,'m^3/(mol*s)'), n=0.313555, w0=(187333,'J/mol'), E0=(18733.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9699132877935568, var=9.374691662326235, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 8.575089629216025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 8.575089629216025""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 8.575089629216025
""",
)

entry(
    index = 122,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3BrCClINOPSSi",
    kinetics = ArrheniusBM(A=(2.09978e+06,'m^3/(mol*s)'), n=0.6, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3BrCClINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3BrCClINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3BrCClINOPSSi",
    kinetics = ArrheniusBM(A=(7.09e+06,'m^3/(mol*s)'), n=0.412, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3BrCClINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3BrCClINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3BrCClINOPSSi",
    kinetics = ArrheniusBM(A=(3.156e+06,'m^3/(mol*s)'), n=0.461, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3BrCClINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3BrCClINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3BrCClINOPSSi",
    kinetics = ArrheniusBM(A=(7.22657e+07,'m^3/(mol*s)'), n=0.062, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3BrCClINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3BrCClINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_3BrCClINOPSSi-inRing_Ext-3BrCClINOPSSi-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3BrCClINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.6368e+13,'m^3/(mol*s)'), n=-2.45156, w0=(196154,'J/mol'), E0=(19615.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.35868716904138, var=93.54889654206913, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 22.8037205515966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 22.8037205515966""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 22.8037205515966
""",
)

entry(
    index = 127,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(500000,'m^3/(mol*s)'), n=0.65, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.29185e+13,'m^3/(mol*s)'), n=-2.25556, w0=(192846,'J/mol'), E0=(19284.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007728846821414157, var=10.215132262394631, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 6.426777159265439"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 6.426777159265439""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 6.426777159265439
""",
)

entry(
    index = 130,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(46800,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(1500,'K'), Tmax=(1900,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(5.51461e+11,'m^3/(mol*s)'), n=-1.57028, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1151766381959885, var=0.08392520885607681, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 0.8701572413191333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 0.8701572413191333""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 0.8701572413191333
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.24e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(28.6108,'m^3/(mol*s)'), n=1.28701, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3508873204812941, var=1.2500735143094257, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.1230542962373744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.1230542962373744""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.1230542962373744
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(6.33097e+06,'m^3/(mol*s)'), n=-0.126595, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0011948175063002551, var=0.7118458320730411, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R
    Total Standard Deviation in ln(k): 1.6944162165011283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 1.6944162165011283""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 1.6944162165011283
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(3.24036e+06,'m^3/(mol*s)'), n=3.5707e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.458191251135313e-17, var=0.04752486418241179, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R
    Total Standard Deviation in ln(k): 0.43703622037861506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.43703622037861506""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.43703622037861506
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.0788e+07,'m^3/(mol*s)'), n=-0.0615385, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10119467299673665, var=0.23309023930038508, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 1.222132439730246"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 1.222132439730246""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 1.222132439730246
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(5.49716e+08,'m^3/(mol*s)'), n=-0.61995, w0=(162800,'J/mol'), E0=(16280,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0029872007601149412, var=0.4146735543299425, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O',), comment="""BM rule fitted to 30 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 1.2984577208356434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 1.2984577208356434""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 1.2984577208356434
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C",
    kinetics = ArrheniusBM(A=(7.87574e+08,'m^3/(mol*s)'), n=-0.53266, w0=(168143,'J/mol'), E0=(16814.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.050372844191036666, var=0.6262466360993251, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C
    Total Standard Deviation in ln(k): 1.7130270023348484"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C
Total Standard Deviation in ln(k): 1.7130270023348484""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C
Total Standard Deviation in ln(k): 1.7130270023348484
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C",
    kinetics = ArrheniusBM(A=(1.16455e+08,'m^3/(mol*s)'), n=-0.339512, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3179822674697152, var=0.2780753180870089, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C
    Total Standard Deviation in ln(k): 1.8561043072456151"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C
Total Standard Deviation in ln(k): 1.8561043072456151""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C
Total Standard Deviation in ln(k): 1.8561043072456151
""",
)

entry(
    index = 140,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.31102e+24,'m^3/(mol*s)'), n=-6.29688, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24311847115999108, var=16.096428271817434, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R',), comment="""BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R
    Total Standard Deviation in ln(k): 8.653918583382982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R
Total Standard Deviation in ln(k): 8.653918583382982""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R
Total Standard Deviation in ln(k): 8.653918583382982
""",
)

entry(
    index = 141,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-2CH-R",
    kinetics = ArrheniusBM(A=(5.61544e+19,'m^3/(mol*s)'), n=-5.23414, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.6181443632259516, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-2CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-2CH-R
    Total Standard Deviation in ln(k): 9.090814982979778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-2CH-R
Total Standard Deviation in ln(k): 9.090814982979778""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-2CH-R
Total Standard Deviation in ln(k): 9.090814982979778
""",
)

entry(
    index = 142,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.75615e+14,'m^3/(mol*s)'), n=-2.73259, w0=(198800,'J/mol'), E0=(19880,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12190255642513333, var=4.341409507856388, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R
    Total Standard Deviation in ln(k): 4.483363722517368"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R
Total Standard Deviation in ln(k): 4.483363722517368""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R
Total Standard Deviation in ln(k): 4.483363722517368
""",
)

entry(
    index = 143,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O_Ext-4R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O_Ext-4R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O_Ext-4R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_3BrCClINOPSSi->O_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R",
    kinetics = ArrheniusBM(A=(1.62598e+07,'m^3/(mol*s)'), n=0.255122, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06239915174409146, var=9.629649721936181e-35, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R
    Total Standard Deviation in ln(k): 0.15678178830173736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R
Total Standard Deviation in ln(k): 0.15678178830173736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R
Total Standard Deviation in ln(k): 0.15678178830173736
""",
)

entry(
    index = 145,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.007e+06,'m^3/(mol*s)'), n=0.317069, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0788858923175833, var=10.756392260751998, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R
    Total Standard Deviation in ln(k): 9.285686034054576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 9.285686034054576""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 9.285686034054576
""",
)

entry(
    index = 146,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C",
    kinetics = ArrheniusBM(A=(6.7813e+09,'m^3/(mol*s)'), n=-0.554643, w0=(197571,'J/mol'), E0=(19757.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4517981639022639, var=1.094361112477809, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C
    Total Standard Deviation in ln(k): 3.232359031832054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C
Total Standard Deviation in ln(k): 3.232359031832054""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C
Total Standard Deviation in ln(k): 3.232359031832054
""",
)

entry(
    index = 147,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(9.57308e+16,'m^3/(mol*s)'), n=-4.56402, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25266302513080524, var=45.624686819957304, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C
    Total Standard Deviation in ln(k): 14.176025018987964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C
Total Standard Deviation in ln(k): 14.176025018987964""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C
Total Standard Deviation in ln(k): 14.176025018987964
""",
)

entry(
    index = 148,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.63507e+14,'m^3/(mol*s)'), n=-2.6312, w0=(196455,'J/mol'), E0=(19645.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07814714422007453, var=10.580081811896685, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 6.71715895161326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.71715895161326""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.71715895161326
""",
)

entry(
    index = 149,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Sp-3C=2CH",
    kinetics = ArrheniusBM(A=(1.21e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Sp-3C=2CH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Sp-3C=2CH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Sp-3C=2CH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Sp-3C=2CH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_N-Sp-3C=2CH",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_N-Sp-3C=2CH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_N-Sp-3C=2CH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_N-Sp-3C=2CH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_N-Sp-3C=2CH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(1.02195e+12,'m^3/(mol*s)'), n=-1.67613, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.0631977592804454, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R_Ext-1CFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 5.1839139680413195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 5.1839139680413195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_3R!H->F_Ext-2R-R_N-4R!H->O_Ext-2R-R_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 5.1839139680413195
""",
)

entry(
    index = 152,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.59358e+07,'m^3/(mol*s)'), n=-0.376247, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006393725549276232, var=1.6311549262143017, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 2.576445635305223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 2.576445635305223""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 2.576445635305223
""",
)

entry(
    index = 153,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(24.5417,'m^3/(mol*s)'), n=1.3063, w0=(105000,'J/mol'), E0=(10500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4220851556899367, var=1.3511068571537062, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.390761827754295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.390761827754295""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.390761827754295
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.41997e+06,'m^3/(mol*s)'), n=2.03379e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0701791321551761e-07, var=1.3573949411693382, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R
    Total Standard Deviation in ln(k): 2.3356628470831757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R
Total Standard Deviation in ln(k): 2.3356628470831757""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R
Total Standard Deviation in ln(k): 2.3356628470831757
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R",
    kinetics = ArrheniusBM(A=(1.5341e+07,'m^3/(mol*s)'), n=-5.79709e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.049992843543761246, var=0.028799346867665023, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R
    Total Standard Deviation in ln(k): 0.4658211261547759"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R
Total Standard Deviation in ln(k): 0.4658211261547759""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R
Total Standard Deviation in ln(k): 0.4658211261547759
""",
)

entry(
    index = 158,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R",
    kinetics = ArrheniusBM(A=(5.72376e+07,'m^3/(mol*s)'), n=-0.266667, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.567444707862951e-10, var=0.3734167743925125, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R
    Total Standard Deviation in ln(k): 1.2250502439511728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R
Total Standard Deviation in ln(k): 1.2250502439511728""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R
Total Standard Deviation in ln(k): 1.2250502439511728
""",
)

entry(
    index = 159,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.7473e+08,'m^3/(mol*s)'), n=-0.588741, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0153211661024847, var=0.5048940697919225, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R
    Total Standard Deviation in ln(k): 1.462977912068491"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.462977912068491""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.462977912068491
""",
)

entry(
    index = 160,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(7.17322e+08,'m^3/(mol*s)'), n=-0.682487, w0=(147500,'J/mol'), E0=(14750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5901830930098657, var=1.4362044171026478, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO
    Total Standard Deviation in ln(k): 3.885381619664692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO
Total Standard Deviation in ln(k): 3.885381619664692""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO
Total Standard Deviation in ln(k): 3.885381619664692
""",
)

entry(
    index = 161,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_N-Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(2.34255e+09,'m^3/(mol*s)'), n=-0.638761, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.140841174280219, var=5.711815422248178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_N-Sp-3C-1CFO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_N-Sp-3C-1CFO
    Total Standard Deviation in ln(k): 12.682758220790616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 12.682758220790616""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 12.682758220790616
""",
)

entry(
    index = 162,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C",
    kinetics = ArrheniusBM(A=(8.01083e+08,'m^3/(mol*s)'), n=-0.535681, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.049930276085996594, var=0.6255692258758125, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C
    Total Standard Deviation in ln(k): 1.7110567529685492"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C
Total Standard Deviation in ln(k): 1.7110567529685492""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C
Total Standard Deviation in ln(k): 1.7110567529685492
""",
)

entry(
    index = 163,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C",
    kinetics = ArrheniusBM(A=(3.92429e+07,'m^3/(mol*s)'), n=-2.04069e-07, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.610921668180418e-17, var=3.634602426333292, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C
    Total Standard Deviation in ln(k): 3.821953910206615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C
Total Standard Deviation in ln(k): 3.821953910206615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C
Total Standard Deviation in ln(k): 3.821953910206615
""",
)

entry(
    index = 164,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C",
    kinetics = ArrheniusBM(A=(1.55563e+07,'m^3/(mol*s)'), n=5.49566e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.5050664115508311, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C
    Total Standard Deviation in ln(k): 1.4247256172567304"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C
Total Standard Deviation in ln(k): 1.4247256172567304""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C
Total Standard Deviation in ln(k): 1.4247256172567304
""",
)

entry(
    index = 165,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_N-3CNO->C",
    kinetics = ArrheniusBM(A=(5.15e+07,'m^3/(mol*s)'), n=-0.24, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_N-3CNO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_N-3CNO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_N-3CNO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_N-3CNO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(6.62538e+25,'m^3/(mol*s)'), n=-6.57335, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2296936572023689, var=27.115687013405577, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.016321603912314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.016321603912314""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.016321603912314
""",
)

entry(
    index = 167,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-2CH-R",
    kinetics = ArrheniusBM(A=(5.12997e+21,'m^3/(mol*s)'), n=-5.85334, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.859689466751467, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-2CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-2CH-R
    Total Standard Deviation in ln(k): 9.69771222801876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-2CH-R
Total Standard Deviation in ln(k): 9.69771222801876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-2CH-R
Total Standard Deviation in ln(k): 9.69771222801876
""",
)

entry(
    index = 168,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16859068524829143, var=3.7628736247711526e-20, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.4235946869423771"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.4235946869423771""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.4235946869423771
""",
)

entry(
    index = 170,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R_Ext-5R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R_Ext-5R!H-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R_Ext-5R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R_Ext-5R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-2CH-R_Ext-5R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.02165e+07,'m^3/(mol*s)'), n=1.96569e-07, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6503074289802206, var=0.9609060278364036, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.5990961488820474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.5990961488820474""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.5990961488820474
""",
)

entry(
    index = 172,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-4R!H-2CH",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-4R!H-2CH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-4R!H-2CH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-4R!H-2CH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-4R!H-2CH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH",
    kinetics = ArrheniusBM(A=(6.05281e+06,'m^3/(mol*s)'), n=0.432905, w0=(201667,'J/mol'), E0=(20166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6189091034252516, var=4.525479227810679, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH
    Total Standard Deviation in ln(k): 8.332318581557093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH
Total Standard Deviation in ln(k): 8.332318581557093""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH
Total Standard Deviation in ln(k): 8.332318581557093
""",
)

entry(
    index = 174,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(6.22465e+06,'m^3/(mol*s)'), n=0.377948, w0=(187333,'J/mol'), E0=(18733.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8006883955311086, var=2.313585216729668, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 5.0610769810352565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 5.0610769810352565""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 5.0610769810352565
""",
)

entry(
    index = 175,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(2.7416e+10,'m^3/(mol*s)'), n=-0.740932, w0=(205250,'J/mol'), E0=(20525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9895520210946384, var=2.792360228610262, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 5.8362954449323405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 5.8362954449323405""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 5.8362954449323405
""",
)

entry(
    index = 176,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.90326e+19,'m^3/(mol*s)'), n=-5.05673, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2428508679360926, var=78.20393043915139, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 18.3386489986133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 18.3386489986133""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 18.3386489986133
""",
)

entry(
    index = 177,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.38548e+08,'m^3/(mol*s)'), n=-0.161826, w0=(197571,'J/mol'), E0=(19757.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.46230175566570203, var=1.6235518990246747, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 3.7159690928250226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 3.7159690928250226""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 3.7159690928250226
""",
)

entry(
    index = 178,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16859068524829143, var=3.7628736247711526e-20, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 0.4235946869423771"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 0.4235946869423771""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 0.4235946869423771
""",
)

entry(
    index = 179,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.18e+06,'m^3/(mol*s)'), n=-0.085, w0=(71000,'J/mol'), E0=(7100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(2.90265e+10,'m^3/(mol*s)'), n=-1.39113, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(500000,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(297.12,'m^3/(mol*s)'), n=0.971996, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6005523355889325, var=0.015436303854962363, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R
    Total Standard Deviation in ln(k): 1.757999611670846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R
Total Standard Deviation in ln(k): 1.757999611670846""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R
Total Standard Deviation in ln(k): 1.757999611670846
""",
)

entry(
    index = 183,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(0.004135,'m^3/(mol*s)'), n=2.525, w0=(71000,'J/mol'), E0=(7100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.15543e+06,'m^3/(mol*s)'), n=5.67594e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.7836333533627092, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C
    Total Standard Deviation in ln(k): 1.7746529918743192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192
""",
)

entry(
    index = 185,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.505e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(200,'K'), Tmax=(300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.805e+07,'m^3/(mol*s)'), n=-3.68291e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6909130213063807e-18, var=6.138719718870696e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_4R!H->C
    Total Standard Deviation in ln(k): 0.01570709577335618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_4R!H->C
Total Standard Deviation in ln(k): 0.01570709577335618""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_4R!H->C
Total Standard Deviation in ln(k): 0.01570709577335618
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.50663e+07,'m^3/(mol*s)'), n=-6.21922e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0157930088378725, var=0.025533416301036095, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C
    Total Standard Deviation in ln(k): 0.3600211341595556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C
Total Standard Deviation in ln(k): 0.3600211341595556""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C
Total Standard Deviation in ln(k): 0.3600211341595556
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(2.52275e+08,'m^3/(mol*s)'), n=-0.533333, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.640548979333404e-11, var=0.38343074242542086, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 1.2413677392650118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.2413677392650118""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.2413677392650118
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.1e+07,'m^3/(mol*s)'), n=1.05326e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.07267224299466188, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R
    Total Standard Deviation in ln(k): 0.5404322678559177"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R
Total Standard Deviation in ln(k): 0.5404322678559177""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R
Total Standard Deviation in ln(k): 0.5404322678559177
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO",
    kinetics = ArrheniusBM(A=(2.07817e+08,'m^3/(mol*s)'), n=-0.524714, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09286041461129897, var=1.1213464681384786, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO
    Total Standard Deviation in ln(k): 2.356204730332115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO
Total Standard Deviation in ln(k): 2.356204730332115""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO
Total Standard Deviation in ln(k): 2.356204730332115
""",
)

entry(
    index = 191,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO",
    kinetics = ArrheniusBM(A=(8.39062e+08,'m^3/(mol*s)'), n=-0.632885, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011976657345507655, var=0.30284486892474555, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO
    Total Standard Deviation in ln(k): 1.133324736351128"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO
Total Standard Deviation in ln(k): 1.133324736351128""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO
Total Standard Deviation in ln(k): 1.133324736351128
""",
)

entry(
    index = 192,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C",
    kinetics = ArrheniusBM(A=(7.629e+08,'m^3/(mol*s)'), n=-0.689515, w0=(154455,'J/mol'), E0=(15445.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5540778563735251, var=1.325187266826214, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C
    Total Standard Deviation in ln(k): 3.699941854493604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C
Total Standard Deviation in ln(k): 3.699941854493604""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C
Total Standard Deviation in ln(k): 3.699941854493604
""",
)

entry(
    index = 193,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_N-1CFO->C",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_N-1CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_N-1CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing",
    kinetics = ArrheniusBM(A=(3.86009e+09,'m^3/(mol*s)'), n=-0.736026, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11335991425317883, var=0.44680103936298426, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing
    Total Standard Deviation in ln(k): 1.624852533645422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing
Total Standard Deviation in ln(k): 1.624852533645422""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing
Total Standard Deviation in ln(k): 1.624852533645422
""",
)

entry(
    index = 195,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(2.45248e+08,'m^3/(mol*s)'), n=-0.38487, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0991662218425231, var=1.582018322191672, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing
    Total Standard Deviation in ln(k): 2.770683258187423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing
Total Standard Deviation in ln(k): 2.770683258187423""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing
Total Standard Deviation in ln(k): 2.770683258187423
""",
)

entry(
    index = 196,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_3CNO-inRing",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_3CNO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_3CNO-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_3CNO-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_3CNO-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_N-3CNO-inRing",
    kinetics = ArrheniusBM(A=(7.7e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_N-3CNO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_N-3CNO-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_N-3CNO-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_N-2CO->C_N-3CNO-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_2CO->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_N-2CO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_N-2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_N-2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_N-1CFO->C_3CNO->C_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R",
    kinetics = ArrheniusBM(A=(2.52495e+27,'m^3/(mol*s)'), n=-6.83792, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21876648539641877, var=22.783101107081812, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R
    Total Standard Deviation in ln(k): 10.118595209729966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R
Total Standard Deviation in ln(k): 10.118595209729966""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R
Total Standard Deviation in ln(k): 10.118595209729966
""",
)

entry(
    index = 201,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.536223587017913, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 6.372421072909329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 6.372421072909329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_N-Sp-4C-2CH_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 6.372421072909329
""",
)

entry(
    index = 202,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_Ext-4R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_Sp-5R!H=3C",
    kinetics = ArrheniusBM(A=(5.18836e+06,'m^3/(mol*s)'), n=0.456743, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5242084718808067, var=0.5312435062659123, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_Sp-5R!H=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_Sp-5R!H=3C
    Total Standard Deviation in ln(k): 10.315975449803545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_Sp-5R!H=3C
Total Standard Deviation in ln(k): 10.315975449803545""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_Sp-5R!H=3C
Total Standard Deviation in ln(k): 10.315975449803545
""",
)

entry(
    index = 204,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_N-Sp-5R!H=3C",
    kinetics = ArrheniusBM(A=(3.4e+37,'m^3/(mol*s)'), n=-9.01, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_N-Sp-5R!H=3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_N-Sp-5R!H=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_N-Sp-5R!H=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_Ext-2CH-R_N-3BrCClINOPSSi-inRing_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-4R!H-2CH_N-Sp-5R!H=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2871.48,'m^3/(mol*s)'), n=1.36056, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1284797071889134, var=1.414218845306865, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R
    Total Standard Deviation in ln(k): 5.2194258193619625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R
Total Standard Deviation in ln(k): 5.2194258193619625""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R
Total Standard Deviation in ln(k): 5.2194258193619625
""",
)

entry(
    index = 206,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.19278e+10,'m^3/(mol*s)'), n=-0.758693, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.495770491077288, var=3.6624363383264167, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R
    Total Standard Deviation in ln(k): 10.10734045585341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R
Total Standard Deviation in ln(k): 10.10734045585341""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_N-Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R
Total Standard Deviation in ln(k): 10.10734045585341
""",
)

entry(
    index = 207,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(5.88256e+21,'m^3/(mol*s)'), n=-5.40115, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.703691587391238, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 9.305757757264416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 9.305757757264416""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_N-4R!H->C_Ext-3BrCClINOPSSi-R_Ext-3BrCClINOPSSi-R
Total Standard Deviation in ln(k): 9.305757757264416
""",
)

entry(
    index = 208,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.73542e+08,'m^3/(mol*s)'), n=-0.178898, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.047258352406939305, var=0.3305689258860327, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.271364493187482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.271364493187482""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.271364493187482
""",
)

entry(
    index = 209,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.536223587017913, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 6.372421072909329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.372421072909329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.372421072909329
""",
)

entry(
    index = 210,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.845,'m^3/(mol*s)'), n=1.52, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(0.0239,'m^3/(mol*s)'), n=2.243, w0=(71000,'J/mol'), E0=(7100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(7.05e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_3BrBrCCClClIINNOOPPSSSiSi-u1_N-2R-inRing_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(1.4799e+07,'m^3/(mol*s)'), n=-4.43449e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.32434502719988945, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R
    Total Standard Deviation in ln(k): 1.141722635385032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.141722635385032""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.141722635385032
""",
)

entry(
    index = 214,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.26848e+08,'m^3/(mol*s)'), n=-0.55, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.18719384195212638, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R
    Total Standard Deviation in ln(k): 0.8673667472246991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 0.8673667472246991""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 0.8673667472246991
""",
)

entry(
    index = 215,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_2R-inRing",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_2R-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_2R-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_N-2R-inRing",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_N-2R-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_N-2R-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_Sp-4R!H=2R",
    kinetics = ArrheniusBM(A=(578146,'m^3/(mol*s)'), n=0.175759, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06243996161282631, var=0.8653650783542394, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_Sp-4R!H=2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_Sp-4R!H=2R
    Total Standard Deviation in ln(k): 2.0217891484895985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_Sp-4R!H=2R
Total Standard Deviation in ln(k): 2.0217891484895985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_Sp-4R!H=2R
Total Standard Deviation in ln(k): 2.0217891484895985
""",
)

entry(
    index = 218,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R",
    kinetics = ArrheniusBM(A=(9.98868e+08,'m^3/(mol*s)'), n=-0.711595, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.019874770421035172, var=0.6700484978613325, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R
    Total Standard Deviation in ln(k): 1.690942380128545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R
Total Standard Deviation in ln(k): 1.690942380128545""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R
Total Standard Deviation in ln(k): 1.690942380128545
""",
)

entry(
    index = 219,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C",
    kinetics = ArrheniusBM(A=(7.61298e+09,'m^3/(mol*s)'), n=-0.886044, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13898275257305456, var=0.39501646066111173, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C
    Total Standard Deviation in ln(k): 1.6091856074382886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C
Total Standard Deviation in ln(k): 1.6091856074382886""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C
Total Standard Deviation in ln(k): 1.6091856074382886
""",
)

entry(
    index = 220,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C",
    kinetics = ArrheniusBM(A=(2.98503e+08,'m^3/(mol*s)'), n=-0.514244, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03686969119907329, var=0.12310334551463858, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C
    Total Standard Deviation in ln(k): 0.7960204953553649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C
Total Standard Deviation in ln(k): 0.7960204953553649""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C
Total Standard Deviation in ln(k): 0.7960204953553649
""",
)

entry(
    index = 221,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(8.09045e+08,'m^3/(mol*s)'), n=-0.842857, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.923656835879974e-09, var=1.2914637284046604, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R
    Total Standard Deviation in ln(k): 2.2782327881968145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R
Total Standard Deviation in ln(k): 2.2782327881968145""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R
Total Standard Deviation in ln(k): 2.2782327881968145
""",
)

entry(
    index = 222,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.38319e+06,'m^3/(mol*s)'), n=-3.04169e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.3279077205677291, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.1479760049827752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.1479760049827752""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.1479760049827752
""",
)

entry(
    index = 223,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_Sp-3CNO-1C",
    kinetics = ArrheniusBM(A=(1.80805e+10,'m^3/(mol*s)'), n=-0.964559, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8653580190429697, var=2.2967499295945233, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_Sp-3CNO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_Sp-3CNO-1C
    Total Standard Deviation in ln(k): 5.212448791473993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_Sp-3CNO-1C
Total Standard Deviation in ln(k): 5.212448791473993""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_Sp-3CNO-1C
Total Standard Deviation in ln(k): 5.212448791473993
""",
)

entry(
    index = 224,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_N-Sp-3CNO-1C",
    kinetics = ArrheniusBM(A=(1.43465e+08,'m^3/(mol*s)'), n=-0.248756, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.31020496668702713, var=1.8327263044935929, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_N-Sp-3CNO-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_N-Sp-3CNO-1C
    Total Standard Deviation in ln(k): 3.4933841715525316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_N-Sp-3CNO-1C
Total Standard Deviation in ln(k): 3.4933841715525316""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_1C-inRing_N-Sp-3CNO-1C
Total Standard Deviation in ln(k): 3.4933841715525316
""",
)

entry(
    index = 225,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R",
    kinetics = ArrheniusBM(A=(7.47266e+07,'m^3/(mol*s)'), n=-0.301656, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10484907111357072, var=0.14300243224887577, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R
    Total Standard Deviation in ln(k): 1.0215437259820683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R
Total Standard Deviation in ln(k): 1.0215437259820683""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R
Total Standard Deviation in ln(k): 1.0215437259820683
""",
)

entry(
    index = 226,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.8435e+08,'m^3/(mol*s)'), n=-0.384133, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002848069424167245, var=0.7068009850805346, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6925659381508393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 1.6925659381508393""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 1.6925659381508393
""",
)

entry(
    index = 227,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C",
    kinetics = ArrheniusBM(A=(7.08893e+08,'m^3/(mol*s)'), n=-0.459841, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6845857894881548, var=2.036600396114356, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C
    Total Standard Deviation in ln(k): 4.581012383557949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C
Total Standard Deviation in ln(k): 4.581012383557949""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C
Total Standard Deviation in ln(k): 4.581012383557949
""",
)

entry(
    index = 228,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_N-3CNO->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_N-3CNO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_N-3CNO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_N-3CNO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_N-3CNO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.38538e+32,'m^3/(mol*s)'), n=-8.31613, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.0631977592804454, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R_Ext-4C-R
    Total Standard Deviation in ln(k): 5.1839139680413195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R_Ext-4C-R
Total Standard Deviation in ln(k): 5.1839139680413195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_3R!H->F_Ext-2CH-R_4R!H->C_Sp-4C-2CH_Ext-4C-R_Ext-4C-R_Ext-2CH-R_Ext-4C-R
Total Standard Deviation in ln(k): 5.1839139680413195
""",
)

entry(
    index = 230,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_Ext-3BrCClINOPSSi-R_4R!H->C_Sp-4C=3BrBrCCClClIINNOOPPSSSiSi_Ext-4C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(7.17948e+35,'m^3/(mol*s)'), n=-8.45106, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(1.12754e+08,'m^3/(mol*s)'), n=-0.120184, w0=(187333,'J/mol'), E0=(18733.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27558012711070856, var=0.03551433839169183, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
    Total Standard Deviation in ln(k): 1.0702096829950607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 1.0702096829950607""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 1.0702096829950607
""",
)

entry(
    index = 233,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_Sp-4R!H=2R_N-4R!H->C_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(7.75e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_3BrCClINOPSSi->O_N-Sp-4R!H=2R_Ext-1CFO-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_2R-inRing",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_2R-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_2R-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing",
    kinetics = ArrheniusBM(A=(8.65419e+10,'m^3/(mol*s)'), n=-1.4012, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11076293667129158, var=0.13376655749343178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing
    Total Standard Deviation in ln(k): 1.01151286269961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing
Total Standard Deviation in ln(k): 1.01151286269961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing
Total Standard Deviation in ln(k): 1.01151286269961
""",
)

entry(
    index = 237,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_2R-inRing",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_2R-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_2R-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing",
    kinetics = ArrheniusBM(A=(8.74141e+09,'m^3/(mol*s)'), n=-0.910412, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3367359411241107, var=0.5233725103684882, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing
    Total Standard Deviation in ln(k): 2.296385553454193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing
Total Standard Deviation in ln(k): 2.296385553454193""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing
Total Standard Deviation in ln(k): 2.296385553454193
""",
)

entry(
    index = 239,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(8.06502e+08,'m^3/(mol*s)'), n=-0.64337, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006282835174823186, var=0.01963624099252782, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO
    Total Standard Deviation in ln(k): 0.29670828613131267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO
Total Standard Deviation in ln(k): 0.29670828613131267""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO
Total Standard Deviation in ln(k): 0.29670828613131267
""",
)

entry(
    index = 240,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_N-Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(5.7e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(1100,'K'), Tmax=(1400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_N-Sp-3C-1CFO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_N-Sp-3C-1CFO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.55114e+09,'m^3/(mol*s)'), n=-1.1, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6290223088470565e-10, var=2.385481895038608, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.096314395311866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.096314395311866""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.096314395311866
""",
)

entry(
    index = 242,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.98065e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.8575717470917588, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 1.8564883221612534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.8564883221612534""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.8564883221612534
""",
)

entry(
    index = 243,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.04e+06,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_Sp-3CNO-1C",
    kinetics = ArrheniusBM(A=(1.02e+08,'m^3/(mol*s)'), n=-0.32, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_Sp-3CNO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_Sp-3CNO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_Sp-3CNO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_Sp-3CNO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_N-Sp-3CNO-1C",
    kinetics = ArrheniusBM(A=(7.39463e+07,'m^3/(mol*s)'), n=-0.300554, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5494627794051327, var=0.0009400122881587426, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_N-Sp-3CNO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_N-Sp-3CNO-1C
    Total Standard Deviation in ln(k): 1.4420241625831092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_N-Sp-3CNO-1C
Total Standard Deviation in ln(k): 1.4420241625831092""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-3CNO-R_N-Sp-3CNO-1C
Total Standard Deviation in ln(k): 1.4420241625831092
""",
)

entry(
    index = 246,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C",
    kinetics = ArrheniusBM(A=(1.49777e+08,'m^3/(mol*s)'), n=-0.266667, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.142704777211466e-08, var=0.5786109659413581, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C
    Total Standard Deviation in ln(k): 1.5249315225351794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C
Total Standard Deviation in ln(k): 1.5249315225351794""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C
Total Standard Deviation in ln(k): 1.5249315225351794
""",
)

entry(
    index = 247,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C",
    kinetics = ArrheniusBM(A=(2.15423e+08,'m^3/(mol*s)'), n=-0.472233, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004984121469645847, var=0.41574972010160965, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C
    Total Standard Deviation in ln(k): 1.3051491714099865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C
Total Standard Deviation in ln(k): 1.3051491714099865""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C
Total Standard Deviation in ln(k): 1.3051491714099865
""",
)

entry(
    index = 248,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.07304e+09,'m^3/(mol*s)'), n=-0.543343, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2886192288092503, var=0.16825203022957477, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_Sp-3C-1C
    Total Standard Deviation in ln(k): 1.547486922797643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_Sp-3C-1C
Total Standard Deviation in ln(k): 1.547486922797643""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_Sp-3C-1C
Total Standard Deviation in ln(k): 1.547486922797643
""",
)

entry(
    index = 249,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_N-Sp-3C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_3CNO->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.4e+37,'m^3/(mol*s)'), n=-9.01, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCFHNO-inRing_N-2BrCFHNO->O_N-2CHN->N_Ext-2CH-R_N-3R!H->F_N-3BrCClINOPSSi-inRing_N-Sp-3BrCClINOPSSi-2BrCCClHINOPSSi_3BrCClINOPSSi->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.144e+13,'m^3/(mol*s)'), n=-2.163, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.307e+06,'m^3/(mol*s)'), n=0.192, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_Sp-3C=1CCFFOO_N-Sp-4R!H=2R_N-2R-inRing_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.1467e+08,'m^3/(mol*s)'), n=-0.471676, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005798092144622778, var=0.6851265997767169, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R
    Total Standard Deviation in ln(k): 1.6739348988156668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 1.6739348988156668""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 1.6739348988156668
""",
)

entry(
    index = 255,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.02e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_1CFO-inRing",
    kinetics = ArrheniusBM(A=(1.668e+09,'m^3/(mol*s)'), n=-0.7, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_1CFO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_1CFO-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_1CFO-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_1CFO-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_N-1CFO-inRing",
    kinetics = ArrheniusBM(A=(2.05e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_N-1CFO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_N-1CFO-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_N-1CFO-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_N-1CFO-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_3C-inRing",
    kinetics = ArrheniusBM(A=(5.781e+11,'m^3/(mol*s)'), n=-1.568, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.10412e+07,'m^3/(mol*s)'), n=-0.0142681, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.142724242208102, var=0.010025074383798795, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing
    Total Standard Deviation in ln(k): 0.5593283115054934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing
Total Standard Deviation in ln(k): 0.5593283115054934""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing
Total Standard Deviation in ln(k): 0.5593283115054934
""",
)

entry(
    index = 260,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.14759e+09,'m^3/(mol*s)'), n=-1.3, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=5.519561616726178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.70987392894025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.70987392894025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.70987392894025
""",
)

entry(
    index = 261,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_3CNO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_3CNO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_3CNO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_3CNO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_3CNO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_N-3CNO->C",
    kinetics = ArrheniusBM(A=(4.09878e+08,'m^3/(mol*s)'), n=-0.4, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=1.8811179631144743, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_N-3CNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_N-3CNO->C
    Total Standard Deviation in ln(k): 2.749571418511616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_N-3CNO->C
Total Standard Deviation in ln(k): 2.749571418511616""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_Sp-3CCNNOO=1C_N-3CNO->C
Total Standard Deviation in ln(k): 2.749571418511616
""",
)

entry(
    index = 263,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.90628e+07,'m^3/(mol*s)'), n=-0.319465, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14995901122765223, var=2.2305291506772655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.3708444816661607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.3708444816661607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_N-3BrCClINOPSSi->Br_N-2R->F_1CFO->C_2CO->C_N-1C-inRing_Ext-1C-R_N-Sp-3CCNNOO=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.3708444816661607
""",
)

entry(
    index = 264,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(7.24e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.02e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_Sp-5R!H=3C_N-2R-inRing_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_2R-inRing",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_2R-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_2R-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_N-2R-inRing",
    kinetics = ArrheniusBM(A=(5.89e+07,'m^3/(mol*s)'), n=-0.278, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_N-2R-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_N-2R-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_N-2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Ext-3C-R_N-Sp-3C=1CCFFOO_N-Sp-5R!H=3C_Sp-3C-1CFO_N-3C-inRing_N-2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 268,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'m^3/(mol*s)'), n=-1.5, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCFOS->S_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H->F_N-3BrBrCCClClIINNOOPPSSSiSi-u1_Ext-2R-R_N-Sp-3BrBrBrCCCCCClClClFFIIINNNOOOOOPPPSSSSiSiSi#1BrBrBrCCCCCCClClClFFFIIINNNOOOOOOPPPSSSSiSiSi_N-3BrCClINOPSSi->O_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

