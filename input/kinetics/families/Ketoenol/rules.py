#!/usr/bin/env python
# encoding: utf-8

name = "Ketoenol/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.66144e-20,'s^-1'), n=9.44259, w0=(790.871,'kJ/mol'), E0=(129.245,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.42082124841163465, var=31.884777160249236, Tref=1000.0, N=101, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 101 training reactions at node Root
    Total Standard Deviation in ln(k): 12.377398613194291"""),
    rank = 11,
    shortDesc = """BM rule fitted to 101 training reactions at node Root
Total Standard Deviation in ln(k): 12.377398613194291""",
    longDesc = 
"""
BM rule fitted to 101 training reactions at node Root
Total Standard Deviation in ln(k): 12.377398613194291
""",
)

entry(
    index = 2,
    label = "Root_3R!H->C",
    kinetics = ArrheniusBM(A=(2.3084e-31,'s^-1'), n=12.6704, w0=(783.702,'kJ/mol'), E0=(138.626,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5451476429702559, var=7.43114449324685, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_3R!H->C',), comment="""BM rule fitted to 47 training reactions at node Root_3R!H->C
    Total Standard Deviation in ln(k): 6.834650702226058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_3R!H->C
Total Standard Deviation in ln(k): 6.834650702226058""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_3R!H->C
Total Standard Deviation in ln(k): 6.834650702226058
""",
)

entry(
    index = 3,
    label = "Root_N-3R!H->C",
    kinetics = ArrheniusBM(A=(1.32057e-11,'s^-1'), n=6.97482, w0=(797.111,'kJ/mol'), E0=(118.697,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28685644868198745, var=16.80306068131882, Tref=1000.0, N=54, data_mean=0.0, correlation='Root_N-3R!H->C',), comment="""BM rule fitted to 54 training reactions at node Root_N-3R!H->C
    Total Standard Deviation in ln(k): 8.938461964278968"""),
    rank = 11,
    shortDesc = """BM rule fitted to 54 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 8.938461964278968""",
    longDesc = 
"""
BM rule fitted to 54 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 8.938461964278968
""",
)

entry(
    index = 4,
    label = "Root_3R!H->C_3C-inRing",
    kinetics = ArrheniusBM(A=(1.05189e-20,'s^-1'), n=9.49865, w0=(783.5,'kJ/mol'), E0=(145.117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.43664435292974063, var=2.6706379695704463, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing',), comment="""BM rule fitted to 13 training reactions at node Root_3R!H->C_3C-inRing
    Total Standard Deviation in ln(k): 4.373251804055378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_3R!H->C_3C-inRing
Total Standard Deviation in ln(k): 4.373251804055378""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_3R!H->C_3C-inRing
Total Standard Deviation in ln(k): 4.373251804055378
""",
)

entry(
    index = 5,
    label = "Root_3R!H->C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.76267e-36,'s^-1'), n=14.186, w0=(783.779,'kJ/mol'), E0=(134.305,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5716791226502428, var=7.37993894144457, Tref=1000.0, N=34, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing',), comment="""BM rule fitted to 34 training reactions at node Root_3R!H->C_N-3C-inRing
    Total Standard Deviation in ln(k): 6.882451643648476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root_3R!H->C_N-3C-inRing
Total Standard Deviation in ln(k): 6.882451643648476""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root_3R!H->C_N-3C-inRing
Total Standard Deviation in ln(k): 6.882451643648476
""",
)

entry(
    index = 6,
    label = "Root_N-3R!H->C_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.64692e-16,'s^-1'), n=8.38243, w0=(798,'kJ/mol'), E0=(133.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3120112477209778, var=14.331975556820195, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing',), comment="""BM rule fitted to 23 training reactions at node Root_N-3R!H->C_1R!H-inRing
    Total Standard Deviation in ln(k): 8.37339287241503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-3R!H->C_1R!H-inRing
Total Standard Deviation in ln(k): 8.37339287241503""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-3R!H->C_1R!H-inRing
Total Standard Deviation in ln(k): 8.37339287241503
""",
)

entry(
    index = 7,
    label = "Root_N-3R!H->C_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(3.74447e-12,'s^-1'), n=7.12963, w0=(796.452,'kJ/mol'), E0=(95.0704,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13927012845721087, var=1.7610428599317072, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing',), comment="""BM rule fitted to 31 training reactions at node Root_N-3R!H->C_N-1R!H-inRing
    Total Standard Deviation in ln(k): 3.0102943978356604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-3R!H->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 3.0102943978356604""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-3R!H->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 3.0102943978356604
""",
)

entry(
    index = 8,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.19466e-12,'s^-1'), n=7.00785, w0=(783.5,'kJ/mol'), E0=(152.801,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3027098685454321, var=3.2576700595765544, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R
    Total Standard Deviation in ln(k): 4.378927260033542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.378927260033542""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.378927260033542
""",
)

