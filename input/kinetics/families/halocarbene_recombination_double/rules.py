#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_recombination_double/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(55496.1,'m^3/(mol*s)'), n=0.377638, w0=(346,'kJ/mol'), E0=(98.8329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09654856679389753, var=4.929253079992656, Tref=1000.0, N=6, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 6 training reactions at node Root
    Total Standard Deviation in ln(k): 4.693481373868086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 4.693481373868086""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 4.693481373868086
""",
)

entry(
    index = 2,
    label = "Root_Ext-1C2s-R",
    kinetics = ArrheniusBM(A=(54986.4,'m^3/(mol*s)'), n=0.37885, w0=(346,'kJ/mol'), E0=(98.8213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2160180026565828, var=0.40485028422884983, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1C2s-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1C2s-R
    Total Standard Deviation in ln(k): 4.330891371240339"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1C2s-R
Total Standard Deviation in ln(k): 4.330891371240339""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1C2s-R
Total Standard Deviation in ln(k): 4.330891371240339
""",
)

entry(
    index = 3,
    label = "Root_Ext-3C2s-R",
    kinetics = ArrheniusBM(A=(1.05385e+15,'m^3/(mol*s)'), n=-2.76308, w0=(346,'kJ/mol'), E0=(121.532,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4241096728691853, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3C2s-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3C2s-R
    Total Standard Deviation in ln(k): 5.5433228923216555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3C2s-R
Total Standard Deviation in ln(k): 5.5433228923216555""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3C2s-R
Total Standard Deviation in ln(k): 5.5433228923216555
""",
)

entry(
    index = 4,
    label = "Root_Ext-1C2s-R_Ext-3C2s-R",
    kinetics = ArrheniusBM(A=(54828.3,'m^3/(mol*s)'), n=0.379233, w0=(346,'kJ/mol'), E0=(98.8181,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.842106149217994, var=2.967550755887112, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1C2s-R_Ext-3C2s-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1C2s-R_Ext-3C2s-R
    Total Standard Deviation in ln(k): 18.13213168478597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1C2s-R_Ext-3C2s-R
Total Standard Deviation in ln(k): 18.13213168478597""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1C2s-R_Ext-3C2s-R
Total Standard Deviation in ln(k): 18.13213168478597
""",
)

entry(
    index = 5,
    label = "Root_Ext-1C2s-R_Ext-3C2s-R_4R!H->Cl",
    kinetics = Arrhenius(A=(325000,'m^3/(mol*s)'), n=0.7, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C2s-R_Ext-3C2s-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C2s-R_Ext-3C2s-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C2s-R_Ext-3C2s-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C2s-R_Ext-3C2s-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-1C2s-R_Ext-3C2s-R_N-4R!H->Cl",
    kinetics = Arrhenius(A=(22600,'m^3/(mol*s)'), n=1.53, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1C2s-R_Ext-3C2s-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1C2s-R_Ext-3C2s-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1C2s-R_Ext-3C2s-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1C2s-R_Ext-3C2s-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

