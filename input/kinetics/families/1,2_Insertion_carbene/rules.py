#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.61758e+07,'m^3/(mol*s)'), n=-0.400452, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0419529894091338, var=0.11001473470189206, Tref=1000.0, N=12, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 12 training reactions at node Root
    Total Standard Deviation in ln(k): 0.7703494571952925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root
Total Standard Deviation in ln(k): 0.7703494571952925""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root
Total Standard Deviation in ln(k): 0.7703494571952925
""",
)

entry(
    index = 2,
    label = "Root_4CbCdCsCtHNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.89529e+06,'m^3/(mol*s)'), n=0.011582, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020986416531298856, var=0.0724196226211752, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4CbCdCsCtHNOSSidSis->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.5922218252841055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.5922218252841055""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.5922218252841055
""",
)

entry(
    index = 3,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.33863e+08,'m^3/(mol*s)'), n=-0.537796, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04894184607890469, var=0.08258735315105603, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.6990905386106441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6990905386106441""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6990905386106441
""",
)

entry(
    index = 4,
    label = "Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.23333e+06,'m^3/(mol*s)'), n=-0.146, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.05212e+06,'m^3/(mol*s)'), n=0.0895127, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.47428387515166337, var=0.06288991772562845, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.6944127300954472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472
""",
)

entry(
    index = 6,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.43491e+08,'m^3/(mol*s)'), n=-0.665687, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.054507644641452926, var=0.030906577146168814, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.4893916509466332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332
""",
)

entry(
    index = 7,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-4CbCdCtHNOSSidSis-R",
    kinetics = ArrheniusBM(A=(2.13e+07,'m^3/(mol*s)'), n=-0.274, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-4CbCdCtHNOSSidSis-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-4CbCdCtHNOSSidSis-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-4CbCdCtHNOSSidSis-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-4CbCdCtHNOSSidSis-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_4CbCdCtHNOSSidSis->Cd",
    kinetics = ArrheniusBM(A=(1.325e+06,'m^3/(mol*s)'), n=0.0073, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_4CbCdCtHNOSSidSis->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_4CbCdCtHNOSSidSis->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_4CbCdCtHNOSSidSis->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_4CbCdCtHNOSSidSis->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_N-4CbCdCtHNOSSidSis->Cd",
    kinetics = ArrheniusBM(A=(33.15,'m^3/(mol*s)'), n=1.475, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_N-4CbCdCtHNOSSidSis->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_N-4CbCdCtHNOSSidSis->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_N-4CbCdCtHNOSSidSis->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_N-4CbCdCtHNOSSidSis->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4933.33,'m^3/(mol*s)'), n=0.797, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4CbCdCsCtHNOSSidSis->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R",
    kinetics = ArrheniusBM(A=(8.08467e+08,'m^3/(mol*s)'), n=-0.805426, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7628799519680863, var=0.11885162711485256, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R
    Total Standard Deviation in ln(k): 2.6079134971899918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R
Total Standard Deviation in ln(k): 2.6079134971899918""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R
Total Standard Deviation in ln(k): 2.6079134971899918
""",
)

entry(
    index = 12,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(2.12655e+08,'m^3/(mol*s)'), n=-0.597643, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05578433882221202, var=0.019976814935947766, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 0.42350962991884356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 0.42350962991884356""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 0.42350962991884356
""",
)

entry(
    index = 13,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(70000,'m^3/(mol*s)'), n=0.465, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_4CbCdCtHNOSSidSis-inRing",
    kinetics = ArrheniusBM(A=(1.08e+07,'m^3/(mol*s)'), n=-0.272, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_4CbCdCtHNOSSidSis-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_4CbCdCtHNOSSidSis-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_4CbCdCtHNOSSidSis-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_4CbCdCtHNOSSidSis-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_N-4CbCdCtHNOSSidSis-inRing",
    kinetics = ArrheniusBM(A=(36700,'m^3/(mol*s)'), n=0.498, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_N-4CbCdCtHNOSSidSis-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_N-4CbCdCtHNOSSidSis-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_N-4CbCdCtHNOSSidSis-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Ext-4CbCdCtHNOSSidSis-R_N-4CbCdCtHNOSSidSis-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(131500,'m^3/(mol*s)'), n=0.313, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CbCdCtHNOSSidSis->Cd",
    kinetics = ArrheniusBM(A=(1.985e+07,'m^3/(mol*s)'), n=-0.324, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CbCdCtHNOSSidSis->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CbCdCtHNOSSidSis->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CbCdCtHNOSSidSis->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CbCdCtHNOSSidSis->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CbCdCtHNOSSidSis->Cd",
    kinetics = ArrheniusBM(A=(203,'m^3/(mol*s)'), n=1.249, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CbCdCtHNOSSidSis->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CbCdCtHNOSSidSis->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CbCdCtHNOSSidSis->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4CbCdCsCtHNOSSidSis->Cs_Ext-4CbCdCtHNOSSidSis-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CbCdCtHNOSSidSis->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

