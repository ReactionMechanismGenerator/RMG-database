#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(76.5449,'m^3/(mol*s)'), n=1.53201, w0=(577800,'J/mol'), E0=(32321.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007507445849901107, var=4.818763115271147, Tref=1000.0, N=145, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 145 training reactions at node Root
    Total Standard Deviation in ln(k): 4.419593478571859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 145 training reactions at node Root
Total Standard Deviation in ln(k): 4.419593478571859""",
    longDesc = 
"""
BM rule fitted to 145 training reactions at node Root
Total Standard Deviation in ln(k): 4.419593478571859
""",
)

entry(
    index = 2,
    label = "Root_Ext-4R-R",
    kinetics = ArrheniusBM(A=(0.383732,'m^3/(mol*s)'), n=2.17026, w0=(573891,'J/mol'), E0=(15657.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1705365449979058, var=12.92946671863943, Tref=1000.0, N=78, data_mean=0.0, correlation='Root_Ext-4R-R',), comment="""BM rule fitted to 78 training reactions at node Root_Ext-4R-R
    Total Standard Deviation in ln(k): 7.637023499534539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 78 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 7.637023499534539""",
    longDesc = 
"""
BM rule fitted to 78 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 7.637023499534539
""",
)

entry(
    index = 3,
    label = "Root_4R->N",
    kinetics = ArrheniusBM(A=(171.819,'m^3/(mol*s)'), n=1.30693, w0=(576750,'J/mol'), E0=(57954.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006344254869555567, var=1.8450924456048479, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_4R->N',), comment="""BM rule fitted to 10 training reactions at node Root_4R->N
    Total Standard Deviation in ln(k): 2.7390557924023935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_4R->N
Total Standard Deviation in ln(k): 2.7390557924023935""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_4R->N
Total Standard Deviation in ln(k): 2.7390557924023935
""",
)

entry(
    index = 4,
    label = "Root_N-4R->N",
    kinetics = ArrheniusBM(A=(335.389,'m^3/(mol*s)'), n=1.38122, w0=(583333,'J/mol'), E0=(58985.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008183131155107437, var=2.452421455099006, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_N-4R->N',), comment="""BM rule fitted to 57 training reactions at node Root_N-4R->N
    Total Standard Deviation in ln(k): 3.160017658556819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 3.160017658556819""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 3.160017658556819
""",
)

entry(
    index = 5,
    label = "Root_Ext-4R-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(3.31468,'m^3/(mol*s)'), n=1.96393, w0=(573127,'J/mol'), E0=(26126.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09153362417006619, var=10.751002198416929, Tref=1000.0, N=63, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0',), comment="""BM rule fitted to 63 training reactions at node Root_Ext-4R-R_5R!H-u0
    Total Standard Deviation in ln(k): 6.803253878279548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 63 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 6.803253878279548""",
    longDesc = 
"""
BM rule fitted to 63 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 6.803253878279548
""",
)

entry(
    index = 6,
    label = "Root_Ext-4R-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(4.83445e+17,'m^3/(mol*s)'), n=-3.62279, w0=(577100,'J/mol'), E0=(121114,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.948304298942851, var=71.42398373401224, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-4R-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 24.3503594314862"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 24.3503594314862""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 24.3503594314862
""",
)

