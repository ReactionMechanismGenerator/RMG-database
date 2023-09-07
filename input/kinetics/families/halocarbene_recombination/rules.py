#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_recombination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(105316,'m^3/(mol*s)'), n=0.635901, w0=(183.269,'kJ/mol'), E0=(88.5797,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09478083976984558, var=0.6936703555024497, Tref=1000.0, N=13, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 13 training reactions at node Root
    Total Standard Deviation in ln(k): 1.9078240124162698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 1.9078240124162698""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 1.9078240124162698
""",
)

entry(
    index = 2,
    label = "Root_3R->H",
    kinetics = ArrheniusBM(A=(0.00482768,'m^3/(mol*s)'), n=1.71263, w0=(205.5,'kJ/mol'), E0=(20.55,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1781102561419967, var=959.4770686989515, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H
    Total Standard Deviation in ln(k): 65.05760076906172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H
Total Standard Deviation in ln(k): 65.05760076906172""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H
Total Standard Deviation in ln(k): 65.05760076906172
""",
)

entry(
    index = 3,
    label = "Root_3R->H_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.75,'m^3/(mol*s)'), n=-0.32, w0=(205.5,'kJ/mol'), E0=(137.257,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_3R->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=-3.9067e-08, w0=(205.5,'kJ/mol'), E0=(74.2853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-3R->H",
    kinetics = ArrheniusBM(A=(87090.7,'m^3/(mol*s)'), n=0.660775, w0=(179.227,'kJ/mol'), E0=(88.1566,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09352226906501894, var=0.3127676357143438, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H
    Total Standard Deviation in ln(k): 1.3561413451238655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 1.3561413451238655""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 1.3561413451238655
""",
)

entry(
    index = 6,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(128827,'m^3/(mol*s)'), n=0.469398, w0=(175,'kJ/mol'), E0=(77.0552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009898522871762284, var=0.3372166703721302, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 1.189027535795669"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 1.189027535795669""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 1.189027535795669
""",
)

entry(
    index = 7,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(285822,'m^3/(mol*s)'), n=0.494398, w0=(173,'kJ/mol'), E0=(99.7128,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5345454069444686, var=2.9622770268594745, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 4.7934819272896565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.7934819272896565""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.7934819272896565
""",
)

entry(
    index = 8,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00976185,'m^3/(mol*s)'), n=2.64543, w0=(173,'kJ/mol'), E0=(60.0344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24524072153041726, var=3.368891203868511, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 4.2957816346285345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.2957816346285345""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.2957816346285345
""",
)

entry(
    index = 9,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_4R!H->Br",
    kinetics = ArrheniusBM(A=(0.000635481,'m^3/(mol*s)'), n=2.96807, w0=(173,'kJ/mol'), E0=(63.7234,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_4R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(0.0386382,'m^3/(mol*s)'), n=2.48543, w0=(173,'kJ/mol'), E0=(60.0344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08388401003596499, var=10.980821498669028, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br
    Total Standard Deviation in ln(k): 6.85391914535648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br
Total Standard Deviation in ln(k): 6.85391914535648""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br
Total Standard Deviation in ln(k): 6.85391914535648
""",
)

entry(
    index = 11,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_4ClF->Cl",
    kinetics = ArrheniusBM(A=(0.00385582,'m^3/(mol*s)'), n=2.7545, w0=(173,'kJ/mol'), E0=(67.0601,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_4ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_N-4ClF->Cl",
    kinetics = ArrheniusBM(A=(786.723,'m^3/(mol*s)'), n=1.25031, w0=(173,'kJ/mol'), E0=(51.8105,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_N-4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_N-4ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_N-4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_N-4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(458326,'m^3/(mol*s)'), n=0.413569, w0=(173,'kJ/mol'), E0=(70.7117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(47833.9,'m^3/(mol*s)'), n=0.584758, w0=(179,'kJ/mol'), E0=(75.2892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08427309479016018, var=2.85064993170164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 3.596509653883644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.596509653883644""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.596509653883644
""",
)

entry(
    index = 15,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-1C2s-R",
    kinetics = ArrheniusBM(A=(0.00128024,'m^3/(mol*s)'), n=2.72845, w0=(179,'kJ/mol'), E0=(56.9635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-1C2s-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-1C2s-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-1C2s-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-1C2s-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-3R->H_2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.58997e+07,'m^3/(mol*s)'), n=-1.99907e-07, w0=(163.5,'kJ/mol'), E0=(53.9233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.2084459636251595e-09, var=0.000316451145076372, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 0.035662393238423296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 0.035662393238423296""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 0.035662393238423296
""",
)

entry(
    index = 17,
    label = "Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.58e+07,'m^3/(mol*s)'), n=-5.18483e-08, w0=(163.5,'kJ/mol'), E0=(58.466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl
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
    index = 18,
    label = "Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.6e+07,'m^3/(mol*s)'), n=9.14635e-09, w0=(163.5,'kJ/mol'), E0=(52.8664,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl
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
    index = 19,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(931900,'m^3/(mol*s)'), n=0.371805, w0=(198.167,'kJ/mol'), E0=(96.2459,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04499885252756342, var=1.229174869982976, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 2.3356753184590615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.3356753184590615""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.3356753184590615
""",
)

entry(
    index = 20,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(518506,'m^3/(mol*s)'), n=0.4717, w0=(242.5,'kJ/mol'), E0=(89.8312,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(1587.78,'m^3/(mol*s)'), n=1.13913, w0=(176,'kJ/mol'), E0=(54.4331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12186324298938127, var=0.4224073205344201, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F
    Total Standard Deviation in ln(k): 1.6091239238388217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F
Total Standard Deviation in ln(k): 1.6091239238388217""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F
Total Standard Deviation in ln(k): 1.6091239238388217
""",
)

entry(
    index = 22,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_3CClO->C",
    kinetics = ArrheniusBM(A=(2.1e+07,'m^3/(mol*s)'), n=-0.207, w0=(173,'kJ/mol'), E0=(54.225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_3CClO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_3CClO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_3CClO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_3CClO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_N-3CClO->C",
    kinetics = ArrheniusBM(A=(37018.9,'m^3/(mol*s)'), n=0.7539, w0=(179,'kJ/mol'), E0=(86.2083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_N-3CClO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_N-3CClO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_N-3CClO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_N-3CClO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

