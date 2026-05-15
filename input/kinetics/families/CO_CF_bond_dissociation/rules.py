#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.7692e+11,'s^-1'), n=0.324855, w0=(858983,'J/mol'), E0=(231198,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6777577784961174, var=182.80081293568, Tref=1000.0, N=29, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 29 training reactions at node Root
    Total Standard Deviation in ln(k): 28.807699237569707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root
Total Standard Deviation in ln(k): 28.807699237569707""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root
Total Standard Deviation in ln(k): 28.807699237569707
""",
)

entry(
    index = 2,
    label = "Root_3C-u0",
    kinetics = ArrheniusBM(A=(2.47818e+09,'s^-1'), n=0.861381, w0=(854900,'J/mol'), E0=(277308,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6692595139791464, var=77.76872148230618, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_3C-u0',), comment="""BM rule fitted to 20 training reactions at node Root_3C-u0
    Total Standard Deviation in ln(k): 19.36062875041854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 19.36062875041854""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 19.36062875041854
""",
)

entry(
    index = 3,
    label = "Root_N-3C-u0",
    kinetics = ArrheniusBM(A=(1.23143e+21,'s^-1'), n=-2.50667, w0=(868056,'J/mol'), E0=(148173,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8624436223105892, var=182.81038519661487, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3C-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-3C-u0
    Total Standard Deviation in ln(k): 29.27244367522054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 29.27244367522054""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 29.27244367522054
""",
)

entry(
    index = 4,
    label = "Root_3C-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.92372e+10,'s^-1'), n=0.470936, w0=(854900,'J/mol'), E0=(298295,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7184201157198755, var=91.48851188125899, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R',), comment="""BM rule fitted to 15 training reactions at node Root_3C-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 20.980291951237902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3C-u0_Ext-3C-R
Total Standard Deviation in ln(k): 20.980291951237902""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3C-u0_Ext-3C-R
Total Standard Deviation in ln(k): 20.980291951237902
""",
)

entry(
    index = 5,
    label = "Root_3C-u0_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.06172e+06,'s^-1'), n=1.81129, w0=(810500,'J/mol'), E0=(200604,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2914832305231129, var=0.8524145049606787, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_4F1sH->H
    Total Standard Deviation in ln(k): 2.583267580159321"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_4F1sH->H
Total Standard Deviation in ln(k): 2.583267580159321""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_4F1sH->H
Total Standard Deviation in ln(k): 2.583267580159321
""",
)

entry(
    index = 6,
    label = "Root_3C-u0_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.26102e+08,'s^-1'), n=1.05774, w0=(884500,'J/mol'), E0=(239223,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7634447603801581, var=1.8615255450780699, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.653418041913274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_N-4F1sH->H
Total Standard Deviation in ln(k): 4.653418041913274""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_N-4F1sH->H
Total Standard Deviation in ln(k): 4.653418041913274
""",
)

entry(
    index = 7,
    label = "Root_N-3C-u0_5R->O",
    kinetics = ArrheniusBM(A=(1442.74,'s^-1'), n=2.34038, w0=(884500,'J/mol'), E0=(262358,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3091352839065565, var=0.07250119342877144, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_5R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
    Total Standard Deviation in ln(k): 1.3165177009397473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
Total Standard Deviation in ln(k): 1.3165177009397473""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
Total Standard Deviation in ln(k): 1.3165177009397473
""",
)

