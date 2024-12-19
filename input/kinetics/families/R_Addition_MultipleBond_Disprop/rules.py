#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond_Disprop/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.78627e+16,'m^3/(mol*s)'), n=-2.90684, w0=(922900,'J/mol'), E0=(118657,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9871930555287386, var=2.843360384978805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 5.8608223168191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 5.8608223168191""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 5.8608223168191
""",
)

entry(
    index = 2,
    label = "Root_6R->C",
    kinetics = Arrhenius(A=(1.60363e+10,'m^3/(mol*s)'), n=-1.06749, Ea=(2.37772,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6R->C',), comment="""BM rule fitted to 1 training reactions at node Root_6R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-6R->C",
    kinetics = Arrhenius(A=(7.82969e+15,'m^3/(mol*s)'), n=-2.51461, Ea=(7.6717,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-6R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

