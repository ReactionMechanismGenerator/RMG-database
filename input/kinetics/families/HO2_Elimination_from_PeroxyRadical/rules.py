#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.976e+15,'s^-1'), n=-0.927093, w0=(756562,'J/mol'), E0=(89343.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08285287782848783, var=2.443561250754706, Tref=1000.0, N=16, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 16 training reactions at node Root
    Total Standard Deviation in ln(k): 3.341953779155402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root
Total Standard Deviation in ln(k): 3.341953779155402""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root
Total Standard Deviation in ln(k): 3.341953779155402
""",
)

entry(
    index = 2,
    label = "Root_Ext-2CNOSSi-R",
    kinetics = ArrheniusBM(A=(1.60841e+13,'s^-1'), n=-0.245129, w0=(742000,'J/mol'), E0=(88326.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020427157690045845, var=2.887876997955713, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2CNOSSi-R
    Total Standard Deviation in ln(k): 3.458122137031378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2CNOSSi-R
Total Standard Deviation in ln(k): 3.458122137031378""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2CNOSSi-R
Total Standard Deviation in ln(k): 3.458122137031378
""",
)

entry(
    index = 3,
    label = "Root_Ext-1CNSSi-R",
    kinetics = ArrheniusBM(A=(5.02556e+13,'s^-1'), n=-0.336946, w0=(761417,'J/mol'), E0=(77954,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.030070730669515225, var=2.885159181790741, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1CNSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 3.4807487532082284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 3.4807487532082284""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 3.4807487532082284
""",
)

entry(
    index = 4,
    label = "Root_2CNOSSi->C",
    kinetics = ArrheniusBM(A=(2.54746e+08,'s^-1'), n=1.24048, w0=(742000,'J/mol'), E0=(69745,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4974070518435492, var=5.094754190530189, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2CNOSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_2CNOSSi->C
    Total Standard Deviation in ln(k): 8.287329520516446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2CNOSSi->C
Total Standard Deviation in ln(k): 8.287329520516446""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2CNOSSi->C
Total Standard Deviation in ln(k): 8.287329520516446
""",
)

entry(
    index = 5,
    label = "Root_N-2CNOSSi->C",
    kinetics = ArrheniusBM(A=(6.38e+12,'s^-1'), n=0, w0=(858500,'J/mol'), E0=(89900.5,'J/mol'), Tmin=(200,'K'), Tmax=(600,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2CNOSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2CNOSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2CNOSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2CNOSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi",
    kinetics = ArrheniusBM(A=(3.41973e+13,'s^-1'), n=-0.343019, w0=(742000,'J/mol'), E0=(88857.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.028784639924004627, var=2.8883679745093582, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi
    Total Standard Deviation in ln(k): 3.4794104236994423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi
Total Standard Deviation in ln(k): 3.4794104236994423""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi
Total Standard Deviation in ln(k): 3.4794104236994423
""",
)

entry(
    index = 7,
    label = "Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi",
    kinetics = ArrheniusBM(A=(3.63e+09,'s^-1'), n=1.11, w0=(742000,'J/mol'), E0=(115984,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-1CNSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2.72874e+13,'s^-1'), n=-0.259275, w0=(765300,'J/mol'), E0=(77420.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04434751060566427, var=2.974412146040792, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1CNSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 3.5688890743495754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1CNSSi-R_6R!H->C
Total Standard Deviation in ln(k): 3.5688890743495754""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1CNSSi-R_6R!H->C
Total Standard Deviation in ln(k): 3.5688890743495754
""",
)

entry(
    index = 9,
    label = "Root_Ext-1CNSSi-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8.66667e+08,'s^-1'), n=1.2, w0=(742000,'J/mol'), E0=(65231.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R",
    kinetics = ArrheniusBM(A=(5.55958e+15,'s^-1'), n=-0.930058, w0=(742000,'J/mol'), E0=(95488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03313060788275115, var=10.514583367205883, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R
    Total Standard Deviation in ln(k): 6.583836450865867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R
Total Standard Deviation in ln(k): 6.583836450865867""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R
Total Standard Deviation in ln(k): 6.583836450865867
""",
)

entry(
    index = 11,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R",
    kinetics = ArrheniusBM(A=(1.20623e+13,'s^-1'), n=-0.311148, w0=(742000,'J/mol'), E0=(82698.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0004445930100490458, var=1.4499591376219958, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 2.415103756912397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 2.415103756912397""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 2.415103756912397
""",
)

entry(
    index = 12,
    label = "Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R",
    kinetics = ArrheniusBM(A=(7.48e+09,'s^-1'), n=1.08, w0=(742000,'J/mol'), E0=(75024.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.44372e+07,'s^-1'), n=1.42743, w0=(742000,'J/mol'), E0=(63759.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.363975764614281e-14, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R
    Total Standard Deviation in ln(k): 8.452200413603722e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 8.452200413603722e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 8.452200413603722e-14
""",
)

entry(
    index = 14,
    label = "Root_Ext-1CNSSi-R_6R!H->C_2CNOSSi->C",
    kinetics = ArrheniusBM(A=(9.79e+08,'s^-1'), n=1.17, w0=(742000,'J/mol'), E0=(75937.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_6R!H->C_2CNOSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_2CNOSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_2CNOSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_2CNOSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-1CNSSi-R_6R!H->C_N-2CNOSSi->C",
    kinetics = ArrheniusBM(A=(6.813e+10,'s^-1'), n=0.493, w0=(858500,'J/mol'), E0=(93961.7,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_6R!H->C_N-2CNOSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_N-2CNOSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_N-2CNOSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_N-2CNOSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R",
    kinetics = ArrheniusBM(A=(1.16502e+18,'s^-1'), n=-1.58493, w0=(742000,'J/mol'), E0=(96286.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0009693176236643967, var=24.317398395642037, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 9.888320250010615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 9.888320250010615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 9.888320250010615
""",
)

entry(
    index = 17,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R_Ext-1CNSSi-R",
    kinetics = ArrheniusBM(A=(8.11e+14,'s^-1'), n=-0.78, w0=(742000,'J/mol'), E0=(87608,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R_Ext-1CNSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R_Ext-1CNSSi-R",
    kinetics = ArrheniusBM(A=(3.1e+19,'s^-1'), n=-1.78, w0=(742000,'J/mol'), E0=(98348.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R_Ext-1CNSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

