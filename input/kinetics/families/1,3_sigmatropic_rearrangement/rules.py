#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(44220.4,'s^-1'), n=2.55125, w0=(755204,'J/mol'), E0=(150530,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06871057353442966, var=57.68226706587711, Tref=1000.0, N=27, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 27 training reactions at node Root
    Total Standard Deviation in ln(k): 15.398370535650425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root
Total Standard Deviation in ln(k): 15.398370535650425""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root
Total Standard Deviation in ln(k): 15.398370535650425
""",
)

entry(
    index = 2,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.38702e+72,'s^-1'), n=-16.8799, w0=(670125,'J/mol'), E0=(378098,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0325128508066552, var=397.64301580674777, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 42.570652188583445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 42.570652188583445""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 42.570652188583445
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(0.000146187,'s^-1'), n=4.93211, w0=(770000,'J/mol'), E0=(113160,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.003495637019007975, var=8.168116975953765, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 5.738299366319756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 5.738299366319756""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 5.738299366319756
""",
)

entry(
    index = 4,
    label = "Root_1R!H-inRing_4R->C",
    kinetics = ArrheniusBM(A=(2.13185e+78,'s^-1'), n=-18.7334, w0=(707000,'J/mol'), E0=(425945,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0411052931213147, var=501.438488492061, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_4R->C
    Total Standard Deviation in ln(k): 47.50751869915296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_4R->C
Total Standard Deviation in ln(k): 47.50751869915296""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_4R->C
Total Standard Deviation in ln(k): 47.50751869915296
""",
)

entry(
    index = 5,
    label = "Root_1R!H-inRing_N-4R->C",
    kinetics = ArrheniusBM(A=(4.0435e+11,'s^-1'), n=1.01704, w0=(559500,'J/mol'), E0=(135903,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H-inRing_3R!H->C",
    kinetics = ArrheniusBM(A=(0.0954007,'s^-1'), n=3.97882, w0=(762750,'J/mol'), E0=(250868,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05104117971660031, var=160.05464641490252, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_3R!H->C
    Total Standard Deviation in ln(k): 25.490690006267023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H-inRing_N-3R!H->C",
    kinetics = ArrheniusBM(A=(0.000109409,'s^-1'), n=4.96965, w0=(771526,'J/mol'), E0=(112528,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00255753453896434, var=7.194105339202176, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-3R!H->C
    Total Standard Deviation in ln(k): 5.383492195805062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-3R!H->C
Total Standard Deviation in ln(k): 5.383492195805062""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-3R!H->C
Total Standard Deviation in ln(k): 5.383492195805062
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(707000,'J/mol'), E0=(405481,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.6259e+11,'s^-1'), n=1.19107, w0=(707000,'J/mol'), E0=(249049,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.23584e+11,'s^-1'), n=1.27308, w0=(707000,'J/mol'), E0=(183610,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H-inRing_3R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700500,'J/mol'), E0=(384026,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H-inRing_3R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(635.413,'s^-1'), n=2.83859, w0=(783500,'J/mol'), E0=(219488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012207818220425905, var=12.527101437509526, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C_N-4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C
    Total Standard Deviation in ln(k): 7.098555561663242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H-inRing_N-3R!H->C_3NS->S",
    kinetics = ArrheniusBM(A=(2628.85,'s^-1'), n=2.78353, w0=(782000,'J/mol'), E0=(89057.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004857179637508415, var=0.25064116944332687, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_3NS->S',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S
    Total Standard Deviation in ln(k): 1.0158560594211685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S
Total Standard Deviation in ln(k): 1.0158560594211685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S
Total Standard Deviation in ln(k): 1.0158560594211685
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S",
    kinetics = ArrheniusBM(A=(0.00132983,'s^-1'), n=4.6492, w0=(769562,'J/mol'), E0=(116133,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011878464585718973, var=6.628325949021129, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S
    Total Standard Deviation in ln(k): 5.1911431859520585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S
Total Standard Deviation in ln(k): 5.1911431859520585""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S
Total Standard Deviation in ln(k): 5.1911431859520585
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(205000,'s^-1'), n=2.37, w0=(783500,'J/mol'), E0=(221387,'J/mol'), Tmin=(600,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4909.53,'s^-1'), n=2.71698, w0=(782000,'J/mol'), E0=(88826.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1408662726283667e-06, var=3.5438674360202764e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.003776812860711284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284
""",
)

entry(
    index = 17,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(0.000164309,'s^-1'), n=4.97161, w0=(787889,'J/mol'), E0=(112114,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.051526042577798054, var=4.08971979394378, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 4.183649319777569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.183649319777569""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.183649319777569
""",
)

entry(
    index = 18,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R",
    kinetics = ArrheniusBM(A=(4.74194e-14,'s^-1'), n=7.69802, w0=(798000,'J/mol'), E0=(92033.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012749512289493472, var=0.8377613591004845, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R
    Total Standard Deviation in ln(k): 1.8669540248408663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R
Total Standard Deviation in ln(k): 1.8669540248408663""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R
Total Standard Deviation in ln(k): 1.8669540248408663
""",
)

entry(
    index = 19,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.50087e+11,'s^-1'), n=0.45162, w0=(707000,'J/mol'), E0=(137659,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008012511677798886, var=3.4768369970791304, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O
    Total Standard Deviation in ln(k): 3.7582167842883063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O
Total Standard Deviation in ln(k): 3.7582167842883063""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O
Total Standard Deviation in ln(k): 3.7582167842883063
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.85602e+09,'s^-1'), n=0.739985, w0=(707000,'J/mol'), E0=(193742,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(87.5,'s^-1'), n=3.23, w0=(782000,'J/mol'), E0=(84839.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R",
    kinetics = ArrheniusBM(A=(8.00067e+12,'s^-1'), n=0.391729, w0=(798000,'J/mol'), E0=(133048,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(6.91728e-07,'s^-1'), n=5.62342, w0=(779800,'J/mol'), E0=(106545,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006515153720890275, var=0.8806591803136841, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 1.897682153588295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 1.897682153588295""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 1.897682153588295
""",
)

entry(
    index = 24,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(8.46061e-15,'s^-1'), n=7.98481, w0=(798000,'J/mol'), E0=(96853.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00263383782615601, var=0.4396759609029318, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 1.335918740070374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.335918740070374""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.335918740070374
""",
)

entry(
    index = 25,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.20077e-11,'s^-1'), n=7.05311, w0=(798000,'J/mol'), E0=(100604,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(7.35011e-13,'s^-1'), n=7.36802, w0=(798000,'J/mol'), E0=(90879,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(1.29627e-12,'s^-1'), n=7.28519, w0=(798000,'J/mol'), E0=(101095,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R",
    kinetics = ArrheniusBM(A=(1.88124e+11,'s^-1'), n=0.620515, w0=(707000,'J/mol'), E0=(161496,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C",
    kinetics = ArrheniusBM(A=(1.93892e+11,'s^-1'), n=0.308436, w0=(707000,'J/mol'), E0=(125262,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C",
    kinetics = ArrheniusBM(A=(7.72033e-12,'s^-1'), n=7.13865, w0=(798000,'J/mol'), E0=(101332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0009406278385854534, var=0.10603351746797161, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C
    Total Standard Deviation in ln(k): 0.6551610235432553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C
Total Standard Deviation in ln(k): 0.6551610235432553""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C
Total Standard Deviation in ln(k): 0.6551610235432553
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(2.24517e-15,'s^-1'), n=8.2595, w0=(798000,'J/mol'), E0=(97485.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O",
    kinetics = ArrheniusBM(A=(3.21561e-15,'s^-1'), n=8.08717, w0=(798000,'J/mol'), E0=(97688.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O",
    kinetics = ArrheniusBM(A=(7.48602e-15,'s^-1'), n=8.00071, w0=(798000,'J/mol'), E0=(97935.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R",
    kinetics = ArrheniusBM(A=(2.19963e-11,'s^-1'), n=6.98648, w0=(798000,'J/mol'), E0=(100797,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006099207969903697, var=0.16754745053310063, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
    Total Standard Deviation in ln(k): 0.8359140406399651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140406399651""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140406399651
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N",
    kinetics = ArrheniusBM(A=(9.61654e-11,'s^-1'), n=6.78703, w0=(798000,'J/mol'), E0=(99834.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.1358e-11,'s^-1'), n=7.08342, w0=(798000,'J/mol'), E0=(101820,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.774397504036697e-05, var=0.31280538790524537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
    Total Standard Deviation in ln(k): 1.1213232657408565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565
""",
)

entry(
    index = 37,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing",
    kinetics = ArrheniusBM(A=(4.38421e-12,'s^-1'), n=7.22006, w0=(798000,'J/mol'), E0=(103463,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing",
    kinetics = ArrheniusBM(A=(7.07407e-11,'s^-1'), n=6.82872, w0=(798000,'J/mol'), E0=(100753,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root",
    kinetics = ArrheniusBM(A=(44220.4,'s^-1'), n=2.55125, w0=(755204,'J/mol'), E0=(150530,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06871057353442966, var=57.68226706587711, Tref=1000.0, N=27, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 27 training reactions at node Root
    Total Standard Deviation in ln(k): 15.398370535650425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root
Total Standard Deviation in ln(k): 15.398370535650425""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root
Total Standard Deviation in ln(k): 15.398370535650425
""",
)

entry(
    index = 40,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.38702e+72,'s^-1'), n=-16.8799, w0=(670125,'J/mol'), E0=(378098,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0325128508066552, var=397.64301580674777, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 42.570652188583445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 42.570652188583445""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 42.570652188583445
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(0.000146187,'s^-1'), n=4.93211, w0=(770000,'J/mol'), E0=(113160,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.003495637019007975, var=8.168116975953765, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 5.738299366319756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 5.738299366319756""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 5.738299366319756
""",
)

entry(
    index = 42,
    label = "Root_1R!H-inRing_4R->C",
    kinetics = ArrheniusBM(A=(2.13185e+78,'s^-1'), n=-18.7334, w0=(707000,'J/mol'), E0=(425945,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0411052931213147, var=501.438488492061, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_4R->C
    Total Standard Deviation in ln(k): 47.50751869915296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_4R->C
Total Standard Deviation in ln(k): 47.50751869915296""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_4R->C
Total Standard Deviation in ln(k): 47.50751869915296
""",
)

entry(
    index = 43,
    label = "Root_1R!H-inRing_N-4R->C",
    kinetics = ArrheniusBM(A=(4.0435e+11,'s^-1'), n=1.01704, w0=(559500,'J/mol'), E0=(135903,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1R!H-inRing_3R!H->C",
    kinetics = ArrheniusBM(A=(0.0954007,'s^-1'), n=3.97882, w0=(762750,'J/mol'), E0=(250868,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05104117971660031, var=160.05464641490252, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_3R!H->C
    Total Standard Deviation in ln(k): 25.490690006267023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_3R!H->C
Total Standard Deviation in ln(k): 25.490690006267023
""",
)

entry(
    index = 45,
    label = "Root_N-1R!H-inRing_N-3R!H->C",
    kinetics = ArrheniusBM(A=(0.000109409,'s^-1'), n=4.96965, w0=(771526,'J/mol'), E0=(112528,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00255753453896434, var=7.194105339202176, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-3R!H->C
    Total Standard Deviation in ln(k): 5.383492195805062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-3R!H->C
Total Standard Deviation in ln(k): 5.383492195805062""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R!H-inRing_N-3R!H->C
Total Standard Deviation in ln(k): 5.383492195805062
""",
)

entry(
    index = 46,
    label = "Root_1R!H-inRing_4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(707000,'J/mol'), E0=(405481,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.6259e+11,'s^-1'), n=1.19107, w0=(707000,'J/mol'), E0=(249049,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.23584e+11,'s^-1'), n=1.27308, w0=(707000,'J/mol'), E0=(183610,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_4R->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H-inRing_3R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700500,'J/mol'), E0=(384026,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H-inRing_3R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(635.413,'s^-1'), n=2.83859, w0=(783500,'J/mol'), E0=(219488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012207818220425905, var=12.527101437509526, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C_N-4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C
    Total Standard Deviation in ln(k): 7.098555561663242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C
Total Standard Deviation in ln(k): 7.098555561663242
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-3R!H->C_3NS->S",
    kinetics = ArrheniusBM(A=(2628.85,'s^-1'), n=2.78353, w0=(782000,'J/mol'), E0=(89057.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004857179637508415, var=0.25064116944332687, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_3NS->S',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S
    Total Standard Deviation in ln(k): 1.0158560594211685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S
Total Standard Deviation in ln(k): 1.0158560594211685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S
Total Standard Deviation in ln(k): 1.0158560594211685
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S",
    kinetics = ArrheniusBM(A=(0.00132983,'s^-1'), n=4.6492, w0=(769562,'J/mol'), E0=(116133,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011878464585718973, var=6.628325949021129, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S
    Total Standard Deviation in ln(k): 5.1911431859520585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S
Total Standard Deviation in ln(k): 5.1911431859520585""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S
Total Standard Deviation in ln(k): 5.1911431859520585
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(205000,'s^-1'), n=2.37, w0=(783500,'J/mol'), E0=(221387,'J/mol'), Tmin=(600,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_3R!H->C_N-4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4909.53,'s^-1'), n=2.71698, w0=(782000,'J/mol'), E0=(88826.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1408662726283667e-06, var=3.5438674360202764e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.003776812860711284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.003776812860711284
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(0.000164309,'s^-1'), n=4.97161, w0=(787889,'J/mol'), E0=(112114,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.051526042577798054, var=4.08971979394378, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 4.183649319777569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.183649319777569""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.183649319777569
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R",
    kinetics = ArrheniusBM(A=(4.74194e-14,'s^-1'), n=7.69802, w0=(798000,'J/mol'), E0=(92033.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012749512289493472, var=0.8377613591004845, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R
    Total Standard Deviation in ln(k): 1.8669540248408663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R
Total Standard Deviation in ln(k): 1.8669540248408663""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R
Total Standard Deviation in ln(k): 1.8669540248408663
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.50087e+11,'s^-1'), n=0.45162, w0=(707000,'J/mol'), E0=(137659,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008012511677798886, var=3.4768369970791304, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O
    Total Standard Deviation in ln(k): 3.7582167842883063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O
Total Standard Deviation in ln(k): 3.7582167842883063""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O
Total Standard Deviation in ln(k): 3.7582167842883063
""",
)

entry(
    index = 58,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.85602e+09,'s^-1'), n=0.739985, w0=(707000,'J/mol'), E0=(193742,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(87.5,'s^-1'), n=3.23, w0=(782000,'J/mol'), E0=(84839.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_3NS->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R",
    kinetics = ArrheniusBM(A=(8.00067e+12,'s^-1'), n=0.391729, w0=(798000,'J/mol'), E0=(133048,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_Ext-3N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(6.91728e-07,'s^-1'), n=5.62342, w0=(779800,'J/mol'), E0=(106545,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006515153720890275, var=0.8806591803136841, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 1.897682153588295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 1.897682153588295""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N
Total Standard Deviation in ln(k): 1.897682153588295
""",
)

entry(
    index = 62,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(8.46061e-15,'s^-1'), n=7.98481, w0=(798000,'J/mol'), E0=(96853.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00263383782615601, var=0.4396759609029318, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 1.335918740070374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.335918740070374""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 1.335918740070374
""",
)

entry(
    index = 63,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.20077e-11,'s^-1'), n=7.05311, w0=(798000,'J/mol'), E0=(100604,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(7.35011e-13,'s^-1'), n=7.36802, w0=(798000,'J/mol'), E0=(90879,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(1.29627e-12,'s^-1'), n=7.28519, w0=(798000,'J/mol'), E0=(101095,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R",
    kinetics = ArrheniusBM(A=(1.88124e+11,'s^-1'), n=0.620515, w0=(707000,'J/mol'), E0=(161496,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-4R-R_5R!H->O_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C",
    kinetics = ArrheniusBM(A=(1.93892e+11,'s^-1'), n=0.308436, w0=(707000,'J/mol'), E0=(125262,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C",
    kinetics = ArrheniusBM(A=(7.72033e-12,'s^-1'), n=7.13865, w0=(798000,'J/mol'), E0=(101332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0009406278385854534, var=0.10603351746797161, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C
    Total Standard Deviation in ln(k): 0.6551610235432553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C
Total Standard Deviation in ln(k): 0.6551610235432553""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C
Total Standard Deviation in ln(k): 0.6551610235432553
""",
)

entry(
    index = 69,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(2.24517e-15,'s^-1'), n=8.2595, w0=(798000,'J/mol'), E0=(97485.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_Ext-5CO-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O",
    kinetics = ArrheniusBM(A=(3.21561e-15,'s^-1'), n=8.08717, w0=(798000,'J/mol'), E0=(97688.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O",
    kinetics = ArrheniusBM(A=(7.48602e-15,'s^-1'), n=8.00071, w0=(798000,'J/mol'), E0=(97935.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_N-5R!H->N_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R",
    kinetics = ArrheniusBM(A=(2.19963e-11,'s^-1'), n=6.98648, w0=(798000,'J/mol'), E0=(100797,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006099207969903697, var=0.16754745053310063, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
    Total Standard Deviation in ln(k): 0.8359140406399651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140406399651""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R
Total Standard Deviation in ln(k): 0.8359140406399651
""",
)

entry(
    index = 73,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N",
    kinetics = ArrheniusBM(A=(9.61654e-11,'s^-1'), n=6.78703, w0=(798000,'J/mol'), E0=(99834.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.1358e-11,'s^-1'), n=7.08342, w0=(798000,'J/mol'), E0=(101820,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.774397504036697e-05, var=0.31280538790524537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
    Total Standard Deviation in ln(k): 1.1213232657408565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N
Total Standard Deviation in ln(k): 1.1213232657408565
""",
)

entry(
    index = 75,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing",
    kinetics = ArrheniusBM(A=(4.38421e-12,'s^-1'), n=7.22006, w0=(798000,'J/mol'), E0=(103463,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing",
    kinetics = ArrheniusBM(A=(7.07407e-11,'s^-1'), n=6.82872, w0=(798000,'J/mol'), E0=(100753,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-3R!H->C_N-3NS->S_Ext-1R!H-R_5R!H->N_N-4R->C_Ext-5N-R_Ext-6R!H-R_N-7R!H->N_N-5N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

