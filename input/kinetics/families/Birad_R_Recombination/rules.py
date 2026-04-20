#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.25564e+08,'m^3/(mol*s)'), n=-0.0635841, w0=(156071,'J/mol'), E0=(15607.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.476812641179286e-05, var=33.368379837283236, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 11.580589105426649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 11.580589105426649""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 11.580589105426649
""",
)

entry(
    index = 2,
    label = "Root_2R->H",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.21648e-07, w0=(201333,'J/mol'), E0=(20133.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1858725180105822e-08, var=1.6421466378806452e-47, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2R->H',), comment="""BM rule fitted to 3 training reactions at node Root_2R->H
    Total Standard Deviation in ln(k): 5.4921420050517145e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2R->H
Total Standard Deviation in ln(k): 5.4921420050517145e-08""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2R->H
Total Standard Deviation in ln(k): 5.4921420050517145e-08
""",
)

entry(
    index = 3,
    label = "Root_N-2R->H",
    kinetics = ArrheniusBM(A=(1.28629e+08,'m^3/(mol*s)'), n=-0.0641885, w0=(122125,'J/mol'), E0=(12212.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01904387619779723, var=34.85684083820902, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2R->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-2R->H
    Total Standard Deviation in ln(k): 11.88374113782806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2R->H
Total Standard Deviation in ln(k): 11.88374113782806""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2R->H
Total Standard Deviation in ln(k): 11.88374113782806
""",
)

entry(
    index = 4,
    label = "Root_2R->H_1R!H->N",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(193000,'J/mol'), E0=(19300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2R->H_1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_2R->H_1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2R->H_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2R->H_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_2R->H_N-1R!H->N",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.28714e-07, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2R->H_N-1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_2R->H_N-1R!H->N
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R->H_N-1R!H->N
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R->H_N-1R!H->N
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 6,
    label = "Root_N-2R->H_1R!H->S",
    kinetics = ArrheniusBM(A=(1.3e+08,'m^3/(mol*s)'), n=0.24, w0=(233500,'J/mol'), E0=(23350,'J/mol'), Tmin=(300,'K'), Tmax=(800,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2R->H_1R!H->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-2R->H_1R!H->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2R->H_1R!H->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2R->H_1R!H->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-2R->H_N-1R!H->S",
    kinetics = ArrheniusBM(A=(1.27293e+08,'m^3/(mol*s)'), n=-0.364536, w0=(85000,'J/mol'), E0=(8500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8230805481624328, var=6.779062860587488, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S',), comment="""BM rule fitted to 3 training reactions at node Root_N-2R->H_N-1R!H->S
    Total Standard Deviation in ln(k): 9.800259647712998"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2R->H_N-1R!H->S
Total Standard Deviation in ln(k): 9.800259647712998""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2R->H_N-1R!H->S
Total Standard Deviation in ln(k): 9.800259647712998
""",
)

entry(
    index = 8,
    label = "Root_2R->H_N-1R!H->N_1OS->O",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2R->H_N-1R!H->N_1OS->O',), comment="""BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->N_1OS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->N_1OS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->N_1OS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_2R->H_N-1R!H->N_N-1OS->O",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(181500,'J/mol'), E0=(18150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2R->H_N-1R!H->N_N-1OS->O',), comment="""BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->N_N-1OS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->N_N-1OS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->N_N-1OS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(4.84265e+08,'m^3/(mol*s)'), n=-0.296706, w0=(77250,'J/mol'), E0=(7725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22847199987885733, var=0.037066746561070354, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi
    Total Standard Deviation in ln(k): 0.9600164061664607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi
Total Standard Deviation in ln(k): 0.9600164061664607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi
Total Standard Deviation in ln(k): 0.9600164061664607
""",
)

entry(
    index = 11,
    label = "Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(349106,'m^3/(mol*s)'), n=0.389287, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->N",
    kinetics = ArrheniusBM(A=(1.42e+10,'m^3/(mol*s)'), n=-0.75, w0=(83500,'J/mol'), E0=(8350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->N",
    kinetics = ArrheniusBM(A=(226935,'m^3/(mol*s)'), n=0.706701, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

