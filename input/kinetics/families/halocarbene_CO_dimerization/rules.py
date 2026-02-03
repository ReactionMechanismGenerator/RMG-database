#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_CO_dimerization/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.22112e+20,'s^-1'), n=-1.46396, w0=(565.5,'kJ/mol'), E0=(97.6906,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6795910255090002, var=1.0348418851075531, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 4 training reactions at node Root
    Total Standard Deviation in ln(k): 3.7468755706450954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 3.7468755706450954""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 3.7468755706450954
""",
)

entry(
    index = 2,
    label = "Root_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.72644e+12,'s^-1'), n=0.805404, w0=(565.5,'kJ/mol'), E0=(72.9488,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21636683876605461, var=0.006888418680191477, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 0.7100212641221405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 0.7100212641221405""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 0.7100212641221405
""",
)

entry(
    index = 3,
    label = "Root_Ext-1C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(3.997e+12,'s^-1'), n=0.449, Ea=(64.9106,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-1C-R_5R!H->C_4Br1sCl1sF1s->F1s",
    kinetics = Arrhenius(A=(6.62099e+12,'s^-1'), n=0.640083, Ea=(177.782,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C-R_5R!H->C_4Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C-R_5R!H->C_4Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C-R_5R!H->C_4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C-R_5R!H->C_4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(9.07123e+12,'s^-1'), n=0.683284, w0=(565.5,'kJ/mol'), E0=(78.6125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18486037481112658, var=0.0024641925784566277, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 0.5639896244867687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 0.5639896244867687""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 0.5639896244867687
""",
)

entry(
    index = 6,
    label = "Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_4Br1sCl1s->Br1s",
    kinetics = Arrhenius(A=(7.3531e+12,'s^-1'), n=0.729529, Ea=(237.53,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_4Br1sCl1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_4Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_4Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_4Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_N-4Br1sCl1s->Br1s",
    kinetics = Arrhenius(A=(6.43849e+12,'s^-1'), n=0.705824, Ea=(225.715,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_N-4Br1sCl1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_N-4Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_N-4Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s_N-4Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

