#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation-Y/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.71536e+09,'m^3/(mol*s)'), n=-0.60604, w0=(561986,'J/mol'), E0=(66460.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011989902655148222, var=0.5275280256637414, Tref=1000.0, N=42, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 42 training reactions at node Root
    Total Standard Deviation in ln(k): 1.4861870149624394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 1.4861870149624394""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 1.4861870149624394
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = ArrheniusBM(A=(4.44453e+26,'m^3/(mol*s)'), n=-6.25402, w0=(494250,'J/mol'), E0=(83616.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25616760566121266, var=80.80783887470666, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 2 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 18.664838402417764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 18.664838402417764""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 18.664838402417764
""",
)

entry(
    index = 3,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(2.66406e+09,'m^3/(mol*s)'), n=-0.603306, w0=(565373,'J/mol'), E0=(66428.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014863932080599407, var=0.5183064699482094, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 40 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 1.4806256024669349"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 1.4806256024669349""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 1.4806256024669349
""",
)

entry(
    index = 4,
    label = "Root_4R->F_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(540500,'J/mol'), E0=(58191.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->F_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->F_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->F_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->F_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H",
    kinetics = ArrheniusBM(A=(5.44775e+07,'m^3/(mol*s)'), n=-0.0316363, w0=(587271,'J/mol'), E0=(58727.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01707252228861849, var=0.4922028501234509, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H',), comment="""BM rule fitted to 35 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H
    Total Standard Deviation in ln(k): 1.4493611807740134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H
Total Standard Deviation in ln(k): 1.4493611807740134""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H
Total Standard Deviation in ln(k): 1.4493611807740134
""",
)

entry(
    index = 6,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H",
    kinetics = ArrheniusBM(A=(5.29656e+06,'m^3/(mol*s)'), n=-3.1555e-08, w0=(412084,'J/mol'), E0=(26156.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014574479897016551, var=0.41251385941446495, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H
    Total Standard Deviation in ln(k): 1.3242053425971314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H
Total Standard Deviation in ln(k): 1.3242053425971314""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H
Total Standard Deviation in ln(k): 1.3242053425971314
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(5.32386e+07,'m^3/(mol*s)'), n=-0.0143471, w0=(502214,'J/mol'), E0=(50221.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008673259761464441, var=0.3987527953273712, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 1.2877196841523404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.2877196841523404""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.2877196841523404
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(7.29643e+07,'m^3/(mol*s)'), n=-0.251266, w0=(643976,'J/mol'), E0=(31837.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009109015325134737, var=0.4965629106420655, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 21 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 1.43556805227485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.43556805227485""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.43556805227485
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(8.16667e+06,'m^3/(mol*s)'), n=2.43385e-08, w0=(406210,'J/mol'), E0=(31825.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12083959715619644, var=0.029204416481743677, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 0.6462122641896045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.6462122641896045""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.6462122641896045
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(3.9685e+06,'m^3/(mol*s)'), n=-1.37125e-08, w0=(416000,'J/mol'), E0=(22080.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09936838897626549, var=0.4932773509929155, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.6576690667124168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.6576690667124168""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.6576690667124168
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4.05117e+07,'m^3/(mol*s)'), n=-0.0223185, w0=(502944,'J/mol'), E0=(50294.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013491724819706123, var=0.22974801437028444, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.9948091594261502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.9948091594261502""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.9948091594261502
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.93704e+07,'m^3/(mol*s)'), n=-7.25844e-07, w0=(501667,'J/mol'), E0=(50166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.560021666006558e-08, var=0.36033988307570763, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.2034089153659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2034089153659""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2034089153659
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(505500,'J/mol'), E0=(50550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(494000,'J/mol'), E0=(49400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.43469e+07,'m^3/(mol*s)'), n=-0.238147, w0=(633333,'J/mol'), E0=(44842.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4721424134947334, var=0.6397922503553959, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.789815210005193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.789815210005193""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.789815210005193
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.08509e+09,'m^3/(mol*s)'), n=-0.556928, w0=(671500,'J/mol'), E0=(67150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.038334311443416605, var=0.5015770793411518, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.516112980431913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.516112980431913""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.516112980431913
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(7.37471e+08,'m^3/(mol*s)'), n=-0.548118, w0=(641500,'J/mol'), E0=(64150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06539578995210048, var=0.3779534857901618, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.396780491423361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.396780491423361""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.396780491423361
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br",
    kinetics = ArrheniusBM(A=(8.16667e+06,'m^3/(mol*s)'), n=0, w0=(400920,'J/mol'), E0=(31634.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br",
    kinetics = ArrheniusBM(A=(8.16667e+06,'m^3/(mol*s)'), n=0, w0=(411500,'J/mol'), E0=(41150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.5e+06,'m^3/(mol*s)'), n=0, w0=(416000,'J/mol'), E0=(35280.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(416000,'J/mol'), E0=(30447.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.93828e+07,'m^3/(mol*s)'), n=-5.2122e-08, w0=(502625,'J/mol'), E0=(50262.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3579066393020782e-07, var=0.09662783948386781, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl
    Total Standard Deviation in ln(k): 0.6231726172168418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6231726172168418""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6231726172168418
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, w0=(505500,'J/mol'), E0=(50550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(505500,'J/mol'), E0=(50550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(505500,'J/mol'), E0=(50550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(494000,'J/mol'), E0=(49400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(6.32325e+07,'m^3/(mol*s)'), n=-0.236464, w0=(630611,'J/mol'), E0=(63061.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7498660037358731, var=1.180991488912037, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 4.062699853764565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.062699853764565""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.062699853764565
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.11082e+08,'m^3/(mol*s)'), n=-0.352588, w0=(641500,'J/mol'), E0=(39089.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06556306637218147, var=0.5832464286180573, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.6957589706714786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.6957589706714786""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.6957589706714786
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C",
    kinetics = ArrheniusBM(A=(4.45559e+09,'m^3/(mol*s)'), n=-0.69616, w0=(653000,'J/mol'), E0=(65300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04791788904805767, var=0.3109331404557689, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C
    Total Standard Deviation in ln(k): 1.2382646335822984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C
Total Standard Deviation in ln(k): 1.2382646335822984""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C
Total Standard Deviation in ln(k): 1.2382646335822984
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(745500,'J/mol'), E0=(74550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.67536e+08,'m^3/(mol*s)'), n=-0.352589, w0=(641500,'J/mol'), E0=(64150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06556305488210509, var=0.485146560097461, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.5610786515608777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.5610786515608777""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.5610786515608777
""",
)

entry(
    index = 32,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.33333e+07,'m^3/(mol*s)'), n=9.6659e-08, w0=(505500,'J/mol'), E0=(50550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.992731271234566e-08, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R
    Total Standard Deviation in ln(k): 5.0068624905391104e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R
Total Standard Deviation in ln(k): 5.0068624905391104e-08""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R
Total Standard Deviation in ln(k): 5.0068624905391104e-08
""",
)

entry(
    index = 33,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.96851e+07,'m^3/(mol*s)'), n=-4.36179e-07, w0=(501667,'J/mol'), E0=(50166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.725440420271771e-07, var=0.36033993726780916, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.2034092494346458"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2034092494346458""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2034092494346458
""",
)

entry(
    index = 34,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(505500,'J/mol'), E0=(50550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(494000,'J/mol'), E0=(49400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.67246e+07,'m^3/(mol*s)'), n=-0.218314, w0=(619417,'J/mol'), E0=(61941.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5028595390830304, var=0.41280963840374957, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.5515137520814957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.5515137520814957""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.5515137520814957
""",
)

entry(
    index = 37,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.3257e+10,'m^3/(mol*s)'), n=-1.25434, w0=(653000,'J/mol'), E0=(65300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8353434830257415, var=2.4651903288156624e-32, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.0988529724264864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0988529724264864""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0988529724264864
""",
)

entry(
    index = 38,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(641500,'J/mol'), E0=(64150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.29007e+10,'m^3/(mol*s)'), n=-1.1347, w0=(641500,'J/mol'), E0=(61785.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9762447934156254, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 2.452876365365893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 2.452876365365893""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 2.452876365365893
""",
)

entry(
    index = 40,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.12927e+09,'m^3/(mol*s)'), n=-0.570904, w0=(653000,'J/mol'), E0=(65300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04460070932531281, var=0.3792944565490591, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.3467159966844713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.3467159966844713""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.3467159966844713
""",
)

entry(
    index = 41,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(641500,'J/mol'), E0=(64150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.44775e+10,'m^3/(mol*s)'), n=-1.1347, w0=(641500,'J/mol'), E0=(64150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9762447934156255, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.418034250478541"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.418034250478541""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.418034250478541
""",
)

entry(
    index = 43,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.33333e+07,'m^3/(mol*s)'), n=1.8255e-07, w0=(505500,'J/mol'), E0=(50550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 44,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(505500,'J/mol'), E0=(50550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(505500,'J/mol'), E0=(50550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(494000,'J/mol'), E0=(49400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(4.32312e+09,'m^3/(mol*s)'), n=-0.902321, w0=(653000,'J/mol'), E0=(58137.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11306279988208066, var=0.3567450033424795, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s
    Total Standard Deviation in ln(k): 1.4814682471086988"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s
Total Standard Deviation in ln(k): 1.4814682471086988""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s
Total Standard Deviation in ln(k): 1.4814682471086988
""",
)

entry(
    index = 48,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, w0=(451500,'J/mol'), E0=(45150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.98e+14,'m^3/(mol*s)'), n=-2.31, w0=(641500,'J/mol'), E0=(64150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.12e+15,'m^3/(mol*s)'), n=-2.27, w0=(653000,'J/mol'), E0=(65300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.33333e+07,'m^3/(mol*s)'), n=0, w0=(505500,'J/mol'), E0=(50550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.50822e+09,'m^3/(mol*s)'), n=-0.740556, w0=(653000,'J/mol'), E0=(57770.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1104787444318883, var=0.9401560886858894, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.2214089234786045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.2214089234786045""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.2214089234786045
""",
)

entry(
    index = 53,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.81e+16,'m^3/(mol*s)'), n=-2.92, w0=(653000,'J/mol'), E0=(65300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, w0=(653000,'J/mol'), E0=(65300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

