#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond_Disprop/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(0.0271662,'m^3/(mol*s)'), n=2.49517, Ea=(64.7926,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-3.239112411997989e-15, var=193.84791188496004, Tref=1000.0, N=10, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 10 training reactions at node Root
    Total Standard Deviation in ln(k): 27.91178126271385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root
Total Standard Deviation in ln(k): 27.91178126271385""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root
Total Standard Deviation in ln(k): 27.91178126271385
""",
)

entry(
    index = 2,
    label = "Root_6R->C",
    kinetics = ArrheniusBM(A=(3.15619e-86,'m^3/(mol*s)'), n=26.7192, w0=(894167,'J/mol'), E0=(46852.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-12.303881331467172, var=283.4495433123181, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6R->C',), comment="""BM rule fitted to 3 training reactions at node Root_6R->C
    Total Standard Deviation in ln(k): 64.66591392991442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6R->C
Total Standard Deviation in ln(k): 64.66591392991442""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6R->C
Total Standard Deviation in ln(k): 64.66591392991442
""",
)

entry(
    index = 3,
    label = "Root_N-6R->C",
    kinetics = ArrheniusBM(A=(6.38629e-10,'m^3/(mol*s)'), n=5.01232, w0=(839700,'J/mol'), E0=(42358.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3486251103732024, var=32.50973963455866, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-6R->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-6R->C
    Total Standard Deviation in ln(k): 12.306403195217383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-6R->C
Total Standard Deviation in ln(k): 12.306403195217383""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-6R->C
Total Standard Deviation in ln(k): 12.306403195217383
""",
)

entry(
    index = 4,
    label = "Root_6R->C_1R!H->O",
    kinetics = ArrheniusBM(A=(1.39799e-07,'m^3/(mol*s)'), n=3.57559, w0=(927000,'J/mol'), E0=(311318,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0012723034945842692, var=7.730853098691835, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6R->C_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_6R->C_1R!H->O
    Total Standard Deviation in ln(k): 5.577244686167825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6R->C_1R!H->O
Total Standard Deviation in ln(k): 5.577244686167825""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6R->C_1R!H->O
Total Standard Deviation in ln(k): 5.577244686167825
""",
)

entry(
    index = 5,
    label = "Root_6R->C_N-1R!H->O",
    kinetics = ArrheniusBM(A=(1.4888e-10,'m^3/(mol*s)'), n=4.19462, w0=(828500,'J/mol'), E0=(180895,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6R->C_N-1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_6R->C_N-1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6R->C_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6R->C_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-6R->C_5R!H->O",
    kinetics = ArrheniusBM(A=(17.4272,'m^3/(mol*s)'), n=2.05933, w0=(912800,'J/mol'), E0=(71801.6,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6R->C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-6R->C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6R->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6R->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-6R->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(6.07408e-14,'m^3/(mol*s)'), n=6.16784, w0=(827517,'J/mol'), E0=(38591.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24958505178039272, var=23.176332624765248, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-6R->C_N-5R!H->O
    Total Standard Deviation in ln(k): 10.278254374583724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-6R->C_N-5R!H->O
Total Standard Deviation in ln(k): 10.278254374583724""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-6R->C_N-5R!H->O
Total Standard Deviation in ln(k): 10.278254374583724
""",
)

entry(
    index = 8,
    label = "Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.0523e-05,'m^3/(mol*s)'), n=2.58803, w0=(927000,'J/mol'), E0=(303780,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(7.34475e-07,'m^3/(mol*s)'), n=3.69312, w0=(927000,'J/mol'), E0=(324410,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6R->C_1R!H->O_Ext-6C-R_Ext-2R!H-R_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-6R->C_N-5R!H->O_3R!H->N",
    kinetics = ArrheniusBM(A=(2454.37,'m^3/(mol*s)'), n=0.869935, w0=(741700,'J/mol'), E0=(36959.9,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-6R->C_N-5R!H->O_N-3R!H->N",
    kinetics = ArrheniusBM(A=(6.20657e-22,'m^3/(mol*s)'), n=8.62015, w0=(844680,'J/mol'), E0=(31266.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1927918407978226, var=30.008917614176156, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O_N-3R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N
    Total Standard Deviation in ln(k): 16.491545334831162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N
Total Standard Deviation in ln(k): 16.491545334831162""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N
Total Standard Deviation in ln(k): 16.491545334831162
""",
)

entry(
    index = 12,
    label = "Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(0.46421,'m^3/(mol*s)'), n=2.48921, w0=(862800,'J/mol'), E0=(160707,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9740844970383028, var=15.80467678293062, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R
    Total Standard Deviation in ln(k): 10.417292081901635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.417292081901635""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.417292081901635
""",
)

entry(
    index = 13,
    label = "Root_N-6R->C_N-5R!H->O_N-3R!H->N_1R!H->O",
    kinetics = ArrheniusBM(A=(0.419384,'m^3/(mol*s)'), n=2.21898, w0=(918800,'J/mol'), E0=(91880,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O_N-3R!H->N_1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-6R->C_N-5R!H->O_N-3R!H->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(0.162517,'m^3/(mol*s)'), n=2.55635, w0=(716200,'J/mol'), E0=(71168.6,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O_N-3R!H->N_N-1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_N-1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O",
    kinetics = ArrheniusBM(A=(4.85951e-13,'m^3/(mol*s)'), n=6.00401, w0=(918800,'J/mol'), E0=(91880,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.3077867121327724, var=8.321711718087771, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O
    Total Standard Deviation in ln(k): 14.094156787848377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O
Total Standard Deviation in ln(k): 14.094156787848377""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O
Total Standard Deviation in ln(k): 14.094156787848377
""",
)

entry(
    index = 16,
    label = "Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_N-1R!H->O",
    kinetics = ArrheniusBM(A=(0.15629,'m^3/(mol*s)'), n=2.72776, w0=(750800,'J/mol'), E0=(166566,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_N-1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_N-1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(95.603,'m^3/(mol*s)'), n=1.70021, w0=(918800,'J/mol'), E0=(91880,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.23949,'m^3/(mol*s)'), n=2.34337, w0=(918800,'J/mol'), E0=(91880,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6R->C_N-5R!H->O_N-3R!H->N_Ext-2R!H-R_1R!H->O_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

