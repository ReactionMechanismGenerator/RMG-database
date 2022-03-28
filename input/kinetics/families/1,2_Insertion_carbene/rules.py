#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.50469e+53,'m^3/(mol*s)'), n=-13.541, w0=(581.04,'kJ/mol'), E0=(336.403,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.513119107657762, var=99.27123869380007, Tref=1000.0, N=63, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 63 training reactions at node Root
    Total Standard Deviation in ln(k): 23.775975334650404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 63 training reactions at node Root
Total Standard Deviation in ln(k): 23.775975334650404""",
    longDesc = 
"""
BM rule fitted to 63 training reactions at node Root
Total Standard Deviation in ln(k): 23.775975334650404
""",
)

entry(
    index = 2,
    label = "HH",
    kinetics = ArrheniusBM(A=(1.57245e+40,'m^3/(mol*s)'), n=-9.46179, w0=(627,'kJ/mol'), E0=(286.086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0057215542285545, var=62.159225863125215, Tref=1000.0, N=4, data_mean=0.0, correlation='HH',), comment="""BM rule fitted to 4 training reactions at node HH
    Total Standard Deviation in ln(k): 20.845057760557747"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HH
Total Standard Deviation in ln(k): 20.845057760557747""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HH
Total Standard Deviation in ln(k): 20.845057760557747
""",
)

entry(
    index = 3,
    label = "HH_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(160.794,'m^3/(mol*s)'), n=1.48251, w0=(627,'kJ/mol'), E0=(132.78,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18444078152295718, var=0.3527504141347885, Tref=1000.0, N=3, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 3 training reactions at node HH_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 1.6540872511930813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HH_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 1.6540872511930813""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HH_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 1.6540872511930813
""",
)

