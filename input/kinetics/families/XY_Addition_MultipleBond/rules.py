#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(247.077,'m^3/(mol*s)'), n=1.0272, w0=(763580,'J/mol'), E0=(219149,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0004274223418148638, var=12.722272212372781, Tref=1000.0, N=44, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 44 training reactions at node Root
    Total Standard Deviation in ln(k): 7.1516220072194905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root
Total Standard Deviation in ln(k): 7.1516220072194905""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root
Total Standard Deviation in ln(k): 7.1516220072194905
""",
)

entry(
    index = 2,
    label = "YY",
    kinetics = ArrheniusBM(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, w0=(575000,'J/mol'), E0=(140198,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='YY',), comment="""BM rule fitted to 1 training reactions at node YY
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node YY
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node YY
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "HY",
    kinetics = ArrheniusBM(A=(128.536,'m^3/(mol*s)'), n=1.11556, w0=(767965,'J/mol'), E0=(220440,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013833068990515033, var=12.168128856577649, Tref=1000.0, N=43, data_mean=0.0, correlation='HY',), comment="""BM rule fitted to 43 training reactions at node HY
    Total Standard Deviation in ln(k): 7.02784278161077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 43 training reactions at node HY
Total Standard Deviation in ln(k): 7.02784278161077""",
    longDesc = 
"""
BM rule fitted to 43 training reactions at node HY
Total Standard Deviation in ln(k): 7.02784278161077
""",
)

