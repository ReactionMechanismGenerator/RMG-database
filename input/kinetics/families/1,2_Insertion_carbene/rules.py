#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.93491e+36,'m^3/(mol*s)'), n=-9.17724, w0=(564792,'J/mol'), E0=(214740,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5025252236484723, var=11.036430015563166, Tref=1000.0, N=24, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 24 training reactions at node Root
    Total Standard Deviation in ln(k): 7.922581213245513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root
Total Standard Deviation in ln(k): 7.922581213245513""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root
Total Standard Deviation in ln(k): 7.922581213245513
""",
)

entry(
    index = 2,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R",
    kinetics = ArrheniusBM(A=(4.61758e+07,'m^3/(mol*s)'), n=-0.400452, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0419529894091338, var=0.11001473470189206, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R
    Total Standard Deviation in ln(k): 0.7703494571952925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R
Total Standard Deviation in ln(k): 0.7703494571952925""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R
Total Standard Deviation in ln(k): 0.7703494571952925
""",
)

entry(
    index = 3,
    label = "Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H",
    kinetics = ArrheniusBM(A=(3.38286e-50,'m^3/(mol*s)'), n=14.5469, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=13.56175112502634, var=636.9627343906748, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H',), comment="""BM rule fitted to 2 training reactions at node Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
    Total Standard Deviation in ln(k): 84.67049734272022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 84.67049734272022""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 84.67049734272022
""",
)

entry(
    index = 4,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H",
    kinetics = ArrheniusBM(A=(12.2263,'m^3/(mol*s)'), n=0.869868, w0=(529300,'J/mol'), E0=(101477,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.40433684912688056, var=39.67342789818601, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
    Total Standard Deviation in ln(k): 13.64311572362326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 13.64311572362326""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H
Total Standard Deviation in ln(k): 13.64311572362326
""",
)

entry(
    index = 5,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.89529e+06,'m^3/(mol*s)'), n=0.011582, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020986416531298856, var=0.0724196226211752, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.5922218252841055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.5922218252841055""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.5922218252841055
""",
)

entry(
    index = 6,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.33863e+08,'m^3/(mol*s)'), n=-0.537796, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04894184607890469, var=0.08258735315105603, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.6990905386106441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6990905386106441""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6990905386106441
""",
)

