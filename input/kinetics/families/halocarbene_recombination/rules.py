#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_recombination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(75605.2,'m^3/(mol*s)'), n=0.682327, w0=(183269,'J/mol'), E0=(87511.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05457040371156418, var=2.6382609270530293, Tref=1000.0, N=13, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 13 training reactions at node Root
    Total Standard Deviation in ln(k): 3.3933474828999826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 3.3933474828999826""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 3.3933474828999826
""",
)

entry(
    index = 2,
    label = "Root_3R->H",
    kinetics = ArrheniusBM(A=(0.00565551,'m^3/(mol*s)'), n=1.68897, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.936386579929548, var=929.3177971072018, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H
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
    kinetics = ArrheniusBM(A=(63154.2,'m^3/(mol*s)'), n=0.705896, w0=(179227,'J/mol'), E0=(87072.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05927841061078631, var=2.2907909046545187, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H
    Total Standard Deviation in ln(k): 3.1831792292503716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 3.1831792292503716""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 3.1831792292503716
""",
)

entry(
    index = 4,
    label = "Root_3R->H_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.75,'m^3/(mol*s)'), n=-0.32, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_2Br1sCl1sF1s->F1s
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
    index = 5,
    label = "Root_3R->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_N-2Br1sCl1sF1s->F1s
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
    index = 6,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(6912.66,'m^3/(mol*s)'), n=0.88362, w0=(175000,'J/mol'), E0=(74275.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.022519973100929, var=8.723497440193778, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.002807282955068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.002807282955068""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.002807282955068
""",
)

entry(
    index = 7,
    label = "Root_N-3R->H_2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.58997e+07,'m^3/(mol*s)'), n=0, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.516371693678081e-17, var=0.00031645152361524197, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s
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
    kinetics = ArrheniusBM(A=(7460.27,'m^3/(mol*s)'), n=0.971709, w0=(198167,'J/mol'), E0=(19816.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04072871657116345, var=1.1710208520609804, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 2.2717317995321182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.2717317995321182""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.2717317995321182
""",
)

entry(
    index = 9,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.688205,'m^3/(mol*s)'), n=2.10503, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04071303363488713, var=4.525941154293647, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 4.367219472194393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.367219472194393""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.367219472194393
""",
)

entry(
    index = 10,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1030.64,'m^3/(mol*s)'), n=1.11337, w0=(179000,'J/mol'), E0=(71471.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.959163457932656, var=17.937199025784615, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 13.413041516348061"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 13.413041516348061""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 13.413041516348061
""",
)

entry(
    index = 11,
    label = "Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.58e+07,'m^3/(mol*s)'), n=0, w0=(163500,'J/mol'), E0=(16350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_4R!H->Cl
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
    kinetics = ArrheniusBM(A=(1.6e+07,'m^3/(mol*s)'), n=0, w0=(163500,'J/mol'), E0=(16350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_2Br1sCl1sF1s->Cl1s_Ext-1C2s-R_N-4R!H->Cl
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
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(518506,'m^3/(mol*s)'), n=0.4717, w0=(242500,'J/mol'), E0=(24250,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_3BrCClFINOPSSi->F
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
    index = 14,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(1645.46,'m^3/(mol*s)'), n=1.1338, w0=(176000,'J/mol'), E0=(17600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16258386636944783, var=0.009743831490678022, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F
    Total Standard Deviation in ln(k): 0.6063912760871357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F
Total Standard Deviation in ln(k): 0.6063912760871357""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F
Total Standard Deviation in ln(k): 0.6063912760871357
""",
)

entry(
    index = 15,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00827325,'m^3/(mol*s)'), n=2.66158, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0018213548763702779, var=4.631531336261048, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 4.3189651969608445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.3189651969608445""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.3189651969608445
""",
)

entry(
    index = 16,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.435021,'m^3/(mol*s)'), n=2.13915, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-2Br1sCl1sF1s->F1s
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
    index = 17,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-1C2s-R",
    kinetics = ArrheniusBM(A=(0.00128024,'m^3/(mol*s)'), n=2.72845, w0=(179000,'J/mol'), E0=(53660.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-1C2s-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-1C2s-R
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
    index = 18,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_3CClO->C",
    kinetics = ArrheniusBM(A=(2.1e+07,'m^3/(mol*s)'), n=-0.207, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_3CClO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_3CClO->C
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
    index = 19,
    label = "Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_N-3CClO->C",
    kinetics = ArrheniusBM(A=(37018.9,'m^3/(mol*s)'), n=0.7539, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_N-3CClO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-2Br1sCl1sF1s->Cl1s_N-3BrCClFINOPSSi->F_N-3CClO->C
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

entry(
    index = 20,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_4R!H->Br",
    kinetics = ArrheniusBM(A=(0.000635481,'m^3/(mol*s)'), n=2.96807, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_4R!H->Br
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
    index = 21,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(0.171991,'m^3/(mol*s)'), n=2.29089, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19875658759278098, var=4.780591033171826, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br
    Total Standard Deviation in ln(k): 4.882653996447726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br
Total Standard Deviation in ln(k): 4.882653996447726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br
Total Standard Deviation in ln(k): 4.882653996447726
""",
)

entry(
    index = 22,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_4ClF->Cl",
    kinetics = ArrheniusBM(A=(0.00385582,'m^3/(mol*s)'), n=2.7545, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_4ClF->Cl
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
    index = 23,
    label = "Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_N-4ClF->Cl",
    kinetics = ArrheniusBM(A=(0.360802,'m^3/(mol*s)'), n=2.20685, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_N-4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s_N-4R!H->Br_N-4ClF->Cl
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

