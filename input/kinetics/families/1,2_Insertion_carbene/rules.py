#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.60198e+80,'m^3/(mol*s)'), n=-21.8675, w0=(579276,'J/mol'), E0=(361048,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4474724960037282, var=62.66727759948699, Tref=1000.0, N=29, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 29 training reactions at node Root
    Total Standard Deviation in ln(k): 19.506882993686364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root
Total Standard Deviation in ln(k): 19.506882993686364""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root
Total Standard Deviation in ln(k): 19.506882993686364
""",
)

entry(
    index = 2,
    label = "CH2",
    kinetics = ArrheniusBM(A=(2.42671e+07,'m^3/(mol*s)'), n=-0.35508, w0=(583923,'J/mol'), E0=(58392.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012975471077608, var=4.048427931488091, Tref=1000.0, N=13, data_mean=0.0, correlation='CH2',), comment="""BM rule fitted to 13 training reactions at node CH2
    Total Standard Deviation in ln(k): 4.066270112496024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node CH2
Total Standard Deviation in ln(k): 4.066270112496024""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node CH2
Total Standard Deviation in ln(k): 4.066270112496024
""",
)

entry(
    index = 3,
    label = "CHY",
    kinetics = ArrheniusBM(A=(2.16594e-15,'m^3/(mol*s)'), n=6.2764, w0=(620583,'J/mol'), E0=(62058.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21438205766650628, var=44.35532892123306, Tref=1000.0, N=6, data_mean=0.0, correlation='CHY',), comment="""BM rule fitted to 6 training reactions at node CHY
    Total Standard Deviation in ln(k): 13.890143202597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node CHY
Total Standard Deviation in ln(k): 13.890143202597""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node CHY
Total Standard Deviation in ln(k): 13.890143202597
""",
)

entry(
    index = 4,
    label = "CY2",
    kinetics = ArrheniusBM(A=(1.58816e+25,'m^3/(mol*s)'), n=-5.79515, w0=(548450,'J/mol'), E0=(278693,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.6479134875461863, var=256.64028572252084, Tref=1000.0, N=10, data_mean=0.0, correlation='CY2',), comment="""BM rule fitted to 10 training reactions at node CY2
    Total Standard Deviation in ln(k): 36.25633493915244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node CY2
Total Standard Deviation in ln(k): 36.25633493915244""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node CY2
Total Standard Deviation in ln(k): 36.25633493915244
""",
)

entry(
    index = 5,
    label = "CF2",
    kinetics = ArrheniusBM(A=(3.78235e+10,'m^3/(mol*s)'), n=-1.48902, w0=(564929,'J/mol'), E0=(260025,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2448976328051893, var=284.7366677957348, Tref=1000.0, N=7, data_mean=0.0, correlation='CF2',), comment="""BM rule fitted to 7 training reactions at node CF2
    Total Standard Deviation in ln(k): 36.9560678416775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node CF2
Total Standard Deviation in ln(k): 36.9560678416775""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node CF2
Total Standard Deviation in ln(k): 36.9560678416775
""",
)

entry(
    index = 6,
    label = "CH2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(2.33736e+17,'m^3/(mol*s)'), n=-4.54388, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CH2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(4.61758e+07,'m^3/(mol*s)'), n=-0.400452, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0419529894091338, var=0.11001473470189202, Tref=1000.0, N=12, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s',), comment="""BM rule fitted to 12 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
    Total Standard Deviation in ln(k): 0.7703494571952924"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
Total Standard Deviation in ln(k): 0.7703494571952924""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
Total Standard Deviation in ln(k): 0.7703494571952924
""",
)

entry(
    index = 8,
    label = "CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H",
    kinetics = ArrheniusBM(A=(4.98836e-05,'m^3/(mol*s)'), n=3.3876, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07373729182154777, var=0.6317192248308732, Tref=1000.0, N=3, data_mean=0.0, correlation='CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H',), comment="""BM rule fitted to 3 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
    Total Standard Deviation in ln(k): 1.778648383863892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 1.778648383863892""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 1.778648383863892
