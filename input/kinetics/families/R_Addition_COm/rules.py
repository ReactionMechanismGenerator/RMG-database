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
    kinetics = ArrheniusBM(A=(5.399e-07,'m^3/(mol*s)'), n=3.6848, w0=(309.147,'kJ/mol'), E0=(0.789777,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21800607627160032, var=1.0779149116324411, Tref=1000.0, N=17, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 17 training reactions at node Root
    Total Standard Deviation in ln(k): 2.629123667318262"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 2.629123667318262""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 2.629123667318262
""",
)

entry(
    index = 2,
    label = "Root_3R->O",
    kinetics = ArrheniusBM(A=(34.1,'m^3/(mol*s)'), n=8.73864e-09, w0=(315.5,'kJ/mol'), E0=(38.2966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O
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
    kinetics = ArrheniusBM(A=(5.26781e-07,'m^3/(mol*s)'), n=3.69359, w0=(308.75,'kJ/mol'), E0=(1.37158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2726407497382492, var=0.8332092296870747, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 16 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 2.514955106572823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 2.514955106572823""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 2.514955106572823
""",
)

entry(
    index = 4,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing",
    kinetics = ArrheniusBM(A=(1543.38,'m^3/(mol*s)'), n=0.822145, w0=(309.5,'kJ/mol'), E0=(44.2693,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.619936358896929, var=0.6050239551292623, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
    Total Standard Deviation in ln(k): 3.116977857423543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 3.116977857423543""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 3.116977857423543
""",
)

entry(
    index = 5,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00721,'m^3/(mol*s)'), n=2.333, w0=(309.5,'kJ/mol'), E0=(24.0321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
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
    index = 6,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.48e+06,'m^3/(mol*s)'), n=-5.71646e-08, w0=(309.5,'kJ/mol'), E0=(56.2476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
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
    index = 7,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing",
    kinetics = ArrheniusBM(A=(4.39285e-08,'m^3/(mol*s)'), n=4.0393, w0=(308.643,'kJ/mol'), E0=(1.19897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3050609923875642, var=0.7568498784418518, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
    Total Standard Deviation in ln(k): 2.510546674490639"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 2.510546674490639""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 2.510546674490639
""",
)

entry(
    index = 8,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(0.329931,'m^3/(mol*s)'), n=2.07304, w0=(309.5,'kJ/mol'), E0=(35.2326,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17748312369238067, var=0.6615994821919932, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 2.07656426623308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 2.07656426623308""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 2.07656426623308
""",
)

entry(
    index = 9,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.38524,'m^3/(mol*s)'), n=2.06248, w0=(309.5,'kJ/mol'), E0=(34.0162,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.38782405154121735, var=0.6270161579590485, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.5618687678621175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.5618687678621175""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.5618687678621175
""",
)

entry(
    index = 10,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(23.0301,'m^3/(mol*s)'), n=1.55685, w0=(309.5,'kJ/mol'), E0=(38.7455,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2575027022079667, var=0.3660078182804922, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 1.8598279688063668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.8598279688063668""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.8598279688063668
""",
)

entry(
    index = 11,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(86.1,'m^3/(mol*s)'), n=1.36, w0=(309.5,'kJ/mol'), E0=(36.9208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(65100,'m^3/(mol*s)'), n=0.45, w0=(309.5,'kJ/mol'), E0=(47.04,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(151000,'m^3/(mol*s)'), n=-5.25699e-09, w0=(309.5,'kJ/mol'), E0=(54.9314,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(55.8514,'m^3/(mol*s)'), n=1.28151, w0=(307.1,'kJ/mol'), E0=(1.0936,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06328152068894752, var=19.051458367848703, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 8.909261714191546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 8.909261714191546""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 8.909261714191546
""",
)

entry(
    index = 15,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H",
    kinetics = ArrheniusBM(A=(108632,'m^3/(mol*s)'), n=-4.60906e-06, w0=(342,'kJ/mol'), E0=(41.8896,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.240078279053628, var=3.3259218898925673, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H
    Total Standard Deviation in ln(k): 4.259269212221103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H
Total Standard Deviation in ln(k): 4.259269212221103""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H
Total Standard Deviation in ln(k): 4.259269212221103
""",
)

entry(
    index = 16,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H",
    kinetics = ArrheniusBM(A=(8419.86,'m^3/(mol*s)'), n=0.883532, w0=(283.833,'kJ/mol'), E0=(0.553942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28895894903747316, var=15.648181251818048, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H
    Total Standard Deviation in ln(k): 8.656314847416924"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 8.656314847416924""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 8.656314847416924
""",
)

entry(
    index = 17,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S",
    kinetics = ArrheniusBM(A=(0.0785,'m^3/(mol*s)'), n=2.33, w0=(272.5,'kJ/mol'), E0=(18.6817,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S",
    kinetics = ArrheniusBM(A=(2.15963e+08,'m^3/(mol*s)'), n=-0.382318, w0=(289.5,'kJ/mol'), E0=(1.07698,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21203992351622103, var=5.181761909275315, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S
    Total Standard Deviation in ln(k): 5.09623905601216"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 5.09623905601216""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 5.09623905601216
""",
)

entry(
    index = 19,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=5.22723e-11, w0=(300,'kJ/mol'), E0=(8.34816,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl",
    kinetics = ArrheniusBM(A=(4.66398e+09,'m^3/(mol*s)'), n=-0.764636, w0=(279,'kJ/mol'), E0=(-7.96975,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

