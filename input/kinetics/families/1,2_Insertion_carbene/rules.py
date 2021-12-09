#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.244e+53,'m^3/(mol*s)'), n=-13.5231, w0=(581040,'J/mol'), E0=(338607,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6026552433651862, var=98.89416387722879, Tref=1000.0, N=63, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 63 training reactions at node Root
    Total Standard Deviation in ln(k): 23.96296917057821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 63 training reactions at node Root
Total Standard Deviation in ln(k): 23.96296917057821""",
    longDesc = 
"""
BM rule fitted to 63 training reactions at node Root
Total Standard Deviation in ln(k): 23.96296917057821
""",
)

entry(
    index = 2,
    label = "HH",
    kinetics = ArrheniusBM(A=(1.3275e-16,'m^3/(mol*s)'), n=6.60406, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3778855523027446, var=125.69336257698696, Tref=1000.0, N=4, data_mean=0.0, correlation='HH',), comment="""BM rule fitted to 4 training reactions at node HH
    Total Standard Deviation in ln(k): 23.425157831565773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HH
Total Standard Deviation in ln(k): 23.425157831565773""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HH
Total Standard Deviation in ln(k): 23.425157831565773
""",
)

entry(
    index = 3,
    label = "HY",
    kinetics = ArrheniusBM(A=(1.16978e+14,'m^3/(mol*s)'), n=-2.17868, w0=(617447,'J/mol'), E0=(141383,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4337491965130608, var=16.300811436341426, Tref=1000.0, N=19, data_mean=0.0, correlation='HY',), comment="""BM rule fitted to 19 training reactions at node HY
    Total Standard Deviation in ln(k): 9.183792304363779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node HY
Total Standard Deviation in ln(k): 9.183792304363779""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node HY
Total Standard Deviation in ln(k): 9.183792304363779
""",
)

entry(
    index = 4,
    label = "YY",
    kinetics = ArrheniusBM(A=(0.209611,'m^3/(mol*s)'), n=1.48266, w0=(424667,'J/mol'), E0=(42466.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14049140450297173, var=52.57772058945326, Tref=1000.0, N=3, data_mean=0.0, correlation='YY',), comment="""BM rule fitted to 3 training reactions at node YY
    Total Standard Deviation in ln(k): 14.889426999479207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node YY
Total Standard Deviation in ln(k): 14.889426999479207""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node YY
Total Standard Deviation in ln(k): 14.889426999479207
""",
)

entry(
    index = 5,
    label = "CH",
    kinetics = ArrheniusBM(A=(9.40126e+27,'m^3/(mol*s)'), n=-6.182, w0=(584000,'J/mol'), E0=(217359,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7447083078494304, var=8.13495154888758, Tref=1000.0, N=19, data_mean=0.0, correlation='CH',), comment="""BM rule fitted to 19 training reactions at node CH
    Total Standard Deviation in ln(k): 7.588999003367698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node CH
Total Standard Deviation in ln(k): 7.588999003367698""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node CH
Total Standard Deviation in ln(k): 7.588999003367698
""",
)

entry(
    index = 6,
    label = "CY",
    kinetics = ArrheniusBM(A=(53.9579,'m^3/(mol*s)'), n=1.35755, w0=(555714,'J/mol'), E0=(353420,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.246662361426132, var=28.07917617079616, Tref=1000.0, N=7, data_mean=0.0, correlation='CY',), comment="""BM rule fitted to 7 training reactions at node CY
    Total Standard Deviation in ln(k): 16.267928951055897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node CY
Total Standard Deviation in ln(k): 16.267928951055897""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node CY
Total Standard Deviation in ln(k): 16.267928951055897
""",
)

entry(
    index = 7,
    label = "OHOY",
    kinetics = ArrheniusBM(A=(2.97161e+08,'m^3/(mol*s)'), n=-0.708509, w0=(614000,'J/mol'), E0=(193518,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3355125335038205, var=16.204830351702757, Tref=1000.0, N=4, data_mean=0.0, correlation='OHOY',), comment="""BM rule fitted to 4 training reactions at node OHOY
    Total Standard Deviation in ln(k): 8.913102215392753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node OHOY
