#!/usr/bin/env python
# encoding: utf-8

name = "XY_elimination_hydroxyl/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.29471e-53,'s^-1'), n=19.0642, w0=(1.25393e+06,'J/mol'), E0=(-11777.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6030706655901165, var=48.63557807331129, Tref=1000.0, N=14, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 14 training reactions at node Root
    Total Standard Deviation in ln(k): 15.496117553334454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.496117553334454""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 15.496117553334454
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(786687,'s^-1'), n=2.06826, w0=(1.22572e+06,'J/mol'), E0=(186848,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06572426672533703, var=35.397976975874734, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 12.092548062853473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 12.092548062853473""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 12.092548062853473
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(3.36992e+13,'s^-1'), n=-0.177525, w0=(1.3047e+06,'J/mol'), E0=(113716,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06700689405116313, var=2.0097828678992498, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 3.0104080169355436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 3.0104080169355436""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 3.0104080169355436
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_5Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(68453,'s^-1'), n=2.17099, w0=(1.1725e+06,'J/mol'), E0=(282524,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_5Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.25497e+12,'s^-1'), n=0.192523, w0=(1.23238e+06,'J/mol'), E0=(188273,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03627415907183131, var=5.083062161268406, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 4.610946119247431"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 4.610946119247431""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 4.610946119247431
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(3.91271e+15,'s^-1'), n=-0.91308, w0=(1.3745e+06,'J/mol'), E0=(113186,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09110474360371991, var=4.490802463962393, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 4.477243445960722"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.477243445960722""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.477243445960722
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(1.46638e+11,'s^-1'), n=0.708452, w0=(1.2e+06,'J/mol'), E0=(116018,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0002077660778895548, var=2.128133909944111, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 2.925054615266597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 2.925054615266597""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 2.925054615266597
""",
)

entry(
    index = 8,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.5706e+11,'s^-1'), n=0.715494, w0=(1.276e+06,'J/mol'), E0=(231823,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(5.80016e+14,'s^-1'), n=-0.567338, w0=(1.276e+06,'J/mol'), E0=(183244,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07747427306529306, var=2.173071636799296, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 3.149907515166377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.149907515166377""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.149907515166377
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(3.9456e+10,'s^-1'), n=0.819032, w0=(1.1015e+06,'J/mol'), E0=(191246,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00032049782896238706, var=0.9987135204554455, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 2.0042504079825347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 2.0042504079825347""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 2.0042504079825347
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.29418e+10,'s^-1'), n=0.745914, w0=(1.3745e+06,'J/mol'), E0=(117272,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.77496e+17,'s^-1'), n=-1.58758, w0=(1.3745e+06,'J/mol'), E0=(116506,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.030405532278326947, var=15.727862887171884, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 8.026848298408312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 8.026848298408312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 8.026848298408312
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(3.42848e+09,'s^-1'), n=1.33002, w0=(1.227e+06,'J/mol'), E0=(125091,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(4.74683e+09,'s^-1'), n=1.36442, w0=(1.173e+06,'J/mol'), E0=(121189,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5Br1sCl1sF1sH->F1s_N-5Br1sCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.9833e+15,'s^-1'), n=-0.802106, w0=(1.276e+06,'J/mol'), E0=(186956,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08107442052799871, var=3.1845085066262686, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
    Total Standard Deviation in ln(k): 3.7811926598735495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
Total Standard Deviation in ln(k): 3.7811926598735495""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R
Total Standard Deviation in ln(k): 3.7811926598735495
""",
)

entry(
    index = 16,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.20378e+08,'s^-1'), n=1.70445, w0=(1.1285e+06,'J/mol'), E0=(197060,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.23964e+08,'s^-1'), n=1.60341, w0=(1.0745e+06,'J/mol'), E0=(193601,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_N-5Br1sCl1sF1s->F1s_N-5Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.14547e+10,'s^-1'), n=0.631481, w0=(1.3745e+06,'J/mol'), E0=(98182.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(2.6978e+09,'s^-1'), n=1.11971, w0=(1.276e+06,'J/mol'), E0=(193858,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(1.97392e+12,'s^-1'), n=0.222289, w0=(1.276e+06,'J/mol'), E0=(175596,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.028034265391885454, var=0.7275535203596748, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 1.7804116779216648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.7804116779216648""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.7804116779216648
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C",
    kinetics = ArrheniusBM(A=(2.39251e+11,'s^-1'), n=0.443131, w0=(1.276e+06,'J/mol'), E0=(173250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0002426586333114885, var=0.5095614775048485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C
    Total Standard Deviation in ln(k): 1.4316612619170346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 1.4316612619170346""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 1.4316612619170346
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C",
    kinetics = ArrheniusBM(A=(1.52349e+10,'s^-1'), n=1.11612, w0=(1.276e+06,'J/mol'), E0=(182141,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_N-Sp-7BrCClFINPSSi-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.98542e+10,'s^-1'), n=0.978818, w0=(1.276e+06,'J/mol'), E0=(185739,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-5Br1sCl1sF1sH->H_5Br1sCl1sF1s->F1s_Ext-2C-R_N-7R!H->O_Sp-7BrCClFINPSSi-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