entry(
    index = 7,
    label = "Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(2.25e+11,'m^3/(mol*s)'), n=-2.85, w0=(627000,'J/mol'), E0=(62700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(1.7,'m^3/(mol*s)'), n=-0.71, w0=(627000,'J/mol'), E0=(62700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_4Br1sCdCl1sCsCtF1s->F1s",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(658000,'J/mol'), E0=(308055,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_4Br1sCdCl1sCsCtF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_4Br1sCdCl1sCsCtF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_4Br1sCdCl1sCsCtF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_4Br1sCdCl1sCsCtF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s",
    kinetics = ArrheniusBM(A=(21.1428,'m^3/(mol*s)'), n=0.728737, w0=(515000,'J/mol'), E0=(64380.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3510979281690037, var=8.65805767085418, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s',), comment="""BM rule fitted to 9 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s
    Total Standard Deviation in ln(k): 6.781003884137905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s
Total Standard Deviation in ln(k): 6.781003884137905""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s
Total Standard Deviation in ln(k): 6.781003884137905
""",
)

entry(
    index = 11,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.23333e+06,'m^3/(mol*s)'), n=-0.146, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.05212e+06,'m^3/(mol*s)'), n=0.0895127, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.47428387515166337, var=0.06288991772562845, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.6944127300954472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472
""",
)

entry(
    index = 13,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.43491e+08,'m^3/(mol*s)'), n=-0.665687, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.054507644641452926, var=0.030906577146168814, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.4893916509466332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332
""",
)

entry(
    index = 14,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCdCl1sCtF1sH-R",
    kinetics = ArrheniusBM(A=(2.13e+07,'m^3/(mol*s)'), n=-0.274, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCdCl1sCtF1sH-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCdCl1sCtF1sH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCdCl1sCtF1sH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCdCl1sCtF1sH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCdCl1sCtF1sH->Ct",
    kinetics = ArrheniusBM(A=(33.15,'m^3/(mol*s)'), n=1.475, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCdCl1sCtF1sH->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCdCl1sCtF1sH->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCdCl1sCtF1sH->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCdCl1sCtF1sH->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCdCl1sCtF1sH->Ct",
    kinetics = ArrheniusBM(A=(1.325e+06,'m^3/(mol*s)'), n=0.0073, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCdCl1sCtF1sH->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCdCl1sCtF1sH->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCdCl1sCtF1sH->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCdCl1sCtF1sH->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(23282.7,'m^3/(mol*s)'), n=-0.144596, w0=(528250,'J/mol'), E0=(52825,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7174598357591814, var=12.189603480199567, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 4 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 8.801917298988151"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 8.801917298988151""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 8.801917298988151
""",
)

entry(
    index = 18,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.73723e-06,'m^3/(mol*s)'), n=2.76727, w0=(504400,'J/mol'), E0=(3641.12,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18895767853771617, var=4.369614112953192, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 4.6653904564994395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 4.6653904564994395""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 4.6653904564994395
""",
)

entry(
    index = 19,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4933.33,'m^3/(mol*s)'), n=0.797, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R",
    kinetics = ArrheniusBM(A=(8.08467e+08,'m^3/(mol*s)'), n=-0.805426, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7628799519680863, var=0.11885162711485256, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R
    Total Standard Deviation in ln(k): 2.6079134971899918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R
Total Standard Deviation in ln(k): 2.6079134971899918""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R
Total Standard Deviation in ln(k): 2.6079134971899918
""",
)

entry(
    index = 21,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(2.12655e+08,'m^3/(mol*s)'), n=-0.597643, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05578433882221202, var=0.019976814935947766, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 0.42350962991884356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 0.42350962991884356""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 0.42350962991884356
""",
)

entry(
    index = 22,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(70000,'m^3/(mol*s)'), n=0.465, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(447000,'J/mol'), E0=(44700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(302939,'m^3/(mol*s)'), n=-0.602721, w0=(555333,'J/mol'), E0=(55533.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.039338863304941726, var=2.030759405409962, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 2.955683391701264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 2.955683391701264""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 2.955683391701264
""",
)

entry(
    index = 25,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(4.93149e-06,'m^3/(mol*s)'), n=2.47357, w0=(537667,'J/mol'), E0=(-3376.47,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22920177759989974, var=4.738235607645339, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 4.939688661381655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 4.939688661381655""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 4.939688661381655
""",
)

entry(
    index = 26,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.63226e-07,'m^3/(mol*s)'), n=3.20783, w0=(454500,'J/mol'), E0=(45450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5438904038945364, var=0.008206778568974105, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 1.5481703045100408"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.5481703045100408""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.5481703045100408
""",
)

entry(
    index = 27,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_4Br1sCdCl1sCtF1sH-inRing",
    kinetics = ArrheniusBM(A=(1.08e+07,'m^3/(mol*s)'), n=-0.272, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_4Br1sCdCl1sCtF1sH-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_4Br1sCdCl1sCtF1sH-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_4Br1sCdCl1sCtF1sH-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_4Br1sCdCl1sCtF1sH-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_N-4Br1sCdCl1sCtF1sH-inRing",
    kinetics = ArrheniusBM(A=(36700,'m^3/(mol*s)'), n=0.498, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_N-4Br1sCdCl1sCtF1sH-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_N-4Br1sCdCl1sCtF1sH-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_N-4Br1sCdCl1sCtF1sH-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Ext-4Br1sCdCl1sCtF1sH-R_N-4Br1sCdCl1sCtF1sH-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(131500,'m^3/(mol*s)'), n=0.313, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_4Br1sCdCl1sCtF1sH->Ct",
    kinetics = ArrheniusBM(A=(203,'m^3/(mol*s)'), n=1.249, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_4Br1sCdCl1sCtF1sH->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_4Br1sCdCl1sCtF1sH->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_4Br1sCdCl1sCtF1sH->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_4Br1sCdCl1sCtF1sH->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_N-4Br1sCdCl1sCtF1sH->Ct",
    kinetics = ArrheniusBM(A=(1.985e+07,'m^3/(mol*s)'), n=-0.324, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_N-4Br1sCdCl1sCtF1sH->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_N-4Br1sCdCl1sCtF1sH->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_N-4Br1sCdCl1sCtF1sH->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H-6R!H_N-4Br1sCdCl1sCtF1sH->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H",
    kinetics = ArrheniusBM(A=(6.21796e+08,'m^3/(mol*s)'), n=-1.68024, w0=(583000,'J/mol'), E0=(-40149,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.480938579353241, var=7.009747379363687, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H
    Total Standard Deviation in ln(k): 6.516110450515046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H
Total Standard Deviation in ln(k): 6.516110450515046""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H
Total Standard Deviation in ln(k): 6.516110450515046
""",
)

entry(
    index = 33,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCsH->H",
    kinetics = ArrheniusBM(A=(739000,'m^3/(mol*s)'), n=0, w0=(500000,'J/mol'), E0=(50000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCsH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCsH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCsH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-5Br1sCsH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.00824e-07,'m^3/(mol*s)'), n=3.1317, w0=(515000,'J/mol'), E0=(580.194,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5486944081657859, var=11.420385480293012, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s
    Total Standard Deviation in ln(k): 10.66600589758599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s
Total Standard Deviation in ln(k): 10.66600589758599""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s
Total Standard Deviation in ln(k): 10.66600589758599
""",
)

entry(
    index = 35,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_N-2F1sH->F1s",
    kinetics = ArrheniusBM(A=(2.33736e+17,'m^3/(mol*s)'), n=-4.54388, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_N-2F1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_N-2F1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_N-2F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_N-2F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(214000,'m^3/(mol*s)'), n=0, w0=(529000,'J/mol'), E0=(113414,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(3200,'m^3/(mol*s)'), n=0, w0=(380000,'J/mol'), E0=(38000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCl1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_3Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.109762,'m^3/(mol*s)'), n=1.4247, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_3Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_3Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_3Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_3Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_N-3Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.01504e+27,'m^3/(mol*s)'), n=-7.09688, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_N-3Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_N-3Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_N-3Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_5Br1sCsH->H_N-3Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(321,'m^3/(mol*s)'), n=0, w0=(447000,'J/mol'), E0=(44700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(2.53881,'m^3/(mol*s)'), n=1.26919, w0=(583000,'J/mol'), E0=(96168.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->H_N-4Br1sCdCl1sCsCtF1s->F1s_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCl1s->Cl1s_2F1sH->F1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

