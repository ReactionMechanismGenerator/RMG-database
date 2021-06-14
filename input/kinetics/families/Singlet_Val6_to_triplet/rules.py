#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_Val6_to_triplet/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.15477e+13,'s^-1'), n=0.120255, w0=(152250,'J/mol'), E0=(15225,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0998889646871146, var=488.606175958841, Tref=1000.0, N=2, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 44.56451937156995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 44.56451937156995""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 44.56451937156995
""",
)

entry(
    index = 2,
    label = "Root_1O2dS2d->O2d",
    kinetics = ArrheniusBM(A=(4.5e+10,'s^-1'), n=0, w0=(176000,'J/mol'), E0=(17600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1O2dS2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_1O2dS2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1O2dS2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1O2dS2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-1O2dS2d->O2d",
    kinetics = ArrheniusBM(A=(2.5e+17,'s^-1'), n=0, w0=(128500,'J/mol'), E0=(12850,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1O2dS2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-1O2dS2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1O2dS2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1O2dS2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

