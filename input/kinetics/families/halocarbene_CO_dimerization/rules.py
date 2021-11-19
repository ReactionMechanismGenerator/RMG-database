#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_CO_dimerization/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.0167e+12,'s^-1'), n=0.69017, w0=(565500,'J/mol'), E0=(29646.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31104427838457743, var=1.5609888446572742, Tref=1000.0, N=3, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 3 training reactions at node Root
    Total Standard Deviation in ln(k): 3.2862250545585434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 3.2862250545585434""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 3.2862250545585434
""",
)

entry(
    index = 2,
    label = "RFC=C=O",
    kinetics = ArrheniusBM(A=(6.62099e+12,'s^-1'), n=0.640083, w0=(565500,'J/mol'), E0=(41536.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='RFC=C=O',), comment="""BM rule fitted to 1 training reactions at node RFC=C=O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node RFC=C=O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node RFC=C=O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "RClC=C=O",
    kinetics = ArrheniusBM(A=(6.43849e+12,'s^-1'), n=0.705824, w0=(565500,'J/mol'), E0=(78398.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='RClC=C=O',), comment="""BM rule fitted to 1 training reactions at node RClC=C=O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node RClC=C=O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node RClC=C=O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "RBrC=C=O",
    kinetics = ArrheniusBM(A=(7.3531e+12,'s^-1'), n=0.729529, w0=(565500,'J/mol'), E0=(56550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='RBrC=C=O',), comment="""BM rule fitted to 1 training reactions at node RBrC=C=O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node RBrC=C=O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node RBrC=C=O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

