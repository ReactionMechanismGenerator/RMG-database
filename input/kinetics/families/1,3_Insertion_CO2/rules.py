#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/rules"
shortDesc = ""
longDesc = """
572 - 575 Some of the tortional motions in the alkyl part of the 
transition states are treated as free rotations as they are relatively loose TSs. 

The dictionary defines CO2 in two ways, allowing the R-R' to insert either way
around. However, there are only rates for one of these ways. The other is
presumably matching the top level node.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.07136e-40,'m^3/(mol*s)'), n=13.4617, w0=(828.043,'kJ/mol'), E0=(191.474,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45335526580941204, var=66.8168716805179, Tref=1000.0, N=23, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 23 training reactions at node Root
    Total Standard Deviation in ln(k): 17.526106407064507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root
Total Standard Deviation in ln(k): 17.526106407064507""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root
Total Standard Deviation in ln(k): 17.526106407064507
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = Arrhenius(A=(2.45635e-08,'m^3/(mol*s)'), n=4.04584, Ea=(168.086,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 1 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(4.43984e-43,'m^3/(mol*s)'), n=14.1534, w0=(821.364,'kJ/mol'), E0=(193.798,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47958712556711075, var=52.99928014755814, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 22 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 15.799585326356816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 15.799585326356816""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 15.799585326356816
""",
)

