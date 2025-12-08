#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.62443e-09,'m^3/(mol*s)'), n=4.14746, w0=(718.364,'kJ/mol'), E0=(395.4,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15325006990509896, var=63.474848598668366, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 16.35699617074341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 16.35699617074341""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 16.35699617074341
""",
)

entry(
    index = 2,
    label = "Root_1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(0.199842,'m^3/(mol*s)'), n=2.2417, w0=(753.875,'kJ/mol'), E0=(242.116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.182008018555932, var=322.94602007397447, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 44.02148553405957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 44.02148553405957""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 44.02148553405957
""",
)

entry(
    index = 3,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(8.51541e-09,'m^3/(mol*s)'), n=4.14536, w0=(749.11,'kJ/mol'), E0=(398.473,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1750317424938415, var=53.719699052462545, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 15.133228093827807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.133228093827807""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.133228093827807
""",
)

entry(
    index = 4,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = Arrhenius(A=(2890,'m^3/(mol*s)'), n=1.16, Ea=(343.506,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2.97498e-05,'m^3/(mol*s)'), n=3.24415, w0=(750.667,'kJ/mol'), E0=(155.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09875943046005553, var=43.2203816311661, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 13.427710698592266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.427710698592266""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.427710698592266
""",
)

entry(
    index = 6,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(4.76729e-19,'m^3/(mol*s)'), n=7.20542, w0=(755.952,'kJ/mol'), E0=(432.994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6022884505988311, var=112.4891910618324, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 22.77569256623402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 22.77569256623402""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 22.77569256623402
""",
)

entry(
    index = 7,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2.49828e-06,'m^3/(mol*s)'), n=3.39699, w0=(745.509,'kJ/mol'), E0=(384.349,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2412356863437334, var=18.724419869753966, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 9.280953854120009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 9.280953854120009""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 9.280953854120009
""",
)

entry(
    index = 8,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s",
    kinetics = Arrhenius(A=(5.66811e-11,'m^3/(mol*s)'), n=4.88105, Ea=(180.508,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00925508,'m^3/(mol*s)'), n=2.53089, w0=(692.5,'kJ/mol'), E0=(142.143,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054127952330834, var=9.232006363555103, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 6.2272304211932425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.2272304211932425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.2272304211932425
""",
)

entry(
    index = 10,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.25661e-19,'m^3/(mol*s)'), n=7.37922, w0=(787.717,'kJ/mol'), E0=(438.871,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4940107275754602, var=87.21452136335157, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 19.963196313613498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 19.963196313613498""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 19.963196313613498
""",
)

entry(
    index = 11,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = Arrhenius(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, Ea=(223.258,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R",
    kinetics = ArrheniusBM(A=(5.11527e-06,'m^3/(mol*s)'), n=3.32781, w0=(752.167,'kJ/mol'), E0=(365.036,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20864419749655808, var=5.027100341695435, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R
    Total Standard Deviation in ln(k): 5.019087480159968"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 5.019087480159968""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 5.019087480159968
""",
)

entry(
    index = 13,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs",
    kinetics = ArrheniusBM(A=(2.08261e-05,'m^3/(mol*s)'), n=3.0904, w0=(804.39,'kJ/mol'), E0=(414.519,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2636884498763666, var=11.49869864525786, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs
    Total Standard Deviation in ln(k): 7.460536537475845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 7.460536537475845""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 7.460536537475845
""",
)

entry(
    index = 14,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs",
    kinetics = ArrheniusBM(A=(0.000170355,'m^3/(mol*s)'), n=3.41516, w0=(675.167,'kJ/mol'), E0=(336.837,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21490021676663595, var=25.196791050669937, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs
    Total Standard Deviation in ln(k): 10.602999739833962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 10.602999739833962""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 10.602999739833962
""",
)

entry(
    index = 15,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1sCs->Cl1s",
    kinetics = Arrhenius(A=(0.006108,'m^3/(mol*s)'), n=2.57909, Ea=(159.246,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1sCs->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1sCs->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1sCs->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1sCs->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1sCs->Cl1s",
    kinetics = Arrhenius(A=(0.0152384,'m^3/(mol*s)'), n=2.47236, Ea=(142.16,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1sCs->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1sCs->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1sCs->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1sCs->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(4.35551e-18,'m^3/(mol*s)'), n=6.8478, w0=(779.12,'kJ/mol'), E0=(438.367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8297092376262959, var=104.37634957768094, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R
    Total Standard Deviation in ln(k): 22.56602121433507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 22.56602121433507""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 22.56602121433507
""",
)

entry(
    index = 18,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.0603e-06,'m^3/(mol*s)'), n=3.38706, w0=(740.071,'kJ/mol'), E0=(361.82,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21129694417125117, var=6.0341068198795735, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
    Total Standard Deviation in ln(k): 5.455412091978765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
Total Standard Deviation in ln(k): 5.455412091978765""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
Total Standard Deviation in ln(k): 5.455412091978765
""",
)

entry(
    index = 19,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0021256,'m^3/(mol*s)'), n=2.9327, w0=(794.5,'kJ/mol'), E0=(386.248,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.038040144670897495, var=0.14344916898298954, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.8548653289999985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.8548653289999985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.8548653289999985
""",
)

entry(
    index = 20,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = Arrhenius(A=(0.000538,'m^3/(mol*s)'), n=3.29, Ea=(437.228,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(2.08219e-05,'m^3/(mol*s)'), n=3.07431, w0=(790.751,'kJ/mol'), E0=(413.699,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2713545451539667, var=12.033752946484018, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 7.636161205740476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 7.636161205740476""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 7.636161205740476
""",
)

entry(
    index = 22,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s",
    kinetics = Arrhenius(A=(0.000614234,'m^3/(mol*s)'), n=3.16963, Ea=(318.436,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00966108,'m^3/(mol*s)'), n=2.95568, w0=(635.079,'kJ/mol'), E0=(328.446,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18731351736347088, var=8.005119587845035, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 6.142698091953715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.142698091953715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.142698091953715
""",
)

entry(
    index = 24,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.016008,'m^3/(mol*s)'), n=2.60695, w0=(720.5,'kJ/mol'), E0=(333.568,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2517712620555509, var=5.184316561865401, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 5.197191317219699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 5.197191317219699""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 5.197191317219699
""",
)

entry(
    index = 25,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.61563e-23,'m^3/(mol*s)'), n=8.18797, w0=(909.868,'kJ/mol'), E0=(451.396,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19848249550467034, var=4.671405137341618, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.8316205936616425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.8316205936616425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.8316205936616425
""",
)

entry(
    index = 26,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.93197e-05,'m^3/(mol*s)'), n=3.07297, w0=(752.167,'kJ/mol'), E0=(360.904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19178911976699337, var=3.6166924321875498, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 4.294407894680735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.294407894680735""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.294407894680735
""",
)

entry(
    index = 27,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(7.55232e-06,'m^3/(mol*s)'), n=3.16085, w0=(801.969,'kJ/mol'), E0=(415.561,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2866243462779529, var=11.751662603192779, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
    Total Standard Deviation in ln(k): 7.592533464360565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
Total Standard Deviation in ln(k): 7.592533464360565""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
Total Standard Deviation in ln(k): 7.592533464360565
""",
)

entry(
    index = 28,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(0.00734196,'m^3/(mol*s)'), n=2.97843, Ea=(311.689,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(0.0163189,'m^3/(mol*s)'), n=2.90186, Ea=(300.412,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.26414,'m^3/(mol*s)'), n=1.78982, w0=(720.5,'kJ/mol'), E0=(338.391,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23441824057610466, var=10.402855165970275, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 7.054954303195877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 7.054954303195877""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 7.054954303195877
""",
)

entry(
    index = 31,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C",
    kinetics = Arrhenius(A=(1.81927e-16,'m^3/(mol*s)'), n=6.80628, Ea=(325.917,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C",
    kinetics = Arrhenius(A=(1.76125e-25,'m^3/(mol*s)'), n=8.86865, Ea=(457.075,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C",
    kinetics = Arrhenius(A=(7.09132e-21,'m^3/(mol*s)'), n=7.51297, Ea=(459.846,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.00881e-05,'m^3/(mol*s)'), n=2.97247, w0=(731,'kJ/mol'), E0=(360.496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16984412133062576, var=3.8179502768107825, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 4.3439113506760885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 4.3439113506760885""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 4.3439113506760885
""",
)

entry(
    index = 35,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.57253e-05,'m^3/(mol*s)'), n=3.24294, w0=(794.5,'kJ/mol'), E0=(361.988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23244300669040274, var=5.185214704804663, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 5.149023235330659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.149023235330659""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.149023235330659
""",
)

entry(
    index = 36,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(5.25434e-07,'m^3/(mol*s)'), n=3.46496, w0=(850.79,'kJ/mol'), E0=(427.256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3248113009442152, var=2.234913944503512, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R
    Total Standard Deviation in ln(k): 3.8131132756367636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R
Total Standard Deviation in ln(k): 3.8131132756367636""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R
Total Standard Deviation in ln(k): 3.8131132756367636
""",
)

entry(
    index = 37,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(7.15522e-09,'m^3/(mol*s)'), n=4.05272, Ea=(334.996,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R",
    kinetics = Arrhenius(A=(88.9,'m^3/(mol*s)'), n=1.51, Ea=(331.373,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O",
    kinetics = Arrhenius(A=(5.66674e-08,'m^3/(mol*s)'), n=3.74252, Ea=(331.889,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(0.000304538,'m^3/(mol*s)'), n=2.68802, w0=(728.284,'kJ/mol'), E0=(368.545,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15721620680180184, var=1.9624922538893657, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 3.2034285324485237"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 3.2034285324485237""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 3.2034285324485237
""",
)

entry(
    index = 41,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R",
    kinetics = Arrhenius(A=(0.000657796,'m^3/(mol*s)'), n=3.03266, Ea=(372.985,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.06396e-07,'m^3/(mol*s)'), n=3.50491, w0=(841.204,'kJ/mol'), E0=(422.692,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33426105868651484, var=0.03371833801310393, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 1.2079724623296706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 1.2079724623296706""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 1.2079724623296706
""",
)

entry(
    index = 43,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C",
    kinetics = Arrhenius(A=(8.68834e-07,'m^3/(mol*s)'), n=3.38642, Ea=(433.585,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = Arrhenius(A=(0.000113417,'m^3/(mol*s)'), n=3.00792, Ea=(381.427,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000582576,'m^3/(mol*s)'), n=2.50881, w0=(716.113,'kJ/mol'), E0=(367.423,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16163968774428752, var=2.2250827324255416, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 3.3965352883712865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.3965352883712865""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.3965352883712865
""",
)

entry(
    index = 46,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C",
    kinetics = Arrhenius(A=(1.17091e-07,'m^3/(mol*s)'), n=3.66153, Ea=(417.423,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.41072e-06,'m^3/(mol*s)'), n=3.34827, Ea=(419.577,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(9.05456e-05,'m^3/(mol*s)'), n=2.75561, Ea=(351.94,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(0.00374667,'m^3/(mol*s)'), n=2.26207, Ea=(344.875,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

