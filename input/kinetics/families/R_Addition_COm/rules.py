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
    kinetics = ArrheniusBM(A=(2.11841e-07,'m^3/(mol*s)'), n=3.9427, w0=(311031,'J/mol'), E0=(-1234.69,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13575344533520034, var=7.854311148868744, Tref=1000.0, N=16, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 16 training reactions at node Root
    Total Standard Deviation in ln(k): 5.959468164861423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root
Total Standard Deviation in ln(k): 5.959468164861423""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root
Total Standard Deviation in ln(k): 5.959468164861423
""",
)

entry(
    index = 2,
    label = "Root_3R->O",
    kinetics = ArrheniusBM(A=(34.1,'m^3/(mol*s)'), n=0, w0=(315500,'J/mol'), E0=(38037.3,'J/mol'), Tmin=(250,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O
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
    kinetics = ArrheniusBM(A=(2.08323e-07,'m^3/(mol*s)'), n=3.95022, w0=(310733,'J/mol'), E0=(263.35,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1293545781998449, var=7.512823412212755, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 15 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 5.819896151009567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 5.819896151009567""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 5.819896151009567
""",
)

entry(
    index = 4,
    label = "Root_N-3R->O_3BrCClFHINPSSi->Cl",
    kinetics = ArrheniusBM(A=(510289,'m^3/(mol*s)'), n=0.692613, w0=(300000,'J/mol'), E0=(8806.86,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl",
    kinetics = ArrheniusBM(A=(4.58372e-06,'m^3/(mol*s)'), n=3.5153, w0=(311500,'J/mol'), E0=(24107.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20527405964849496, var=0.6303372002404294, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl
    Total Standard Deviation in ln(k): 2.1073988879835306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl
Total Standard Deviation in ln(k): 2.1073988879835306""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl
Total Standard Deviation in ln(k): 2.1073988879835306
""",
)

entry(
    index = 6,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing",
    kinetics = ArrheniusBM(A=(5.44233,'m^3/(mol*s)'), n=1.61182, w0=(309500,'J/mol'), E0=(38312.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.45664945129539924, var=0.9066904653816424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing
    Total Standard Deviation in ln(k): 3.0562750928360427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing
Total Standard Deviation in ln(k): 3.0562750928360427""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing
Total Standard Deviation in ln(k): 3.0562750928360427
""",
)

entry(
    index = 7,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing",
    kinetics = ArrheniusBM(A=(3.88591e-10,'m^3/(mol*s)'), n=4.72567, w0=(311833,'J/mol'), E0=(2198.09,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27199401204558205, var=0.36475445233267323, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing
    Total Standard Deviation in ln(k): 1.8941598813892644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing
Total Standard Deviation in ln(k): 1.8941598813892644""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing
Total Standard Deviation in ln(k): 1.8941598813892644
""",
)

entry(
    index = 8,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00721,'m^3/(mol*s)'), n=2.333, w0=(309500,'J/mol'), E0=(19464.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.48e+06,'m^3/(mol*s)'), n=0, w0=(309500,'J/mol'), E0=(53857.6,'J/mol'), Tmin=(295,'K'), Tmax=(500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S",
    kinetics = ArrheniusBM(A=(0.0785,'m^3/(mol*s)'), n=2.33, w0=(272500,'J/mol'), E0=(17156.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S",
    kinetics = ArrheniusBM(A=(3.72468e-10,'m^3/(mol*s)'), n=4.73082, w0=(315409,'J/mol'), E0=(7551.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2716117939454119, var=0.3574739272942776, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S
    Total Standard Deviation in ln(k): 1.8810552219262369"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S
Total Standard Deviation in ln(k): 1.8810552219262369""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S
Total Standard Deviation in ln(k): 1.8810552219262369
""",
)

entry(
    index = 12,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C",
    kinetics = ArrheniusBM(A=(3.20526e-10,'m^3/(mol*s)'), n=4.75465, w0=(309500,'J/mol'), E0=(3920.47,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.26993938778100807, var=0.3202843583115101, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C
    Total Standard Deviation in ln(k): 1.8127928394088793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C
Total Standard Deviation in ln(k): 1.8127928394088793""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C
Total Standard Deviation in ln(k): 1.8127928394088793
""",
)

entry(
    index = 13,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C",
    kinetics = ArrheniusBM(A=(10660.4,'m^3/(mol*s)'), n=0.267963, w0=(342000,'J/mol'), E0=(39557.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.498300370263393e-14, var=3.447156939379626, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C
    Total Standard Deviation in ln(k): 3.72209554762774"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C
Total Standard Deviation in ln(k): 3.72209554762774""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C
Total Standard Deviation in ln(k): 3.72209554762774
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000449881,'m^3/(mol*s)'), n=2.9724, w0=(309500,'J/mol'), E0=(29276.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.33380827393585727, var=0.5816574297381158, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.367654912933306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.367654912933306""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.367654912933306
""",
)

entry(
    index = 15,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(2.21686,'m^3/(mol*s)'), n=1.88741, w0=(309500,'J/mol'), E0=(37668.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1631993703566574, var=0.32974246485079184, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 1.5612318331652342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.5612318331652342""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.5612318331652342
""",
)

entry(
    index = 16,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(151000,'m^3/(mol*s)'), n=0, w0=(309500,'J/mol'), E0=(54199.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(86.1,'m^3/(mol*s)'), n=1.36, w0=(309500,'J/mol'), E0=(35435.6,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(65100,'m^3/(mol*s)'), n=0.45, w0=(309500,'J/mol'), E0=(45510.1,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

