#!/usr/bin/env python
# encoding: utf-8

name = "PFAS_Hydrolysis/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.5902e-14,'m^3/(mol*s)'), n=5.2654, w0=(903.929,'kJ/mol'), E0=(235.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4675676974820811, var=137.2966267481057, Tref=1000.0, N=21, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 21 training reactions at node Root
    Total Standard Deviation in ln(k): 24.66500448868329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 24.66500448868329""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 24.66500448868329
""",
)

entry(
    index = 2,
    label = "Root_3F1sH->F1s",
    kinetics = ArrheniusBM(A=(2.6452e-06,'m^3/(mol*s)'), n=3.08631, w0=(933.5,'kJ/mol'), E0=(217.572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23273174372951383, var=101.58475236825463, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3F1sH->F1s',), comment="""BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
    Total Standard Deviation in ln(k): 20.790329923411573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 20.790329923411573""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 20.790329923411573
""",
)

entry(
    index = 3,
    label = "Root_N-3F1sH->F1s",
    kinetics = ArrheniusBM(A=(6.60079e-18,'m^3/(mol*s)'), n=6.52811, w0=(830,'kJ/mol'), E0=(316.502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6540807586985928, var=105.52449573640949, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3F1sH->F1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
    Total Standard Deviation in ln(k): 22.23708344277036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 22.23708344277036""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 22.23708344277036
""",
)

