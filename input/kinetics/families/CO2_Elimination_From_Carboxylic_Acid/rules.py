#!/usr/bin/env python
# encoding: utf-8

name = "CO2_Elimination_From_Carboxylic_Acid/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.21565e-09,'s^-1'), n=6.12086, w0=(828500,'J/mol'), E0=(142329,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5290566326618145, var=4.970649217201842, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 5.798835420605267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 5.798835420605267""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 5.798835420605267
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R-R",
    kinetics = ArrheniusBM(A=(5.7603e-08,'s^-1'), n=5.71781, w0=(828500,'J/mol'), E0=(148218,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.563922870646803, var=5.471010817238656, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R-R
    Total Standard Deviation in ln(k): 6.106005471416499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 6.106005471416499""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 6.106005471416499
""",
)

entry(
    index = 3,
    label = "Root_Ext-2R-R_7R!H->F",
    kinetics = Arrhenius(A=(5.85e-12,'s^-1'), n=6.85, Ea=(136.108,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(3.75265e-07,'s^-1'), n=5.487, w0=(828500,'J/mol'), E0=(147860,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5604104583593817, var=6.161256376488735, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
    Total Standard Deviation in ln(k): 6.384195470827783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 6.384195470827783""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 6.384195470827783
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.20362e-06,'s^-1'), n=5.26551, w0=(828500,'J/mol'), E0=(145098,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5400750817847844, var=12.72880994996101, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 8.509357679479532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 8.509357679479532""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 8.509357679479532
""",
)

entry(
    index = 6,
    label = "Root_Ext-2R-R_N-7R!H->F_6F1sH->H",
    kinetics = Arrhenius(A=(181000,'s^-1'), n=2.09, Ea=(178.625,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H",
    kinetics = Arrhenius(A=(2.54e-21,'s^-1'), n=9.6, Ea=(116.332,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(0.00202568,'s^-1'), n=4.3992, w0=(828500,'J/mol'), E0=(157633,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5914123253367648, var=33.048042095296786, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 13.01066666465502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 13.01066666465502""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 13.01066666465502
""",
)

entry(
    index = 9,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = Arrhenius(A=(1.15e-12,'s^-1'), n=7.1, Ea=(136.768,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H",
    kinetics = Arrhenius(A=(1.36e+06,'s^-1'), n=1.81, Ea=(183.507,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H",
    kinetics = Arrhenius(A=(2.1e-13,'s^-1'), n=7.32, Ea=(137.634,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

