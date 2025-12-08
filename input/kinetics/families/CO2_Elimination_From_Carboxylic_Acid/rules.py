#!/usr/bin/env python
# encoding: utf-8

name = "CO2_Elimination_From_Carboxylic_Acid/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.21543e-09,'s^-1'), n=6.12087, w0=(828.5,'kJ/mol'), E0=(142.337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5280870885088149, var=4.9707485512487875, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 5.796444039780933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 5.796444039780933""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 5.796444039780933
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R-R",
    kinetics = ArrheniusBM(A=(5.75969e-08,'s^-1'), n=5.71782, w0=(828.5,'kJ/mol'), E0=(148.226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.562906563550766, var=5.47111143486807, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R-R
    Total Standard Deviation in ln(k): 6.1034950546628375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 6.1034950546628375""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 6.1034950546628375
""",
)

entry(
    index = 3,
    label = "Root_Ext-2R-R_7R!H->F",
    kinetics = Arrhenius(A=(5.85e-12,'s^-1'), n=6.85, Ea=(136.108,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(3.75264e-07,'s^-1'), n=5.487, w0=(828.5,'kJ/mol'), E0=(147.869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5593759368961116, var=6.161437892034857, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
    Total Standard Deviation in ln(k): 6.3816694705011825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 6.3816694705011825""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 6.3816694705011825
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.20314e-06,'s^-1'), n=5.26553, w0=(828.5,'kJ/mol'), E0=(145.106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5390264142193653, var=12.72949826126348, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 8.506916216602685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 8.506916216602685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 8.506916216602685
""",
)

entry(
    index = 6,
    label = "Root_Ext-2R-R_N-7R!H->F_6F1sH->H",
    kinetics = Arrhenius(A=(181000,'s^-1'), n=2.09, Ea=(178.625,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H",
    kinetics = Arrhenius(A=(2.54e-21,'s^-1'), n=9.6, Ea=(116.332,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(0.00202532,'s^-1'), n=4.39922, w0=(828.5,'kJ/mol'), E0=(157.642,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5914123253367646, var=33.04804209529682, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 13.010666664655025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 13.010666664655025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 13.010666664655025
""",
)

entry(
    index = 9,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = Arrhenius(A=(1.15e-12,'s^-1'), n=7.1, Ea=(136.768,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H",
    kinetics = Arrhenius(A=(1.36e+06,'s^-1'), n=1.81, Ea=(183.507,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H",
    kinetics = Arrhenius(A=(2.1e-13,'s^-1'), n=7.32, Ea=(137.634,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClILiNOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

