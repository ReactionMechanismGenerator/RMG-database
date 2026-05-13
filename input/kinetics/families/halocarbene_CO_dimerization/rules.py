#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_CO_dimerization/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.00905e+20,'s^-1'), n=-1.52591, w0=(565.5,'kJ/mol'), E0=(97.9876,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6997333288577562, var=1.0872036113819283, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 4 training reactions at node Root
    Total Standard Deviation in ln(k): 3.8484422895333714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 3.8484422895333714""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 3.8484422895333714
""",
)

entry(
    index = 2,
    label = "Root_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.70403e+12,'s^-1'), n=0.767275, w0=(565.5,'kJ/mol'), E0=(72.8441,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2314840994907021, var=0.008435532019279058, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 0.7657435391326964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 0.7657435391326964""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 0.7657435391326964
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
    kinetics = ArrheniusBM(A=(9.47008e+12,'s^-1'), n=0.677929, w0=(565.5,'kJ/mol'), E0=(77.9791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19352156587534877, var=0.0030932506431147365, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 0.5977324401115213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 0.5977324401115213""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1C-R_5R!H->C_N-4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 0.5977324401115213
""",
)

