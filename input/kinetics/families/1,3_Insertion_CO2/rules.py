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
    kinetics = ArrheniusBM(A=(1.07099e-40,'m^3/(mol*s)'), n=13.4618, w0=(828043,'J/mol'), E0=(191462,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45191668992837025, var=66.81664672430327, Tref=1000.0, N=23, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 23 training reactions at node Root
    Total Standard Deviation in ln(k): 17.522464309210044"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root
Total Standard Deviation in ln(k): 17.522464309210044""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root
Total Standard Deviation in ln(k): 17.522464309210044
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
    kinetics = ArrheniusBM(A=(4.43486e-43,'m^3/(mol*s)'), n=14.1535, w0=(821364,'J/mol'), E0=(193785,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47814454042466226, var=52.99900598696253, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 22 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 15.79592299225378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 15.79592299225378""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 15.79592299225378
""",
)

entry(
    index = 4,
    label = "Root_N-4R->F_5R->C",
    kinetics = ArrheniusBM(A=(3.12857e-09,'m^3/(mol*s)'), n=4.0875, w0=(767750,'J/mol'), E0=(288074,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3958139426290338, var=46.88600194351812, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_5R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_5R->C
    Total Standard Deviation in ln(k): 14.721600836609937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_5R->C
Total Standard Deviation in ln(k): 14.721600836609937""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_5R->C
Total Standard Deviation in ln(k): 14.721600836609937
""",
)

entry(
    index = 5,
    label = "Root_N-4R->F_N-5R->C",
    kinetics = ArrheniusBM(A=(2.6e-46,'m^3/(mol*s)'), n=15.1132, w0=(833278,'J/mol'), E0=(184820,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48336537229205645, var=56.44906477667637, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C',), comment="""BM rule fitted to 18 training reactions at node Root_N-4R->F_N-5R->C
    Total Standard Deviation in ln(k): 16.276580253274155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-4R->F_N-5R->C
Total Standard Deviation in ln(k): 16.276580253274155""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-4R->F_N-5R->C
Total Standard Deviation in ln(k): 16.276580253274155
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
    kinetics = ArrheniusBM(A=(3.21934e-09,'m^3/(mol*s)'), n=4.08282, w0=(775167,'J/mol'), E0=(287488,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3633073998423729, var=45.648326934967706, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C
    Total Standard Deviation in ln(k): 14.45753364385355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 14.45753364385355""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 14.45753364385355
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(5.63085e-46,'m^3/(mol*s)'), n=15.0054, w0=(828500,'J/mol'), E0=(186266,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5453965109129857, var=62.36493934700616, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C',), comment="""BM rule fitted to 16 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C
    Total Standard Deviation in ln(k): 17.202031686999533"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 17.202031686999533""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 17.202031686999533
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C",
    kinetics = ArrheniusBM(A=(7.37882e-49,'m^3/(mol*s)'), n=15.9782, w0=(871500,'J/mol'), E0=(171399,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7699743966629601, var=1.0055606467793836, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C
    Total Standard Deviation in ln(k): 3.9449101990306157"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 3.9449101990306157""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_N-4BrCClHILiNOPSSi->C
Total Standard Deviation in ln(k): 3.9449101990306157
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H",
    kinetics = ArrheniusBM(A=(2.63764e-10,'m^3/(mol*s)'), n=4.58365, w0=(810500,'J/mol'), E0=(283856,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5589330845772863, var=107.03357152488849, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H
    Total Standard Deviation in ln(k): 22.144748281341922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H
Total Standard Deviation in ln(k): 22.144748281341922""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H
Total Standard Deviation in ln(k): 22.144748281341922
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->H",
    kinetics = Arrhenius(A=(3.99078e-08,'m^3/(mol*s)'), n=3.39053, Ea=(304.609,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_N-4HN->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.75284e-46,'m^3/(mol*s)'), n=15.0067, w0=(828500,'J/mol'), E0=(184016,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5734149780643178, var=69.53651834975973, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 18.15793815456435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 18.15793815456435""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 18.15793815456435
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H_Ext-5C-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(1.15601e-09,'m^3/(mol*s)'), n=4.43694, Ea=(287.389,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H_Ext-5C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H_Ext-5C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_5R->C_N-4BrCClHILiNOPSSi->C_4HN->H_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1",
    kinetics = ArrheniusBM(A=(1.38198e-13,'m^3/(mol*s)'), n=5.14738, w0=(828500,'J/mol'), E0=(106034,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5321773278466547, var=12.173383687517147, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1
    Total Standard Deviation in ln(k): 8.331725117514978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 8.331725117514978""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 8.331725117514978
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1",
    kinetics = ArrheniusBM(A=(2.23437e-51,'m^3/(mol*s)'), n=16.6414, w0=(828500,'J/mol'), E0=(201499,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5487436315351242, var=7.607303403640793, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1
    Total Standard Deviation in ln(k): 6.908080908840122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 6.908080908840122""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 6.908080908840122
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
    kinetics = ArrheniusBM(A=(4.60368e-45,'m^3/(mol*s)'), n=14.8486, w0=(828500,'J/mol'), E0=(201994,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5550982139878436, var=4.053103421778447, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O
    Total Standard Deviation in ln(k): 5.430716107223335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O
Total Standard Deviation in ln(k): 5.430716107223335""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O
Total Standard Deviation in ln(k): 5.430716107223335
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.15721e-55,'m^3/(mol*s)'), n=17.7765, w0=(828500,'J/mol'), E0=(205787,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4582250930504244, var=1.362889005925966, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O
    Total Standard Deviation in ln(k): 3.491703938833771"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O
Total Standard Deviation in ln(k): 3.491703938833771""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O
Total Standard Deviation in ln(k): 3.491703938833771
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.47731e-42,'m^3/(mol*s)'), n=14.2134, w0=(828500,'J/mol'), E0=(204529,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6562092941508039, var=0.2537563724196329, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 2.6586370640417463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 2.6586370640417463""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 2.6586370640417463
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
    kinetics = ArrheniusBM(A=(1.09578e-58,'m^3/(mol*s)'), n=18.7325, w0=(828500,'J/mol'), E0=(199364,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5043892941500342, var=0.4704864795999656, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F
    Total Standard Deviation in ln(k): 2.6423980093689186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F
Total Standard Deviation in ln(k): 2.6423980093689186""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F
Total Standard Deviation in ln(k): 2.6423980093689186
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F",
    kinetics = ArrheniusBM(A=(0.0352627,'m^3/(mol*s)'), n=2.34043, w0=(828500,'J/mol'), E0=(309871,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.385671106975245, var=3.341635576780213, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F
    Total Standard Deviation in ln(k): 4.633706884883315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F
Total Standard Deviation in ln(k): 4.633706884883315""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F
Total Standard Deviation in ln(k): 4.633706884883315
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C",
    kinetics = ArrheniusBM(A=(7.08572e-41,'m^3/(mol*s)'), n=13.6708, w0=(828500,'J/mol'), E0=(204408,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6862832810020016, var=0.32368497394361495, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C
    Total Standard Deviation in ln(k): 2.864890173146874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 2.864890173146874""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 2.864890173146874
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
    kinetics = ArrheniusBM(A=(4.8159e-58,'m^3/(mol*s)'), n=18.5401, w0=(828500,'J/mol'), E0=(199239,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5084944145427037, var=0.3688003123770822, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.4950783494852318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.4950783494852318""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 2.4950783494852318
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
    kinetics = ArrheniusBM(A=(4.54485e-58,'m^3/(mol*s)'), n=18.529, w0=(828500,'J/mol'), E0=(198611,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4824392507703974, var=0.6069596133618841, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.7740001634788927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.7740001634788927""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.7740001634788927
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
    kinetics = ArrheniusBM(A=(5.22285e-58,'m^3/(mol*s)'), n=18.5326, w0=(828500,'J/mol'), E0=(198311,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5292811539623584, var=0.9161100922973696, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 3.2486570648506126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 3.2486570648506126""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-5R->C_4BrCClHILiNOPSSi->C_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 3.2486570648506126
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