Total Standard Deviation in ln(k): 8.913102215392753""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node OHOY
Total Standard Deviation in ln(k): 8.913102215392753
""",
)

entry(
    index = 8,
    label = "OH",
    kinetics = ArrheniusBM(A=(2.97161e+08,'m^3/(mol*s)'), n=-0.708509, w0=(614000,'J/mol'), E0=(193518,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3355125335038205, var=16.204830351702757, Tref=1000.0, N=4, data_mean=0.0, correlation='OH',), comment="""BM rule fitted to 4 training reactions at node OH
    Total Standard Deviation in ln(k): 8.913102215392753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node OH
Total Standard Deviation in ln(k): 8.913102215392753""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node OH
Total Standard Deviation in ln(k): 8.913102215392753
""",
)

entry(
    index = 9,
    label = "CC",
    kinetics = ArrheniusBM(A=(1.34094e-99,'m^3/(mol*s)'), n=30.0383, w0=(519000,'J/mol'), E0=(51900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.542447308995467, var=273.0558490462895, Tref=1000.0, N=3, data_mean=0.0, correlation='CC',), comment="""BM rule fitted to 3 training reactions at node CC
    Total Standard Deviation in ln(k): 39.5151061348087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CC
Total Standard Deviation in ln(k): 39.5151061348087""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CC
Total Standard Deviation in ln(k): 39.5151061348087
""",
)

entry(
    index = 10,
    label = "CO",
    kinetics = ArrheniusBM(A=(6.15709e-54,'m^3/(mol*s)'), n=16.7351, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2779029257972399, var=135.7923332073154, Tref=1000.0, N=3, data_mean=0.0, correlation='CO',), comment="""BM rule fitted to 3 training reactions at node CO
    Total Standard Deviation in ln(k): 26.57198270868904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CO
Total Standard Deviation in ln(k): 26.57198270868904""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CO
Total Standard Deviation in ln(k): 26.57198270868904
""",
)

entry(
    index = 11,
    label = "HH_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(0.0002978,'m^3/(mol*s)'), n=3.12491, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10165039056608514, var=0.6354575154082022, Tref=1000.0, N=3, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 3 training reactions at node HH_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 1.8534893692827277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HH_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 1.8534893692827277""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HH_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 1.8534893692827277
""",
)

