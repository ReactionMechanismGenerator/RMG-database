#!/usr/bin/env python
# encoding: utf-8

name = "Ketoenol/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.64543e-12,'s^-1'), n=7.0342, w0=(791900,'J/mol'), E0=(96088.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.025591830299650252, var=3.209136248979107, Tref=1000.0, N=15, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 15 training reactions at node Root
    Total Standard Deviation in ln(k): 3.6555959704468117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 3.6555959704468117""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 3.6555959704468117
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
    kinetics = ArrheniusBM(A=(2.14216e-12,'s^-1'), n=7.10076, w0=(794000,'J/mol'), E0=(95211.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.027300955354671547, var=2.809838899397277, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R!H->C
    Total Standard Deviation in ln(k): 3.4290473906824763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 3.4290473906824763""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 3.4290473906824763
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
    kinetics = ArrheniusBM(A=(1.30473e-11,'s^-1'), n=6.87514, w0=(798000,'J/mol'), E0=(99876.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0117411635116814, var=0.6446492092925814, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 1.6391032023367265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N
Total Standard Deviation in ln(k): 1.6391032023367265""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N
Total Standard Deviation in ln(k): 1.6391032023367265
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
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.09806e-11,'s^-1'), n=6.89792, w0=(798000,'J/mol'), E0=(99858.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0190200390037195, var=1.0964123289271033, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.1469413209668056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.1469413209668056""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.1469413209668056
""",
)

entry(
    index = 8,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.24893e-09,'s^-1'), n=6.18216, w0=(798000,'J/mol'), E0=(107861,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
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
    index = 9,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(3.10725e-11,'s^-1'), n=6.76455, w0=(798000,'J/mol'), E0=(102204,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_6R!H->N
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
    index = 10,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(6.36022e-11,'s^-1'), n=6.62861, w0=(798000,'J/mol'), E0=(100596,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
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
    index = 11,
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
    index = 12,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.87238e-12,'s^-1'), n=7.05581, w0=(798000,'J/mol'), E0=(99707.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02252736485366013, var=0.8629404088644341, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.9188917676717938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9188917676717938""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9188917676717938
""",
)

entry(
    index = 13,
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
    index = 14,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.68509e-11,'s^-1'), n=6.88807, w0=(798000,'J/mol'), E0=(102832,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(2.36128e-12,'s^-1'), n=7.07296, w0=(798000,'J/mol'), E0=(99585.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.029593247978928896, var=1.2653129163997325, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 2.3294037749260914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 2.3294037749260914""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 2.3294037749260914
""",
)

entry(
    index = 16,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(7.93116e-11,'s^-1'), n=6.59023, w0=(798000,'J/mol'), E0=(104253,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004083326014350255, var=0.36678964389307633, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 1.2243905404532403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 1.2243905404532403""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 1.2243905404532403
""",
)

entry(
    index = 17,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.02789e-13,'s^-1'), n=7.48219, w0=(798000,'J/mol'), E0=(95953.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(1.30511e-12,'s^-1'), n=7.26372, w0=(798000,'J/mol'), E0=(105105,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.42992e-10,'s^-1'), n=6.22192, w0=(798000,'J/mol'), E0=(104542,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.0517082806578122e-05, var=0.15820189146844285, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 0.7974520617821278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7974520617821278""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7974520617821278
""",
)

entry(
    index = 20,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.95577e-10,'s^-1'), n=6.41822, w0=(798000,'J/mol'), E0=(102434,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(5.58698e-10,'s^-1'), n=6.27942, w0=(798000,'J/mol'), E0=(105618,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_N-7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_N-7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_3BrClFINOPSSi->N_Ext-1R!H-R_Ext-5R!H-R_N-5R!H-inRing_Sp-6R!H-5R!H_N-5R!H->C_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

