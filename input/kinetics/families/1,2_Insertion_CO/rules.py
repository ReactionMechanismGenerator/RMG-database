#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.00380681,'m^3/(mol*s)'), n=2.83534, w0=(722.933,'kJ/mol'), E0=(323.466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.010754833276949566, var=80.58889985168734, Tref=1000.0, N=15, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 15 training reactions at node Root
    Total Standard Deviation in ln(k): 18.02379371015199"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 18.02379371015199""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 18.02379371015199
""",
)

entry(
    index = 2,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.0096162,'m^3/(mol*s)'), n=2.81163, w0=(707.8,'kJ/mol'), E0=(360.683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14579455807344396, var=32.24392502772673, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs',), comment="""BM rule fitted to 10 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.749952421113377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.749952421113377""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.749952421113377
""",
)

entry(
    index = 3,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000538,'m^3/(mol*s)'), n=3.29, w0=(655.5,'kJ/mol'), E0=(448.955,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.0118807,'m^3/(mol*s)'), n=2.76523, w0=(713.611,'kJ/mol'), E0=(345.557,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22343949396153373, var=5.954151137674041, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 5.453185758190856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 5.453185758190856""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 5.453185758190856
""",
)

entry(
    index = 5,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.0201957,'m^3/(mol*s)'), n=2.62581, w0=(735.3,'kJ/mol'), E0=(345.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.36511479707618816, var=7.164731456852299, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R',), comment="""BM rule fitted to 5 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R
    Total Standard Deviation in ln(k): 6.2834514517653925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.2834514517653925""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.2834514517653925
""",
)

entry(
    index = 6,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(0.0026956,'m^3/(mol*s)'), n=2.93313, w0=(794.5,'kJ/mol'), E0=(387.509,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s",
    kinetics = ArrheniusBM(A=(0.0270345,'m^3/(mol*s)'), n=2.58298, w0=(720.5,'kJ/mol'), E0=(340.488,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25906933291314677, var=2.9301042026274278, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s',), comment="""BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s
    Total Standard Deviation in ln(k): 4.082542692204979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.082542692204979""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s
Total Standard Deviation in ln(k): 4.082542692204979
""",
)

entry(
    index = 8,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C",
    kinetics = ArrheniusBM(A=(1.84346,'m^3/(mol*s)'), n=2.0364, w0=(720.5,'kJ/mol'), E0=(344.399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.26314699591391894, var=4.003648838577825, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C
    Total Standard Deviation in ln(k): 4.672471833169928"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C
Total Standard Deviation in ln(k): 4.672471833169928""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C
Total Standard Deviation in ln(k): 4.672471833169928
""",
)

entry(
    index = 9,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(8.29763,'m^3/(mol*s)'), n=1.78932, w0=(720.5,'kJ/mol'), E0=(339.095,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3161957846247408, var=8.849246342592508, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R
    Total Standard Deviation in ln(k): 6.758084096165084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.758084096165084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.758084096165084
""",
)

entry(
    index = 10,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720.5,'kJ/mol'), E0=(334.124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81927e-16,'m^3/(mol*s)'), n=6.80628, w0=(720.5,'kJ/mol'), E0=(310.202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->F1s_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(0.0164,'m^3/(mol*s)'), n=2.86, w0=(720.5,'kJ/mol'), E0=(354.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(0.000179486,'m^3/(mol*s)'), n=3.40866, w0=(675.167,'kJ/mol'), E0=(336.825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21195615461406508, var=25.03199200938381, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 10.562640039096285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.562640039096285""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.562640039096285
""",
)

entry(
    index = 14,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.000614234,'m^3/(mol*s)'), n=3.16963, w0=(794.5,'kJ/mol'), E0=(363.512,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00962603,'m^3/(mol*s)'), n=2.95613, w0=(615.5,'kJ/mol'), E0=(328.448,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18731351736345964, var=8.005119587844957, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 6.14269809195366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.14269809195366""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.14269809195366
""",
)

entry(
    index = 16,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.00734196,'m^3/(mol*s)'), n=2.97843, w0=(636.5,'kJ/mol'), E0=(335.809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0163189,'m^3/(mol*s)'), n=2.90186, w0=(594.5,'kJ/mol'), E0=(321.364,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000742267,'m^3/(mol*s)'), n=2.83796, w0=(753.2,'kJ/mol'), E0=(242.307,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2632766423807829, var=145.9379134136138, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs',), comment="""BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs
    Total Standard Deviation in ln(k): 27.392216985255285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 27.392216985255285""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 27.392216985255285
""",
)

entry(
    index = 19,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(0.0711444,'m^3/(mol*s)'), n=2.26675, w0=(757,'kJ/mol'), E0=(295.916,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11077368402443419, var=66.76874779178424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 16.6594463424353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 16.6594463424353""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 16.6594463424353
""",
)

entry(
    index = 20,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, w0=(750.5,'kJ/mol'), E0=(245.723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCtHNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(2890,'m^3/(mol*s)'), n=1.16, w0=(763.5,'kJ/mol'), E0=(343.19,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2.97982e-05,'m^3/(mol*s)'), n=3.24395, w0=(750.667,'kJ/mol'), E0=(155.78,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10120818548749766, var=44.29408324435667, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 13.5965657078993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.5965657078993""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.5965657078993
""",
)

entry(
    index = 23,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(5.66811e-11,'m^3/(mol*s)'), n=4.88105, w0=(867,'kJ/mol'), E0=(181.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00925502,'m^3/(mol*s)'), n=2.53089, w0=(692.5,'kJ/mol'), E0=(142.143,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05412795233083378, var=9.232006363555076, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 6.227230421193233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.227230421193233""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.227230421193233
""",
)

entry(
    index = 25,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.006108,'m^3/(mol*s)'), n=2.57909, w0=(719.5,'kJ/mol'), E0=(150.342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0152384,'m^3/(mol*s)'), n=2.47236, w0=(665.5,'kJ/mol'), E0=(134.033,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

