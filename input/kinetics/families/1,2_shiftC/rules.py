#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftC/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.6964e+20,'s^-1'), n=-2.11952, w0=(346000,'J/mol'), E0=(196648,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16358820638457122, var=44.125287505364916, Tref=1000.0, N=14, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 14 training reactions at node Root
    Total Standard Deviation in ln(k): 13.72785281728103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 13.72785281728103""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root
Total Standard Deviation in ln(k): 13.72785281728103
""",
)

entry(
    index = 2,
    label = "Root_2C-inRing",
    kinetics = ArrheniusBM(A=(1.45019e+12,'s^-1'), n=0.230345, w0=(346000,'J/mol'), E0=(73646.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.602528453014257e-15, var=1.7594408983748204, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_2C-inRing
    Total Standard Deviation in ln(k): 2.659159152278503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2C-inRing
Total Standard Deviation in ln(k): 2.659159152278503""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2C-inRing
Total Standard Deviation in ln(k): 2.659159152278503
""",
)

entry(
    index = 3,
    label = "Root_N-2C-inRing",
    kinetics = ArrheniusBM(A=(1.1964e+26,'s^-1'), n=-3.84227, w0=(346000,'J/mol'), E0=(226355,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.254612307638064, var=16.564467728647873, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2C-inRing',), comment="""BM rule fitted to 12 training reactions at node Root_N-2C-inRing
    Total Standard Deviation in ln(k): 8.798894719843853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2C-inRing
Total Standard Deviation in ln(k): 8.798894719843853""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2C-inRing
Total Standard Deviation in ln(k): 8.798894719843853
""",
)

entry(
    index = 4,
    label = "Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.889e+11,'s^-1'), n=0.232, w0=(346000,'J/mol'), E0=(73563.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-2C-inRing_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.66145e-43,'s^-1'), n=16.5685, w0=(346000,'J/mol'), E0=(34600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9282086058575623, var=18.335046347453236, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2C-inRing_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-2C-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 10.916346214418185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 10.916346214418185""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 10.916346214418185
""",
)

entry(
    index = 6,
    label = "Root_N-2C-inRing_1C-inRing",
    kinetics = ArrheniusBM(A=(271458,'s^-1'), n=2.15092, w0=(346000,'J/mol'), E0=(189236,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04365810055905589, var=16.762119635932194, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2C-inRing_1C-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_N-2C-inRing_1C-inRing
    Total Standard Deviation in ln(k): 8.317393403926824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2C-inRing_1C-inRing
Total Standard Deviation in ln(k): 8.317393403926824""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2C-inRing_1C-inRing
Total Standard Deviation in ln(k): 8.317393403926824
""",
)

entry(
    index = 7,
    label = "Root_N-2C-inRing_N-1C-inRing",
    kinetics = ArrheniusBM(A=(8.71621e+08,'s^-1'), n=1.32857, w0=(346000,'J/mol'), E0=(202707,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=108.5858712952931, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_N-1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_N-1C-inRing
    Total Standard Deviation in ln(k): 20.89025059204401"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_N-1C-inRing
Total Standard Deviation in ln(k): 20.89025059204401""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_N-1C-inRing
Total Standard Deviation in ln(k): 20.89025059204401
""",
)

entry(
    index = 8,
    label = "Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(1.53838e-43,'s^-1'), n=16.7623, w0=(346000,'J/mol'), E0=(34600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=12.968454541620165, var=19.263561723371954, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 41.382893868574726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 41.382893868574726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 41.382893868574726
""",
)

entry(
    index = 9,
    label = "Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(4.6044e-43,'s^-1'), n=16.3747, w0=(346000,'J/mol'), E0=(34600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=13.507168738944157, var=19.26356172337115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 42.73644712818256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 42.73644712818256""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_Ext-2C-R_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 42.73644712818256
""",
)

entry(
    index = 10,
    label = "Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(6.47522e+10,'s^-1'), n=0.703091, w0=(346000,'J/mol'), E0=(196769,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.205056906028515e-15, var=6.493939517144499, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 5.108708339076415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.108708339076415""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.108708339076415
""",
)

entry(
    index = 11,
    label = "Root_N-2C-inRing_1C-inRing_3C-inRing",
    kinetics = ArrheniusBM(A=(6.77003e+08,'s^-1'), n=1.3041, w0=(346000,'J/mol'), E0=(192099,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.447725953338633e-15, var=6.493939517145264, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_1C-inRing_3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_3C-inRing
    Total Standard Deviation in ln(k): 5.108708339076711"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_3C-inRing
Total Standard Deviation in ln(k): 5.108708339076711""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_3C-inRing
Total Standard Deviation in ln(k): 5.108708339076711
""",
)

entry(
    index = 12,
    label = "Root_N-2C-inRing_1C-inRing_N-3C-inRing",
    kinetics = ArrheniusBM(A=(979197,'s^-1'), n=1.68844, w0=(346000,'J/mol'), E0=(198020,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4058647621519051e-15, var=108.58587129529421, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2C-inRing_1C-inRing_N-3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_N-3C-inRing
    Total Standard Deviation in ln(k): 20.890250592044122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 20.890250592044122""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2C-inRing_1C-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 20.890250592044122
""",
)