entry(
    index = 12,
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
    index = 13,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(9.84988e+18,'m^3/(mol*s)'), n=-3.65089, w0=(643250,'J/mol'), E0=(195217,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2689673577859495, var=110.24343525067603, Tref=1000.0, N=4, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 4 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 24.237451804311014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 24.237451804311014""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 24.237451804311014
""",
)

entry(
    index = 14,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(391.174,'m^3/(mol*s)'), n=1.12309, w0=(610567,'J/mol'), E0=(73581.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04129319589067769, var=10.391374000854803, Tref=1000.0, N=15, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 15 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 6.566146415191295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 6.566146415191295""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 6.566146415191295
""",
)

entry(
    index = 15,
    label = "YY_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.18345,'m^3/(mol*s)'), n=0.764042, w0=(413500,'J/mol'), E0=(41350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.790053776114707, var=13.222171864649557, Tref=1000.0, N=2, data_mean=0.0, correlation='YY_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s
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
    index = 16,
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
    index = 17,
    label = "CH_Ext-4CbCdCsCt-R",
    kinetics = ArrheniusBM(A=(1.67081e+07,'m^3/(mol*s)'), n=-0.25099, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0578342058181985, var=0.11014630287494767, Tref=1000.0, N=12, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R',), comment="""BM rule fitted to 12 training reactions at node CH_Ext-4CbCdCsCt-R
    Total Standard Deviation in ln(k): 0.8106494977068928"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node CH_Ext-4CbCdCsCt-R
Total Standard Deviation in ln(k): 0.8106494977068928""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node CH_Ext-4CbCdCsCt-R
Total Standard Deviation in ln(k): 0.8106494977068928
""",
)

entry(
    index = 18,
    label = "CH_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(4.29958e+26,'m^3/(mol*s)'), n=-5.77431, w0=(584000,'J/mol'), E0=(286846,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.7225947200543095, var=365.40292185179175, Tref=1000.0, N=2, data_mean=0.0, correlation='CH_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 47.67479693507707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 47.67479693507707""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 47.67479693507707
""",
)

entry(
    index = 19,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.71679e-28,'m^3/(mol*s)'), n=9.53557, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.583341855553953, var=3.892549274873464, Tref=1000.0, N=5, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 5 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 5.42093405282634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 5.42093405282634""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 5.42093405282634
""",
)

entry(
    index = 20,
    label = "CY_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(1.27878e-57,'m^3/(mol*s)'), n=18.1435, w0=(538667,'J/mol'), E0=(53866.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4127005465209341, var=3.3658994929738193, Tref=1000.0, N=3, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 3 training reactions at node CY_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 7.227463599015265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CY_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.227463599015265""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CY_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.227463599015265
""",
)

entry(
    index = 21,
    label = "CY_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(5.80619e-06,'m^3/(mol*s)'), n=3.34489, w0=(568500,'J/mol'), E0=(341043,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.35041385600548225, var=12.356870521649794, Tref=1000.0, N=4, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 4 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 7.92754985661445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.92754985661445""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.92754985661445
""",
)

entry(
    index = 22,
    label = "OH_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(4.67448e-06,'m^3/(mol*s)'), n=3.15288, w0=(614000,'J/mol'), E0=(61400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='OH_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node OH_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node OH_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node OH_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "OH_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(3.16752e-07,'m^3/(mol*s)'), n=3.59532, w0=(614000,'J/mol'), E0=(162353,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08396792506211626, var=10.140921128810062, Tref=1000.0, N=3, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 3 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 6.595016044815871"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 6.595016044815871""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 6.595016044815871
""",
)

entry(
    index = 24,
    label = "CC_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(1.17766e-80,'m^3/(mol*s)'), n=24.619, w0=(519000,'J/mol'), E0=(51900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=22.34405263497189, var=42.86058327263803, Tref=1000.0, N=2, data_mean=0.0, correlation='CC_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 2 training reactions at node CC_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 69.26543430418596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CC_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 69.26543430418596""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CC_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 69.26543430418596
""",
)

entry(
    index = 25,
    label = "CC_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(2.22791e-07,'m^3/(mol*s)'), n=3.59921, w0=(519000,'J/mol'), E0=(51900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CC_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node CC_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CC_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CC_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "CO_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(5.9242e-66,'m^3/(mol*s)'), n=20.148, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=17.321484755736744, var=25.565583205176964, Tref=1000.0, N=2, data_mean=0.0, correlation='CO_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 53.65774418739183"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 53.65774418739183""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 53.65774418739183
""",
)

entry(
    index = 27,
    label = "CO_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.26474e-05,'m^3/(mol*s)'), n=2.95311, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CO_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CO_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CO_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CO_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
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
    index = 29,
    label = "HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s",
    kinetics = ArrheniusBM(A=(0.000130111,'m^3/(mol*s)'), n=3.20394, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2216614596813846, var=0.3883872655048153, Tref=1000.0, N=2, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s
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
    index = 30,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(7.17793e-29,'m^3/(mol*s)'), n=9.77658, w0=(614167,'J/mol'), E0=(-36640.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.9475590632820916, var=47.66489250787773, Tref=1000.0, N=3, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 3 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 23.75913411631206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 23.75913411631206""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 23.75913411631206
""",
)

entry(
    index = 31,
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
    index = 32,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(4.88137e+07,'m^3/(mol*s)'), n=-0.254532, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14958435028524644, var=4.3600149984513505, Tref=1000.0, N=6, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 6 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 4.561857011480642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 4.561857011480642""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 4.561857011480642
""",
)

entry(
    index = 33,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(0.0886093,'m^3/(mol*s)'), n=2.07674, w0=(664944,'J/mol'), E0=(77228.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15553375818186635, var=10.784919724936154, Tref=1000.0, N=9, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 9 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 6.974418826947979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 6.974418826947979""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 6.974418826947979
""",
)

entry(
    index = 34,
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
    index = 35,
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
    index = 36,
    label = "CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs",
    kinetics = ArrheniusBM(A=(1.13979e+06,'m^3/(mol*s)'), n=0.0863482, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028930781342124477, var=0.07206277691595277, Tref=1000.0, N=3, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs',), comment="""BM rule fitted to 3 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs
    Total Standard Deviation in ln(k): 0.610851733130727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.610851733130727""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.610851733130727
""",
)

entry(
    index = 37,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs",
    kinetics = ArrheniusBM(A=(4.08908e+07,'m^3/(mol*s)'), n=-0.363436, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.067468680435866, var=0.0824986432715594, Tref=1000.0, N=9, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs',), comment="""BM rule fitted to 9 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs
    Total Standard Deviation in ln(k): 0.7453308749429745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.7453308749429745""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.7453308749429745
""",
)

entry(
    index = 38,
    label = "CH_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(6.68018e-11,'m^3/(mol*s)'), n=4.72997, w0=(584000,'J/mol'), E0=(227703,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "CH_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.79958e-05,'m^3/(mol*s)'), n=3.10993, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_3Br1sCCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(3.3398e-07,'m^3/(mol*s)'), n=3.60759, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_3Br1sCCl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_3Br1sCCl1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_3Br1sCCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_3Br1sCCl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(2.72318e-26,'m^3/(mol*s)'), n=8.93362, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5317112651527381, var=3.9645985647384903, Tref=1000.0, N=4, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s',), comment="""BM rule fitted to 4 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s
    Total Standard Deviation in ln(k): 5.327646050832906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s
Total Standard Deviation in ln(k): 5.327646050832906""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s
Total Standard Deviation in ln(k): 5.327646050832906
""",
)

entry(
    index = 42,
    label = "CY_2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(3.01249e-05,'m^3/(mol*s)'), n=3.17037, w0=(458000,'J/mol'), E0=(45800,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(2.77066e-59,'m^3/(mol*s)'), n=18.6041, w0=(579000,'J/mol'), E0=(57900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=15.859515793666755, var=1.7645188631816184, Tref=1000.0, N=2, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 42.51102335151977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 42.51102335151977""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 42.51102335151977
""",
)

entry(
    index = 44,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_Ext-4CbCdCsCt-R",
    kinetics = ArrheniusBM(A=(1.33582e-06,'m^3/(mol*s)'), n=3.3552, w0=(658000,'J/mol'), E0=(369109,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_Ext-4CbCdCsCt-R',), comment="""BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_Ext-4CbCdCsCt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_Ext-4CbCdCsCt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_Ext-4CbCdCsCt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.42311e-06,'m^3/(mol*s)'), n=3.42841, w0=(500000,'J/mol'), E0=(50000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.84039e-86,'m^3/(mol*s)'), n=26.3373, w0=(558000,'J/mol'), E0=(55800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=24.584541838941217, var=0.31418087963789376, Tref=1000.0, N=2, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s
    Total Standard Deviation in ln(k): 62.89389652867011"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 62.89389652867011""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 62.89389652867011
""",
)

entry(
    index = 47,
    label = "OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(1.76395e-12,'m^3/(mol*s)'), n=5.02686, w0=(614000,'J/mol'), E0=(165851,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(1.32836e-09,'m^3/(mol*s)'), n=4.28606, w0=(614000,'J/mol'), E0=(143834,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.827606888873764, var=17.099167872578207, Tref=1000.0, N=2, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 15.394348025907975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 15.394348025907975""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 15.394348025907975
""",
)

entry(
    index = 49,
    label = "CC_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(5.7066e-06,'m^3/(mol*s)'), n=3.19155, w0=(519000,'J/mol'), E0=(51900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CC_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CC_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CC_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CC_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "CC_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(0.000166864,'m^3/(mol*s)'), n=2.82973, w0=(519000,'J/mol'), E0=(51900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CC_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CC_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CC_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CC_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "CO_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.40908e-07,'m^3/(mol*s)'), n=3.45227, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CO_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.12553e-07,'m^3/(mol*s)'), n=3.34134, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
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
    index = 54,
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
    index = 55,
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
    index = 56,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(56.8668,'m^3/(mol*s)'), n=0.977345, w0=(556000,'J/mol'), E0=(103001,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004804305618508593, var=1.6958898219066687, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 2.6227641290455668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 2.6227641290455668""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 2.6227641290455668
""",
)

entry(
    index = 57,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(182781,'m^3/(mol*s)'), n=0.429862, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11376049719385548, var=1.910664979516552, Tref=1000.0, N=4, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 4 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 3.0569116538211136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.0569116538211136""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.0569116538211136
""",
)

entry(
    index = 58,
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
    index = 59,
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
    index = 60,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(3.76867e+06,'m^3/(mol*s)'), n=0.00270422, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.021651136664414, var=195.2652024627637, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 43.143408608142536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 43.143408608142536""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 43.143408608142536
""",
)

entry(
    index = 61,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(0.00611152,'m^3/(mol*s)'), n=2.38439, w0=(688357,'J/mol'), E0=(77028.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.059315306573447704, var=7.773198662503887, Tref=1000.0, N=7, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 7 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 5.738326387244643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 5.738326387244643""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 5.738326387244643
""",
)

entry(
    index = 62,
    label = "CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.23333e+06,'m^3/(mol*s)'), n=-0.146, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(490107,'m^3/(mol*s)'), n=0.201831, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47428387515166337, var=0.06288991772562845, Tref=1000.0, N=2, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.6944127300954472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472
""",
)

entry(
    index = 64,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(9.16873e+07,'m^3/(mol*s)'), n=-0.471498, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07514139712124894, var=0.030917554547640714, Tref=1000.0, N=6, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.5412978340284114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5412978340284114""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5412978340284114
""",
)

entry(
    index = 65,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R",
    kinetics = ArrheniusBM(A=(2.13e+07,'m^3/(mol*s)'), n=-0.274, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.325e+06,'m^3/(mol*s)'), n=0.0073, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(33.15,'m^3/(mol*s)'), n=1.475, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(3.33873e-07,'m^3/(mol*s)'), n=3.38172, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(3.33078e-25,'m^3/(mol*s)'), n=8.64964, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5066804945605197, var=3.9034464344061863, Tref=1000.0, N=3, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 3 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 5.233850044838711"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 5.233850044838711""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 5.233850044838711
""",
)

entry(
    index = 70,
    label = "CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(4.96165e-06,'m^3/(mol*s)'), n=3.30609, w0=(658000,'J/mol'), E0=(65800,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.78425e-05,'m^3/(mol*s)'), n=3.22746, w0=(500000,'J/mol'), E0=(50000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(6.158e-07,'m^3/(mol*s)'), n=3.54561, w0=(658000,'J/mol'), E0=(65800,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(7.43831e-06,'m^3/(mol*s)'), n=3.35156, w0=(458000,'J/mol'), E0=(45800,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.23355e-09,'m^3/(mol*s)'), n=4.16722, w0=(614000,'J/mol'), E0=(141218,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.67626e-09,'m^3/(mol*s)'), n=4.20006, w0=(614000,'J/mol'), E0=(61400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
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
    index = 77,
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
    index = 78,
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
    index = 79,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1414.37,'m^3/(mol*s)'), n=1.0539, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.052114587802603474, var=0.19207253541555555, Tref=1000.0, N=3, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.0095379892829406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.0095379892829406""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.0095379892829406
""",
)

entry(
    index = 80,
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
    index = 81,
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
    index = 82,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(6.9697e-08,'m^3/(mol*s)'), n=3.78805, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24659187965062845, var=2.6435928301472624, Tref=1000.0, N=3, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 3.8791022547197236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.8791022547197236""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.8791022547197236
""",
)

entry(
    index = 83,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(3.22787e+06,'m^3/(mol*s)'), n=-0.092476, w0=(656750,'J/mol'), E0=(65675,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3761948964338802, var=0.059028709504851846, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s
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
    index = 84,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00202175,'m^3/(mol*s)'), n=2.43245, w0=(656750,'J/mol'), E0=(65817.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.750422289637572, var=10.429484289402051, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 13.384842981939265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 13.384842981939265""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 13.384842981939265
""",
)

entry(
    index = 85,
    label = "CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4933.33,'m^3/(mol*s)'), n=0.797, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(36700,'m^3/(mol*s)'), n=0.498, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_Sp-6R!H-4CbCdCt
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(1.10825e+08,'m^3/(mol*s)'), n=-0.494291, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07395628830263912, var=0.02913633692336577, Tref=1000.0, N=5, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 5 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
    Total Standard Deviation in ln(k): 0.5280154542513239"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.5280154542513239""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.5280154542513239
""",
)

entry(
    index = 88,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C",
    kinetics = ArrheniusBM(A=(1.0827e-21,'m^3/(mol*s)'), n=7.59417, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.554751041316875, var=0.2040317110632598, Tref=1000.0, N=2, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C',), comment="""BM rule fitted to 2 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C
    Total Standard Deviation in ln(k): 12.349634312037441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C
Total Standard Deviation in ln(k): 12.349634312037441""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C
Total Standard Deviation in ln(k): 12.349634312037441
""",
)

entry(
    index = 89,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_N-3Br1sCH->C",
    kinetics = ArrheniusBM(A=(5.49685e-07,'m^3/(mol*s)'), n=3.52855, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_N-3Br1sCH->C',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_N-3Br1sCH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_N-3Br1sCH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_N-3Br1sCH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(227.818,'m^3/(mol*s)'), n=1.29984, w0=(529000,'J/mol'), E0=(52900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5467902985585142, var=0.040311495617509956, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R
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
    kinetics = ArrheniusBM(A=(1.02669e-09,'m^3/(mol*s)'), n=4.31342, w0=(730500,'J/mol'), E0=(73050,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.9513487199804715, var=3.0964353862811893, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
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
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(70000,'m^3/(mol*s)'), n=0.465, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.27295e+08,'m^3/(mol*s)'), n=-0.522177, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07236307725614684, var=0.011171574677922782, Tref=1000.0, N=4, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.39370859440397243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39370859440397243""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39370859440397243
""",
)

entry(
    index = 98,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.24049e-06,'m^3/(mol*s)'), n=3.20888, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.9253e-06,'m^3/(mol*s)'), n=3.16987, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
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
    index = 101,
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
    index = 102,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(5.40342e+08,'m^3/(mol*s)'), n=-0.740623, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.787034462320638, var=0.09796882358847864, Tref=1000.0, N=2, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.6049550376933333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933333""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933333
""",
)

entry(
    index = 103,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.985e+07,'m^3/(mol*s)'), n=-0.324, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(203,'m^3/(mol*s)'), n=1.249, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(131500,'m^3/(mol*s)'), n=0.313, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.08e+07,'m^3/(mol*s)'), n=-0.272, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

