#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Intra_Elimination_LiR/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.42031e+27,'s^-1'), n=-3.90391, w0=(741100,'J/mol'), E0=(69929.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16499692467391203, var=3.733835948653539, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 4 training reactions at node Root
    Total Standard Deviation in ln(k): 4.288342043643909"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 4.288342043643909""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 4.288342043643909
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R",
    kinetics = ArrheniusBM(A=(1.84651e+28,'s^-1'), n=-3.88359, w0=(741100,'J/mol'), E0=(78301.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23079195197825578, var=6.309766423662204, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R
    Total Standard Deviation in ln(k): 5.615623123573294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R
Total Standard Deviation in ln(k): 5.615623123573294""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R
Total Standard Deviation in ln(k): 5.615623123573294
""",
)

entry(
    index = 3,
    label = "Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.20531e+14,'s^-1'), n=0.219161, w0=(741100,'J/mol'), E0=(39190.5,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_2R!H-u0",
    kinetics = ArrheniusBM(A=(3.92231e+16,'s^-1'), n=-0.357468, w0=(741100,'J/mol'), E0=(73987.2,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_2R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_2R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_N-2R!H-u0",
    kinetics = ArrheniusBM(A=(2.28642e+17,'s^-1'), n=-0.785762, w0=(741100,'J/mol'), E0=(37715.9,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_N-2R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_N-2R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_N-2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R-R_N-2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