""",
)

entry(
    index = 9,
    label = "CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H",
    kinetics = ArrheniusBM(A=(9.40452e-26,'m^3/(mol*s)'), n=9.1652, w0=(614167,'J/mol'), E0=(61416.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3550268235468481, var=77.29051119679426, Tref=1000.0, N=3, data_mean=0.0, correlation='CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H',), comment="""BM rule fitted to 3 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
    Total Standard Deviation in ln(k): 18.516660068290715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 18.516660068290715""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 18.516660068290715
""",
)

entry(
    index = 10,
    label = "CY2_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(447000,'J/mol'), E0=(44700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY2_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CY2_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY2_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY2_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(8.36677e-05,'m^3/(mol*s)'), n=2.6422, w0=(541500,'J/mol'), E0=(54150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.6030037174699305, var=4.474280122311449, Tref=1000.0, N=2, data_mean=0.0, correlation='CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 2 training reactions at node CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 8.268162247440944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 8.268162247440944""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 8.268162247440944
""",
)

entry(
    index = 12,
    label = "CF2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.33582e-06,'m^3/(mol*s)'), n=3.3552, w0=(658000,'J/mol'), E0=(369109,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CF2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node CF2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CF2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CF2_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(2.00698e-39,'m^3/(mol*s)'), n=13.0386, w0=(549417,'J/mol'), E0=(-28985.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.183636016711576, var=41.63145094559093, Tref=1000.0, N=6, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 6 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 13.39643663908338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 13.39643663908338""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 13.39643663908338
""",
)

entry(
    index = 14,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.89529e+06,'m^3/(mol*s)'), n=0.011582, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020986416531298856, var=0.0724196226211752, Tref=1000.0, N=3, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 3 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.5922218252841055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.5922218252841055""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.5922218252841055
""",
)

entry(
    index = 15,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.33863e+08,'m^3/(mol*s)'), n=-0.537796, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.048941846078904706, var=0.08258735315105603, Tref=1000.0, N=9, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.6990905386106443"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6990905386106443""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6990905386106443
""",
)

entry(
    index = 16,
    label = "CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(1.50896,'m^3/(mol*s)'), n=2.11145, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(1.81858e-05,'m^3/(mol*s)'), n=3.49325, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2216614596813846, var=0.3883872655048153, Tref=1000.0, N=2, data_mean=0.0, correlation='CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 4.318866571931314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 4.318866571931314""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 4.318866571931314
""",
)

entry(
    index = 18,
    label = "CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(0.00948844,'m^3/(mol*s)'), n=2.40423, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_3Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(1.06713e-37,'m^3/(mol*s)'), n=12.6766, w0=(556000,'J/mol'), E0=(55600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.120124765589443, var=13.16559085515051, Tref=1000.0, N=2, data_mean=0.0, correlation='CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 27.676388349346496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 27.676388349346496""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 27.676388349346496
""",
)

entry(
    index = 20,
    label = "CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCbCdCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(0.109762,'m^3/(mol*s)'), n=1.4247, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCbCdCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCbCdCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCbCdCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCbCdCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCbCdCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(739000,'m^3/(mol*s)'), n=0, w0=(500000,'J/mol'), E0=(50000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCbCdCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCbCdCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCbCdCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY2_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCbCdCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H",
    kinetics = ArrheniusBM(A=(3.26413e-09,'m^3/(mol*s)'), n=4.30786, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H",
    kinetics = ArrheniusBM(A=(3.95372e-25,'m^3/(mol*s)'), n=8.69645, w0=(533900,'J/mol'), E0=(-37611.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1106259148931465, var=19.16925284775985, Tref=1000.0, N=5, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H',), comment="""BM rule fitted to 5 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H
    Total Standard Deviation in ln(k): 11.567789887096158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 11.567789887096158""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 11.567789887096158
""",
)

entry(
    index = 24,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.23333e+06,'m^3/(mol*s)'), n=-0.146, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.05212e+06,'m^3/(mol*s)'), n=0.0895127, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.47428387515166337, var=0.06288991772562845, Tref=1000.0, N=2, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.6944127300954472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472
""",
)

