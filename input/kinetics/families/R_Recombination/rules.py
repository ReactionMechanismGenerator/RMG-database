#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = ""
longDesc = """
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.28791e+07,'m^3/(mol*s)'), n=-0.046213, w0=(162429,'J/mol'), E0=(5028.22,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06912729734300636, var=8.011539075472735, Tref=1000.0, N=269, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 269 training reactions at node Root
    Total Standard Deviation in ln(k): 5.8480216120922766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 269 training reactions at node Root
Total Standard Deviation in ln(k): 5.8480216120922766""",
    longDesc = 
"""
BM rule fitted to 269 training reactions at node Root
Total Standard Deviation in ln(k): 5.8480216120922766
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(6.71997e+08,'m^3/(mol*s)'), n=-0.457983, w0=(189328,'J/mol'), E0=(18932.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15231348860762392, var=16.174706543936477, Tref=1000.0, N=87, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 87 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 8.445298696990179"""),
    rank = 11,
    shortDesc = """BM rule fitted to 87 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 8.445298696990179""",
    longDesc = 
"""
BM rule fitted to 87 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 8.445298696990179
""",
)

entry(
    index = 3,
    label = "Root_1R->H_N-2R-inRing",
    kinetics = ArrheniusBM(A=(1.94526e+09,'m^3/(mol*s)'), n=-0.657523, w0=(186568,'J/mol'), E0=(18656.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.28624847412313514, var=20.75914428939544, Tref=1000.0, N=73, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing',), comment="""BM rule fitted to 73 training reactions at node Root_1R->H_N-2R-inRing
    Total Standard Deviation in ln(k): 9.853232118209151"""),
    rank = 11,
    shortDesc = """BM rule fitted to 73 training reactions at node Root_1R->H_N-2R-inRing
Total Standard Deviation in ln(k): 9.853232118209151""",
    longDesc = 
"""
BM rule fitted to 73 training reactions at node Root_1R->H_N-2R-inRing
Total Standard Deviation in ln(k): 9.853232118209151
""",
)

entry(
    index = 4,
    label = "Root_1R->H_N-2R-inRing_2R->S",
    kinetics = ArrheniusBM(A=(1.01224e+07,'m^3/(mol*s)'), n=0.564397, w0=(181667,'J/mol'), E0=(18166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.2992478272400607, var=17.01679294351001, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_2R->S',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_2R->S
    Total Standard Deviation in ln(k): 14.046820588596644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_2R->S
Total Standard Deviation in ln(k): 14.046820588596644""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_2R->S
Total Standard Deviation in ln(k): 14.046820588596644
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-2R-inRing_N-2R->S",
    kinetics = ArrheniusBM(A=(1.17275e+10,'m^3/(mol*s)'), n=-1.07499, w0=(186779,'J/mol'), E0=(18677.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3247631711388397, var=21.827274675958144, Tref=1000.0, N=70, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S',), comment="""BM rule fitted to 70 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S
    Total Standard Deviation in ln(k): 10.182043783726249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 70 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S
Total Standard Deviation in ln(k): 10.182043783726249""",
    longDesc = 
"""
BM rule fitted to 70 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S
Total Standard Deviation in ln(k): 10.182043783726249
""",
)

entry(
    index = 6,
    label = "Root_1R->H_N-2R-inRing_2R->S_Ext-2S-R",
    kinetics = ArrheniusBM(A=(6.94752e+06,'m^3/(mol*s)'), n=1.02083, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_2R->S_Ext-2S-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_2R->S_Ext-2S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_2CHNO->N",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0.493, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(200,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_2CHNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_2CHNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_2CHNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_2CHNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N",
    kinetics = ArrheniusBM(A=(1.49283e+10,'m^3/(mol*s)'), n=-1.12324, w0=(188275,'J/mol'), E0=(18827.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3613273903065836, var=22.688909860434602, Tref=1000.0, N=69, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N',), comment="""BM rule fitted to 69 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N
    Total Standard Deviation in ln(k): 10.456987731531031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 69 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N
Total Standard Deviation in ln(k): 10.456987731531031""",
    longDesc = 
"""
BM rule fitted to 69 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N
Total Standard Deviation in ln(k): 10.456987731531031
""",
)

entry(
    index = 9,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(1.62217e+10,'m^3/(mol*s)'), n=-1.14114, w0=(189719,'J/mol'), E0=(18971.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.37891598602926285, var=23.038249281751177, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R',), comment="""BM rule fitted to 64 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R
    Total Standard Deviation in ln(k): 10.574412984212527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R
Total Standard Deviation in ln(k): 10.574412984212527""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R
Total Standard Deviation in ln(k): 10.574412984212527
""",
)

entry(
    index = 10,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_2CHO->H",
    kinetics = ArrheniusBM(A=(30255.8,'m^3/(mol*s)'), n=0.454367, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3774142242586176, var=47.94959741791935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_2CHO->H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_2CHO->H
    Total Standard Deviation in ln(k): 14.830194859219086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_2CHO->H
Total Standard Deviation in ln(k): 14.830194859219086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_2CHO->H
Total Standard Deviation in ln(k): 14.830194859219086
""",
)

entry(
    index = 11,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H",
    kinetics = ArrheniusBM(A=(6.50652e+07,'m^3/(mol*s)'), n=0.123367, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03757162961902423, var=0.10534383787595203, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H
    Total Standard Deviation in ln(k): 0.7450722393365657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H
Total Standard Deviation in ln(k): 0.7450722393365657""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H
Total Standard Deviation in ln(k): 0.7450722393365657
""",
)

entry(
    index = 12,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(2.22137e+11,'m^3/(mol*s)'), n=-1.62312, w0=(189962,'J/mol'), E0=(18996.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6669857114336222, var=46.01196101102668, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C',), comment="""BM rule fitted to 26 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C
    Total Standard Deviation in ln(k): 17.786948749018432"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C
Total Standard Deviation in ln(k): 17.786948749018432""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C
Total Standard Deviation in ln(k): 17.786948749018432
""",
)

entry(
    index = 13,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_2CO->C",
    kinetics = ArrheniusBM(A=(5.37e+07,'m^3/(mol*s)'), n=0.15395, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0638883423777328, var=3.290805964782287, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_2CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_2CO->C
    Total Standard Deviation in ln(k): 6.309791736806655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_2CO->C
Total Standard Deviation in ln(k): 6.309791736806655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_2CO->C
Total Standard Deviation in ln(k): 6.309791736806655
""",
)

entry(
    index = 14,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_N-2CO->C",
    kinetics = ArrheniusBM(A=(1.62e+08,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(2100,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_N-2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_N-2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_N-2CHO->H_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(2.42361e+17,'m^3/(mol*s)'), n=-4.05186, w0=(207938,'J/mol'), E0=(20793.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18680029122949374, var=34.99950426602853, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 12.32943613422403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F
Total Standard Deviation in ln(k): 12.32943613422403""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F
Total Standard Deviation in ln(k): 12.32943613422403
""",
)

entry(
    index = 16,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(2.15628e+08,'m^3/(mol*s)'), n=-0.411157, w0=(161200,'J/mol'), E0=(16120,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.003595877896047, var=72.7148250207673, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F',), comment="""BM rule fitted to 10 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 27.154261168220877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F
Total Standard Deviation in ln(k): 27.154261168220877""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F
Total Standard Deviation in ln(k): 27.154261168220877
""",
)

entry(
    index = 17,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(9.64542e+17,'m^3/(mol*s)'), n=-4.2364, w0=(207400,'J/mol'), E0=(20740,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19153773410054956, var=37.595146131367414, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R
    Total Standard Deviation in ln(k): 12.77325982797745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R
Total Standard Deviation in ln(k): 12.77325982797745""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R
Total Standard Deviation in ln(k): 12.77325982797745
""",
)

entry(
    index = 18,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl",
    kinetics = ArrheniusBM(A=(1.06959e+15,'m^3/(mol*s)'), n=-3.3975, w0=(143857,'J/mol'), E0=(14385.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07059964743699368, var=24.90183646172746, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl
    Total Standard Deviation in ln(k): 10.181362891150272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl
Total Standard Deviation in ln(k): 10.181362891150272""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl
Total Standard Deviation in ln(k): 10.181362891150272
""",
)

entry(
    index = 19,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl",
    kinetics = ArrheniusBM(A=(2.90891e+06,'m^3/(mol*s)'), n=0.42289, w0=(201667,'J/mol'), E0=(20166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.5146295431833976, var=15.527749289962587, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl
    Total Standard Deviation in ln(k): 14.217876428349674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl
Total Standard Deviation in ln(k): 14.217876428349674""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl
Total Standard Deviation in ln(k): 14.217876428349674
""",
)

entry(
    index = 20,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(9.25401e+22,'m^3/(mol*s)'), n=-5.56834, w0=(197571,'J/mol'), E0=(19757.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19176710866949578, var=18.297920683384834, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R
    Total Standard Deviation in ln(k): 9.05729548073755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 9.05729548073755""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 9.05729548073755
""",
)

entry(
    index = 21,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C",
    kinetics = ArrheniusBM(A=(4.03184e+16,'m^3/(mol*s)'), n=-3.61022, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1251049929458495, var=9.586590315811591, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C
    Total Standard Deviation in ln(k): 6.521438888201966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C
Total Standard Deviation in ln(k): 6.521438888201966""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C
Total Standard Deviation in ln(k): 6.521438888201966
""",
)

entry(
    index = 22,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_N-2CHO->C",
    kinetics = ArrheniusBM(A=(1.22604e+11,'m^3/(mol*s)'), n=-2.86567, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9878236278062718, var=1.2163224389741848e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_N-2CHO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_N-2CHO->C
    Total Standard Deviation in ln(k): 2.488960590959757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_N-2CHO->C
Total Standard Deviation in ln(k): 2.488960590959757""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_N-2CHO->C
Total Standard Deviation in ln(k): 2.488960590959757
""",
)

entry(
    index = 23,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS",
    kinetics = ArrheniusBM(A=(2.84566e+06,'m^3/(mol*s)'), n=0.426924, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1994712244511689, var=0.09694164604554087, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS
    Total Standard Deviation in ln(k): 1.1253673375027171"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS
Total Standard Deviation in ln(k): 1.1253673375027171""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS
Total Standard Deviation in ln(k): 1.1253673375027171
""",
)

entry(
    index = 24,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_N-Sp-3OS-2CHOOS",
    kinetics = ArrheniusBM(A=(46800,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(1500,'K'), Tmax=(1900,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_N-Sp-3OS-2CHOOS',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_N-Sp-3OS-2CHOOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_N-Sp-3OS-2CHOOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_N-Sp-3OS-2CHOOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.88466e+19,'m^3/(mol*s)'), n=-4.44659, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13068008073838294, var=22.198593200401746, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R
    Total Standard Deviation in ln(k): 9.77372802011819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R
Total Standard Deviation in ln(k): 9.77372802011819""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R
Total Standard Deviation in ln(k): 9.77372802011819
""",
)

entry(
    index = 26,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_2CHO->C",
    kinetics = ArrheniusBM(A=(500000,'m^3/(mol*s)'), n=0.65, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_2CHO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_2CHO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_2CHO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_2CHO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_N-2CHO->C",
    kinetics = ArrheniusBM(A=(43950,'m^3/(mol*s)'), n=1, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(298,'K'), Tmax=(6000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_N-2CHO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_N-2CHO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_N-2CHO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_N-3ClOS->Cl_Sp-3OS-2CHOOS_N-2CHO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->C",
    kinetics = ArrheniusBM(A=(4.93969e+06,'m^3/(mol*s)'), n=0.0748939, w0=(157079,'J/mol'), E0=(15707.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.021143187246948587, var=2.983515778129799, Tref=1000.0, N=164, data_mean=0.0, correlation='Root_1R->C',), comment="""BM rule fitted to 164 training reactions at node Root_1R->C
    Total Standard Deviation in ln(k): 3.515873752933057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 164 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.515873752933057""",
    longDesc = 
"""
BM rule fitted to 164 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.515873752933057
""",
)

entry(
    index = 29,
    label = "Root_N-1R->C",
    kinetics = ArrheniusBM(A=(8.92232e+06,'m^3/(mol*s)'), n=0.314966, w0=(81166.7,'J/mol'), E0=(18143.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.29870235201905426, var=13.811997184161026, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R->C',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R->C
    Total Standard Deviation in ln(k): 8.201005178576093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 8.201005178576093""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 8.201005178576093
""",
)

entry(
    index = 30,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.14472e+07,'m^3/(mol*s)'), n=0.219154, w0=(209857,'J/mol'), E0=(20985.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7535411346178692, var=21.377365707565875, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 11.1623450597277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.1623450597277""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.1623450597277
""",
)

entry(
    index = 31,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.22827e+07,'m^3/(mol*s)'), n=0.172987, w0=(197571,'J/mol'), E0=(19757.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02057943756101408, var=0.2515344135981482, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 1.0571460554417598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.0571460554417598""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.0571460554417598
""",
)

entry(
    index = 32,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(138976,'m^3/(mol*s)'), n=0.838621, w0=(180588,'J/mol'), E0=(18058.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10080687384336641, var=6.609465083140319, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R',), comment="""BM rule fitted to 17 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R
    Total Standard Deviation in ln(k): 5.407232946368493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 5.407232946368493""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 5.407232946368493
""",
)

entry(
    index = 33,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.01846e+07,'m^3/(mol*s)'), n=0.342681, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04178003370565318, var=0.2726914782705248, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing
    Total Standard Deviation in ln(k): 1.15184500261956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing
Total Standard Deviation in ln(k): 1.15184500261956""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing
Total Standard Deviation in ln(k): 1.15184500261956
""",
)

entry(
    index = 34,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(3.22095e+11,'m^3/(mol*s)'), n=-1.64353, w0=(192294,'J/mol'), E0=(19229.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24821370413186064, var=29.405909692307336, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing
    Total Standard Deviation in ln(k): 11.494772755507592"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.494772755507592""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.494772755507592
""",
)

entry(
    index = 35,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C",
    kinetics = ArrheniusBM(A=(5.77303e+17,'m^3/(mol*s)'), n=-4.12948, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1819231110890671, var=8.7602285810451, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C
    Total Standard Deviation in ln(k): 6.390644640718434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C
Total Standard Deviation in ln(k): 6.390644640718434""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C
Total Standard Deviation in ln(k): 6.390644640718434
""",
)

entry(
    index = 36,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.75,'m^3/(mol*s)'), n=-0.32, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.28943e+28,'m^3/(mol*s)'), n=-7.23229, w0=(198800,'J/mol'), E0=(19880,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1936785849351029, var=19.811789919247353, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 9.409793024260008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 9.409793024260008""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 9.409793024260008
""",
)

entry(
    index = 38,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_4R!H->C",
    kinetics = ArrheniusBM(A=(3.11e+34,'m^3/(mol*s)'), n=-9.59, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_N-3BrClFINOPSSi->F_3ClOS->Cl_2CHO->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_1R->C_2R-inRing",
    kinetics = ArrheniusBM(A=(1.56213e+09,'m^3/(mol*s)'), n=-0.646243, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01251184007725324, var=0.2596057720721391, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->C_2R-inRing',), comment="""BM rule fitted to 10 training reactions at node Root_1R->C_2R-inRing
    Total Standard Deviation in ln(k): 1.0528798430208304"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->C_2R-inRing
Total Standard Deviation in ln(k): 1.0528798430208304""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->C_2R-inRing
Total Standard Deviation in ln(k): 1.0528798430208304
""",
)

entry(
    index = 42,
    label = "Root_1R->C_N-2R-inRing",
    kinetics = ArrheniusBM(A=(3.4772e+06,'m^3/(mol*s)'), n=0.118875, w0=(156045,'J/mol'), E0=(15604.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.026986241844565877, var=3.1467462639678465, Tref=1000.0, N=154, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing',), comment="""BM rule fitted to 154 training reactions at node Root_1R->C_N-2R-inRing
    Total Standard Deviation in ln(k): 3.6240183386139178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 154 training reactions at node Root_1R->C_N-2R-inRing
Total Standard Deviation in ln(k): 3.6240183386139178""",
    longDesc = 
"""
BM rule fitted to 154 training reactions at node Root_1R->C_N-2R-inRing
Total Standard Deviation in ln(k): 3.6240183386139178
""",
)

entry(
    index = 43,
    label = "Root_N-1R->C_1BrClFHNOS->Cl",
    kinetics = ArrheniusBM(A=(3.24625e+12,'m^3/(mol*s)'), n=-2.82209, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_1BrClFHNOS->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_1BrClFHNOS->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_1BrClFHNOS->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_1BrClFHNOS->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl",
    kinetics = ArrheniusBM(A=(9.35262e+06,'m^3/(mol*s)'), n=0.331805, w0=(78882.4,'J/mol'), E0=(20890.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2163811441176766, var=12.125065590928722, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl
    Total Standard Deviation in ln(k): 7.524372235272984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl
Total Standard Deviation in ln(k): 7.524372235272984""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl
Total Standard Deviation in ln(k): 7.524372235272984
""",
)

entry(
    index = 45,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(355085,'m^3/(mol*s)'), n=0.0254762, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00019421097900009282, var=37.58191179649965, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 12.290333485123663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.290333485123663""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.290333485123663
""",
)

entry(
    index = 46,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(6.82479e+06,'m^3/(mol*s)'), n=0.310513, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6470645560454384, var=7.393757394843565, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R
    Total Standard Deviation in ln(k): 7.076958602708617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R
Total Standard Deviation in ln(k): 7.076958602708617""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R
Total Standard Deviation in ln(k): 7.076958602708617
""",
)

entry(
    index = 47,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(4.27e+07,'m^3/(mol*s)'), n=0.338, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.68758e+07,'m^3/(mol*s)'), n=0.176718, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.026919267571991545, var=0.07901660097312979, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.6311652092208463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.6311652092208463""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.6311652092208463
""",
)

entry(
    index = 49,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.22915e+07,'m^3/(mol*s)'), n=0.181361, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1489920501984019, var=0.10041008290210698, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.0096033162086009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009
""",
)

entry(
    index = 50,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.25109e+08,'m^3/(mol*s)'), n=-0.247784, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.46154e+07,'m^3/(mol*s)'), n=0.266307, w0=(178375,'J/mol'), E0=(17837.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03543925091156924, var=1.063407207626836, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing
    Total Standard Deviation in ln(k): 2.156358979027584"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 2.156358979027584""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 2.156358979027584
""",
)

entry(
    index = 52,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.35338e+07,'m^3/(mol*s)'), n=0.337482, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06473678945074876, var=0.16285884646625434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 0.971681599438312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.971681599438312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.971681599438312
""",
)

entry(
    index = 53,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(7.66431e+06,'m^3/(mol*s)'), n=0.347881, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17016890191634104, var=0.2974812683061607, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.520979521855843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.520979521855843""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.520979521855843
""",
)

entry(
    index = 54,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.53843e+11,'m^3/(mol*s)'), n=-1.7151, w0=(196429,'J/mol'), E0=(19642.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2881076304352014, var=30.817197257633087, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 14 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.852822305794904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.852822305794904""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.852822305794904
""",
)

entry(
    index = 55,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Sp-3R!H#2CCCHHHOOO",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Sp-3R!H#2CCCHHHOOO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Sp-3R!H#2CCCHHHOOO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Sp-3R!H#2CCCHHHOOO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Sp-3R!H#2CCCHHHOOO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO",
    kinetics = ArrheniusBM(A=(1.19651e+08,'m^3/(mol*s)'), n=-3.20624e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16819443494880856, var=0.07267224299466185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO
    Total Standard Deviation in ln(k): 0.9630313506418686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO
Total Standard Deviation in ln(k): 0.9630313506418686""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO
Total Standard Deviation in ln(k): 0.9630313506418686
""",
)

entry(
    index = 57,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO",
    kinetics = ArrheniusBM(A=(1.15997e+21,'m^3/(mol*s)'), n=-5.57879, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2558965756126182, var=5.974776905175695, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO
    Total Standard Deviation in ln(k): 5.543201694101767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO
Total Standard Deviation in ln(k): 5.543201694101767""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO
Total Standard Deviation in ln(k): 5.543201694101767
""",
)

entry(
    index = 58,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO",
    kinetics = ArrheniusBM(A=(1.92362e+15,'m^3/(mol*s)'), n=-3.04249, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12644301549327913, var=2.695628953502119, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO
    Total Standard Deviation in ln(k): 3.6091443777530277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO
Total Standard Deviation in ln(k): 3.6091443777530277""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO
Total Standard Deviation in ln(k): 3.6091443777530277
""",
)

entry(
    index = 59,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.05228e+30,'m^3/(mol*s)'), n=-7.57703, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17795683406446308, var=5.713237626643598, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 5.238921656345168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.238921656345168""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.238921656345168
""",
)

entry(
    index = 60,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(1.72215e+10,'m^3/(mol*s)'), n=-0.966317, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10086383407124434, var=0.31828891958274713, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R
    Total Standard Deviation in ln(k): 1.3844401162810993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 1.3844401162810993""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 1.3844401162810993
""",
)

entry(
    index = 61,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(5.69233e+08,'m^3/(mol*s)'), n=-0.511616, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11567367939225613, var=0.4319738291304277, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R
    Total Standard Deviation in ln(k): 1.608243821275936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 1.608243821275936""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 1.608243821275936
""",
)

entry(
    index = 62,
    label = "Root_1R->C_N-2R-inRing_2R->O",
    kinetics = ArrheniusBM(A=(106946,'m^3/(mol*s)'), n=0.349277, w0=(137522,'J/mol'), E0=(13752.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007772303370760851, var=2.7394176424219596, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O',), comment="""BM rule fitted to 23 training reactions at node Root_1R->C_N-2R-inRing_2R->O
    Total Standard Deviation in ln(k): 3.3376027528603553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_1R->C_N-2R-inRing_2R->O
Total Standard Deviation in ln(k): 3.3376027528603553""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_1R->C_N-2R-inRing_2R->O
Total Standard Deviation in ln(k): 3.3376027528603553
""",
)

entry(
    index = 63,
    label = "Root_1R->C_N-2R-inRing_N-2R->O",
    kinetics = ArrheniusBM(A=(5.51858e+06,'m^3/(mol*s)'), n=0.0883083, w0=(159298,'J/mol'), E0=(15929.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.024613356976261835, var=2.763512221210433, Tref=1000.0, N=131, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O',), comment="""BM rule fitted to 131 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O
    Total Standard Deviation in ln(k): 3.394477092239871"""),
    rank = 11,
    shortDesc = """BM rule fitted to 131 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O
Total Standard Deviation in ln(k): 3.394477092239871""",
    longDesc = 
"""
BM rule fitted to 131 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O
Total Standard Deviation in ln(k): 3.394477092239871
""",
)

entry(
    index = 64,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N",
    kinetics = ArrheniusBM(A=(148793,'m^3/(mol*s)'), n=0.730808, w0=(76000,'J/mol'), E0=(50729,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6349749523232976, var=3.2431098492756587, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N
    Total Standard Deviation in ln(k): 5.2056689614522265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N
Total Standard Deviation in ln(k): 5.2056689614522265""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N
Total Standard Deviation in ln(k): 5.2056689614522265
""",
)

entry(
    index = 65,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N",
    kinetics = ArrheniusBM(A=(2.25125e+07,'m^3/(mol*s)'), n=0.433994, w0=(83000,'J/mol'), E0=(33628.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.5724571032623498, var=26.840516268085764, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N
    Total Standard Deviation in ln(k): 16.84955819729413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N
Total Standard Deviation in ln(k): 16.84955819729413""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N
Total Standard Deviation in ln(k): 16.84955819729413
""",
)

entry(
    index = 66,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1785.64,'m^3/(mol*s)'), n=0.0220967, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.63315e+06,'m^3/(mol*s)'), n=0.0938491, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.77012e+06,'m^3/(mol*s)'), n=-0.0289636, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing",
    kinetics = ArrheniusBM(A=(4.4197e+06,'m^3/(mol*s)'), n=0.173431, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1097017345178382, var=0.8159359144189625, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing
    Total Standard Deviation in ln(k): 2.086493076125835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing
Total Standard Deviation in ln(k): 2.086493076125835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing
Total Standard Deviation in ln(k): 2.086493076125835
""",
)

entry(
    index = 70,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(9.42e+06,'m^3/(mol*s)'), n=0.408, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(3.02093e+07,'m^3/(mol*s)'), n=0.125846, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.47660747185827573, var=1.386468955460086, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R
    Total Standard Deviation in ln(k): 3.5580500164857103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 3.5580500164857103""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 3.5580500164857103
""",
)

entry(
    index = 72,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(2.59427e+07,'m^3/(mol*s)'), n=0.192092, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.035225327597470955, var=0.01056069269555372, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R
    Total Standard Deviation in ln(k): 0.2945229114894713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 0.2945229114894713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 0.2945229114894713
""",
)

entry(
    index = 73,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(3.62e+07,'m^3/(mol*s)'), n=0.228, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(2.2e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1200,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.45982e+07,'m^3/(mol*s)'), n=0.267307, w0=(178733,'J/mol'), E0=(17873.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03456242716001357, var=1.0585519943787185, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.1494311190613704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.1494311190613704""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.1494311190613704
""",
)

entry(
    index = 76,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(2.09978e+06,'m^3/(mol*s)'), n=0.6, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(7.09e+06,'m^3/(mol*s)'), n=0.412, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.156e+06,'m^3/(mol*s)'), n=0.461, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(7.22657e+07,'m^3/(mol*s)'), n=0.062, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.03368e+09,'m^3/(mol*s)'), n=-0.310401, w0=(199875,'J/mol'), E0=(19987.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13128642607969432, var=0.7094076822608714, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C
    Total Standard Deviation in ln(k): 2.0183804308142013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C
Total Standard Deviation in ln(k): 2.0183804308142013""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C
Total Standard Deviation in ln(k): 2.0183804308142013
""",
)

entry(
    index = 81,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.11133e+13,'m^3/(mol*s)'), n=-2.69109, w0=(191833,'J/mol'), E0=(19183.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7992797268425917, var=45.82563932189044, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C
    Total Standard Deviation in ln(k): 15.579221933648226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 15.579221933648226""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 15.579221933648226
""",
)

entry(
    index = 82,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_Sp-3R!H-2CHO",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_Sp-3R!H-2CHO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_Sp-3R!H-2CHO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_Sp-3R!H-2CHO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_Sp-3R!H-2CHO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_N-Sp-3R!H-2CHO",
    kinetics = ArrheniusBM(A=(1.21e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_N-Sp-3R!H-2CHO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_N-Sp-3R!H-2CHO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_N-Sp-3R!H-2CHO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_N-Sp-3R!H#2CCCHHHOOO_N-Sp-3R!H-2CHO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.48952e+22,'m^3/(mol*s)'), n=-5.97762, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.9225918374612365, var=2.1841047002555745, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R
    Total Standard Deviation in ln(k): 12.818499580810895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R
Total Standard Deviation in ln(k): 12.818499580810895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R
Total Standard Deviation in ln(k): 12.818499580810895
""",
)

entry(
    index = 85,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.31027e+14,'m^3/(mol*s)'), n=-2.70444, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11239379132878427, var=4.600921598482703, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R
    Total Standard Deviation in ln(k): 4.582504881399268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R
Total Standard Deviation in ln(k): 4.582504881399268""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R
Total Standard Deviation in ln(k): 4.582504881399268
""",
)

entry(
    index = 86,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.38538e+32,'m^3/(mol*s)'), n=-8.31613, w0=(187333,'J/mol'), E0=(18733.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13714718458336772, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.34459091603861236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.34459091603861236""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.34459091603861236
""",
)

entry(
    index = 87,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_1C-inRing",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(1.79861e+10,'m^3/(mol*s)'), n=-0.973503, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0958344498312535, var=0.3102582992770782, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing
    Total Standard Deviation in ln(k): 1.3574442477537638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing
Total Standard Deviation in ln(k): 1.3574442477537638""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing
Total Standard Deviation in ln(k): 1.3574442477537638
""",
)

entry(
    index = 89,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.15204e+08,'m^3/(mol*s)'), n=-0.555925, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.35880633950739715, var=0.8335128198586998, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.7317849114763417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R
Total Standard Deviation in ln(k): 2.7317849114763417""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R
Total Standard Deviation in ln(k): 2.7317849114763417
""",
)

entry(
    index = 90,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R",
    kinetics = ArrheniusBM(A=(105383,'m^3/(mol*s)'), n=0.350074, w0=(143857,'J/mol'), E0=(14385.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010280682494321928, var=2.7056016226475306, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R',), comment="""BM rule fitted to 21 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R
    Total Standard Deviation in ln(k): 3.323362071170779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R
Total Standard Deviation in ln(k): 3.323362071170779""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R
Total Standard Deviation in ln(k): 3.323362071170779
""",
)

entry(
    index = 91,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.7e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S",
    kinetics = ArrheniusBM(A=(69181.1,'m^3/(mol*s)'), n=0.764865, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03639418016190122, var=1.0362331955515207, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S
    Total Standard Deviation in ln(k): 2.1321735605013337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S
Total Standard Deviation in ln(k): 2.1321735605013337""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S
Total Standard Deviation in ln(k): 2.1321735605013337
""",
)

entry(
    index = 93,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S",
    kinetics = ArrheniusBM(A=(3.15788e+09,'m^3/(mol*s)'), n=-0.892664, w0=(158754,'J/mol'), E0=(15875.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.059856046264589846, var=5.178632134985917, Tref=1000.0, N=126, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S',), comment="""BM rule fitted to 126 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S
    Total Standard Deviation in ln(k): 4.712489131744962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 126 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S
Total Standard Deviation in ln(k): 4.712489131744962""",
    longDesc = 
"""
BM rule fitted to 126 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S
Total Standard Deviation in ln(k): 4.712489131744962
""",
)

entry(
    index = 94,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.04219e+09,'m^3/(mol*s)'), n=-0.666693, w0=(76357.1,'J/mol'), E0=(55458,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06458738003907305, var=2.7819848882805664, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R
    Total Standard Deviation in ln(k): 3.5060342636083592"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R
Total Standard Deviation in ln(k): 3.5060342636083592""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R
Total Standard Deviation in ln(k): 3.5060342636083592
""",
)

entry(
    index = 95,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4709502203626317, var=0.4813240235668652, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-1N-R
    Total Standard Deviation in ln(k): 2.5741274836274104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.5741274836274104""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.5741274836274104
""",
)

entry(
    index = 96,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O",
    kinetics = ArrheniusBM(A=(0.820101,'m^3/(mol*s)'), n=2.41505, w0=(71000,'J/mol'), E0=(680.865,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5607570996826429, var=1.6937104050430816, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O
    Total Standard Deviation in ln(k): 4.017952383487661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O
Total Standard Deviation in ln(k): 4.017952383487661""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O
Total Standard Deviation in ln(k): 4.017952383487661
""",
)

entry(
    index = 97,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O",
    kinetics = ArrheniusBM(A=(7.24539e+06,'m^3/(mol*s)'), n=0.606766, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.3859426480679575, var=33.61904000393023, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O
    Total Standard Deviation in ln(k): 20.13123412435933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O
Total Standard Deviation in ln(k): 20.13123412435933""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O
Total Standard Deviation in ln(k): 20.13123412435933
""",
)

entry(
    index = 98,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(249317,'m^3/(mol*s)'), n=0.611, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2R_4R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(6.44369e+06,'m^3/(mol*s)'), n=0.245, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Sp-3R!H-2R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.25e+07,'m^3/(mol*s)'), n=0.284, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_Ext-2R-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_N-Sp-3R!H-2R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.89049e+07,'m^3/(mol*s)'), n=0.213701, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.9467611356354685e-05, var=0.012109149066047924, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.22075362911252447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22075362911252447""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22075362911252447
""",
)

entry(
    index = 102,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.03598e+07,'m^3/(mol*s)'), n=0.00764768, w0=(187333,'J/mol'), E0=(18733.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2970367021065268, var=4.47209214178044, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 7.4983639423993145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.4983639423993145""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.4983639423993145
""",
)

entry(
    index = 103,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO",
    kinetics = ArrheniusBM(A=(1.62598e+07,'m^3/(mol*s)'), n=0.255122, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06239915174409146, var=9.629649721936181e-35, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO
    Total Standard Deviation in ln(k): 0.15678178830173736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO
Total Standard Deviation in ln(k): 0.15678178830173736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO
Total Standard Deviation in ln(k): 0.15678178830173736
""",
)

entry(
    index = 104,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-Sp-4R!H-2CHO",
    kinetics = ArrheniusBM(A=(6.117e+08,'m^3/(mol*s)'), n=-0.152, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-Sp-4R!H-2CHO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-Sp-4R!H-2CHO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-Sp-4R!H-2CHO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-Sp-4R!H-2CHO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO",
    kinetics = ArrheniusBM(A=(2.19868e+09,'m^3/(mol*s)'), n=-0.387221, w0=(190200,'J/mol'), E0=(19020,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1014956519348729, var=0.14226689263790918, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO
    Total Standard Deviation in ln(k): 1.011165865060086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO
Total Standard Deviation in ln(k): 1.011165865060086""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO
Total Standard Deviation in ln(k): 1.011165865060086
""",
)

entry(
    index = 106,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO",
    kinetics = ArrheniusBM(A=(4.75376e+07,'m^3/(mol*s)'), n=0.0030318, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4346821220492238, var=1.1566369500321274, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO
    Total Standard Deviation in ln(k): 3.248199715071691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO
Total Standard Deviation in ln(k): 3.248199715071691""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO
Total Standard Deviation in ln(k): 3.248199715071691
""",
)

entry(
    index = 107,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C",
    kinetics = ArrheniusBM(A=(2.55169e+17,'m^3/(mol*s)'), n=-4.36108, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21903407700277286, var=33.35106213511694, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C
    Total Standard Deviation in ln(k): 12.127757822195838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C
Total Standard Deviation in ln(k): 12.127757822195838""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C
Total Standard Deviation in ln(k): 12.127757822195838
""",
)

entry(
    index = 108,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_N-2CHO->C",
    kinetics = ArrheniusBM(A=(700000,'m^3/(mol*s)'), n=0.493, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_N-2CHO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_N-2CHO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_N-2CHO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_N-2CHO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.2e+38,'m^3/(mol*s)'), n=-10.6, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_Sp-4C-2CHO_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.536223587017913, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 6.372421072909329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.372421072909329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.372421072909329
""",
)

entry(
    index = 112,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(4.38538e+32,'m^3/(mol*s)'), n=-8.31613, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.0631977592804454, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 5.1839139680413195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 5.1839139680413195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 5.1839139680413195
""",
)

entry(
    index = 114,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.668e+09,'m^3/(mol*s)'), n=-0.7, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_Sp-3R!H-2R_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_1C-inRing",
    kinetics = ArrheniusBM(A=(2.52966e+09,'m^3/(mol*s)'), n=-0.720394, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0329788338602979, var=2.2202828217281576, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_1C-inRing
    Total Standard Deviation in ln(k): 5.582602458105895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_1C-inRing
Total Standard Deviation in ln(k): 5.582602458105895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_1C-inRing
Total Standard Deviation in ln(k): 5.582602458105895
""",
)

entry(
    index = 116,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.28714e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 117,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C",
    kinetics = ArrheniusBM(A=(8.70479e+06,'m^3/(mol*s)'), n=-4.60593e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.773342796476042e-08, var=0.275252594970827, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C
    Total Standard Deviation in ln(k): 1.0517747477968553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C
Total Standard Deviation in ln(k): 1.0517747477968553""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C
Total Standard Deviation in ln(k): 1.0517747477968553
""",
)

entry(
    index = 118,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(103797,'m^3/(mol*s)'), n=0.351276, w0=(156000,'J/mol'), E0=(15600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012266338764700117, var=2.7071207539392153, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C',), comment="""BM rule fitted to 18 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C
    Total Standard Deviation in ln(k): 3.3292767702426507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C
Total Standard Deviation in ln(k): 3.3292767702426507""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C
Total Standard Deviation in ln(k): 3.3292767702426507
""",
)

entry(
    index = 119,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04415470256864107, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C
    Total Standard Deviation in ln(k): 0.11094146374030418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C
Total Standard Deviation in ln(k): 0.11094146374030418""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C
Total Standard Deviation in ln(k): 0.11094146374030418
""",
)

entry(
    index = 120,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(129687,'m^3/(mol*s)'), n=0.801692, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3723820346018363, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C
    Total Standard Deviation in ln(k): 0.9356332527684328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328
""",
)

entry(
    index = 121,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C",
    kinetics = ArrheniusBM(A=(1.56962e+09,'m^3/(mol*s)'), n=-0.81965, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07045519951363563, var=4.661918072339151, Tref=1000.0, N=90, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C',), comment="""BM rule fitted to 90 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C
    Total Standard Deviation in ln(k): 4.505541912459456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 90 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C
Total Standard Deviation in ln(k): 4.505541912459456""",
    longDesc = 
"""
BM rule fitted to 90 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C
Total Standard Deviation in ln(k): 4.505541912459456
""",
)

entry(
    index = 122,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C",
    kinetics = ArrheniusBM(A=(8.90727e+09,'m^3/(mol*s)'), n=-1.00097, w0=(123139,'J/mol'), E0=(12313.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.051211262526404726, var=6.405624352584167, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C',), comment="""BM rule fitted to 36 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C
    Total Standard Deviation in ln(k): 5.202522668466121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C
Total Standard Deviation in ln(k): 5.202522668466121""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C
Total Standard Deviation in ln(k): 5.202522668466121
""",
)

entry(
    index = 123,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0",
    kinetics = ArrheniusBM(A=(2.37719e+10,'m^3/(mol*s)'), n=-0.974918, w0=(78500,'J/mol'), E0=(7850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0353464477837112, var=0.6881106657456486, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0
    Total Standard Deviation in ln(k): 1.7517867546664327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 1.7517867546664327""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 1.7517867546664327
""",
)

entry(
    index = 124,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0",
    kinetics = ArrheniusBM(A=(3.61842e+15,'m^3/(mol*s)'), n=-3.69129, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0093018310425466, var=139.72823596203577, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0
    Total Standard Deviation in ln(k): 28.745808571502433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 28.745808571502433""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 28.745808571502433
""",
)

entry(
    index = 125,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.10008e+08,'m^3/(mol*s)'), n=-0.339512, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5198152603821848, var=1.474141239534708, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R
    Total Standard Deviation in ln(k): 3.740101915796612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R
Total Standard Deviation in ln(k): 3.740101915796612""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R
Total Standard Deviation in ln(k): 3.740101915796612
""",
)

entry(
    index = 126,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(2.49151e+08,'m^3/(mol*s)'), n=0.0472428, w0=(71000,'J/mol'), E0=(27446.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O_Ext-1S-R",
    kinetics = ArrheniusBM(A=(106000,'m^3/(mol*s)'), n=1.21, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O_Ext-1S-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O_Ext-1S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_N-1OS->O_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.85833e+07,'m^3/(mol*s)'), n=0.213459, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.198896793630605e-05, var=0.012049465033958805, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.2202910083072202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.2202910083072202""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.2202910083072202
""",
)

entry(
    index = 129,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2CHO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2CHO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO_Ext-2CHO-R",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO_Ext-2CHO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO_Ext-2CHO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Sp-4R!H-2CHO_Ext-2CHO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_Sp-4C=3R!H",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_Sp-4C=3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_Sp-4C=3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_Sp-4C=3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_Sp-4C=3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H",
    kinetics = ArrheniusBM(A=(4.22706e+09,'m^3/(mol*s)'), n=-0.472787, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07277150462476355, var=0.04802746660583578, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H
    Total Standard Deviation in ln(k): 0.6221840720985681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H
Total Standard Deviation in ln(k): 0.6221840720985681""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H
Total Standard Deviation in ln(k): 0.6221840720985681
""",
)

entry(
    index = 134,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_N-Sp-3R!H-2CHO_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C",
    kinetics = ArrheniusBM(A=(9.57308e+16,'m^3/(mol*s)'), n=-4.56402, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25266302397300067, var=49.267441738513114, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C
    Total Standard Deviation in ln(k): 14.70622156373453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C
Total Standard Deviation in ln(k): 14.70622156373453""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C
Total Standard Deviation in ln(k): 14.70622156373453
""",
)

entry(
    index = 136,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.536223587017913, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C
    Total Standard Deviation in ln(k): 6.372421072909329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C
Total Standard Deviation in ln(k): 6.372421072909329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C
Total Standard Deviation in ln(k): 6.372421072909329
""",
)

entry(
    index = 137,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_4R!H->C_N-Sp-4C-2CHO_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_6BrF->Br",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_6BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_6BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_6BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_6BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_N-6BrF->Br",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_N-6BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_N-6BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_N-6BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H->C_3BrClFINOPSSi->F_Ext-2CHO-R_Ext-2CHO-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-6R!H->Cl_N-6BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_2R-inRing_Ext-2R-R_N-Sp-3R!H-2R_Ext-1C-R_N-1C-inRing_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.38319e+06,'m^3/(mol*s)'), n=-3.04169e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.3279077205677291, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.1479760049827752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.1479760049827752""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.1479760049827752
""",
)

entry(
    index = 143,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing",
    kinetics = ArrheniusBM(A=(3.5471e+06,'m^3/(mol*s)'), n=-0.0529334, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025947195813883325, var=0.4395334977433274, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing
    Total Standard Deviation in ln(k): 1.394279639884687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing
Total Standard Deviation in ln(k): 1.394279639884687""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing
Total Standard Deviation in ln(k): 1.394279639884687
""",
)

entry(
    index = 144,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(38.169,'m^3/(mol*s)'), n=1.25645, w0=(151143,'J/mol'), E0=(15114.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14892996976808734, var=1.29109987991916, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing
    Total Standard Deviation in ln(k): 2.6521077325216624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 2.6521077325216624""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 2.6521077325216624
""",
)

entry(
    index = 145,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6642490346951677, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6689674238572052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.6689674238572052""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.6689674238572052
""",
)

entry(
    index = 146,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3940,'m^3/(mol*s)'), n=1.25, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.64952e+09,'m^3/(mol*s)'), n=-0.840864, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07242866886808222, var=4.839535679501582, Tref=1000.0, N=88, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R',), comment="""BM rule fitted to 88 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.592187190811246"""),
    rank = 11,
    shortDesc = """BM rule fitted to 88 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.592187190811246""",
    longDesc = 
"""
BM rule fitted to 88 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.592187190811246
""",
)

entry(
    index = 148,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N",
    kinetics = ArrheniusBM(A=(1.04914e+09,'m^3/(mol*s)'), n=-0.577655, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07146127553612974, var=24.369228876979903, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N
    Total Standard Deviation in ln(k): 10.075965578588645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N
Total Standard Deviation in ln(k): 10.075965578588645""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N
Total Standard Deviation in ln(k): 10.075965578588645
""",
)

entry(
    index = 149,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N",
    kinetics = ArrheniusBM(A=(1.33883e+10,'m^3/(mol*s)'), n=-1.08162, w0=(125471,'J/mol'), E0=(12547.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05151526211114507, var=6.676526334508655, Tref=1000.0, N=34, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N',), comment="""BM rule fitted to 34 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N
    Total Standard Deviation in ln(k): 5.309465303648348"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N
Total Standard Deviation in ln(k): 5.309465303648348""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N
Total Standard Deviation in ln(k): 5.309465303648348
""",
)

entry(
    index = 150,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C",
    kinetics = ArrheniusBM(A=(2.72112e+10,'m^3/(mol*s)'), n=-0.98654, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25200377643955907, var=0.0006122197784863265, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C
    Total Standard Deviation in ln(k): 0.6827786287928705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C
Total Standard Deviation in ln(k): 0.6827786287928705""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C
Total Standard Deviation in ln(k): 0.6827786287928705
""",
)

entry(
    index = 151,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C",
    kinetics = ArrheniusBM(A=(9.29149e+06,'m^3/(mol*s)'), n=-0.3, w0=(75166.7,'J/mol'), E0=(7516.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.403097204578484e-11, var=16.77957818736314, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C
    Total Standard Deviation in ln(k): 8.211972928043448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C
Total Standard Deviation in ln(k): 8.211972928043448""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C
Total Standard Deviation in ln(k): 8.211972928043448
""",
)

entry(
    index = 152,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R",
    kinetics = ArrheniusBM(A=(58500,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(473,'K'), Tmax=(703,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_3R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(5.15e+07,'m^3/(mol*s)'), n=-0.24, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_N-3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_N-3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_N-3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_N-1BrFNOS->N_1OS->O_Ext-2R-R_N-3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.83921e+07,'m^3/(mol*s)'), n=0.213314, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00011150177525074285, var=0.013222711839658728, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.23080474409830198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.23080474409830198""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.23080474409830198
""",
)

entry(
    index = 157,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H",
    kinetics = ArrheniusBM(A=(3.15956e+07,'m^3/(mol*s)'), n=0.215726, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0022644853455516876, var=7.490440640908408e-07, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H
    Total Standard Deviation in ln(k): 0.007424706391292111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H
Total Standard Deviation in ln(k): 0.007424706391292111""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H
Total Standard Deviation in ln(k): 0.007424706391292111
""",
)

entry(
    index = 159,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H",
    kinetics = ArrheniusBM(A=(2.5021e+10,'m^3/(mol*s)'), n=-0.72284, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2406798463897532, var=0.000995063531188551, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H
    Total Standard Deviation in ln(k): 0.6679618536124499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H
Total Standard Deviation in ln(k): 0.6679618536124499""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H
Total Standard Deviation in ln(k): 0.6679618536124499
""",
)

entry(
    index = 160,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.90326e+19,'m^3/(mol*s)'), n=-5.05673, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.653369690823422, var=91.55450293110613, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 28.361451450432188"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R
Total Standard Deviation in ln(k): 28.361451450432188""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R
Total Standard Deviation in ln(k): 28.361451450432188
""",
)

entry(
    index = 161,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_N-Sp-3R!H-2C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.04e+06,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_3R!H->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(27200,'m^3/(mol*s)'), n=0.504, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(252000,'m^3/(mol*s)'), n=0.34, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(36.6949,'m^3/(mol*s)'), n=1.25965, w0=(147500,'J/mol'), E0=(14750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19005733480466572, var=1.2794295923382644, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 2.7451243964314984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 2.7451243964314984""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 2.7451243964314984
""",
)

entry(
    index = 166,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(89.4,'m^3/(mol*s)'), n=1.54, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_2BrCClFNS->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.44625e+09,'m^3/(mol*s)'), n=-0.983007, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09283946909436741, var=7.700827489792934, Tref=1000.0, N=49, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 49 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.796477979064827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 49 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.796477979064827""",
    longDesc = 
"""
BM rule fitted to 49 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.796477979064827
""",
)

entry(
    index = 168,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(3.892e+12,'m^3/(mol*s)'), n=-1.99427, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07504069681485791, var=20.417937381682936, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F
    Total Standard Deviation in ln(k): 9.247182848319863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F
Total Standard Deviation in ln(k): 9.247182848319863""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F
Total Standard Deviation in ln(k): 9.247182848319863
""",
)

entry(
    index = 169,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(3.27076e+08,'m^3/(mol*s)'), n=-0.499175, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03288614709724039, var=0.6917937803738233, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F',), comment="""BM rule fitted to 36 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 1.7500496989982381"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F
Total Standard Deviation in ln(k): 1.7500496989982381""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F
Total Standard Deviation in ln(k): 1.7500496989982381
""",
)

entry(
    index = 170,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N_Ext-2N-R_Ext-2N-R",
    kinetics = ArrheniusBM(A=(1.75326e+12,'m^3/(mol*s)'), n=-1.41237, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N_Ext-2N-R_Ext-2N-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N_Ext-2N-R_Ext-2N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N_Ext-2N-R_Ext-2N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_2BrClFN->N_Ext-2N-R_Ext-2N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.81583e+09,'m^3/(mol*s)'), n=-1.03438, w0=(126594,'J/mol'), E0=(12659.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04469155419264046, var=6.9279620405381, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R',), comment="""BM rule fitted to 32 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R
    Total Standard Deviation in ln(k): 5.388957963565762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R
Total Standard Deviation in ln(k): 5.388957963565762""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R
Total Standard Deviation in ln(k): 5.388957963565762
""",
)

entry(
    index = 172,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_2BrClF->Cl",
    kinetics = ArrheniusBM(A=(7.28777e+28,'m^3/(mol*s)'), n=-6.81702, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_2BrClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_2BrClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_2BrClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_2BrClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_N-2BrClF->Cl",
    kinetics = ArrheniusBM(A=(17646.5,'m^3/(mol*s)'), n=0.382496, w0=(95000,'J/mol'), E0=(9500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_N-2BrClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_N-2BrClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_N-2BrClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_N-2BrClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.30329e+10,'m^3/(mol*s)'), n=-0.937308, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(5.66445e+06,'m^3/(mol*s)'), n=-0.45, w0=(77250,'J/mol'), E0=(7725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.401841872999714, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R
    Total Standard Deviation in ln(k): 3.697549959467405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.697549959467405""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.697549959467405
""",
)

entry(
    index = 176,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(2.80134e+07,'m^3/(mol*s)'), n=0.213024, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00015052741899771715, var=0.015297628183288132, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 0.2483310227156471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.2483310227156471""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.2483310227156471
""",
)

entry(
    index = 177,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(3.203e+07,'m^3/(mol*s)'), n=0.214, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_Sp-4C-3R!H_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.25e+08,'m^3/(mol*s)'), n=-0.119, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_4R!H->C_Sp-3R!H-2CHO_N-Sp-4C=3R!H_N-Sp-4C-3R!H_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.27e+36,'m^3/(mol*s)'), n=-9.86, w0=(216000,'J/mol'), E0=(21600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_N-4R!H->C_2CHO->C_Sp-3R!H-2C_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(27.0871,'m^3/(mol*s)'), n=1.29418, w0=(111800,'J/mol'), E0=(11180,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3703998468992621, var=1.2877737998775645, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.205628685278682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.205628685278682""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.205628685278682
""",
)

entry(
    index = 182,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(2.89097e+06,'m^3/(mol*s)'), n=-0.0365829, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00892931059814646, var=1.27254122680126, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 2.2839163322115086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.2839163322115086""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.2839163322115086
""",
)

entry(
    index = 183,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(3.24036e+06,'m^3/(mol*s)'), n=3.5707e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.458191251135313e-17, var=0.04752486418241179, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 0.43703622037861506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 0.43703622037861506""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 0.43703622037861506
""",
)

entry(
    index = 184,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C",
    kinetics = ArrheniusBM(A=(5.28068e+09,'m^3/(mol*s)'), n=-0.525317, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008449525406348222, var=5.71732706506989, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C',), comment="""BM rule fitted to 26 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C
    Total Standard Deviation in ln(k): 4.81473853146839"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C
Total Standard Deviation in ln(k): 4.81473853146839""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C
Total Standard Deviation in ln(k): 4.81473853146839
""",
)

entry(
    index = 185,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(2.13615e+09,'m^3/(mol*s)'), n=-1.06363, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12553226434624076, var=5.151702243363729, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C',), comment="""BM rule fitted to 23 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C
    Total Standard Deviation in ln(k): 4.865627398991172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C
Total Standard Deviation in ln(k): 4.865627398991172""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C
Total Standard Deviation in ln(k): 4.865627398991172
""",
)

entry(
    index = 186,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.91046e+10,'m^3/(mol*s)'), n=-1.20133, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.57618571570149, var=16.448981993952476, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 9.578375935854332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 9.578375935854332""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 9.578375935854332
""",
)

entry(
    index = 187,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R",
    kinetics = ArrheniusBM(A=(3.82136e+07,'m^3/(mol*s)'), n=-0.209021, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01575591061162168, var=0.3213359212262395, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R',), comment="""BM rule fitted to 22 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R
    Total Standard Deviation in ln(k): 1.1760018523759395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 1.1760018523759395""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 1.1760018523759395
""",
)

entry(
    index = 188,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C",
    kinetics = ArrheniusBM(A=(6.27915e+08,'m^3/(mol*s)'), n=-0.515732, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15195860487817078, var=2.484869675912471, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C
    Total Standard Deviation in ln(k): 3.541963545078736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C
Total Standard Deviation in ln(k): 3.541963545078736""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C
Total Standard Deviation in ln(k): 3.541963545078736
""",
)

entry(
    index = 189,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C",
    kinetics = ArrheniusBM(A=(6.35251e+11,'m^3/(mol*s)'), n=-1.70975, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21005796391624093, var=0.6343518640644189, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C
    Total Standard Deviation in ln(k): 2.1244793226722543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C
Total Standard Deviation in ln(k): 2.1244793226722543""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C
Total Standard Deviation in ln(k): 2.1244793226722543
""",
)

entry(
    index = 190,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O",
    kinetics = ArrheniusBM(A=(23585.8,'m^3/(mol*s)'), n=0.399185, w0=(105833,'J/mol'), E0=(10583.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0885364287939095, var=15.313810395895914, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O
    Total Standard Deviation in ln(k): 8.06755583919254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O
Total Standard Deviation in ln(k): 8.06755583919254""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O
Total Standard Deviation in ln(k): 8.06755583919254
""",
)

entry(
    index = 191,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(4.60063e+10,'m^3/(mol*s)'), n=-1.20553, w0=(128741,'J/mol'), E0=(12874.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03955362302680148, var=5.923648473277099, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O',), comment="""BM rule fitted to 29 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O
    Total Standard Deviation in ln(k): 4.9786147590818235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O
Total Standard Deviation in ln(k): 4.9786147590818235""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O
Total Standard Deviation in ln(k): 4.9786147590818235
""",
)

entry(
    index = 192,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_2R->N",
    kinetics = ArrheniusBM(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(600,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_2R->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_2R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_2R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_2R->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_N-2R->N",
    kinetics = ArrheniusBM(A=(122000,'m^3/(mol*s)'), n=0.2, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_N-2R->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_N-2R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_N-2R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_N-1BrClFHNOS->Cl_1BrFNOS->N_Ext-2R-R_3R!H-u0_N-3R!H->C_Ext-1N-R_N-2R->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(2.69074e+07,'m^3/(mol*s)'), n=0.212153, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004025751725425149, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.010114954083982785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.010114954083982785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.010114954083982785
""",
)

entry(
    index = 195,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(9.48448e+06,'m^3/(mol*s)'), n=-0.273702, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3243923006376589, var=1.5708090532204264, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.3276290240615967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.3276290240615967""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.3276290240615967
""",
)

entry(
    index = 197,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(24.5417,'m^3/(mol*s)'), n=1.3063, w0=(105000,'J/mol'), E0=(10500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4220851556899367, var=1.3511068571537062, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.390761827754295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.390761827754295""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.390761827754295
""",
)

entry(
    index = 198,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.41997e+06,'m^3/(mol*s)'), n=2.03379e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0701791321551761e-07, var=1.3573949411693382, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.3356628470831757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.3356628470831757""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.3356628470831757
""",
)

entry(
    index = 199,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.15275e+10,'m^3/(mol*s)'), n=-0.490495, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0917981818802879, var=3.744993632773614, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.110209219205112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.110209219205112""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.110209219205112
""",
)

entry(
    index = 202,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C",
    kinetics = ArrheniusBM(A=(7.31593e+10,'m^3/(mol*s)'), n=-0.925823, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.48548279838691155, var=10.148419570630312, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C',), comment="""BM rule fitted to 18 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C
    Total Standard Deviation in ln(k): 7.606207205806868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C
Total Standard Deviation in ln(k): 7.606207205806868""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C
Total Standard Deviation in ln(k): 7.606207205806868
""",
)

entry(
    index = 203,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.01295e+07,'m^3/(mol*s)'), n=-0.0141403, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6542557587659921, var=1.392337693223965, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C
    Total Standard Deviation in ln(k): 4.009393153735599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 4.009393153735599""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 4.009393153735599
""",
)

entry(
    index = 204,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.33481e+07,'m^3/(mol*s)'), n=-0.279753, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08973137136354488, var=4.661232864462107, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 16 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.5536563909017085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.5536563909017085""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.5536563909017085
""",
)

entry(
    index = 205,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.02397e+13,'m^3/(mol*s)'), n=-2.65005, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3042325955693828, var=13.669355543356852, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 8.176328389991447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 8.176328389991447""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 8.176328389991447
""",
)

entry(
    index = 206,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_3BrClFO->F",
    kinetics = ArrheniusBM(A=(2.29531e+22,'m^3/(mol*s)'), n=-5.77419, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.7736779381566006, var=31.839887445087363, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_3BrClFO->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_3BrClFO->F
    Total Standard Deviation in ln(k): 18.281127429750715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_3BrClFO->F
Total Standard Deviation in ln(k): 18.281127429750715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_3BrClFO->F
Total Standard Deviation in ln(k): 18.281127429750715
""",
)

entry(
    index = 207,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_N-3BrClFO->F",
    kinetics = ArrheniusBM(A=(2.28e+35,'m^3/(mol*s)'), n=-8.68, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_N-3BrClFO->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_N-3BrClFO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_N-3BrClFO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_N-3BrClFO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C",
    kinetics = ArrheniusBM(A=(2.14111e+08,'m^3/(mol*s)'), n=-0.500739, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27982582269423517, var=1.1605859883687857, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C
    Total Standard Deviation in ln(k): 2.862791009607146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C
Total Standard Deviation in ln(k): 2.862791009607146""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C
Total Standard Deviation in ln(k): 2.862791009607146
""",
)

entry(
    index = 209,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C",
    kinetics = ArrheniusBM(A=(1.24576e+07,'m^3/(mol*s)'), n=-0.0192847, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0009672290820125796, var=0.20271400431754613, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C',), comment="""BM rule fitted to 16 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C
    Total Standard Deviation in ln(k): 0.9050375738438716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C
Total Standard Deviation in ln(k): 0.9050375738438716""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C
Total Standard Deviation in ln(k): 0.9050375738438716
""",
)

entry(
    index = 210,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(9.3042e+08,'m^3/(mol*s)'), n=-0.614675, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005609701825202483, var=3.0106861616704235, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C
    Total Standard Deviation in ln(k): 3.492576505803169"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C
Total Standard Deviation in ln(k): 3.492576505803169""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C
Total Standard Deviation in ln(k): 3.492576505803169
""",
)

entry(
    index = 211,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(8.08607e+07,'m^3/(mol*s)'), n=-5.09395e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04062402930232317, var=0.29799143580925214, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 1.1964270740744711"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.1964270740744711""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.1964270740744711
""",
)

entry(
    index = 212,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O",
    kinetics = ArrheniusBM(A=(1.52619e+07,'m^3/(mol*s)'), n=-6.53409e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15989752451550138, var=0.06567934312931165, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O
    Total Standard Deviation in ln(k): 0.9155257071693345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O
Total Standard Deviation in ln(k): 0.9155257071693345""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O
Total Standard Deviation in ln(k): 0.9155257071693345
""",
)

entry(
    index = 213,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O",
    kinetics = ArrheniusBM(A=(1.0848e+13,'m^3/(mol*s)'), n=-2.16589, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.390088079941935, var=0.04442972260791839, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O
    Total Standard Deviation in ln(k): 1.402686064265084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O
Total Standard Deviation in ln(k): 1.402686064265084""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O
Total Standard Deviation in ln(k): 1.402686064265084
""",
)

entry(
    index = 214,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.34416e+06,'m^3/(mol*s)'), n=-0.0421358, w0=(98750,'J/mol'), E0=(9875,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4107019976578008, var=0.8617921759955831, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 2.8929655165217394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.8929655165217394""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.8929655165217394
""",
)

entry(
    index = 215,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C",
    kinetics = ArrheniusBM(A=(4.17752e+09,'m^3/(mol*s)'), n=-0.905494, w0=(125900,'J/mol'), E0=(12590,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.049143648023889104, var=5.887483489606049, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C',), comment="""BM rule fitted to 25 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C
    Total Standard Deviation in ln(k): 4.9877931782592855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 4.9877931782592855""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 4.9877931782592855
""",
)

entry(
    index = 216,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C",
    kinetics = ArrheniusBM(A=(1.80268e+18,'m^3/(mol*s)'), n=-3.39214, w0=(146500,'J/mol'), E0=(14650,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.022971424195940456, var=0.18168948418918468, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C
    Total Standard Deviation in ln(k): 0.9122364646019766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 0.9122364646019766""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C
Total Standard Deviation in ln(k): 0.9122364646019766
""",
)

entry(
    index = 217,
    label = "Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R-inRing_N-2R->S_N-2CHNO->N_Ext-2CHO-R_Ext-2CHO-R_N-3R!H-inRing_Ext-3R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.18e+06,'m^3/(mol*s)'), n=-0.085, w0=(71000,'J/mol'), E0=(7100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(297.12,'m^3/(mol*s)'), n=0.971996, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6005523355889325, var=0.015436303854962363, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 1.757999611670846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.757999611670846""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.757999611670846
""",
)

entry(
    index = 220,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(0.004135,'m^3/(mol*s)'), n=2.525, w0=(71000,'J/mol'), E0=(7100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.15543e+06,'m^3/(mol*s)'), n=5.67594e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.7836333533627092, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 1.7746529918743192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192
""",
)

entry(
    index = 222,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.505e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(200,'K'), Tmax=(300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.02e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.223e+10,'m^3/(mol*s)'), n=-0.506, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.24268e+11,'m^3/(mol*s)'), n=-0.967059, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5147041442936513, var=10.247479220213412, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R',), comment="""BM rule fitted to 14 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.710721103089886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.710721103089886""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.710721103089886
""",
)

entry(
    index = 226,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.90628e+07,'m^3/(mol*s)'), n=-0.319465, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14995901122765223, var=2.2305291506772655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.3708444816661607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.3708444816661607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.3708444816661607
""",
)

entry(
    index = 227,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.00763e+07,'m^3/(mol*s)'), n=-0.0145517, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9381482123292634, var=2.36232293585952, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 5.438404085074936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.438404085074936""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.438404085074936
""",
)

entry(
    index = 228,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl",
    kinetics = ArrheniusBM(A=(9.81086e+08,'m^3/(mol*s)'), n=-0.80827, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09154334473665084, var=0.9297974480597565, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl
    Total Standard Deviation in ln(k): 2.163094354018921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl
Total Standard Deviation in ln(k): 2.163094354018921""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl
Total Standard Deviation in ln(k): 2.163094354018921
""",
)

entry(
    index = 229,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl",
    kinetics = ArrheniusBM(A=(100506,'m^3/(mol*s)'), n=0.321528, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08637249987628275, var=10.09381035109277, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl
    Total Standard Deviation in ln(k): 6.586211540329883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl
Total Standard Deviation in ln(k): 6.586211540329883""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl
Total Standard Deviation in ln(k): 6.586211540329883
""",
)

entry(
    index = 230,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F",
    kinetics = ArrheniusBM(A=(1.28274e+15,'m^3/(mol*s)'), n=-2.81002, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.5915776732425098, var=1.2444799571288427, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F
    Total Standard Deviation in ln(k): 8.747909205099575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F
Total Standard Deviation in ln(k): 8.747909205099575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F
Total Standard Deviation in ln(k): 8.747909205099575
""",
)

entry(
    index = 231,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F",
    kinetics = ArrheniusBM(A=(1.96769e+12,'m^3/(mol*s)'), n=-2.49008, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.561975312443171, var=20.897815470982355, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F
    Total Standard Deviation in ln(k): 25.651846856202972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F
Total Standard Deviation in ln(k): 25.651846856202972""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F
Total Standard Deviation in ln(k): 25.651846856202972
""",
)

entry(
    index = 232,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.42839e+09,'m^3/(mol*s)'), n=-0.858081, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2836956944043455, var=1.879997451977643, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.461555640720101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.461555640720101""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.461555640720101
""",
)

entry(
    index = 233,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.42539e+07,'m^3/(mol*s)'), n=-0.0588999, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0006873947870885464, var=0.08095746924661941, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R',), comment="""BM rule fitted to 13 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R
    Total Standard Deviation in ln(k): 0.572134916759976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R
Total Standard Deviation in ln(k): 0.572134916759976""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R
Total Standard Deviation in ln(k): 0.572134916759976
""",
)

entry(
    index = 234,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.40149e+06,'m^3/(mol*s)'), n=0.21338, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0017612663798735474, var=0.03659456747547423, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.38792523090451425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.38792523090451425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.38792523090451425
""",
)

entry(
    index = 235,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(8.08049e+08,'m^3/(mol*s)'), n=-0.685207, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6917880236490241, var=1.0574712108854185, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.799698489863698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.799698489863698""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.799698489863698
""",
)

entry(
    index = 236,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_Sp-3C#1C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(700,'K'), Tmax=(1300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_Sp-3C#1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_Sp-3C#1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_Sp-3C#1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_Sp-3C#1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C",
    kinetics = ArrheniusBM(A=(6.69463e+07,'m^3/(mol*s)'), n=-7.99781e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5431028170894588, var=1.169250943463992, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C
    Total Standard Deviation in ln(k): 3.5323382233389444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C
Total Standard Deviation in ln(k): 3.5323382233389444""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C
Total Standard Deviation in ln(k): 3.5323382233389444
""",
)

entry(
    index = 238,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.51e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.03525e+13,'m^3/(mol*s)'), n=-2.15889, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.973209122599727, var=0.6161879564490669, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl
    Total Standard Deviation in ln(k): 16.58173285619418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl
Total Standard Deviation in ln(k): 16.58173285619418""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl
Total Standard Deviation in ln(k): 16.58173285619418
""",
)

entry(
    index = 240,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_N-3BrCl->Cl",
    kinetics = ArrheniusBM(A=(310000,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_N-3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_N-3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_2BrClF->F",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=0, w0=(77500,'J/mol'), E0=(7750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_2BrClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_2BrClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_2BrClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_2BrClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_N-2BrClF->F",
    kinetics = ArrheniusBM(A=(2471.06,'m^3/(mol*s)'), n=0.904611, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_N-2BrClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_N-2BrClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_N-2BrClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_3R!H->O_Ext-1C-R_N-2BrClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F",
    kinetics = ArrheniusBM(A=(4.89025e+07,'m^3/(mol*s)'), n=-0.0872928, w0=(138167,'J/mol'), E0=(13816.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.028349900009321957, var=1.9500655922472314, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F',), comment="""BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F
    Total Standard Deviation in ln(k): 2.870738171430556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F
Total Standard Deviation in ln(k): 2.870738171430556""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F
Total Standard Deviation in ln(k): 2.870738171430556
""",
)

entry(
    index = 244,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F",
    kinetics = ArrheniusBM(A=(1.55067e+10,'m^3/(mol*s)'), n=-1.14677, w0=(122026,'J/mol'), E0=(12202.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07300119405006171, var=7.019863103051127, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F',), comment="""BM rule fitted to 19 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F
    Total Standard Deviation in ln(k): 5.494970535714952"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F
Total Standard Deviation in ln(k): 5.494970535714952""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F
Total Standard Deviation in ln(k): 5.494970535714952
""",
)

entry(
    index = 245,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl",
    kinetics = ArrheniusBM(A=(3.78978e+23,'m^3/(mol*s)'), n=-5.14229, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6840673045874602, var=5.791996170721132, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl
    Total Standard Deviation in ln(k): 6.543471052225111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl
Total Standard Deviation in ln(k): 6.543471052225111""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl
Total Standard Deviation in ln(k): 6.543471052225111
""",
)

entry(
    index = 246,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_N-2BrClF->Cl",
    kinetics = ArrheniusBM(A=(8.69957e+07,'m^3/(mol*s)'), n=1.4253e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0307128888740362, var=2.413897921625167, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_N-2BrClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_N-2BrClF->Cl
    Total Standard Deviation in ln(k): 5.704432432467972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_N-2BrClF->Cl
Total Standard Deviation in ln(k): 5.704432432467972""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_N-2BrClF->Cl
Total Standard Deviation in ln(k): 5.704432432467972
""",
)

entry(
    index = 247,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.845,'m^3/(mol*s)'), n=1.52, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(0.0239,'m^3/(mol*s)'), n=2.243, w0=(71000,'J/mol'), E0=(7100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-1C_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.05e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_2R->O_Ext-2O-R_N-3R!H->C_N-1C-inRing_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.66162e+11,'m^3/(mol*s)'), n=-1.04561, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15735395298261987, var=2.9166807203134337, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.8191068788315063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.8191068788315063""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.8191068788315063
""",
)

entry(
    index = 251,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(8.53922e+07,'m^3/(mol*s)'), n=-0.366667, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.47840081731895e-10, var=0.6179647339259807, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O
    Total Standard Deviation in ln(k): 1.5759369389680384"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O
Total Standard Deviation in ln(k): 1.5759369389680384""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O
Total Standard Deviation in ln(k): 1.5759369389680384
""",
)

entry(
    index = 252,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(8.09045e+08,'m^3/(mol*s)'), n=-0.842857, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.923656798976024e-09, var=1.2914637284046604, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 2.2782327881968145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.2782327881968145""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.2782327881968145
""",
)

entry(
    index = 253,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(4.08827e+07,'m^3/(mol*s)'), n=-0.166667, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.0483586226707595e-10, var=0.2145040668203127, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 0.9284847072091169"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F
Total Standard Deviation in ln(k): 0.9284847072091169""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F
Total Standard Deviation in ln(k): 0.9284847072091169
""",
)

entry(
    index = 255,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.26211e+07,'m^3/(mol*s)'), n=-0.41693, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.048519644711244994, var=1.0788940168572585, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 2.2042234352789687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 2.2042234352789687""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 2.2042234352789687
""",
)

entry(
    index = 256,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br",
    kinetics = ArrheniusBM(A=(1.69158e+09,'m^3/(mol*s)'), n=-0.838064, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0315988796402225, var=11.501395669676128, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br
    Total Standard Deviation in ln(k): 9.390756918241319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br
Total Standard Deviation in ln(k): 9.390756918241319""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br
Total Standard Deviation in ln(k): 9.390756918241319
""",
)

entry(
    index = 257,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br",
    kinetics = ArrheniusBM(A=(2101.18,'m^3/(mol*s)'), n=0.782425, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09109769161563774, var=13.803032201107863, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br',), comment="""BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br
    Total Standard Deviation in ln(k): 7.676967081267349"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br
Total Standard Deviation in ln(k): 7.676967081267349""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br
Total Standard Deviation in ln(k): 7.676967081267349
""",
)

entry(
    index = 258,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.26e+18,'m^3/(mol*s)'), n=-3.5, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_3BrClFO->F_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.816e+40,'m^3/(mol*s)'), n=-10.56, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-2C-R_N-3BrClFO->F_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C",
    kinetics = ArrheniusBM(A=(8.65419e+10,'m^3/(mol*s)'), n=-1.4012, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11076293667129158, var=0.13376655749343178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C
    Total Standard Deviation in ln(k): 1.01151286269961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C
Total Standard Deviation in ln(k): 1.01151286269961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C
Total Standard Deviation in ln(k): 1.01151286269961
""",
)

entry(
    index = 261,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-5R!H-2C",
    kinetics = ArrheniusBM(A=(578146,'m^3/(mol*s)'), n=0.175759, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06243996161282631, var=0.8653650783542394, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-5R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-5R!H-2C
    Total Standard Deviation in ln(k): 2.0217891484895985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-5R!H-2C
Total Standard Deviation in ln(k): 2.0217891484895985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-5R!H-2C
Total Standard Deviation in ln(k): 2.0217891484895985
""",
)

entry(
    index = 262,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO",
    kinetics = ArrheniusBM(A=(3.63105e+07,'m^3/(mol*s)'), n=-0.118135, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09812769830724073, var=0.8853225170864677, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO
    Total Standard Deviation in ln(k): 2.132838887656121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO
Total Standard Deviation in ln(k): 2.132838887656121""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO
Total Standard Deviation in ln(k): 2.132838887656121
""",
)

entry(
    index = 263,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO",
    kinetics = ArrheniusBM(A=(1.41035e+07,'m^3/(mol*s)'), n=-0.0582281, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0014254821486938106, var=0.07747373274449407, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO',), comment="""BM rule fitted to 11 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO
    Total Standard Deviation in ln(k): 0.5615816533094558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO
Total Standard Deviation in ln(k): 0.5615816533094558""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO
Total Standard Deviation in ln(k): 0.5615816533094558
""",
)

entry(
    index = 264,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(5.749e+06,'m^3/(mol*s)'), n=0.214, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(8.43648e+08,'m^3/(mol*s)'), n=-0.692983, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4860153208082551, var=0.496261552627412, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 2.633396366652887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 2.633396366652887""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 2.633396366652887
""",
)

entry(
    index = 266,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_Sp-3C-1C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.61751e+07,'m^3/(mol*s)'), n=-6.16459e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.8359635529677596, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.926397146884914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.926397146884914""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R
Total Standard Deviation in ln(k): 3.926397146884914
""",
)

entry(
    index = 268,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.568e+40,'m^3/(mol*s)'), n=-10.21, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_N-3BrCClO->C_N-3BrClO->O_3BrCl->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl",
    kinetics = ArrheniusBM(A=(5.22702e+07,'m^3/(mol*s)'), n=-0.0787487, w0=(155333,'J/mol'), E0=(15533.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02451618762175356, var=4.9403887668910045, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl
    Total Standard Deviation in ln(k): 4.517520176167911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl
Total Standard Deviation in ln(k): 4.517520176167911""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl
Total Standard Deviation in ln(k): 4.517520176167911
""",
)

entry(
    index = 270,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl",
    kinetics = ArrheniusBM(A=(4.4323e+07,'m^3/(mol*s)'), n=-0.099908, w0=(121000,'J/mol'), E0=(12100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010361591850434167, var=1.5954990583812823, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl
    Total Standard Deviation in ln(k): 2.5582764871690657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl
Total Standard Deviation in ln(k): 2.5582764871690657""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl
Total Standard Deviation in ln(k): 2.5582764871690657
""",
)

entry(
    index = 271,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.68932e+09,'m^3/(mol*s)'), n=-0.967138, w0=(118964,'J/mol'), E0=(11896.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06778529350464901, var=8.464686155979734, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R',), comment="""BM rule fitted to 14 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R
    Total Standard Deviation in ln(k): 6.002917844743358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.002917844743358""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.002917844743358
""",
)

entry(
    index = 272,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C",
    kinetics = ArrheniusBM(A=(9.41375e+09,'m^3/(mol*s)'), n=-0.868761, w0=(133250,'J/mol'), E0=(13325,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06536771439585853, var=4.820752765144456, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C
    Total Standard Deviation in ln(k): 4.565879466839341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C
Total Standard Deviation in ln(k): 4.565879466839341""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C
Total Standard Deviation in ln(k): 4.565879466839341
""",
)

entry(
    index = 273,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_N-3BrCCl->C",
    kinetics = ArrheniusBM(A=(3.10362e+29,'m^3/(mol*s)'), n=-7.43807, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_N-3BrCCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_N-3BrCCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_N-3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_N-3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl_Ext-3BrCClFINPSSi-R",
    kinetics = ArrheniusBM(A=(2.16447e+13,'m^3/(mol*s)'), n=-2.06111, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl_Ext-3BrCClFINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl_Ext-3BrCClFINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl_Ext-3BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_N-Sp-3BrCClFINPSSi-1C_2BrClF->Cl_Ext-3BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 275,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.04023e+12,'m^3/(mol*s)'), n=-1.07166, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9125875942573384, var=1.0150541438967988, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.312702149012238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.312702149012238""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.312702149012238
""",
)

entry(
    index = 276,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.24e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.26848e+08,'m^3/(mol*s)'), n=-0.55, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.18719384195212638, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 0.8673667472246991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 0.8673667472246991""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 0.8673667472246991
""",
)

entry(
    index = 278,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.55114e+09,'m^3/(mol*s)'), n=-1.1, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6290223088470565e-10, var=2.385481895038608, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 3.096314395311866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 3.096314395311866""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 3.096314395311866
""",
)

entry(
    index = 279,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.98065e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.8575717470917588, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 1.8564883221612534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.8564883221612534""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.8564883221612534
""",
)

entry(
    index = 280,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.14427e+07,'m^3/(mol*s)'), n=-0.25, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.08329721466536308, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 0.5785917397417829"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 0.5785917397417829""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 0.5785917397417829
""",
)

entry(
    index = 281,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(1.4e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(1.40244e+08,'m^3/(mol*s)'), n=-0.486419, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05660625256296303, var=0.9524191860640369, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br',), comment="""BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 2.098687143732801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 2.098687143732801""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 2.098687143732801
""",
)

entry(
    index = 284,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(2.61e+20,'m^3/(mol*s)'), n=-4.16, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_N-6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_3BrF->Br_Ext-2C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.872689,'m^3/(mol*s)'), n=1.86906, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06927577281098518, var=19.79125405093615, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R
    Total Standard Deviation in ln(k): 9.092597302573001"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R
Total Standard Deviation in ln(k): 9.092597302573001""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R
Total Standard Deviation in ln(k): 9.092597302573001
""",
)

entry(
    index = 287,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.144e+13,'m^3/(mol*s)'), n=-2.163, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.307e+06,'m^3/(mol*s)'), n=0.192, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-5R!H-2C_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.02e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_Sp-4R!H=3BrBrCCClClOO_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO",
    kinetics = ArrheniusBM(A=(2.1838e+06,'m^3/(mol*s)'), n=0.213378, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00012636871532894028, var=0.09909832320097778, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO',), comment="""BM rule fitted to 9 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO
    Total Standard Deviation in ln(k): 0.6314058293054976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO
Total Standard Deviation in ln(k): 0.6314058293054976""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO
Total Standard Deviation in ln(k): 0.6314058293054976
""",
)

entry(
    index = 291,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO",
    kinetics = ArrheniusBM(A=(5.67927e+10,'m^3/(mol*s)'), n=-1.26686, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04628379485594601, var=0.016181722463235428, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO
    Total Standard Deviation in ln(k): 0.3713080775392354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO
Total Standard Deviation in ln(k): 0.3713080775392354""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO
Total Standard Deviation in ln(k): 0.3713080775392354
""",
)

entry(
    index = 292,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 293,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_3BrCClO->C_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.45019e+07,'m^3/(mol*s)'), n=-0.118123, w0=(146500,'J/mol'), E0=(14650,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.553220035741629, var=23.930171509944362, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.196858273429688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.196858273429688""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.196858273429688
""",
)

entry(
    index = 295,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.58758e+07,'m^3/(mol*s)'), n=-0.196729, w0=(95000,'J/mol'), E0=(9500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.194188275337443, var=18.76893549339875, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 21.7358640462344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 21.7358640462344""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 21.7358640462344
""",
)

entry(
    index = 296,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_2BrClF->Br",
    kinetics = ArrheniusBM(A=(1.83961e-10,'m^3/(mol*s)'), n=4.9034, w0=(95000,'J/mol'), E0=(9500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_2BrClF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_2BrClF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_2BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_2BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br",
    kinetics = ArrheniusBM(A=(4.1872e+09,'m^3/(mol*s)'), n=-0.983792, w0=(120808,'J/mol'), E0=(12080.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06689582892829628, var=8.432759574580496, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br',), comment="""BM rule fitted to 13 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br
    Total Standard Deviation in ln(k): 5.989673091405689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br
Total Standard Deviation in ln(k): 5.989673091405689""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br
Total Standard Deviation in ln(k): 5.989673091405689
""",
)

entry(
    index = 298,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(13966.5,'m^3/(mol*s)'), n=0.851267, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_2BrClF->Cl",
    kinetics = ArrheniusBM(A=(2.83841e+07,'m^3/(mol*s)'), n=-0.124284, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.8173205029976955, var=4.404153343002604, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_2BrClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_2BrClF->Cl
    Total Standard Deviation in ln(k): 11.285846754203854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_2BrClF->Cl
Total Standard Deviation in ln(k): 11.285846754203854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_2BrClF->Cl
Total Standard Deviation in ln(k): 11.285846754203854
""",
)

entry(
    index = 300,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_N-2BrClF->Cl",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_N-2BrClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_N-2BrClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_N-2BrClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_3BrCCl->C_N-2BrClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.045e+09,'m^3/(mol*s)'), n=-0.155, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.75e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_5R!H->O_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.14759e+09,'m^3/(mol*s)'), n=-1.3, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=5.519561616726178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.70987392894025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.70987392894025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.70987392894025
""",
)

entry(
    index = 304,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_N-4R!H->C_Ext-2C-R_N-5R!H->F_5BrCClINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.70046e+07,'m^3/(mol*s)'), n=-0.310596, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.050622581079904395, var=0.5556016594801264, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 1.6214957181473881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 1.6214957181473881""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 1.6214957181473881
""",
)

entry(
    index = 306,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(3.7825e+09,'m^3/(mol*s)'), n=-0.838064, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0315988796402227, var=1.2438535871505778, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 4.827801613908831"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 4.827801613908831""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 4.827801613908831
""",
)

entry(
    index = 307,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(0.262388,'m^3/(mol*s)'), n=1.84767, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(1.24116e+12,'m^3/(mol*s)'), n=-1.70328, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0479956330405713, var=9.25818087769394, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F
    Total Standard Deviation in ln(k): 11.245577005399817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F
Total Standard Deviation in ln(k): 11.245577005399817""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F
Total Standard Deviation in ln(k): 11.245577005399817
""",
)

entry(
    index = 309,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(0.926954,'m^3/(mol*s)'), n=1.93973, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10632795446047869, var=11.538410229017435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 7.076886986635893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F
Total Standard Deviation in ln(k): 7.076886986635893""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F
Total Standard Deviation in ln(k): 7.076886986635893
""",
)

entry(
    index = 310,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.04918e+06,'m^3/(mol*s)'), n=0.213251, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00013798341536148888, var=0.060961023872127366, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.4953215226285012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.4953215226285012""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.4953215226285012
""",
)

entry(
    index = 311,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_3BrCClO-inRing",
    kinetics = ArrheniusBM(A=(5.781e+11,'m^3/(mol*s)'), n=-1.568, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_3BrCClO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_3BrCClO-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_3BrCClO-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_3BrCClO-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_N-3BrCClO-inRing",
    kinetics = ArrheniusBM(A=(5.89e+07,'m^3/(mol*s)'), n=-0.278, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_N-3BrCClO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_N-3BrCClO-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_N-3BrCClO-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_N-Sp-4R!H-3BrCClO_N-3BrCClO-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1437.61,'m^3/(mol*s)'), n=1.09579, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_2BrClF->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(410.863,'m^3/(mol*s)'), n=1.33656, w0=(95000,'J/mol'), E0=(9500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(6.84618,'m^3/(mol*s)'), n=1.32431, w0=(95000,'J/mol'), E0=(9500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_3BrCClFINPSSi->F_N-2BrClF->Cl_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.01884e+08,'m^3/(mol*s)'), n=-0.59042, w0=(125889,'J/mol'), E0=(12588.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12317114248532375, var=9.225117330486402, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C',), comment="""BM rule fitted to 9 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 6.398432674830539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C
Total Standard Deviation in ln(k): 6.398432674830539""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C
Total Standard Deviation in ln(k): 6.398432674830539
""",
)

entry(
    index = 317,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.79065e+13,'m^3/(mol*s)'), n=-1.86888, w0=(109375,'J/mol'), E0=(10937.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05972366141338131, var=1.2344729219769406, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 2.3774571847539363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.3774571847539363""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.3774571847539363
""",
)

entry(
    index = 318,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'m^3/(mol*s)'), n=-1.5, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_3R!H->C_4R!H->C_Ext-2C-R_N-5R!H->O_Ext-2C-R_Ext-1C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(10014.3,'m^3/(mol*s)'), n=0.814498, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05147561620024199, var=0.5005225736282355, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 1.5476380737451465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 1.5476380737451465""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 1.5476380737451465
""",
)

entry(
    index = 320,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_4R!H->F",
    kinetics = ArrheniusBM(A=(2.61e+20,'m^3/(mol*s)'), n=-4.16, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.4e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_N-4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_N-4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_N-6CClFINOPSSi->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.61e+20,'m^3/(mol*s)'), n=-4.16, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_6R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.0120018,'m^3/(mol*s)'), n=2.37126, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_N-3BrClFO->Cl_N-3BrF->Br_Ext-2C-R_N-6R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.92432e+06,'m^3/(mol*s)'), n=0.212764, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00020627826416470317, var=0.015197222285993836, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.24765604215378806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24765604215378806""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24765604215378806
""",
)

entry(
    index = 325,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(3.406e+06,'m^3/(mol*s)'), n=0.211, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R",
    kinetics = ArrheniusBM(A=(6.91241e+11,'m^3/(mol*s)'), n=-1.58733, w0=(133250,'J/mol'), E0=(13325,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10134339720935424, var=10.628530930686342, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R
    Total Standard Deviation in ln(k): 6.790354234954921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 6.790354234954921""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 6.790354234954921
""",
)

entry(
    index = 327,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl",
    kinetics = ArrheniusBM(A=(37020,'m^3/(mol*s)'), n=0.27383, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2813461351078374, var=9.153871462273763, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl
    Total Standard Deviation in ln(k): 6.772299102211457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl
Total Standard Deviation in ln(k): 6.772299102211457""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl
Total Standard Deviation in ln(k): 6.772299102211457
""",
)

entry(
    index = 328,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_N-3BrCCl->Cl",
    kinetics = ArrheniusBM(A=(1.81048e+30,'m^3/(mol*s)'), n=-7.09644, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_N-3BrCCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_N-3BrCCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_N-3BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_N-3BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.61359e+11,'m^3/(mol*s)'), n=-1.4048, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5081716130487887, var=0.010089181152055815, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.4781785445816915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.4781785445816915""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.4781785445816915
""",
)

entry(
    index = 330,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_2ClF->F",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(77500,'J/mol'), E0=(7750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_2ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_2ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_2ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_2ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_N-2ClF->F",
    kinetics = ArrheniusBM(A=(2578.46,'m^3/(mol*s)'), n=0.884262, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_N-2ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_N-2ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_N-2ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_N-2ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.41e+06,'m^3/(mol*s)'), n=0.13553, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0385813605207892, var=0.9147642637194259, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 4.526895878994763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 4.526895878994763""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 4.526895878994763
""",
)

entry(
    index = 333,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.83855e+06,'m^3/(mol*s)'), n=0.213183, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00010035158993549042, var=0.009543722532482049, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.19609867441050194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.19609867441050194""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.19609867441050194
""",
)

entry(
    index = 334,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.918e+06,'m^3/(mol*s)'), n=0.213, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R",
    kinetics = ArrheniusBM(A=(503936,'m^3/(mol*s)'), n=0.201599, w0=(146500,'J/mol'), E0=(14650,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4909903565862891, var=28.077794572380725, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R
    Total Standard Deviation in ln(k): 11.856431408305534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 11.856431408305534""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 11.856431408305534
""",
)

entry(
    index = 336,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.17037e+12,'m^3/(mol*s)'), n=-1.62373, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl",
    kinetics = ArrheniusBM(A=(58730.7,'m^3/(mol*s)'), n=0.120563, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22537422888034733, var=12.062884295612854, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl
    Total Standard Deviation in ln(k): 7.529045260726398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl
Total Standard Deviation in ln(k): 7.529045260726398""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl
Total Standard Deviation in ln(k): 7.529045260726398
""",
)

entry(
    index = 338,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.21509e+31,'m^3/(mol*s)'), n=-7.40295, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.64994e+14,'m^3/(mol*s)'), n=-2.23152, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 341,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(0.00243875,'m^3/(mol*s)'), n=2.77174, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_N-4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_Ext-1C-R_N-3R!H->C_Ext-1C-R_3BrClFO->Cl_Ext-2C-R_N-6R!H->Br_6CClFINOPSSi->Cl_Ext-2C-R_Ext-2C-R_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.73772e+06,'m^3/(mol*s)'), n=0.212577, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002012875862712629, var=0.0027626568967285335, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.11042832265502614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.11042832265502614""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.11042832265502614
""",
)

entry(
    index = 343,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.942e+06,'m^3/(mol*s)'), n=0.212, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(2.53123,'m^3/(mol*s)'), n=1.5854, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_Ext-3BrCCl-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 346,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10.4062,'m^3/(mol*s)'), n=1.35186, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.622854080197698, var=2.276579561256996, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 17.152586198863773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 17.152586198863773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 17.152586198863773
""",
)

entry(
    index = 347,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.674e+06,'m^3/(mol*s)'), n=0.22, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_2BrCClFN->C_Ext-1C-R_N-3R!H->F_Ext-3BrCClO-R_N-Sp-3BrBrCCClClOO=1C_Ext-2C-R_N-Sp-4R!H=3BrBrCCClClOO_Sp-4R!H-3BrCClO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.05803e+27,'m^3/(mol*s)'), n=-6.59025, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.98116e+19,'m^3/(mol*s)'), n=-4.24465, w0=(120000,'J/mol'), E0=(12000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-2R-inRing_N-2R->O_N-2BrCClFNS->S_N-2BrCClFN->C_N-2BrClFN->N_Ext-1C-R_N-3R!H->O_Sp-3BrCClFINPSSi-1C_N-3BrCClFINPSSi->F_Ext-1C-R_N-2BrClF->Br_Sp-4R!H-1C_3BrCCl->Cl_4R!H->Cl_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

