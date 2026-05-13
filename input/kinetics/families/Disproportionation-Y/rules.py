#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation-Y/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.19126e+09,'m^3/(mol*s)'), n=-0.608471, w0=(561.986,'kJ/mol'), E0=(71.3614,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10031122924999919, var=0.48029990761569036, Tref=1000.0, N=42, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 42 training reactions at node Root
    Total Standard Deviation in ln(k): 1.6413933048118652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 1.6413933048118652""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 1.6413933048118652
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = ArrheniusBM(A=(1.57302e+17,'m^3/(mol*s)'), n=-3.29848, w0=(494.25,'kJ/mol'), E0=(71.3939,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08450552872404533, var=91.4326625167961, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 2 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 19.38168806257332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 19.38168806257332""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 19.38168806257332
""",
)

entry(
    index = 3,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(2.88129e+09,'m^3/(mol*s)'), n=-0.594208, w0=(565.373,'kJ/mol'), E0=(71.3614,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10423172625690806, var=0.46121564110071755, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 40 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 1.623361664907418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 1.623361664907418""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 1.623361664907418
""",
)

entry(
    index = 4,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H",
    kinetics = ArrheniusBM(A=(9.28607e+08,'m^3/(mol*s)'), n=-0.393575, w0=(587.271,'kJ/mol'), E0=(89.7711,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13360484049464624, var=0.40518613492657013, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H',), comment="""BM rule fitted to 35 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H
    Total Standard Deviation in ln(k): 1.6117892865501753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H
Total Standard Deviation in ln(k): 1.6117892865501753""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H
Total Standard Deviation in ln(k): 1.6117892865501753
""",
)

entry(
    index = 5,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->H",
    kinetics = ArrheniusBM(A=(5.32457e+06,'m^3/(mol*s)'), n=0.000711411, w0=(412.084,'kJ/mol'), E0=(37.2184,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012927915966369793, var=0.3896722522091154, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H
    Total Standard Deviation in ln(k): 1.2839126859063534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H
Total Standard Deviation in ln(k): 1.2839126859063534""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H
Total Standard Deviation in ln(k): 1.2839126859063534
""",
)

entry(
    index = 6,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.03018e+08,'m^3/(mol*s)'), n=-0.101608, w0=(502.214,'kJ/mol'), E0=(80.978,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03993571617444821, var=0.4427883879615895, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 1.4343387573045112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.4343387573045112""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.4343387573045112
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(6.23578e+10,'m^3/(mol*s)'), n=-1.15514, w0=(643.976,'kJ/mol'), E0=(84.281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.015290440136244915, var=0.6038124517749592, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 21 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 1.5962049995337704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.5962049995337704""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.5962049995337704
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(8.16667e+06,'m^3/(mol*s)'), n=-1.34323e-09, w0=(406.21,'kJ/mol'), E0=(36.1306,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(3.9685e+06,'m^3/(mol*s)'), n=-3.90188e-08, w0=(416,'kJ/mol'), E0=(23.0012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.064379142725545, var=0.4397101122614039, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.4911093221181615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4911093221181615""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4911093221181615
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.11863e+08,'m^3/(mol*s)'), n=-0.154631, w0=(502.944,'kJ/mol'), E0=(84.3246,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05351184983761427, var=0.2442231855336425, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.1251707546288294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.1251707546288294""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.1251707546288294
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.22098e+08,'m^3/(mol*s)'), n=-0.174178, w0=(501.667,'kJ/mol'), E0=(85.7864,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0625192500194824, var=0.43706828229216876, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.4824367550161213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.4824367550161213""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.4824367550161213
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.43225e+09,'m^3/(mol*s)'), n=-0.830246, w0=(633.333,'kJ/mol'), E0=(74.8145,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49460674508365404, var=0.9487442619208486, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.19541272943827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.19541272943827""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.19541272943827
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.69366e+11,'m^3/(mol*s)'), n=-1.18281, w0=(671.5,'kJ/mol'), E0=(101.399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1299252555029932, var=0.8591211897152042, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.184610062935415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.184610062935415""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.184610062935415
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(3.59692e+09,'m^3/(mol*s)'), n=-0.781097, w0=(641.5,'kJ/mol'), E0=(74.2509,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09158847649517517, var=0.64096839865242, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.835122767726204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.835122767726204""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.835122767726204
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_4BrClO->Cl",
    kinetics = Arrhenius(A=(8.16667e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_4BrClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_4BrClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_4BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_4BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Cl",
    kinetics = Arrhenius(A=(8.16667e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = Arrhenius(A=(2.5e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.93828e+07,'m^3/(mol*s)'), n=4.00423e-08, w0=(502.625,'kJ/mol'), E0=(69.1925,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.131534497955784e-08, var=0.09662784107815152, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl
    Total Standard Deviation in ln(k): 0.6231723096057115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6231723096057115""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6231723096057115
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl",
    kinetics = Arrhenius(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, Ea=(15.1879,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(5e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(4.68135e+09,'m^3/(mol*s)'), n=-0.837975, w0=(630.611,'kJ/mol'), E0=(74.9927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7740359326955396, var=1.8119786992972569, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 4.643382940754345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.643382940754345""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.643382940754345
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.03371e+09,'m^3/(mol*s)'), n=-0.586164, w0=(641.5,'kJ/mol'), E0=(61.8875,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09038178883077484, var=0.5835814251820923, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.75855719134509"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.75855719134509""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.75855719134509
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C",
    kinetics = ArrheniusBM(A=(1.42287e+10,'m^3/(mol*s)'), n=-0.866872, w0=(653,'kJ/mol'), E0=(68.3367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06605710061143397, var=0.3101864830872259, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C
    Total Standard Deviation in ln(k): 1.282497542690133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C
Total Standard Deviation in ln(k): 1.282497542690133""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C
Total Standard Deviation in ln(k): 1.282497542690133
""",
)

entry(
    index = 24,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C",
    kinetics = Arrhenius(A=(1e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.20454e+08,'m^3/(mol*s)'), n=-0.586164, w0=(641.5,'kJ/mol'), E0=(64.5989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11612439396277328, var=0.9450557867300579, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.240652587129445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.240652587129445""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.240652587129445
""",
)

entry(
    index = 26,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.33333e+07,'m^3/(mol*s)'), n=-4.09588e-08, w0=(505.5,'kJ/mol'), E0=(81.7025,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.609144593860216e-09, var=5.829960888751039e-19, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R
    Total Standard Deviation in ln(k): 5.573775909707441e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R
Total Standard Deviation in ln(k): 5.573775909707441e-09""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R
Total Standard Deviation in ln(k): 5.573775909707441e-09
""",
)

entry(
    index = 27,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.9685e+07,'m^3/(mol*s)'), n=-1.72694e-08, w0=(501.667,'kJ/mol'), E0=(65.0019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.664877861015856e-11, var=0.3603397611104758, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.2034085219978943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2034085219978943""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2034085219978943
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.36473e+14,'m^3/(mol*s)'), n=-2.22529, w0=(619.417,'kJ/mol'), E0=(102.768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5315372919225424, var=1.162739936952722, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 3.497235077792238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.497235077792238""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.497235077792238
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.36e+13,'m^3/(mol*s)'), n=-2.26, w0=(653,'kJ/mol'), E0=(113.902,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8353434830257415, var=2.4651903288156624e-32, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.0988529724264864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0988529724264864""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0988529724264864
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C",
    kinetics = Arrhenius(A=(3e+07,'m^3/(mol*s)'), n=0, Ea=(8.368,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.03083e+11,'m^3/(mol*s)'), n=-1.3659, w0=(641.5,'kJ/mol'), E0=(65.6313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8979021931323072, var=0.012275126038303533, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 2.478146611025363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 2.478146611025363""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 2.478146611025363
""",
)

entry(
    index = 32,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.27455e+09,'m^3/(mol*s)'), n=-0.729798, w0=(653,'kJ/mol'), E0=(66.4526,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12744373425058092, var=0.5335358647948554, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.784539843668329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.784539843668329""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.784539843668329
""",
)

entry(
    index = 33,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C",
    kinetics = Arrhenius(A=(3e+07,'m^3/(mol*s)'), n=0, Ea=(8.368,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.2285e+14,'m^3/(mol*s)'), n=-2.31, w0=(641.5,'kJ/mol'), E0=(99.0903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9762447934156255, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.418034250478541"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.418034250478541""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.418034250478541
""",
)

entry(
    index = 35,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.33333e+07,'m^3/(mol*s)'), n=-9.17155e-09, w0=(505.5,'kJ/mol'), E0=(80.577,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 36,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(5e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(6.69272e+10,'m^3/(mol*s)'), n=-1.30512, w0=(653,'kJ/mol'), E0=(42.1547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21535039247462373, var=0.45038241338748924, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s
    Total Standard Deviation in ln(k): 1.886469857637948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s
Total Standard Deviation in ln(k): 1.886469857637948""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s
Total Standard Deviation in ln(k): 1.886469857637948
""",
)

entry(
    index = 38,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s",
    kinetics = Arrhenius(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, Ea=(15.1879,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = Arrhenius(A=(1.12e+15,'m^3/(mol*s)'), n=-2.27, Ea=(9.37216,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.94372e+10,'m^3/(mol*s)'), n=-1.22042, w0=(653,'kJ/mol'), E0=(39.2537,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10473201125529107, var=1.4342918569068377, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.6640550675003265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.6640550675003265""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.6640550675003265
""",
)

entry(
    index = 41,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, Ea=(15.1879,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

