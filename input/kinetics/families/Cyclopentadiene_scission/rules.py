#!/usr/bin/env python
# encoding: utf-8

name = "Cyclopentadiene_scission/rules"
shortDesc = "Scission of one of the adjacent single bonds in a CPD subunit to form a conjugated singlet carbene"
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.45e+12,'s^-1'), n=0.194, w0=(685000,'J/mol'), E0=(106333,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 1 training reactions at node Root
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