entry(
    index = 4,
    label = "HH_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->Br1s",
    kinetics = ArrheniusBM(A=(1.50896,'m^3/(mol*s)'), n=2.11145, w0=(627,'kJ/mol'), E0=(120.317,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->Br1s
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
    index = 5,
    label = "HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s",
    kinetics = ArrheniusBM(A=(11.6611,'m^3/(mol*s)'), n=1.785, w0=(627,'kJ/mol'), E0=(127.726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12638824541802388, var=0.1087312542899948, Tref=1000.0, N=2, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s
    Total Standard Deviation in ln(k): 0.9786082211207049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s
Total Standard Deviation in ln(k): 0.9786082211207049""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s
Total Standard Deviation in ln(k): 0.9786082211207049
""",
)

entry(
    index = 6,
    label = "HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_3Cl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(2.13948,'m^3/(mol*s)'), n=1.96174, w0=(627,'kJ/mol'), E0=(121.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_3Cl1sF1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_3Cl1sF1sH->F1s
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
    index = 7,
    label = "HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_N-3Cl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(1.39739,'m^3/(mol*s)'), n=2.08325, w0=(627,'kJ/mol'), E0=(124.994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_N-3Cl1sF1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node HH_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->Br1s_N-3Cl1sF1sH->F1s
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
    index = 8,
    label = "HH_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(3.26413e-09,'m^3/(mol*s)'), n=4.30786, w0=(627,'kJ/mol'), E0=(215.887,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HH_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node HH_N-2Br1sCl1sF1sHI1s->H
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
    index = 9,
    label = "HY",
    kinetics = ArrheniusBM(A=(1.19308e+15,'m^3/(mol*s)'), n=-2.48619, w0=(617.447,'kJ/mol'), E0=(143.525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4567526169257262, var=16.42503569342746, Tref=1000.0, N=19, data_mean=0.0, correlation='HY',), comment="""BM rule fitted to 19 training reactions at node HY
    Total Standard Deviation in ln(k): 9.27237233211209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node HY
Total Standard Deviation in ln(k): 9.27237233211209""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node HY
Total Standard Deviation in ln(k): 9.27237233211209
""",
)

entry(
    index = 10,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.09705e+20,'m^3/(mol*s)'), n=-4.05784, w0=(643.25,'kJ/mol'), E0=(196.789,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2457410906396802, var=110.73801540920508, Tref=1000.0, N=4, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 4 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 24.226257307947215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 24.226257307947215""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 24.226257307947215
""",
)

entry(
    index = 11,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(7.17793e-29,'m^3/(mol*s)'), n=9.77658, w0=(614.167,'kJ/mol'), E0=(40.8472,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.871898927309629, var=53.89863301171256, Tref=1000.0, N=3, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 3 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 24.44628983841625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 24.44628983841625""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 24.44628983841625
""",
)

entry(
    index = 12,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(3.98081e-09,'m^3/(mol*s)'), n=4.16158, w0=(730.5,'kJ/mol'), E0=(145.218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->F1s
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
    index = 13,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(490.447,'m^3/(mol*s)'), n=0.685287, w0=(556,'kJ/mol'), E0=(104.475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00036256892132874644, var=1.6680856284811425, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 2.5901143242066227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 2.5901143242066227""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 2.5901143242066227
""",
)

entry(
    index = 14,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.53881,'m^3/(mol*s)'), n=1.26919, w0=(583,'kJ/mol'), E0=(96.1337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_4Br1sCl1s->Cl1s
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
    index = 15,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_N-4Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(214000,'m^3/(mol*s)'), n=-6.53332e-08, w0=(529,'kJ/mol'), E0=(113.537,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_N-4Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->F1s_N-4Br1sCl1s->Cl1s
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
    index = 16,
    label = "HY_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(0.0514528,'m^3/(mol*s)'), n=2.19387, w0=(730.5,'kJ/mol'), E0=(80.0732,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s
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
    index = 17,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1504.93,'m^3/(mol*s)'), n=0.934412, w0=(610.567,'kJ/mol'), E0=(51.7021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0017462377678182982, var=10.47826062367848, Tref=1000.0, N=15, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 15 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 6.493743349677761"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 6.493743349677761""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 6.493743349677761
""",
)

entry(
    index = 18,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(4.88137e+07,'m^3/(mol*s)'), n=-0.254532, w0=(529,'kJ/mol'), E0=(65.0974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14958433561577356, var=4.360014987880059, Tref=1000.0, N=6, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 6 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 4.5618569695479625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 4.5618569695479625""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 4.5618569695479625
""",
)

entry(
    index = 19,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(182781,'m^3/(mol*s)'), n=0.429862, w0=(529,'kJ/mol'), E0=(67.3104,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11376048881184615, var=1.910664946019741, Tref=1000.0, N=4, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 4 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 3.0569116084701915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.0569116084701915""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 3.0569116084701915
""",
)

entry(
    index = 20,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.94494e+11,'m^3/(mol*s)'), n=-1.44224, w0=(529,'kJ/mol'), E0=(47.9409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_6R!H->C
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
    index = 21,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1414.37,'m^3/(mol*s)'), n=1.0539, w0=(529,'kJ/mol'), E0=(73.7669,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00634481711925604, var=0.25011904153038805, Tref=1000.0, N=3, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.0185479085825118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.0185479085825118""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.0185479085825118
""",
)

entry(
    index = 22,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(227.818,'m^3/(mol*s)'), n=1.29984, w0=(529,'kJ/mol'), E0=(75.7342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0204191866451209, var=0.4525545401550183, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 1.3999333595844436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 1.3999333595844436""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 1.3999333595844436
""",
)

entry(
    index = 23,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(4.43208,'m^3/(mol*s)'), n=1.83751, w0=(529,'kJ/mol'), E0=(79.743,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_Ext-3Br1sCCl1sHI1s-R_N-6R!H->C_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
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
    index = 24,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.21206e+18,'m^3/(mol*s)'), n=-3.24664, w0=(529,'kJ/mol'), E0=(38.1761,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->F1s
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
    index = 25,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=-3.02437e-08, w0=(529,'kJ/mol'), E0=(77.1661,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->F1s
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
    index = 26,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(7.6765,'m^3/(mol*s)'), n=1.46392, w0=(664.944,'kJ/mol'), E0=(80.3477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10316422275018103, var=10.421495061020293, Tref=1000.0, N=9, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 9 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 6.730960621514095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 6.730960621514095""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 6.730960621514095
""",
)

entry(
    index = 27,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(3.76867e+06,'m^3/(mol*s)'), n=0.00270408, w0=(583,'kJ/mol'), E0=(2.97164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-12.601168777332983, var=361.2258937203764, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 69.76310998171257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 69.76310998171257""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 69.76310998171257
""",
)

entry(
    index = 28,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=5.28703e-09, w0=(583,'kJ/mol'), E0=(75.2086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sHI1s->Cl1s
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
    index = 29,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.33736e+17,'m^3/(mol*s)'), n=-4.54388, w0=(583,'kJ/mol'), E0=(180.008,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sHI1s->Cl1s
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
    index = 30,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(0.013261,'m^3/(mol*s)'), n=2.2731, w0=(688.357,'kJ/mol'), E0=(58.0977,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05103196771681782, var=7.159345808690377, Tref=1000.0, N=7, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 7 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 5.492281424906893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 5.492281424906893""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 5.492281424906893
""",
)

entry(
    index = 31,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(6.9697e-08,'m^3/(mol*s)'), n=3.78805, w0=(730.5,'kJ/mol'), E0=(73.1317,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3001410487914693, var=2.9282398409420045, Tref=1000.0, N=3, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 4.184646053545055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 4.184646053545055""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 4.184646053545055
""",
)

entry(
    index = 32,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(5.4487,'m^3/(mol*s)'), n=1.52711, w0=(730.5,'kJ/mol'), E0=(132.147,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02090651070256912, var=1.7269912187795557, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
    Total Standard Deviation in ln(k): 2.6870522832325783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 2.6870522832325783""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
Total Standard Deviation in ln(k): 2.6870522832325783
""",
)

entry(
    index = 33,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R",
    kinetics = ArrheniusBM(A=(22.4644,'m^3/(mol*s)'), n=1.4485, w0=(730.5,'kJ/mol'), E0=(137.198,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R_Ext-3Br1sCCl1sHI1s-R
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
    index = 34,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(3.22787e+06,'m^3/(mol*s)'), n=-0.0924759, w0=(656.75,'kJ/mol'), E0=(67.7712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12610951792154945, var=0.26951270124779947, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 1.3576085364528785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 1.3576085364528785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 1.3576085364528785
""",
)

entry(
    index = 35,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_4Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.80806e+08,'m^3/(mol*s)'), n=-0.709128, w0=(730.5,'kJ/mol'), E0=(65.25,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_4Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_4Cl1sF1s->F1s
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
    index = 36,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_N-4Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(37104.3,'m^3/(mol*s)'), n=0.524176, w0=(583,'kJ/mol'), E0=(70.2924,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_N-4Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1s->F1s_N-4Cl1sF1s->F1s
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
    index = 37,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00196975,'m^3/(mol*s)'), n=2.43508, w0=(656.75,'kJ/mol'), E0=(63.191,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1360459495935581, var=0.536668528117854, Tref=1000.0, N=2, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 1.810446073712933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 1.810446073712933""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 1.810446073712933
""",
)

entry(
    index = 38,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_3Br1sCCl1sHI1s->C",
    kinetics = ArrheniusBM(A=(113.748,'m^3/(mol*s)'), n=1.11248, w0=(730.5,'kJ/mol'), E0=(108.719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_3Br1sCCl1sHI1s->C',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_3Br1sCCl1sHI1s->C
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
    index = 39,
    label = "HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_N-3Br1sCCl1sHI1s->C",
    kinetics = ArrheniusBM(A=(2.70149e+08,'m^3/(mol*s)'), n=-1.26599, w0=(583,'kJ/mol'), E0=(35.9196,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_N-3Br1sCCl1sHI1s->C',), comment="""BM rule fitted to 1 training reactions at node HY_N-3Br1sCCl1sF1sHI1s->F1s_N-4Br1sCl1sF1sI1s->Br1s_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1s->F1s_N-3Br1sCCl1sHI1s->C
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
    index = 40,
    label = "YY",
    kinetics = ArrheniusBM(A=(7.12506e+14,'m^3/(mol*s)'), n=-2.96729, w0=(424.667,'kJ/mol'), E0=(136.816,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5496726164829923, var=62.62422940093214, Tref=1000.0, N=3, data_mean=0.0, correlation='YY',), comment="""BM rule fitted to 3 training reactions at node YY
    Total Standard Deviation in ln(k): 17.24565264902038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node YY
Total Standard Deviation in ln(k): 17.24565264902038""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node YY
Total Standard Deviation in ln(k): 17.24565264902038
""",
)

entry(
    index = 41,
    label = "YY_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.18345,'m^3/(mol*s)'), n=0.764042, w0=(413.5,'kJ/mol'), E0=(18.2209,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5676419187717117, var=30.872492929782375, Tref=1000.0, N=2, data_mean=0.0, correlation='YY_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 12.56514967984041"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 12.56514967984041""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 12.56514967984041
""",
)

entry(
    index = 42,
    label = "YY_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(321,'m^3/(mol*s)'), n=2.45346e-08, w0=(447,'kJ/mol'), E0=(96.0283,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='YY_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s_4Br1sCl1sI1s->Cl1s
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
    index = 43,
    label = "YY_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(3200,'m^3/(mol*s)'), n=1.45247e-08, w0=(380,'kJ/mol'), E0=(65.8284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='YY_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node YY_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCl1sI1s->Cl1s
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
    index = 44,
    label = "YY_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=-9.29881e-08, w0=(447,'kJ/mol'), E0=(131.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='YY_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node YY_N-2Br1sCl1sF1sHI1s->F1s
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
    index = 45,
    label = "CH",
    kinetics = ArrheniusBM(A=(6.44768e+28,'m^3/(mol*s)'), n=-6.4458, w0=(584,'kJ/mol'), E0=(218.637,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6591608693425184, var=5.4995193120720405, Tref=1000.0, N=19, data_mean=0.0, correlation='CH',), comment="""BM rule fitted to 19 training reactions at node CH
    Total Standard Deviation in ln(k): 6.357498133665092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node CH
Total Standard Deviation in ln(k): 6.357498133665092""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node CH
Total Standard Deviation in ln(k): 6.357498133665092
""",
)

entry(
    index = 46,
    label = "CH_Ext-4CbCdCsCt-R",
    kinetics = ArrheniusBM(A=(1.67081e+07,'m^3/(mol*s)'), n=-0.25099, w0=(584,'kJ/mol'), E0=(109.752,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05783420702249951, var=0.11014630093021238, Tref=1000.0, N=12, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R',), comment="""BM rule fitted to 12 training reactions at node CH_Ext-4CbCdCsCt-R
    Total Standard Deviation in ln(k): 0.8106494948591996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node CH_Ext-4CbCdCsCt-R
Total Standard Deviation in ln(k): 0.8106494948591996""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node CH_Ext-4CbCdCsCt-R
Total Standard Deviation in ln(k): 0.8106494948591996
""",
)

entry(
    index = 47,
    label = "CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs",
    kinetics = ArrheniusBM(A=(1.13979e+06,'m^3/(mol*s)'), n=0.0863482, w0=(584,'kJ/mol'), E0=(109.735,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028930780883000492, var=0.07206277511555077, Tref=1000.0, N=3, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs',), comment="""BM rule fitted to 3 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs
    Total Standard Deviation in ln(k): 0.6108517252544917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.6108517252544917""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.6108517252544917
""",
)

entry(
    index = 48,
    label = "CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.16448e+06,'m^3/(mol*s)'), n=-0.144618, w0=(584,'kJ/mol'), E0=(102.471,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
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
    index = 49,
    label = "CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(490107,'m^3/(mol*s)'), n=0.201831, w0=(584,'kJ/mol'), E0=(108.551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.043461663341785264, var=0.18543765059589312, Tref=1000.0, N=2, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.9724886431361681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9724886431361681""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9724886431361681
""",
)

entry(
    index = 50,
    label = "CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(486642,'m^3/(mol*s)'), n=0.225671, w0=(584,'kJ/mol'), E0=(108.428,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
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
    index = 51,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs",
    kinetics = ArrheniusBM(A=(4.08908e+07,'m^3/(mol*s)'), n=-0.363436, w0=(584,'kJ/mol'), E0=(109.758,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06746868097934366, var=0.08249864412907129, Tref=1000.0, N=9, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs',), comment="""BM rule fitted to 9 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs
    Total Standard Deviation in ln(k): 0.7453308793010623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.7453308793010623""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs
Total Standard Deviation in ln(k): 0.7453308793010623
""",
)

entry(
    index = 52,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(9.16873e+07,'m^3/(mol*s)'), n=-0.471498, w0=(584,'kJ/mol'), E0=(108.674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07514139785501385, var=0.03091755307632206, Tref=1000.0, N=6, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.5412978274845682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5412978274845682""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5412978274845682
""",
)

entry(
    index = 53,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(3.55364e+07,'m^3/(mol*s)'), n=-0.357533, w0=(584,'kJ/mol'), E0=(107.976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_Sp-6R!H-4CbCdCt
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
    index = 54,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(1.10825e+08,'m^3/(mol*s)'), n=-0.494291, w0=(584,'kJ/mol'), E0=(108.813,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0739562917847758, var=0.02913633587331158, Tref=1000.0, N=5, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 5 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
    Total Standard Deviation in ln(k): 0.5280154568341594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.5280154568341594""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.5280154568341594
""",
)

entry(
    index = 55,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.36692e+07,'m^3/(mol*s)'), n=-0.382746, w0=(584,'kJ/mol'), E0=(106.821,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
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
    index = 56,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.27295e+08,'m^3/(mol*s)'), n=-0.522177, w0=(584,'kJ/mol'), E0=(109.312,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07236308446794819, var=0.011171575725256783, Tref=1000.0, N=4, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.39370862245649435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39370862245649435""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39370862245649435
""",
)

entry(
    index = 57,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(5.40342e+08,'m^3/(mol*s)'), n=-0.740623, w0=(584,'kJ/mol'), E0=(109.081,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07212098919745502, var=0.007692440233300485, Tref=1000.0, N=2, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.35703692796408437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.35703692796408437""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.35703692796408437
""",
)

entry(
    index = 58,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.8535e+08,'m^3/(mol*s)'), n=-0.589251, w0=(584,'kJ/mol'), E0=(107.814,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
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
    index = 59,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.57523e+09,'m^3/(mol*s)'), n=-0.891994, w0=(584,'kJ/mol'), E0=(110.348,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
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

entry(
    index = 60,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(7.68921e+08,'m^3/(mol*s)'), n=-0.779019, w0=(584,'kJ/mol'), E0=(111.029,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
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
    index = 61,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.16958e+06,'m^3/(mol*s)'), n=0.171554, w0=(584,'kJ/mol'), E0=(108.056,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
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
    index = 62,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R",
    kinetics = ArrheniusBM(A=(3.11579e+08,'m^3/(mol*s)'), n=-0.607843, w0=(584,'kJ/mol'), E0=(113.515,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_Ext-4CbCdCt-R
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
    index = 63,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(8.17451e+07,'m^3/(mol*s)'), n=-0.50563, w0=(584,'kJ/mol'), E0=(111.079,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_4CbCdCt->Cd
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
    index = 64,
    label = "CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(21122.7,'m^3/(mol*s)'), n=0.671539, w0=(584,'kJ/mol'), E0=(111.182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node CH_Ext-4CbCdCsCt-R_N-4CbCdCsCt->Cs_N-4CbCdCt->Cd
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
    index = 65,
    label = "CH_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(3.1861e+27,'m^3/(mol*s)'), n=-6.07002, w0=(584,'kJ/mol'), E0=(287.514,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5812749967363261, var=220.69207514042446, Tref=1000.0, N=2, data_mean=0.0, correlation='CH_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 31.242249878021042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 31.242249878021042""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 31.242249878021042
""",
)

entry(
    index = 66,
    label = "CH_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(6.68018e-11,'m^3/(mol*s)'), n=4.72997, w0=(584,'kJ/mol'), E0=(228.996,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->F1s
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
    index = 67,
    label = "CH_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.79957e-05,'m^3/(mol*s)'), n=3.10993, w0=(584,'kJ/mol'), E0=(140.025,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CH_3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->F1s
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
    index = 68,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(0.00023561,'m^3/(mol*s)'), n=2.67696, w0=(584,'kJ/mol'), E0=(176.605,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06140068338498148, var=2.176444724058605, Tref=1000.0, N=5, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 5 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 3.1118143213985663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 3.1118143213985663""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 3.1118143213985663
""",
)

entry(
    index = 69,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_3Br1sCCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(3.3398e-07,'m^3/(mol*s)'), n=3.60759, w0=(584,'kJ/mol'), E0=(182.432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_3Br1sCCl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_3Br1sCCl1sH->Cl1s
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
    index = 70,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(2.18628e-05,'m^3/(mol*s)'), n=2.94416, w0=(584,'kJ/mol'), E0=(169.46,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08450722928530859, var=2.966374345416031, Tref=1000.0, N=4, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s',), comment="""BM rule fitted to 4 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s
    Total Standard Deviation in ln(k): 3.665118151344325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s
Total Standard Deviation in ln(k): 3.665118151344325""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s
Total Standard Deviation in ln(k): 3.665118151344325
""",
)

entry(
    index = 71,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(3.33872e-07,'m^3/(mol*s)'), n=3.38172, w0=(584,'kJ/mol'), E0=(175.912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_2Br1sCl1sF1sHI1s->F1s
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
    index = 72,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(0.00162495,'m^3/(mol*s)'), n=2.43564, w0=(584,'kJ/mol'), E0=(171.386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.027130249649059007, var=0.9392093380070419, Tref=1000.0, N=3, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 3 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 2.0110116189485745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.0110116189485745""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.0110116189485745
""",
)

entry(
    index = 73,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C",
    kinetics = ArrheniusBM(A=(5.00807e-06,'m^3/(mol*s)'), n=3.10588, w0=(584,'kJ/mol'), E0=(155.269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09627616074934456, var=0.5326628706745564, Tref=1000.0, N=2, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C',), comment="""BM rule fitted to 2 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C
    Total Standard Deviation in ln(k): 1.705030867897116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C
Total Standard Deviation in ln(k): 1.705030867897116""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C
Total Standard Deviation in ln(k): 1.705030867897116
""",
)

entry(
    index = 74,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.24049e-06,'m^3/(mol*s)'), n=3.20888, w0=(584,'kJ/mol'), E0=(157.226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_2Br1sCl1s->Cl1s
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
    index = 75,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.9253e-06,'m^3/(mol*s)'), n=3.16987, w0=(584,'kJ/mol'), E0=(151.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_3Br1sCH->C_N-2Br1sCl1s->Cl1s
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
    index = 76,
    label = "CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_N-3Br1sCH->C",
    kinetics = ArrheniusBM(A=(5.49685e-07,'m^3/(mol*s)'), n=3.52855, w0=(584,'kJ/mol'), E0=(174.773,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_N-3Br1sCH->C',), comment="""BM rule fitted to 1 training reactions at node CH_N-3Br1sCCl1sF1sHI1s->F1s_N-3Br1sCCl1sH->Cl1s_N-2Br1sCl1sF1sHI1s->F1s_N-3Br1sCH->C
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
    index = 77,
    label = "CY",
    kinetics = ArrheniusBM(A=(104.891,'m^3/(mol*s)'), n=1.20304, w0=(555.714,'kJ/mol'), E0=(352.855,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.777380006033631, var=25.083631456492316, Tref=1000.0, N=7, data_mean=0.0, correlation='CY',), comment="""BM rule fitted to 7 training reactions at node CY
    Total Standard Deviation in ln(k): 14.50620618988802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node CY
Total Standard Deviation in ln(k): 14.50620618988802""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node CY
Total Standard Deviation in ln(k): 14.50620618988802
""",
)

entry(
    index = 78,
    label = "CY_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(6.49375e-13,'m^3/(mol*s)'), n=5.33465, w0=(538.667,'kJ/mol'), E0=(264.106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29053050618029913, var=10.223018529022832, Tref=1000.0, N=3, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 3 training reactions at node CY_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 7.139806913191501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CY_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.139806913191501""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CY_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.139806913191501
""",
)

entry(
    index = 79,
    label = "CY_2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(3.01249e-05,'m^3/(mol*s)'), n=3.17037, w0=(458,'kJ/mol'), E0=(273.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Br1s
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
    index = 80,
    label = "CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s",
    kinetics = ArrheniusBM(A=(1.2012e-10,'m^3/(mol*s)'), n=4.66895, w0=(579,'kJ/mol'), E0=(278.225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17521033742536213, var=13.662879193128079, Tref=1000.0, N=2, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s
    Total Standard Deviation in ln(k): 7.850395820592586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 7.850395820592586""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s
Total Standard Deviation in ln(k): 7.850395820592586
""",
)

entry(
    index = 81,
    label = "CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(4.96165e-06,'m^3/(mol*s)'), n=3.30609, w0=(658,'kJ/mol'), E0=(300.389,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_5Cl1sF1s->F1s
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
    index = 82,
    label = "CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.78425e-05,'m^3/(mol*s)'), n=3.22746, w0=(500,'kJ/mol'), E0=(286.146,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CY_2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Br1s_N-5Cl1sF1s->F1s
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
    index = 83,
    label = "CY_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(8.68619e-06,'m^3/(mol*s)'), n=3.22251, w0=(568.5,'kJ/mol'), E0=(340.237,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21935560952967964, var=6.817060158071854, Tref=1000.0, N=4, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 4 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 5.785407896000591"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 5.785407896000591""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 5.785407896000591
""",
)

entry(
    index = 84,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R",
    kinetics = ArrheniusBM(A=(1.33582e-06,'m^3/(mol*s)'), n=3.3552, w0=(658,'kJ/mol'), E0=(372.673,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R',), comment="""BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_Ext-4Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.42311e-06,'m^3/(mol*s)'), n=3.42841, w0=(500,'kJ/mol'), E0=(332.503,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_5Br1sCl1sF1sI1s->Cl1s
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
    index = 86,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.76839e-08,'m^3/(mol*s)'), n=3.93843, w0=(558,'kJ/mol'), E0=(331.989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3048192623022214, var=16.823155120458388, Tref=1000.0, N=2, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s
    Total Standard Deviation in ln(k): 14.013632522321476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 14.013632522321476""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s
Total Standard Deviation in ln(k): 14.013632522321476
""",
)

entry(
    index = 87,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(6.158e-07,'m^3/(mol*s)'), n=3.54561, w0=(658,'kJ/mol'), E0=(334.807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_5Br1sF1s->F1s
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
    index = 88,
    label = "CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(7.43831e-06,'m^3/(mol*s)'), n=3.35156, w0=(458,'kJ/mol'), E0=(323.891,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CY_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCl1sF1sI1s->Cl1s_N-5Br1sF1s->F1s
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
    index = 89,
    label = "OHOY",
    kinetics = ArrheniusBM(A=(2.13916e+09,'m^3/(mol*s)'), n=-1.00842, w0=(614,'kJ/mol'), E0=(194.239,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17406617270594374, var=16.167420070870673, Tref=1000.0, N=4, data_mean=0.0, correlation='OHOY',), comment="""BM rule fitted to 4 training reactions at node OHOY
    Total Standard Deviation in ln(k): 8.498137434485294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node OHOY
Total Standard Deviation in ln(k): 8.498137434485294""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node OHOY
Total Standard Deviation in ln(k): 8.498137434485294
""",
)

entry(
    index = 90,
    label = "OH",
    kinetics = ArrheniusBM(A=(2.13916e+09,'m^3/(mol*s)'), n=-1.00842, w0=(614,'kJ/mol'), E0=(194.239,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17406617270594374, var=16.167420070870673, Tref=1000.0, N=4, data_mean=0.0, correlation='OH',), comment="""BM rule fitted to 4 training reactions at node OH
    Total Standard Deviation in ln(k): 8.498137434485294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node OH
Total Standard Deviation in ln(k): 8.498137434485294""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node OH
Total Standard Deviation in ln(k): 8.498137434485294
""",
)

entry(
    index = 91,
    label = "OH_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(4.67448e-06,'m^3/(mol*s)'), n=3.15288, w0=(614,'kJ/mol'), E0=(90.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='OH_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node OH_2Br1sCl1sF1sHI1s->H
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
    index = 92,
    label = "OH_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(4.23875e-06,'m^3/(mol*s)'), n=3.21724, w0=(614,'kJ/mol'), E0=(164.088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.108323539544058, var=9.91321701645709, Tref=1000.0, N=3, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 3 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 6.58413054393339"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 6.58413054393339""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 6.58413054393339
""",
)

entry(
    index = 93,
    label = "OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(1.76395e-12,'m^3/(mol*s)'), n=5.02686, w0=(614,'kJ/mol'), E0=(167.02,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s
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
    index = 94,
    label = "OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s",
    kinetics = ArrheniusBM(A=(2.63835e-09,'m^3/(mol*s)'), n=4.14506, w0=(614,'kJ/mol'), E0=(143.299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23722374380764835, var=0.044009247151562056, Tref=1000.0, N=2, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s
    Total Standard Deviation in ln(k): 1.016600520901901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 1.016600520901901""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s
Total Standard Deviation in ln(k): 1.016600520901901
""",
)

entry(
    index = 95,
    label = "OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.23354e-09,'m^3/(mol*s)'), n=4.16722, w0=(614,'kJ/mol'), E0=(144.228,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_2Br1sCl1s->Cl1s
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
    index = 96,
    label = "OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.67626e-09,'m^3/(mol*s)'), n=4.20006, w0=(614,'kJ/mol'), E0=(141.512,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node OH_N-2Br1sCl1sF1sHI1s->H_N-2Br1sCl1sF1sI1s->F1s_N-2Br1sCl1s->Cl1s
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
    index = 97,
    label = "CC",
    kinetics = ArrheniusBM(A=(1.34094e-99,'m^3/(mol*s)'), n=30.0383, w0=(519,'kJ/mol'), E0=(51.9,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6620854538738407, var=85.54837375342689, Tref=1000.0, N=3, data_mean=0.0, correlation='CC',), comment="""BM rule fitted to 3 training reactions at node CC
    Total Standard Deviation in ln(k): 20.20579991644221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CC
Total Standard Deviation in ln(k): 20.20579991644221""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CC
Total Standard Deviation in ln(k): 20.20579991644221
""",
)

entry(
    index = 98,
    label = "CC_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(4.75016e+11,'m^3/(mol*s)'), n=-1.62726, w0=(519,'kJ/mol'), E0=(415.907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02873165458744823, var=48.530456786660096, Tref=1000.0, N=2, data_mean=0.0, correlation='CC_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 2 training reactions at node CC_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 14.037937368069308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CC_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 14.037937368069308""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CC_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 14.037937368069308
""",
)

entry(
    index = 99,
    label = "CC_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(5.7066e-06,'m^3/(mol*s)'), n=3.19155, w0=(519,'kJ/mol'), E0=(387.908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CC_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CC_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->F1s
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
    index = 100,
    label = "CC_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(0.000166864,'m^3/(mol*s)'), n=2.82973, w0=(519,'kJ/mol'), E0=(346.264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CC_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CC_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->F1s
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
    index = 101,
    label = "CC_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(2.22791e-07,'m^3/(mol*s)'), n=3.59921, w0=(519,'kJ/mol'), E0=(453.783,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CC_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node CC_N-2Br1sCl1sF1sHI1s->H
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
    index = 102,
    label = "CO",
    kinetics = ArrheniusBM(A=(1.33981e+28,'m^3/(mol*s)'), n=-6.56923, w0=(531,'kJ/mol'), E0=(379.915,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6010424776860186, var=51.413166251670845, Tref=1000.0, N=3, data_mean=0.0, correlation='CO',), comment="""BM rule fitted to 3 training reactions at node CO
    Total Standard Deviation in ln(k): 15.884703894552402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node CO
Total Standard Deviation in ln(k): 15.884703894552402""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node CO
Total Standard Deviation in ln(k): 15.884703894552402
""",
)

entry(
    index = 103,
    label = "CO_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.14358e+07,'m^3/(mol*s)'), n=-0.641018, w0=(531,'kJ/mol'), E0=(341.525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17570294811609, var=29.477358162589667, Tref=1000.0, N=2, data_mean=0.0, correlation='CO_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.325783866314726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.325783866314726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.325783866314726
""",
)

entry(
    index = 104,
    label = "CO_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.40908e-07,'m^3/(mol*s)'), n=3.45227, w0=(531,'kJ/mol'), E0=(320.794,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CO_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->F1s
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
    index = 105,
    label = "CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.12553e-07,'m^3/(mol*s)'), n=3.34134, w0=(531,'kJ/mol'), E0=(278.221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s
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
    index = 106,
    label = "CO_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1.26474e-05,'m^3/(mol*s)'), n=2.95311, w0=(531,'kJ/mol'), E0=(223.988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CO_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node CO_N-2Br1sCl1sF1sHI1s->F1s
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

