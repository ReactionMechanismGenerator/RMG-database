#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.11746e-45,'s^-1'), n=16.9026, w0=(771000,'J/mol'), E0=(-859.303,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5745173911872379, var=52.09733235475162, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 18.425947277680763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 18.425947277680763""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 18.425947277680763
""",
)

entry(
    index = 2,
    label = "Root_3R!H->C",
    kinetics = ArrheniusBM(A=(0.0954007,'s^-1'), n=3.97882, w0=(762750,'J/mol'), E0=(250868,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05104117971660031, var=160.05464641490252, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_3R!H->C
    Total Standard Deviation in ln(k): 25.490690006267023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023
""",
)

entry(
    index = 3,
    label = "Root_N-3R!H->C",
    kinetics = ArrheniusBM(A=(2628.85,'s^-1'), n=2.78353, w0=(782000,'J/mol'), E0=(89057.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004857179637508415, var=0.25064116944332687, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C
    Total Standard Deviation in ln(k): 1.0158560594211685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 1.0158560594211685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 1.0158560594211685
""",
)

entry(
    index = 4,
    label = "Root_3R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700500,'J/mol'), E0=(384026,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_3R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(635.413,'s^-1'), n=2.83859, w0=(783500,'J/mol'), E0=(219488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012207818220425905, var=12.527101437509526, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R!H->C_N-4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_3R!H->C_N-4R->C
    Total Standard Deviation in ln(k): 7.098555561663242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242
""",
)

entry(
    index = 6,
    label = "Root_N-3R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4909.53,'s^-1'), n=2.71698, w0=(782000,'J/mol'), E0=(88826.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1408662726283667e-06, var=3.5438674360202764e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.003776812860711284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284
""",
)

entry(
    index = 7,
    label = "Root_3R!H->C_N-4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(205000,'s^-1'), n=2.37, w0=(783500,'J/mol'), E0=(221387,'J/mol'), Tmin=(600,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-3R!H->C_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(87.5,'s^-1'), n=3.23, w0=(782000,'J/mol'), E0=(84839.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