entry(
    index = 4,
    label = "HF",
    kinetics = ArrheniusBM(A=(0.158098,'m^3/(mol*s)'), n=2.01821, w0=(870853,'J/mol'), E0=(254279,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1442917023547015, var=22.7949768521676, Tref=1000.0, N=17, data_mean=0.0, correlation='HF',), comment="""BM rule fitted to 17 training reactions at node HF
    Total Standard Deviation in ln(k): 9.933966228188362"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node HF
Total Standard Deviation in ln(k): 9.933966228188362""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node HF
Total Standard Deviation in ln(k): 9.933966228188362
""",
)

entry(
    index = 5,
    label = "HCl",
    kinetics = ArrheniusBM(A=(4381.22,'m^3/(mol*s)'), n=0.635957, w0=(714278,'J/mol'), E0=(213925,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008636259553422284, var=2.9794354489891894, Tref=1000.0, N=18, data_mean=0.0, correlation='HCl',), comment="""BM rule fitted to 18 training reactions at node HCl
    Total Standard Deviation in ln(k): 3.4820806304431966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node HCl
Total Standard Deviation in ln(k): 3.4820806304431966""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node HCl
Total Standard Deviation in ln(k): 3.4820806304431966
""",
)

entry(
    index = 6,
    label = "HBr",
    kinetics = ArrheniusBM(A=(1.00271e-07,'m^3/(mol*s)'), n=3.78598, w0=(670125,'J/mol'), E0=(197782,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.301177653173562, var=23.099811026665936, Tref=1000.0, N=8, data_mean=0.0, correlation='HBr',), comment="""BM rule fitted to 8 training reactions at node HBr
    Total Standard Deviation in ln(k): 12.904500993454715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node HBr
Total Standard Deviation in ln(k): 12.904500993454715""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node HBr
Total Standard Deviation in ln(k): 12.904500993454715
""",
)

entry(
    index = 7,
    label = "HF_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.165834,'m^3/(mol*s)'), n=2.03144, w0=(857350,'J/mol'), E0=(265963,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009904598100702992, var=19.820965103745564, Tref=1000.0, N=10, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 10 training reactions at node HF_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 8.950115335663156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node HF_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 8.950115335663156""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node HF_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 8.950115335663156
""",
)

entry(
    index = 8,
    label = "HF_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.56721e+32,'m^3/(mol*s)'), n=-7.40875, w0=(847000,'J/mol'), E0=(355628,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node HF_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "HF_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(0.0403022,'m^3/(mol*s)'), n=2.1385, w0=(897333,'J/mol'), E0=(222764,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.327984587034131, var=218.62407586677293, Tref=1000.0, N=6, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 6 training reactions at node HF_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 48.05391781888977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node HF_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 48.05391781888977""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node HF_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 48.05391781888977
""",
)

entry(
    index = 10,
    label = "HCl_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(1435.14,'m^3/(mol*s)'), n=0.679021, w0=(711000,'J/mol'), E0=(209355,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01702258866269468, var=2.370517720324283, Tref=1000.0, N=12, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 12 training reactions at node HCl_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 3.1293578192068905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node HCl_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 3.1293578192068905""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node HCl_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 3.1293578192068905
""",
)

entry(
    index = 11,
    label = "HCl_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(170.285,'m^3/(mol*s)'), n=1.26128, w0=(720833,'J/mol'), E0=(218262,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.041735562822434034, var=5.376647654180947, Tref=1000.0, N=6, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 6 training reactions at node HCl_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 4.75336260871227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node HCl_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 4.75336260871227""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node HCl_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 4.75336260871227
""",
)

entry(
    index = 12,
    label = "HBr_3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(645500,'J/mol'), E0=(275727,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node HBr_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "HBr_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.16672e-05,'m^3/(mol*s)'), n=3.2052, w0=(673643,'J/mol'), E0=(194613,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05501937785949342, var=23.39179645315067, Tref=1000.0, N=7, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 7 training reactions at node HBr_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 9.834154150812303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node HBr_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 9.834154150812303""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node HBr_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 9.834154150812303
""",
)

entry(
    index = 14,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.145694,'m^3/(mol*s)'), n=2.04868, w0=(858500,'J/mol'), E0=(265899,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00906637076369402, var=20.10777890494391, Tref=1000.0, N=7, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 7 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 9.01235234161528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 9.01235234161528""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 9.01235234161528
""",
)

entry(
    index = 15,
    label = "HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(0.430132,'m^3/(mol*s)'), n=1.71044, w0=(858500,'J/mol'), E0=(243799,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0002592053915667386, var=0.023805321282881098, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 0.3099613068852112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 0.3099613068852112""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 0.3099613068852112
""",
)

entry(
    index = 16,
    label = "HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(1.64483e+40,'m^3/(mol*s)'), n=-10.004, w0=(847000,'J/mol'), E0=(368699,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd",
    kinetics = ArrheniusBM(A=(0.711846,'m^3/(mol*s)'), n=1.73819, w0=(858500,'J/mol'), E0=(236816,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.6286913328141925, var=14.469088428009858, Tref=1000.0, N=4, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd',), comment="""BM rule fitted to 4 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd
    Total Standard Deviation in ln(k): 14.230414498937108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd
Total Standard Deviation in ln(k): 14.230414498937108""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd
Total Standard Deviation in ln(k): 14.230414498937108
""",
)

entry(
    index = 18,
    label = "HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd",
    kinetics = ArrheniusBM(A=(1.50125e-09,'m^3/(mol*s)'), n=4.53481, w0=(975000,'J/mol'), E0=(136930,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.227846444099074, var=40.86360846036479, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd',), comment="""BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd
    Total Standard Deviation in ln(k): 23.437928526028873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd
Total Standard Deviation in ln(k): 23.437928526028873""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd
Total Standard Deviation in ln(k): 23.437928526028873
""",
)

entry(
    index = 19,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(55.9963,'m^3/(mol*s)'), n=1.07423, w0=(711000,'J/mol'), E0=(207294,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03317689213029003, var=3.30896533554926, Tref=1000.0, N=7, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R
    Total Standard Deviation in ln(k): 3.7300847294514337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 3.7300847294514337""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 3.7300847294514337
""",
)

entry(
    index = 20,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.67537e+06,'m^3/(mol*s)'), n=-0.427308, w0=(711000,'J/mol'), E0=(214377,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011499404137086623, var=1.1478140395402414, Tref=1000.0, N=3, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.1506839447115147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1506839447115147""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1506839447115147
""",
)

entry(
    index = 21,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.869146,'m^3/(mol*s)'), n=2.05209, w0=(699500,'J/mol'), E0=(218809,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005713380450709146, var=2.2234217355135737, Tref=1000.0, N=2, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R
    Total Standard Deviation in ln(k): 3.0036442881083776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R
Total Standard Deviation in ln(k): 3.0036442881083776""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R
Total Standard Deviation in ln(k): 3.0036442881083776
""",
)

entry(
    index = 22,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.13622e-08,'m^3/(mol*s)'), n=4.19281, w0=(763500,'J/mol'), E0=(185671,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.395944296303954, var=218.07838787030826, Tref=1000.0, N=2, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 48.18765450187803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 48.18765450187803""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 48.18765450187803
""",
)

entry(
    index = 23,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R",
    kinetics = ArrheniusBM(A=(0.000199725,'m^3/(mol*s)'), n=2.85909, w0=(657000,'J/mol'), E0=(207374,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10021767310317693, var=21.973824872916857, Tref=1000.0, N=4, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R',), comment="""BM rule fitted to 4 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R
    Total Standard Deviation in ln(k): 9.649248767178477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R
Total Standard Deviation in ln(k): 9.649248767178477""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R
Total Standard Deviation in ln(k): 9.649248767178477
""",
)

entry(
    index = 24,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0802844,'m^3/(mol*s)'), n=2.08675, w0=(715250,'J/mol'), E0=(171483,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.892411430688644, var=181.88006960927544, Tref=1000.0, N=2, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 44.35405912545515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 44.35405912545515""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 44.35405912545515
""",
)

entry(
    index = 25,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F",
    kinetics = ArrheniusBM(A=(130.91,'m^3/(mol*s)'), n=1.02648, w0=(858500,'J/mol'), E0=(225552,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06024987956517272, var=6.694627063510916, Tref=1000.0, N=4, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F',), comment="""BM rule fitted to 4 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F
    Total Standard Deviation in ln(k): 5.338428614935718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 5.338428614935718""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 5.338428614935718
""",
)

entry(
    index = 26,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(0.112882,'m^3/(mol*s)'), n=2.08157, w0=(858500,'J/mol'), E0=(265942,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01012307352917687, var=20.293111147497633, Tref=1000.0, N=3, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F',), comment="""BM rule fitted to 3 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F
    Total Standard Deviation in ln(k): 9.056340537412042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 9.056340537412042""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 9.056340537412042
""",
)

entry(
    index = 27,
    label = "HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(52.9173,'m^3/(mol*s)'), n=1.09798, w0=(858500,'J/mol'), E0=(249103,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.707837,'m^3/(mol*s)'), n=1.7387, w0=(858500,'J/mol'), E0=(236903,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.7429514059337947, var=15.57170963752324, Tref=1000.0, N=3, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 14.802723916912289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 14.802723916912289""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 14.802723916912289
""",
)

entry(
    index = 29,
    label = "HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd",
    kinetics = ArrheniusBM(A=(7.80335e-09,'m^3/(mol*s)'), n=4.28272, w0=(975000,'J/mol'), E0=(135013,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd",
    kinetics = ArrheniusBM(A=(0.109156,'m^3/(mol*s)'), n=1.86531, w0=(975000,'J/mol'), E0=(170750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_N-3CdO2d->Cd_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(2713.63,'m^3/(mol*s)'), n=0.572028, w0=(711000,'J/mol'), E0=(208352,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003225129163285609, var=3.412723312204887, Tref=1000.0, N=6, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.7115622365534726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.7115622365534726""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.7115622365534726
""",
)

entry(
    index = 32,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.18057,'m^3/(mol*s)'), n=1.62936, w0=(711000,'J/mol'), E0=(219824,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, w0=(711000,'J/mol'), E0=(215085,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.1566e+06,'m^3/(mol*s)'), n=-0.375399, w0=(711000,'J/mol'), E0=(211963,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, w0=(711000,'J/mol'), E0=(212590,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(40.7026,'m^3/(mol*s)'), n=1.65435, w0=(699500,'J/mol'), E0=(223829,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-3COCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.62705,'m^3/(mol*s)'), n=1.85266, w0=(699500,'J/mol'), E0=(213680,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_3COCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(1.09358e-06,'m^3/(mol*s)'), n=3.74071, w0=(827500,'J/mol'), E0=(114319,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_N-3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-3COCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.18878,'m^3/(mol*s)'), n=1.76475, w0=(657000,'J/mol'), E0=(179631,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.239222,'m^3/(mol*s)'), n=1.96737, w0=(657000,'J/mol'), E0=(226782,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01405662458527905, var=13.879295328941307, Tref=1000.0, N=3, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 7.503943906209868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.503943906209868""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.503943906209868
""",
)

entry(
    index = 41,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd",
    kinetics = ArrheniusBM(A=(6.29599,'m^3/(mol*s)'), n=1.45405, w0=(657000,'J/mol'), E0=(182401,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_3COCdCddO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd",
    kinetics = ArrheniusBM(A=(2.0193e-06,'m^3/(mol*s)'), n=3.68936, w0=(773500,'J/mol'), E0=(105799,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-4COCdCddCtO2d-R_N-3COCdCddO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(148.811,'m^3/(mol*s)'), n=0.941619, w0=(858500,'J/mol'), E0=(215322,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012824852924365986, var=24.354166144100567, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 9.925578901029967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 9.925578901029967""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 9.925578901029967
""",
)

entry(
    index = 44,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4.14111,'m^3/(mol*s)'), n=1.29695, w0=(858500,'J/mol'), E0=(229024,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C",
    kinetics = ArrheniusBM(A=(3.17276,'m^3/(mol*s)'), n=1.63179, w0=(858500,'J/mol'), E0=(243320,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.182995,'m^3/(mol*s)'), n=2.01011, w0=(858500,'J/mol'), E0=(278045,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002781781410684276, var=20.479442798937797, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C
    Total Standard Deviation in ln(k): 9.079261296313975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C
Total Standard Deviation in ln(k): 9.079261296313975""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C
Total Standard Deviation in ln(k): 9.079261296313975
""",
)

entry(
    index = 47,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.138693,'m^3/(mol*s)'), n=1.88884, w0=(858500,'J/mol'), E0=(208822,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0030289162982661804, var=2.0738456968621537, Tref=1000.0, N=2, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F
    Total Standard Deviation in ln(k): 2.8945998756167213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 2.8945998756167213""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 2.8945998756167213
""",
)

entry(
    index = 48,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(25.0352,'m^3/(mol*s)'), n=1.25316, w0=(858500,'J/mol'), E0=(238919,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(2319.81,'m^3/(mol*s)'), n=0.57284, w0=(711000,'J/mol'), E0=(205932,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0037359137489393407, var=13.17307805141431, Tref=1000.0, N=3, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R',), comment="""BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
    Total Standard Deviation in ln(k): 7.285519601235778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.285519601235778""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.285519601235778
""",
)

entry(
    index = 50,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, w0=(711000,'J/mol'), E0=(220112,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R",
    kinetics = ArrheniusBM(A=(14.4535,'m^3/(mol*s)'), n=1.42908, w0=(657000,'J/mol'), E0=(239925,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.019405123982718337, var=14.49726876971505, Tref=1000.0, N=2, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R',), comment="""BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R
    Total Standard Deviation in ln(k): 7.681841348118741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R
Total Standard Deviation in ln(k): 7.681841348118741""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R
Total Standard Deviation in ln(k): 7.681841348118741
""",
)

entry(
    index = 52,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(26.4943,'m^3/(mol*s)'), n=1.22463, w0=(858500,'J/mol'), E0=(202816,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(12.2191,'m^3/(mol*s)'), n=1.4473, w0=(858500,'J/mol'), E0=(293945,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-6R!H->F_N-5R!H->C_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(10.477,'m^3/(mol*s)'), n=1.29062, w0=(858500,'J/mol'), E0=(214595,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(415.056,'m^3/(mol*s)'), n=0.819164, w0=(711000,'J/mol'), E0=(200058,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0015583992925488114, var=35.8340817495606, Tref=1000.0, N=2, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.004575517732196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.004575517732196""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.004575517732196
""",
)

entry(
    index = 56,
    label = "HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.882649,'m^3/(mol*s)'), n=1.68333, w0=(657000,'J/mol'), E0=(219941,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HBr_N-3COCdCddCtO2d->Ct_Ext-3COCdCddO2d-R_N-5R!H->C_Ext-3COCdCddO2d-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, w0=(711000,'J/mol'), E0=(210237,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node HCl_3COCdCddCtO2d->Cd_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

