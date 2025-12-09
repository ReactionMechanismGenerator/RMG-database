#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.35507e+20,'m^3/(mol*s)'), n=-4.94684, w0=(533.238,'kJ/mol'), E0=(165.782,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.411071116334955, var=65.07947200105878, Tref=1000.0, N=42, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 42 training reactions at node Root
    Total Standard Deviation in ln(k): 17.205410519636512"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 17.205410519636512""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 17.205410519636512
""",
)

entry(
    index = 2,
    label = "Root_1R->C",
    kinetics = ArrheniusBM(A=(8.22066e+26,'m^3/(mol*s)'), n=-5.83374, w0=(480.889,'kJ/mol'), E0=(187.022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5114754087067763, var=5.773042380857716, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R->C',), comment="""BM rule fitted to 18 training reactions at node Root_1R->C
    Total Standard Deviation in ln(k): 6.101922389271167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 6.101922389271167""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 6.101922389271167
""",
)

entry(
    index = 3,
    label = "Root_N-1R->C",
    kinetics = ArrheniusBM(A=(14.3926,'m^3/(mol*s)'), n=0.498844, w0=(572.5,'kJ/mol'), E0=(115.688,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14533925510195617, var=66.84774457855417, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->C',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->C
    Total Standard Deviation in ln(k): 16.755982227082395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 16.755982227082395""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 16.755982227082395
""",
)

entry(
    index = 4,
    label = "Root_1R->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(2.65278e+11,'m^3/(mol*s)'), n=-1.63781, w0=(490.417,'kJ/mol'), E0=(146.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13397771223832142, var=5.3258033883552045, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->C_Ext-3R-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->C_Ext-3R-R
    Total Standard Deviation in ln(k): 4.963095328299593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 4.963095328299593""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 4.963095328299593
""",
)

entry(
    index = 5,
    label = "Root_1R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.5716e+09,'m^3/(mol*s)'), n=-0.704858, w0=(474.2,'kJ/mol'), E0=(80.124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0031786026970339956, var=0.5008544564158384, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.4267589343562348"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.4267589343562348""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.4267589343562348
""",
)

entry(
    index = 6,
    label = "Root_1R->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.33384e+09,'m^3/(mol*s)'), n=-0.775738, w0=(480,'kJ/mol'), E0=(86.9429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.031816340694179074, var=0.14337316365077765, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 0.839026452988057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.839026452988057""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.839026452988057
""",
)

entry(
    index = 7,
    label = "Root_1R->C_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(5.61734e+06,'m^3/(mol*s)'), n=-0.137363, w0=(480,'kJ/mol'), E0=(154.984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8057614146062959, var=0.435875967625411, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
    Total Standard Deviation in ln(k): 3.348070374782754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 3.348070374782754""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 3.348070374782754
""",
)

