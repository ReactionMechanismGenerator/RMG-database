#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = SurfaceArrheniusBM(A=(1.57514e+135,'m^2/(mol*s)'), n=-34.9301, w0=(407981,'J/mol'), E0=(342774,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8969500736876843, var=69.96954491172329, Tref=1000.0, N=272, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 272 training reactions at node Root
    Total Standard Deviation in ln(k): 21.535374151501507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 272 training reactions at node Root
Total Standard Deviation in ln(k): 21.535374151501507""",
    longDesc = 
"""
BM rule fitted to 272 training reactions at node Root
Total Standard Deviation in ln(k): 21.535374151501507
""",
)

entry(
    index = 2,
    label = "Root_Ext-1R!H-R",
    kinetics = SurfaceArrheniusBM(A=(2.40471e+167,'m^2/(mol*s)'), n=-44.3921, w0=(449993,'J/mol'), E0=(369632,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.394859162274529, var=51.35873363130022, Tref=1000.0, N=135, data_mean=0.0, correlation='Root_Ext-1R!H-R',), comment="""BM rule fitted to 135 training reactions at node Root_Ext-1R!H-R
    Total Standard Deviation in ln(k): 20.384169600096914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 135 training reactions at node Root_Ext-1R!H-R
Total Standard Deviation in ln(k): 20.384169600096914""",
    longDesc = 
"""
BM rule fitted to 135 training reactions at node Root_Ext-1R!H-R
Total Standard Deviation in ln(k): 20.384169600096914
""",
)

entry(
    index = 3,
    label = "Root_Sp-3Xo#1R!H",
    kinetics = SurfaceArrheniusBM(A=(5.18239e+42,'m^2/(mol*s)'), n=-7.66453, w0=(298401,'J/mol'), E0=(182126,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3881559238449434, var=37.35129885231663, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H',), comment="""BM rule fitted to 26 training reactions at node Root_Sp-3Xo#1R!H
    Total Standard Deviation in ln(k): 13.227346699325741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_Sp-3Xo#1R!H
Total Standard Deviation in ln(k): 13.227346699325741""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_Sp-3Xo#1R!H
Total Standard Deviation in ln(k): 13.227346699325741
""",
)

entry(
    index = 4,
    label = "Root_N-Sp-3Xo#1R!H",
    kinetics = SurfaceArrheniusBM(A=(4.67728e+12,'m^2/(mol*s)'), n=1.22753, w0=(382552,'J/mol'), E0=(130841,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07209702000199963, var=38.69812887774173, Tref=1000.0, N=111, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H',), comment="""BM rule fitted to 111 training reactions at node Root_N-Sp-3Xo#1R!H
    Total Standard Deviation in ln(k): 12.652168205689994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 111 training reactions at node Root_N-Sp-3Xo#1R!H
Total Standard Deviation in ln(k): 12.652168205689994""",
    longDesc = 
"""
BM rule fitted to 111 training reactions at node Root_N-Sp-3Xo#1R!H
Total Standard Deviation in ln(k): 12.652168205689994
""",
)

entry(
    index = 5,
    label = "Root_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = SurfaceArrheniusBM(A=(1.18323e+106,'m^2/(mol*s)'), n=-26.186, w0=(467913,'J/mol'), E0=(211036,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3893825934822164, var=32.08301811604532, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 24 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 14.846106065470398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 14.846106065470398""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 14.846106065470398
""",
)

