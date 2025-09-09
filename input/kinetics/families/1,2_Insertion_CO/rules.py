#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.62296e-09,'m^3/(mol*s)'), n=4.14748, w0=(718364,'J/mol'), E0=(395378,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1506352053874501, var=63.47466201412426, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 16.35040268457951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 16.35040268457951""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 16.35040268457951
""",
)

entry(
    index = 2,
    label = "Root_1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(0.199718,'m^3/(mol*s)'), n=2.24177, w0=(753875,'J/mol'), E0=(242102,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.183488841253884, var=322.93110733299676, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 44.02437438338351"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 44.02437438338351""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 44.02437438338351
""",
)

entry(
    index = 3,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(9.0059e-09,'m^3/(mol*s)'), n=4.13839, w0=(713466,'J/mol'), E0=(398523,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17185584066676693, var=53.714118298713394, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 15.124485195328518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.124485195328518""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.124485195328518
""",
)

entry(
    index = 4,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = Arrhenius(A=(2890,'m^3/(mol*s)'), n=1.16, Ea=(343.506,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2.97515e-05,'m^3/(mol*s)'), n=3.24415, w0=(750667,'J/mol'), E0=(155515,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09985991127821993, var=43.21950705372896, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 13.430342378800736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.430342378800736""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.430342378800736
""",
)

entry(
    index = 6,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(4.86587e-19,'m^3/(mol*s)'), n=7.20287, w0=(723500,'J/mol'), E0=(432992,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6054583825336317, var=112.48420212855686, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 22.783185716719306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 22.783185716719306""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 22.783185716719306
""",
)

entry(
    index = 7,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2.3953e-06,'m^3/(mol*s)'), n=3.40222, w0=(708184,'J/mol'), E0=(384299,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23941655519595087, var=18.72859385058981, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 9.27735000048524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 9.27735000048524""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 9.27735000048524
""",
)

entry(
    index = 8,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s",
    kinetics = Arrhenius(A=(5.66811e-11,'m^3/(mol*s)'), n=4.88105, Ea=(180.508,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00925502,'m^3/(mol*s)'), n=2.53089, w0=(692500,'J/mol'), E0=(142134,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054127952330834, var=9.232006363555097, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 6.227230421193242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.227230421193242""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.227230421193242
""",
)

entry(
    index = 10,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->O",
    kinetics = Arrhenius(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, Ea=(223.258,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O",
    kinetics = ArrheniusBM(A=(1.25613e-19,'m^3/(mol*s)'), n=7.37927, w0=(720500,'J/mol'), E0=(438847,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4970880919320776, var=87.2140993526292, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O
    Total Standard Deviation in ln(k): 19.97088308920006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 19.97088308920006""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 19.97088308920006
""",
)

entry(
    index = 12,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R",
    kinetics = ArrheniusBM(A=(5.11355e-06,'m^3/(mol*s)'), n=3.32785, w0=(752167,'J/mol'), E0=(365016,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20622158461342185, var=5.0271348621172365, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R
    Total Standard Deviation in ln(k): 5.013015945875581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 5.013015945875581""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 5.013015945875581
""",
)

entry(
    index = 13,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs",
    kinetics = ArrheniusBM(A=(4.83895e-05,'m^3/(mol*s)'), n=2.98549, w0=(665786,'J/mol'), E0=(415512,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2518057571062162, var=11.385687323707824, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs
    Total Standard Deviation in ln(k): 7.397192029977364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 7.397192029977364""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 7.397192029977364
""",
)

entry(
    index = 14,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs",
    kinetics = ArrheniusBM(A=(0.000170286,'m^3/(mol*s)'), n=3.41521, w0=(675167,'J/mol'), E0=(336819,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21214319061767542, var=25.207455638600557, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs
    Total Standard Deviation in ln(k): 10.598201915211302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 10.598201915211302""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 10.598201915211302
""",
)

entry(
    index = 15,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Br1s",
    kinetics = Arrhenius(A=(0.0152384,'m^3/(mol*s)'), n=2.47236, Ea=(142.16,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Br1s",
    kinetics = Arrhenius(A=(0.006108,'m^3/(mol*s)'), n=2.57909, Ea=(159.246,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(4.35183e-18,'m^3/(mol*s)'), n=6.8479, w0=(720500,'J/mol'), E0=(438342,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8327463012035188, var=104.37565583198128, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R
    Total Standard Deviation in ln(k): 22.573583961854393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R
Total Standard Deviation in ln(k): 22.573583961854393""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R
Total Standard Deviation in ln(k): 22.573583961854393
""",
)

entry(
    index = 18,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.05954e-06,'m^3/(mol*s)'), n=3.3871, w0=(740071,'J/mol'), E0=(361800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20891908640185927, var=6.034143814748373, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
    Total Standard Deviation in ln(k): 5.449452670950615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
Total Standard Deviation in ln(k): 5.449452670950615""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
Total Standard Deviation in ln(k): 5.449452670950615
""",
)

entry(
    index = 19,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0021256,'m^3/(mol*s)'), n=2.9327, w0=(794500,'J/mol'), E0=(386225,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.038040144670983864, var=0.14344916898309887, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.8548653290005049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.8548653290005049""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.8548653290005049
""",
)

entry(
    index = 20,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O",
    kinetics = ArrheniusBM(A=(4.59049e-05,'m^3/(mol*s)'), n=2.97594, w0=(667500,'J/mol'), E0=(414628,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2599211831269906, var=11.9255069437579, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O
    Total Standard Deviation in ln(k): 7.576085556962115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 7.576085556962115""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 7.576085556962115
""",
)

entry(
    index = 21,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->O",
    kinetics = Arrhenius(A=(0.000538,'m^3/(mol*s)'), n=3.29, Ea=(437.228,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s",
    kinetics = Arrhenius(A=(0.000614234,'m^3/(mol*s)'), n=3.16963, Ea=(318.436,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00962594,'m^3/(mol*s)'), n=2.95613, w0=(615500,'J/mol'), E0=(328430,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18731351736347102, var=8.005119587845035, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 6.142698091953715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.142698091953715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.142698091953715
""",
)

entry(
    index = 24,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.0160075,'m^3/(mol*s)'), n=2.60695, w0=(720500,'J/mol'), E0=(333549,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2494841567578414, var=5.184151226712931, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 5.191372035153691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 5.191372035153691""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 5.191372035153691
""",
)

entry(
    index = 25,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.63749e-23,'m^3/(mol*s)'), n=8.18722, w0=(720500,'J/mol'), E0=(451381,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19848249550466338, var=4.671405137340891, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.831620593661288"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.831620593661288""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.831620593661288
""",
)

entry(
    index = 26,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.93187e-05,'m^3/(mol*s)'), n=3.07297, w0=(752167,'J/mol'), E0=(360884,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1893656427344283, var=3.616698684120363, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 4.288322051634823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.288322051634823""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.288322051634823
""",
)

entry(
    index = 27,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(1.49688e-05,'m^3/(mol*s)'), n=3.07573, w0=(667500,'J/mol'), E0=(416352,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2763247367517298, var=11.650153399052751, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R
    Total Standard Deviation in ln(k): 7.536909385308967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R
Total Standard Deviation in ln(k): 7.536909385308967""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R
Total Standard Deviation in ln(k): 7.536909385308967
""",
)

entry(
    index = 28,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s",
    kinetics = Arrhenius(A=(0.0163189,'m^3/(mol*s)'), n=2.90186, Ea=(300.412,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s",
    kinetics = Arrhenius(A=(0.00734196,'m^3/(mol*s)'), n=2.97843, Ea=(311.689,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.26438,'m^3/(mol*s)'), n=1.78982, w0=(720500,'J/mol'), E0=(338372,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23441824057610486, var=10.402855165970266, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 7.054954303195876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 7.054954303195876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 7.054954303195876
""",
)

entry(
    index = 31,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C",
    kinetics = Arrhenius(A=(1.81927e-16,'m^3/(mol*s)'), n=6.80628, Ea=(325.917,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_6R!H->C",
    kinetics = Arrhenius(A=(1.76125e-25,'m^3/(mol*s)'), n=8.86865, Ea=(457.075,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C",
    kinetics = Arrhenius(A=(7.09132e-21,'m^3/(mol*s)'), n=7.51297, Ea=(459.846,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.00873e-05,'m^3/(mol*s)'), n=2.97247, w0=(731000,'J/mol'), E0=(360476,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16750494752417383, var=3.818334100036333, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 4.338230923424657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 4.338230923424657""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 4.338230923424657
""",
)

entry(
    index = 35,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.57255e-05,'m^3/(mol*s)'), n=3.24294, w0=(794500,'J/mol'), E0=(361967,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23244300669039936, var=5.185214704805551, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 5.1490232353310414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.1490232353310414""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.1490232353310414
""",
)

entry(
    index = 36,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(5.25968e-07,'m^3/(mol*s)'), n=3.46483, w0=(667500,'J/mol'), E0=(427234,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3220506709051024, var=2.234697681393165, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R
    Total Standard Deviation in ln(k): 3.806032012065142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R
Total Standard Deviation in ln(k): 3.806032012065142""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R
Total Standard Deviation in ln(k): 3.806032012065142
""",
)

entry(
    index = 37,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(7.15522e-09,'m^3/(mol*s)'), n=4.05272, Ea=(334.996,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R",
    kinetics = Arrhenius(A=(88.9,'m^3/(mol*s)'), n=1.51, Ea=(331.373,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->O_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O",
    kinetics = Arrhenius(A=(5.66674e-08,'m^3/(mol*s)'), n=3.74252, Ea=(331.889,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(0.000303813,'m^3/(mol*s)'), n=2.68832, w0=(709833,'J/mol'), E0=(368524,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1549813378983976, var=1.9635364312510046, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 3.1985603165129217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 3.1985603165129217""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 3.1985603165129217
""",
)

entry(
    index = 41,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R",
    kinetics = Arrhenius(A=(0.000657796,'m^3/(mol*s)'), n=3.03266, Ea=(372.985,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.06388e-07,'m^3/(mol*s)'), n=3.50491, w0=(667500,'J/mol'), E0=(422670,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33426105868651845, var=0.0337183380131677, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 1.2079724623300276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 1.2079724623300276""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 1.2079724623300276
""",
)

entry(
    index = 43,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C",
    kinetics = Arrhenius(A=(8.68834e-07,'m^3/(mol*s)'), n=3.38642, Ea=(433.585,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O",
    kinetics = ArrheniusBM(A=(0.000582592,'m^3/(mol*s)'), n=2.50881, w0=(667500,'J/mol'), E0=(367412,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16163968774428025, var=2.225082732425535, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O
    Total Standard Deviation in ln(k): 3.3965352883712634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 3.3965352883712634""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 3.3965352883712634
""",
)

entry(
    index = 45,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->O",
    kinetics = Arrhenius(A=(0.000113417,'m^3/(mol*s)'), n=3.00792, Ea=(381.427,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C",
    kinetics = Arrhenius(A=(1.17091e-07,'m^3/(mol*s)'), n=3.66153, Ea=(417.423,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.41072e-06,'m^3/(mol*s)'), n=3.34827, Ea=(419.577,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->O_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_8BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(9.05456e-05,'m^3/(mol*s)'), n=2.75561, Ea=(351.94,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_8BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_8BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_N-8BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(0.00374667,'m^3/(mol*s)'), n=2.26207, Ea=(344.875,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_N-8BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_N-8BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_N-8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->O_N-8BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

