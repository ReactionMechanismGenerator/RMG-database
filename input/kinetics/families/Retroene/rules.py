#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.69762e+27,'s^-1'), n=-4.4977, w0=(1.11211e+06,'J/mol'), E0=(176669,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14486523882846947, var=132.63092240559882, Tref=1000.0, N=66, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 66 training reactions at node Root
    Total Standard Deviation in ln(k): 23.451614637409254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 23.451614637409254""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 23.451614637409254
""",
)

entry(
    index = 2,
    label = "Root_4R!H->C",
    kinetics = ArrheniusBM(A=(2.60995e+12,'s^-1'), n=-0.232363, w0=(1.11255e+06,'J/mol'), E0=(171058,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08178908396205459, var=5.664309242707326, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_4R!H->C',), comment="""BM rule fitted to 65 training reactions at node Root_4R!H->C
    Total Standard Deviation in ln(k): 4.976731471406514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_4R!H->C
Total Standard Deviation in ln(k): 4.976731471406514""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_4R!H->C
Total Standard Deviation in ln(k): 4.976731471406514
""",
)

entry(
    index = 3,
    label = "Root_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.46545e+14,'s^-1'), n=0.20628, w0=(1.0836e+06,'J/mol'), E0=(30025.7,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_4R!H->C_1R!H->O",
    kinetics = ArrheniusBM(A=(9.88064e+10,'s^-1'), n=0.145534, w0=(1.17025e+06,'J/mol'), E0=(162131,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08910027457046228, var=12.875945198171234, Tref=1000.0, N=34, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O',), comment="""BM rule fitted to 34 training reactions at node Root_4R!H->C_1R!H->O
    Total Standard Deviation in ln(k): 7.417474409373551"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root_4R!H->C_1R!H->O
Total Standard Deviation in ln(k): 7.417474409373551""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root_4R!H->C_1R!H->O
Total Standard Deviation in ln(k): 7.417474409373551
""",
)

entry(
    index = 5,
    label = "Root_4R!H->C_N-1R!H->O",
    kinetics = ArrheniusBM(A=(1.75937e+14,'s^-1'), n=-0.752182, w0=(1.04926e+06,'J/mol'), E0=(177823,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09940869752124652, var=3.0101612294936864, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O',), comment="""BM rule fitted to 31 training reactions at node Root_4R!H->C_N-1R!H->O
    Total Standard Deviation in ln(k): 3.72794911351602"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_4R!H->C_N-1R!H->O
Total Standard Deviation in ln(k): 3.72794911351602""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_4R!H->C_N-1R!H->O
Total Standard Deviation in ln(k): 3.72794911351602
""",
)

entry(
    index = 6,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.39379e+10,'s^-1'), n=0.636141, w0=(1.183e+06,'J/mol'), E0=(153232,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08208416277232389, var=3.1024985670630194, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R',), comment="""BM rule fitted to 17 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.7373641153678494"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.7373641153678494""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.7373641153678494
""",
)

entry(
    index = 7,
    label = "Root_4R!H->C_1R!H->O_3R!H-inRing",
    kinetics = ArrheniusBM(A=(7.51733e+12,'s^-1'), n=-0.801522, w0=(1.0245e+06,'J/mol'), E0=(143090,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010065863716581231, var=81.8360764684643, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_3R!H-inRing
    Total Standard Deviation in ln(k): 18.160785079462567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_3R!H-inRing
Total Standard Deviation in ln(k): 18.160785079462567""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_3R!H-inRing
Total Standard Deviation in ln(k): 18.160785079462567
""",
)

