#!/usr/bin/env python
# encoding: utf-8

name = "Cation_R_Recombination/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 0,
    label = "Root",
    kinetics = ArrheniusChargeTransferBM(A=(7.25239e+06,'m^3/(mol*s)'), n=0.211611, w0=(159759,'J/mol'), E0=(7480.68,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0396322771044, var=5.01691061618, Tref=1000.0, N=145, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 4.58987665919"""),
    rank = 0,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 4.58987665919""",
    longDesc =
u"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 4.58987665919
""",
)