entry(
    index = 8,
    label = "Root_N-3C-u0_N-5R->O",
    kinetics = ArrheniusBM(A=(9.58631e+15,'s^-1'), n=-0.959937, w0=(863357,'J/mol'), E0=(88914.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7742604615997749, var=5.222373300839574, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
    Total Standard Deviation in ln(k): 6.5267013968133805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
Total Standard Deviation in ln(k): 6.5267013968133805""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
Total Standard Deviation in ln(k): 6.5267013968133805
""",
)

entry(
    index = 9,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.88378e+08,'s^-1'), n=1.25681, w0=(854900,'J/mol'), E0=(341318,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7542736892274401, var=20.61472203885867, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 10.997346550305378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.997346550305378""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.997346550305378
""",
)

entry(
    index = 10,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.712078,'s^-1'), n=3.52746, w0=(854900,'J/mol'), E0=(181257,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2527575518203657, var=31.37635153084892, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.864512106901413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.864512106901413""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.864512106901413
""",
)

entry(
    index = 11,
    label = "Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(560000,'s^-1'), n=1.87, Ea=(187.16,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.24508e+08,'s^-1'), n=0.995515, w0=(884500,'J/mol'), E0=(242338,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8599959327159629, var=0.4886018210428632, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
    Total Standard Deviation in ln(k): 3.5621047972691544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
Total Standard Deviation in ln(k): 3.5621047972691544""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
Total Standard Deviation in ln(k): 3.5621047972691544
""",
)

entry(
    index = 13,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C",
    kinetics = Arrhenius(A=(8.1e+07,'s^-1'), n=1.22, Ea=(203.77,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C",
    kinetics = Arrhenius(A=(5066.67,'s^-1'), n=2.17, Ea=(279.293,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = Arrhenius(A=(413.333,'s^-1'), n=2.51, Ea=(275.492,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R",
    kinetics = ArrheniusBM(A=(8.0753e+17,'s^-1'), n=-1.61059, w0=(869700,'J/mol'), E0=(87219.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8571501529406776, var=9.315323403483951, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
    Total Standard Deviation in ln(k): 8.27229848369812"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
Total Standard Deviation in ln(k): 8.27229848369812""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
Total Standard Deviation in ln(k): 8.27229848369812
""",
)

entry(
    index = 17,
    label = "Root_N-3C-u0_N-5R->O_4F1sH->H",
    kinetics = Arrhenius(A=(2.78e+10,'s^-1'), n=0.74, Ea=(93.971,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3C-u0_N-5R->O_N-4F1sH->H",
    kinetics = Arrhenius(A=(5.95e+09,'s^-1'), n=1.2, Ea=(114.447,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_N-4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(5.33529e+06,'s^-1'), n=1.68731, w0=(810500,'J/mol'), E0=(371458,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6733351941705963, var=2.373086586630239, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H',), comment="""BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 4.78005643929893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 4.78005643929893""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 4.78005643929893
""",
)

entry(
    index = 20,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.51262e+09,'s^-1'), n=0.944838, w0=(884500,'J/mol'), E0=(316948,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8162107718604638, var=1.158683241102774, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.20872076868567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.20872076868567""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.20872076868567
""",
)

entry(
    index = 21,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.26773e+06,'s^-1'), n=1.81827, w0=(810500,'J/mol'), E0=(243824,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3011800064263426, var=0.07060990627683403, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 1.2894424057733238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.2894424057733238""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.2894424057733238
""",
)

entry(
    index = 22,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(3.00447e+11,'s^-1'), n=0.142229, w0=(884500,'J/mol'), E0=(179410,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6192537485214316, var=0.4264811837744896, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 2.8651167453379944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 2.8651167453379944""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 2.8651167453379944
""",
)

entry(
    index = 23,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = Arrhenius(A=(1.63e+08,'s^-1'), n=1.07, Ea=(213.91,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(7.65e+08,'s^-1'), n=0.9, Ea=(218.355,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.52814e+20,'s^-1'), n=-2.29136, w0=(866000,'J/mol'), E0=(94145,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9018499239610573, var=13.34948207081968, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
    Total Standard Deviation in ln(k): 9.59064371714607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
Total Standard Deviation in ln(k): 9.59064371714607""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
Total Standard Deviation in ln(k): 9.59064371714607
""",
)

entry(
    index = 26,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O",
    kinetics = Arrhenius(A=(2.59e+10,'s^-1'), n=0.65, Ea=(93.4178,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C",
    kinetics = ArrheniusBM(A=(2.39758e+07,'s^-1'), n=1.55051, w0=(810500,'J/mol'), E0=(376423,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4330065775066352, var=15.076349500593945, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
    Total Standard Deviation in ln(k): 8.87199674093404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 8.87199674093404""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 8.87199674093404
""",
)

entry(
    index = 28,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C",
    kinetics = ArrheniusBM(A=(1.09359e+06,'s^-1'), n=1.83434, w0=(810500,'J/mol'), E0=(366392,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9059763464226868, var=0.15395528289839813, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
    Total Standard Deviation in ln(k): 3.062923104012883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.062923104012883""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.062923104012883
""",
)

entry(
    index = 29,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.78616e+10,'s^-1'), n=0.778363, w0=(884500,'J/mol'), E0=(324643,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.757449698666084, var=5.235323067579039, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
    Total Standard Deviation in ln(k): 6.490139869103488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.490139869103488""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.490139869103488
""",
)

entry(
    index = 30,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.40039e+08,'s^-1'), n=1.04554, w0=(884500,'J/mol'), E0=(303503,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0007821082272592, var=0.21194032785901493, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.437447342551842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.437447342551842""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.437447342551842
""",
)

entry(
    index = 31,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(5.66667e+08,'s^-1'), n=1.16, Ea=(347.838,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R",
    kinetics = Arrhenius(A=(1.865e+06,'s^-1'), n=1.71, Ea=(300.769,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.65774e+11,'s^-1'), n=0.00218836, w0=(884500,'J/mol'), E0=(177973,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6972849589862858, var=1.4477353565343012, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
    Total Standard Deviation in ln(k): 4.1641070894827825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 4.1641070894827825""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 4.1641070894827825
""",
)

entry(
    index = 34,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C",
    kinetics = Arrhenius(A=(6.23333e+10,'s^-1'), n=0.42, Ea=(209.094,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.37949e+12,'s^-1'), n=-0.260918, w0=(884500,'J/mol'), E0=(58357.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6856115219003344, var=11.027371376508752, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 8.379863250291843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.379863250291843""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.379863250291843
""",
)

entry(
    index = 36,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R",
    kinetics = Arrhenius(A=(1.66e+07,'s^-1'), n=1.5, Ea=(382.799,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R",
    kinetics = Arrhenius(A=(3.895e+06,'s^-1'), n=1.63, Ea=(392.778,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(5.8714e+09,'s^-1'), n=0.800009, w0=(884500,'J/mol'), E0=(319231,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47358980818755825, var=0.32894092038645495, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.339707294461017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.339707294461017""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.339707294461017
""",
)

entry(
    index = 39,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.19667e+11,'s^-1'), n=0.77, Ea=(346.77,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(4.77e+08,'s^-1'), n=1.06, Ea=(337.901,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(2.65e+08,'s^-1'), n=1.02, Ea=(339.685,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(2.235e+11,'s^-1'), n=0.12, Ea=(209.772,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.08e+12,'s^-1'), n=-0.04, Ea=(213.084,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.27763e+13,'s^-1'), n=-0.461038, w0=(884500,'J/mol'), E0=(42156.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20493121391191868, var=2.5877165065631265, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.7397957545966576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 3.7397957545966576""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 3.7397957545966576
""",
)

entry(
    index = 45,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(3.4e+06,'s^-1'), n=1.62, Ea=(129.638,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(5.9e+09,'s^-1'), n=0.8, Ea=(332.105,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(2.49e+09,'s^-1'), n=0.79, Ea=(333.774,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(4.5e+06,'s^-1'), n=1.39, Ea=(90.007,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(9.25e+06,'s^-1'), n=1.44, Ea=(99.829,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