entry(
    index = 4,
    label = "Root_N-4R->F_5R->C",
    kinetics = ArrheniusBM(A=(3.12797e-09,'m^3/(mol*s)'), n=4.08752, w0=(767.75,'kJ/mol'), E0=(288.091,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3979291114851909, var=46.886551895422684, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_5R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_5R->C
    Total Standard Deviation in ln(k): 14.726995837331117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_5R->C
Total Standard Deviation in ln(k): 14.726995837331117""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_5R->C
Total Standard Deviation in ln(k): 14.726995837331117
""",
)

entry(
    index = 5,
    label = "Root_N-4R->F_N-5R->C",
    kinetics = ArrheniusBM(A=(2.60566e-46,'m^3/(mol*s)'), n=15.1129, w0=(833.278,'kJ/mol'), E0=(184.834,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4847383601931309, var=56.449367076592786, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C',), comment="""BM rule fitted to 18 training reactions at node Root_N-4R->F_N-5R->C
    Total Standard Deviation in ln(k): 16.280070302346786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-4R->F_N-5R->C
Total Standard Deviation in ln(k): 16.280070302346786""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-4R->F_N-5R->C
Total Standard Deviation in ln(k): 16.280070302346786
""",
)

entry(
    index = 6,
    label = "Root_N-4R->F_5R->C_4BrCClHILiNOPSSi->C",
    kinetics = Arrhenius(A=(7.3e-05,'m^3/(mol*s)'), n=3.13, Ea=(493.712,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_5R->C_4BrCClHILiNOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_4BrCClHILiNOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(3.21883e-09,'m^3/(mol*s)'), n=4.08284, w0=(775.167,'kJ/mol'), E0=(287.506,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.36541538390720274, var=45.64889297830392, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C
    Total Standard Deviation in ln(k): 14.462914063718879"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 14.462914063718879""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 14.462914063718879
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(5.64286e-46,'m^3/(mol*s)'), n=15.0051, w0=(828.5,'kJ/mol'), E0=(186.28,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5467808866900148, var=62.365326093410516, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C',), comment="""BM rule fitted to 16 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C
    Total Standard Deviation in ln(k): 17.205559106890508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 17.205559106890508""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 17.205559106890508
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(7.37882e-49,'m^3/(mol*s)'), n=15.9782, w0=(871.5,'kJ/mol'), E0=(171.409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7699743966629304, var=1.0055606467792602, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C
    Total Standard Deviation in ln(k): 3.944910199030417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 3.944910199030417""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 3.944910199030417
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->N",
    kinetics = Arrhenius(A=(3.99078e-08,'m^3/(mol*s)'), n=3.39053, Ea=(304.609,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N",
    kinetics = ArrheniusBM(A=(2.63739e-10,'m^3/(mol*s)'), n=4.58366, w0=(810.5,'kJ/mol'), E0=(283.874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5589330845772869, var=107.03357152488856, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N
    Total Standard Deviation in ln(k): 22.144748281341933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N
Total Standard Deviation in ln(k): 22.144748281341933""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N
Total Standard Deviation in ln(k): 22.144748281341933
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.76757e-46,'m^3/(mol*s)'), n=15.0064, w0=(828.5,'kJ/mol'), E0=(184.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.574784379305225, var=69.53698796644322, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 18.16143531111665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 18.16143531111665""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 18.16143531111665
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N_Ext-5C-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(1.15601e-09,'m^3/(mol*s)'), n=4.43694, Ea=(287.389,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N_Ext-5C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N_Ext-5C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->N_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1",
    kinetics = ArrheniusBM(A=(1.382e-13,'m^3/(mol*s)'), n=5.14738, w0=(828.5,'kJ/mol'), E0=(106.041,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5321773278466484, var=12.173383687517438, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1
    Total Standard Deviation in ln(k): 8.331725117515044"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 8.331725117515044""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 8.331725117515044
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1",
    kinetics = ArrheniusBM(A=(2.23564e-51,'m^3/(mol*s)'), n=16.6413, w0=(828.5,'kJ/mol'), E0=(201.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5502511888179683, var=7.607364484990715, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1
    Total Standard Deviation in ln(k): 6.911890939491869"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 6.911890939491869""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 6.911890939491869
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1_Ext-4C-R",
    kinetics = Arrhenius(A=(2.10377e-14,'m^3/(mol*s)'), n=5.39092, Ea=(133.97,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O",
    kinetics = ArrheniusBM(A=(4.60364e-45,'m^3/(mol*s)'), n=14.8486, w0=(828.5,'kJ/mol'), E0=(202.006,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.556538527841711, var=4.053067926443998, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O
    Total Standard Deviation in ln(k): 5.434317313452676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O
Total Standard Deviation in ln(k): 5.434317313452676""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O
Total Standard Deviation in ln(k): 5.434317313452676
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.15723e-55,'m^3/(mol*s)'), n=17.7765, w0=(828.5,'kJ/mol'), E0=(205.8,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45984246246162397, var=1.3628816735458817, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O
    Total Standard Deviation in ln(k): 3.49576138539793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O
Total Standard Deviation in ln(k): 3.49576138539793""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O
Total Standard Deviation in ln(k): 3.49576138539793
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.47732e-42,'m^3/(mol*s)'), n=14.2134, w0=(828.5,'kJ/mol'), E0=(204.541,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.657673630949881, var=0.2537614281038658, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 2.6623263621912887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 2.6623263621912887""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 2.6623263621912887
""",
)

entry(
    index = 20,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R",
    kinetics = Arrhenius(A=(2.17633e-48,'m^3/(mol*s)'), n=15.6938, Ea=(206.967,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F",
    kinetics = ArrheniusBM(A=(1.09579e-58,'m^3/(mol*s)'), n=18.7325, w0=(828.5,'kJ/mol'), E0=(199.378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5059646668535649, var=0.4704868262309178, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F
    Total Standard Deviation in ln(k): 2.6463567387901987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F
Total Standard Deviation in ln(k): 2.6463567387901987""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F
Total Standard Deviation in ln(k): 2.6463567387901987
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F",
    kinetics = ArrheniusBM(A=(0.0352626,'m^3/(mol*s)'), n=2.34043, w0=(828.5,'kJ/mol'), E0=(309.89,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.385671106975245, var=3.341635576780217, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F
    Total Standard Deviation in ln(k): 4.633706884883318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F
Total Standard Deviation in ln(k): 4.633706884883318""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F
Total Standard Deviation in ln(k): 4.633706884883318
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C",
    kinetics = ArrheniusBM(A=(7.08572e-41,'m^3/(mol*s)'), n=13.6708, w0=(828.5,'kJ/mol'), E0=(204.421,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6862832810020018, var=0.32368497394357704, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C
    Total Standard Deviation in ln(k): 2.864890173146807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 2.864890173146807""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 2.864890173146807
""",
)

entry(
    index = 24,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C",
    kinetics = Arrhenius(A=(6.7151e-46,'m^3/(mol*s)'), n=15.2932, Ea=(217.498,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.8159e-58,'m^3/(mol*s)'), n=18.5401, w0=(828.5,'kJ/mol'), E0=(199.252,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5100656931529022, var=0.3687952964931024, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.4990180066454335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.4990180066454335""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.4990180066454335
""",
)

entry(
    index = 26,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(3.78787e-61,'m^3/(mol*s)'), n=19.4705, Ea=(233.815,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R",
    kinetics = Arrhenius(A=(0.106,'m^3/(mol*s)'), n=2.13, Ea=(322.168,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = Arrhenius(A=(1.23235e-39,'m^3/(mol*s)'), n=13.3058, Ea=(214.361,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = Arrhenius(A=(4.0741e-42,'m^3/(mol*s)'), n=14.0358, Ea=(212.142,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.54485e-58,'m^3/(mol*s)'), n=18.529, w0=(828.5,'kJ/mol'), E0=(198.625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48400673925739457, var=0.6069498225551314, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.7779259797570823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.7779259797570823""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.7779259797570823
""",
)

entry(
    index = 31,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(5.76471e-58,'m^3/(mol*s)'), n=18.5725, Ea=(232.258,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(3.90079e-58,'m^3/(mol*s)'), n=18.5063, Ea=(231.893,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(5.22281e-58,'m^3/(mol*s)'), n=18.5326, w0=(828.5,'kJ/mol'), E0=(198.324,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5292811539623676, var=0.9161100922972057, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 3.2486570648504642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 3.2486570648504642""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 3.2486570648504642
""",
)

entry(
    index = 34,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0",
    kinetics = Arrhenius(A=(3.23183e-56,'m^3/(mol*s)'), n=18.045, Ea=(233.567,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0",
    kinetics = Arrhenius(A=(7.55543e-60,'m^3/(mol*s)'), n=19.034, Ea=(224.389,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

