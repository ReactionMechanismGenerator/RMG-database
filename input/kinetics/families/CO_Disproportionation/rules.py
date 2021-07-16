#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.26213e+08,'m^3/(mol*s)'), n=-0.304933, w0=(555750,'J/mol'), E0=(51228.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010370501779796268, var=1.4505817431476606, Tref=1000.0, N=40, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 40 training reactions at node Root
    Total Standard Deviation in ln(k): 2.417110564311995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root
Total Standard Deviation in ln(k): 2.417110564311995""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root
Total Standard Deviation in ln(k): 2.417110564311995
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.52184e-07, w0=(624500,'J/mol'), E0=(62450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 2 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 3,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(2.2626e+08,'m^3/(mol*s)'), n=-0.304955, w0=(552132,'J/mol'), E0=(51217.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010299550635531265, var=1.4506415100316445, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 38 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 2.4171424781071256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.4171424781071256""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.4171424781071256
""",
)

entry(
    index = 4,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.29951e+08,'m^3/(mol*s)'), n=-0.341525, w0=(571500,'J/mol'), E0=(40067.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25846379949349907, var=7.30810835690849, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 6.068909748210734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 6.068909748210734""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 6.068909748210734
""",
)

entry(
    index = 5,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.83533e+08,'m^3/(mol*s)'), n=-0.260671, w0=(546967,'J/mol'), E0=(57714,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.053320279166543964, var=0.9326916467871187, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O',), comment="""BM rule fitted to 30 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 2.070062740499068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 2.070062740499068""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 2.070062740499068
""",
)

entry(
    index = 6,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(2.3035e+08,'m^3/(mol*s)'), n=-0.341933, w0=(571500,'J/mol'), E0=(40044,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2573899518411482, var=7.37032125247884, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R
    Total Standard Deviation in ln(k): 6.0892304865062545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R
Total Standard Deviation in ln(k): 6.0892304865062545""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R
Total Standard Deviation in ln(k): 6.0892304865062545
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1",
    kinetics = ArrheniusBM(A=(3.88588e+07,'m^3/(mol*s)'), n=-4.06955e-07, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.5083971249720928, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1
    Total Standard Deviation in ln(k): 1.4294156489886742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1
Total Standard Deviation in ln(k): 1.4294156489886742""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1
Total Standard Deviation in ln(k): 1.4294156489886742
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_4BrCHN->N",
    kinetics = ArrheniusBM(A=(7.1e+06,'m^3/(mol*s)'), n=0, w0=(535000,'J/mol'), E0=(32601,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_4BrCHN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_4BrCHN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_4BrCHN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_4BrCHN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N",
    kinetics = ArrheniusBM(A=(3.09874e+07,'m^3/(mol*s)'), n=-2.12665e-08, w0=(547379,'J/mol'), E0=(54737.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0010699907799495345, var=1.1253926840410515, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N',), comment="""BM rule fitted to 29 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N
    Total Standard Deviation in ln(k): 2.129402140817998"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N
Total Standard Deviation in ln(k): 2.129402140817998""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N
Total Standard Deviation in ln(k): 2.129402140817998
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.79349e+08,'m^3/(mol*s)'), n=-0.419602, w0=(571500,'J/mol'), E0=(28331,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.28937402210254554, var=7.751828377951696, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 6.308674956567821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.308674956567821""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.308674956567821
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C",
    kinetics = ArrheniusBM(A=(2.37502e+07,'m^3/(mol*s)'), n=-3.87454e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0022357244698801527, var=0.8603225730181941, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C',), comment="""BM rule fitted to 26 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C
    Total Standard Deviation in ln(k): 1.865080857660669"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C
Total Standard Deviation in ln(k): 1.865080857660669""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C
Total Standard Deviation in ln(k): 1.865080857660669
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C",
    kinetics = ArrheniusBM(A=(9.03103e+07,'m^3/(mol*s)'), n=6.60703e-07, w0=(546333,'J/mol'), E0=(54633.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.29123213614993404, var=0.22810473122184852, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C
    Total Standard Deviation in ln(k): 1.6892067443758203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C
Total Standard Deviation in ln(k): 1.6892067443758203""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C
Total Standard Deviation in ln(k): 1.6892067443758203
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(6.75927e+07,'m^3/(mol*s)'), n=-0.0404796, w0=(571500,'J/mol'), E0=(52782.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9295487538337235, var=6.106406137879262, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 9.80204206739676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 9.80204206739676""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 9.80204206739676
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.83344e+12,'m^3/(mol*s)'), n=-1.86291, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022262966749359486, var=0.7565835597382505, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 1.799691996033835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.799691996033835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.799691996033835
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.99896e+07,'m^3/(mol*s)'), n=-1.05405e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005125652715318646, var=1.2092274587690415, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.217383024186132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.217383024186132""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.217383024186132
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_4BrH->Br",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=0, w0=(523000,'J/mol'), E0=(52300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_4BrH->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_4BrH->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_4BrH->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_4BrH->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_N-4BrH->Br",
    kinetics = ArrheniusBM(A=(9.0299e+07,'m^3/(mol*s)'), n=6.25553e-08, w0=(558000,'J/mol'), E0=(55800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04970053958702819, var=0.0049443218046344006, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_N-4BrH->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_N-4BrH->Br
    Total Standard Deviation in ln(k): 0.2658404219818662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_N-4BrH->Br
Total Standard Deviation in ln(k): 0.2658404219818662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_N-4BrCH->C_N-4BrH->Br
Total Standard Deviation in ln(k): 0.2658404219818662
""",
)

entry(
    index = 20,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_5BrN->N",
    kinetics = ArrheniusBM(A=(1.24e+17,'m^3/(mol*s)'), n=-3.29, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(1140,'K'), Tmax=(1650,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_5BrN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_5BrN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_5BrN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_5BrN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5BrN->N",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5BrN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5BrN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5BrN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5BrN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(9.00001e+07,'m^3/(mol*s)'), n=-9.26571e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.2077456298229986e-09, var=2.052683297350807e-49, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F
    Total Standard Deviation in ln(k): 8.059662386489948e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F
Total Standard Deviation in ln(k): 8.059662386489948e-09""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F
Total Standard Deviation in ln(k): 8.059662386489948e-09
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(1.99775e+07,'m^3/(mol*s)'), n=-1.05423e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004831436287520861, var=1.2092870095235582, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F',), comment="""BM rule fitted to 18 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 2.216698068814673"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.216698068814673""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.216698068814673
""",
)

entry(
    index = 24,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=-5.25094e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.2077456298229982e-09, var=0.0, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R
    Total Standard Deviation in ln(k): 8.059662386489944e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 8.059662386489944e-09""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 8.059662386489944e-09
""",
)

entry(
    index = 25,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.35527e+07,'m^3/(mol*s)'), n=-1.42004e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5769636942231178, var=0.8448990822754837, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C',), comment="""BM rule fitted to 16 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 3.292377773978961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.292377773978961""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.292377773978961
""",
)

entry(
    index = 26,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.34165e+07,'m^3/(mol*s)'), n=-4.9914e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5990137911088773e-17, var=0.6909863268735121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 1.666447807467594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.666447807467594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.666447807467594
""",
)

entry(
    index = 27,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.00001e+07,'m^3/(mol*s)'), n=-1.0785e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_5R!H->F_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C",
    kinetics = ArrheniusBM(A=(7.43475e+07,'m^3/(mol*s)'), n=3.86277e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0485846305060802, var=4.3205696333489305, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C
    Total Standard Deviation in ln(k): 6.801673066506776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C
Total Standard Deviation in ln(k): 6.801673066506776""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C
Total Standard Deviation in ln(k): 6.801673066506776
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C",
    kinetics = ArrheniusBM(A=(4.33827e+07,'m^3/(mol*s)'), n=-1.43564e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6132231012025505, var=0.867170496742862, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C
    Total Standard Deviation in ln(k): 3.407610753281159"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C
Total Standard Deviation in ln(k): 3.407610753281159""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C
Total Standard Deviation in ln(k): 3.407610753281159
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_N-Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_N-Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_N-Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_N-5BrCClINOPSSi->C_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.24071e+07,'m^3/(mol*s)'), n=-3.57839e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7121999401106333e-07, var=4.719499072844586, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R
    Total Standard Deviation in ln(k): 4.355168725520282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R
Total Standard Deviation in ln(k): 4.355168725520282""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R
Total Standard Deviation in ln(k): 4.355168725520282
""",
)

entry(
    index = 33,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.12133e+07,'m^3/(mol*s)'), n=-9.23436e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=16.708497797687528, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R
    Total Standard Deviation in ln(k): 8.19456099691273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R
Total Standard Deviation in ln(k): 8.19456099691273""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R
Total Standard Deviation in ln(k): 8.19456099691273
""",
)

entry(
    index = 34,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.17532e+08,'m^3/(mol*s)'), n=2.63538e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.30566038092716397, var=0.29603682536802245, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.8587525526849447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R
Total Standard Deviation in ln(k): 1.8587525526849447""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R
Total Standard Deviation in ln(k): 1.8587525526849447
""",
)

entry(
    index = 35,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(5.73008e+07,'m^3/(mol*s)'), n=-1.21935e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24792546422855172, var=0.3157005991179311, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R
    Total Standard Deviation in ln(k): 1.7493336207226258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R
Total Standard Deviation in ln(k): 1.7493336207226258""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R
Total Standard Deviation in ln(k): 1.7493336207226258
""",
)

entry(
    index = 36,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_Sp-5C=4C_Ext-4C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.2e+08,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-4C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(5.98168e+07,'m^3/(mol*s)'), n=-1.21968e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02917145391161383, var=0.0814072959081807, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C
    Total Standard Deviation in ln(k): 0.6452853971787856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 0.6452853971787856""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 0.6452853971787856
""",
)

entry(
    index = 43,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(2.7386e+07,'m^3/(mol*s)'), n=4.35355e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.06648230014354244, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C
    Total Standard Deviation in ln(k): 0.5169041366802003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 0.5169041366802003""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 0.5169041366802003
""",
)

entry(
    index = 44,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.34848e+07,'m^3/(mol*s)'), n=-2.28001e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.32880390778633084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.1495436707873932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.1495436707873932""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.1495436707873932
""",
)

entry(
    index = 46,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-4BrCHN->N_4BrCH->C_Ext-4C-R_N-5R!H->F_5BrCClINOPSSi->C_N-Sp-5C=4C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