entry(
    index = 4,
    label = "Root_3F1sH->F1s_4R->F",
    kinetics = ArrheniusBM(A=(7.71485e-07,'m^3/(mol*s)'), n=3.20931, w0=(933.5,'kJ/mol'), E0=(306.033,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1446442755937482, var=180.17417274195515, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
    Total Standard Deviation in ln(k): 27.272780946600292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
Total Standard Deviation in ln(k): 27.272780946600292""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
Total Standard Deviation in ln(k): 27.272780946600292
""",
)

entry(
    index = 5,
    label = "Root_3F1sH->F1s_N-4R->F",
    kinetics = ArrheniusBM(A=(8.6744e-07,'m^3/(mol*s)'), n=3.23607, w0=(933.5,'kJ/mol'), E0=(183.683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2813344286958862, var=31.685368216658638, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F',), comment="""BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
    Total Standard Deviation in ln(k): 11.991475599318733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 11.991475599318733""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 11.991475599318733
""",
)

entry(
    index = 6,
    label = "Root_N-3F1sH->F1s_4R->H",
    kinetics = ArrheniusBM(A=(3.78472e-15,'m^3/(mol*s)'), n=5.78552, w0=(830,'kJ/mol'), E0=(360.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5459315819807791, var=93.70769150978725, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
    Total Standard Deviation in ln(k): 20.77807087112411"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
Total Standard Deviation in ln(k): 20.77807087112411""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
Total Standard Deviation in ln(k): 20.77807087112411
""",
)

entry(
    index = 7,
    label = "Root_N-3F1sH->F1s_N-4R->H",
    kinetics = ArrheniusBM(A=(6.54043e-13,'m^3/(mol*s)'), n=5.00119, w0=(830,'kJ/mol'), E0=(254.469,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5763211929661782, var=0.790455027100245, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
    Total Standard Deviation in ln(k): 3.230403794381119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 3.230403794381119""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 3.230403794381119
""",
)

entry(
    index = 8,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.05093e-07,'m^3/(mol*s)'), n=3.44969, w0=(933.5,'kJ/mol'), E0=(350.482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11424387202949775, var=0.1768706059348355, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.1301560321351751"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.1301560321351751""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.1301560321351751
""",
)

entry(
    index = 9,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H",
    kinetics = ArrheniusBM(A=(3.68764e-06,'m^3/(mol*s)'), n=3.19922, w0=(933.5,'kJ/mol'), E0=(232.662,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17731766390938972, var=64.43917235273025, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
    Total Standard Deviation in ln(k): 16.538334825136843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 16.538334825136843""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 16.538334825136843
""",
)

entry(
    index = 10,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H",
    kinetics = ArrheniusBM(A=(5.11379e-09,'m^3/(mol*s)'), n=3.793, w0=(933.5,'kJ/mol'), E0=(150.965,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.38701340086156155, var=1.9746354937105428, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H',), comment="""BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
    Total Standard Deviation in ln(k): 3.7894837734489606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 3.7894837734489606""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 3.7894837734489606
""",
)

entry(
    index = 11,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.24258e-16,'m^3/(mol*s)'), n=5.89843, w0=(830,'kJ/mol'), E0=(346.501,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5842609148593002, var=167.6413254901238, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
    Total Standard Deviation in ln(k): 27.42457598435601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
Total Standard Deviation in ln(k): 27.42457598435601""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
Total Standard Deviation in ln(k): 27.42457598435601
""",
)

entry(
    index = 12,
    label = "Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(5.1e-13,'m^3/(mol*s)'), n=5.03, w0=(830,'kJ/mol'), E0=(251.73,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.75863e-08,'m^3/(mol*s)'), n=3.56448, w0=(933.5,'kJ/mol'), E0=(343.352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.129267017016879, var=0.5979954658498282, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 1.8750564742578033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 1.8750564742578033""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 1.8750564742578033
""",
)

entry(
    index = 14,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.1125e-06,'m^3/(mol*s)'), n=3.22, w0=(933.5,'kJ/mol'), E0=(364.742,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.23564e-06,'m^3/(mol*s)'), n=3.12804, w0=(933.5,'kJ/mol'), E0=(219.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19191634919541212, var=109.29373017240566, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 21.440432443304008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
Total Standard Deviation in ln(k): 21.440432443304008""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
Total Standard Deviation in ln(k): 21.440432443304008
""",
)

entry(
    index = 16,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.90021e-09,'m^3/(mol*s)'), n=3.7824, w0=(933.5,'kJ/mol'), E0=(153.541,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4019630205228908, var=0.45562059285080025, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R',), comment="""BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
    Total Standard Deviation in ln(k): 2.3631469706545816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 2.3631469706545816""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 2.3631469706545816
""",
)

entry(
    index = 17,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.62424e-12,'m^3/(mol*s)'), n=4.88194, w0=(854.347,'kJ/mol'), E0=(403.264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43589851152997383, var=5.184484677090115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 5.659896606344731"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 5.659896606344731""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 5.659896606344731
""",
)

entry(
    index = 18,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.6075e-13,'m^3/(mol*s)'), n=5.03, w0=(830,'kJ/mol'), E0=(258.407,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(5.64167e-09,'m^3/(mol*s)'), n=3.77, w0=(933.5,'kJ/mol'), E0=(341.667,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.48333e-07,'m^3/(mol*s)'), n=3.36, w0=(933.5,'kJ/mol'), E0=(345.028,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.48216e-06,'m^3/(mol*s)'), n=3.2847, w0=(933.5,'kJ/mol'), E0=(255.158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1540170364824897, var=1.3921655949535876, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.7523657428913233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.7523657428913233""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.7523657428913233
""",
)

entry(
    index = 22,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(4.305e-07,'m^3/(mol*s)'), n=3.26, w0=(933.5,'kJ/mol'), E0=(144.118,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.25388e-09,'m^3/(mol*s)'), n=3.79529, w0=(933.5,'kJ/mol'), E0=(154.884,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.44354882028231624, var=0.23972887938540297, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.0960049842397117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.0960049842397117""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.0960049842397117
""",
)

entry(
    index = 24,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.565e-08,'m^3/(mol*s)'), n=3.6, w0=(933.5,'kJ/mol'), E0=(147.854,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(1.21667e-12,'m^3/(mol*s)'), n=4.98, w0=(830,'kJ/mol'), E0=(402.608,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.3e-07,'m^3/(mol*s)'), n=3.33, w0=(933.5,'kJ/mol'), E0=(255.119,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.04995e-09,'m^3/(mol*s)'), n=3.79872, w0=(933.5,'kJ/mol'), E0=(155.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4834507409173432, var=0.18290049520314963, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.072062747464364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.072062747464364""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.072062747464364
""",
)

entry(
    index = 28,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(9.2e-09,'m^3/(mol*s)'), n=3.71, w0=(933.5,'kJ/mol'), E0=(151.324,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(4.69692e-09,'m^3/(mol*s)'), n=3.77714, w0=(933.5,'kJ/mol'), E0=(156.106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5480968373932545, var=0.30135929590192356, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 2.4776511434032154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.4776511434032154""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.4776511434032154
""",
)

entry(
    index = 30,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.67e-09,'m^3/(mol*s)'), n=3.86, w0=(933.5,'kJ/mol'), E0=(155.432,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(5.96854e-09,'m^3/(mol*s)'), n=3.751, w0=(933.5,'kJ/mol'), E0=(156.471,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6721723967414251, var=0.6947079085984775, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 3.35980480863903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 3.35980480863903""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 3.35980480863903
""",
)

entry(
    index = 32,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(2.895e-09,'m^3/(mol*s)'), n=3.83, w0=(933.5,'kJ/mol'), E0=(155.372,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(9.05e-09,'m^3/(mol*s)'), n=3.71, w0=(933.5,'kJ/mol'), E0=(155.851,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(4.335e-09,'m^3/(mol*s)'), n=3.78, w0=(933.5,'kJ/mol'), E0=(157.196,'kJ/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

