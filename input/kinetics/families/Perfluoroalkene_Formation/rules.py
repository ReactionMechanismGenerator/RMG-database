#!/usr/bin/env python
# encoding: utf-8

name = "Perfluoroalkene_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.41151,'s^-1'), n=3.62449, w0=(749000,'J/mol'), E0=(309003,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4240079800651651, var=138.50012568630504, Tref=1000.0, N=6, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 6 training reactions at node Root
    Total Standard Deviation in ln(k): 24.658287223233753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 24.658287223233753""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 24.658287223233753
""",
)

entry(
    index = 2,
    label = "Root_5R->O",
    kinetics = ArrheniusBM(A=(5.56366e+07,'s^-1'), n=1.15082, w0=(749000,'J/mol'), E0=(261346,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4484928866972968, var=16.456785477863004, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5R->O',), comment="""BM rule fitted to 4 training reactions at node Root_5R->O
    Total Standard Deviation in ln(k): 9.259468070525168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5R->O
Total Standard Deviation in ln(k): 9.259468070525168""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5R->O
Total Standard Deviation in ln(k): 9.259468070525168
""",
)

entry(
    index = 3,
    label = "Root_N-5R->O",
    kinetics = ArrheniusBM(A=(7.80392e-17,'s^-1'), n=8.87726, w0=(749000,'J/mol'), E0=(401157,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34334158844297824, var=62.26264735557078, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->O
    Total Standard Deviation in ln(k): 16.681366976912084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->O
Total Standard Deviation in ln(k): 16.681366976912084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->O
Total Standard Deviation in ln(k): 16.681366976912084
""",
)

entry(
    index = 4,
    label = "Root_5R->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.24388e+11,'s^-1'), n=0.12185, w0=(786000,'J/mol'), E0=(284263,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5717287601531954, var=61.314256936671654, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5R->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_5R->O_Ext-2C-R
    Total Standard Deviation in ln(k): 17.134265838662348"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5R->O_Ext-2C-R
Total Standard Deviation in ln(k): 17.134265838662348""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5R->O_Ext-2C-R
Total Standard Deviation in ln(k): 17.134265838662348
""",
)

entry(
    index = 5,
    label = "Root_5R->O_Ext-3C-R",
    kinetics = Arrhenius(A=(206500,'s^-1'), n=1.73, Ea=(292.703,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_5R->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-5R->O_Ext-1C-R",
    kinetics = Arrhenius(A=(6.33333e+09,'s^-1'), n=1.49, Ea=(574.237,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C",
    kinetics = Arrhenius(A=(1.23e+06,'s^-1'), n=1.56, Ea=(338.205,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(6.23333e+07,'s^-1'), n=1.21, Ea=(343.422,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