entry(
    index = 8,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(3.80526e+09,'s^-1'), n=0.557473, w0=(1.17523e+06,'J/mol'), E0=(167509,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06985395151529518, var=15.195398944716686, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing',), comment="""BM rule fitted to 15 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing
    Total Standard Deviation in ln(k): 7.99022561771435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.99022561771435""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.99022561771435
""",
)

entry(
    index = 9,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C",
    kinetics = ArrheniusBM(A=(1.13654e+14,'s^-1'), n=-0.713755, w0=(1.0543e+06,'J/mol'), E0=(175246,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09769887345958214, var=2.5615805550933186, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C',), comment="""BM rule fitted to 27 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C
    Total Standard Deviation in ln(k): 3.454040713171818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 3.454040713171818""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 3.454040713171818
""",
)

entry(
    index = 10,
    label = "Root_4R!H->C_N-1R!H->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(4.66324e+09,'s^-1'), n=1.0266, w0=(1.01525e+06,'J/mol'), E0=(221067,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.6261064540329477, var=38.372409117272156, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_N-2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C
    Total Standard Deviation in ln(k): 21.529245342658523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 21.529245342658523""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 21.529245342658523
""",
)

entry(
    index = 11,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.3023e+08,'s^-1'), n=0.995367, w0=(1.183e+06,'J/mol'), E0=(138104,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9718999545224009, var=2.144363497198564, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.37762263812869"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.37762263812869""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.37762263812869
""",
)

entry(
    index = 12,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_7R!H->O",
    kinetics = ArrheniusBM(A=(6.63512e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(94204,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(6.01187e+09,'s^-1'), n=0.754214, w0=(1.183e+06,'J/mol'), E0=(159151,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09510808833121338, var=0.3875877265781486, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O',), comment="""BM rule fitted to 12 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O
    Total Standard Deviation in ln(k): 1.4870438207877734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.4870438207877734""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 1.4870438207877734
""",
)

entry(
    index = 14,
    label = "Root_4R!H->C_1R!H->O_3R!H-inRing_Ext-4C-R",
    kinetics = ArrheniusBM(A=(550000,'s^-1'), n=0.9, w0=(1.0245e+06,'J/mol'), E0=(131295,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_3R!H-inRing_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_3R!H-inRing_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_3R!H-inRing_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_3R!H-inRing_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.70358e+06,'s^-1'), n=1.58277, w0=(1.183e+06,'J/mol'), E0=(173228,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03155295581004311, var=0.24981443779741802, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R',), comment="""BM rule fitted to 9 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R
    Total Standard Deviation in ln(k): 1.0812742500274948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R
Total Standard Deviation in ln(k): 1.0812742500274948""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R
Total Standard Deviation in ln(k): 1.0812742500274948
""",
)

entry(
    index = 16,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.70672e+11,'s^-1'), n=-0.237439, w0=(1.183e+06,'J/mol'), E0=(161695,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004913256994020603, var=47.85043960098877, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 13.879901731532712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.879901731532712""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.879901731532712
""",
)

entry(
    index = 17,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_5R!H->O",
    kinetics = ArrheniusBM(A=(3.96667e+10,'s^-1'), n=0.59, w0=(1.183e+06,'J/mol'), E0=(179850,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_N-5R!H->O",
    kinetics = ArrheniusBM(A=(3.33333e+07,'s^-1'), n=1.2, w0=(1.0665e+06,'J/mol'), E0=(177017,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.46401e+12,'s^-1'), n=-0.158593, w0=(1.0845e+06,'J/mol'), E0=(176009,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09120822726898409, var=2.288308081150335, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 15 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.2617601570296633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.2617601570296633""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.2617601570296633
""",
)

entry(
    index = 20,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O",
    kinetics = ArrheniusBM(A=(3.94505e+09,'s^-1'), n=0.601596, w0=(1.0845e+06,'J/mol'), E0=(169425,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07591793873856303, var=4.052420941329839, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O
    Total Standard Deviation in ln(k): 4.226405752097705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O
Total Standard Deviation in ln(k): 4.226405752097705""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O
Total Standard Deviation in ln(k): 4.226405752097705
""",
)

entry(
    index = 21,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.32284e+18,'s^-1'), n=-2.21337, w0=(968000,'J/mol'), E0=(173278,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09274224034300145, var=3.2786817472081715, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O
    Total Standard Deviation in ln(k): 3.8630206695740643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.8630206695740643""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.8630206695740643
""",
)

entry(
    index = 22,
    label = "Root_4R!H->C_N-1R!H->O_N-2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.8e+12,'s^-1'), n=0, w0=(1.0665e+06,'J/mol'), E0=(218338,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_N-2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_4R!H->C_N-1R!H->O_N-2R!H->C_2NOS->S",
    kinetics = ArrheniusBM(A=(5.6608e+10,'s^-1'), n=0, w0=(953500,'J/mol'), E0=(119669,'J/mol'), Tmin=(588,'K'), Tmax=(691,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_N-2R!H->C_2NOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_2NOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S",
    kinetics = ArrheniusBM(A=(3.11827e+11,'s^-1'), n=-0.293682, w0=(1.0205e+06,'J/mol'), E0=(160991,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001642907944431047, var=4.049121298193099, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S
    Total Standard Deviation in ln(k): 4.03814174042697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 4.03814174042697""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 4.03814174042697
""",
)

entry(
    index = 25,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.45626e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(142579,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.82163e+08,'s^-1'), n=0.989298, w0=(1.183e+06,'J/mol'), E0=(138899,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9397855924827363, var=2.0052075611816607, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 5.200082488575585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.200082488575585""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.200082488575585
""",
)

entry(
    index = 27,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R",
    kinetics = ArrheniusBM(A=(8.60672e+08,'s^-1'), n=0.975858, w0=(1.183e+06,'J/mol'), E0=(154165,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8106532067876975, var=2.4765646750760326, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R',), comment="""BM rule fitted to 7 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R
    Total Standard Deviation in ln(k): 5.191689703536848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R
Total Standard Deviation in ln(k): 5.191689703536848""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R
Total Standard Deviation in ln(k): 5.191689703536848
""",
)

entry(
    index = 28,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.09881e+10,'s^-1'), n=0.632458, w0=(1.183e+06,'J/mol'), E0=(164532,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1408693790180404, var=0.053707762569230044, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R
    Total Standard Deviation in ln(k): 0.8185392202824676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 0.8185392202824676""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 0.8185392202824676
""",
)

entry(
    index = 29,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.32388e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(156130,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.72908e+06,'s^-1'), n=1.66491, w0=(1.183e+06,'J/mol'), E0=(172562,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.062098384893677284, var=0.15842678504256216, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 0.9539680358266616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 0.9539680358266616""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 0.9539680358266616
""",
)

entry(
    index = 31,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(4.24828e+14,'s^-1'), n=-0.820293, w0=(1.183e+06,'J/mol'), E0=(193063,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0018304600500318844, var=4.827869185588401, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 4.4094857873895865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.4094857873895865""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.4094857873895865
""",
)

entry(
    index = 32,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.72259e+12,'s^-1'), n=-0.0948649, w0=(1.183e+06,'J/mol'), E0=(172576,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005388821963453984, var=0.5959934247797803, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 1.5612074705444146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5612074705444146""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5612074705444146
""",
)

entry(
    index = 33,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(58002.5,'s^-1'), n=0.286, w0=(1.183e+06,'J/mol'), E0=(125561,'J/mol'), Tmin=(500,'K'), Tmax=(1300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.03406e+08,'s^-1'), n=1.25673, w0=(1.0845e+06,'J/mol'), E0=(177221,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03936086616282145, var=1.4404858450236613, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N
    Total Standard Deviation in ln(k): 2.5049845366985655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.5049845366985655""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.5049845366985655
""",
)

entry(
    index = 35,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.18527e+12,'s^-1'), n=-0.0115864, w0=(1.0845e+06,'J/mol'), E0=(169271,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0704975947618844, var=2.3195327210082453, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N',), comment="""BM rule fitted to 10 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N
    Total Standard Deviation in ln(k): 3.230343606944405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 3.230343606944405""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 3.230343606944405
""",
)

entry(
    index = 36,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.16228e+08,'s^-1'), n=0.988266, w0=(1.0845e+06,'J/mol'), E0=(162518,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0025626047091315556, var=9.251604624994211, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 6.104131234895419"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 6.104131234895419""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 6.104131234895419
""",
)

entry(
    index = 37,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(7.24523e+06,'s^-1'), n=1.35008, w0=(1.0845e+06,'J/mol'), E0=(171424,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.024461205742499107, var=5.078314475822991, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R
    Total Standard Deviation in ln(k): 4.579154043078822"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 4.579154043078822""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 4.579154043078822
""",
)

entry(
    index = 38,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.54601e+20,'s^-1'), n=-3.0326, w0=(968000,'J/mol'), E0=(170265,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12749591170885038, var=3.8667020133400993, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R
    Total Standard Deviation in ln(k): 4.262438806876281"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 4.262438806876281""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 4.262438806876281
""",
)

entry(
    index = 39,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.23333e+11,'s^-1'), n=0, w0=(968000,'J/mol'), E0=(182946,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_2NO->O",
    kinetics = ArrheniusBM(A=(4.1009e+10,'s^-1'), n=0, w0=(1.0665e+06,'J/mol'), E0=(167048,'J/mol'), Tmin=(725,'K'), Tmax=(810,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_N-2NO->O",
    kinetics = ArrheniusBM(A=(7.8141e+10,'s^-1'), n=0, w0=(974500,'J/mol'), E0=(160561,'J/mol'), Tmin=(602,'K'), Tmax=(694,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_N-2R!H->C_N-2NOS->S_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.39881e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(136330,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.2598e+13,'s^-1'), n=-0.459377, w0=(1.183e+06,'J/mol'), E0=(156365,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0006121978434094917, var=0.04941026246110573, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 0.44715910440908485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R
Total Standard Deviation in ln(k): 0.44715910440908485""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R
Total Standard Deviation in ln(k): 0.44715910440908485
""",
)

entry(
    index = 44,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.26986e+13,'s^-1'), n=-0.442687, w0=(1.183e+06,'J/mol'), E0=(141989,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0089736677479887, var=1.7601354926927055, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.68223089749146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.68223089749146""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.68223089749146
""",
)

entry(
    index = 45,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.4107e+13,'s^-1'), n=-0.432391, w0=(1.183e+06,'J/mol'), E0=(160784,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0010628098785811556, var=0.16224599752348345, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.8101730807390738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8101730807390738""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8101730807390738
""",
)

entry(
    index = 46,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_7C-inRing",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(165471,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing",
    kinetics = ArrheniusBM(A=(3.93467e+06,'s^-1'), n=1.69077, w0=(1.183e+06,'J/mol'), E0=(172691,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.047594001962377265, var=0.10410275187919844, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing
    Total Standard Deviation in ln(k): 0.7664098514942174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.7664098514942174""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.7664098514942174
""",
)

entry(
    index = 48,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(181493,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(6.26345e+11,'s^-1'), n=0.219787, w0=(1.183e+06,'J/mol'), E0=(170925,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.8745213110839e-15, var=2.116729755416175, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 2.9166861328622713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.9166861328622713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.9166861328622713
""",
)

entry(
    index = 50,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.30743e+07,'s^-1'), n=1.34294, w0=(1.0845e+06,'J/mol'), E0=(186642,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014692611028300074, var=6.989117524371048, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R
    Total Standard Deviation in ln(k): 5.336822036500276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R
Total Standard Deviation in ln(k): 5.336822036500276""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R
Total Standard Deviation in ln(k): 5.336822036500276
""",
)

entry(
    index = 51,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.08779e+07,'s^-1'), n=1.30493, w0=(1.0845e+06,'J/mol'), E0=(168720,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00044315246717545727, var=0.047018350676703256, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 0.4358144939813908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.4358144939813908""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.4358144939813908
""",
)

entry(
    index = 52,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.10319e+11,'s^-1'), n=0.204824, w0=(1.0845e+06,'J/mol'), E0=(175924,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.061353959294216984, var=3.4900972510040535, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R
    Total Standard Deviation in ln(k): 3.899362049801037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R
Total Standard Deviation in ln(k): 3.899362049801037""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R
Total Standard Deviation in ln(k): 3.899362049801037
""",
)

entry(
    index = 53,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.59965e+09,'s^-1'), n=0.653805, w0=(1.0845e+06,'J/mol'), E0=(159613,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006151462620514832, var=1.8383730646871563, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 2.733608402853133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.733608402853133""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.733608402853133
""",
)

entry(
    index = 54,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->O",
    kinetics = ArrheniusBM(A=(1.2535e+06,'s^-1'), n=1.80968, w0=(1.0845e+06,'J/mol'), E0=(155867,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->O",
    kinetics = ArrheniusBM(A=(11.5839,'s^-1'), n=3.09547, w0=(1.0845e+06,'J/mol'), E0=(137668,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(21.2645,'s^-1'), n=2.97303, w0=(1.0845e+06,'J/mol'), E0=(145085,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.78363e+11,'s^-1'), n=0.169307, w0=(1.0845e+06,'J/mol'), E0=(163318,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.80655,'s^-1'), n=3.07798, w0=(1.0845e+06,'J/mol'), E0=(148263,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2419.21,'s^-1'), n=2.3826, w0=(1.0845e+06,'J/mol'), E0=(171107,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_5R!H->O_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.54049e+21,'s^-1'), n=-3.24953, w0=(968000,'J/mol'), E0=(163723,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1297736116659072, var=2.9989072691974563, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 3.797734921010004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.797734921010004""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.797734921010004
""",
)

entry(
    index = 61,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_7C-inRing",
    kinetics = ArrheniusBM(A=(1.25594e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(155092,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.98582e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(160232,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_N-7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4C-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.32702e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(116943,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.37297e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(151179,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.84721e+12,'s^-1'), n=-0.302094, w0=(1.183e+06,'J/mol'), E0=(150154,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.255606157999161e-05, var=0.017017844750293856, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.2616044249499389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2616044249499389""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2616044249499389
""",
)

entry(
    index = 66,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(1.11936e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(158970,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_Sp-9R!H-8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(1.99054e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(166153,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-4C-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R",
    kinetics = ArrheniusBM(A=(139248,'s^-1'), n=2.06526, w0=(1.183e+06,'J/mol'), E0=(165686,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6647699949854299, var=1.1672292911792304, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R
    Total Standard Deviation in ln(k): 3.8361597962833978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.8361597962833978""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.8361597962833978
""",
)

entry(
    index = 69,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.16053e+06,'s^-1'), n=1.87467, w0=(1.183e+06,'J/mol'), E0=(182477,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(6.96433e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(174127,'J/mol'), Tmin=(900,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1708.21,'s^-1'), n=2.62955, w0=(1.0845e+06,'J/mol'), E0=(162976,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(85500.5,'s^-1'), n=2.19797, w0=(1.0845e+06,'J/mol'), E0=(186561,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-4C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(111514,'s^-1'), n=2.05353, w0=(1.0845e+06,'J/mol'), E0=(161295,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.3077e+06,'s^-1'), n=1.41637, w0=(1.0845e+06,'J/mol'), E0=(156860,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O",
    kinetics = ArrheniusBM(A=(2.01084e+12,'s^-1'), n=0.0883205, w0=(1.0845e+06,'J/mol'), E0=(183925,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.021492990850914453, var=5.303057773824753, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 4.670580394351897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 4.670580394351897""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 4.670580394351897
""",
)

entry(
    index = 76,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O",
    kinetics = ArrheniusBM(A=(9.58447e+09,'s^-1'), n=0.427548, w0=(1.0845e+06,'J/mol'), E0=(167154,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023199101818381307, var=14.082287951603485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 7.581333161482922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 7.581333161482922""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 7.581333161482922
""",
)

entry(
    index = 77,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.6009e+07,'s^-1'), n=1.28561, w0=(1.0845e+06,'J/mol'), E0=(152714,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00720347818867495, var=1.1128229402110497, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.1329027100546143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1329027100546143""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1329027100546143
""",
)

entry(
    index = 78,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(5.01614e+11,'s^-1'), n=0.272082, w0=(1.0845e+06,'J/mol'), E0=(164653,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0004677404420120619, var=2.2953718575893025, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 3.038446033140682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.038446033140682""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.038446033140682
""",
)

entry(
    index = 79,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.84364e+21,'s^-1'), n=-3.37687, w0=(968000,'J/mol'), E0=(155107,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12158036022019265, var=4.26315521405602, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 4.4447369115914395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.4447369115914395""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.4447369115914395
""",
)

entry(
    index = 80,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing",
    kinetics = ArrheniusBM(A=(1.32702e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(152192,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.32702e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(151418,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(7.94328e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(172170,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(170162,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(168938,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_1R!H->O_N-3R!H-inRing_Ext-4C-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_8R!H->N",
    kinetics = ArrheniusBM(A=(2.87851e+08,'s^-1'), n=1.30992, w0=(1.0845e+06,'J/mol'), E0=(187582,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_N-8R!H->N",
    kinetics = ArrheniusBM(A=(6.1395e+07,'s^-1'), n=1.36832, w0=(1.0845e+06,'J/mol'), E0=(163924,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_N-8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_N-8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_7BrCClFILiOPSSi->O_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_8R!H->N",
    kinetics = ArrheniusBM(A=(6552.1,'s^-1'), n=2.29082, w0=(1.0845e+06,'J/mol'), E0=(167773,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_N-8R!H->N",
    kinetics = ArrheniusBM(A=(459.236,'s^-1'), n=2.68918, w0=(1.0845e+06,'J/mol'), E0=(145855,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_N-8R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_N-8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4C-R_N-7BrCClFILiOPSSi->O_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->O",
    kinetics = ArrheniusBM(A=(1.65185e+07,'s^-1'), n=1.51788, w0=(1.0845e+06,'J/mol'), E0=(159604,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->O",
    kinetics = ArrheniusBM(A=(1017.11,'s^-1'), n=2.55399, w0=(1.0845e+06,'J/mol'), E0=(143955,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->O",
    kinetics = ArrheniusBM(A=(8.27867e+08,'s^-1'), n=1.04991, w0=(1.0845e+06,'J/mol'), E0=(160247,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->O",
    kinetics = ArrheniusBM(A=(2.0173e+12,'s^-1'), n=0.0499164, w0=(1.0845e+06,'J/mol'), E0=(158672,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.34275e+16,'s^-1'), n=-2.11924, w0=(968000,'J/mol'), E0=(122130,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0013608568101268583, var=1.6674726433047609, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.5921468035711666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.5921468035711666""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.5921468035711666
""",
)

entry(
    index = 94,
    label = "Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(6.5e+10,'s^-1'), n=0, w0=(968000,'J/mol'), E0=(139431,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->C_N-1R!H->O_2R!H->C_N-5R!H->O_Ext-4C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

