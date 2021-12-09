#!/usr/bin/env python
# encoding: utf-8

name = "Ketoenol/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.70715e-12,'s^-1'), n=7.18941, w0=(792618,'J/mol'), E0=(96849.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.048623136096174725, var=7.38275188734163, Tref=1000.0, N=17, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 17 training reactions at node Root
    Total Standard Deviation in ln(k): 5.569278438749864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 5.569278438749864""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 5.569278438749864
""",
)

entry(
    index = 2,
    label = "Root_3R!H->C",
    kinetics = ArrheniusBM(A=(75.1006,'s^-1'), n=3.11041, w0=(783500,'J/mol'), E0=(209076,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00848789959541425, var=6.520606768146176, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_3R!H->C
    Total Standard Deviation in ln(k): 5.140513384866411"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R!H->C
Total Standard Deviation in ln(k): 5.140513384866411""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R!H->C
Total Standard Deviation in ln(k): 5.140513384866411
""",
)

entry(
    index = 3,
    label = "Root_N-3R!H->C",
    kinetics = ArrheniusBM(A=(2.87617e-12,'s^-1'), n=7.25159, w0=(794571,'J/mol'), E0=(96067.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05095623138621764, var=6.9856901089733165, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R!H->C',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R!H->C
    Total Standard Deviation in ln(k): 5.4266369823609475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 5.4266369823609475""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 5.4266369823609475
""",
)

entry(
    index = 4,
    label = "Root_3R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(205000,'s^-1'), n=2.37, w0=(783500,'J/mol'), E0=(221387,'J/mol'), Tmin=(600,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(7.04228e-12,'s^-1'), n=7.149, w0=(798000,'J/mol'), E0=(99279.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.037889180917409476, var=6.328452360267048, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 5.138393785410001"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N
Total Standard Deviation in ln(k): 5.138393785410001""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N
Total Standard Deviation in ln(k): 5.138393785410001
""",
)

entry(
    index = 6,
    label = "Root_N-3R!H->C_N-3BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1583.91,'s^-1'), n=2.85161, w0=(782000,'J/mol'), E0=(88955.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003045184023974304, var=0.28211849898893376, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-3BrClFINOPSSi->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-3BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 1.0724628112272296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-3BrClFINOPSSi->N
Total Standard Deviation in ln(k): 1.0724628112272296""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-3BrClFINOPSSi->N
Total Standard Deviation in ln(k): 1.0724628112272296
""",
)

entry(
    index = 7,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R",
    kinetics = ArrheniusBM(A=(4.42102e-08,'s^-1'), n=6.02684, w0=(798000,'J/mol'), E0=(100291,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04644471083794055, var=26.35201393188678, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R
    Total Standard Deviation in ln(k): 10.407844939707589"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R
Total Standard Deviation in ln(k): 10.407844939707589""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R
Total Standard Deviation in ln(k): 10.407844939707589
""",
)

entry(
    index = 8,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.59297e-14,'s^-1'), n=7.69658, w0=(798000,'J/mol'), E0=(100978,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008127373484941138, var=0.13233644987650478, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.749704609952026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.749704609952026""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.749704609952026
""",
)

entry(
    index = 9,
    label = "Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2857.3,'s^-1'), n=2.79065, w0=(782000,'J/mol'), E0=(88663.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.015825826525184e-07, var=0.0007766175206250726, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.05586817935319939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.05586817935319939""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.05586817935319939
""",
)

entry(
    index = 10,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.00037e+12,'s^-1'), n=0.391734, w0=(798000,'J/mol'), E0=(115905,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.63498e-12,'s^-1'), n=7.20509, w0=(798000,'J/mol'), E0=(105249,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(2.13103e-12,'s^-1'), n=7.21352, w0=(798000,'J/mol'), E0=(101137,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(6.18181e-12,'s^-1'), n=7.01339, w0=(798000,'J/mol'), E0=(99403.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.52889e-15,'s^-1'), n=8.14889, w0=(798000,'J/mol'), E0=(98709.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0060049628157933235, var=0.37717516496187486, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 1.246287639507079"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C
Total Standard Deviation in ln(k): 1.246287639507079""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C
Total Standard Deviation in ln(k): 1.246287639507079
""",
)

entry(
    index = 15,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.43586e-13,'s^-1'), n=7.42108, w0=(798000,'J/mol'), E0=(102563,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004210953566892827, var=0.20127748890718947, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.9099838245929136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.9099838245929136""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.9099838245929136
""",
)

entry(
    index = 16,
    label = "Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(87.5,'s^-1'), n=3.23, w0=(782000,'J/mol'), E0=(85014.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.24517e-15,'s^-1'), n=8.2595, w0=(798000,'J/mol'), E0=(103171,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_7R!H->O",
    kinetics = ArrheniusBM(A=(9.26244e-13,'s^-1'), n=7.34559, w0=(798000,'J/mol'), E0=(102159,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(6.99061e-13,'s^-1'), n=7.44526, w0=(798000,'J/mol'), E0=(102738,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004731463438640534, var=0.28391442034031983, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O
    Total Standard Deviation in ln(k): 1.0800835278451721"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.0800835278451721""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.0800835278451721
""",
)

entry(
    index = 20,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N",
    kinetics = ArrheniusBM(A=(2.42473e-12,'s^-1'), n=7.26154, w0=(798000,'J/mol'), E0=(100991,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0010131706773348554, var=0.27551282913717107, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N
    Total Standard Deviation in ln(k): 1.0548173841742803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N
Total Standard Deviation in ln(k): 1.0548173841742803""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N
Total Standard Deviation in ln(k): 1.0548173841742803
""",
)

entry(
    index = 21,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_N-5NO->N",
    kinetics = ArrheniusBM(A=(1.40253e-13,'s^-1'), n=7.701, w0=(798000,'J/mol'), E0=(107078,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_N-5NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_N-5NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_N-5NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_N-5NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_5N-inRing",
    kinetics = ArrheniusBM(A=(4.47903e-12,'s^-1'), n=7.22226, w0=(798000,'J/mol'), E0=(102310,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_N-5N-inRing",
    kinetics = ArrheniusBM(A=(1.70268e-12,'s^-1'), n=7.27027, w0=(798000,'J/mol'), E0=(100050,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_N-5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_N-5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H->C_Ext-6R!H-R_N-7R!H->O_5NO->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

