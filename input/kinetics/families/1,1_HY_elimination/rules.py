#!/usr/bin/env python
# encoding: utf-8

name = "1,1_HY_elimination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.01775e+16,'s^-1'), n=-0.552278, w0=(625500,'J/mol'), E0=(62550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.030055821259874344, var=8.835877390914995, Tref=1000.0, N=11, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 11 training reactions at node Root
    Total Standard Deviation in ln(k): 6.034633006626597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root
Total Standard Deviation in ln(k): 6.034633006626597""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root
Total Standard Deviation in ln(k): 6.034633006626597
""",
)

entry(
    index = 2,
    label = "HF",
    kinetics = ArrheniusBM(A=(2.09298e+09,'s^-1'), n=1.56845, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1702332965104714, var=7.24337714538659, Tref=1000.0, N=5, data_mean=0.0, correlation='HF',), comment="""BM rule fitted to 5 training reactions at node HF
    Total Standard Deviation in ln(k): 5.823170190612696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node HF
Total Standard Deviation in ln(k): 5.823170190612696""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node HF
Total Standard Deviation in ln(k): 5.823170190612696
""",
)

entry(
    index = 3,
    label = "HCl",
    kinetics = ArrheniusBM(A=(1.39e+15,'s^-1'), n=0, w0=(583000,'J/mol'), E0=(58300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl',), comment="""BM rule fitted to 1 training reactions at node HCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "HBr",
    kinetics = ArrheniusBM(A=(2.29907e+23,'s^-1'), n=-2.52607, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10013405411784822, var=6.993534421097308, Tref=1000.0, N=5, data_mean=0.0, correlation='HBr',), comment="""BM rule fitted to 5 training reactions at node HBr
    Total Standard Deviation in ln(k): 5.55317344943995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node HBr
Total Standard Deviation in ln(k): 5.55317344943995""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node HBr
Total Standard Deviation in ln(k): 5.55317344943995
""",
)

entry(
    index = 5,
    label = "HF_Ext-5R!H!Val7-R",
    kinetics = ArrheniusBM(A=(50840.6,'s^-1'), n=2.9312, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2414035656517986, var=2.2527539567955337, Tref=1000.0, N=3, data_mean=0.0, correlation='HF_Ext-5R!H!Val7-R',), comment="""BM rule fitted to 3 training reactions at node HF_Ext-5R!H!Val7-R
    Total Standard Deviation in ln(k): 3.615483993477693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HF_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 3.615483993477693""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HF_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 3.615483993477693
""",
)

entry(
    index = 6,
    label = "HF_4Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(6.97e+14,'s^-1'), n=0, w0=(730500,'J/mol'), E0=(73050,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_4Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HF_4Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "HF_N-4Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(6.97e+14,'s^-1'), n=0, w0=(730500,'J/mol'), E0=(73050,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-4Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HF_N-4Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_N-4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_N-4Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "HBr_Ext-5R!H!Val7-R",
    kinetics = ArrheniusBM(A=(2.52488e+20,'s^-1'), n=-1.65615, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.053276049217654754, var=3.6527394237177124, Tref=1000.0, N=4, data_mean=0.0, correlation='HBr_Ext-5R!H!Val7-R',), comment="""BM rule fitted to 4 training reactions at node HBr_Ext-5R!H!Val7-R
    Total Standard Deviation in ln(k): 3.9653374128097574"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HBr_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 3.9653374128097574""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HBr_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 3.9653374128097574
""",
)

entry(
    index = 9,
    label = "HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R",
    kinetics = ArrheniusBM(A=(3027.37,'s^-1'), n=3.25992, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.389158083137616, var=0.23186184030221715, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R',), comment="""BM rule fitted to 2 training reactions at node HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
    Total Standard Deviation in ln(k): 9.480793291912889"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 9.480793291912889""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 9.480793291912889
""",
)

entry(
    index = 10,
    label = "HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R",
    kinetics = ArrheniusBM(A=(2.89822e+17,'s^-1'), n=-0.811925, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.27595721114454, var=0.6250625549751672, Tref=1000.0, N=2, data_mean=0.0, correlation='HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R',), comment="""BM rule fitted to 2 training reactions at node HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
    Total Standard Deviation in ln(k): 2.278321376276896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 2.278321376276896""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 2.278321376276896
""",
)

entry(
    index = 11,
    label = "HBr_Ext-5R!H!Val7-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.39e+15,'s^-1'), n=0, w0=(529000,'J/mol'), E0=(52900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_Ext-5R!H!Val7-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node HBr_Ext-5R!H!Val7-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_Ext-5R!H!Val7-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_Ext-5R!H!Val7-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "HBr_Ext-5R!H!Val7-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.39e+15,'s^-1'), n=0, w0=(529000,'J/mol'), E0=(52900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_Ext-5R!H!Val7-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node HBr_Ext-5R!H!Val7-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_Ext-5R!H!Val7-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_Ext-5R!H!Val7-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R",
    kinetics = ArrheniusBM(A=(6.97e+14,'s^-1'), n=0, w0=(730500,'J/mol'), E0=(73050,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R",
    kinetics = ArrheniusBM(A=(1.39e+15,'s^-1'), n=0, w0=(529000,'J/mol'), E0=(52900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R',), comment="""BM rule fitted to 1 training reactions at node HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R_Ext-5R!H!Val7-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