entry(
    index = 8,
    label = "Root_1R->C_N-Sp-2R=1C",
    kinetics = ArrheniusBM(A=(1.52735e+09,'m^3/(mol*s)'), n=-0.643653, w0=(462.5,'kJ/mol'), E0=(86.0387,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-Sp-2R=1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
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
    index = 9,
    label = "Root_N-1R->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(9.20495e-08,'m^3/(mol*s)'), n=2.80526, w0=(572.5,'kJ/mol'), E0=(94.0421,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33821735314084, var=68.45180347157101, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R->C_Ext-3R-R
    Total Standard Deviation in ln(k): 17.436089308940275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 17.436089308940275""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 17.436089308940275
""",
)

entry(
    index = 10,
    label = "Root_1R->C_Ext-3R-R_4R!H->F",
    kinetics = ArrheniusBM(A=(3.57904e-20,'m^3/(mol*s)'), n=7.10843, w0=(498.625,'kJ/mol'), E0=(38.3505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30886754501971014, var=3.774842986878959, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_Ext-3R-R_4R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F
    Total Standard Deviation in ln(k): 4.671039901132235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F
Total Standard Deviation in ln(k): 4.671039901132235""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F
Total Standard Deviation in ln(k): 4.671039901132235
""",
)

entry(
    index = 11,
    label = "Root_1R->C_Ext-3R-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(0.531385,'m^3/(mol*s)'), n=1.91075, w0=(474,'kJ/mol'), E0=(98.7387,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0577200283147992, var=2.936408170988897, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-3R-R_N-4R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-3R-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.5803294046746075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-3R-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.5803294046746075""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-3R-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.5803294046746075
""",
)

entry(
    index = 12,
    label = "Root_1R->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.18e+07,'m^3/(mol*s)'), n=6.19075e-08, w0=(486,'kJ/mol'), E0=(120.542,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
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
    index = 13,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(9.41381e+08,'m^3/(mol*s)'), n=-0.607357, w0=(480,'kJ/mol'), E0=(102.627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8605472268145399, var=0.32011771778424614, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
    Total Standard Deviation in ln(k): 3.296436947119931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 3.296436947119931""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 3.296436947119931
""",
)

entry(
    index = 14,
    label = "Root_1R->C_Ext-1C-R_N-Sp-2R=1C",
    kinetics = ArrheniusBM(A=(4.63231e+09,'m^3/(mol*s)'), n=-0.7664, w0=(462.5,'kJ/mol'), E0=(62.4716,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.531045570523121e-05, var=1.207652770696561, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
    Total Standard Deviation in ln(k): 2.2032829979338837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.2032829979338837""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.2032829979338837
""",
)

entry(
    index = 15,
    label = "Root_1R->C_Ext-2R-R_3R->C",
    kinetics = ArrheniusBM(A=(4.13595e+09,'m^3/(mol*s)'), n=-0.801251, w0=(474,'kJ/mol'), E0=(99.4882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19861665279429036, var=0.00880915275316388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
    Total Standard Deviation in ln(k): 0.6871954103490457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.6871954103490457""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.6871954103490457
""",
)

entry(
    index = 16,
    label = "Root_1R->C_Ext-2R-R_N-3R->C",
    kinetics = ArrheniusBM(A=(5.04518e+06,'m^3/(mol*s)'), n=0.00954463, w0=(486,'kJ/mol'), E0=(139.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0023056586957650605, var=1.6591495532180562, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
    Total Standard Deviation in ln(k): 2.5880518558752854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.5880518558752854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.5880518558752854
""",
)

entry(
    index = 17,
    label = "Root_1R->C_Sp-2R=1C_3R->C",
    kinetics = ArrheniusBM(A=(1.98e+06,'m^3/(mol*s)'), n=-1.90181e-08, w0=(474,'kJ/mol'), E0=(153.806,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
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
    index = 18,
    label = "Root_1R->C_Sp-2R=1C_N-3R->C",
    kinetics = ArrheniusBM(A=(700000,'m^3/(mol*s)'), n=1.22665e-08, w0=(486,'kJ/mol'), E0=(119.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_N-3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
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
    index = 19,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R",
    kinetics = ArrheniusBM(A=(0.54674,'m^3/(mol*s)'), n=0.403578, w0=(572.5,'kJ/mol'), E0=(9.45776,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08935538835671465, var=63.113197024229564, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R
    Total Standard Deviation in ln(k): 16.15089123764743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 16.15089123764743""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 16.15089123764743
""",
)

entry(
    index = 20,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.77682e-10,'m^3/(mol*s)'), n=3.84394, w0=(572.5,'kJ/mol'), E0=(128.58,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4611093498437399, var=66.81098980268217, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 17.544867740977896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R
Total Standard Deviation in ln(k): 17.544867740977896""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R
Total Standard Deviation in ln(k): 17.544867740977896
""",
)

entry(
    index = 21,
    label = "Root_1R->C_Ext-3R-R_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.10298e-06,'m^3/(mol*s)'), n=3.07477, w0=(474,'kJ/mol'), E0=(78.6589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-3R-R_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R->C_Ext-3R-R_4R!H->F_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.01799e-05,'m^3/(mol*s)'), n=2.87159, w0=(474,'kJ/mol'), E0=(101.042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-3R-R_4R!H->F_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R->C_Ext-3R-R_4R!H->F_2R->C",
    kinetics = ArrheniusBM(A=(2.07011e-05,'m^3/(mol*s)'), n=2.98446, w0=(474,'kJ/mol'), E0=(119.563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-3R-R_4R!H->F_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R->C_Ext-3R-R_4R!H->F_N-2R->C",
    kinetics = ArrheniusBM(A=(4.81575e-05,'m^3/(mol*s)'), n=2.76922, w0=(572.5,'kJ/mol'), E0=(109.078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-3R-R_4R!H->F_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_4R!H->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_1R->C_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.000161154,'m^3/(mol*s)'), n=2.94391, w0=(474,'kJ/mol'), E0=(70.9316,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_N-4R!H->F_4BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_1R->C_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br",
    kinetics = ArrheniusBM(A=(8.68219e-05,'m^3/(mol*s)'), n=2.97056, w0=(474,'kJ/mol'), E0=(87.4167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-3R-R_N-4R!H->F_N-4BrCClINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.54e+07,'m^3/(mol*s)'), n=2.10705e-08, w0=(486,'kJ/mol'), E0=(122.419,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
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
    kinetics = ArrheniusBM(A=(4.29568e+09,'m^3/(mol*s)'), n=-0.811807, w0=(462.5,'kJ/mol'), E0=(89.3485,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
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
    kinetics = ArrheniusBM(A=(2.40609e+09,'m^3/(mol*s)'), n=-0.732703, w0=(474,'kJ/mol'), E0=(105.014,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
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
    kinetics = ArrheniusBM(A=(5.13998e+06,'m^3/(mol*s)'), n=0.0486651, w0=(486,'kJ/mol'), E0=(124.125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
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
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O",
    kinetics = ArrheniusBM(A=(3.45714e+18,'m^3/(mol*s)'), n=-6.27931, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7069243995453159, var=7.275329276055336, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O
    Total Standard Deviation in ln(k): 7.183527458959164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O
Total Standard Deviation in ln(k): 7.183527458959164""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O
Total Standard Deviation in ln(k): 7.183527458959164
""",
)

entry(
    index = 32,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(0.000458156,'m^3/(mol*s)'), n=2.90532, w0=(572.5,'kJ/mol'), E0=(92.4916,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7849549160088755, var=166.56885191364628, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O
    Total Standard Deviation in ln(k): 27.845671342759637"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O
Total Standard Deviation in ln(k): 27.845671342759637""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O
Total Standard Deviation in ln(k): 27.845671342759637
""",
)

entry(
    index = 33,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(0.00856188,'m^3/(mol*s)'), n=1.82425, w0=(572.5,'kJ/mol'), E0=(123.821,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6657497022480221, var=14.860106953348003, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 9.400752956801002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 9.400752956801002""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 9.400752956801002
""",
)

entry(
    index = 34,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0954689,'m^3/(mol*s)'), n=1.03371, w0=(572.5,'kJ/mol'), E0=(221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3256000947819442, var=0.2474015388930768, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C
    Total Standard Deviation in ln(k): 1.8152353961984609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C
Total Standard Deviation in ln(k): 1.8152353961984609""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C
Total Standard Deviation in ln(k): 1.8152353961984609
""",
)

entry(
    index = 35,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0399565,'m^3/(mol*s)'), n=0.942842, w0=(572.5,'kJ/mol'), E0=(189.932,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3932036013092655, var=0.009179124962109295, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C
    Total Standard Deviation in ln(k): 1.1800179041408267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.1800179041408267""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.1800179041408267
""",
)

entry(
    index = 36,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.68662e+22,'m^3/(mol*s)'), n=-7.26865, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8269667660443971, var=0.3464181891450105, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.2577389053685355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.2577389053685355""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.2577389053685355
""",
)

entry(
    index = 37,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-4O-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.1217e+13,'m^3/(mol*s)'), n=-4.90461, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-4O-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-4O-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-4O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-4O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C",
    kinetics = ArrheniusBM(A=(2.41542e-05,'m^3/(mol*s)'), n=3.34676, w0=(572.5,'kJ/mol'), E0=(93.4291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.547101108649816, var=279.6621939467631, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C
    Total Standard Deviation in ln(k): 34.90001828677636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C
Total Standard Deviation in ln(k): 34.90001828677636""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C
Total Standard Deviation in ln(k): 34.90001828677636
""",
)

entry(
    index = 39,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4CF->C",
    kinetics = ArrheniusBM(A=(0.00477623,'m^3/(mol*s)'), n=2.38781, w0=(572.5,'kJ/mol'), E0=(83.097,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O",
    kinetics = ArrheniusBM(A=(5.94726e-18,'m^3/(mol*s)'), n=5.99013, w0=(572.5,'kJ/mol'), E0=(92.6681,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1719186220149367, var=17.98944585862287, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O
    Total Standard Deviation in ln(k): 13.959958680936797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 13.959958680936797""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 13.959958680936797
""",
)

entry(
    index = 41,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.078767,'m^3/(mol*s)'), n=1.76958, w0=(572.5,'kJ/mol'), E0=(115.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48443360083063847, var=3.50537854212211, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O
    Total Standard Deviation in ln(k): 4.970566408746826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.970566408746826""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.970566408746826
""",
)

entry(
    index = 42,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0109819,'m^3/(mol*s)'), n=1.36153, w0=(572.5,'kJ/mol'), E0=(223.66,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.00912799,'m^3/(mol*s)'), n=1.12396, w0=(572.5,'kJ/mol'), E0=(187.909,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.15657e+22,'m^3/(mol*s)'), n=-7.27714, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8117256661589868, var=0.30060699169244115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 3.138660620277749"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 3.138660620277749""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 3.138660620277749
""",
)

entry(
    index = 45,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.03164e+22,'m^3/(mol*s)'), n=-7.25167, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(282.198,'m^3/(mol*s)'), n=1.44131, w0=(572.5,'kJ/mol'), E0=(127.62,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03121091162125639, var=890.7517446171922, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 59.91066873842166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 59.91066873842166""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 59.91066873842166
""",
)

entry(
    index = 47,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.7648e-05,'m^3/(mol*s)'), n=3.05252, w0=(572.5,'kJ/mol'), E0=(64.5877,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(8.2559e-37,'m^3/(mol*s)'), n=11.144, w0=(572.5,'kJ/mol'), E0=(-27.8831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.2569990942416376, var=27.246639015118088, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R
    Total Standard Deviation in ln(k): 16.135230941992813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R
Total Standard Deviation in ln(k): 16.135230941992813""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R
Total Standard Deviation in ln(k): 16.135230941992813
""",
)

entry(
    index = 49,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.69865e-12,'m^3/(mol*s)'), n=4.74744, w0=(572.5,'kJ/mol'), E0=(126.731,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C",
    kinetics = ArrheniusBM(A=(4.41807e-05,'m^3/(mol*s)'), n=2.68884, w0=(572.5,'kJ/mol'), E0=(112.649,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5851058560977576, var=0.2723401435687425, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C
    Total Standard Deviation in ln(k): 2.5163106507603277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C
Total Standard Deviation in ln(k): 2.5163106507603277""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C
Total Standard Deviation in ln(k): 2.5163106507603277
""",
)

entry(
    index = 51,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_N-5CF->C",
    kinetics = ArrheniusBM(A=(0.000391103,'m^3/(mol*s)'), n=2.46641, w0=(572.5,'kJ/mol'), E0=(92.6683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_N-5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_N-5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(2.08478e+22,'m^3/(mol*s)'), n=-7.30073, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.23082e+22,'m^3/(mol*s)'), n=-7.25355, w0=(572.5,'kJ/mol'), E0=(5.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_4R!H->O_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(774488,'m^3/(mol*s)'), n=0.652409, w0=(572.5,'kJ/mol'), E0=(22.0859,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.74781e-06,'m^3/(mol*s)'), n=3.54047, w0=(572.5,'kJ/mol'), E0=(185.914,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-3R-R_N-4R!H->O_4CF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(5.64807e-09,'m^3/(mol*s)'), n=2.90926, w0=(572.5,'kJ/mol'), E0=(109.527,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6677089291438637, var=0.0332992986148678, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 2.043486595661105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 2.043486595661105""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 2.043486595661105
""",
)

entry(
    index = 57,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.07952e-10,'m^3/(mol*s)'), n=4.09873, w0=(572.5,'kJ/mol'), E0=(90.4318,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.15733e-05,'m^3/(mol*s)'), n=2.67724, w0=(572.5,'kJ/mol'), E0=(113.187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5885194367825252, var=0.9375920901136175, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.4198637773902503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4198637773902503""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4198637773902503
""",
)

entry(
    index = 59,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.12796e-05,'m^3/(mol*s)'), n=2.71651, w0=(572.5,'kJ/mol'), E0=(111.534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(4.30764e-09,'m^3/(mol*s)'), n=2.93926, w0=(572.5,'kJ/mol'), E0=(109.534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(7.4056e-09,'m^3/(mol*s)'), n=2.87926, w0=(572.5,'kJ/mol'), E0=(109.519,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_5R!H->O_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(7.30815e-05,'m^3/(mol*s)'), n=2.59582, w0=(572.5,'kJ/mol'), E0=(114.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(5.1903e-05,'m^3/(mol*s)'), n=2.71449, w0=(572.5,'kJ/mol'), E0=(112.538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C_Ext-3R-R_Ext-2R-R_Ext-2R-R_N-5R!H->O_5CF->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

