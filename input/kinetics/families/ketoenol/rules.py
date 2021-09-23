#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.000244134,'s^-1'), n=4.98481, w0=(783263,'J/mol'), E0=(116784,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.036954718624156536, var=4.143630220325711, Tref=1000.0, N=19, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 19 training reactions at node Root
    Total Standard Deviation in ln(k): 4.173671487051275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 4.173671487051275""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 4.173671487051275
""",
)

entry(
    index = 2,
    label = "Root_4R->C",
    kinetics = ArrheniusBM(A=(7.88579e+21,'s^-1'), n=-1.81416, w0=(703750,'J/mol'), E0=(216779,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-29.470976721039033, var=1852.2904403864713, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C
    Total Standard Deviation in ln(k): 160.32795747506685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 160.32795747506685""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 160.32795747506685
""",
)

entry(
    index = 3,
    label = "Root_N-4R->C",
    kinetics = ArrheniusBM(A=(1.62985e-08,'s^-1'), n=6.15131, w0=(792618,'J/mol'), E0=(104854,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03619485067575475, var=3.8346489698107864, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-4R->C
    Total Standard Deviation in ln(k): 4.016666137746275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 4.016666137746275""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 4.016666137746275
""",
)

entry(
    index = 4,
    label = "Root_4R->C_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.23584e+11,'s^-1'), n=1.27308, w0=(707000,'J/mol'), E0=(183610,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_4R->C_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700500,'J/mol'), E0=(384026,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-4R->C_3R!H->C",
    kinetics = ArrheniusBM(A=(635.413,'s^-1'), n=2.83859, w0=(783500,'J/mol'), E0=(219488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012207818220425905, var=12.527101437509526, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_3R!H->C
    Total Standard Deviation in ln(k): 7.098555561663242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_3R!H->C
Total Standard Deviation in ln(k): 7.098555561663242""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_3R!H->C
Total Standard Deviation in ln(k): 7.098555561663242
""",
)

entry(
    index = 7,
    label = "Root_N-4R->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(1.36227e-08,'s^-1'), n=6.17457, w0=(794571,'J/mol'), E0=(104564,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.036663879476713866, var=3.6167730030024967, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->C_N-3R!H->C
    Total Standard Deviation in ln(k): 3.9046884509108764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->C_N-3R!H->C
Total Standard Deviation in ln(k): 3.9046884509108764""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->C_N-3R!H->C
Total Standard Deviation in ln(k): 3.9046884509108764
""",
)

entry(
    index = 8,
    label = "Root_N-4R->C_3R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(205000,'s^-1'), n=2.37, w0=(783500,'J/mol'), E0=(221387,'J/mol'), Tmin=(600,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_3R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_3R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_3R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_3R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-4R->C_N-3R!H->C_3NS->S",
    kinetics = ArrheniusBM(A=(2628.85,'s^-1'), n=2.78353, w0=(782000,'J/mol'), E0=(89057.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004857179637508415, var=0.25064116944332687, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_3NS->S',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-3R!H->C_3NS->S
    Total Standard Deviation in ln(k): 1.0158560594211685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-3R!H->C_3NS->S
Total Standard Deviation in ln(k): 1.0158560594211685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-3R!H->C_3NS->S
Total Standard Deviation in ln(k): 1.0158560594211685
""",
)

entry(
    index = 10,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S",
    kinetics = ArrheniusBM(A=(4.71117e-08,'s^-1'), n=6.01657, w0=(798000,'J/mol'), E0=(106563,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.042885526969415354, var=3.2069381670551236, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S
    Total Standard Deviation in ln(k): 3.697817339145407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S
Total Standard Deviation in ln(k): 3.697817339145407""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S
Total Standard Deviation in ln(k): 3.697817339145407
""",
)

entry(
    index = 11,
    label = "Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4909.53,'s^-1'), n=2.71698, w0=(782000,'J/mol'), E0=(88826.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1408662726283667e-06, var=3.5438674360202764e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.003776812860711284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284
""",
)

entry(
    index = 12,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R",
    kinetics = ArrheniusBM(A=(2.92444,'s^-1'), n=3.72909, w0=(798000,'J/mol'), E0=(116830,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06573990524748347, var=12.669811692818818, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R
    Total Standard Deviation in ln(k): 7.300965786524997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R
Total Standard Deviation in ln(k): 7.300965786524997""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R
Total Standard Deviation in ln(k): 7.300965786524997
""",
)

entry(
    index = 13,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(7.72033e-12,'s^-1'), n=7.13865, w0=(798000,'J/mol'), E0=(101332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000940629431949834, var=0.10603351980903279, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 0.6551610347530803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 0.6551610347530803""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 0.6551610347530803
""",
)

entry(
    index = 14,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(8.46062e-15,'s^-1'), n=7.98481, w0=(798000,'J/mol'), E0=(96853.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0026338346337519743, var=0.43967595157844896, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 1.3359187179535994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.3359187179535994""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.3359187179535994
""",
)

entry(
    index = 15,
    label = "Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(87.5,'s^-1'), n=3.23, w0=(782000,'J/mol'), E0=(84839.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.00067e+12,'s^-1'), n=0.391729, w0=(798000,'J/mol'), E0=(133048,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.20077e-11,'s^-1'), n=7.05311, w0=(798000,'J/mol'), E0=(100604,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(7.35011e-13,'s^-1'), n=7.36802, w0=(798000,'J/mol'), E0=(90879,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(1.29627e-12,'s^-1'), n=7.28519, w0=(798000,'J/mol'), E0=(101095,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R",
    kinetics = ArrheniusBM(A=(2.19963e-11,'s^-1'), n=6.98648, w0=(798000,'J/mol'), E0=(100797,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0060992050567732995, var=0.1675474541205485, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R
    Total Standard Deviation in ln(k): 0.8359140421055807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140421055807""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140421055807
""",
)

entry(
    index = 21,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5BrCClFIOPSSi-R_Ext-5BrCClFIOPSSi-R",
    kinetics = ArrheniusBM(A=(2.24517e-15,'s^-1'), n=8.2595, w0=(798000,'J/mol'), E0=(97485.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5BrCClFIOPSSi-R_Ext-5BrCClFIOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5BrCClFIOPSSi-R_Ext-5BrCClFIOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5BrCClFIOPSSi-R_Ext-5BrCClFIOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5BrCClFIOPSSi-R_Ext-5BrCClFIOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(3.21561e-15,'s^-1'), n=8.08717, w0=(798000,'J/mol'), E0=(97688.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(7.48602e-15,'s^-1'), n=8.00071, w0=(798000,'J/mol'), E0=(97935.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_7R!H->N",
    kinetics = ArrheniusBM(A=(9.61654e-11,'s^-1'), n=6.78703, w0=(798000,'J/mol'), E0=(99834.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.1358e-11,'s^-1'), n=7.08342, w0=(798000,'J/mol'), E0=(101820,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.774397504038806e-05, var=0.31280538790524537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
    Total Standard Deviation in ln(k): 1.1213232657408565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565
""",
)

entry(
    index = 26,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing",
    kinetics = ArrheniusBM(A=(4.38421e-12,'s^-1'), n=7.22006, w0=(798000,'J/mol'), E0=(103463,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing",
    kinetics = ArrheniusBM(A=(7.07407e-11,'s^-1'), n=6.82872, w0=(798000,'J/mol'), E0=(100753,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

