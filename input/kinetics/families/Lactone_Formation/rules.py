#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(3.78157e+09,'s^-1'), n=0.978824, Ea=(255.875,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.4610903130376875e-15, var=85.39031335855428, Tref=1000.0, N=17, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 17 training reactions at node Root
    Total Standard Deviation in ln(k): 18.525131225896597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 18.525131225896597""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 18.525131225896597
""",
)

entry(
    index = 2,
    label = "Root_6F1sH->F1s",
    kinetics = ArrheniusBM(A=(3.19447e+10,'s^-1'), n=0.729192, w0=(933.5,'kJ/mol'), E0=(133.278,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18089836747434998, var=2.583136162827217, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_6F1sH->F1s',), comment="""BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
    Total Standard Deviation in ln(k): 3.6765563704700606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 3.6765563704700606""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 3.6765563704700606
""",
)

entry(
    index = 3,
    label = "Root_N-6F1sH->F1s",
    kinetics = ArrheniusBM(A=(9.11633e-43,'s^-1'), n=15.7299, w0=(830,'kJ/mol'), E0=(46.8731,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.373487029093847, var=34.8195822928352, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-6F1sH->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
    Total Standard Deviation in ln(k): 17.793100056176883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 17.793100056176883""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 17.793100056176883
""",
)

entry(
    index = 4,
    label = "Root_6F1sH->F1s_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.26334e+10,'s^-1'), n=0.731979, w0=(933.5,'kJ/mol'), E0=(133.947,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1738555019597208, var=2.8752533314533553, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 3.836166332321318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 3.836166332321318""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 3.836166332321318
""",
)

entry(
    index = 5,
    label = "Root_N-6F1sH->F1s_Ext-3C-R",
    kinetics = Arrhenius(A=(627251,'s^-1'), n=1.995, Ea=(319.29,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-8.997534477772192e-16, var=89.06593733433054, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 18.9196374887785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 18.9196374887785""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 18.9196374887785
""",
)

entry(
    index = 6,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(2.22707e+12,'s^-1'), n=0.153066, w0=(933.5,'kJ/mol'), E0=(140.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4047518703461982, var=2.2233442097440057, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
    Total Standard Deviation in ln(k): 4.006201443818575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 4.006201443818575""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 4.006201443818575
""",
)

entry(
    index = 7,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(1.11356e+15,'s^-1'), n=-0.473309, w0=(933.5,'kJ/mol'), E0=(143.014,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.026145864106236913, var=2.5487812565902543, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 3.2662332175860045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 3.2662332175860045""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 3.2662332175860045
""",
)

entry(
    index = 8,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.28596e+06,'s^-1'), n=1.585, w0=(830,'kJ/mol'), E0=(156.166,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1702874213823726, var=0.05114146896546384, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.393781062771061"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.393781062771061""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.393781062771061
""",
)

entry(
    index = 9,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R",
    kinetics = Arrhenius(A=(26400,'s^-1'), n=2.44, Ea=(368.245,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.92781e+11,'s^-1'), n=0.414684, w0=(933.5,'kJ/mol'), E0=(141.825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4416677098170093, var=0.945624191220723, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
    Total Standard Deviation in ln(k): 3.05918660729115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 3.05918660729115""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 3.05918660729115
""",
)

entry(
    index = 11,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(3.19e+11,'s^-1'), n=0.34, Ea=(222,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.90025e+13,'s^-1'), n=-0.107419, w0=(933.5,'kJ/mol'), E0=(148.799,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17323918181247056, var=0.7188208308340039, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 2.134954922348717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.134954922348717""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.134954922348717
""",
)

entry(
    index = 13,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = Arrhenius(A=(1.17e+07,'s^-1'), n=1.55, Ea=(266.433,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.94791e+11,'s^-1'), n=0.477127, w0=(933.5,'kJ/mol'), E0=(139.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48744136389809734, var=0.8574590445660951, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 3.0810933727919565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 3.0810933727919565""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 3.0810933727919565
""",
)

entry(
    index = 15,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(4.465e+10,'s^-1'), n=0.59, Ea=(237.41,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C",
    kinetics = ArrheniusBM(A=(2.18952e+15,'s^-1'), n=-0.526957, w0=(933.5,'kJ/mol'), E0=(154.356,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20427857195930532, var=0.04561943053093455, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
    Total Standard Deviation in ln(k): 0.9414482070454904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 0.9414482070454904""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 0.9414482070454904
""",
)

entry(
    index = 17,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C",
    kinetics = Arrhenius(A=(1.8e+12,'s^-1'), n=0.42, Ea=(202.372,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(7.67813e+10,'s^-1'), n=0.61187, w0=(933.5,'kJ/mol'), E0=(136.938,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5640920685289639, var=0.46888698665279877, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 2.7900655756001087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 2.7900655756001087""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 2.7900655756001087
""",
)

entry(
    index = 19,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = Arrhenius(A=(5.3e+09,'s^-1'), n=0.85, Ea=(233.214,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = Arrhenius(A=(7.78e+15,'s^-1'), n=-0.84, Ea=(208.506,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = Arrhenius(A=(5.51e+14,'s^-1'), n=-0.2, Ea=(235.136,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(3.77793e+11,'s^-1'), n=0.398137, w0=(933.5,'kJ/mol'), E0=(135.689,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6695154883295846, var=0.5131215581937485, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 3.1182416472958927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 3.1182416472958927""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 3.1182416472958927
""",
)

entry(
    index = 23,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = Arrhenius(A=(3.66e+07,'s^-1'), n=1.61, Ea=(231.308,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C",
    kinetics = ArrheniusBM(A=(1.4948e+11,'s^-1'), n=0.513313, w0=(933.5,'kJ/mol'), E0=(131.681,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8508919403261448, var=0.9936358957726975, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
    Total Standard Deviation in ln(k): 4.136265172106335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
Total Standard Deviation in ln(k): 4.136265172106335""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
Total Standard Deviation in ln(k): 4.136265172106335
""",
)

entry(
    index = 25,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C",
    kinetics = Arrhenius(A=(3.35e+10,'s^-1'), n=0.7, Ea=(232.005,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C",
    kinetics = Arrhenius(A=(1.59e+10,'s^-1'), n=0.8, Ea=(233.056,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C",
    kinetics = Arrhenius(A=(1.045e+11,'s^-1'), n=0.55, Ea=(232.571,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