entry(
    index = 26,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.43491e+08,'m^3/(mol*s)'), n=-0.665687, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.054507644641452926, var=0.030906577146168814, Tref=1000.0, N=6, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.4893916509466332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332
""",
)

entry(
    index = 27,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R",
    kinetics = ArrheniusBM(A=(2.13e+07,'m^3/(mol*s)'), n=-0.274, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.325e+06,'m^3/(mol*s)'), n=0.0073, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(33.15,'m^3/(mol*s)'), n=1.475, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_3Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.13948,'m^3/(mol*s)'), n=1.96174, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_3Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_3Cl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_3Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_3Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_N-3Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.39739,'m^3/(mol*s)'), n=2.08325, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_N-3Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_N-3Cl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_N-3Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->Br1s_N-3Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_3Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.93293e-05,'m^3/(mol*s)'), n=3.0651, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_3Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_3Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_3Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_3Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_N-3Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.000582952,'m^3/(mol*s)'), n=2.73661, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_N-3Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_N-3Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_N-3Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-3Br1sCl1sF1sI1s->F1s_N-3Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_4Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(3.98081e-09,'m^3/(mol*s)'), n=4.16158, w0=(730500,'J/mol'), E0=(145905,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_4Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_4Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.91368e-07,'m^3/(mol*s)'), n=3.16976, w0=(484750,'J/mol'), E0=(46495.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.40497953669014153, var=8.013816699056477, Tref=1000.0, N=4, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 4 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 6.692677988913652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.692677988913652""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.692677988913652
""",
)

entry(
    index = 36,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4933.33,'m^3/(mol*s)'), n=0.797, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(36700,'m^3/(mol*s)'), n=0.498, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(4.06627e+08,'m^3/(mol*s)'), n=-0.685418, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05364796386969384, var=0.029065280330606118, Tref=1000.0, N=5, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 5 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
    Total Standard Deviation in ln(k): 0.4765719918873029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.4765719918873029""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.4765719918873029
""",
)

entry(
    index = 39,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(321,'m^3/(mol*s)'), n=0, w0=(447000,'J/mol'), E0=(44700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(76002.3,'m^3/(mol*s)'), n=-0.0861778, w0=(497333,'J/mol'), E0=(100496,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06015571945358966, var=0.3784099523471752, Tref=1000.0, N=3, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 3 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 1.384358507033966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 1.384358507033966""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 1.384358507033966
""",
)

entry(
    index = 41,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(70000,'m^3/(mol*s)'), n=0.465, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.54161e+08,'m^3/(mol*s)'), n=-0.709186, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.052492247434476294, var=0.01116623172253938, Tref=1000.0, N=4, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.34373121019806296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.34373121019806296""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.34373121019806296
""",
)

entry(
    index = 43,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.53881,'m^3/(mol*s)'), n=1.26919, w0=(583000,'J/mol'), E0=(96168.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_4Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.63226e-07,'m^3/(mol*s)'), n=3.20783, w0=(454500,'J/mol'), E0=(45450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5438904038945364, var=0.008206778568974105, Tref=1000.0, N=2, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 1.5481703045100408"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.5481703045100408""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.5481703045100408
""",
)

entry(
    index = 45,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.91963e+09,'m^3/(mol*s)'), n=-0.927006, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.787034462320638, var=0.09796882358847864, Tref=1000.0, N=2, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.6049550376933333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933333""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933333
""",
)

entry(
    index = 46,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.985e+07,'m^3/(mol*s)'), n=-0.324, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(203,'m^3/(mol*s)'), n=1.249, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sH->Br1s",
    kinetics = ArrheniusBM(A=(3200,'m^3/(mol*s)'), n=0, w0=(380000,'J/mol'), E0=(38000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sH->Br1s',), comment="""BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sH->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sH->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sH->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sH->Br1s",
    kinetics = ArrheniusBM(A=(214000,'m^3/(mol*s)'), n=0, w0=(529000,'J/mol'), E0=(113414,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sH->Br1s',), comment="""BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sH->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sH->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CF2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHI1sNOSSidSis->H_N-4Br1sCl1sF1s->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sH->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(131500,'m^3/(mol*s)'), n=0.313, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.08e+07,'m^3/(mol*s)'), n=-0.272, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sHI1sNOSSidSis->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