entry(
    index = 6,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H",
    kinetics = SurfaceArrheniusBM(A=(5.14497e+199,'m^2/(mol*s)'), n=-53.9805, w0=(449528,'J/mol'), E0=(442139,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.891164473329081, var=47.141973551936914, Tref=1000.0, N=88, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H',), comment="""BM rule fitted to 88 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H
    Total Standard Deviation in ln(k): 21.028745948843607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 88 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 21.028745948843607""",
    longDesc = 
"""
BM rule fitted to 88 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 21.028745948843607
""",
)

entry(
    index = 7,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H",
    kinetics = SurfaceArrheniusBM(A=(1.18035e+26,'m^2/(mol*s)'), n=-2.59937, w0=(433075,'J/mol'), E0=(100279,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07893732278475336, var=50.28281800492878, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H',), comment="""BM rule fitted to 23 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H
    Total Standard Deviation in ln(k): 14.413987325258654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 14.413987325258654""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H
Total Standard Deviation in ln(k): 14.413987325258654
""",
)

entry(
    index = 8,
    label = "Root_Sp-3Xo#1R!H_2R->O",
    kinetics = SurfaceArrheniusBM(A=(8.82294e+16,'m^2/(mol*s)'), n=0, w0=(352230,'J/mol'), E0=(55315,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_2R->O',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-3Xo#1R!H_2R->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-3Xo#1R!H_2R->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-3Xo#1R!H_2R->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_Sp-3Xo#1R!H_N-2R->O",
    kinetics = SurfaceArrheniusBM(A=(9.14006e+45,'m^2/(mol*s)'), n=-8.62715, w0=(296248,'J/mol'), E0=(192143,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.437984754937424, var=35.596790205302725, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_N-2R->O',), comment="""BM rule fitted to 25 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O
    Total Standard Deviation in ln(k): 13.061324259475706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O
Total Standard Deviation in ln(k): 13.061324259475706""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O
Total Standard Deviation in ln(k): 13.061324259475706
""",
)

entry(
    index = 10,
    label = "Root_N-Sp-3Xo#1R!H_2R->C",
    kinetics = SurfaceArrheniusBM(A=(7.2624e+19,'m^2/(mol*s)'), n=-0.793678, w0=(339590,'J/mol'), E0=(163762,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020952688544341215, var=28.160351948247598, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C',), comment="""BM rule fitted to 28 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C
    Total Standard Deviation in ln(k): 10.691037914897297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C
Total Standard Deviation in ln(k): 10.691037914897297""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C
Total Standard Deviation in ln(k): 10.691037914897297
""",
)

entry(
    index = 11,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C",
    kinetics = SurfaceArrheniusBM(A=(9.10249e+09,'m^2/(mol*s)'), n=1.99353, w0=(397045,'J/mol'), E0=(119117,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11222287797029276, var=42.754463001812866, Tref=1000.0, N=83, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C',), comment="""BM rule fitted to 83 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C
    Total Standard Deviation in ln(k): 13.390307633230297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 83 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C
Total Standard Deviation in ln(k): 13.390307633230297""",
    longDesc = 
"""
BM rule fitted to 83 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C
Total Standard Deviation in ln(k): 13.390307633230297
""",
)

entry(
    index = 12,
    label = "Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H",
    kinetics = SurfaceArrheniusBM(A=(1.08345e+117,'m^2/(mol*s)'), n=-29.4633, w0=(484304,'J/mol'), E0=(231393,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5653630369210718, var=41.06347855152741, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H
    Total Standard Deviation in ln(k): 16.7795740326608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 16.7795740326608""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 16.7795740326608
""",
)

entry(
    index = 13,
    label = "Root_Ext-1R!H-R_Ext-5R!H-R_N-Sp-3Xo-1R!H",
    kinetics = SurfaceArrheniusBM(A=(392995,'m^2/(mol*s)'), n=3.57186, w0=(418740,'J/mol'), E0=(271.602,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3319988164081935, var=7.419751407439232, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1R!H-R_Ext-5R!H-R_N-Sp-3Xo-1R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_N-Sp-3Xo-1R!H
    Total Standard Deviation in ln(k): 6.294909988994371"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_N-Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 6.294909988994371""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_N-Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 6.294909988994371
""",
)

entry(
    index = 14,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R",
    kinetics = SurfaceArrheniusBM(A=(5.84924e+19,'m^2/(mol*s)'), n=-0.615032, w0=(491104,'J/mol'), E0=(80855.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.018038659187304497, var=13.454942869878538, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 7.398887973701893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 7.398887973701893""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 7.398887973701893
""",
)

entry(
    index = 15,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C",
    kinetics = SurfaceArrheniusBM(A=(3.33203e+248,'m^2/(mol*s)'), n=-68.4564, w0=(433737,'J/mol'), E0=(544584,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.6449150680802394, var=47.19503601327136, Tref=1000.0, N=58, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 58 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 22.93033607448069"""),
    rank = 11,
    shortDesc = """BM rule fitted to 58 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 22.93033607448069""",
    longDesc = 
"""
BM rule fitted to 58 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 22.93033607448069
""",
)

entry(
    index = 16,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C",
    kinetics = SurfaceArrheniusBM(A=(7.48353e+38,'m^2/(mol*s)'), n=-6.52202, w0=(463488,'J/mol'), E0=(123740,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.33029165317527415, var=11.436463627684128, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 7.609459713867804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 7.609459713867804""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 7.609459713867804
""",
)

entry(
    index = 17,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R",
    kinetics = SurfaceArrheniusBM(A=(2.09845e+57,'m^2/(mol*s)'), n=-11.6529, w0=(376367,'J/mol'), E0=(89560.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.9260620816342477, var=13.89589138279187, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R
    Total Standard Deviation in ln(k): 17.33756728607439"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R
Total Standard Deviation in ln(k): 17.33756728607439""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R
Total Standard Deviation in ln(k): 17.33756728607439
""",
)

entry(
    index = 18,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_2R->C",
    kinetics = SurfaceArrheniusBM(A=(1.61967e+37,'m^2/(mol*s)'), n=-5.82212, w0=(380416,'J/mol'), E0=(174657,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2589042363866633, var=37.28963168838113, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_2R->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_2R->C
    Total Standard Deviation in ln(k): 12.892475417391502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_2R->C
Total Standard Deviation in ln(k): 12.892475417391502""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_2R->C
Total Standard Deviation in ln(k): 12.892475417391502
""",
)

entry(
    index = 19,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C",
    kinetics = SurfaceArrheniusBM(A=(1.05837e-34,'m^2/(mol*s)'), n=15.1445, w0=(456619,'J/mol'), E0=(-40776.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.865606854605415, var=27.670655328373577, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C
    Total Standard Deviation in ln(k): 25.283194391975897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C
Total Standard Deviation in ln(k): 25.283194391975897""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C
Total Standard Deviation in ln(k): 25.283194391975897
""",
)

entry(
    index = 20,
    label = "Root_Sp-3Xo#1R!H_N-2R->O_2CHN->N",
    kinetics = SurfaceArrheniusBM(A=(1.60621e+37,'m^2/(mol*s)'), n=-6.46926, w0=(264657,'J/mol'), E0=(177034,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2753735753858046, var=82.2545759842997, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_N-2R->O_2CHN->N',), comment="""BM rule fitted to 4 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_2CHN->N
    Total Standard Deviation in ln(k): 18.87369956705952"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_2CHN->N
Total Standard Deviation in ln(k): 18.87369956705952""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_2CHN->N
Total Standard Deviation in ln(k): 18.87369956705952
""",
)

entry(
    index = 21,
    label = "Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N",
    kinetics = SurfaceArrheniusBM(A=(4.63402e+48,'m^2/(mol*s)'), n=-9.3407, w0=(302265,'J/mol'), E0=(197242,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4623513589417758, var=33.72237322788738, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N',), comment="""BM rule fitted to 21 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N
    Total Standard Deviation in ln(k): 12.803377481415586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N
Total Standard Deviation in ln(k): 12.803377481415586""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N
Total Standard Deviation in ln(k): 12.803377481415586
""",
)

entry(
    index = 22,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H",
    kinetics = SurfaceArrheniusBM(A=(7.43444e+21,'m^2/(mol*s)'), n=-1.40158, w0=(359772,'J/mol'), E0=(173190,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0379943322428607, var=39.23751609284379, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H',), comment="""BM rule fitted to 16 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H
    Total Standard Deviation in ln(k): 12.653094882294695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 12.653094882294695""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 12.653094882294695
""",
)

entry(
    index = 23,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H",
    kinetics = SurfaceArrheniusBM(A=(3.26968e+20,'m^2/(mol*s)'), n=-0.970526, w0=(312681,'J/mol'), E0=(159066,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029934960774732525, var=21.667197520530717, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H',), comment="""BM rule fitted to 12 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H
    Total Standard Deviation in ln(k): 9.406861732593525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 9.406861732593525""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 9.406861732593525
""",
)

entry(
    index = 24,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N",
    kinetics = SurfaceArrheniusBM(A=(75.3061,'m^2/(mol*s)'), n=4.39262, w0=(383632,'J/mol'), E0=(118812,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2221161090213995, var=50.436400048652395, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N',), comment="""BM rule fitted to 38 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N
    Total Standard Deviation in ln(k): 14.79542635755025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N
Total Standard Deviation in ln(k): 14.79542635755025""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N
Total Standard Deviation in ln(k): 14.79542635755025
""",
)

entry(
    index = 25,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N",
    kinetics = SurfaceArrheniusBM(A=(1.98118e+18,'m^2/(mol*s)'), n=-0.479647, w0=(408372,'J/mol'), E0=(121992,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0031597227176554275, var=33.17114725796785, Tref=1000.0, N=45, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N',), comment="""BM rule fitted to 45 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N
    Total Standard Deviation in ln(k): 11.554090072997543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 45 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N
Total Standard Deviation in ln(k): 11.554090072997543""",
    longDesc = 
"""
BM rule fitted to 45 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N
Total Standard Deviation in ln(k): 11.554090072997543
""",
)

entry(
    index = 26,
    label = "Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_6R!H->C",
    kinetics = SurfaceArrheniusBM(A=(2.08052e+18,'m^2/(mol*s)'), n=-0.235905, w0=(491104,'J/mol'), E0=(62386.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00484808790235725, var=10.92372277968423, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_6R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_6R!H->C
    Total Standard Deviation in ln(k): 6.638042181143128"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_6R!H->C
Total Standard Deviation in ln(k): 6.638042181143128""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_6R!H->C
Total Standard Deviation in ln(k): 6.638042181143128
""",
)

entry(
    index = 27,
    label = "Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_N-6R!H->C",
    kinetics = SurfaceArrheniusBM(A=(1.64123e+83,'m^2/(mol*s)'), n=-19.5411, w0=(470703,'J/mol'), E0=(7518.88,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.8037080394981935, var=188.03521339414823, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_N-6R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_N-6R!H->C
    Total Standard Deviation in ln(k): 39.559734862039605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_N-6R!H->C
Total Standard Deviation in ln(k): 39.559734862039605""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_Ext-5R!H-R_Sp-3Xo-1R!H_N-6R!H->C
Total Standard Deviation in ln(k): 39.559734862039605
""",
)

entry(
    index = 28,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H",
    kinetics = SurfaceArrheniusBM(A=(3.57425e+56,'m^2/(mol*s)'), n=-11.7762, w0=(473243,'J/mol'), E0=(169182,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6098748643777594, var=34.09338285285741, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H',), comment="""BM rule fitted to 28 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H
    Total Standard Deviation in ln(k): 13.237904639544219"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 13.237904639544219""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 13.237904639544219
""",
)

entry(
    index = 29,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H",
    kinetics = SurfaceArrheniusBM(A=(2.53807e+274,'m^2/(mol*s)'), n=-76.0684, w0=(396864,'J/mol'), E0=(589272,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.078849594123279, var=24.44147259644912, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H',), comment="""BM rule fitted to 30 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H
    Total Standard Deviation in ln(k): 20.159438785784783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 20.159438785784783""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 20.159438785784783
""",
)

entry(
    index = 30,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H",
    kinetics = SurfaceArrheniusBM(A=(1.45902e+36,'m^2/(mol*s)'), n=-5.73381, w0=(470102,'J/mol'), E0=(112127,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2800220416541504, var=7.375583391802708, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H
    Total Standard Deviation in ln(k): 6.148037567781896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 6.148037567781896""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 6.148037567781896
""",
)

entry(
    index = 31,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_N-Sp-3Xo-1R!H",
    kinetics = SurfaceArrheniusBM(A=(1.16208e+17,'m^2/(mol*s)'), n=0, w0=(390740,'J/mol'), E0=(137617,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_N-Sp-3Xo-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_N-Sp-3Xo-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_N-Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_N-Sp-3Xo-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_Sp-6R!H-2R",
    kinetics = SurfaceArrheniusBM(A=(3.55976e+17,'m^2/(mol*s)'), n=0.0733274, w0=(376367,'J/mol'), E0=(19888.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_Sp-6R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_Sp-6R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_Sp-6R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_Sp-6R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_N-Sp-6R!H-2R",
    kinetics = SurfaceArrheniusBM(A=(1.53323e+15,'m^2/(mol*s)'), n=0.796924, w0=(376367,'J/mol'), E0=(27386.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_N-Sp-6R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_N-Sp-6R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_N-Sp-6R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_Ext-2R-R_N-Sp-6R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O",
    kinetics = SurfaceArrheniusBM(A=(6.39043e-49,'m^2/(mol*s)'), n=19.4081, w0=(442409,'J/mol'), E0=(-73771.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.50262240353867, var=28.189497938013286, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O
    Total Standard Deviation in ln(k): 26.982144163276075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O
Total Standard Deviation in ln(k): 26.982144163276075""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O
Total Standard Deviation in ln(k): 26.982144163276075
""",
)

entry(
    index = 35,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_N-2HO->O",
    kinetics = SurfaceArrheniusBM(A=(7.91246e+10,'m^2/(mol*s)'), n=1.63398, w0=(470829,'J/mol'), E0=(-18769.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.17692755167948, var=14.695192344116979, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_N-2HO->O',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_N-2HO->O
    Total Standard Deviation in ln(k): 18.179806203784224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_N-2HO->O
Total Standard Deviation in ln(k): 18.179806203784224""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_N-2HO->O
Total Standard Deviation in ln(k): 18.179806203784224
""",
)

entry(
    index = 36,
    label = "Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C",
    kinetics = SurfaceArrheniusBM(A=(1.56711e+65,'m^2/(mol*s)'), n=-14.1479, w0=(268529,'J/mol'), E0=(235159,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6994128854333748, var=48.825549016360085, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C',), comment="""BM rule fitted to 13 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C
    Total Standard Deviation in ln(k): 15.765461503733503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C
Total Standard Deviation in ln(k): 15.765461503733503""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C
Total Standard Deviation in ln(k): 15.765461503733503
""",
)

entry(
    index = 37,
    label = "Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C",
    kinetics = SurfaceArrheniusBM(A=(1.5145e-09,'m^2/(mol*s)'), n=7.50797, w0=(357086,'J/mol'), E0=(72564.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9460730470145949, var=16.408062204428354, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C',), comment="""BM rule fitted to 8 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C
    Total Standard Deviation in ln(k): 10.497621539431204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C
Total Standard Deviation in ln(k): 10.497621539431204""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C
Total Standard Deviation in ln(k): 10.497621539431204
""",
)

entry(
    index = 38,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C",
    kinetics = SurfaceArrheniusBM(A=(1.01754e+10,'m^2/(mol*s)'), n=2.14464, w0=(384934,'J/mol'), E0=(136354,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4719292706445465, var=66.51482295697618, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 17.535693663778755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C
Total Standard Deviation in ln(k): 17.535693663778755""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C
Total Standard Deviation in ln(k): 17.535693663778755
""",
)

entry(
    index = 39,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C",
    kinetics = SurfaceArrheniusBM(A=(1.14766e+20,'m^2/(mol*s)'), n=-0.937764, w0=(327421,'J/mol'), E0=(190091,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03447456366908308, var=2.6927947972202007, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 3.376337113280562"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 3.376337113280562""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 3.376337113280562
""",
)

entry(
    index = 40,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet211",
    kinetics = SurfaceArrheniusBM(A=(2.32699e+20,'m^2/(mol*s)'), n=-0.927007, w0=(313758,'J/mol'), E0=(178253,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.026863200015417785, var=26.977486748917624, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet211',), comment="""BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet211
    Total Standard Deviation in ln(k): 10.480060666051736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet211
Total Standard Deviation in ln(k): 10.480060666051736""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet211
Total Standard Deviation in ln(k): 10.480060666051736
""",
)

entry(
    index = 41,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet111",
    kinetics = SurfaceArrheniusBM(A=(8.56951e+21,'m^2/(mol*s)'), n=-1.38946, w0=(311604,'J/mol'), E0=(142493,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05534014901662765, var=12.006756638767104, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet111',), comment="""BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet111
    Total Standard Deviation in ln(k): 7.0856064363681766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet111
Total Standard Deviation in ln(k): 7.0856064363681766""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_N-Sp-3Xo-1R!H_facet111
Total Standard Deviation in ln(k): 7.0856064363681766
""",
)

entry(
    index = 42,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N",
    kinetics = SurfaceArrheniusBM(A=(8.04592e-35,'m^2/(mol*s)'), n=15.0301, w0=(408038,'J/mol'), E0=(32603.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6307697073843109, var=43.59009075306925, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N',), comment="""BM rule fitted to 19 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N
    Total Standard Deviation in ln(k): 14.820669231968536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N
Total Standard Deviation in ln(k): 14.820669231968536""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N
Total Standard Deviation in ln(k): 14.820669231968536
""",
)

entry(
    index = 43,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N",
    kinetics = SurfaceArrheniusBM(A=(4.63738e+12,'m^2/(mol*s)'), n=1.19639, w0=(359226,'J/mol'), E0=(146962,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05270916432382204, var=67.48125246288559, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N',), comment="""BM rule fitted to 19 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N
    Total Standard Deviation in ln(k): 16.600727003076706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N
Total Standard Deviation in ln(k): 16.600727003076706""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N
Total Standard Deviation in ln(k): 16.600727003076706
""",
)

entry(
    index = 44,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N",
    kinetics = SurfaceArrheniusBM(A=(4.43941e+45,'m^2/(mol*s)'), n=-8.41388, w0=(342116,'J/mol'), E0=(192901,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3410679779844214, var=49.19252458685362, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N',), comment="""BM rule fitted to 8 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N
    Total Standard Deviation in ln(k): 14.917641861629903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N
Total Standard Deviation in ln(k): 14.917641861629903""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N
Total Standard Deviation in ln(k): 14.917641861629903
""",
)

entry(
    index = 45,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N",
    kinetics = SurfaceArrheniusBM(A=(2.21657e-26,'m^2/(mol*s)'), n=12.4647, w0=(422698,'J/mol'), E0=(12201.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.49294167929563565, var=35.953322128917016, Tref=1000.0, N=37, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N',), comment="""BM rule fitted to 37 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N
    Total Standard Deviation in ln(k): 13.259156804079756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 37 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N
Total Standard Deviation in ln(k): 13.259156804079756""",
    longDesc = 
"""
BM rule fitted to 37 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N
Total Standard Deviation in ln(k): 13.259156804079756
""",
)

entry(
    index = 46,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet111",
    kinetics = SurfaceArrheniusBM(A=(9.84829e+57,'m^2/(mol*s)'), n=-12.1976, w0=(472347,'J/mol'), E0=(173529,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6336597471000702, var=34.88292255019425, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet111',), comment="""BM rule fitted to 27 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet111
    Total Standard Deviation in ln(k): 13.432429408860344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet111
Total Standard Deviation in ln(k): 13.432429408860344""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet111
Total Standard Deviation in ln(k): 13.432429408860344
""",
)

entry(
    index = 47,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet001",
    kinetics = SurfaceArrheniusBM(A=(1.2297e+16,'m^2/(mol*s)'), n=0, w0=(497435,'J/mol'), E0=(48679.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet001',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet001
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet001
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_Sp-3Xo-1R!H_facet001
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet111",
    kinetics = SurfaceArrheniusBM(A=(1.75143e+272,'m^2/(mol*s)'), n=-75.3759, w0=(394849,'J/mol'), E0=(586924,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.113927712613465, var=24.72820738471334, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet111',), comment="""BM rule fitted to 28 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet111
    Total Standard Deviation in ln(k): 20.305541055735777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet111
Total Standard Deviation in ln(k): 20.305541055735777""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet111
Total Standard Deviation in ln(k): 20.305541055735777
""",
)

entry(
    index = 49,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet001",
    kinetics = SurfaceArrheniusBM(A=(14903.4,'m^2/(mol*s)'), n=3.8572, w0=(425071,'J/mol'), E0=(3772.63,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.042853798327232774, var=3.0900685762470905, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet001',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet001
    Total Standard Deviation in ln(k): 3.631714636649247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet001
Total Standard Deviation in ln(k): 3.631714636649247""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_5R!H->C_N-Sp-3Xo-1R!H_facet001
Total Standard Deviation in ln(k): 3.631714636649247
""",
)

entry(
    index = 50,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet211",
    kinetics = SurfaceArrheniusBM(A=(2.38102e+29,'m^2/(mol*s)'), n=-3.77531, w0=(471952,'J/mol'), E0=(98275.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18547639085810522, var=10.587574987864699, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet211',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet211
    Total Standard Deviation in ln(k): 6.989139147024395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet211
Total Standard Deviation in ln(k): 6.989139147024395""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet211
Total Standard Deviation in ln(k): 6.989139147024395
""",
)

entry(
    index = 51,
    label = "Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet111",
    kinetics = SurfaceArrheniusBM(A=(1.44689e+39,'m^2/(mol*s)'), n=-6.56353, w0=(467881,'J/mol'), E0=(118002,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.297002257711145, var=9.482770901709403, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet111',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet111
    Total Standard Deviation in ln(k): 6.919639685529385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet111
Total Standard Deviation in ln(k): 6.919639685529385""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_Sp-5R!H-1R!H_N-5R!H->C_Sp-3Xo-1R!H_facet111
Total Standard Deviation in ln(k): 6.919639685529385
""",
)

entry(
    index = 52,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet211",
    kinetics = SurfaceArrheniusBM(A=(1.70395e-56,'m^2/(mol*s)'), n=21.6467, w0=(443572,'J/mol'), E0=(-34734.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.465379395446674, var=14.099382353536285, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet211',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet211
    Total Standard Deviation in ln(k): 23.77228051212761"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet211
Total Standard Deviation in ln(k): 23.77228051212761""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet211
Total Standard Deviation in ln(k): 23.77228051212761
""",
)

entry(
    index = 53,
    label = "Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet111",
    kinetics = SurfaceArrheniusBM(A=(1.09952e+17,'m^2/(mol*s)'), n=0, w0=(427156,'J/mol'), E0=(54005.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet111',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet111
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet111
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-Sp-5R!H-1R!H_N-2R->C_2HO->O_facet111
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet211",
    kinetics = SurfaceArrheniusBM(A=(2.0864e+48,'m^2/(mol*s)'), n=-9.15925, w0=(271767,'J/mol'), E0=(150963,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07752314507393739, var=28.964429647162707, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet211',), comment="""BM rule fitted to 6 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet211
    Total Standard Deviation in ln(k): 10.98398763959116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet211
Total Standard Deviation in ln(k): 10.98398763959116""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet211
Total Standard Deviation in ln(k): 10.98398763959116
""",
)

entry(
    index = 55,
    label = "Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet111",
    kinetics = SurfaceArrheniusBM(A=(2.33862e+97,'m^2/(mol*s)'), n=-23.6577, w0=(265754,'J/mol'), E0=(348155,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0347162039357691, var=21.056728430392727, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet111',), comment="""BM rule fitted to 7 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet111
    Total Standard Deviation in ln(k): 11.799039795534902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet111
Total Standard Deviation in ln(k): 11.799039795534902""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_2CH->C_facet111
Total Standard Deviation in ln(k): 11.799039795534902
""",
)

entry(
    index = 56,
    label = "Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet211",
    kinetics = SurfaceArrheniusBM(A=(2.54179e+16,'m^2/(mol*s)'), n=0, w0=(390365,'J/mol'), E0=(91547.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet211',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet211
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet211
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet211
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet111",
    kinetics = SurfaceArrheniusBM(A=(2.01071e+06,'m^2/(mol*s)'), n=3.03633, w0=(348730,'J/mol'), E0=(112759,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6436549588740802, var=11.325387499798081, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet111',), comment="""BM rule fitted to 6 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet111
    Total Standard Deviation in ln(k): 8.36380118573777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet111
Total Standard Deviation in ln(k): 8.36380118573777""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Sp-3Xo#1R!H_N-2R->O_N-2CHN->N_N-2CH->C_facet111
Total Standard Deviation in ln(k): 8.36380118573777
""",
)

entry(
    index = 58,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet211",
    kinetics = SurfaceArrheniusBM(A=(8.3846e+19,'m^2/(mol*s)'), n=-0.785077, w0=(388073,'J/mol'), E0=(126542,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01014512844372736, var=0.6450215888467409, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet211',), comment="""BM rule fitted to 5 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet211
    Total Standard Deviation in ln(k): 1.6355578878112242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet211
Total Standard Deviation in ln(k): 1.6355578878112242""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet211
Total Standard Deviation in ln(k): 1.6355578878112242
""",
)

entry(
    index = 59,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet111",
    kinetics = SurfaceArrheniusBM(A=(524.933,'m^2/(mol*s)'), n=4.29736, w0=(381010,'J/mol'), E0=(159353,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8329414587262665, var=186.3712193596614, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet111',), comment="""BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet111
    Total Standard Deviation in ln(k): 29.46102894212376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet111
Total Standard Deviation in ln(k): 29.46102894212376""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_1R!H->C_facet111
Total Standard Deviation in ln(k): 29.46102894212376
""",
)

entry(
    index = 60,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R",
    kinetics = SurfaceArrheniusBM(A=(9.53522e+18,'m^2/(mol*s)'), n=-0.366741, w0=(316198,'J/mol'), E0=(224764,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0024898490583958794, var=76.45236775478749, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 17.535066947621488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 17.535066947621488""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 17.535066947621488
""",
)

entry(
    index = 61,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet211",
    kinetics = SurfaceArrheniusBM(A=(2.77774e-14,'m^2/(mol*s)'), n=8.97487, w0=(403678,'J/mol'), E0=(88488.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5917350312055247, var=43.14800728653251, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet211',), comment="""BM rule fitted to 16 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet211
    Total Standard Deviation in ln(k): 14.655303364809086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet211
Total Standard Deviation in ln(k): 14.655303364809086""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet211
Total Standard Deviation in ln(k): 14.655303364809086
""",
)

entry(
    index = 62,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet111",
    kinetics = SurfaceArrheniusBM(A=(1.64942e+16,'m^2/(mol*s)'), n=0, w0=(427619,'J/mol'), E0=(93367.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet111',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet111
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet111
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet111
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet1",
    kinetics = SurfaceArrheniusBM(A=(1.64942e+16,'m^2/(mol*s)'), n=0, w0=(438632,'J/mol'), E0=(62808.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet1',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_Sp-3Xo-1N_facet1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet211",
    kinetics = SurfaceArrheniusBM(A=(8.50353e-13,'m^2/(mol*s)'), n=8.5161, w0=(355711,'J/mol'), E0=(81530.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5074913462846371, var=15.324722115509099, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet211',), comment="""BM rule fitted to 16 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet211
    Total Standard Deviation in ln(k): 9.123000867006265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet211
Total Standard Deviation in ln(k): 9.123000867006265""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet211
Total Standard Deviation in ln(k): 9.123000867006265
""",
)

entry(
    index = 65,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet111",
    kinetics = SurfaceArrheniusBM(A=(2.13171e+16,'m^2/(mol*s)'), n=0, w0=(364154,'J/mol'), E0=(381365,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet111',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet111
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet111
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet111
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet0001step",
    kinetics = SurfaceArrheniusBM(A=(2.13171e+16,'m^2/(mol*s)'), n=0, w0=(390389,'J/mol'), E0=(117770,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet0001step',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet0001step
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet0001step
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_1R!H->N_N-Sp-3Xo-1N_facet0001step
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_Sp-3Xo-1CO",
    kinetics = SurfaceArrheniusBM(A=(4.81217e+48,'m^2/(mol*s)'), n=-9.29827, w0=(378298,'J/mol'), E0=(154588,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3845701930091715, var=12.262833964437554, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_Sp-3Xo-1CO',), comment="""BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_Sp-3Xo-1CO
    Total Standard Deviation in ln(k): 7.9865041034366895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_Sp-3Xo-1CO
Total Standard Deviation in ln(k): 7.9865041034366895""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_Sp-3Xo-1CO
Total Standard Deviation in ln(k): 7.9865041034366895
""",
)

entry(
    index = 68,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_N-Sp-3Xo-1CO",
    kinetics = SurfaceArrheniusBM(A=(6.26622e+19,'m^2/(mol*s)'), n=-0.787521, w0=(305934,'J/mol'), E0=(183163,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0252922487607271, var=5.522038136574187, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_N-Sp-3Xo-1CO',), comment="""BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_N-Sp-3Xo-1CO
    Total Standard Deviation in ln(k): 4.774478788539029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_N-Sp-3Xo-1CO
Total Standard Deviation in ln(k): 4.774478788539029""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_2HNO->N_N-Sp-3Xo-1CO
Total Standard Deviation in ln(k): 4.774478788539029
""",
)

entry(
    index = 69,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C",
    kinetics = SurfaceArrheniusBM(A=(1.19571e-18,'m^2/(mol*s)'), n=10.1976, w0=(413580,'J/mol'), E0=(10461.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5350272059459763, var=31.400865825969806, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C',), comment="""BM rule fitted to 25 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C
    Total Standard Deviation in ln(k): 12.578118260100682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C
Total Standard Deviation in ln(k): 12.578118260100682""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C
Total Standard Deviation in ln(k): 12.578118260100682
""",
)

entry(
    index = 70,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C",
    kinetics = SurfaceArrheniusBM(A=(1.59511e+15,'m^2/(mol*s)'), n=0.363995, w0=(441692,'J/mol'), E0=(153100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.015610771378276506, var=4.938616633571274, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C
    Total Standard Deviation in ln(k): 4.4943455100750676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C
Total Standard Deviation in ln(k): 4.4943455100750676""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C
Total Standard Deviation in ln(k): 4.4943455100750676
""",
)

entry(
    index = 71,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_Sp-5R!H-2C",
    kinetics = SurfaceArrheniusBM(A=(1.864e+18,'m^2/(mol*s)'), n=0, w0=(316198,'J/mol'), E0=(206686,'J/mol'), Tmin=(298,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_Sp-5R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_Sp-5R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_Sp-5R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_Sp-5R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_N-Sp-5R!H-2C",
    kinetics = SurfaceArrheniusBM(A=(8.733e+16,'m^2/(mol*s)'), n=0, w0=(316198,'J/mol'), E0=(232671,'J/mol'), Tmin=(298,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_N-Sp-5R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_N-Sp-5R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_N-Sp-5R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_2R->C_Sp-3Xo-1R!H_N-1R!H->C_Ext-2C-R_N-Sp-5R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_2HO->O",
    kinetics = SurfaceArrheniusBM(A=(2.32149e+22,'m^2/(mol*s)'), n=-1.51575, w0=(366167,'J/mol'), E0=(98935.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03247112308398761, var=11.661658872364502, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_2HO->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_2HO->O
    Total Standard Deviation in ln(k): 6.927589854433306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_2HO->O
Total Standard Deviation in ln(k): 6.927589854433306""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_2HO->O
Total Standard Deviation in ln(k): 6.927589854433306
""",
)

entry(
    index = 74,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O",
    kinetics = SurfaceArrheniusBM(A=(2.66651e-20,'m^2/(mol*s)'), n=10.6104, w0=(428553,'J/mol'), E0=(-2130.14,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6119788454193801, var=29.834308185209128, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O',), comment="""BM rule fitted to 19 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O
    Total Standard Deviation in ln(k): 12.487656873887435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O
Total Standard Deviation in ln(k): 12.487656873887435""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O
Total Standard Deviation in ln(k): 12.487656873887435
""",
)

entry(
    index = 75,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet211",
    kinetics = SurfaceArrheniusBM(A=(3.51932e+13,'m^2/(mol*s)'), n=0.852458, w0=(443332,'J/mol'), E0=(141429,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04406299335321257, var=2.467022128534978, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet211',), comment="""BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet211
    Total Standard Deviation in ln(k): 3.259499692961258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet211
Total Standard Deviation in ln(k): 3.259499692961258""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet211
Total Standard Deviation in ln(k): 3.259499692961258
""",
)

entry(
    index = 76,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet111",
    kinetics = SurfaceArrheniusBM(A=(4.4697e+16,'m^2/(mol*s)'), n=-0.063298, w0=(435886,'J/mol'), E0=(168492,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005727277627589054, var=7.6715204332427565, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet111',), comment="""BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet111
    Total Standard Deviation in ln(k): 5.567007069067135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet111
Total Standard Deviation in ln(k): 5.567007069067135""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_N-1CO->C_facet111
Total Standard Deviation in ln(k): 5.567007069067135
""",
)

entry(
    index = 77,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C",
    kinetics = SurfaceArrheniusBM(A=(1.77743e-20,'m^2/(mol*s)'), n=10.6606, w0=(481549,'J/mol'), E0=(-293.437,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9905121946422896, var=21.732111173630404, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C
    Total Standard Deviation in ln(k): 11.834340451859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C
Total Standard Deviation in ln(k): 11.834340451859""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C
Total Standard Deviation in ln(k): 11.834340451859
""",
)

entry(
    index = 78,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C",
    kinetics = SurfaceArrheniusBM(A=(3.53039e-20,'m^2/(mol*s)'), n=10.5803, w0=(404093,'J/mol'), E0=(-9694.56,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.919500347981324, var=42.2850085702528, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C',), comment="""BM rule fitted to 13 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C
    Total Standard Deviation in ln(k): 17.859040766405183"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C
Total Standard Deviation in ln(k): 17.859040766405183""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C
Total Standard Deviation in ln(k): 17.859040766405183
""",
)

entry(
    index = 79,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet211",
    kinetics = SurfaceArrheniusBM(A=(1.14543e+16,'m^2/(mol*s)'), n=0, w0=(501939,'J/mol'), E0=(102144,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet211',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet211
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet211
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet211
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet111",
    kinetics = SurfaceArrheniusBM(A=(1.04704e-17,'m^2/(mol*s)'), n=9.87164, w0=(474408,'J/mol'), E0=(-20058.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.633981389472654, var=26.37424699141001, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet111',), comment="""BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet111
    Total Standard Deviation in ln(k): 14.400970944328558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet111
Total Standard Deviation in ln(k): 14.400970944328558""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_Sp-3Xo-1C_facet111
Total Standard Deviation in ln(k): 14.400970944328558
""",
)

entry(
    index = 81,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet211",
    kinetics = SurfaceArrheniusBM(A=(3.0744e+25,'m^2/(mol*s)'), n=-2.67508, w0=(401464,'J/mol'), E0=(155463,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13636370436974846, var=44.702051605875106, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet211',), comment="""BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet211
    Total Standard Deviation in ln(k): 13.746199484232868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet211
Total Standard Deviation in ln(k): 13.746199484232868""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet211
Total Standard Deviation in ln(k): 13.746199484232868
""",
)

entry(
    index = 82,
    label = "Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet111",
    kinetics = SurfaceArrheniusBM(A=(6.29061e-32,'m^2/(mol*s)'), n=14.1254, w0=(404511,'J/mol'), E0=(-129428,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.228890362246813, var=49.1105754639089, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet111',), comment="""BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet111
    Total Standard Deviation in ln(k): 27.186885995655178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet111
Total Standard Deviation in ln(k): 27.186885995655178""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-Sp-3Xo#1R!H_N-2R->C_N-1R!H->N_N-2HNO->N_1CO->C_N-2HO->O_N-Sp-3Xo-1C_facet111
Total Standard Deviation in ln(k): 27.186885995655178
""",
)

