#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.32437e+15,'m^3/(mol*s)'), n=-2.51852, w0=(581040,'J/mol'), E0=(243177,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.547224988398209, var=123.64786272273753, Tref=1000.0, N=63, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 63 training reactions at node Root
    Total Standard Deviation in ln(k): 23.667001933128063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 63 training reactions at node Root
Total Standard Deviation in ln(k): 23.667001933128063""",
    longDesc = 
"""
BM rule fitted to 63 training reactions at node Root
Total Standard Deviation in ln(k): 23.667001933128063
""",
)

entry(
    index = 2,
    label = "HH",
    kinetics = ArrheniusBM(A=(1.85953e-16,'m^3/(mol*s)'), n=6.55366, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3889956320740039, var=125.81479234121664, Tref=1000.0, N=4, data_mean=0.0, correlation='HH',), comment="""BM rule fitted to 4 training reactions at node HH
    Total Standard Deviation in ln(k): 23.463926637429502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HH
Total Standard Deviation in ln(k): 23.463926637429502""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HH
Total Standard Deviation in ln(k): 23.463926637429502
""",
)

entry(
    index = 3,
    label = "HY",
    kinetics = ArrheniusBM(A=(9.07699e+10,'m^3/(mol*s)'), n=-1.32182, w0=(617447,'J/mol'), E0=(133140,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38011123549485737, var=17.951257233626407, Tref=1000.0, N=19, data_mean=0.0, correlation='HY',), comment="""BM rule fitted to 19 training reactions at node HY
    Total Standard Deviation in ln(k): 9.448900174723416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node HY
Total Standard Deviation in ln(k): 9.448900174723416""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node HY
Total Standard Deviation in ln(k): 9.448900174723416
""",
)

entry(
    index = 4,
    label = "YY",
    kinetics = ArrheniusBM(A=(0.237593,'m^3/(mol*s)'), n=1.46393, w0=(424667,'J/mol'), E0=(42466.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14462199176476542, var=52.55527556127668, Tref=1000.0, N=3, data_mean=0.0, correlation='YY',), comment="""BM rule fitted to 3 training reactions at node YY
    Total Standard Deviation in ln(k): 14.896702281890803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node YY
Total Standard Deviation in ln(k): 14.896702281890803""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node YY
Total Standard Deviation in ln(k): 14.896702281890803
""",
)

entry(
    index = 5,
    label = "CH",
    kinetics = ArrheniusBM(A=(3.84636e+45,'m^3/(mol*s)'), n=-11.245, w0=(584000,'J/mol'), E0=(304940,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.8351197672194188, var=25.940135796921076, Tref=1000.0, N=19, data_mean=0.0, correlation='CH',), comment="""BM rule fitted to 19 training reactions at node CH
    Total Standard Deviation in ln(k): 14.821262052106135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node CH
Total Standard Deviation in ln(k): 14.821262052106135""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node CH
Total Standard Deviation in ln(k): 14.821262052106135
""",
)

entry(
    index = 6,
    label = "CH2_CH",
    kinetics = ArrheniusBM(A=(1.58681e+07,'m^3/(mol*s)'), n=-0.243277, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05953456777347124, var=0.11016045087362174, Tref=1000.0, N=12, data_mean=0.0, correlation='CH2_CH',), comment="""BM rule fitted to 12 training reactions at node CH2_CH
    Total Standard Deviation in ln(k): 0.814964492962345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node CH2_CH
Total Standard Deviation in ln(k): 0.814964492962345""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node CH2_CH
Total Standard Deviation in ln(k): 0.814964492962345
""",
)

entry(
    index = 7,
    label = "CHY_CH",
    kinetics = ArrheniusBM(A=(2.79958e-05,'m^3/(mol*s)'), n=3.10993, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_CH',), comment="""BM rule fitted to 1 training reactions at node CHY_CH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_CH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_CH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "CYY_CH",
    kinetics = ArrheniusBM(A=(45917.4,'m^3/(mol*s)'), n=0.490915, w0=(584000,'J/mol'), E0=(232843,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7603451701127985, var=33.5155086634446, Tref=1000.0, N=3, data_mean=0.0, correlation='CYY_CH',), comment="""BM rule fitted to 3 training reactions at node CYY_CH
    Total Standard Deviation in ln(k): 13.516343666843827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CYY_CH
Total Standard Deviation in ln(k): 13.516343666843827""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CYY_CH
Total Standard Deviation in ln(k): 13.516343666843827
""",
)

