#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.33234e+08,'m^3/(mol*s)'), n=-0.309527, w0=(538.545,'kJ/mol'), E0=(50.9344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05944516128848271, var=1.683315296172411, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 2.750355941453302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 2.750355941453302""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 2.750355941453302
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = ArrheniusBM(A=(1.11948e+13,'m^3/(mol*s)'), n=-2.00436, w0=(540.5,'kJ/mol'), E0=(81.6543,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2255519346134576, var=0.9675969199156964, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 2 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 10.076389665025324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 10.076389665025324""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 10.076389665025324
""",
)

entry(
    index = 3,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(2.32909e+08,'m^3/(mol*s)'), n=-0.309338, w0=(538.419,'kJ/mol'), E0=(50.9208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05933169303352933, var=1.683744031704995, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 31 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 2.7504020573530537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.7504020573530537""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.7504020573530537
""",
)

entry(
    index = 4,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R",
    kinetics = ArrheniusBM(A=(1.75075e+08,'m^3/(mol*s)'), n=-0.314009, w0=(552.375,'kJ/mol'), E0=(46.165,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01104235126075822, var=1.7265614662309297, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R',), comment="""BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R
    Total Standard Deviation in ln(k): 2.661940149092394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R
Total Standard Deviation in ln(k): 2.661940149092394""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R
Total Standard Deviation in ln(k): 2.661940149092394
""",
)

entry(
    index = 5,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->O",
    kinetics = ArrheniusBM(A=(4.03707e+07,'m^3/(mol*s)'), n=-0.0402976, w0=(481.167,'kJ/mol'), E0=(68.8474,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2977863699243333, var=6.534013276499907, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->O
    Total Standard Deviation in ln(k): 10.897779469030574"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->O
Total Standard Deviation in ln(k): 10.897779469030574""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->O
Total Standard Deviation in ln(k): 10.897779469030574
""",
)

entry(
    index = 6,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->O",
    kinetics = ArrheniusBM(A=(6.00747e+07,'m^3/(mol*s)'), n=9.79443e-05, w0=(525,'kJ/mol'), E0=(36.2882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00018587693605234503, var=1.3235711967532091, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O
    Total Standard Deviation in ln(k): 2.3068458582336557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O
Total Standard Deviation in ln(k): 2.3068458582336557""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O
Total Standard Deviation in ln(k): 2.3068458582336557
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = Arrhenius(A=(1.5e+06,'m^3/(mol*s)'), n=0, Ea=(8.368,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.75195e+08,'m^3/(mol*s)'), n=-0.314086, w0=(557.053,'kJ/mol'), E0=(46.1825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010985529762791381, var=1.7262367726915029, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 2.66154967920985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.66154967920985""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.66154967920985
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->O_4O-u1",
    kinetics = Arrhenius(A=(3.3e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->O_4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->O_4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_4BrCClHILiNOPSSi->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(3.12377e+07,'m^3/(mol*s)'), n=1.18051e-07, w0=(503.75,'kJ/mol'), E0=(40.6723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0977860635779144, var=5.53950819353696, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHILiNOPSSi->O_N-4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->O_N-4O-u1
    Total Standard Deviation in ln(k): 7.4766329601785975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 7.4766329601785975""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHILiNOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 7.4766329601785975
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->O_2Br1sCl1sF1sHI1s->F1s",
    kinetics = Arrhenius(A=(2.5e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->O_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(6.00762e+07,'m^3/(mol*s)'), n=0.000107007, w0=(505.5,'kJ/mol'), E0=(32.972,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00027521597222476786, var=1.3240886714439162, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 2.3075211448896935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.3075211448896935""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.3075211448896935
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.25591e+17,'m^3/(mol*s)'), n=-3.53614, w0=(555.5,'kJ/mol'), E0=(94.4218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1192202985376147, var=3.3269872051821383, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.46875424175625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.46875424175625""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.46875424175625
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C",
    kinetics = ArrheniusBM(A=(7.99675e+07,'m^3/(mol*s)'), n=-0.00102515, w0=(553.5,'kJ/mol'), E0=(92.3299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003241494254429288, var=1.0710878982446579, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
    Total Standard Deviation in ln(k): 2.0829124796986833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
Total Standard Deviation in ln(k): 2.0829124796986833""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
Total Standard Deviation in ln(k): 2.0829124796986833
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.99573e+06,'m^3/(mol*s)'), n=0.144819, w0=(558.625,'kJ/mol'), E0=(39.1865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03215648378337366, var=0.7535017299076495, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
    Total Standard Deviation in ln(k): 1.8209949928477367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
Total Standard Deviation in ln(k): 1.8209949928477367""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
Total Standard Deviation in ln(k): 1.8209949928477367
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C",
    kinetics = Arrhenius(A=(4e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C",
    kinetics = ArrheniusBM(A=(9.01884e+07,'m^3/(mol*s)'), n=0.000218311, w0=(498.5,'kJ/mol'), E0=(52.0244,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.45271299666588194, var=0.9153378465585457, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
    Total Standard Deviation in ln(k): 3.0554658500323826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
Total Standard Deviation in ln(k): 3.0554658500323826""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
Total Standard Deviation in ln(k): 3.0554658500323826
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C",
    kinetics = Arrhenius(A=(6e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.1529e+17,'m^3/(mol*s)'), n=-3.2809, w0=(559.5,'kJ/mol'), E0=(90.1019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9381243410879869, var=5.55907787587735, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 7.083799921384638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.083799921384638""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.083799921384638
""",
)

entry(
    index = 20,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHILiNOPSSi-R",
    kinetics = Arrhenius(A=(1.2e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHILiNOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHILiNOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHILiNOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHILiNOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHILiNOPSSi",
    kinetics = ArrheniusBM(A=(6.40294e+07,'m^3/(mol*s)'), n=0.00363571, w0=(559.5,'kJ/mol'), E0=(92.3299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.198027582217755e-17, var=1.1009420470081581, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHILiNOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHILiNOPSSi
    Total Standard Deviation in ln(k): 2.103484027846209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHILiNOPSSi
Total Standard Deviation in ln(k): 2.103484027846209""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHILiNOPSSi
Total Standard Deviation in ln(k): 2.103484027846209
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHILiNOPSSi",
    kinetics = Arrhenius(A=(9.033e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHILiNOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHILiNOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHILiNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHILiNOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F",
    kinetics = ArrheniusBM(A=(1.09913e+08,'m^3/(mol*s)'), n=-0.0931895, w0=(559.833,'kJ/mol'), E0=(95.1922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1257238386507349, var=0.874781956428024, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
    Total Standard Deviation in ln(k): 2.1909133297395775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
Total Standard Deviation in ln(k): 2.1909133297395775""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
Total Standard Deviation in ln(k): 2.1909133297395775
""",
)

entry(
    index = 24,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F",
    kinetics = ArrheniusBM(A=(4.98363e+06,'m^3/(mol*s)'), n=0.145089, w0=(557.417,'kJ/mol'), E0=(39.1687,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.032292240689189004, var=0.7528250182043972, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
    Total Standard Deviation in ln(k): 1.820554487820163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
Total Standard Deviation in ln(k): 1.820554487820163""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
Total Standard Deviation in ln(k): 1.820554487820163
""",
)

entry(
    index = 25,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H",
    kinetics = ArrheniusBM(A=(9.03018e+07,'m^3/(mol*s)'), n=5.22623e-08, w0=(536,'kJ/mol'), E0=(86.7727,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1019910880521685, var=0.020821354172517827, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
    Total Standard Deviation in ln(k): 0.545534396838917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
Total Standard Deviation in ln(k): 0.545534396838917""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
Total Standard Deviation in ln(k): 0.545534396838917
""",
)

entry(
    index = 26,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H",
    kinetics = ArrheniusBM(A=(1.96331e+08,'m^3/(mol*s)'), n=-0.0207331, w0=(479.75,'kJ/mol'), E0=(66.1054,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013260065087765383, var=2.1999011561850264, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
    Total Standard Deviation in ln(k): 3.0067525970405664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
Total Standard Deviation in ln(k): 3.0067525970405664""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
Total Standard Deviation in ln(k): 3.0067525970405664
""",
)

entry(
    index = 27,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s",
    kinetics = Arrhenius(A=(2.23e+07,'m^3/(mol*s)'), n=0, Ea=(1.33051,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s",
    kinetics = ArrheniusBM(A=(3.53766e+11,'m^3/(mol*s)'), n=-1.12914, w0=(547.5,'kJ/mol'), E0=(106.152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17827425252739032, var=0.6849136010186807, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
    Total Standard Deviation in ln(k): 2.107034125683052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
Total Standard Deviation in ln(k): 2.107034125683052""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
Total Standard Deviation in ln(k): 2.107034125683052
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br",
    kinetics = Arrhenius(A=(5e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br",
    kinetics = ArrheniusBM(A=(4.98498e+06,'m^3/(mol*s)'), n=0.145063, w0=(554.6,'kJ/mol'), E0=(39.1614,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03225419705613187, var=0.7529668375696095, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
    Total Standard Deviation in ln(k): 1.820622731415809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
Total Standard Deviation in ln(k): 1.820622731415809""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
Total Standard Deviation in ln(k): 1.820622731415809
""",
)

entry(
    index = 31,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->H",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=-5.60202e-09, w0=(539.5,'kJ/mol'), E0=(73.6051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09888896739422573, var=0.01955805574459248, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->H
    Total Standard Deviation in ln(k): 0.528827181048888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->H
Total Standard Deviation in ln(k): 0.528827181048888""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->H
Total Standard Deviation in ln(k): 0.528827181048888
""",
)

entry(
    index = 32,
    label = "Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->H",
    kinetics = ArrheniusBM(A=(1.62348e+08,'m^3/(mol*s)'), n=0.000104, w0=(420,'kJ/mol'), E0=(64.7522,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.553540862245973, var=7.626664266065631, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->H
    Total Standard Deviation in ln(k): 6.9271659511959855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->H
Total Standard Deviation in ln(k): 6.9271659511959855""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHILiNOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->H
Total Standard Deviation in ln(k): 6.9271659511959855
""",
)

entry(
    index = 33,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R",
    kinetics = ArrheniusBM(A=(4.9532e+07,'m^3/(mol*s)'), n=8.44264e-06, w0=(547.5,'kJ/mol'), E0=(89.9114,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06645294458865263, var=2.6057891664438952, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R
    Total Standard Deviation in ln(k): 3.403102167383463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R
Total Standard Deviation in ln(k): 3.403102167383463""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R
Total Standard Deviation in ln(k): 3.403102167383463
""",
)

entry(
    index = 34,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHILiNOPSSi->O",
    kinetics = ArrheniusBM(A=(4.90666e+07,'m^3/(mol*s)'), n=0.00528409, w0=(571.5,'kJ/mol'), E0=(52.5157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.145107000736439, var=3.420797620145901, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHILiNOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHILiNOPSSi->O
    Total Standard Deviation in ln(k): 9.097553476754356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHILiNOPSSi->O
Total Standard Deviation in ln(k): 9.097553476754356""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHILiNOPSSi->O
Total Standard Deviation in ln(k): 9.097553476754356
""",
)

entry(
    index = 35,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O",
    kinetics = ArrheniusBM(A=(5.24514e+07,'m^3/(mol*s)'), n=-0.196046, w0=(543.333,'kJ/mol'), E0=(48.3492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14344748092442164, var=0.4230917681123524, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O
    Total Standard Deviation in ln(k): 1.6644108552463146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O
Total Standard Deviation in ln(k): 1.6644108552463146""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O
Total Standard Deviation in ln(k): 1.6644108552463146
""",
)

entry(
    index = 36,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_6R!H->Cl",
    kinetics = Arrhenius(A=(1.5e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=3.86217e-09, w0=(547.5,'kJ/mol'), E0=(84.3028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_N-6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHILiNOPSSi-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 38,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_4BrCClHN->C",
    kinetics = ArrheniusBM(A=(1.34164e+07,'m^3/(mol*s)'), n=4.17383e-08, w0=(547.5,'kJ/mol'), E0=(55.5771,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.5990137911088773e-17, var=0.6909863268735121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_4BrCClHN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_4BrCClHN->C
    Total Standard Deviation in ln(k): 1.666447807467594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_4BrCClHN->C
Total Standard Deviation in ln(k): 1.666447807467594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_4BrCClHN->C
Total Standard Deviation in ln(k): 1.666447807467594
""",
)

entry(
    index = 39,
    label = "Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_N-4BrCClHN->C",
    kinetics = Arrhenius(A=(7.1e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_N-4BrCClHN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_N-4BrCClHN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_N-4BrCClHN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHILiNOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHILiNOPSSi->O_N-4BrCClHN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

