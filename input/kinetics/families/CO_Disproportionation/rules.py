#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.22153e+08,'m^3/(mol*s)'), n=-0.30144, w0=(538545,'J/mol'), E0=(52206,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00609676168067026, var=1.471494080423145, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 2.4471655040897002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 2.4471655040897002""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 2.4471655040897002
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = ArrheniusBM(A=(1.0118e+17,'m^3/(mol*s)'), n=-3.5096, w0=(540500,'J/mol'), E0=(74783.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.6923442808920424, var=23.356488200257658, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 2 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 16.453278220699985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 16.453278220699985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 16.453278220699985
""",
)

entry(
    index = 3,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(2.10155e+08,'m^3/(mol*s)'), n=-0.293831, w0=(538419,'J/mol'), E0=(51795.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0007657004564548826, var=1.4624408777256033, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 31 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 2.4262785028007907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.4262785028007907""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.4262785028007907
""",
)

entry(
    index = 4,
    label = "Root_4R->F_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.56076e+06,'m^3/(mol*s)'), n=-0.37188, w0=(456500,'J/mol'), E0=(53882.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->F_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_4R->F_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->F_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->F_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(624500,'J/mol'), E0=(62450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.54341e+08,'m^3/(mol*s)'), n=-0.293949, w0=(552375,'J/mol'), E0=(47542.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005028914109254805, var=1.6475732536556684, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 2.5858699062906316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 2.5858699062906316""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 2.5858699062906316
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.88585e+07,'m^3/(mol*s)'), n=-1.37186e-06, w0=(481167,'J/mol'), E0=(48116.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23667450879198645, var=14.314694158999966, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 8.179527553124553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 8.179527553124553""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 8.179527553124553
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(5.82482e+07,'m^3/(mol*s)'), n=0.00613463, w0=(525000,'J/mol'), E0=(62869.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0006814739112206298, var=1.1136605340104735, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 2.1173114946029674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 2.1173114946029674""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 2.1173114946029674
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.5e+06,'m^3/(mol*s)'), n=0, w0=(463500,'J/mol'), E0=(46350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.58028e+08,'m^3/(mol*s)'), n=-0.29671, w0=(557053,'J/mol'), E0=(47626.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0041354585220646925, var=1.6365440576655519, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 2.5749976987684673"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.5749976987684673""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.5749976987684673
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1",
    kinetics = ArrheniusBM(A=(3.3e+06,'m^3/(mol*s)'), n=0, w0=(436000,'J/mol'), E0=(43600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(8.47383e+07,'m^3/(mol*s)'), n=-6.21879e-07, w0=(503750,'J/mol'), E0=(50375,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.869432596513741, var=2.8830969004063767, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
    Total Standard Deviation in ln(k): 5.588480948873488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 5.588480948873488""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 5.588480948873488
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(661500,'J/mol'), E0=(66150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(5.3449e+07,'m^3/(mol*s)'), n=0.0176911, w0=(505500,'J/mol'), E0=(50550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0033647747605111246, var=1.1123656983996422, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 2.1228232118268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.1228232118268""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.1228232118268
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.50985e+12,'m^3/(mol*s)'), n=-1.834, w0=(555500,'J/mol'), E0=(55550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.348932807076703, var=2.542729147143, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.0734535699512975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.0734535699512975""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.0734535699512975
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C",
    kinetics = ArrheniusBM(A=(6.25167e+07,'m^3/(mol*s)'), n=-9.0103e-08, w0=(553500,'J/mol'), E0=(55350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0031921542129807468, var=1.0702847590705382, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
    Total Standard Deviation in ln(k): 2.0820104970522872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
Total Standard Deviation in ln(k): 2.0820104970522872""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
Total Standard Deviation in ln(k): 2.0820104970522872
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.07891e+06,'m^3/(mol*s)'), n=0.147057, w0=(558625,'J/mol'), E0=(40807.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.028139476788709043, var=0.7450897853973363, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
    Total Standard Deviation in ln(k): 1.8011611243176393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
Total Standard Deviation in ln(k): 1.8011611243176393""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
Total Standard Deviation in ln(k): 1.8011611243176393
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(436000,'J/mol'), E0=(43600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(1004,'K'), Tmax=(1006,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C",
    kinetics = ArrheniusBM(A=(6.96799e+07,'m^3/(mol*s)'), n=0.0338771, w0=(498500,'J/mol'), E0=(49850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24867130550542382, var=0.4249142058009384, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
    Total Standard Deviation in ln(k): 1.931597728448083"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
Total Standard Deviation in ln(k): 1.931597728448083""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
Total Standard Deviation in ln(k): 1.931597728448083
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.61035e+12,'m^3/(mol*s)'), n=-1.84566, w0=(559500,'J/mol'), E0=(55950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9145279427973008, var=7.286723720769605, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 7.709377164164958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.709377164164958""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.709377164164958
""",
)

entry(
    index = 24,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.2e+08,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi",
    kinetics = ArrheniusBM(A=(6.2313e+07,'m^3/(mol*s)'), n=-9.35116e-08, w0=(559500,'J/mol'), E0=(55950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.198027582217755e-17, var=1.1009420470081581, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi
    Total Standard Deviation in ln(k): 2.103484027846209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi
Total Standard Deviation in ln(k): 2.103484027846209""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi
Total Standard Deviation in ln(k): 2.103484027846209
""",
)

entry(
    index = 26,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi",
    kinetics = ArrheniusBM(A=(9.033e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F",
    kinetics = ArrheniusBM(A=(9.73296e+06,'m^3/(mol*s)'), n=0.0622327, w0=(559833,'J/mol'), E0=(55983.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02244669160841792, var=0.370834765711014, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
    Total Standard Deviation in ln(k): 1.27720628428308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
Total Standard Deviation in ln(k): 1.27720628428308""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
Total Standard Deviation in ln(k): 1.27720628428308
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F",
    kinetics = ArrheniusBM(A=(5.04951e+06,'m^3/(mol*s)'), n=0.147811, w0=(557417,'J/mol'), E0=(40789.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.024894622095148367, var=0.7494905720258703, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
    Total Standard Deviation in ln(k): 1.798111077039817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
Total Standard Deviation in ln(k): 1.798111077039817""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
Total Standard Deviation in ln(k): 1.798111077039817
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H",
    kinetics = ArrheniusBM(A=(9.06547e+07,'m^3/(mol*s)'), n=6.04376e-07, w0=(536000,'J/mol'), E0=(53600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09418405436783228, var=0.020821354172507158, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
    Total Standard Deviation in ln(k): 0.525918734315385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
Total Standard Deviation in ln(k): 0.525918734315385""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
Total Standard Deviation in ln(k): 0.525918734315385
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H",
    kinetics = ArrheniusBM(A=(398759,'m^3/(mol*s)'), n=0.698585, w0=(479750,'J/mol'), E0=(47975,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9997914002048836, var=5.718788261674738, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
    Total Standard Deviation in ln(k): 7.306159769579684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
Total Standard Deviation in ln(k): 7.306159769579684""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
Total Standard Deviation in ln(k): 7.306159769579684
""",
)

entry(
    index = 31,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.24e+17,'m^3/(mol*s)'), n=-3.29, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(1140,'K'), Tmax=(1650,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.3e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s",
    kinetics = ArrheniusBM(A=(2.23e+07,'m^3/(mol*s)'), n=0, w0=(621500,'J/mol'), E0=(62150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.34148e+07,'m^3/(mol*s)'), n=6.48377e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07796006527962528, var=0.6194006755696545, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
    Total Standard Deviation in ln(k): 1.773646410187546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
Total Standard Deviation in ln(k): 1.773646410187546""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
Total Standard Deviation in ln(k): 1.773646410187546
""",
)

entry(
    index = 37,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br",
    kinetics = ArrheniusBM(A=(5.05103e+06,'m^3/(mol*s)'), n=0.14778, w0=(554600,'J/mol'), E0=(40782,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.026894009020033128, var=0.7519926610728278, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
    Total Standard Deviation in ln(k): 1.8060292363038886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
Total Standard Deviation in ln(k): 1.8060292363038886""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
Total Standard Deviation in ln(k): 1.8060292363038886
""",
)

entry(
    index = 39,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(514000,'J/mol'), E0=(51400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=0, w0=(558000,'J/mol'), E0=(55800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(168431,'m^3/(mol*s)'), n=0.798014, w0=(420000,'J/mol'), E0=(42000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9676196688144243, var=7.626664266065631, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s
    Total Standard Deviation in ln(k): 10.48012777674486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 10.48012777674486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 10.48012777674486
""",
)

entry(
    index = 42,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=6.92418e-08, w0=(539500,'J/mol'), E0=(53950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 43,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.6701e+07,'m^3/(mol*s)'), n=4.35436e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5802397596505944, var=6.126243023057026, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 8.932421265126099"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 8.932421265126099""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 8.932421265126099
""",
)

entry(
    index = 44,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.35259e+06,'m^3/(mol*s)'), n=0.34378, w0=(571500,'J/mol'), E0=(48305.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7079809437654317, var=0.7504398514196472, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 3.515507121771856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 3.515507121771856""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 3.515507121771856
""",
)

entry(
    index = 45,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(6.26195e+07,'m^3/(mol*s)'), n=-0.225888, w0=(543333,'J/mol'), E0=(47954,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14155019311980244, var=0.365970777372714, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 1.5684286336873867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 1.5684286336873867""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 1.5684286336873867
""",
)

entry(
    index = 46,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Br",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=0, w0=(523000,'J/mol'), E0=(52300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Br",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=0, w0=(556000,'J/mol'), E0=(55600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(1.5e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(9.00001e+07,'m^3/(mol*s)'), n=-1.0785e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 50,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O",
    kinetics = ArrheniusBM(A=(5.12e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(53273.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O",
    kinetics = ArrheniusBM(A=(3.2e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->N",
    kinetics = ArrheniusBM(A=(7.1e+06,'m^3/(mol*s)'), n=0, w0=(535000,'J/mol'), E0=(32890,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N",
    kinetics = ArrheniusBM(A=(1.34165e+07,'m^3/(mol*s)'), n=-4.9914e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5990137911088773e-17, var=0.6909863268735121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N
    Total Standard Deviation in ln(k): 1.666447807467594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N
Total Standard Deviation in ln(k): 1.666447807467594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N
Total Standard Deviation in ln(k): 1.666447807467594
""",
)

entry(
    index = 54,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_Sp-5ClO-4C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_Sp-5ClO-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_Sp-5ClO-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_N-Sp-5ClO-4C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_N-Sp-5ClO-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_N-Sp-5ClO-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_N-Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->N_N-Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

