#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(690.728,'m^3/(mol*s)'), n=1.18525, w0=(594667,'J/mol'), E0=(112441,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18212324863436316, var=2.3267629471429303, Tref=1000.0, N=15, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 15 training reactions at node Root
    Total Standard Deviation in ln(k): 3.515564965141919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 3.515564965141919""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 3.515564965141919
""",
)

entry(
    index = 2,
    label = "Root_2HVal7->Val7",
    kinetics = ArrheniusBM(A=(4.9474e-66,'m^3/(mol*s)'), n=19.9969, w0=(637333,'J/mol'), E0=(7130.25,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.292374760735473, var=368.7697449956288, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2HVal7->Val7',), comment="""BM rule fitted to 3 training reactions at node Root_2HVal7->Val7
    Total Standard Deviation in ln(k): 41.74485920636278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2HVal7->Val7
Total Standard Deviation in ln(k): 41.74485920636278""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2HVal7->Val7
Total Standard Deviation in ln(k): 41.74485920636278
""",
)

entry(
    index = 3,
    label = "Root_N-2HVal7->Val7",
    kinetics = ArrheniusBM(A=(4.61758e+07,'m^3/(mol*s)'), n=-0.400452, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0419529894091338, var=0.11001473470189206, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2HVal7->Val7',), comment="""BM rule fitted to 12 training reactions at node Root_N-2HVal7->Val7
    Total Standard Deviation in ln(k): 0.7703494571952925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2HVal7->Val7
Total Standard Deviation in ln(k): 0.7703494571952925""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2HVal7->Val7
Total Standard Deviation in ln(k): 0.7703494571952925
""",
)

entry(
    index = 4,
    label = "Root_2HVal7->Val7_3HVal7->Val7",
    kinetics = ArrheniusBM(A=(4.94288e-91,'m^3/(mol*s)'), n=27.4825, w0=(642500,'J/mol'), E0=(43149.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=11.472248446017062, var=127.32258716438885, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2HVal7->Val7_3HVal7->Val7',), comment="""BM rule fitted to 2 training reactions at node Root_2HVal7->Val7_3HVal7->Val7
    Total Standard Deviation in ln(k): 51.44563634618226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2HVal7->Val7_3HVal7->Val7
Total Standard Deviation in ln(k): 51.44563634618226""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2HVal7->Val7_3HVal7->Val7
Total Standard Deviation in ln(k): 51.44563634618226
""",
)

entry(
    index = 5,
    label = "Root_2HVal7->Val7_N-3HVal7->Val7",
    kinetics = ArrheniusBM(A=(2.25e+11,'m^3/(mol*s)'), n=-2.85, w0=(627000,'J/mol'), E0=(62700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2HVal7->Val7_N-3HVal7->Val7',), comment="""BM rule fitted to 1 training reactions at node Root_2HVal7->Val7_N-3HVal7->Val7
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2HVal7->Val7_N-3HVal7->Val7
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2HVal7->Val7_N-3HVal7->Val7
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs",
    kinetics = ArrheniusBM(A=(1.89529e+06,'m^3/(mol*s)'), n=0.011582, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020986416531298856, var=0.0724196226211752, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs
    Total Standard Deviation in ln(k): 0.5922218252841055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs
Total Standard Deviation in ln(k): 0.5922218252841055""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs
Total Standard Deviation in ln(k): 0.5922218252841055
""",
)

entry(
    index = 7,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs",
    kinetics = ArrheniusBM(A=(1.33863e+08,'m^3/(mol*s)'), n=-0.537796, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04894184607890469, var=0.08258735315105603, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs
    Total Standard Deviation in ln(k): 0.6990905386106441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs
Total Standard Deviation in ln(k): 0.6990905386106441""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs
Total Standard Deviation in ln(k): 0.6990905386106441
""",
)

entry(
    index = 8,
    label = "Root_2HVal7->Val7_3HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->H",
    kinetics = ArrheniusBM(A=(1.7,'m^3/(mol*s)'), n=-0.71, w0=(627000,'J/mol'), E0=(62700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2HVal7->Val7_3HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->H',), comment="""BM rule fitted to 1 training reactions at node Root_2HVal7->Val7_3HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2HVal7->Val7_3HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2HVal7->Val7_3HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_2HVal7->Val7_3HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->H",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(658000,'J/mol'), E0=(310915,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2HVal7->Val7_3HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->H',), comment="""BM rule fitted to 1 training reactions at node Root_2HVal7->Val7_3HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2HVal7->Val7_3HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2HVal7->Val7_3HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.23333e+06,'m^3/(mol*s)'), n=-0.146, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.05212e+06,'m^3/(mol*s)'), n=0.0895127, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.47428387515166337, var=0.06288991772562845, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.6944127300954472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472
""",
)

entry(
    index = 12,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.43491e+08,'m^3/(mol*s)'), n=-0.665687, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.054507644641452926, var=0.030906577146168814, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.4893916509466332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332
""",
)

entry(
    index = 13,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-4CdCtH-R",
    kinetics = ArrheniusBM(A=(2.13e+07,'m^3/(mol*s)'), n=-0.274, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-4CdCtH-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-4CdCtH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-4CdCtH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-4CdCtH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_4CdCtH->Ct",
    kinetics = ArrheniusBM(A=(33.15,'m^3/(mol*s)'), n=1.475, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_4CdCtH->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_4CdCtH->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_4CdCtH->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_4CdCtH->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_N-4CdCtH->Ct",
    kinetics = ArrheniusBM(A=(1.325e+06,'m^3/(mol*s)'), n=0.0073, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_N-4CdCtH->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_N-4CdCtH->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_N-4CdCtH->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_N-4CdCtH->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4933.33,'m^3/(mol*s)'), n=0.797, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R",
    kinetics = ArrheniusBM(A=(8.08467e+08,'m^3/(mol*s)'), n=-0.805426, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7628799519680863, var=0.11885162711485256, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R
    Total Standard Deviation in ln(k): 2.6079134971899918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R
Total Standard Deviation in ln(k): 2.6079134971899918""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R
Total Standard Deviation in ln(k): 2.6079134971899918
""",
)

entry(
    index = 18,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(2.12655e+08,'m^3/(mol*s)'), n=-0.597643, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05578433882221202, var=0.019976814935947766, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 0.42350962991884356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 0.42350962991884356""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 0.42350962991884356
""",
)

entry(
    index = 19,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(70000,'m^3/(mol*s)'), n=0.465, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_4CdCtH-inRing",
    kinetics = ArrheniusBM(A=(1.08e+07,'m^3/(mol*s)'), n=-0.272, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_4CdCtH-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_4CdCtH-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_4CdCtH-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_4CdCtH-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_N-4CdCtH-inRing",
    kinetics = ArrheniusBM(A=(36700,'m^3/(mol*s)'), n=0.498, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_N-4CdCtH-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_N-4CdCtH-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_N-4CdCtH-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Ext-4CdCtH-R_N-4CdCtH-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(131500,'m^3/(mol*s)'), n=0.313, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CdCtH->Ct",
    kinetics = ArrheniusBM(A=(203,'m^3/(mol*s)'), n=1.249, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CdCtH->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CdCtH->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CdCtH->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_4CdCtH->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CdCtH->Ct",
    kinetics = ArrheniusBM(A=(1.985e+07,'m^3/(mol*s)'), n=-0.324, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CdCtH->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CdCtH->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CdCtH->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2HVal7->Val7_N-4CbCdCsCtHNOSSidSisVal7->Cs_Ext-4CdCtH-R_Ext-6R!H-R_Sp-7R!H-6R!H_N-4CdCtH->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