entry(
    index = 9,
    label = "CY",
    kinetics = ArrheniusBM(A=(2.52583e+17,'m^3/(mol*s)'), n=-3.08088, w0=(555714,'J/mol'), E0=(382995,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1324658113820543, var=32.82826857577086, Tref=1000.0, N=7, data_mean=0.0, correlation='CY',), comment="""BM rule fitted to 7 training reactions at node CY
    Total Standard Deviation in ln(k): 14.33171326067386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node CY
Total Standard Deviation in ln(k): 14.33171326067386""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node CY
Total Standard Deviation in ln(k): 14.33171326067386
""",
)

entry(
    index = 10,
    label = "CHY_CY",
    kinetics = ArrheniusBM(A=(4.50792e-57,'m^3/(mol*s)'), n=17.955, w0=(538667,'J/mol'), E0=(53866.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4542348587393783, var=3.3697179772238393, Tref=1000.0, N=3, data_mean=0.0, correlation='CHY_CY',), comment="""BM rule fitted to 3 training reactions at node CHY_CY
    Total Standard Deviation in ln(k): 7.333906831212735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CHY_CY
Total Standard Deviation in ln(k): 7.333906831212735""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CHY_CY
Total Standard Deviation in ln(k): 7.333906831212735
""",
)

entry(
    index = 11,
    label = "CYY_CY",
    kinetics = ArrheniusBM(A=(0.0173668,'m^3/(mol*s)'), n=2.38455, w0=(568500,'J/mol'), E0=(352505,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2609585315720448, var=21.262793782870972, Tref=1000.0, N=4, data_mean=0.0, correlation='CYY_CY',), comment="""BM rule fitted to 4 training reactions at node CYY_CY
    Total Standard Deviation in ln(k): 9.89982830136085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CYY_CY
Total Standard Deviation in ln(k): 9.89982830136085""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CYY_CY
Total Standard Deviation in ln(k): 9.89982830136085
""",
)

entry(
    index = 12,
    label = "CYY_CY_Ext-4Cs-R",
    kinetics = ArrheniusBM(A=(1.33582e-06,'m^3/(mol*s)'), n=3.3552, w0=(658000,'J/mol'), E0=(369109,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_CY_Ext-4Cs-R',), comment="""BM rule fitted to 1 training reactions at node CYY_CY_Ext-4Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_CY_Ext-4Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_CY_Ext-4Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "OHOY",
    kinetics = ArrheniusBM(A=(1.00227e+09,'m^3/(mol*s)'), n=-0.847987, w0=(614000,'J/mol'), E0=(195600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3622830447933867, var=16.21740296898308, Tref=1000.0, N=4, data_mean=0.0, correlation='OHOY',), comment="""BM rule fitted to 4 training reactions at node OHOY
    Total Standard Deviation in ln(k): 8.98349482022512"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node OHOY
Total Standard Deviation in ln(k): 8.98349482022512""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node OHOY
Total Standard Deviation in ln(k): 8.98349482022512
""",
)

entry(
    index = 14,
    label = "OH",
    kinetics = ArrheniusBM(A=(1.00227e+09,'m^3/(mol*s)'), n=-0.847987, w0=(614000,'J/mol'), E0=(195600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3622830447933867, var=16.21740296898308, Tref=1000.0, N=4, data_mean=0.0, correlation='OH',), comment="""BM rule fitted to 4 training reactions at node OH
    Total Standard Deviation in ln(k): 8.98349482022512"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node OH
Total Standard Deviation in ln(k): 8.98349482022512""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node OH
Total Standard Deviation in ln(k): 8.98349482022512
""",
)

entry(
    index = 15,
    label = "CHY_OH",
    kinetics = ArrheniusBM(A=(4.67448e-06,'m^3/(mol*s)'), n=3.15288, w0=(614000,'J/mol'), E0=(61400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_OH',), comment="""BM rule fitted to 1 training reactions at node CHY_OH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_OH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_OH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "CYY_OH",
    kinetics = ArrheniusBM(A=(4.45944e-07,'m^3/(mol*s)'), n=3.5554, w0=(614000,'J/mol'), E0=(162917,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09019050907694896, var=10.107947307952784, Tref=1000.0, N=3, data_mean=0.0, correlation='CYY_OH',), comment="""BM rule fitted to 3 training reactions at node CYY_OH
    Total Standard Deviation in ln(k): 6.600263178172934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CYY_OH
Total Standard Deviation in ln(k): 6.600263178172934""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CYY_OH
Total Standard Deviation in ln(k): 6.600263178172934
""",
)

entry(
    index = 17,
    label = "CC",
    kinetics = ArrheniusBM(A=(1.29472e-98,'m^3/(mol*s)'), n=29.6992, w0=(519000,'J/mol'), E0=(51900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.617196854003732, var=273.5046730356107, Tref=1000.0, N=3, data_mean=0.0, correlation='CC',), comment="""BM rule fitted to 3 training reactions at node CC
    Total Standard Deviation in ln(k): 39.73013347426121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CC
Total Standard Deviation in ln(k): 39.73013347426121""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CC
Total Standard Deviation in ln(k): 39.73013347426121
""",
)

entry(
    index = 18,
    label = "CH2_CC",
    kinetics = ArrheniusBM(A=(0.000166864,'m^3/(mol*s)'), n=2.82973, w0=(519000,'J/mol'), E0=(51900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CC',), comment="""BM rule fitted to 1 training reactions at node CH2_CC
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CC
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CC
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "CHY_CC",
    kinetics = ArrheniusBM(A=(5.7066e-06,'m^3/(mol*s)'), n=3.19155, w0=(519000,'J/mol'), E0=(51900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_CC',), comment="""BM rule fitted to 1 training reactions at node CHY_CC
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_CC
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_CC
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "CYY_CC",
    kinetics = ArrheniusBM(A=(2.22791e-07,'m^3/(mol*s)'), n=3.59921, w0=(519000,'J/mol'), E0=(51900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_CC',), comment="""BM rule fitted to 1 training reactions at node CYY_CC
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_CC
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_CC
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "CO",
    kinetics = ArrheniusBM(A=(1.92463e-53,'m^3/(mol*s)'), n=16.5647, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3154740796436606, var=136.01308652924484, Tref=1000.0, N=3, data_mean=0.0, correlation='CO',), comment="""BM rule fitted to 3 training reactions at node CO
    Total Standard Deviation in ln(k): 26.685363642100636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CO
Total Standard Deviation in ln(k): 26.685363642100636""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CO
Total Standard Deviation in ln(k): 26.685363642100636
""",
)

entry(
    index = 22,
    label = "CH2_CO",
    kinetics = ArrheniusBM(A=(1.26474e-05,'m^3/(mol*s)'), n=2.95311, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CO',), comment="""BM rule fitted to 1 training reactions at node CH2_CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "CHY_CO",
    kinetics = ArrheniusBM(A=(2.12553e-07,'m^3/(mol*s)'), n=3.34134, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_CO',), comment="""BM rule fitted to 1 training reactions at node CHY_CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "CYY_CO",
    kinetics = ArrheniusBM(A=(1.40908e-07,'m^3/(mol*s)'), n=3.45227, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_CO',), comment="""BM rule fitted to 1 training reactions at node CYY_CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "HH_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(0.00032606,'m^3/(mol*s)'), n=3.11135, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10463897713665615, var=0.6358584887392338, Tref=1000.0, N=3, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 3 training reactions at node HH_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 1.8615024970529013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HH_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 1.8615024970529013""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HH_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 1.8615024970529013
""",
)

entry(
    index = 26,
    label = "HH_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(3.26413e-09,'m^3/(mol*s)'), n=4.30786, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HH_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node HH_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HH_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HH_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.08523e+18,'m^3/(mol*s)'), n=-3.46325, w0=(643250,'J/mol'), E0=(191060,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1921533901605716, var=87.59229344044181, Tref=1000.0, N=4, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 4 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 21.757827140691447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 21.757827140691447""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 21.757827140691447
""",
)

entry(
    index = 28,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(332.98,'m^3/(mol*s)'), n=1.07974, w0=(610567,'J/mol'), E0=(48870.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03930933841998634, var=11.710598823356426, Tref=1000.0, N=15, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 15 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 6.959121416495342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 6.959121416495342""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 6.959121416495342
""",
)

entry(
    index = 29,
    label = "YY_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.32908,'m^3/(mol*s)'), n=0.754387, w0=(413500,'J/mol'), E0=(41350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.790053776114707, var=13.22217186464956, Tref=1000.0, N=2, data_mean=0.0, correlation='YY_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 9.27473846583569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 9.27473846583569""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 9.27473846583569
""",
)

entry(
    index = 30,
    label = "YY_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(447000,'J/mol'), E0=(44700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='YY_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node YY_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node YY_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node YY_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "CH_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(3.33873e-07,'m^3/(mol*s)'), n=3.38172, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CH_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "CH_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.57099e-21,'m^3/(mol*s)'), n=7.5385, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.554751041316875, var=0.2040317110632598, Tref=1000.0, N=2, data_mean=0.0, correlation='CH_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node CH_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 12.349634312037441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 12.349634312037441""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 12.349634312037441
""",
)

entry(
    index = 33,
    label = "CH2_CH_4CbCdCsCt->Cs",
    kinetics = ArrheniusBM(A=(1.11076e+06,'m^3/(mol*s)'), n=0.0902065, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02978136207648571, var=0.07202623469935532, Tref=1000.0, N=3, data_mean=0.0, correlation='CH2_CH_4CbCdCsCt->Cs',), comment="""BM rule fitted to 3 training reactions at node CH2_CH_4CbCdCsCt->Cs
    Total Standard Deviation in ln(k): 0.6128524056002446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CH2_CH_4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.6128524056002446""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CH2_CH_4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.6128524056002446
""",
)

entry(
    index = 34,
    label = "CH2_CH_N-4CbCdCsCt->Cs",
    kinetics = ArrheniusBM(A=(3.85029e+07,'m^3/(mol*s)'), n=-0.354438, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0694522983922838, var=0.08248921948283036, Tref=1000.0, N=9, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs',), comment="""BM rule fitted to 9 training reactions at node CH2_CH_N-4CbCdCsCt->Cs
    Total Standard Deviation in ln(k): 0.7502819513493225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node CH2_CH_N-4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.7502819513493225""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node CH2_CH_N-4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.7502819513493225
""",
)

entry(
    index = 35,
    label = "CYY_CH_2Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(6.68018e-11,'m^3/(mol*s)'), n=4.72997, w0=(584000,'J/mol'), E0=(227703,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_CH_2Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CYY_CH_2Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_CH_2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_CH_2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "CYY_CH_N-2Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(5.62317e-34,'m^3/(mol*s)'), n=11.2536, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.048899557302017, var=0.5469008688921847, Tref=1000.0, N=2, data_mean=0.0, correlation='CYY_CH_N-2Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node CYY_CH_N-2Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 21.705922368126018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CYY_CH_N-2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 21.705922368126018""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CYY_CH_N-2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 21.705922368126018
""",
)

entry(
    index = 37,
    label = "CHY_CY_5Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(3.01249e-05,'m^3/(mol*s)'), n=3.17037, w0=(458000,'J/mol'), E0=(45800,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_CY_5Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node CHY_CY_5Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_CY_5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_CY_5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "CHY_CY_N-5Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(1.01273e-58,'m^3/(mol*s)'), n=18.4103, w0=(579000,'J/mol'), E0=(57900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=15.859515793666755, var=1.7645188631816184, Tref=1000.0, N=2, data_mean=0.0, correlation='CHY_CY_N-5Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node CHY_CY_N-5Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 42.51102335151977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CHY_CY_N-5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 42.51102335151977""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CHY_CY_N-5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 42.51102335151977
""",
)

entry(
    index = 39,
    label = "CYY_CY_5Br1sCl1sF1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.42311e-06,'m^3/(mol*s)'), n=3.42841, w0=(500000,'J/mol'), E0=(50000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_CY_5Br1sCl1sF1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CYY_CY_5Br1sCl1sF1sI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_CY_5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_CY_5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.23588e-87,'m^3/(mol*s)'), n=26.6746, w0=(558000,'J/mol'), E0=(55800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=24.234824459427724, var=0.31418087963789393, Tref=1000.0, N=2, data_mean=0.0, correlation='CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s
    Total Standard Deviation in ln(k): 62.015209645470385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 62.015209645470385""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 62.015209645470385
""",
)

entry(
    index = 41,
    label = "CYY_OH_2Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(1.76395e-12,'m^3/(mol*s)'), n=5.02686, w0=(614000,'J/mol'), E0=(165851,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_OH_2Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CYY_OH_2Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_OH_2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_OH_2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "CYY_OH_N-2Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(1.3004e-09,'m^3/(mol*s)'), n=4.2889, w0=(614000,'J/mol'), E0=(143815,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.827606888873764, var=17.099167872578207, Tref=1000.0, N=2, data_mean=0.0, correlation='CYY_OH_N-2Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node CYY_OH_N-2Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 15.394348025907975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CYY_OH_N-2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 15.394348025907975""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CYY_OH_N-2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 15.394348025907975
""",
)

entry(
    index = 43,
    label = "HH_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->Br1s",
    kinetics = ArrheniusBM(A=(1.50896,'m^3/(mol*s)'), n=2.11145, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s",
    kinetics = ArrheniusBM(A=(0.000143772,'m^3/(mol*s)'), n=3.189, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2216614596813846, var=0.3883872655048153, Tref=1000.0, N=2, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s
    Total Standard Deviation in ln(k): 4.318866571931314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s
Total Standard Deviation in ln(k): 4.318866571931314""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s
Total Standard Deviation in ln(k): 4.318866571931314
""",
)

entry(
    index = 45,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.479e-26,'m^3/(mol*s)'), n=9.07073, w0=(614167,'J/mol'), E0=(45044.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.9956066514669297, var=43.49109305419067, Tref=1000.0, N=3, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 3 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 20.747432082412942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 20.747432082412942""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 20.747432082412942
""",
)

entry(
    index = 46,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(0.00948844,'m^3/(mol*s)'), n=2.40423, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(5.70102e+07,'m^3/(mol*s)'), n=-0.281212, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18464146808422008, var=5.903103286997895, Tref=1000.0, N=6, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 6 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 5.334688329728893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 5.334688329728893""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 5.334688329728893
""",
)

entry(
    index = 48,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(0.0265635,'m^3/(mol*s)'), n=2.14784, w0=(664944,'J/mol'), E0=(76437.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1561957903190938, var=8.50925982117968, Tref=1000.0, N=9, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 9 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 6.240391378973565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 6.240391378973565""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 6.240391378973565
""",
)

entry(
    index = 49,
    label = "YY_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(321,'m^3/(mol*s)'), n=0, w0=(447000,'J/mol'), E0=(44700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='YY_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "YY_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(3200,'m^3/(mol*s)'), n=0, w0=(380000,'J/mol'), E0=(38000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='YY_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "CH_N-2Br1sCl1sF1sHI1s->F1s_2Br1sCl1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.24049e-06,'m^3/(mol*s)'), n=3.20888, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-2Br1sCl1sF1sHI1s->F1s_2Br1sCl1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-2Br1sCl1sF1sHI1s->F1s_2Br1sCl1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_N-2Br1sCl1sF1sHI1s->F1s_2Br1sCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_N-2Br1sCl1sF1sHI1s->F1s_2Br1sCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "CH_N-2Br1sCl1sF1sHI1s->F1s_N-2Br1sCl1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.9253e-06,'m^3/(mol*s)'), n=3.16987, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-2Br1sCl1sF1sHI1s->F1s_N-2Br1sCl1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-2Br1sCl1sF1sHI1s->F1s_N-2Br1sCl1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_N-2Br1sCl1sF1sHI1s->F1s_N-2Br1sCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_N-2Br1sCl1sF1sHI1s->F1s_N-2Br1sCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.23333e+06,'m^3/(mol*s)'), n=-0.146, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(471473,'m^3/(mol*s)'), n=0.207628, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47428387515166337, var=0.06288991772562845, Tref=1000.0, N=2, data_mean=0.0, correlation='CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.6944127300954472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472
""",
)

entry(
    index = 55,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(8.57441e+07,'m^3/(mol*s)'), n=-0.461477, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07735060340980143, var=0.030918885319345182, Tref=1000.0, N=6, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.5468561897805673"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5468561897805673""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5468561897805673
""",
)

entry(
    index = 56,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R",
    kinetics = ArrheniusBM(A=(2.13e+07,'m^3/(mol*s)'), n=-0.274, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "CH2_CH_N-4CbCdCsCt->Cs_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.325e+06,'m^3/(mol*s)'), n=0.0073, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "CH2_CH_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(33.15,'m^3/(mol*s)'), n=1.475, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "CYY_CH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.3398e-07,'m^3/(mol*s)'), n=3.60759, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_CH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CYY_CH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_CH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_CH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "CYY_CH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(5.49685e-07,'m^3/(mol*s)'), n=3.52855, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_CH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CYY_CH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_CH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_CH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(4.96165e-06,'m^3/(mol*s)'), n=3.30609, w0=(658000,'J/mol'), E0=(65800,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(1.78425e-05,'m^3/(mol*s)'), n=3.22746, w0=(500000,'J/mol'), E0=(50000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CHY_CY_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(6.158e-07,'m^3/(mol*s)'), n=3.54561, w0=(658000,'J/mol'), E0=(65800,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(7.43831e-06,'m^3/(mol*s)'), n=3.35156, w0=(458000,'J/mol'), E0=(45800,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_CY_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "CYY_OH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.23355e-09,'m^3/(mol*s)'), n=4.16722, w0=(614000,'J/mol'), E0=(141218,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_OH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CYY_OH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_OH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_OH_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "CYY_OH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.67626e-09,'m^3/(mol*s)'), n=4.20006, w0=(614000,'J/mol'), E0=(61400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CYY_OH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CYY_OH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CYY_OH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CYY_OH_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_3Cl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(2.13948,'m^3/(mol*s)'), n=1.96174, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_3Cl1sF1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_3Cl1sF1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_3Cl1sF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_3Cl1sF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_N-3Cl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(1.39739,'m^3/(mol*s)'), n=2.08325, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_N-3Cl1sF1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_N-3Cl1sF1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_N-3Cl1sF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_N-3Cl1sF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(3.98081e-09,'m^3/(mol*s)'), n=4.16158, w0=(730500,'J/mol'), E0=(145905,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(52.2138,'m^3/(mol*s)'), n=0.987889, w0=(556000,'J/mol'), E0=(102880,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004804305618508648, var=1.6958898219066687, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 2.6227641290455677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 2.6227641290455677""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 2.6227641290455677
""",
)

entry(
    index = 71,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(165146,'m^3/(mol*s)'), n=0.445034, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11710514359669284, var=1.9140851116918103, Tref=1000.0, N=4, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 4 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 3.0677943271948247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.0677943271948247""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.0677943271948247
""",
)

entry(
    index = 72,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(61.0758,'m^3/(mol*s)'), n=1.42287, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(52.5907,'m^3/(mol*s)'), n=-0.0213628, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=11.638043888421807, var=195.265202462764, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 57.25494818542244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 57.25494818542244""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 57.25494818542244
""",
)

entry(
    index = 75,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(0.0115339,'m^3/(mol*s)'), n=2.29312, w0=(688357,'J/mol'), E0=(77028.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08112660736719177, var=7.762576913865359, Tref=1000.0, N=7, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 7 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 5.789308578381027"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 5.789308578381027""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 5.789308578381027
""",
)

entry(
    index = 76,
    label = "CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4933.33,'m^3/(mol*s)'), n=0.797, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_4CbCdCsCt->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(36700,'m^3/(mol*s)'), n=0.498, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(1.03751e+08,'m^3/(mol*s)'), n=-0.484428, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07613065074427958, var=0.029144243287908624, Tref=1000.0, N=5, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 5 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
    Total Standard Deviation in ln(k): 0.533525101999015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.533525101999015""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.533525101999015
""",
)

entry(
    index = 79,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.53881,'m^3/(mol*s)'), n=1.26919, w0=(583000,'J/mol'), E0=(96168.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_4Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_N-4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(214000,'m^3/(mol*s)'), n=0, w0=(529000,'J/mol'), E0=(113414,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_N-4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_N-4Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_N-4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_N-4Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.92494,'m^3/(mol*s)'), n=1.71005, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1350.13,'m^3/(mol*s)'), n=1.06085, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05364678948243505, var=0.19250121228432304, Tref=1000.0, N=3, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.0143676434519715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.0143676434519715""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.0143676434519715
""",
)

entry(
    index = 83,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.33736e+17,'m^3/(mol*s)'), n=-4.54388, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(8.68414e-08,'m^3/(mol*s)'), n=3.75516, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25384183722262, var=2.644784618624256, Tref=1000.0, N=3, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 3.898052877624122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.898052877624122""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.898052877624122
""",
)

entry(
    index = 86,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.88449e+06,'m^3/(mol*s)'), n=-0.0756572, w0=(656750,'J/mol'), E0=(65675,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3761948964338802, var=0.059028709504851846, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 3.9448430406391615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.9448430406391615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 3.9448430406391615
""",
)

entry(
    index = 87,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.0178297,'m^3/(mol*s)'), n=2.12602, w0=(656750,'J/mol'), E0=(72066.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.4651603830882185, var=10.429484289402048, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 12.668104523272545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 12.668104523272545""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 12.668104523272545
""",
)

entry(
    index = 88,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(70000,'m^3/(mol*s)'), n=0.465, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.1934e+08,'m^3/(mol*s)'), n=-0.512527, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07449059678931585, var=0.011172841518900372, Tref=1000.0, N=4, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.39906613464683327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39906613464683327""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39906613464683327
""",
)

entry(
    index = 90,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(217.861,'m^3/(mol*s)'), n=1.30652, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5467902985585142, var=0.040311495617509956, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 1.7763501246343105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 1.7763501246343105""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 1.7763501246343105
""",
)

entry(
    index = 91,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(1.30675e-09,'m^3/(mol*s)'), n=4.27735, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.9513487199804715, var=3.0964353862811893, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 10.94311944006548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 10.94311944006548""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 10.94311944006548
""",
)

entry(
    index = 92,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_4Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(137.111,'m^3/(mol*s)'), n=1.09916, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_4Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_4Cl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_4Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_4Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_N-4Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(38.9548,'m^3/(mol*s)'), n=1.37766, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_N-4Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_N-4Cl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_N-4Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_N-4Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_3Br1sCCl1sHI1s->C",
    kinetics = ArrheniusBM(A=(113.748,'m^3/(mol*s)'), n=1.11248, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_3Br1sCCl1sHI1s->C',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_3Br1sCCl1sHI1s->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_3Br1sCCl1sHI1s->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_3Br1sCCl1sHI1s->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_N-3Br1sCCl1sHI1s->C",
    kinetics = ArrheniusBM(A=(0.109762,'m^3/(mol*s)'), n=1.4247, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_N-3Br1sCCl1sHI1s->C',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_N-3Br1sCCl1sHI1s->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_N-3Br1sCCl1sHI1s->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_N-3Br1sCCl1sHI1s->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(5.0668e+08,'m^3/(mol*s)'), n=-0.731004, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.787034462320638, var=0.09796882358847864, Tref=1000.0, N=2, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.6049550376933333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933333""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933333
""",
)

entry(
    index = 97,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.985e+07,'m^3/(mol*s)'), n=-0.324, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(203,'m^3/(mol*s)'), n=1.249, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(3.10984,'m^3/(mol*s)'), n=1.8816, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(22.4644,'m^3/(mol*s)'), n=1.4485, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(131500,'m^3/(mol*s)'), n=0.313, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.08e+07,'m^3/(mol*s)'), n=-0.272, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH2_CH_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

