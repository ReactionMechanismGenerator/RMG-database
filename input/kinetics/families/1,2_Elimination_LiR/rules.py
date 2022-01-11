#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Elimination_LiR/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(1.03918e+13,'s^-1'), n=0.266823, Ea=(48.3171,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.169679482110385e-15, var=39.92165140788381, Tref=1000.0, N=10, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 10 training reactions at node Root
    Total Standard Deviation in ln(k): 12.666634483937468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root
Total Standard Deviation in ln(k): 12.666634483937468""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root
Total Standard Deviation in ln(k): 12.666634483937468
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R-R",
    kinetics = Arrhenius(A=(1.6261e+14,'s^-1'), n=0.234207, Ea=(97.5599,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.3496301716658287e-15, var=117.48228499542802, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R
    Total Standard Deviation in ln(k): 21.72917220914441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 21.72917220914441""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 21.72917220914441
""",
)

entry(
    index = 3,
    label = "Root_3R->F",
    kinetics = Arrhenius(A=(2.47928e+13,'s^-1'), n=0.0523532, Ea=(1.77399,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->F',), comment="""BM rule fitted to 1 training reactions at node Root_3R->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_N-3R->F",
    kinetics = ArrheniusBM(A=(9.15357e+73,'s^-1'), n=-18.0653, w0=(694200,'J/mol'), E0=(88944.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23368013843917557, var=24.196303894894704, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->F
    Total Standard Deviation in ln(k): 10.448375480286963"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->F
Total Standard Deviation in ln(k): 10.448375480286963""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->F
Total Standard Deviation in ln(k): 10.448375480286963
""",
)

entry(
    index = 5,
    label = "Root_Ext-3R-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.64384e+31,'s^-1'), n=-4.72524, w0=(741100,'J/mol'), E0=(9911.42,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2101947124094859, var=22.757813031131217, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_5R!H->C
    Total Standard Deviation in ln(k): 10.091746105650293"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_5R!H->C
Total Standard Deviation in ln(k): 10.091746105650293""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_5R!H->C
Total Standard Deviation in ln(k): 10.091746105650293
""",
)

entry(
    index = 6,
    label = "Root_Ext-3R-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.9357e+12,'s^-1'), n=-0.0182849, w0=(741100,'J/mol'), E0=(44201.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-3R->F_3ClHO->Cl",
    kinetics = Arrhenius(A=(1.03509e+13,'s^-1'), n=-0.00858289, Ea=(0.072948,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->F_3ClHO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->F_3ClHO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->F_3ClHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->F_3ClHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-3R->F_N-3ClHO->Cl",
    kinetics = ArrheniusBM(A=(1.29924e+76,'s^-1'), n=-18.6883, w0=(670425,'J/mol'), E0=(91614.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1798781997982985, var=29.964308720037355, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->F_N-3ClHO->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->F_N-3ClHO->Cl
    Total Standard Deviation in ln(k): 11.42580783512062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->F_N-3ClHO->Cl
Total Standard Deviation in ln(k): 11.42580783512062""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->F_N-3ClHO->Cl
Total Standard Deviation in ln(k): 11.42580783512062
""",
)

entry(
    index = 9,
    label = "Root_Ext-3R-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(6.8039e+12,'s^-1'), n=0.472198, w0=(741100,'J/mol'), E0=(24627.2,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-3R-R_5R!H->C_2R!H-u0",
    kinetics = ArrheniusBM(A=(1.20441e+16,'s^-1'), n=0.126298, w0=(741100,'J/mol'), E0=(26896.2,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_5R!H->C_2R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R!H->C_2R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R!H->C_2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R!H->C_2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-3R-R_5R!H->C_N-2R!H-u0",
    kinetics = ArrheniusBM(A=(9.54823e+14,'s^-1'), n=0.356617, w0=(741100,'J/mol'), E0=(23860.3,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_5R!H->C_N-2R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R!H->C_N-2R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R!H->C_N-2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_5R!H->C_N-2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-3R->F_N-3ClHO->Cl_2R!H-u0",
    kinetics = ArrheniusBM(A=(5.35515e+82,'s^-1'), n=-20.7752, w0=(646867,'J/mol'), E0=(94952.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.2408646361924225, var=15.321571089508458, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->F_N-3ClHO->Cl_2R!H-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0
    Total Standard Deviation in ln(k): 23.527654521747877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0
Total Standard Deviation in ln(k): 23.527654521747877""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0
Total Standard Deviation in ln(k): 23.527654521747877
""",
)

entry(
    index = 13,
    label = "Root_N-3R->F_N-3ClHO->Cl_N-2R!H-u0",
    kinetics = ArrheniusBM(A=(8.59528e+12,'s^-1'), n=0.518458, w0=(741100,'J/mol'), E0=(19375.8,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->F_N-3ClHO->Cl_N-2R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_N-2R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_N-2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_N-2R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_1R!H->C",
    kinetics = Arrhenius(A=(2.73627e+11,'s^-1'), n=0.349755, Ea=(9.42179,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C",
    kinetics = ArrheniusBM(A=(3.89714e+88,'s^-1'), n=-22.5246, w0=(688150,'J/mol'), E0=(100610,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.291464897902951, var=118.70114603009215, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C
    Total Standard Deviation in ln(k): 40.16186336585088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C
Total Standard Deviation in ln(k): 40.16186336585088""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C
Total Standard Deviation in ln(k): 40.16186336585088
""",
)

entry(
    index = 16,
    label = "Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_1NO->O",
    kinetics = Arrhenius(A=(8.67089e+11,'s^-1'), n=0.423598, Ea=(30.5741,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_N-1NO->O",
    kinetics = Arrhenius(A=(4.01353e+10,'s^-1'), n=0.395823, Ea=(4.40595,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_N-1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_N-1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_N-1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->F_N-3ClHO->Cl_2R!H-u0_N-1R!H->C_N-1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

