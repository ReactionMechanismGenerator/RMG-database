#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/rules"
shortDesc = ""
longDesc = """
.. [MRHCBSQB31DHR] M.R. Harper (mrharper_at_mit_dot_edu or michael_dot_harper_dot_jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 method.
The zero-point energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were from 600 K to 2000 K (in 200 K increments).
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.46013,'m^3/(mol*s)'), n=1.65813, w0=(309.26,'kJ/mol'), E0=(35.0115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11537021406729327, var=2.2540103864782677, Tref=1000.0, N=25, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 25 training reactions at node Root
    Total Standard Deviation in ln(k): 3.2996562535180143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 3.2996562535180143""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 3.2996562535180143
""",
)

entry(
    index = 2,
    label = "Root_3R->O",
    kinetics = Arrhenius(A=(34.1,'m^3/(mol*s)'), n=0, Ea=(12.552,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-3R->O",
    kinetics = ArrheniusBM(A=(8.18431,'m^3/(mol*s)'), n=1.62949, w0=(309,'kJ/mol'), E0=(35.2786,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11125278711769374, var=2.1885058628082565, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 24 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 3.245254400505945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 3.245254400505945""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 3.245254400505945
""",
)

entry(
    index = 4,
    label = "Root_N-3R->O_3BrCClFHILiNPSSi-inRing",
    kinetics = ArrheniusBM(A=(2.9873e+12,'m^3/(mol*s)'), n=-1.83865, w0=(309.5,'kJ/mol'), E0=(88.3418,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7492643634509331, var=19.22517857168778, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHILiNPSSi-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing
    Total Standard Deviation in ln(k): 10.672640680985154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing
Total Standard Deviation in ln(k): 10.672640680985154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing
Total Standard Deviation in ln(k): 10.672640680985154
""",
)

entry(
    index = 5,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing",
    kinetics = ArrheniusBM(A=(72.3876,'m^3/(mol*s)'), n=1.36241, w0=(308.955,'kJ/mol'), E0=(37.1962,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07424789166528742, var=1.8599385894143288, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing',), comment="""BM rule fitted to 22 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing
    Total Standard Deviation in ln(k): 2.920601480198346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing
Total Standard Deviation in ln(k): 2.920601480198346""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing
Total Standard Deviation in ln(k): 2.920601480198346
""",
)

entry(
    index = 6,
    label = "Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_4R!H->O",
    kinetics = Arrhenius(A=(0.00721,'m^3/(mol*s)'), n=2.333, Ea=(79.1989,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_N-4R!H->O",
    kinetics = Arrhenius(A=(1.48e+06,'m^3/(mol*s)'), n=0, Ea=(13.9327,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing_Ext-3BrCClFHILiNPSSi-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C",
    kinetics = ArrheniusBM(A=(82.6638,'m^3/(mol*s)'), n=1.34621, w0=(309.5,'kJ/mol'), E0=(37.4135,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07308513015339768, var=1.7913295390847204, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C
    Total Standard Deviation in ln(k): 2.8667796261275176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 2.8667796261275176""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 2.8667796261275176
""",
)

entry(
    index = 9,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C",
    kinetics = Arrhenius(A=(39205.8,'m^3/(mol*s)'), n=0.466, Ea=(8.32616,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=16.727866914248505, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C
    Total Standard Deviation in ln(k): 8.199309342237632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 8.199309342237632""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 8.199309342237632
""",
)

entry(
    index = 10,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0975505,'m^3/(mol*s)'), n=2.1272, w0=(309.5,'kJ/mol'), E0=(28.7802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15060152792921594, var=1.1242739114361322, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.5040521560334135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.5040521560334135""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.5040521560334135
""",
)

entry(
    index = 11,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_3BrClHS->H",
    kinetics = ArrheniusBM(A=(108625,'m^3/(mol*s)'), n=3.40544e-06, w0=(342,'kJ/mol'), E0=(42.0738,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22965952706397344, var=3.3312781784544088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_3BrClHS->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_3BrClHS->H
    Total Standard Deviation in ln(k): 4.23603423961363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_3BrClHS->H
Total Standard Deviation in ln(k): 4.23603423961363""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_3BrClHS->H
Total Standard Deviation in ln(k): 4.23603423961363
""",
)

entry(
    index = 12,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H",
    kinetics = ArrheniusBM(A=(5.93364e+09,'m^3/(mol*s)'), n=-0.792006, w0=(283.833,'kJ/mol'), E0=(19.2713,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11005208683164575, var=23.3123829941055, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H
    Total Standard Deviation in ln(k): 9.955954831704492"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 9.955954831704492""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 9.955954831704492
""",
)

entry(
    index = 13,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(0.000102254,'m^3/(mol*s)'), n=2.95462, w0=(309.5,'kJ/mol'), E0=(24.6457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.274171574041219, var=13.940609415670908, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 15.711666264302766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 15.711666264302766""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 15.711666264302766
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(0.159162,'m^3/(mol*s)'), n=2.07023, w0=(309.5,'kJ/mol'), E0=(28.7921,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12693616824412626, var=1.3090080190473476, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.612590354084446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.612590354084446""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.612590354084446
""",
)

entry(
    index = 15,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_3BrClS->S",
    kinetics = Arrhenius(A=(0.0785,'m^3/(mol*s)'), n=2.33, Ea=(9.33032,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_3BrClS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_3BrClS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_3BrClS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_3BrClS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S",
    kinetics = ArrheniusBM(A=(3.96438e+11,'m^3/(mol*s)'), n=-1.31744, w0=(289.5,'kJ/mol'), E0=(1.40127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9921003823903957, var=5.694365672835682, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S
    Total Standard Deviation in ln(k): 7.276587793366115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 7.276587793366115""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 7.276587793366115
""",
)

entry(
    index = 17,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = Arrhenius(A=(0.00292607,'m^3/(mol*s)'), n=2.53895, Ea=(18.1366,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C",
    kinetics = ArrheniusBM(A=(0.344932,'m^3/(mol*s)'), n=1.926, w0=(309.5,'kJ/mol'), E0=(28.9215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11210725290903542, var=0.9530754357014053, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 2.2388108115857674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 2.2388108115857674""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 2.2388108115857674
""",
)

entry(
    index = 19,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C",
    kinetics = Arrhenius(A=(0.044717,'m^3/(mol*s)'), n=2.50145, Ea=(20.1485,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.00038,'m^3/(mol*s)'), n=1.49534, w0=(309.5,'kJ/mol'), E0=(29.2407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13285739246707087, var=1.229700386829896, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.5569004918534466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.5569004918534466""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.5569004918534466
""",
)

entry(
    index = 23,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R",
    kinetics = Arrhenius(A=(86.1,'m^3/(mol*s)'), n=1.36, Ea=(20.0832,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.00377486,'m^3/(mol*s)'), n=2.39679, w0=(309.5,'kJ/mol'), E0=(23.2264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20471932392855288, var=1.0213668974866132, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O
    Total Standard Deviation in ln(k): 2.5404095223350107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 2.5404095223350107""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 2.5404095223350107
""",
)

entry(
    index = 25,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.357894,'m^3/(mol*s)'), n=1.93149, w0=(309.5,'kJ/mol'), E0=(23.3251,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02721028638464279, var=1.4625341585392388, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 2.4927995027242456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.4927995027242456""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.4927995027242456
""",
)

entry(
    index = 26,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R",
    kinetics = Arrhenius(A=(0.00319398,'m^3/(mol*s)'), n=2.29874, Ea=(6.82299,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R",
    kinetics = Arrhenius(A=(0.0078093,'m^3/(mol*s)'), n=2.36815, Ea=(10.2421,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R",
    kinetics = Arrhenius(A=(0.00120086,'m^3/(mol*s)'), n=2.6776, Ea=(3.24074,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

