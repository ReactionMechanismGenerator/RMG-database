#!/usr/bin/env python
# encoding: utf-8

name = "amide_alcoholysis/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.16851e-28,'cm^3/(mol*s)'), n=10.8636, w0=(754000,'J/mol'), E0=(-9701.51,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6599999694238405, var=14.540178389964264, Tref=1000.0, N=6, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 9.302664150322693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 9.302664150322693""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 9.302664150322693
""",
)

entry(
    index = 2,
    label = "Root_6R->C",
    kinetics = ArrheniusBM(A=(4519.42,'cm^3/(mol*s)'), n=0.695918, w0=(754000,'J/mol'), E0=(45910.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05767765801675886, var=1.0206316576672756, Tref=1000.0, N=2, correlation='Root_6R->C',), comment="""BM rule fitted to 2 training reactions at node Root_6R->C
    Total Standard Deviation in ln(k): 2.170228738159957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6R->C
Total Standard Deviation in ln(k): 2.170228738159957""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6R->C
Total Standard Deviation in ln(k): 2.170228738159957
""",
)

entry(
    index = 3,
    label = "Root_N-6R->C",
    kinetics = ArrheniusBM(A=(1.32528e-24,'cm^3/(mol*s)'), n=10.0951, w0=(754000,'J/mol'), E0=(-9405.88,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9414305595600523, var=29.13997483576673, Tref=1000.0, N=4, correlation='Root_N-6R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-6R->C
    Total Standard Deviation in ln(k): 13.187255052075335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6R->C
Total Standard Deviation in ln(k): 13.187255052075335""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6R->C
Total Standard Deviation in ln(k): 13.187255052075335
""",
)

entry(
    index = 4,
    label = "Root_6R->C_Ext-4R-R",
    kinetics = ArrheniusBM(A=(0.636073e+6,'cm^3/(mol*s)'), n=0.680875, w0=(754000,'J/mol'), E0=(84756.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_6R->C_Ext-4R-R',), comment="""BM rule fitted to 2 training reactions at node Root_6R->C_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6R->C_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6R->C_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-6R->C_4R-inRing",
    kinetics = ArrheniusBM(A=(495.477e+6,'cm^3/(mol*s)'), n=-0.144487, w0=(754000,'J/mol'), E0=(94192.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-6R->C_4R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-6R->C_4R-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6R->C_4R-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6R->C_4R-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-6R->C_N-4R-inRing",
    kinetics = ArrheniusBM(A=(1.43709e+14,'cm^3/(mol*s)'), n=-0.961865, w0=(754000,'J/mol'), E0=(76687.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.028202313520198023, var=2.246286802917813, Tref=1000.0, N=3, correlation='Root_N-6R->C_N-4R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-6R->C_N-4R-inRing
    Total Standard Deviation in ln(k): 3.0754803502482617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6R->C_N-4R-inRing
Total Standard Deviation in ln(k): 3.0754803502482617""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6R->C_N-4R-inRing
Total Standard Deviation in ln(k): 3.0754803502482617
""",
)

entry(
    index = 7,
    label = "Root_N-6R->C_N-4R-inRing_Ext-4R-R",
    kinetics = ArrheniusBM(A=(1.02563e+14,'cm^3/(mol*s)'), n=-0.968276, w0=(754000,'J/mol'), E0=(76647.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.027473811164184667, var=4.566608003521137, Tref=1000.0, N=2, correlation='Root_N-6R->C_N-4R-inRing_Ext-4R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-6R->C_N-4R-inRing_Ext-4R-R
    Total Standard Deviation in ln(k): 4.3530730200399566"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6R->C_N-4R-inRing_Ext-4R-R
Total Standard Deviation in ln(k): 4.3530730200399566""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6R->C_N-4R-inRing_Ext-4R-R
Total Standard Deviation in ln(k): 4.3530730200399566
""",
)

entry(
    index = 8,
    label = "Root_N-6R->C_N-4R-inRing_Ext-4R-R_Ext-10R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(6.47185e+14,'cm^3/(mol*s)'), n=-0.965789, w0=(754000,'J/mol'), E0=(85833.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-6R->C_N-4R-inRing_Ext-4R-R_Ext-10R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-6R->C_N-4R-inRing_Ext-4R-R_Ext-10R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6R->C_N-4R-inRing_Ext-4R-R_Ext-10R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6R->C_N-4R-inRing_Ext-4R-R_Ext-10R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

