#!/usr/bin/env python
# encoding: utf-8

name = "Cation_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusChargeTransferBM(A=(4.77752e+08,'m^3/(mol*s)'), n=0.196434, w0=(362933,'J/mol'), E0=(36293.3,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07422928322961901, var=9.529900931242484, Tref=1000.0, N=3, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 3 training reactions at node Root
    Total Standard Deviation in ln(k): 6.3752306998135735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 6.3752306998135735""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 6.3752306998135735
""",
)

entry(
    index = 2,
    label = "Root_1R!H->N",
    kinetics = ArrheniusChargeTransferBM(A=(16042,'m^3/(mol*s)'), n=1.52384, w0=(306200,'J/mol'), E0=(30620,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->N",
    kinetics = ArrheniusChargeTransferBM(A=(3.92132e+11,'m^3/(mol*s)'), n=-0.667361, w0=(391300,'J/mol'), E0=(39130,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.841226598634285, var=51.94290239962386, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->N
    Total Standard Deviation in ln(k): 19.074608775904846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->N
Total Standard Deviation in ln(k): 19.074608775904846""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->N
Total Standard Deviation in ln(k): 19.074608775904846
""",
)

entry(
    index = 4,
    label = "Root_N-1R!H->N_2R!H-inRing",
    kinetics = ArrheniusChargeTransferBM(A=(303.68,'m^3/(mol*s)'), n=1.59181, w0=(391300,'J/mol'), E0=(39130,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->N_2R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->N_2R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->N_2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->N_2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-1R!H->N_N-2R!H-inRing",
    kinetics = ArrheniusChargeTransferBM(A=(500060,'m^3/(mol*s)'), n=1.50675, w0=(391300,'J/mol'), E0=(39130,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->N_N-2R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->N_N-2R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->N_N-2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->N_N-2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

