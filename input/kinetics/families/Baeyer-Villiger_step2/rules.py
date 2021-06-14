#!/usr/bin/env python
# encoding: utf-8

name = "Baeyer-Villiger_step2/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1493.34,'s^-1'), n=2.77783, w0=(1.5435e+06,'J/mol'), E0=(155908,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017957832601807906, var=13.798034157896952, Tref=1000.0, N=2, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 7.491850003971119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.491850003971119""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.491850003971119
""",
)

entry(
    index = 2,
    label = "Root_1C-inRing",
    kinetics = ArrheniusBM(A=(7.6032e+10,'s^-1'), n=0.572241, w0=(1.5435e+06,'J/mol'), E0=(166559,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-1C-inRing",
    kinetics = ArrheniusBM(A=(8.47125e+10,'s^-1'), n=0.82328, w0=(1.5435e+06,'J/mol'), E0=(205933,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

