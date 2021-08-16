#!/usr/bin/env python
# encoding: utf-8

name = "Birad_recombination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.25413e+07,'s^-1'), n=1.20046, w0=(161000,'J/mol'), E0=(16100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07426102205682039, var=5.843756410023497, Tref=1000.0, N=5, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 5 training reactions at node Root
    Total Standard Deviation in ln(k): 5.032804546753876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 5.032804546753876""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 5.032804546753876
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(8.69088e+06,'s^-1'), n=1.2163, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03637485531705508, var=0.9131482536096801, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 2.0070947114127926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 2.0070947114127926""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 2.0070947114127926
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(2.18e+16,'s^-1'), n=0, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+12,'s^-1'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(550,'K'), Tmax=(650,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.91273e+06,'s^-1'), n=1.38112, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9611482244452804, var=0.025199359283703242, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.733183069397409"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.733183069397409""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.733183069397409
""",
)

entry(
    index = 6,
    label = "Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.21e+10,'s^-1'), n=0.137, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

