#!/usr/bin/env python
# encoding: utf-8

name = "Bimolec_Hydroperoxide_Decomposition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(9.56168e+10,'m^3/(mol*s)'), n=-1.56082, w0=(530000,'J/mol'), E0=(84729.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05596479637465522, var=12.199334969367145, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 4 training reactions at node Root
    Total Standard Deviation in ln(k): 7.142662808121239"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 7.142662808121239""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 7.142662808121239
""",
)

entry(
    index = 2,
    label = "Root_5R-inRing",
    kinetics = ArrheniusBM(A=(2.512e+08,'m^3/(mol*s)'), n=0, w0=(530000,'J/mol'), E0=(98688.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_5R-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-5R-inRing",
    kinetics = ArrheniusBM(A=(2.40446e+15,'m^3/(mol*s)'), n=-3.07436, w0=(530000,'J/mol'), E0=(90571.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07273255958472015, var=8.341559373079228, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R-inRing
    Total Standard Deviation in ln(k): 5.972772433237581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R-inRing
Total Standard Deviation in ln(k): 5.972772433237581""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R-inRing
Total Standard Deviation in ln(k): 5.972772433237581
""",
)

entry(
    index = 4,
    label = "Root_N-5R-inRing_5R->C",
    kinetics = ArrheniusBM(A=(647863,'m^3/(mol*s)'), n=-0.422825, w0=(530000,'J/mol'), E0=(68850.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0677542868543719e-14, var=2.0856100788436827, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R-inRing_5R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R-inRing_5R->C
    Total Standard Deviation in ln(k): 2.8951665197877587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R-inRing_5R->C
Total Standard Deviation in ln(k): 2.8951665197877587""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R-inRing_5R->C
Total Standard Deviation in ln(k): 2.8951665197877587
""",
)

entry(
    index = 5,
    label = "Root_N-5R-inRing_N-5R->C",
    kinetics = ArrheniusBM(A=(1.7295e+06,'m^3/(mol*s)'), n=0, w0=(530000,'J/mol'), E0=(75670.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R-inRing_N-5R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R-inRing_N-5R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R-inRing_N-5R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R-inRing_N-5R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-5R-inRing_5R->C_Ext-7R-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(63100,'m^3/(mol*s)'), n=0, w0=(530000,'J/mol'), E0=(78414.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R-inRing_5R->C_Ext-7R-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R-inRing_5R->C_Ext-7R-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R-inRing_5R->C_Ext-7R-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R-inRing_5R->C_Ext-7R-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

