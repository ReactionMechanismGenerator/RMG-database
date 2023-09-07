#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_CO_dimerization/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.7198e+11,'s^-1'), n=1.14926, w0=(565.5,'kJ/mol'), E0=(30.9354,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011316853405667404, var=1.7060578878139843, Tref=1000.0, N=3, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 3 training reactions at node Root
    Total Standard Deviation in ln(k): 2.6469420990431853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 2.6469420990431853""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 2.6469420990431853
""",
)

entry(
    index = 2,
    label = "RFC=C=O",
    kinetics = ArrheniusBM(A=(7.15699e+14,'s^-1'), n=0.0573689, w0=(565.5,'kJ/mol'), E0=(38.5982,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='RFC=C=O',), comment="""BM rule fitted to 1 training reactions at node RFC=C=O
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
    kinetics = ArrheniusBM(A=(6.43849e+12,'s^-1'), n=0.705824, w0=(565.5,'kJ/mol'), E0=(75.4297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='RClC=C=O',), comment="""BM rule fitted to 1 training reactions at node RClC=C=O
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
    kinetics = ArrheniusBM(A=(7.3531e+12,'s^-1'), n=0.729529, w0=(565.5,'kJ/mol'), E0=(79.3223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='RBrC=C=O',), comment="""BM rule fitted to 1 training reactions at node RBrC=C=O
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

