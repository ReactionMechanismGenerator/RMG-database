#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.59232e+10,'m^3/(mol*s)'), n=-1.53854, w0=(213000,'J/mol'), E0=(5492.44,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07089946866729961, var=0.46390042815407184, Tref=1000.0, N=8, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 8 training reactions at node Root
    Total Standard Deviation in ln(k): 1.5435691658384416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 1.5435691658384416""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 1.5435691658384416
""",
)

entry(
    index = 2,
    label = "Root_Ext-5R-R",
    kinetics = ArrheniusBM(A=(8.00346e+13,'m^3/(mol*s)'), n=-2.39139, w0=(213000,'J/mol'), E0=(19271,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11014933828574046, var=0.6936015787958725, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-5R-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-5R-R
    Total Standard Deviation in ln(k): 1.9463555546516302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-5R-R
Total Standard Deviation in ln(k): 1.9463555546516302""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-5R-R
Total Standard Deviation in ln(k): 1.9463555546516302
""",
)

entry(
    index = 3,
    label = "Root_Ext-3R-R",
    kinetics = ArrheniusBM(A=(2.13565e+09,'m^3/(mol*s)'), n=-0.982686, w0=(213000,'J/mol'), E0=(9815.71,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.155088700701577, var=3.6678857531903013, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R
    Total Standard Deviation in ln(k): 9.254209245766118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 9.254209245766118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 9.254209245766118
""",
)

entry(
    index = 4,
    label = "Root_Ext-5R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.46293e+13,'m^3/(mol*s)'), n=-2.3617, w0=(213000,'J/mol'), E0=(19109.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1175239280999607, var=6.252228011041329, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-5R-R_7R!H->C
    Total Standard Deviation in ln(k): 7.820579993842215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 7.820579993842215""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 7.820579993842215
""",
)

entry(
    index = 5,
    label = "Root_Ext-5R-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.094e+17,'m^3/(mol*s)'), n=-4.5, w0=(213000,'J/mol'), E0=(3793.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5R-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-3R-R_5R->C",
    kinetics = ArrheniusBM(A=(1.1e+06,'m^3/(mol*s)'), n=0, w0=(213000,'J/mol'), E0=(5168.55,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_5R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-3R-R_N-5R->C",
    kinetics = ArrheniusBM(A=(190000,'m^3/(mol*s)'), n=0, w0=(213000,'J/mol'), E0=(-4877.84,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-5R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-5R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-5R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-5R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-5R-R_7R!H->C_7C-inRing",
    kinetics = ArrheniusBM(A=(2.74681e+06,'m^3/(mol*s)'), n=-0.0101077, w0=(213000,'J/mol'), E0=(16796.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8243065462140909, var=3.014120957818995, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C_7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing
    Total Standard Deviation in ln(k): 5.551587432042679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 5.551587432042679""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 5.551587432042679
""",
)

entry(
    index = 9,
    label = "Root_Ext-5R-R_7R!H->C_N-7C-inRing",
    kinetics = ArrheniusBM(A=(3.18266e+14,'m^3/(mol*s)'), n=-2.69381, w0=(213000,'J/mol'), E0=(-4280.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1238172880969069, var=0.2143724373616906, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C_N-7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing
    Total Standard Deviation in ln(k): 1.2392984962991611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 1.2392984962991611""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 1.2392984962991611
""",
)

entry(
    index = 10,
    label = "Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(213000,'J/mol'), E0=(22550.7,'J/mol'), Tmin=(303,'K'), Tmax=(329,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_7C-inRing_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R",
    kinetics = ArrheniusBM(A=(3.2e+06,'m^3/(mol*s)'), n=0, w0=(213000,'J/mol'), E0=(15374.8,'J/mol'), Tmin=(243,'K'), Tmax=(293,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5R-R_7R!H->C_N-7C-inRing_Ext-5R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