entry(
    index = 9,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(7.42914e-29,'s^-1'), n=11.8348, w0=(783.5,'kJ/mol'), E0=(117.871,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7121819508346441, var=0.027051696850322902, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O
    Total Standard Deviation in ln(k): 2.1191286847009194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O
Total Standard Deviation in ln(k): 2.1191286847009194""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O
Total Standard Deviation in ln(k): 2.1191286847009194
""",
)

entry(
    index = 10,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(9.42267e-25,'s^-1'), n=10.6927, w0=(783.5,'kJ/mol'), E0=(144.823,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3888954266868317, var=1.1180953874237196, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 3.096931653261236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.096931653261236""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.096931653261236
""",
)

entry(
    index = 11,
    label = "Root_3R!H->C_N-3C-inRing_1R!H->N",
    kinetics = Arrhenius(A=(9.27692e-54,'s^-1'), n=19.1913, Ea=(180.189,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N",
    kinetics = ArrheniusBM(A=(1.83026e-35,'s^-1'), n=13.8929, w0=(783.5,'kJ/mol'), E0=(135.079,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6006347301670059, var=6.33401302729255, Tref=1000.0, N=33, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N',), comment="""BM rule fitted to 33 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N
    Total Standard Deviation in ln(k): 6.554542509986668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N
Total Standard Deviation in ln(k): 6.554542509986668""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N
Total Standard Deviation in ln(k): 6.554542509986668
""",
)

entry(
    index = 13,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(4.25655e-17,'s^-1'), n=8.55114, w0=(798,'kJ/mol'), E0=(115.664,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26497173988350653, var=2.8328248394369915, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 4.039927290265277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 4.039927290265277""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 4.039927290265277
""",
)

entry(
    index = 14,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(4.41855e-16,'s^-1'), n=8.25908, w0=(798,'kJ/mol'), E0=(160.956,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3684904749387331, var=17.08330980202511, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 9.211818619820768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 9.211818619820768""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 9.211818619820768
""",
)

entry(
    index = 15,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N",
    kinetics = ArrheniusBM(A=(4.96183e-12,'s^-1'), n=7.09618, w0=(798,'kJ/mol'), E0=(96.1995,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15307161695431326, var=1.2733270190534556, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N',), comment="""BM rule fitted to 28 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N
    Total Standard Deviation in ln(k): 2.646781053824308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N
Total Standard Deviation in ln(k): 2.646781053824308""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N
Total Standard Deviation in ln(k): 2.646781053824308
""",
)

entry(
    index = 16,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N",
    kinetics = ArrheniusBM(A=(77.3565,'s^-1'), n=3.23425, w0=(782,'kJ/mol'), E0=(87.0046,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13848273159863436, var=0.26567923460444265, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N
    Total Standard Deviation in ln(k): 1.381268845583612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N
Total Standard Deviation in ln(k): 1.381268845583612""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N
Total Standard Deviation in ln(k): 1.381268845583612
""",
)

entry(
    index = 17,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.77843e-16,'s^-1'), n=8.2772, w0=(783.5,'kJ/mol'), E0=(145.929,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3153974027524752, var=5.711578914209146, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 5.583554072081672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 5.583554072081672""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 5.583554072081672
""",
)

entry(
    index = 18,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C",
    kinetics = Arrhenius(A=(0.0332916,'s^-1'), n=3.98637, Ea=(105.771,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(5.66974e-32,'s^-1'), n=12.7337, Ea=(112.625,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.04678e-24,'s^-1'), n=10.5829, w0=(783.5,'kJ/mol'), E0=(143.977,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3609578400335502, var=1.7320200602820202, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.5452855662259184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.5452855662259184""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.5452855662259184
""",
)

entry(
    index = 21,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFILiNPSSi->N",
    kinetics = Arrhenius(A=(7.8149e-27,'s^-1'), n=11.304, Ea=(126.826,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFILiNPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFILiNPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFILiNPSSi->N",
    kinetics = Arrhenius(A=(2.16654e-24,'s^-1'), n=10.6408, Ea=(128.297,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFILiNPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFILiNPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.71689e-38,'s^-1'), n=14.6893, w0=(783.5,'kJ/mol'), E0=(131.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.608931793765921, var=6.550811155219054, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R',), comment="""BM rule fitted to 17 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R
    Total Standard Deviation in ln(k): 6.661009091583746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R
Total Standard Deviation in ln(k): 6.661009091583746""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R
Total Standard Deviation in ln(k): 6.661009091583746
""",
)

entry(
    index = 24,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.46771e-32,'s^-1'), n=12.9236, w0=(783.5,'kJ/mol'), E0=(138.194,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.579303393007679, var=6.426836388563327, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R',), comment="""BM rule fitted to 13 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R
    Total Standard Deviation in ln(k): 6.537781328701153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 6.537781328701153""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 6.537781328701153
""",
)

entry(
    index = 25,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N",
    kinetics = ArrheniusBM(A=(6.87594e-16,'s^-1'), n=8.19782, w0=(798,'kJ/mol'), E0=(118.768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26775554630835335, var=5.678901573969646, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N
    Total Standard Deviation in ln(k): 5.450125733055174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N
Total Standard Deviation in ln(k): 5.450125733055174""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N
Total Standard Deviation in ln(k): 5.450125733055174
""",
)

entry(
    index = 26,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N",
    kinetics = ArrheniusBM(A=(2.68076e-18,'s^-1'), n=8.90232, w0=(798,'kJ/mol'), E0=(112.603,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26007770451495216, var=1.4284320621695705, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N
    Total Standard Deviation in ln(k): 3.0494614065620866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N
Total Standard Deviation in ln(k): 3.0494614065620866""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N
Total Standard Deviation in ln(k): 3.0494614065620866
""",
)

entry(
    index = 27,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.10041e-13,'s^-1'), n=7.58065, w0=(798,'kJ/mol'), E0=(150.142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.39472961419903213, var=24.68364768458551, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 10.951836167877357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 10.951836167877357""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 10.951836167877357
""",
)

entry(
    index = 28,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(9.41153e-18,'s^-1'), n=8.73151, w0=(798,'kJ/mol'), E0=(170.209,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3466563791421085, var=13.505788535269113, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 8.238441941528142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 8.238441941528142""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 8.238441941528142
""",
)

entry(
    index = 29,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.87753e-13,'s^-1'), n=7.31742, w0=(798,'kJ/mol'), E0=(93.7684,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13947827414530364, var=1.732222840093259, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.9889586858749864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.9889586858749864""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.9889586858749864
""",
)

entry(
    index = 30,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.06569e-10,'s^-1'), n=6.49948, w0=(798,'kJ/mol'), E0=(99.6749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.171130697091662, var=0.04582828135632844, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.8591411103810269"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.8591411103810269""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.8591411103810269
""",
)

entry(
    index = 31,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.56693e-11,'s^-1'), n=6.90276, w0=(798,'kJ/mol'), E0=(103.682,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17370254204968705, var=1.2256809330352676, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.655890279574646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.655890279574646""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.655890279574646
""",
)

entry(
    index = 32,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N",
    kinetics = Arrhenius(A=(3.10725e-11,'s^-1'), n=6.76455, Ea=(75.3833,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = Arrhenius(A=(6.36022e-11,'s^-1'), n=6.62861, Ea=(72.851,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(95.2155,'s^-1'), n=3.22023, w0=(782,'kJ/mol'), E0=(86.3901,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15818810030301317, var=0.007104353151065897, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.5664312954024191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.5664312954024191""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFILiNOPSSi->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.5664312954024191
""",
)

entry(
    index = 35,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N",
    kinetics = Arrhenius(A=(3.65781e-21,'s^-1'), n=9.63784, Ea=(120.135,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(4.12921e-14,'s^-1'), n=7.59046, w0=(783.5,'kJ/mol'), E0=(148.377,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4186476185084994, var=17.564099102818147, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N
    Total Standard Deviation in ln(k): 9.453631808423909"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N
Total Standard Deviation in ln(k): 9.453631808423909""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N
Total Standard Deviation in ln(k): 9.453631808423909
""",
)

entry(
    index = 37,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N",
    kinetics = ArrheniusBM(A=(1.09748e-20,'s^-1'), n=9.50762, w0=(783.5,'kJ/mol'), E0=(153.845,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18344124684717478, var=6.001232207361077, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N
    Total Standard Deviation in ln(k): 5.3719898761144185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 5.3719898761144185""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 5.3719898761144185
""",
)

entry(
    index = 38,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N",
    kinetics = ArrheniusBM(A=(7.65129e-27,'s^-1'), n=11.2828, w0=(783.5,'kJ/mol'), E0=(137.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48332540371865473, var=3.1335242806066415, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N',), comment="""BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N
    Total Standard Deviation in ln(k): 4.76312004179723"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 4.76312004179723""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 4.76312004179723
""",
)

entry(
    index = 39,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.05097e-34,'s^-1'), n=13.4716, w0=(783.5,'kJ/mol'), E0=(131.162,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6377866244487778, var=3.598088567826211, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 5.405186393406428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.405186393406428""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.405186393406428
""",
)

entry(
    index = 40,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.31869e-48,'s^-1'), n=17.5634, w0=(783.5,'kJ/mol'), E0=(123.935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5744425493374123, var=0.23238401046242738, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 2.409730085330826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.409730085330826""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.409730085330826
""",
)

entry(
    index = 41,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_7R!H->C",
    kinetics = Arrhenius(A=(1.00696e-46,'s^-1'), n=17.0834, Ea=(126.242,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.8966e-53,'s^-1'), n=19.0441, w0=(783.5,'kJ/mol'), E0=(130.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3885310001814153, var=4.937342150412215, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 5.430756117323642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 5.430756117323642""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-1C-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 5.430756117323642
""",
)

entry(
    index = 43,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.47365e-39,'s^-1'), n=14.9104, w0=(783.5,'kJ/mol'), E0=(130.1,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5240374819112659, var=2.413233441503237, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 4.430949920519061"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.430949920519061""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.430949920519061
""",
)

entry(
    index = 44,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.80328e-17,'s^-1'), n=8.51551, w0=(783.5,'kJ/mol'), E0=(130.77,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3566484201960663, var=5.49511490396765, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 5.595533651529699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.595533651529699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.595533651529699
""",
)

entry(
    index = 45,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_5R!H->N",
    kinetics = Arrhenius(A=(7.03103e-17,'s^-1'), n=8.43292, Ea=(153.029,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N",
    kinetics = ArrheniusBM(A=(7.74337e-18,'s^-1'), n=8.76417, w0=(798,'kJ/mol'), E0=(116.744,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2305065161378522, var=6.131966687891958, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N
    Total Standard Deviation in ln(k): 5.543449117482446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 5.543449117482446""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 5.543449117482446
""",
)

entry(
    index = 47,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.65974e-17,'s^-1'), n=8.67839, w0=(798,'kJ/mol'), E0=(118.477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37611232897758257, var=0.42205752128452007, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N
    Total Standard Deviation in ln(k): 2.247401125106147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N
Total Standard Deviation in ln(k): 2.247401125106147""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N
Total Standard Deviation in ln(k): 2.247401125106147
""",
)

entry(
    index = 48,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(6.95358e-20,'s^-1'), n=9.34941, w0=(798,'kJ/mol'), E0=(98.9016,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018663885511340926, var=1.5919151172207289, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N
    Total Standard Deviation in ln(k): 2.576290857089274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N
Total Standard Deviation in ln(k): 2.576290857089274""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N
Total Standard Deviation in ln(k): 2.576290857089274
""",
)

entry(
    index = 49,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->N",
    kinetics = Arrhenius(A=(1.18952e-19,'s^-1'), n=9.32392, Ea=(161.52,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N",
    kinetics = ArrheniusBM(A=(1.58517e-12,'s^-1'), n=7.23743, w0=(798,'kJ/mol'), E0=(142.089,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38693287712392593, var=25.36137769982915, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N
    Total Standard Deviation in ln(k): 11.068055269914632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N
Total Standard Deviation in ln(k): 11.068055269914632""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N
Total Standard Deviation in ln(k): 11.068055269914632
""",
)

entry(
    index = 51,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C",
    kinetics = Arrhenius(A=(6.87223e-13,'s^-1'), n=7.30388, Ea=(159.322,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.39307e-19,'s^-1'), n=9.02682, w0=(798,'kJ/mol'), E0=(166.849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5034501295008034, var=20.427458241860435, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 10.325700228143324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 10.325700228143324""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 10.325700228143324
""",
)

entry(
    index = 53,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R",
    kinetics = ArrheniusBM(A=(2.17002e-09,'s^-1'), n=6.35356, w0=(798,'kJ/mol'), E0=(87.8174,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3299093010727894, var=1.7004265134395142, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R
    Total Standard Deviation in ln(k): 3.4431004643426757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R
Total Standard Deviation in ln(k): 3.4431004643426757""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R
Total Standard Deviation in ln(k): 3.4431004643426757
""",
)

entry(
    index = 54,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.089e-11,'s^-1'), n=7.03228, w0=(798,'kJ/mol'), E0=(81.9883,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.604637074529278, var=2.2310331805474815, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O
    Total Standard Deviation in ln(k): 4.513589939115949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O
Total Standard Deviation in ln(k): 4.513589939115949""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O
Total Standard Deviation in ln(k): 4.513589939115949
""",
)

entry(
    index = 55,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.26823e-12,'s^-1'), n=7.26732, w0=(798,'kJ/mol'), E0=(99.7679,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04671371521454639, var=0.7054615338499556, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O
    Total Standard Deviation in ln(k): 1.8011833697377924"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.8011833697377924""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.8011833697377924
""",
)

entry(
    index = 56,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->N",
    kinetics = Arrhenius(A=(6.24893e-09,'s^-1'), n=6.18216, Ea=(82.1219,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(3.28386e-10,'s^-1'), n=6.61019, w0=(798,'kJ/mol'), E0=(99.3004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17686561857823532, var=0.0662026337066262, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 0.9602017550022814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 0.9602017550022814""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 0.9602017550022814
""",
)

entry(
    index = 58,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.44829e-11,'s^-1'), n=6.97848, w0=(798,'kJ/mol'), E0=(100.595,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18924972389578626, var=1.086636116288838, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 2.5652745464328706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 2.5652745464328706""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 2.5652745464328706
""",
)

entry(
    index = 59,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = Arrhenius(A=(6.42858e-10,'s^-1'), n=6.4885, Ea=(88.6777,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFILiOPSSi->O",
    kinetics = Arrhenius(A=(8.47848e-14,'s^-1'), n=7.46671, Ea=(127.454,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFILiOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFILiOPSSi->O",
    kinetics = Arrhenius(A=(6.84389e-11,'s^-1'), n=6.70227, Ea=(141.395,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFILiOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N_Ext-6R!H-R",
    kinetics = Arrhenius(A=(1.77862e-15,'s^-1'), n=8.01018, Ea=(145.434,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_5BrCClFILiNPSSi->N_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C",
    kinetics = ArrheniusBM(A=(7.75193e-29,'s^-1'), n=11.8591, w0=(783.5,'kJ/mol'), E0=(131.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4449969630574862, var=10.34025053777337, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C
    Total Standard Deviation in ln(k): 7.564561049102675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C
Total Standard Deviation in ln(k): 7.564561049102675""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C
Total Standard Deviation in ln(k): 7.564561049102675
""",
)

entry(
    index = 64,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_N-6R!H->C",
    kinetics = Arrhenius(A=(8.55896e-23,'s^-1'), n=10.1131, Ea=(126.084,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.90018e-31,'s^-1'), n=12.5819, w0=(783.5,'kJ/mol'), E0=(130.861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5810246875041711, var=2.5005452084811703, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.62997111643219"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.62997111643219""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.62997111643219
""",
)

entry(
    index = 66,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O",
    kinetics = ArrheniusBM(A=(5.83828e-30,'s^-1'), n=12.1991, w0=(783.5,'kJ/mol'), E0=(125.958,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8975768800906928, var=9.060499526323158, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O
    Total Standard Deviation in ln(k): 8.28960392042301"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O
Total Standard Deviation in ln(k): 8.28960392042301""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O
Total Standard Deviation in ln(k): 8.28960392042301
""",
)

entry(
    index = 67,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(8.36201e-39,'s^-1'), n=14.8452, w0=(783.5,'kJ/mol'), E0=(130.026,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5485000828707988, var=3.8762967953101297, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
    Total Standard Deviation in ln(k): 5.325126135022126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 5.325126135022126""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 5.325126135022126
""",
)

entry(
    index = 68,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing",
    kinetics = ArrheniusBM(A=(4.9568e-34,'s^-1'), n=13.4595, w0=(783.5,'kJ/mol'), E0=(121.425,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.534145506563827, var=2.288238203502116, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing
    Total Standard Deviation in ln(k): 4.374621590715536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing
Total Standard Deviation in ln(k): 4.374621590715536""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing
Total Standard Deviation in ln(k): 4.374621590715536
""",
)

entry(
    index = 69,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing",
    kinetics = ArrheniusBM(A=(5.05948e-40,'s^-1'), n=15.2997, w0=(783.5,'kJ/mol'), E0=(132.03,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5188730734320319, var=1.5228798589423929, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing',), comment="""BM rule fitted to 9 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing
    Total Standard Deviation in ln(k): 3.7776448825351117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing
Total Standard Deviation in ln(k): 3.7776448825351117""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing
Total Standard Deviation in ln(k): 3.7776448825351117
""",
)

entry(
    index = 70,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-5BrClFILiNOPSSi-R",
    kinetics = Arrhenius(A=(1.5544e-16,'s^-1'), n=8.25988, Ea=(88.0644,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-5BrClFILiNOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-5BrClFILiNOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-5BrClFILiNOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-5BrClFILiNOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_Ext-1R!H-R",
    kinetics = Arrhenius(A=(1.03729e-10,'s^-1'), n=6.68631, Ea=(102.806,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.18795e-17,'s^-1'), n=8.71475, w0=(798,'kJ/mol'), E0=(131.703,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.386014003492072, var=0.07690656524338871, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N
    Total Standard Deviation in ln(k): 1.525838223430887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N
Total Standard Deviation in ln(k): 1.525838223430887""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N
Total Standard Deviation in ln(k): 1.525838223430887
""",
)

entry(
    index = 73,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(3.60051e-20,'s^-1'), n=9.44468, w0=(798,'kJ/mol'), E0=(100.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08406166626072396, var=0.022276618893129242, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N
    Total Standard Deviation in ln(k): 0.5104240217208295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N
Total Standard Deviation in ln(k): 0.5104240217208295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N
Total Standard Deviation in ln(k): 0.5104240217208295
""",
)

entry(
    index = 74,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N",
    kinetics = ArrheniusBM(A=(1.17332e-17,'s^-1'), n=8.72352, w0=(798,'kJ/mol'), E0=(116.807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27691597563417586, var=0.1780932350794811, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N
    Total Standard Deviation in ln(k): 1.5417889212623794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N
Total Standard Deviation in ln(k): 1.5417889212623794""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N
Total Standard Deviation in ln(k): 1.5417889212623794
""",
)

entry(
    index = 75,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N",
    kinetics = ArrheniusBM(A=(2.51185e-17,'s^-1'), n=8.62551, w0=(798,'kJ/mol'), E0=(119.791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4450894425116584, var=0.9626994271798481, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N
    Total Standard Deviation in ln(k): 3.085306061310456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 3.085306061310456""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 3.085306061310456
""",
)

entry(
    index = 76,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N_Ext-5R!H-R",
    kinetics = Arrhenius(A=(5.23245e-20,'s^-1'), n=9.38178, Ea=(107.208,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_N-7R!H->N_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N",
    kinetics = ArrheniusBM(A=(1.60836e-18,'s^-1'), n=8.93383, w0=(798,'kJ/mol'), E0=(140.933,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40831231091152637, var=0.4432703118111877, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N
    Total Standard Deviation in ln(k): 2.3606338443833033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N
Total Standard Deviation in ln(k): 2.3606338443833033""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N
Total Standard Deviation in ln(k): 2.3606338443833033
""",
)

entry(
    index = 78,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_N-5R!H->N",
    kinetics = Arrhenius(A=(2.95366e-14,'s^-1'), n=7.77475, Ea=(152.142,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_N-5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_N-5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(2.39461e-19,'s^-1'), n=9.1953, w0=(798,'kJ/mol'), E0=(148.569,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16842189681778294, var=50.506329633065135, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 14.670382829396397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 14.670382829396397""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 14.670382829396397
""",
)

entry(
    index = 80,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.35299e-19,'s^-1'), n=9.20066, w0=(798,'kJ/mol'), E0=(182.1,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7738239106632889, var=8.716989547618939, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 7.863170952987401"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.863170952987401""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.863170952987401
""",
)

entry(
    index = 81,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.19422e-11,'s^-1'), n=6.64635, w0=(798,'kJ/mol'), E0=(78.2019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4966466265433182, var=6.655518301741122, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.419729781316641"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.419729781316641""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.419729781316641
""",
)

entry(
    index = 82,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(7.80609e-12,'s^-1'), n=7.13985, Ea=(64.5475,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing",
    kinetics = ArrheniusBM(A=(8.78864e-13,'s^-1'), n=7.36514, w0=(798,'kJ/mol'), E0=(99.6243,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02011049140849096, var=0.6463391142279901, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing
    Total Standard Deviation in ln(k): 1.6622400167848812"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing
Total Standard Deviation in ln(k): 1.6622400167848812""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing
Total Standard Deviation in ln(k): 1.6622400167848812
""",
)

entry(
    index = 84,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing",
    kinetics = ArrheniusBM(A=(2.14789e-12,'s^-1'), n=7.16914, w0=(798,'kJ/mol'), E0=(100.184,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06603337109309566, var=0.8553896062818201, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing
    Total Standard Deviation in ln(k): 2.0200378395534067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing
Total Standard Deviation in ln(k): 2.0200378395534067""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing
Total Standard Deviation in ln(k): 2.0200378395534067
""",
)

entry(
    index = 85,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_5R!H-inRing",
    kinetics = Arrhenius(A=(3.03926e-10,'s^-1'), n=6.64444, Ea=(82.2627,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.39632e-10,'s^-1'), n=6.59369, w0=(798,'kJ/mol'), E0=(97.8564,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17368958193793832, var=0.0258825890646434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_N-5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_N-5R!H-inRing
    Total Standard Deviation in ln(k): 0.7589291014914147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_N-5R!H-inRing
Total Standard Deviation in ln(k): 0.7589291014914147""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->N_N-5R!H-inRing
Total Standard Deviation in ln(k): 0.7589291014914147
""",
)

entry(
    index = 87,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H",
    kinetics = ArrheniusBM(A=(1.49875e-11,'s^-1'), n=6.98067, w0=(798,'kJ/mol'), E0=(97.8136,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2270589721169141, var=0.8214293451314088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H
    Total Standard Deviation in ln(k): 2.387446248315343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H
Total Standard Deviation in ln(k): 2.387446248315343""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H
Total Standard Deviation in ln(k): 2.387446248315343
""",
)

entry(
    index = 88,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H",
    kinetics = Arrhenius(A=(1.03652e-10,'s^-1'), n=6.72069, Ea=(82.5831,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_7R!H->N",
    kinetics = Arrhenius(A=(2.33301e-26,'s^-1'), n=11.129, Ea=(116.406,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_N-7R!H->N",
    kinetics = Arrhenius(A=(9.38708e-30,'s^-1'), n=12.1418, Ea=(114.989,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_N-7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_N-7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R_Ext-3C-R_N-5BrCClFILiNPSSi->N_6R!H->C_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(2.46192e-37,'s^-1'), n=14.4758, w0=(783.5,'kJ/mol'), E0=(116.558,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5982390054546733, var=14.560951148792562, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_Sp-6R!H#5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 9.152944448946496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 9.152944448946496""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 9.152944448946496
""",
)

entry(
    index = 92,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(3.15389e-23,'s^-1'), n=10.2555, w0=(783.5,'kJ/mol'), E0=(149.123,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6434530373974792, var=1.7066133640959524, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-Sp-6R!H#5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 4.235650214339361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 4.235650214339361""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 4.235650214339361
""",
)

entry(
    index = 93,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.30356e-39,'s^-1'), n=14.9991, w0=(783.5,'kJ/mol'), E0=(139.018,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41803148923870204, var=0.004087241298491071, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 1.1784961677922285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.1784961677922285""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.1784961677922285
""",
)

entry(
    index = 94,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H",
    kinetics = ArrheniusBM(A=(1.51146e-43,'s^-1'), n=16.1521, w0=(783.5,'kJ/mol'), E0=(117.84,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5423655726526208, var=31.71440328296875, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H
    Total Standard Deviation in ln(k): 12.652501916886925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H
Total Standard Deviation in ln(k): 12.652501916886925""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H
Total Standard Deviation in ln(k): 12.652501916886925
""",
)

entry(
    index = 95,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6CN-5R!H",
    kinetics = ArrheniusBM(A=(1.43791e-33,'s^-1'), n=13.3588, w0=(783.5,'kJ/mol'), E0=(133.431,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.680704723250762, var=2.4831316638494103, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6CN-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6CN-5R!H
    Total Standard Deviation in ln(k): 4.869366019707415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6CN-5R!H
Total Standard Deviation in ln(k): 4.869366019707415""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6CN-5R!H
Total Standard Deviation in ln(k): 4.869366019707415
""",
)

entry(
    index = 96,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N",
    kinetics = Arrhenius(A=(2.59344e-34,'s^-1'), n=13.552, Ea=(109.766,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N",
    kinetics = Arrhenius(A=(1.41171e-33,'s^-1'), n=13.3174, Ea=(105.78,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R",
    kinetics = ArrheniusBM(A=(4.10514e-41,'s^-1'), n=15.6119, w0=(783.5,'kJ/mol'), E0=(130.729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5250741157479571, var=1.3251686595093166, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R',), comment="""BM rule fitted to 8 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R
    Total Standard Deviation in ln(k): 3.6270519321416788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R
Total Standard Deviation in ln(k): 3.6270519321416788""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R
Total Standard Deviation in ln(k): 3.6270519321416788
""",
)

entry(
    index = 99,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.40384e-17,'s^-1'), n=8.69281, w0=(798,'kJ/mol'), E0=(131.543,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3859715448461029, var=0.24454103210736627, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R
    Total Standard Deviation in ln(k): 1.9611411020814284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 1.9611411020814284""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 1.9611411020814284
""",
)

entry(
    index = 100,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N_Ext-5C-R",
    kinetics = Arrhenius(A=(4.43945e-20,'s^-1'), n=9.41864, Ea=(117.984,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_N-7R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N_Ext-6CO-R",
    kinetics = Arrhenius(A=(1.19581e-17,'s^-1'), n=8.72753, Ea=(108.255,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N_Ext-6CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N_Ext-6CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N_Ext-6CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_5R!H->N_Ext-6CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R",
    kinetics = ArrheniusBM(A=(5.98187e-17,'s^-1'), n=8.51746, w0=(798,'kJ/mol'), E0=(123.885,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41808353790394814, var=0.5007224002219028, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R
    Total Standard Deviation in ln(k): 2.469046595537014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 2.469046595537014""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 2.469046595537014
""",
)

entry(
    index = 103,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N_Ext-1R!H-R",
    kinetics = Arrhenius(A=(3.57404e-19,'s^-1'), n=9.1193, Ea=(135.561,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->N_5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N",
    kinetics = Arrhenius(A=(2.52338e-22,'s^-1'), n=10.05, Ea=(150.418,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N",
    kinetics = Arrhenius(A=(1.62343e-20,'s^-1'), n=9.5285, Ea=(156.362,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFILiNNOOPSSi",
    kinetics = Arrhenius(A=(4.58562e-24,'s^-1'), n=10.6226, Ea=(173.215,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFILiNNOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFILiNNOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFILiNNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFILiNNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFILiNNOOPSSi",
    kinetics = Arrhenius(A=(2.02819e-14,'s^-1'), n=7.71417, Ea=(180.621,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFILiNNOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFILiNNOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFILiNNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFILiNNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N",
    kinetics = Arrhenius(A=(1.68509e-11,'s^-1'), n=6.88807, Ea=(73.4794,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N",
    kinetics = ArrheniusBM(A=(7.85383e-13,'s^-1'), n=7.40653, w0=(798,'kJ/mol'), E0=(99.3862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04427006012322049, var=0.5870520892722171, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N
    Total Standard Deviation in ln(k): 1.6472457819262154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N
Total Standard Deviation in ln(k): 1.6472457819262154""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N
Total Standard Deviation in ln(k): 1.6472457819262154
""",
)

entry(
    index = 110,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N",
    kinetics = ArrheniusBM(A=(7.31226e-09,'s^-1'), n=6.08076, w0=(798,'kJ/mol'), E0=(106.938,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12327352192631685, var=1.7586576315223457, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N
    Total Standard Deviation in ln(k): 2.9682996520950335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N
Total Standard Deviation in ln(k): 2.9682996520950335""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N
Total Standard Deviation in ln(k): 2.9682996520950335
""",
)

entry(
    index = 111,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N",
    kinetics = ArrheniusBM(A=(4.46521e-15,'s^-1'), n=8.01403, w0=(798,'kJ/mol'), E0=(95.6631,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.035939042278277766, var=0.7145775608455458, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N
    Total Standard Deviation in ln(k): 1.784955581174701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N
Total Standard Deviation in ln(k): 1.784955581174701""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N
Total Standard Deviation in ln(k): 1.784955581174701
""",
)

entry(
    index = 112,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_5R!H->N",
    kinetics = Arrhenius(A=(6.56099e-43,'s^-1'), n=15.9484, Ea=(111.981,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_N-5R!H->N",
    kinetics = Arrhenius(A=(7.84947e-45,'s^-1'), n=16.5411, Ea=(129.059,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_N-5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_N-5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6CN-5R!H_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.47427e-42,'s^-1'), n=16.1833, w0=(783.5,'kJ/mol'), E0=(143.49,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4730378725606841, var=0.6700473232323596, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 2.8295417008896226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 2.8295417008896226""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 2.8295417008896226
""",
)

entry(
    index = 115,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(3.07542e-40,'s^-1'), n=15.2436, w0=(783.5,'kJ/mol'), E0=(120.661,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5567176216114472, var=0.7622646904026281, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 3.1490775076307287"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 3.1490775076307287""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 3.1490775076307287
""",
)

entry(
    index = 116,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_8R!H->C",
    kinetics = Arrhenius(A=(2.18792e-17,'s^-1'), n=8.63308, Ea=(112.872,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(9.00746e-18,'s^-1'), n=8.75254, Ea=(115.264,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->N_N-5R!H->N_Ext-6N-R_7R!H->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C",
    kinetics = Arrhenius(A=(9.14825e-17,'s^-1'), n=8.45574, Ea=(104.82,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(4.10787e-17,'s^-1'), n=8.57309, Ea=(108.743,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFILiNOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->N_Ext-6CO-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(2.45856e-13,'s^-1'), n=7.55, w0=(798,'kJ/mol'), E0=(99.006,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.019929732451848023, var=3.379569158770093, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 3.735500391647633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 3.735500391647633""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 3.735500391647633
""",
)

entry(
    index = 121,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(1.88244e-12,'s^-1'), n=7.29881, w0=(798,'kJ/mol'), E0=(99.4538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07934940250714372, var=0.29471064401843994, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 1.2876860726382162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 1.2876860726382162""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 1.2876860726382162
""",
)

entry(
    index = 122,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R",
    kinetics = ArrheniusBM(A=(1.25882e-08,'s^-1'), n=5.98677, w0=(798,'kJ/mol'), E0=(105.747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13063985424424193, var=3.4346862886841327, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R
    Total Standard Deviation in ln(k): 4.0435976443843185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R
Total Standard Deviation in ln(k): 4.0435976443843185""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R
Total Standard Deviation in ln(k): 4.0435976443843185
""",
)

entry(
    index = 123,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(4.23706e-14,'s^-1'), n=7.73362, w0=(798,'kJ/mol'), E0=(101.148,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06866871584753206, var=1.8221240072793141, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 2.878647629493287"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 2.878647629493287""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 2.878647629493287
""",
)

entry(
    index = 124,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(7.23908e-15,'s^-1'), n=7.95432, w0=(798,'kJ/mol'), E0=(93.2086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05457556266824342, var=1.092181702731196, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 2.2322229895925934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 2.2322229895925934""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 2.2322229895925934
""",
)

entry(
    index = 125,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(7.44467e-42,'s^-1'), n=15.9932, w0=(783.5,'kJ/mol'), E0=(143.806,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4456943536155986, var=0.4924567119878702, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R
    Total Standard Deviation in ln(k): 2.5266631127525785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 2.5266631127525785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 2.5266631127525785
""",
)

entry(
    index = 126,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N",
    kinetics = Arrhenius(A=(2.74964e-45,'s^-1'), n=16.6685, Ea=(116.975,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N",
    kinetics = ArrheniusBM(A=(1.36212e-38,'s^-1'), n=14.7791, w0=(783.5,'kJ/mol'), E0=(124.384,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5809558156707739, var=1.2247524195115425, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N',), comment="""BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N
    Total Standard Deviation in ln(k): 3.6782988796469778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 3.6782988796469778""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 3.6782988796469778
""",
)

entry(
    index = 128,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R",
    kinetics = Arrhenius(A=(4.42405e-12,'s^-1'), n=7.19519, Ea=(76.6476,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N",
    kinetics = Arrhenius(A=(2.83728e-12,'s^-1'), n=7.25327, Ea=(73.9748,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N",
    kinetics = Arrhenius(A=(1.32223e-12,'s^-1'), n=7.33725, Ea=(69.6232,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.36653e-10,'s^-1'), n=6.34655, w0=(798,'kJ/mol'), E0=(102.475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07635581480856772, var=0.00016587361332813841, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.2176681509792649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.2176681509792649""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFILiNOPSSi->N_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_5CN->N_Ext-5N-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.2176681509792649
""",
)

entry(
    index = 132,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_Sp-6C-5C",
    kinetics = ArrheniusBM(A=(7.14936e-38,'s^-1'), n=14.6094, w0=(783.5,'kJ/mol'), E0=(127.608,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.799409849602967, var=11.767586207644909, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_Sp-6C-5C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_Sp-6C-5C
    Total Standard Deviation in ln(k): 13.910719365169818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_Sp-6C-5C
Total Standard Deviation in ln(k): 13.910719365169818""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_Sp-6C-5C
Total Standard Deviation in ln(k): 13.910719365169818
""",
)

entry(
    index = 133,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_N-Sp-6C-5C",
    kinetics = ArrheniusBM(A=(5.58728e-39,'s^-1'), n=14.8715, w0=(783.5,'kJ/mol'), E0=(122.702,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6661873888921138, var=4.034110256072837, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_N-Sp-6C-5C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_N-Sp-6C-5C
    Total Standard Deviation in ln(k): 5.700367030849721"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_N-Sp-6C-5C
Total Standard Deviation in ln(k): 5.700367030849721""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFILiNPSSi->N_N-Sp-6C-5C
Total Standard Deviation in ln(k): 5.700367030849721
""",
)

