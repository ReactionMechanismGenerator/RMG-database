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
    kinetics = ArrheniusBM(A=(6.29343,'m^3/(mol*s)'), n=1.66139, w0=(309260,'J/mol'), E0=(34985.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11573007844677136, var=2.245248935561745, Tref=1000.0, N=25, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 25 training reactions at node Root
    Total Standard Deviation in ln(k): 3.2947051547119814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 3.2947051547119814""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 3.2947051547119814
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
    kinetics = ArrheniusBM(A=(7.99521,'m^3/(mol*s)'), n=1.6324, w0=(309000,'J/mol'), E0=(35256,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1115888061711757, var=2.1796999039379337, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 24 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 3.240126015973336"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 3.240126015973336""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 3.240126015973336
""",
)

entry(
    index = 4,
    label = "Root_N-3R->O_3BrCClFHILiNPSSi-inRing",
    kinetics = ArrheniusBM(A=(2.9842e+12,'m^3/(mol*s)'), n=-1.83853, w0=(309500,'J/mol'), E0=(88335.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7492643634509326, var=19.225178571687767, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHILiNPSSi-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing
    Total Standard Deviation in ln(k): 10.67264068098515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing
Total Standard Deviation in ln(k): 10.67264068098515""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHILiNPSSi-inRing
Total Standard Deviation in ln(k): 10.67264068098515
""",
)

entry(
    index = 5,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing",
    kinetics = ArrheniusBM(A=(70.3758,'m^3/(mol*s)'), n=1.36591, w0=(308955,'J/mol'), E0=(37168.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07463121575859509, var=1.8512158602129138, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing',), comment="""BM rule fitted to 22 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing
    Total Standard Deviation in ln(k): 2.915146008202195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing
Total Standard Deviation in ln(k): 2.915146008202195""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing
Total Standard Deviation in ln(k): 2.915146008202195
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
    kinetics = ArrheniusBM(A=(82.4216,'m^3/(mol*s)'), n=1.34657, w0=(309500,'J/mol'), E0=(37408.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07291224505541641, var=1.7913810978170361, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C
    Total Standard Deviation in ln(k): 2.8663838548869465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 2.8663838548869465""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C
Total Standard Deviation in ln(k): 2.8663838548869465
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
    kinetics = ArrheniusBM(A=(0.0975068,'m^3/(mol*s)'), n=2.12726, w0=(309500,'J/mol'), E0=(28778.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15047370452906858, var=1.1242926907944517, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.5037487446341427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.5037487446341427""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.5037487446341427
""",
)

entry(
    index = 11,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_3BrClHS->H",
    kinetics = ArrheniusBM(A=(108628,'m^3/(mol*s)'), n=2.13154e-07, w0=(342000,'J/mol'), E0=(42072.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22965952706397344, var=3.3312781784544088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_3BrClHS->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_3BrClHS->H
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
    kinetics = ArrheniusBM(A=(8420.83,'m^3/(mol*s)'), n=0.883518, w0=(283833,'J/mol'), E0=(435.813,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.401267284743942, var=8.301756895320313, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H
    Total Standard Deviation in ln(k): 9.296969052955761"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 9.296969052955761""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 9.296969052955761
""",
)

entry(
    index = 13,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(0.000102219,'m^3/(mol*s)'), n=2.95466, w0=(309500,'J/mol'), E0=(24644.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2741715740412194, var=13.940609415670894, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 15.711666264302762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 15.711666264302762""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 15.711666264302762
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(0.159021,'m^3/(mol*s)'), n=2.07034, w0=(309500,'J/mol'), E0=(28790,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12680805925897037, var=1.309014302619107, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.6122739772701853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.6122739772701853""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.6122739772701853
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
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.2204460492503136e-16, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S
    Total Standard Deviation in ln(k): 5.579010173995762e-16"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 5.579010173995762e-16""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 5.579010173995762e-16
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
    kinetics = ArrheniusBM(A=(0.345213,'m^3/(mol*s)'), n=1.9259, w0=(309500,'J/mol'), E0=(28921.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11197236064544114, var=0.9530845555890362, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 2.238481250093344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 2.238481250093344""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 2.238481250093344
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
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Br",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Br",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_N-3BrCClFHILiNPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.00478,'m^3/(mol*s)'), n=1.49528, w0=(309500,'J/mol'), E0=(29240.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13273787963556394, var=1.2297118459789653, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.5566105664237306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.5566105664237306""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.5566105664237306
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
    kinetics = ArrheniusBM(A=(0.00377487,'m^3/(mol*s)'), n=2.39679, w0=(309500,'J/mol'), E0=(23225.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20471932392855188, var=1.021366897486608, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O
    Total Standard Deviation in ln(k): 2.5404095223350027"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 2.5404095223350027""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 2.5404095223350027
""",
)

entry(
    index = 25,
    label = "Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.358238,'m^3/(mol*s)'), n=1.93137, w0=(309500,'J/mol'), E0=(23325.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.011879235910704779, var=1.5932829402420126, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 2.5603304336492037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.5603304336492037""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHILiNPSSi-inRing_3BrCClFHILiNPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.5603304336492037
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

