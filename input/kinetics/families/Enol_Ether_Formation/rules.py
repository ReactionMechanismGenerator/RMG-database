#!/usr/bin/env python
# encoding: utf-8

name = "Enol_Ether_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.81953e+23,'s^-1'), n=-3.14815, w0=(583.4,'kJ/mol'), E0=(317.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20776677842673713, var=9.57108555622445, Tref=1000.0, N=5, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 5 training reactions at node Root
    Total Standard Deviation in ln(k): 6.724110291269355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 6.724110291269355""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 6.724110291269355
""",
)

entry(
    index = 2,
    label = "Root_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.0255e+08,'s^-1'), n=1.21898, w0=(613,'kJ/mol'), E0=(287.174,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06260593053595537, var=0.335144645893498, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3C-R
    Total Standard Deviation in ln(k): 1.3178761221435273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3C-R
Total Standard Deviation in ln(k): 1.3178761221435273""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3C-R
Total Standard Deviation in ln(k): 1.3178761221435273
""",
)

entry(
    index = 3,
    label = "Root_Ext-5C-R",
    kinetics = Arrhenius(A=(80.6667,'s^-1'), n=3.11, Ea=(83.6298,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-3C-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.15964e+08,'s^-1'), n=1.22, w0=(613,'kJ/mol'), E0=(290.301,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07674969062986392, var=0.14845252409017645, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 0.9652535671291035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 0.9652535671291035""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 0.9652535671291035
""",
)

entry(
    index = 5,
    label = "Root_Ext-3C-R_Ext-5C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.30333e+09,'s^-1'), n=0.87, Ea=(171.828,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(1.05333e+07,'s^-1'), n=1.56, Ea=(167.516,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.27667e+09,'s^-1'), n=0.88, Ea=(170.612,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

