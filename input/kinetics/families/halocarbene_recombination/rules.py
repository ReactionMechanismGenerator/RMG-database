#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_recombination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(117780,'m^3/(mol*s)'), n=0.621987, w0=(183.269,'kJ/mol'), E0=(88.258,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0897131863118456, var=0.6492739684095894, Tref=1000.0, N=13, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 13 training reactions at node Root
    Total Standard Deviation in ln(k): 1.840776191357316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 1.840776191357316""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 1.840776191357316
""",
)

entry(
    index = 2,
    label = "Root_3R->H",
    kinetics = ArrheniusBM(A=(0.00482768,'m^3/(mol*s)'), n=1.71263, w0=(205.5,'kJ/mol'), E0=(20.55,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.936386579929548, var=929.3177971072018, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H
    Total Standard Deviation in ln(k): 65.97906870509816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H
Total Standard Deviation in ln(k): 65.97906870509816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H
Total Standard Deviation in ln(k): 65.97906870509816
""",
)

entry(
    index = 3,
    label = "Root_N-3R->H",
    kinetics = ArrheniusBM(A=(98401.8,'m^3/(mol*s)'), n=0.645585, w0=(179.227,'kJ/mol'), E0=(87.8938,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08926642300838682, var=0.26416508207305356, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H
    Total Standard Deviation in ln(k): 1.2546610289923223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 1.2546610289923223""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 1.2546610289923223
""",
)

entry(
    index = 4,
    label = "Root_3R->H_2Br1sCl1sF1s->Cl1s",
    kinetics = Arrhenius(A=(1e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_3R->H_N-2Br1sCl1sF1s->Cl1s",
    kinetics = Arrhenius(A=(2.75,'m^3/(mol*s)'), n=-0.32, Ea=(32.2001,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_N-2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R",
    kinetics = ArrheniusBM(A=(135703,'m^3/(mol*s)'), n=0.463027, w0=(175,'kJ/mol'), E0=(77.0879,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013092347664404615, var=0.32984536916576296, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R
    Total Standard Deviation in ln(k): 1.1842581234356575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R
Total Standard Deviation in ln(k): 1.1842581234356575""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R
Total Standard Deviation in ln(k): 1.1842581234356575
""",
)

entry(
    index = 7,
    label = "Root_N-3R->H_2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.58997e+07,'m^3/(mol*s)'), n=9.71152e-08, w0=(163.5,'kJ/mol'), E0=(53.9233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.516371693678081e-17, var=0.00031645152361524197, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 0.035662401481539555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 0.035662401481539555""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 0.035662401481539555
""",
)

entry(
    index = 8,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(884315,'m^3/(mol*s)'), n=0.378327, w0=(198.167,'kJ/mol'), E0=(94.791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04541090156114323, var=1.2303205688995067, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 2.3377462114655168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.3377462114655168""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.3377462114655168
""",
)

entry(
    index = 9,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(3.79413e+06,'m^3/(mol*s)'), n=0.174285, w0=(173,'kJ/mol'), E0=(108.829,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3890963077020638, var=1.1625755421261272, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C
    Total Standard Deviation in ln(k): 3.1391903344727448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C
Total Standard Deviation in ln(k): 3.1391903344727448""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C
Total Standard Deviation in ln(k): 3.1391903344727448
""",
)

entry(
    index = 10,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(50098.4,'m^3/(mol*s)'), n=0.579003, w0=(179,'kJ/mol'), E0=(75.2584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.8929283524549771, var=20.170731856753324, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C
    Total Standard Deviation in ln(k): 13.759735075645082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C
Total Standard Deviation in ln(k): 13.759735075645082""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C
Total Standard Deviation in ln(k): 13.759735075645082
""",
)

entry(
    index = 11,
    label = "Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl",
    kinetics = Arrhenius(A=(1.58e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl",
    kinetics = Arrhenius(A=(1.6e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFILiNOPSSi->F",
    kinetics = Arrhenius(A=(518506,'m^3/(mol*s)'), n=0.4717, Ea=(2.886,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFILiNOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFILiNOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFILiNOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFILiNOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F",
    kinetics = ArrheniusBM(A=(1587.78,'m^3/(mol*s)'), n=1.13913, w0=(176,'kJ/mol'), E0=(53.8441,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16258386636944822, var=0.00974383149067795, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F
    Total Standard Deviation in ln(k): 0.6063912760871359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F
Total Standard Deviation in ln(k): 0.6063912760871359""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F
Total Standard Deviation in ln(k): 0.6063912760871359
""",
)

entry(
    index = 15,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_2Br1sCl1sF1s->Cl1s",
    kinetics = Arrhenius(A=(0.362967,'m^3/(mol*s)'), n=2.17505, Ea=(-18.5552,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(49.7173,'m^3/(mol*s)'), n=1.57667, w0=(173,'kJ/mol'), E0=(84.8811,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.153976485809718, var=1.304108377531839, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 2.67623422884719"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.67623422884719""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.67623422884719
""",
)

entry(
    index = 17,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C_Ext-1C2s-R",
    kinetics = Arrhenius(A=(0.00128024,'m^3/(mol*s)'), n=2.72845, Ea=(64.1698,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C_Ext-1C2s-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C_Ext-1C2s-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C_Ext-1C2s-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_N-3BrCClFILiNOPSSi->C_Ext-1C2s-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_3CClO->C",
    kinetics = Arrhenius(A=(2.1e+07,'m^3/(mol*s)'), n=-0.207, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_3CClO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_3CClO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_3CClO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_3CClO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_N-3CClO->C",
    kinetics = Arrhenius(A=(37018.9,'m^3/(mol*s)'), n=0.7539, Ea=(3.775,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_N-3CClO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_N-3CClO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_N-3CClO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFILiNOPSSi->F_N-3CClO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_4R!H->Br",
    kinetics = Arrhenius(A=(0.000488623,'m^3/(mol*s)'), n=3.00904, Ea=(3.8448,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_4R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(388.688,'m^3/(mol*s)'), n=1.32196, w0=(173,'kJ/mol'), E0=(85.2397,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15870294984917208, var=1.724002219727201, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br
    Total Standard Deviation in ln(k): 3.0309936473008596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br
Total Standard Deviation in ln(k): 3.0309936473008596""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br
Total Standard Deviation in ln(k): 3.0309936473008596
""",
)

entry(
    index = 22,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_4ClF->Cl",
    kinetics = Arrhenius(A=(0.00296475,'m^3/(mol*s)'), n=2.79547, Ea=(4.97686,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_4ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_N-4ClF->Cl",
    kinetics = Arrhenius(A=(0.195803,'m^3/(mol*s)'), n=2.25958, Ea=(-2.3378,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_N-4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_N-4ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_N-4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFILiNOPSSi-R_3BrCClFILiNOPSSi->C_N-2Br1sCl1sF1s->Cl1s_N-4R!H->Br_N-4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

