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
    kinetics = ArrheniusBM(A=(8.84834e-08,'m^3/(mol*s)'), n=4.04003, w0=(311767,'J/mol'), E0=(18497.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.34901204780000616, var=1.312973380326202, Tref=1000.0, N=15, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 15 training reactions at node Root
    Total Standard Deviation in ln(k): 3.174041394240774"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 3.174041394240774""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 3.174041394240774
""",
)

entry(
    index = 2,
    label = "Root_3R->O",
    kinetics = ArrheniusBM(A=(34.1,'m^3/(mol*s)'), n=0, w0=(315500,'J/mol'), E0=(38680.4,'J/mol'), Tmin=(250,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O
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
    kinetics = ArrheniusBM(A=(2.52892e-07,'m^3/(mol*s)'), n=3.91171, w0=(311500,'J/mol'), E0=(20148.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2565375932481569, var=0.8662030436982899, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 2.510374350072273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 2.510374350072273""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 2.510374350072273
""",
)

entry(
    index = 4,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing",
    kinetics = ArrheniusBM(A=(0.54353,'m^3/(mol*s)'), n=1.90208, w0=(309500,'J/mol'), E0=(34802.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8899633431015483, var=5.713141267334562, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
    Total Standard Deviation in ln(k): 7.027842325024919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 7.027842325024919""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 7.027842325024919
""",
)

entry(
    index = 5,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing",
    kinetics = ArrheniusBM(A=(1.98274e-10,'m^3/(mol*s)'), n=4.84396, w0=(311833,'J/mol'), E0=(-1284.85,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3423534458267846, var=0.6708318766756058, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
    Total Standard Deviation in ln(k): 2.502149308743089"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 2.502149308743089""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 2.502149308743089
""",
)

entry(
    index = 6,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00721,'m^3/(mol*s)'), n=2.333, w0=(309500,'J/mol'), E0=(19547.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.48e+06,'m^3/(mol*s)'), n=0, w0=(309500,'J/mol'), E0=(30950,'J/mol'), Tmin=(295,'K'), Tmax=(500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->S",
    kinetics = ArrheniusBM(A=(0.0785,'m^3/(mol*s)'), n=2.33, w0=(272500,'J/mol'), E0=(17010.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S",
    kinetics = ArrheniusBM(A=(1.89419e-10,'m^3/(mol*s)'), n=4.8497, w0=(315409,'J/mol'), E0=(-14.0108,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.31305882830599674, var=0.617183119173318, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S
    Total Standard Deviation in ln(k): 2.361519954830997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S
Total Standard Deviation in ln(k): 2.361519954830997""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S
Total Standard Deviation in ln(k): 2.361519954830997
""",
)

entry(
    index = 10,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C",
    kinetics = ArrheniusBM(A=(1.58745e-10,'m^3/(mol*s)'), n=4.87772, w0=(309500,'J/mol'), E0=(7681.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3161332320216064, var=0.5774520046009709, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C
    Total Standard Deviation in ln(k): 2.3177080575631877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C
Total Standard Deviation in ln(k): 2.3177080575631877""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C
Total Standard Deviation in ln(k): 2.3177080575631877
""",
)

entry(
    index = 11,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_N-3CH->C",
    kinetics = ArrheniusBM(A=(8670.49,'m^3/(mol*s)'), n=0.298626, w0=(342000,'J/mol'), E0=(39387,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4035802319134083e-14, var=3.4471569393796186, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_N-3CH->C
    Total Standard Deviation in ln(k): 3.7220955476277338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_N-3CH->C
Total Standard Deviation in ln(k): 3.7220955476277338""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_N-3CH->C
Total Standard Deviation in ln(k): 3.7220955476277338
""",
)

entry(
    index = 12,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0017649,'m^3/(mol*s)'), n=2.83344, w0=(309500,'J/mol'), E0=(30438.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.46583540094766596, var=1.0501424159045343, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.2248221776009673"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.2248221776009673""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.2248221776009673
""",
)

entry(
    index = 13,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(6.56364,'m^3/(mol*s)'), n=1.7839, w0=(309500,'J/mol'), E0=(38382.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25380045622134867, var=0.6455339621509006, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 2.248396556003819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 2.248396556003819""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 2.248396556003819
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(151000,'m^3/(mol*s)'), n=0, w0=(309500,'J/mol'), E0=(53377.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(86.1,'m^3/(mol*s)'), n=1.36, w0=(309500,'J/mol'), E0=(32718.8,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(65100,'m^3/(mol*s)'), n=0.45, w0=(309500,'J/mol'), E0=(44182.4,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

