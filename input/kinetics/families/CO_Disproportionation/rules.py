#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.44804e+08,'m^3/(mol*s)'), n=-0.316468, w0=(538545,'J/mol'), E0=(51636.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0015262798766649014, var=1.5100424317381118, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 2.4673291920341294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 2.4673291920341294""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 2.4673291920341294
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = ArrheniusBM(A=(1.91814e+13,'m^3/(mol*s)'), n=-2.08199, w0=(540500,'J/mol'), E0=(85041.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5137923689620686, var=23.356488200257434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 2 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 10.979529698262821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 10.979529698262821""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 10.979529698262821
""",
)

entry(
    index = 3,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(2.44434e+08,'m^3/(mol*s)'), n=-0.316263, w0=(538419,'J/mol'), E0=(51621.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0012485532670703742, var=1.5100571051120721, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 31 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 2.466643355578353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.466643355578353""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.466643355578353
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
    kinetics = ArrheniusBM(A=(1.8511e+08,'m^3/(mol*s)'), n=-0.321896, w0=(552375,'J/mol'), E0=(46880.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014223369626327878, var=1.7241779015513476, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 2.66811374055901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 2.66811374055901""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 2.66811374055901
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.92024e+07,'m^3/(mol*s)'), n=8.16549e-08, w0=(481167,'J/mol'), E0=(48116.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48741399506278976, var=3.2097582940341836, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 4.816301211993547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 4.816301211993547""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 4.816301211993547
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(6.00699e+07,'m^3/(mol*s)'), n=0.000109188, w0=(525000,'J/mol'), E0=(41401,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00018113466936108436, var=1.3236105062180352, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 2.3068681919395404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 2.3068681919395404""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 2.3068681919395404
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
    kinetics = ArrheniusBM(A=(1.85246e+08,'m^3/(mol*s)'), n=-0.32198, w0=(557053,'J/mol'), E0=(46898.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014325958481070253, var=1.7234747446018375, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 2.667834676769385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.667834676769385""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.667834676769385
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
    kinetics = ArrheniusBM(A=(3.12377e+07,'m^3/(mol*s)'), n=1.45838e-07, w0=(503750,'J/mol'), E0=(50375,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1264395127355322, var=2.8830969004063802, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
    Total Standard Deviation in ln(k): 6.234226969531257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 6.234226969531257""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 6.234226969531257
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
    kinetics = ArrheniusBM(A=(6.00753e+07,'m^3/(mol*s)'), n=0.000109034, w0=(505500,'J/mol'), E0=(50550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0003327378179787912, var=1.3236808744461168, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 2.3073104124558945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.3073104124558945""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.3073104124558945
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.1421e+13,'m^3/(mol*s)'), n=-2.12972, w0=(555500,'J/mol'), E0=(55550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3005019187046334, var=11.656645142198801, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
    Total Standard Deviation in ln(k): 12.624687873452743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.624687873452743""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.624687873452743
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C",
    kinetics = ArrheniusBM(A=(6.25168e+07,'m^3/(mol*s)'), n=-3.45136e-07, w0=(553500,'J/mol'), E0=(55350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003192143355334613, var=1.070284523440864, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
    Total Standard Deviation in ln(k): 2.082010241471024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
Total Standard Deviation in ln(k): 2.082010241471024""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
Total Standard Deviation in ln(k): 2.082010241471024
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.35714e+06,'m^3/(mol*s)'), n=0.135187, w0=(558625,'J/mol'), E0=(39956.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03499839790919297, var=0.7634279169875918, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
    Total Standard Deviation in ln(k): 1.8395601608136714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
Total Standard Deviation in ln(k): 1.8395601608136714""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
Total Standard Deviation in ln(k): 1.8395601608136714
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
    kinetics = ArrheniusBM(A=(9.01885e+07,'m^3/(mol*s)'), n=0.000218257, w0=(498500,'J/mol'), E0=(49850,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2661694215799445, var=0.4148271921788538, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
    Total Standard Deviation in ln(k): 1.9599587109569427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
Total Standard Deviation in ln(k): 1.9599587109569427""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
Total Standard Deviation in ln(k): 1.9599587109569427
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
    kinetics = ArrheniusBM(A=(1.23449e+13,'m^3/(mol*s)'), n=-2.14335, w0=(559500,'J/mol'), E0=(55950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9380257635261333, var=7.2867237207734314, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 7.768416914741335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.768416914741335""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.768416914741335
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
    kinetics = ArrheniusBM(A=(6.23131e+07,'m^3/(mol*s)'), n=-3.49414e-07, w0=(559500,'J/mol'), E0=(55950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.198027582217755e-17, var=1.1009420470081581, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi
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
    kinetics = ArrheniusBM(A=(2.98195e+07,'m^3/(mol*s)'), n=0.0257922, w0=(559833,'J/mol'), E0=(55983.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0024439866322249807, var=1.5370553811673036, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
    Total Standard Deviation in ln(k): 2.491571878328233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
Total Standard Deviation in ln(k): 2.491571878328233""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
Total Standard Deviation in ln(k): 2.491571878328233
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F",
    kinetics = ArrheniusBM(A=(5.344e+06,'m^3/(mol*s)'), n=0.135462, w0=(557417,'J/mol'), E0=(39938.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03513841557944398, var=0.7627399901293258, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
    Total Standard Deviation in ln(k): 1.8391225894742675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
Total Standard Deviation in ln(k): 1.8391225894742675""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
Total Standard Deviation in ln(k): 1.8391225894742675
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H",
    kinetics = ArrheniusBM(A=(9.0302e+07,'m^3/(mol*s)'), n=-1.29891e-07, w0=(536000,'J/mol'), E0=(53600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1019910880521685, var=0.020821354172517827, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
    Total Standard Deviation in ln(k): 0.545534396838917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
Total Standard Deviation in ln(k): 0.545534396838917""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
Total Standard Deviation in ln(k): 0.545534396838917
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H",
    kinetics = ArrheniusBM(A=(1.93391e+07,'m^3/(mol*s)'), n=0.267658, w0=(479750,'J/mol'), E0=(47975,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.025362236003123807, var=1.541524865671735, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
    Total Standard Deviation in ln(k): 2.552766392973036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
Total Standard Deviation in ln(k): 2.552766392973036""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
Total Standard Deviation in ln(k): 2.552766392973036
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
    kinetics = ArrheniusBM(A=(4.05287e+07,'m^3/(mol*s)'), n=3.44701e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.366606069790188e-08, var=1.8967965625483778, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
    Total Standard Deviation in ln(k): 2.76100623629726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
Total Standard Deviation in ln(k): 2.76100623629726""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
Total Standard Deviation in ln(k): 2.76100623629726
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
    kinetics = ArrheniusBM(A=(5.34536e+06,'m^3/(mol*s)'), n=0.135438, w0=(554600,'J/mol'), E0=(39931,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03510195829096911, var=0.7628712296327066, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
    Total Standard Deviation in ln(k): 1.8391816089371245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
Total Standard Deviation in ln(k): 1.8391816089371245""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
Total Standard Deviation in ln(k): 1.8391816089371245
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
    kinetics = ArrheniusBM(A=(2.20001e+06,'m^3/(mol*s)'), n=0.535316, w0=(420000,'J/mol'), E0=(42000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.553540862245973, var=7.626664266065631, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s
    Total Standard Deviation in ln(k): 6.9271659511959855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 6.9271659511959855""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 6.9271659511959855
""",
)

entry(
    index = 42,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=2.47112e-08, w0=(539500,'J/mol'), E0=(53950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s
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
    kinetics = ArrheniusBM(A=(4.95288e+07,'m^3/(mol*s)'), n=2.07798e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.4435660415346896e-08, var=2.4078016270543454, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 3.1107660445024883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 3.1107660445024883""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 3.1107660445024883
""",
)

entry(
    index = 44,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(5.86578e+07,'m^3/(mol*s)'), n=-0.0219961, w0=(571500,'J/mol'), E0=(53053.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7548503564847089, var=0.7504398514200321, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 3.6332694652880737"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 3.6332694652880737""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 3.6332694652880737
""",
)

entry(
    index = 45,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(5.49658e+07,'m^3/(mol*s)'), n=-0.202911, w0=(543333,'J/mol'), E0=(48998.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11412682380708698, var=0.3975736520698647, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 1.5508052785163553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 1.5508052785163553""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 1.5508052785163553
""",
)

entry(
    index = 46,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=0, w0=(556000,'J/mol'), E0=(55600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=0, w0=(523000,'J/mol'), E0=(52300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl
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
    kinetics = ArrheniusBM(A=(8.99999e+07,'m^3/(mol*s)'), n=1.01746e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl
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
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C",
    kinetics = ArrheniusBM(A=(1.34165e+07,'m^3/(mol*s)'), n=-5.25438e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.5990137911088773e-17, var=0.6909863268735121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C
    Total Standard Deviation in ln(k): 1.666447807467594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C
Total Standard Deviation in ln(k): 1.666447807467594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C
Total Standard Deviation in ln(k): 1.666447807467594
""",
)

entry(
    index = 53,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C",
    kinetics = ArrheniusBM(A=(7.1e+06,'m^3/(mol*s)'), n=0, w0=(535000,'J/mol'), E0=(32890,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C
Total Standard Deviation in ln(k): 11.540182761524994
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
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

