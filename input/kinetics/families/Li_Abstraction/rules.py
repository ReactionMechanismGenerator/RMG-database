#!/usr/bin/env python
# encoding: utf-8

name = "Li_Abstraction/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.83608e+11,'m^3/(mol*s)'), n=-0.510924, w0=(464500,'J/mol'), E0=(75534.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07018974762276049, var=13.57503199120961, Tref=1000.0, N=2, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 7.562664269461141"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.562664269461141""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.562664269461141
""",
)

entry(
    index = 2,
    label = "Root_2ClF->F",
    kinetics = ArrheniusBM(A=(67.2982,'m^3/(mol*s)'), n=2.43284, w0=(531000,'J/mol'), E0=(69102.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_2ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-2ClF->F",
    kinetics = ArrheniusBM(A=(1092.65,'m^3/(mol*s)'), n=1.96179, w0=(398000,'J/mol'), E0=(28572.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

