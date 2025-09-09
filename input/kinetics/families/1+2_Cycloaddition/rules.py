#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.12226e+61,'m^3/(mol*s)'), n=-16.0884, w0=(533238,'J/mol'), E0=(246558,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2722699579412944, var=172.54165599779202, Tref=1000.0, N=42, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 42 training reactions at node Root
    Total Standard Deviation in ln(k): 29.529878363341602"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 29.529878363341602""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 29.529878363341602
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R-R",
    kinetics = ArrheniusBM(A=(8.2809e+64,'m^3/(mol*s)'), n=-17.1, w0=(555517,'J/mol'), E0=(252503,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3371116120760236, var=190.18498805714407, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-3R-R
    Total Standard Deviation in ln(k): 31.006391901463598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 31.006391901463598""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 31.006391901463598
""",
)

entry(
    index = 3,
    label = "Root_1R->C",
    kinetics = ArrheniusBM(A=(2.94176e+08,'m^3/(mol*s)'), n=-0.463393, w0=(476125,'J/mol'), E0=(47612.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05349156708281672, var=2.5349342802848747, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->C',), comment="""BM rule fitted to 12 training reactions at node Root_1R->C
    Total Standard Deviation in ln(k): 3.326235253360758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.326235253360758""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.326235253360758
""",
)

entry(
    index = 4,
    label = "Root_N-1R->C",
    kinetics = Arrhenius(A=(0.53862,'m^3/(mol*s)'), n=1.86213, Ea=(24.8236,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-3R-R_Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(8.38341e+83,'m^3/(mol*s)'), n=-22.4573, w0=(543529,'J/mol'), E0=(255951,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.966919107381292, var=358.5627861506535, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R',), comment="""BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
    Total Standard Deviation in ln(k): 42.9031784176823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
Total Standard Deviation in ln(k): 42.9031784176823""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
Total Standard Deviation in ln(k): 42.9031784176823
""",
)

entry(
    index = 6,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(0.000185287,'m^3/(mol*s)'), n=2.48586, w0=(572500,'J/mol'), E0=(122114,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6955281655065114, var=4.168392351628768, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
    Total Standard Deviation in ln(k): 5.840553869024548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 5.840553869024548""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 5.840553869024548
""",
)

entry(
    index = 7,
    label = "Root_1R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.5716e+09,'m^3/(mol*s)'), n=-0.704858, w0=(474200,'J/mol'), E0=(47420,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003178602591253677, var=0.5008544564983712, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.4267589342073508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.4267589342073508""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.4267589342073508
""",
)

entry(
    index = 8,
    label = "Root_1R->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.33384e+09,'m^3/(mol*s)'), n=-0.775738, w0=(480000,'J/mol'), E0=(48000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03181634044488337, var=0.1433731634963656, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 0.8390264519529201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264519529201""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264519529201
""",
)

entry(
    index = 9,
    label = "Root_1R->C_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(0.00650771,'m^3/(mol*s)'), n=2.42295, w0=(480000,'J/mol'), E0=(48000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.587997258796586, var=0.16964704494037178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
    Total Standard Deviation in ln(k): 4.815657794528946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 4.815657794528946""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 4.815657794528946
""",
)

entry(
    index = 10,
    label = "Root_1R->C_N-Sp-2R=1C",
    kinetics = Arrhenius(A=(1.77e+09,'m^3/(mol*s)'), n=-0.662, Ea=(0.157737,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-Sp-2R=1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O",
    kinetics = ArrheniusBM(A=(1.51573e+73,'m^3/(mol*s)'), n=-19.5078, w0=(572500,'J/mol'), E0=(57250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.201514588840799, var=507.3214741338958, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O
    Total Standard Deviation in ln(k): 50.68569151890344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O
Total Standard Deviation in ln(k): 50.68569151890344""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O
Total Standard Deviation in ln(k): 50.68569151890344
""",
)

entry(
    index = 12,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.17824e-12,'m^3/(mol*s)'), n=5.10651, w0=(531458,'J/mol'), E0=(99181.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12352543373606474, var=88.63265079662075, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O
    Total Standard Deviation in ln(k): 19.183926820418357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O
Total Standard Deviation in ln(k): 19.183926820418357""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O
Total Standard Deviation in ln(k): 19.183926820418357
""",
)

entry(
    index = 13,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(8.45774e-05,'m^3/(mol*s)'), n=2.5714, w0=(572500,'J/mol'), E0=(120114,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7460883696108487, var=4.576739706677535, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
    Total Standard Deviation in ln(k): 6.163386999776856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
Total Standard Deviation in ln(k): 6.163386999776856""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
Total Standard Deviation in ln(k): 6.163386999776856
""",
)

entry(
    index = 14,
    label = "Root_1R->C_Ext-1C-R_Ext-1C-R",
    kinetics = Arrhenius(A=(3.18e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(9.41381e+08,'m^3/(mol*s)'), n=-0.607357, w0=(480000,'J/mol'), E0=(48000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2790521167276606, var=0.007777354492480229, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
    Total Standard Deviation in ln(k): 0.877932175956457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 0.877932175956457""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 0.877932175956457
""",
)

entry(
    index = 16,
    label = "Root_1R->C_Ext-1C-R_N-Sp-2R=1C",
    kinetics = ArrheniusBM(A=(4.63231e+09,'m^3/(mol*s)'), n=-0.7664, w0=(462500,'J/mol'), E0=(46250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0009309671137264789, var=1.1655949953965052, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
    Total Standard Deviation in ln(k): 2.1667057286443416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.1667057286443416""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.1667057286443416
""",
)

entry(
    index = 17,
    label = "Root_1R->C_Ext-2R-R_3R->C",
    kinetics = ArrheniusBM(A=(4.13595e+09,'m^3/(mol*s)'), n=-0.801251, w0=(474000,'J/mol'), E0=(47400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0395530227295251, var=0.0335984334446083, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
    Total Standard Deviation in ln(k): 0.46684489712018756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.46684489712018756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.46684489712018756
""",
)

entry(
    index = 18,
    label = "Root_1R->C_Ext-2R-R_N-3R->C",
    kinetics = ArrheniusBM(A=(3.86082e+06,'m^3/(mol*s)'), n=0.0243327, w0=(486000,'J/mol'), E0=(48600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02516094828390788, var=1.7607258136569388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
    Total Standard Deviation in ln(k): 2.7233484267253916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.7233484267253916""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.7233484267253916
""",
)

entry(
    index = 19,
    label = "Root_1R->C_Sp-2R=1C_3R->C",
    kinetics = Arrhenius(A=(1.98e+06,'m^3/(mol*s)'), n=0, Ea=(22.1334,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R->C_Sp-2R=1C_N-3R->C",
    kinetics = Arrhenius(A=(700000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_N-3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.82187e+63,'m^3/(mol*s)'), n=-18.1352, w0=(572500,'J/mol'), E0=(57250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0327056932932392, var=0.34661724107051156, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.287572643565924"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.287572643565924""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.287572643565924
""",
)

entry(
    index = 22,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(2.73238e-05,'m^3/(mol*s)'), n=4.17252, Ea=(-219.263,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C",
    kinetics = ArrheniusBM(A=(2.66099e+11,'m^3/(mol*s)'), n=-1.6382, w0=(490417,'J/mol'), E0=(146247,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13440794849427926, var=5.325940616635925, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C
    Total Standard Deviation in ln(k): 4.964235927896662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C
Total Standard Deviation in ln(k): 4.964235927896662""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C
Total Standard Deviation in ln(k): 4.964235927896662
""",
)

entry(
    index = 24,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C",
    kinetics = ArrheniusBM(A=(1.25194e-20,'m^3/(mol*s)'), n=7.39441, w0=(572500,'J/mol'), E0=(78134.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.36459434399760143, var=94.79238733942586, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C
    Total Standard Deviation in ln(k): 20.434443988694632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C
Total Standard Deviation in ln(k): 20.434443988694632""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C
Total Standard Deviation in ln(k): 20.434443988694632
""",
)

entry(
    index = 25,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O",
    kinetics = Arrhenius(A=(2.17596e-11,'m^3/(mol*s)'), n=4.37463, Ea=(150.001,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-7.198027582217753e-16, var=27.439778177234164, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O
    Total Standard Deviation in ln(k): 10.501402088694494"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 10.501402088694494""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 10.501402088694494
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1106.35,'m^3/(mol*s)'), n=0.603027, w0=(572500,'J/mol'), E0=(136674,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28581201102463416, var=5.4824686992705765, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O
    Total Standard Deviation in ln(k): 5.41214208078228"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 5.41214208078228""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 5.41214208078228
""",
)

entry(
    index = 27,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R",
    kinetics = Arrhenius(A=(1.54e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R",
    kinetics = Arrhenius(A=(4.7e+09,'m^3/(mol*s)'), n=-0.823, Ea=(0.096232,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R",
    kinetics = Arrhenius(A=(1.85e+09,'m^3/(mol*s)'), n=-0.7, Ea=(-0.281165,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R",
    kinetics = Arrhenius(A=(7.6e+06,'m^3/(mol*s)'), n=0, Ea=(0.4184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(3.61592e+63,'m^3/(mol*s)'), n=-18.144, w0=(572500,'J/mol'), E0=(57250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-22.015638261979277, var=0.19933301083027996, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 56.210722594421675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 56.210722594421675""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 56.210722594421675
""",
)

entry(
    index = 32,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.72865e-13,'m^3/(mol*s)'), n=3.65675, Ea=(-187.206,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F",
    kinetics = ArrheniusBM(A=(3.57904e-20,'m^3/(mol*s)'), n=7.10843, w0=(498625,'J/mol'), E0=(38339.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30875733744126155, var=3.774398665489801, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F
    Total Standard Deviation in ln(k): 4.670533759173948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F
Total Standard Deviation in ln(k): 4.670533759173948""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F
Total Standard Deviation in ln(k): 4.670533759173948
""",
)

entry(
    index = 34,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F",
    kinetics = ArrheniusBM(A=(2.95403e-06,'m^3/(mol*s)'), n=3.41638, w0=(474000,'J/mol'), E0=(47400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4682509003578339, var=1.6252770610652112, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F
    Total Standard Deviation in ln(k): 3.732273469565739"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F
Total Standard Deviation in ln(k): 3.732273469565739""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F
Total Standard Deviation in ln(k): 3.732273469565739
""",
)

entry(
    index = 35,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(0.00192603,'m^3/(mol*s)'), n=2.48837, w0=(572500,'J/mol'), E0=(119860,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1164768720954952, var=195.41652430443347, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R
    Total Standard Deviation in ln(k): 30.829702711280895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 30.829702711280895""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 30.829702711280895
""",
)

entry(
    index = 36,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R",
    kinetics = Arrhenius(A=(9.45453e-05,'m^3/(mol*s)'), n=2.81848, Ea=(57.0506,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.35759e-11,'m^3/(mol*s)'), n=4.20212, w0=(572500,'J/mol'), E0=(91079,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1683723626336593, var=0.12620296416805693, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.6477922209241784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.6477922209241784""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.6477922209241784
""",
)

entry(
    index = 38,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(2.50469e-12,'m^3/(mol*s)'), n=4.73863, Ea=(191.908,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(0.0711577,'m^3/(mol*s)'), n=1.78642, w0=(572500,'J/mol'), E0=(115669,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48915167951968164, var=3.504724156362121, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R
    Total Standard Deviation in ln(k): 4.9820705185212395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 4.9820705185212395""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 4.9820705185212395
""",
)

entry(
    index = 40,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R",
    kinetics = Arrhenius(A=(2.25175e-06,'m^3/(mol*s)'), n=3.12644, Ea=(164.45,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(2.91753e-11,'m^3/(mol*s)'), n=3.05655, Ea=(-182.493,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(1.07579e-11,'m^3/(mol*s)'), n=3.237, Ea=(-183.604,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R",
    kinetics = Arrhenius(A=(4.10298e-06,'m^3/(mol*s)'), n=3.07477, Ea=(21.6954,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R",
    kinetics = Arrhenius(A=(1.01799e-05,'m^3/(mol*s)'), n=2.87159, Ea=(40.5376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C",
    kinetics = Arrhenius(A=(2.07011e-05,'m^3/(mol*s)'), n=2.98446, Ea=(43.7961,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C",
    kinetics = Arrhenius(A=(4.81575e-05,'m^3/(mol*s)'), n=2.76922, Ea=(37.8393,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Br",
    kinetics = Arrhenius(A=(0.000145611,'m^3/(mol*s)'), n=2.95653, Ea=(-0.108502,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Br",
    kinetics = Arrhenius(A=(8.68219e-05,'m^3/(mol*s)'), n=2.97056, Ea=(7.89502,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C",
    kinetics = ArrheniusBM(A=(9645.87,'m^3/(mol*s)'), n=0.564784, w0=(572500,'J/mol'), E0=(149811,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15611848611495954, var=296.19122451516154, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C
    Total Standard Deviation in ln(k): 34.89416313767613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C
Total Standard Deviation in ln(k): 34.89416313767613""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C
Total Standard Deviation in ln(k): 34.89416313767613
""",
)

entry(
    index = 50,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C",
    kinetics = Arrhenius(A=(0.00491008,'m^3/(mol*s)'), n=2.38401, Ea=(88.3837,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(3.09714e-11,'m^3/(mol*s)'), n=4.27056, w0=(572500,'J/mol'), E0=(91813.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2128015945113981, var=0.033257769864249, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 3.4128379683690886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 3.4128379683690886""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 3.4128379683690886
""",
)

entry(
    index = 52,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = Arrhenius(A=(3.89377e-10,'m^3/(mol*s)'), n=3.9548, Ea=(119.057,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(3.98222e-05,'m^3/(mol*s)'), n=2.70597, w0=(572500,'J/mol'), E0=(112396,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.589832865664426, var=0.2723554110138554, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 2.5282168837751797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 2.5282168837751797""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 2.5282168837751797
""",
)

entry(
    index = 54,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(0.000352549,'m^3/(mol*s)'), n=2.48352, Ea=(177.184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.2412e-05,'m^3/(mol*s)'), n=3.07293, w0=(572500,'J/mol'), E0=(157072,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33631353739567954, var=705.9390473680345, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 54.10984458091803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 54.10984458091803""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 54.10984458091803
""",
)

entry(
    index = 56,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C",
    kinetics = Arrhenius(A=(3.87031e-05,'m^3/(mol*s)'), n=3.04873, Ea=(22.9526,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = Arrhenius(A=(2.35526e-11,'m^3/(mol*s)'), n=4.30096, Ea=(124.391,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = Arrhenius(A=(4.0727e-11,'m^3/(mol*s)'), n=4.24017, Ea=(124.38,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.64857e-05,'m^3/(mol*s)'), n=2.69436, w0=(572500,'J/mol'), E0=(112934,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5944663503659965, var=0.9376777933368773, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.434894488402427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.434894488402427""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.434894488402427
""",
)

entry(
    index = 60,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2.81961e-05,'m^3/(mol*s)'), n=2.73363, Ea=(177.495,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = Arrhenius(A=(0.00828286,'m^3/(mol*s)'), n=2.34779, Ea=(55.5774,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2.67496e-08,'m^3/(mol*s)'), n=3.75287, Ea=(187.312,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(6.58773e-05,'m^3/(mol*s)'), n=2.61294, Ea=(182.613,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(4.67866e-05,'m^3/(mol*s)'), n=2.73161, Ea=(179.832,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