entry(
    index = 7,
    label = "Root_4R->N_4N-u1",
    kinetics = ArrheniusBM(A=(135.925,'m^3/(mol*s)'), n=1.34946, w0=(569125,'J/mol'), E0=(45274.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08840786488763987, var=0.34412425210452896, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_4R->N_4N-u1',), comment="""BM rule fitted to 8 training reactions at node Root_4R->N_4N-u1
    Total Standard Deviation in ln(k): 1.398150102686657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_4R->N_4N-u1
Total Standard Deviation in ln(k): 1.398150102686657""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_4R->N_4N-u1
Total Standard Deviation in ln(k): 1.398150102686657
""",
)

entry(
    index = 8,
    label = "Root_4R->N_N-4N-u1",
    kinetics = ArrheniusBM(A=(0.621183,'m^3/(mol*s)'), n=1.79525, w0=(607250,'J/mol'), E0=(75109.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19236995601706847, var=4.313472827692801, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->N_N-4N-u1',), comment="""BM rule fitted to 2 training reactions at node Root_4R->N_N-4N-u1
    Total Standard Deviation in ln(k): 4.646956197592991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->N_N-4N-u1
Total Standard Deviation in ln(k): 4.646956197592991""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->N_N-4N-u1
Total Standard Deviation in ln(k): 4.646956197592991
""",
)

entry(
    index = 9,
    label = "Root_N-4R->N_4CHOS->C",
    kinetics = ArrheniusBM(A=(16.4541,'m^3/(mol*s)'), n=1.55694, w0=(563559,'J/mol'), E0=(73074.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13338684927622338, var=1.169681120078925, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-4R->N_4CHOS->C
    Total Standard Deviation in ln(k): 2.5032998492672687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R->N_4CHOS->C
Total Standard Deviation in ln(k): 2.5032998492672687""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R->N_4CHOS->C
Total Standard Deviation in ln(k): 2.5032998492672687
""",
)

entry(
    index = 10,
    label = "Root_N-4R->N_N-4CHOS->C",
    kinetics = ArrheniusBM(A=(1170.97,'m^3/(mol*s)'), n=1.28855, w0=(591738,'J/mol'), E0=(49911.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.041404382627020814, var=0.6595390013177806, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C',), comment="""BM rule fitted to 40 training reactions at node Root_N-4R->N_N-4CHOS->C
    Total Standard Deviation in ln(k): 1.7321166951458924"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-4R->N_N-4CHOS->C
Total Standard Deviation in ln(k): 1.7321166951458924""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-4R->N_N-4CHOS->C
Total Standard Deviation in ln(k): 1.7321166951458924
""",
)

entry(
    index = 11,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N",
    kinetics = ArrheniusBM(A=(0.00984266,'m^3/(mol*s)'), n=2.60013, w0=(599375,'J/mol'), E0=(19766.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7799244398017502, var=30.66064328854914, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N
    Total Standard Deviation in ln(k): 15.572801791472143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N
Total Standard Deviation in ln(k): 15.572801791472143""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N
Total Standard Deviation in ln(k): 15.572801791472143
""",
)

entry(
    index = 12,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N",
    kinetics = ArrheniusBM(A=(5.1275,'m^3/(mol*s)'), n=1.96326, w0=(569309,'J/mol'), E0=(-2883.86,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5405802962821876, var=9.490235624631232, Tref=1000.0, N=55, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N',), comment="""BM rule fitted to 55 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N
    Total Standard Deviation in ln(k): 7.534074143723972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 55 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N
Total Standard Deviation in ln(k): 7.534074143723972""",
    longDesc = 
"""
BM rule fitted to 55 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N
Total Standard Deviation in ln(k): 7.534074143723972
""",
)

entry(
    index = 13,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C",
    kinetics = ArrheniusBM(A=(1.98552,'m^3/(mol*s)'), n=1.32666, w0=(562042,'J/mol'), E0=(32717.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04489547333649911, var=3.6945779798667755, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C
    Total Standard Deviation in ln(k): 3.966161128912621"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C
Total Standard Deviation in ln(k): 3.966161128912621""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C
Total Standard Deviation in ln(k): 3.966161128912621
""",
)

entry(
    index = 14,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C",
    kinetics = ArrheniusBM(A=(2.84171e+18,'m^3/(mol*s)'), n=-3.84298, w0=(637333,'J/mol'), E0=(124253,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.99223046706053, var=82.87684945324548, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C
    Total Standard Deviation in ln(k): 23.256055393337405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C
Total Standard Deviation in ln(k): 23.256055393337405""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C
Total Standard Deviation in ln(k): 23.256055393337405
""",
)

entry(
    index = 15,
    label = "Root_4R->N_4N-u1_2R!H-u1",
    kinetics = ArrheniusBM(A=(123.801,'m^3/(mol*s)'), n=1.35359, w0=(577357,'J/mol'), E0=(43866,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0838401646293852, var=0.3778890718608688, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1',), comment="""BM rule fitted to 7 training reactions at node Root_4R->N_4N-u1_2R!H-u1
    Total Standard Deviation in ln(k): 1.4430181131200719"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R->N_4N-u1_2R!H-u1
Total Standard Deviation in ln(k): 1.4430181131200719""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R->N_4N-u1_2R!H-u1
Total Standard Deviation in ln(k): 1.4430181131200719
""",
)

entry(
    index = 16,
    label = "Root_4R->N_4N-u1_N-2R!H-u1",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_4N-u1_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_4R->N_N-4N-u1_1R!H->N",
    kinetics = ArrheniusBM(A=(2.14335e-08,'m^3/(mol*s)'), n=3.82365, w0=(589000,'J/mol'), E0=(44051.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_N-4N-u1_1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_N-4N-u1_1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_N-4N-u1_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_N-4N-u1_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_4R->N_N-4N-u1_N-1R!H->N",
    kinetics = ArrheniusBM(A=(5.61333e-06,'m^3/(mol*s)'), n=3.391, w0=(625500,'J/mol'), E0=(62581.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_N-4N-u1_N-1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_N-4N-u1_N-1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_N-4N-u1_N-1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_N-4N-u1_N-1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(16.9187,'m^3/(mol*s)'), n=1.55192, w0=(563300,'J/mol'), E0=(70522.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3109568304842985, var=1.8153607309626356, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C
    Total Standard Deviation in ln(k): 3.482384854278073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C
Total Standard Deviation in ln(k): 3.482384854278073""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C
Total Standard Deviation in ln(k): 3.482384854278073
""",
)

entry(
    index = 20,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(11.8568,'m^3/(mol*s)'), n=1.60239, w0=(563929,'J/mol'), E0=(73393.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09141396531548798, var=1.7014536546396284, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.844655380597524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.844655380597524""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.844655380597524
""",
)

entry(
    index = 21,
    label = "Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(45036.3,'m^3/(mol*s)'), n=0.583981, w0=(557600,'J/mol'), E0=(55760,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.055335839512987456, var=5.295135802475801, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 4.752163151876969"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.752163151876969""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.752163151876969
""",
)

entry(
    index = 22,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O",
    kinetics = ArrheniusBM(A=(761.319,'m^3/(mol*s)'), n=1.30669, w0=(601045,'J/mol'), E0=(41720.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04321676200614542, var=0.6031619039450257, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O',), comment="""BM rule fitted to 22 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O
    Total Standard Deviation in ln(k): 1.665532231109375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O
Total Standard Deviation in ln(k): 1.665532231109375""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O
Total Standard Deviation in ln(k): 1.665532231109375
""",
)

entry(
    index = 23,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O",
    kinetics = ArrheniusBM(A=(4115.16,'m^3/(mol*s)'), n=1.19882, w0=(589115,'J/mol'), E0=(57400.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.026231426391866507, var=0.42917486967047497, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O
    Total Standard Deviation in ln(k): 1.3792389125499238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O
Total Standard Deviation in ln(k): 1.3792389125499238""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O
Total Standard Deviation in ln(k): 1.3792389125499238
""",
)

entry(
    index = 24,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N",
    kinetics = ArrheniusBM(A=(1.11747e+10,'m^3/(mol*s)'), n=-0.951689, w0=(602625,'J/mol'), E0=(100366,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.631984364060142, var=40.55134635840639, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N
    Total Standard Deviation in ln(k): 21.89172960593503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N
Total Standard Deviation in ln(k): 21.89172960593503""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N
Total Standard Deviation in ln(k): 21.89172960593503
""",
)

entry(
    index = 25,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(0.163682,'m^3/(mol*s)'), n=2.28537, w0=(596125,'J/mol'), E0=(-2114.43,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.433755068894434, var=21.481570203729575, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N
    Total Standard Deviation in ln(k): 20.43167732251813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N
Total Standard Deviation in ln(k): 20.43167732251813""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N
Total Standard Deviation in ln(k): 20.43167732251813
""",
)

entry(
    index = 26,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O",
    kinetics = ArrheniusBM(A=(2.27485e-05,'m^3/(mol*s)'), n=3.61134, w0=(658333,'J/mol'), E0=(-31530.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5617229483947741, var=0.7916768113238771, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O
    Total Standard Deviation in ln(k): 3.195101728508319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O
Total Standard Deviation in ln(k): 3.195101728508319""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O
Total Standard Deviation in ln(k): 3.195101728508319
""",
)

entry(
    index = 27,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(227.706,'m^3/(mol*s)'), n=1.46248, w0=(544465,'J/mol'), E0=(54445.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07613779923032318, var=11.3577860438265, Tref=1000.0, N=43, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O',), comment="""BM rule fitted to 43 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O
    Total Standard Deviation in ln(k): 6.947521752261853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 43 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O
Total Standard Deviation in ln(k): 6.947521752261853""",
    longDesc = 
"""
BM rule fitted to 43 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O
Total Standard Deviation in ln(k): 6.947521752261853
""",
)

entry(
    index = 28,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(97648.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(0.0337834,'m^3/(mol*s)'), n=1.77326, w0=(563000,'J/mol'), E0=(4756.14,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3542500257343754, var=1.4344800176511403, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 3.2911422312511722"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 3.2911422312511722""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 3.2911422312511722
""",
)

entry(
    index = 30,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(2.6e+09,'m^3/(mol*s)'), n=-1.26, w0=(551500,'J/mol'), E0=(34913.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_N-Sp-2R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_1NOS->O",
    kinetics = ArrheniusBM(A=(5.7209e+06,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(20296,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_1NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_1NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_1NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_1NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O",
    kinetics = ArrheniusBM(A=(4.71824e+18,'m^3/(mol*s)'), n=-3.90657, w0=(616250,'J/mol'), E0=(124915,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.6178925766997465, var=50.07307454547724, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O
    Total Standard Deviation in ln(k): 20.763592202663844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O
Total Standard Deviation in ln(k): 20.763592202663844""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O
Total Standard Deviation in ln(k): 20.763592202663844
""",
)

entry(
    index = 33,
    label = "Root_4R->N_4N-u1_2R!H-u1_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(97.18,'m^3/(mol*s)'), n=1.38035, w0=(581125,'J/mol'), E0=(36551.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1174061377159747, var=0.9685448374036849, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.2679438188850685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.2679438188850685""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.2679438188850685
""",
)

entry(
    index = 35,
    label = "Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(82.6213,'m^3/(mol*s)'), n=1.38035, w0=(591250,'J/mol'), E0=(59125,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5787018105298811, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.4540246495725655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4540246495725655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4540246495725655
""",
)

entry(
    index = 36,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.04007e+08,'m^3/(mol*s)'), n=-0.641541, w0=(539000,'J/mol'), E0=(94986.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5089267739715351, var=1.3259860748533647, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 3.587192372944012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.587192372944012""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.587192372944012
""",
)

entry(
    index = 37,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N",
    kinetics = ArrheniusBM(A=(34.41,'m^3/(mol*s)'), n=1.44661, w0=(544000,'J/mol'), E0=(54400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43780050013999694, var=0.5999111817527254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N
    Total Standard Deviation in ln(k): 2.6527474307051118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 2.6527474307051118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 2.6527474307051118
""",
)

entry(
    index = 38,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N",
    kinetics = ArrheniusBM(A=(6.75617e+07,'m^3/(mol*s)'), n=-0.0357893, w0=(597250,'J/mol'), E0=(59725,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1140300975885116, var=16.478303783487792, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N
    Total Standard Deviation in ln(k): 13.449550144949319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.449550144949319""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.449550144949319
""",
)

entry(
    index = 39,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C",
    kinetics = ArrheniusBM(A=(112.108,'m^3/(mol*s)'), n=1.32982, w0=(553333,'J/mol'), E0=(46084.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07356566042383848, var=0.901197705462786, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C
    Total Standard Deviation in ln(k): 2.0879620883817496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 2.0879620883817496""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 2.0879620883817496
""",
)

entry(
    index = 40,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C",
    kinetics = ArrheniusBM(A=(0.615829,'m^3/(mol*s)'), n=1.96425, w0=(571875,'J/mol'), E0=(75296.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31045860474032627, var=0.9595215316593622, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 2.743788397345642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.743788397345642""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.743788397345642
""",
)

entry(
    index = 41,
    label = "Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H",
    kinetics = ArrheniusBM(A=(4.6737e+06,'m^3/(mol*s)'), n=5.94821e-07, w0=(556250,'J/mol'), E0=(55625,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0450894874009553e-07, var=4.263272832149988, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H
    Total Standard Deviation in ln(k): 4.139316232956384"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 4.139316232956384""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 4.139316232956384
""",
)

entry(
    index = 42,
    label = "Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_N-Sp-5R!H-1R!H",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_N-Sp-5R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_N-Sp-5R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_N-Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_N-Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1",
    kinetics = ArrheniusBM(A=(199.503,'m^3/(mol*s)'), n=1.42052, w0=(598208,'J/mol'), E0=(59820.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054914128893287124, var=0.21030678988471846, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1
    Total Standard Deviation in ln(k): 1.05733103277646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1
Total Standard Deviation in ln(k): 1.05733103277646""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1
Total Standard Deviation in ln(k): 1.05733103277646
""",
)

entry(
    index = 44,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(5286.42,'m^3/(mol*s)'), n=1.12227, w0=(604450,'J/mol'), E0=(53985.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04825845742218551, var=0.23705431038577612, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1
    Total Standard Deviation in ln(k): 1.0973222998803942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1
Total Standard Deviation in ln(k): 1.0973222998803942""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1
Total Standard Deviation in ln(k): 1.0973222998803942
""",
)

entry(
    index = 45,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1",
    kinetics = ArrheniusBM(A=(2918.61,'m^3/(mol*s)'), n=1.23867, w0=(593667,'J/mol'), E0=(56079,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.024821150567068174, var=0.4510440284709127, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1
    Total Standard Deviation in ln(k): 1.4087409995655844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1
Total Standard Deviation in ln(k): 1.4087409995655844""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1
Total Standard Deviation in ln(k): 1.4087409995655844
""",
)

entry(
    index = 46,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_N-2R!H-u1",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H",
    kinetics = ArrheniusBM(A=(1.36425e-17,'m^3/(mol*s)'), n=6.64861, w0=(587500,'J/mol'), E0=(-12941.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9061806186074375, var=24.835038546284007, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H
    Total Standard Deviation in ln(k): 12.267385976702148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H
Total Standard Deviation in ln(k): 12.267385976702148""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H
Total Standard Deviation in ln(k): 12.267385976702148
""",
)

entry(
    index = 48,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_N-Sp-2N-1R!H",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(648000,'J/mol'), E0=(54170.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_N-Sp-2N-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_N-Sp-2N-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_N-Sp-2N-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_N-Sp-2N-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O",
    kinetics = ArrheniusBM(A=(1.8853e+06,'m^3/(mol*s)'), n=0.332417, w0=(598500,'J/mol'), E0=(40111.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48440829182245476, var=6.9157034187503745, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O
    Total Standard Deviation in ln(k): 6.4891034436544075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O
Total Standard Deviation in ln(k): 6.4891034436544075""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O
Total Standard Deviation in ln(k): 6.4891034436544075
""",
)

entry(
    index = 50,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(5.9191e-07,'m^3/(mol*s)'), n=3.21489, w0=(589000,'J/mol'), E0=(24346.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_N-1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_N-1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS",
    kinetics = ArrheniusBM(A=(7.38113e+07,'m^3/(mol*s)'), n=-8.07774e-08, w0=(655500,'J/mol'), E0=(1088.46,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06280608228446091, var=6.8952486502763435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS
    Total Standard Deviation in ln(k): 5.421999069670699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS
Total Standard Deviation in ln(k): 5.421999069670699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS
Total Standard Deviation in ln(k): 5.421999069670699
""",
)

entry(
    index = 52,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS",
    kinetics = ArrheniusBM(A=(2.19318e-05,'m^3/(mol*s)'), n=3.61592, w0=(658900,'J/mol'), E0=(-33089.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008309840122592735, var=0.0365845111854325, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS
    Total Standard Deviation in ln(k): 0.40432623672436824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS
Total Standard Deviation in ln(k): 0.40432623672436824""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS
Total Standard Deviation in ln(k): 0.40432623672436824
""",
)

entry(
    index = 53,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_5R!H->N",
    kinetics = ArrheniusBM(A=(4.1753e-08,'m^3/(mol*s)'), n=3.29239, w0=(625500,'J/mol'), E0=(43176.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N",
    kinetics = ArrheniusBM(A=(15.1932,'m^3/(mol*s)'), n=1.84345, w0=(542536,'J/mol'), E0=(15614.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09124025461987828, var=1.6887344562395232, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N',), comment="""BM rule fitted to 42 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N
    Total Standard Deviation in ln(k): 2.8344264887801187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.8344264887801187""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.8344264887801187
""",
)

entry(
    index = 55,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.17653,'m^3/(mol*s)'), n=1.10567, w0=(563000,'J/mol'), E0=(3072.28,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.314520698902224, var=1.2584318477413965, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.039161791034125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.039161791034125""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.039161791034125
""",
)

entry(
    index = 56,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_Sp-2R!H-1N",
    kinetics = ArrheniusBM(A=(1.237e-11,'m^3/(mol*s)'), n=4.72018, w0=(548000,'J/mol'), E0=(72549.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_Sp-2R!H-1N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_Sp-2R!H-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_Sp-2R!H-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_Sp-2R!H-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_N-Sp-2R!H-1N",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=-0.34, w0=(684500,'J/mol'), E0=(61174.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_N-Sp-2R!H-1N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_N-Sp-2R!H-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_N-Sp-2R!H-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->C_N-1NOS->O_N-Sp-2R!H-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N",
    kinetics = ArrheniusBM(A=(81.7183,'m^3/(mol*s)'), n=1.38035, w0=(550250,'J/mol'), E0=(14285.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6204493662846748, var=3.9540263770573922, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
    Total Standard Deviation in ln(k): 5.545280338111078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 5.545280338111078""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 5.545280338111078
""",
)

entry(
    index = 59,
    label = "Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N",
    kinetics = ArrheniusBM(A=(1222.75,'m^3/(mol*s)'), n=1.08731, w0=(612000,'J/mol'), E0=(51891.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.880107590500096, var=0.27344860374733626, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
    Total Standard Deviation in ln(k): 3.2596479531592055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.2596479531592055""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.2596479531592055
""",
)

entry(
    index = 60,
    label = "Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(648000,'J/mol'), E0=(64800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H",
    kinetics = ArrheniusBM(A=(5.00408e+06,'m^3/(mol*s)'), n=-0.213333, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.4360805116511824e-10, var=0.5876693418882462, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H
    Total Standard Deviation in ln(k): 1.536821780682512"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 1.536821780682512""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 1.536821780682512
""",
)

entry(
    index = 63,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_N-Sp-5R!H-1R!H",
    kinetics = ArrheniusBM(A=(3.01e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(98632.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_N-Sp-5R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_N-Sp-5R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_N-Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_N-Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_Sp-2C-1N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(553500,'J/mol'), E0=(55350,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_N-Sp-2C-1N",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_N-Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_N-Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C",
    kinetics = ArrheniusBM(A=(8.11905e+07,'m^3/(mol*s)'), n=-0.34, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=14.717775896447819, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C
    Total Standard Deviation in ln(k): 7.690916252578899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 7.690916252578899""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 7.690916252578899
""",
)

entry(
    index = 67,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C",
    kinetics = ArrheniusBM(A=(6.61167e+07,'m^3/(mol*s)'), n=2.77409e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.7507532944488107, var=36.13951493076956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C
    Total Standard Deviation in ln(k): 21.475698718431726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 21.475698718431726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 21.475698718431726
""",
)

entry(
    index = 68,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_Sp-2NO-1C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=1.87, w0=(566000,'J/mol'), E0=(56600,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_Sp-2NO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C",
    kinetics = ArrheniusBM(A=(87.4311,'m^3/(mol*s)'), n=1.32982, w0=(547000,'J/mol'), E0=(26495.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6123916082581375, var=1.0791074750368763, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
    Total Standard Deviation in ln(k): 3.621193144618949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 3.621193144618949""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 3.621193144618949
""",
)

entry(
    index = 70,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(0.000312293,'m^3/(mol*s)'), n=2.90354, w0=(587833,'J/mol'), E0=(53849,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1230320030307755, var=0.5384824975894967, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 1.7802276338704983"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.7802276338704983""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.7802276338704983
""",
)

entry(
    index = 71,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O",
    kinetics = ArrheniusBM(A=(1.70765e+07,'m^3/(mol*s)'), n=7.53848e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9494596051172368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O
    Total Standard Deviation in ln(k): 1.9534182263699047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O
Total Standard Deviation in ln(k): 1.9534182263699047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O
Total Standard Deviation in ln(k): 1.9534182263699047
""",
)

entry(
    index = 73,
    label = "Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O",
    kinetics = ArrheniusBM(A=(1.27916e+06,'m^3/(mol*s)'), n=-3.7648e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9639738002758667, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O
    Total Standard Deviation in ln(k): 1.9682923503688117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O
Total Standard Deviation in ln(k): 1.9682923503688117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O
Total Standard Deviation in ln(k): 1.9682923503688117
""",
)

entry(
    index = 74,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C",
    kinetics = ArrheniusBM(A=(180.916,'m^3/(mol*s)'), n=1.41908, w0=(594625,'J/mol'), E0=(59462.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05734069577939827, var=0.9655647825075765, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C
    Total Standard Deviation in ln(k): 2.1139880562302724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C
Total Standard Deviation in ln(k): 2.1139880562302724""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C
Total Standard Deviation in ln(k): 2.1139880562302724
""",
)

entry(
    index = 75,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C",
    kinetics = ArrheniusBM(A=(204.448,'m^3/(mol*s)'), n=1.42089, w0=(600000,'J/mol'), E0=(60000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05487466294537096, var=0.23425984562370605, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C
    Total Standard Deviation in ln(k): 1.1081757792920701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C
Total Standard Deviation in ln(k): 1.1081757792920701""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C
Total Standard Deviation in ln(k): 1.1081757792920701
""",
)

entry(
    index = 76,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O",
    kinetics = ArrheniusBM(A=(3.08924e+06,'m^3/(mol*s)'), n=0.344613, w0=(670750,'J/mol'), E0=(71316.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2522028424953557, var=6.0581551465221715, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O
    Total Standard Deviation in ln(k): 8.080556867668387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O
Total Standard Deviation in ln(k): 8.080556867668387""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O
Total Standard Deviation in ln(k): 8.080556867668387
""",
)

entry(
    index = 77,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O",
    kinetics = ArrheniusBM(A=(5550.68,'m^3/(mol*s)'), n=1.11287, w0=(587875,'J/mol'), E0=(54599.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012192917709028375, var=0.2607328130650783, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O
    Total Standard Deviation in ln(k): 1.054293353120414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O
Total Standard Deviation in ln(k): 1.054293353120414""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O
Total Standard Deviation in ln(k): 1.054293353120414
""",
)

entry(
    index = 78,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(46201.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(100953,'m^3/(mol*s)'), n=0.813929, w0=(599125,'J/mol'), E0=(74644.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10915397915610936, var=0.525434426695319, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.7274256541983357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.7274256541983357""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.7274256541983357
""",
)

entry(
    index = 80,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(591167,'J/mol'), E0=(59116.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04104070874570528, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 0.10311735865755094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.10311735865755094""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.10311735865755094
""",
)

entry(
    index = 81,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O",
    kinetics = ArrheniusBM(A=(4.09438e-20,'m^3/(mol*s)'), n=7.31305, w0=(625500,'J/mol'), E0=(13317.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23706545185669597, var=40.171650205492554, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O
    Total Standard Deviation in ln(k): 13.301875151660841"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O
Total Standard Deviation in ln(k): 13.301875151660841""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O
Total Standard Deviation in ln(k): 13.301875151660841
""",
)

entry(
    index = 82,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_N-1R!H->O",
    kinetics = ArrheniusBM(A=(3.71959e-06,'m^3/(mol*s)'), n=3.45108, w0=(511500,'J/mol'), E0=(41011.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_N-1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_N-1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_5R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(24711.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N",
    kinetics = ArrheniusBM(A=(10.725,'m^3/(mol*s)'), n=1.90892, w0=(598500,'J/mol'), E0=(11124.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8611054555760191, var=1.2141850405896415, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N
    Total Standard Deviation in ln(k): 4.372600429820919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N
Total Standard Deviation in ln(k): 4.372600429820919""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N
Total Standard Deviation in ln(k): 4.372600429820919
""",
)

entry(
    index = 85,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_5R!H->C",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56853,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_Sp-5R!H=4CCOOSS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(2.85561e+07,'m^3/(mol*s)'), n=-0.375, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.06912283083491383, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R
    Total Standard Deviation in ln(k): 0.5270693322083513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R
Total Standard Deviation in ln(k): 0.5270693322083513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R
Total Standard Deviation in ln(k): 0.5270693322083513
""",
)

entry(
    index = 88,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C",
    kinetics = ArrheniusBM(A=(9.5058e+06,'m^3/(mol*s)'), n=-4.37112e-08, w0=(663500,'J/mol'), E0=(41589.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7525837574319836e-08, var=1.076658747326155, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C
    Total Standard Deviation in ln(k): 2.0801566196337635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C
Total Standard Deviation in ln(k): 2.0801566196337635""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C
Total Standard Deviation in ln(k): 2.0801566196337635
""",
)

entry(
    index = 89,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C",
    kinetics = ArrheniusBM(A=(3.06823e-33,'m^3/(mol*s)'), n=11.5608, w0=(648500,'J/mol'), E0=(-37786,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1311443344629586, var=3.4442370952847847, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C
    Total Standard Deviation in ln(k): 9.075152857245785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C
Total Standard Deviation in ln(k): 9.075152857245785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C
Total Standard Deviation in ln(k): 9.075152857245785
""",
)

entry(
    index = 90,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S",
    kinetics = ArrheniusBM(A=(1.98159e-12,'m^3/(mol*s)'), n=4.51961, w0=(522500,'J/mol'), E0=(12254.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.892917471575851, var=236.8699718122503, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S
    Total Standard Deviation in ln(k): 53.198050577502784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S
Total Standard Deviation in ln(k): 53.198050577502784""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S
Total Standard Deviation in ln(k): 53.198050577502784
""",
)

entry(
    index = 91,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S",
    kinetics = ArrheniusBM(A=(17.2722,'m^3/(mol*s)'), n=1.83189, w0=(544077,'J/mol'), E0=(18667,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11024155371116076, var=1.0388503421215214, Tref=1000.0, N=39, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S',), comment="""BM rule fitted to 39 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S
    Total Standard Deviation in ln(k): 2.3202951705012307"""),
    rank = 11,
    shortDesc = """BM rule fitted to 39 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S
Total Standard Deviation in ln(k): 2.3202951705012307""",
    longDesc = 
"""
BM rule fitted to 39 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S
Total Standard Deviation in ln(k): 2.3202951705012307
""",
)

entry(
    index = 92,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(935562,'m^3/(mol*s)'), n=-0.468454, w0=(563000,'J/mol'), E0=(41637.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07198396235717106, var=0.2938701865733815, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C
    Total Standard Deviation in ln(k): 1.2676270012587783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 1.2676270012587783""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 1.2676270012587783
""",
)

entry(
    index = 93,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_N-Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(602200,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(40463,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_N-Sp-6R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_N-Sp-6R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(589000,'J/mol'), E0=(45404.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O",
    kinetics = ArrheniusBM(A=(0.46,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(35268.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(625500,'J/mol'), E0=(51859.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N_4N-u1_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.02e+06,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_4C-u1",
    kinetics = ArrheniusBM(A=(1.15e+07,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4C-u1",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1",
    kinetics = ArrheniusBM(A=(2.19e+08,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1",
    kinetics = ArrheniusBM(A=(8.49e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(47358.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(638000,'J/mol'), E0=(77381.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O",
    kinetics = ArrheniusBM(A=(0.00010394,'m^3/(mol*s)'), n=3.02774, w0=(562750,'J/mol'), E0=(47277.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8568478925825855, var=0.083327900484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O
    Total Standard Deviation in ln(k): 2.73158245570468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O
Total Standard Deviation in ln(k): 2.73158245570468""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O
Total Standard Deviation in ln(k): 2.73158245570468
""",
)

entry(
    index = 108,
    label = "Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_4HO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_Ext-1R!H-R_Sp-5R!H-1R!H_N-4HO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N",
    kinetics = ArrheniusBM(A=(178.214,'m^3/(mol*s)'), n=1.42089, w0=(568000,'J/mol'), E0=(56800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 111,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=1.52807e-07, w0=(621250,'J/mol'), E0=(62125,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 112,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H",
    kinetics = ArrheniusBM(A=(237.941,'m^3/(mol*s)'), n=1.42089, w0=(594700,'J/mol'), E0=(59470,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054874663929626345, var=0.2454307711437369, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H
    Total Standard Deviation in ln(k): 1.1310412438815372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H
Total Standard Deviation in ln(k): 1.1310412438815372""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H
Total Standard Deviation in ln(k): 1.1310412438815372
""",
)

entry(
    index = 113,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H",
    kinetics = ArrheniusBM(A=(158.771,'m^3/(mol*s)'), n=1.42089, w0=(608833,'J/mol'), E0=(60883.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0548746646168159, var=0.3603397606017289, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H
    Total Standard Deviation in ln(k): 1.341284562656334"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H
Total Standard Deviation in ln(k): 1.341284562656334""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H
Total Standard Deviation in ln(k): 1.341284562656334
""",
)

entry(
    index = 114,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_2R!H->C",
    kinetics = ArrheniusBM(A=(9.04e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(662000,'J/mol'), E0=(47976.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(8137.79,'m^3/(mol*s)'), n=1.09281, w0=(577800,'J/mol'), E0=(58849.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03620730193697195, var=0.2854344123568272, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.162024130095498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.162024130095498""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.162024130095498
""",
)

entry(
    index = 117,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(604667,'J/mol'), E0=(60466.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04104071632119799, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.10311737769145222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.10311737769145222""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.10311737769145222
""",
)

entry(
    index = 118,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O",
    kinetics = ArrheniusBM(A=(677.321,'m^3/(mol*s)'), n=1.44792, w0=(657250,'J/mol'), E0=(58842.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03633496085430713, var=0.028750657654443026, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O
    Total Standard Deviation in ln(k): 0.43121712987894956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O
Total Standard Deviation in ln(k): 0.43121712987894956""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O
Total Standard Deviation in ln(k): 0.43121712987894956
""",
)

entry(
    index = 119,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O",
    kinetics = ArrheniusBM(A=(119884,'m^3/(mol*s)'), n=0.793481, w0=(579750,'J/mol'), E0=(76821.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13451436586717408, var=0.7097248998690975, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O
    Total Standard Deviation in ln(k): 2.02686830694364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O
Total Standard Deviation in ln(k): 2.02686830694364""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O
Total Standard Deviation in ln(k): 2.02686830694364
""",
)

entry(
    index = 120,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(55750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(608000,'J/mol'), E0=(60800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 122,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_4N-u1",
    kinetics = ArrheniusBM(A=(7.49208e-08,'m^3/(mol*s)'), n=4.04714, w0=(625500,'J/mol'), E0=(58689.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_4N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_4N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_4N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_4N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_N-4N-u1",
    kinetics = ArrheniusBM(A=(2.884e-08,'m^3/(mol*s)'), n=3.73641, w0=(625500,'J/mol'), E0=(72218.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_N-4N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_N-4N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_N-4N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_2R!H->N_Sp-2N-1R!H_1R!H->O_N-4N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_5CO->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(17330.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_N-5CO->C",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(13374.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_N-5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_N-5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->N_N-2R!H->N_1R!H->O_N-5R!H->N_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(3.47e+08,'m^3/(mol*s)'), n=-0.75, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R_Ext-4COS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R_Ext-4COS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R_Ext-4COS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_Ext-4COS-R_Ext-4COS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C",
    kinetics = ArrheniusBM(A=(7.09222e+06,'m^3/(mol*s)'), n=-1.82017e-08, w0=(655500,'J/mol'), E0=(18657.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03033922080218608, var=1.5693563328273934, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C
    Total Standard Deviation in ln(k): 2.587640078867295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C
Total Standard Deviation in ln(k): 2.587640078867295""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C
Total Standard Deviation in ln(k): 2.587640078867295
""",
)

entry(
    index = 128,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C",
    kinetics = ArrheniusBM(A=(2.11547e+08,'m^3/(mol*s)'), n=-0.313028, w0=(679500,'J/mol'), E0=(76755.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12167865343175763, var=0.6437215165799257, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C
    Total Standard Deviation in ln(k): 1.914169472146607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C
Total Standard Deviation in ln(k): 1.914169472146607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C
Total Standard Deviation in ln(k): 1.914169472146607
""",
)

entry(
    index = 129,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(635000,'J/mol'), E0=(6270.39,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.0294,'m^3/(mol*s)'), n=2.69, w0=(662000,'J/mol'), E0=(33464.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_4COS->C",
    kinetics = ArrheniusBM(A=(3.37e-12,'m^3/(mol*s)'), n=4.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_4COS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_4COS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_4COS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_4COS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C",
    kinetics = ArrheniusBM(A=(87.627,'m^3/(mol*s)'), n=1.43819, w0=(514250,'J/mol'), E0=(29804.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.017374686359450126, var=0.03974491286341071, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C
    Total Standard Deviation in ln(k): 0.4433215062458953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C
Total Standard Deviation in ln(k): 0.4433215062458953""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C
Total Standard Deviation in ln(k): 0.4433215062458953
""",
)

entry(
    index = 133,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O",
    kinetics = ArrheniusBM(A=(11.4006,'m^3/(mol*s)'), n=1.91038, w0=(595400,'J/mol'), E0=(21798.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02609482959117017, var=0.3875004658147189, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O
    Total Standard Deviation in ln(k): 1.313503170250616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O
Total Standard Deviation in ln(k): 1.313503170250616""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O
Total Standard Deviation in ln(k): 1.313503170250616
""",
)

entry(
    index = 134,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O",
    kinetics = ArrheniusBM(A=(13673.4,'m^3/(mol*s)'), n=0.570768, w0=(536529,'J/mol'), E0=(19688,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8546417106109898, var=7.071800778864522, Tref=1000.0, N=34, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O',), comment="""BM rule fitted to 34 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O
    Total Standard Deviation in ln(k): 7.4785044349428125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O
Total Standard Deviation in ln(k): 7.4785044349428125""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O
Total Standard Deviation in ln(k): 7.4785044349428125
""",
)

entry(
    index = 135,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-1.94626e-08, w0=(563000,'J/mol'), E0=(19905.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9622744622417605e-09, var=1.6745141564148134e-17, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.3133879754506031e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.3133879754506031e-08""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.3133879754506031e-08
""",
)

entry(
    index = 136,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10974.5,'m^3/(mol*s)'), n=7.68845e-08, w0=(563000,'J/mol'), E0=(19802.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2290956255676566e-17, var=0.06917824979652494, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.5272805777722495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495
""",
)

entry(
    index = 137,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(601500,'J/mol'), E0=(75336.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4CHOS->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_Sp-2C-1N",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_N-Sp-2C-1N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_N-Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_N-Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_1CO->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_1CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_1CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_N-1CO->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_N-1CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_N-1CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(3.6,'m^3/(mol*s)'), n=2, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(211.933,'m^3/(mol*s)'), n=1.42089, w0=(595875,'J/mol'), E0=(59587.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05487466192466684, var=0.2135346724240081, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 1.0642603451673014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.0642603451673014""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.0642603451673014
""",
)

entry(
    index = 145,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_Ext-2NO-R",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_Ext-2NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_Ext-2NO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_N-Sp-2NO-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(500,'m^3/(mol*s)'), n=1.5, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(4919.75,'m^3/(mol*s)'), n=1.14078, w0=(574750,'J/mol'), E0=(55918.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014663380331153596, var=0.27208609719602533, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 1.08255002480332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.08255002480332""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.08255002480332
""",
)

entry(
    index = 150,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 152,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(666000,'J/mol'), E0=(66600,'J/mol'), Tmin=(295,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(648500,'J/mol'), E0=(59319.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C",
    kinetics = ArrheniusBM(A=(23739.9,'m^3/(mol*s)'), n=1.06417, w0=(589333,'J/mol'), E0=(58933.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4757799687165822, var=4.841357739016837, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C
    Total Standard Deviation in ln(k): 8.119025613270948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C
Total Standard Deviation in ln(k): 8.119025613270948""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C
Total Standard Deviation in ln(k): 8.119025613270948
""",
)

entry(
    index = 155,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C",
    kinetics = ArrheniusBM(A=(841.375,'m^3/(mol*s)'), n=1.39007, w0=(570167,'J/mol'), E0=(60295,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01764788437096908, var=0.7683247228970326, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C
    Total Standard Deviation in ln(k): 1.8015745915808237"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C
Total Standard Deviation in ln(k): 1.8015745915808237""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C
Total Standard Deviation in ln(k): 1.8015745915808237
""",
)

entry(
    index = 156,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(545000,'J/mol'), E0=(54500,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(671000,'J/mol'), E0=(67100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56999.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(3.40826e+06,'m^3/(mol*s)'), n=-2.28069e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 160,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_N-Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(1.20333e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_N-Sp-5R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_N-Sp-5R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(55695.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_N-4COS->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_1CNS->C",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(515000,'J/mol'), E0=(39525.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_N-1CNS->C",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(513500,'J/mol'), E0=(42507.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_5COS->S_N-4COS->C_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(573833,'J/mol'), E0=(21511.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03872283658228287, var=0.003687235162771551, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 0.2190263021681399"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 0.2190263021681399""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 0.2190263021681399
""",
)

entry(
    index = 166,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(7.45181,'m^3/(mol*s)'), n=1.90892, w0=(627750,'J/mol'), E0=(62775,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8809875394276374, var=0.011502560091510204, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 2.4285443457657907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 2.4285443457657907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 2.4285443457657907
""",
)

entry(
    index = 167,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(10435.5,'m^3/(mol*s)'), n=0.604115, w0=(533150,'J/mol'), E0=(-3821.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.289440655341603, var=19.698731228461046, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R
    Total Standard Deviation in ln(k): 14.650029815189617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R
Total Standard Deviation in ln(k): 14.650029815189617""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R
Total Standard Deviation in ln(k): 14.650029815189617
""",
)

entry(
    index = 168,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS",
    kinetics = ArrheniusBM(A=(5.08215e+06,'m^3/(mol*s)'), n=-2.156e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.8487835248037475e-08, var=0.19740695447292192, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS
    Total Standard Deviation in ln(k): 0.8907139134007048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS
Total Standard Deviation in ln(k): 0.8907139134007048""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS
Total Standard Deviation in ln(k): 0.8907139134007048
""",
)

entry(
    index = 169,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS",
    kinetics = ArrheniusBM(A=(384095,'m^3/(mol*s)'), n=0.135638, w0=(537786,'J/mol'), E0=(63874.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.058598163214847246, var=1.4410358277500281, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS
    Total Standard Deviation in ln(k): 2.5537787366263016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS
Total Standard Deviation in ln(k): 2.5537787366263016""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS
Total Standard Deviation in ln(k): 2.5537787366263016
""",
)

entry(
    index = 170,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=5.24452e-08, w0=(563000,'J/mol'), E0=(21124.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 171,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_1NO->O",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(662000,'J/mol'), E0=(66200,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O",
    kinetics = ArrheniusBM(A=(200.038,'m^3/(mol*s)'), n=1.42089, w0=(573833,'J/mol'), E0=(57383.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054874661098006025, var=0.36033975866889256, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O
    Total Standard Deviation in ln(k): 1.3412845505876048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O
Total Standard Deviation in ln(k): 1.3412845505876048""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O
Total Standard Deviation in ln(k): 1.3412845505876048
""",
)

entry(
    index = 173,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2694.35,'m^3/(mol*s)'), n=1.20848, w0=(573833,'J/mol'), E0=(53393.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013509522983567904, var=0.5468798206070957, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 1.5164716418839155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.5164716418839155""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.5164716418839155
""",
)

entry(
    index = 175,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(23588.5,'m^3/(mol*s)'), n=1.06552, w0=(609250,'J/mol'), E0=(60925,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6761713695632989, var=0.41113237262952895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.984351249045606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.984351249045606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.984351249045606
""",
)

entry(
    index = 179,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(400,'m^3/(mol*s)'), n=1.5, w0=(564000,'J/mol'), E0=(56400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(33.4541,'m^3/(mol*s)'), n=1.78536, w0=(573250,'J/mol'), E0=(50750.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20147811603791788, var=0.27148248712845674, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 1.5507732128102802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.5507732128102802""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.5507732128102802
""",
)

entry(
    index = 181,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.82e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_1R!H->O_N-Sp-5R!H=4CCOOSS_2R!H->C_4COS->C_Sp-5R!H-4C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_2R!H->O",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(625500,'J/mol'), E0=(26705.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(548000,'J/mol'), E0=(31955.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0426036023134155, var=0.11276809873671895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O
    Total Standard Deviation in ln(k): 3.2928163591177713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O
Total Standard Deviation in ln(k): 3.2928163591177713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O
Total Standard Deviation in ln(k): 3.2928163591177713
""",
)

entry(
    index = 185,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C",
    kinetics = ArrheniusBM(A=(9955.74,'m^3/(mol*s)'), n=0.610082, w0=(526062,'J/mol'), E0=(-5161.94,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.764633640188899, var=24.53328009536312, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C
    Total Standard Deviation in ln(k): 16.875985278658277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C
Total Standard Deviation in ln(k): 16.875985278658277""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C
Total Standard Deviation in ln(k): 16.875985278658277
""",
)

entry(
    index = 188,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.7641e+06,'m^3/(mol*s)'), n=-0.0462319, w0=(561500,'J/mol'), E0=(17554.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2144940523654643, var=1.5169644222011907, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C
    Total Standard Deviation in ln(k): 3.008063935012343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C
Total Standard Deviation in ln(k): 3.008063935012343""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C
Total Standard Deviation in ln(k): 3.008063935012343
""",
)

entry(
    index = 189,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=-5.78148e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 190,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(341158,'m^3/(mol*s)'), n=0.159319, w0=(537400,'J/mol'), E0=(72316.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012764658041212053, var=1.78304604151697, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R
    Total Standard Deviation in ln(k): 2.709009730904846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R
Total Standard Deviation in ln(k): 2.709009730904846""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R
Total Standard Deviation in ln(k): 2.709009730904846
""",
)

entry(
    index = 191,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C",
    kinetics = ArrheniusBM(A=(1.44938e+08,'m^3/(mol*s)'), n=-0.656672, w0=(538700,'J/mol'), E0=(51750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.015100791888068623, var=0.06882506933829433, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C
    Total Standard Deviation in ln(k): 0.5638745627724189"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C
Total Standard Deviation in ln(k): 0.5638745627724189""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C
Total Standard Deviation in ln(k): 0.5638745627724189
""",
)

entry(
    index = 192,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_N-5CO->C",
    kinetics = ArrheniusBM(A=(2.89e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_N-5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_N-5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(20706.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->C_Sp-2R!H-1C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_2NO->O",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(625500,'J/mol'), E0=(55947.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(178.214,'m^3/(mol*s)'), n=1.42089, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 196,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(323.865,'m^3/(mol*s)'), n=1.46107, w0=(586750,'J/mol'), E0=(42728,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23284945485790864, var=0.6476388655306268, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 2.1983797414238784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.1983797414238784""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.1983797414238784
""",
)

entry(
    index = 197,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(642000,'J/mol'), E0=(64200,'J/mol'), Tmin=(300,'K'), Tmax=(1000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(720,'m^3/(mol*s)'), n=1.5, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(612000,'J/mol'), E0=(63724.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_N-4HO->O_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(39565.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_4COS->O_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_1CNS-inRing",
    kinetics = ArrheniusBM(A=(0.000675,'m^3/(mol*s)'), n=2.7, w0=(483500,'J/mol'), E0=(35785.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_1CNS-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_1CNS-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_1CNS-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_1CNS-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing",
    kinetics = ArrheniusBM(A=(30.8823,'m^3/(mol*s)'), n=1.00723, w0=(532143,'J/mol'), E0=(46648.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.5699258349692005, var=26.071960456115825, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing
    Total Standard Deviation in ln(k): 16.693419611260254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing
Total Standard Deviation in ln(k): 16.693419611260254""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing
Total Standard Deviation in ln(k): 16.693419611260254
""",
)

entry(
    index = 206,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C_Ext-4CS-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=0, w0=(561500,'J/mol'), E0=(36677.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C_Ext-4CS-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C_Ext-4CS-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C_Ext-4CS-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_N-2R!H->C_Ext-4CS-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Ext-1CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Ext-1CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS",
    kinetics = ArrheniusBM(A=(4.77012e+06,'m^3/(mol*s)'), n=-0.224333, w0=(536818,'J/mol'), E0=(53681.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0023056595278611387, var=0.734016272845928, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS
    Total Standard Deviation in ln(k): 1.7233448731964514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 1.7233448731964514""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 1.7233448731964514
""",
)

entry(
    index = 209,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS",
    kinetics = ArrheniusBM(A=(0.000269656,'m^3/(mol*s)'), n=2.91991, w0=(539000,'J/mol'), E0=(23511.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2766789743656475, var=3.675346905285673, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS
    Total Standard Deviation in ln(k): 4.538489869419958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 4.538489869419958""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 4.538489869419958
""",
)

entry(
    index = 210,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C",
    kinetics = ArrheniusBM(A=(2.14316e+08,'m^3/(mol*s)'), n=-0.7125, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.1701254570353375e-11, var=0.09039604166475083, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C
    Total Standard Deviation in ln(k): 0.6027423351607799"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C
Total Standard Deviation in ln(k): 0.6027423351607799""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C
Total Standard Deviation in ln(k): 0.6027423351607799
""",
)

entry(
    index = 211,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(979000,'m^3/(mol*s)'), n=0, w0=(537500,'J/mol'), E0=(38210.6,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_4O-u1_N-2R!H->C_Sp-2NO-1R!H_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(625500,'J/mol'), E0=(52128.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4CHOS->C_4HO->O_N-4O-u1_N-1R!H->O_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-2C-R",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(26972.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(2883.87,'m^3/(mol*s)'), n=0.430865, w0=(529400,'J/mol'), E0=(74637.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.853732040419501, var=23.748651972108167, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R
    Total Standard Deviation in ln(k): 16.9397739953667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R
Total Standard Deviation in ln(k): 16.9397739953667""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R
Total Standard Deviation in ln(k): 16.9397739953667
""",
)

entry(
    index = 218,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C",
    kinetics = ArrheniusBM(A=(8.57423e+06,'m^3/(mol*s)'), n=-0.274184, w0=(536333,'J/mol'), E0=(53633.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002818027022280064, var=0.4646994076753968, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C
    Total Standard Deviation in ln(k): 1.373685606859153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C
Total Standard Deviation in ln(k): 1.373685606859153""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C
Total Standard Deviation in ln(k): 1.373685606859153
""",
)

entry(
    index = 219,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C",
    kinetics = ArrheniusBM(A=(340826,'m^3/(mol*s)'), n=-2.03079e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 220,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(0.000740847,'m^3/(mol*s)'), n=2.91991, w0=(539000,'J/mol'), E0=(35253.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004220313209984355, var=8.94173911161422, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R
    Total Standard Deviation in ln(k): 6.005311154003196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R
Total Standard Deviation in ln(k): 6.005311154003196""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R
Total Standard Deviation in ln(k): 6.005311154003196
""",
)

entry(
    index = 221,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Sp-5CO-4CCOS",
    kinetics = ArrheniusBM(A=(964000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(92497.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Sp-5CO-4CCOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Sp-5CO-4CCOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Sp-5CO-4CCOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Sp-5CO-4CCOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-Sp-5CO-4CCOS",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-Sp-5CO-4CCOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-Sp-5CO-4CCOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-Sp-5CO-4CCOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-Sp-5CO-4CCOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS",
    kinetics = ArrheniusBM(A=(2.40321e+08,'m^3/(mol*s)'), n=-0.716667, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-8.959354181955872e-11, var=0.07236419854681579, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS
    Total Standard Deviation in ln(k): 0.5392856545722735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS
Total Standard Deviation in ln(k): 0.5392856545722735""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS
Total Standard Deviation in ln(k): 0.5392856545722735
""",
)

entry(
    index = 224,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_N-Sp-5C-4CS",
    kinetics = ArrheniusBM(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_N-Sp-5C-4CS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_N-Sp-5C-4CS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_N-Sp-5C-4CS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_N-Sp-5C-4CS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(2.92174e+06,'m^3/(mol*s)'), n=-0.165461, w0=(527000,'J/mol'), E0=(52700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17109444833057352, var=0.012736500736547286, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R
    Total Standard Deviation in ln(k): 0.6561321436322961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.6561321436322961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.6561321436322961
""",
)

entry(
    index = 226,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS",
    kinetics = ArrheniusBM(A=(2.68198,'m^3/(mol*s)'), n=1.27037, w0=(527000,'J/mol'), E0=(52700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.189097793822231, var=67.87381372743074, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS
    Total Standard Deviation in ln(k): 27.041494607627474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS
Total Standard Deviation in ln(k): 27.041494607627474""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS
Total Standard Deviation in ln(k): 27.041494607627474
""",
)

entry(
    index = 227,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_N-Sp-7R!H-1CNS",
    kinetics = ArrheniusBM(A=(84300,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(76690.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_N-Sp-7R!H-1CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_N-Sp-7R!H-1CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_N-Sp-7R!H-1CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_N-Sp-7R!H-1CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(7.43976e+07,'m^3/(mol*s)'), n=-0.55, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.374285187524525e-09, var=1.3251618088368264, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R
    Total Standard Deviation in ln(k): 2.307764272533085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R
Total Standard Deviation in ln(k): 2.307764272533085""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R
Total Standard Deviation in ln(k): 2.307764272533085
""",
)

entry(
    index = 229,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(1.67028e+06,'m^3/(mol*s)'), n=-0.0892194, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008454082745427579, var=0.025812025329597206, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 0.34332458300492497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.34332458300492497""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.34332458300492497
""",
)

entry(
    index = 230,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Sp-5C-4CS",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Sp-5C-4CS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Sp-5C-4CS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Sp-5C-4CS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Sp-5C-4CS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_N-Sp-5C-4CS",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_N-Sp-5C-4CS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_N-Sp-5C-4CS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_N-Sp-5C-4CS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_N-Sp-5C-4CS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(241000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C_Ext-1CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_N-5CO->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(85952.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R_Ext-4CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R_Ext-4CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_N-Sp-6R!H-1CNS_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(7.76827e+08,'m^3/(mol*s)'), n=-0.9, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0763652085225523e-17, var=0.04891149884417046, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R
    Total Standard Deviation in ln(k): 0.4433660913390881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R
Total Standard Deviation in ln(k): 0.4433660913390881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R
Total Standard Deviation in ln(k): 0.4433660913390881
""",
)

entry(
    index = 235,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_4CS->C",
    kinetics = ArrheniusBM(A=(783000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_4CS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_4CS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_4CS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_4CS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_N-4CS->C",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_N-4CS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_N-4CS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_N-4CS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Ext-1CNS-R_N-4CS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_4CS->C",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_4CS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_4CS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_4CS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_4CS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_N-4CS->C",
    kinetics = ArrheniusBM(A=(7.19e-07,'m^3/(mol*s)'), n=3.13, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_N-4CS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_N-4CS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_N-4CS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_Ext-5CO-R_2R!H->C_N-1CNS-inRing_Ext-1CNS-R_Sp-7R!H-1CNS_N-4CS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(1.52735e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 240,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(2.56e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-1CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-1CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=-8.08745e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 242,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_N-4CS->C",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_N-4CS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_N-4CS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_N-4CS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_N-4CS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(2.86e+09,'m^3/(mol*s)'), n=-1.1, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R_Ext-4CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R_Ext-4CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_5CO->C_2R!H->C_Sp-5C-4CS_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R_Ext-1CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R_Ext-1CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-4CS-R_Ext-4CS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->N_N-1R!H->O_N-5R!H->N_N-5COS->S_N-4COS->O_N-Sp-5CCCCCOOOSS#4CCCCCCOOOSSS_Ext-1CNS-R_Sp-6R!H-1CNS_5CO->C_Ext-1CNS-R_4CS->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

