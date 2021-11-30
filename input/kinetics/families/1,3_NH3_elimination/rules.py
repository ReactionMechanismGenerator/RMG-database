#!/usr/bin/env python
# encoding: utf-8

name = "1,3_NH3_elimination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.13848e+28,'s^-1'), n=-4.81619, w0=(650125,'J/mol'), E0=(293679,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14582612901420383, var=13.966892144572673, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 4 training reactions at node Root
    Total Standard Deviation in ln(k): 7.858554474439377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 7.858554474439377""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 7.858554474439377
""",
)

entry(
    index = 2,
    label = "Root_Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(1.97485e+10,'s^-1'), n=0.469968, w0=(623000,'J/mol'), E0=(253467,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1154245615347588, var=1.7024423165047282, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Sp-3R!H-2R!H',), comment="""BM rule fitted to 3 training reactions at node Root_Sp-3R!H-2R!H
    Total Standard Deviation in ln(k): 2.905743140982356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 2.905743140982356""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 2.905743140982356
""",
)

entry(
    index = 3,
    label = "Root_N-Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(4.9e+09,'s^-1'), n=1.34, w0=(731500,'J/mol'), E0=(256182,'J/mol'), Tmin=(500,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-Sp-3R!H-2R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-Sp-3R!H-2R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Sp-3R!H-2R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.52e+09,'s^-1'), n=0.95, w0=(595000,'J/mol'), E0=(267575,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-3R!H-2R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Sp-3R!H-2R!H_2R!H->C",
    kinetics = ArrheniusBM(A=(16333.3,'s^-1'), n=2.65, w0=(679000,'J/mol'), E0=(243587,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-3R!H-2R!H_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Sp-3R!H-2R!H_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.13e+08,'s^-1'), n=1.06, w0=(595000,'J/mol'), E0=(249159,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Sp-3R!H-2R!H_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Sp-3R!H-2R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

