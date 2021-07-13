#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(75.1467,'m^3/(mol*s)'), n=1.14017, w0=(776280,'J/mol'), E0=(210804,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.045878343548360526, var=4.041232899065857, Tref=1000.0, N=41, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 41 training reactions at node Root
    Total Standard Deviation in ln(k): 4.145354651727632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 41 training reactions at node Root
Total Standard Deviation in ln(k): 4.145354651727632""",
    longDesc = 
"""
BM rule fitted to 41 training reactions at node Root
Total Standard Deviation in ln(k): 4.145354651727632
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.03596e+06,'m^3/(mol*s)'), n=-0.220146, w0=(863175,'J/mol'), E0=(239884,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05817143812674828, var=9.691274573172977, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 6.387062477646476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.387062477646476""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.387062477646476
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(68.6596,'m^3/(mol*s)'), n=1.15244, w0=(693524,'J/mol'), E0=(210600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04579409426650649, var=3.9591418492090287, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 21 training reactions at node Root_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 4.104000690437351"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.104000690437351""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.104000690437351
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(97107.5,'m^3/(mol*s)'), n=0.0690772, w0=(865062,'J/mol'), E0=(232297,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06591412865293547, var=9.263437600966732, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 16 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 6.267204203675559"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.267204203675559""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.267204203675559
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.00668e+08,'m^3/(mol*s)'), n=-0.797789, w0=(854667,'J/mol'), E0=(273989,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0674688468933297, var=2.9747026941164787, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 3.6271517468525016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.6271517468525016""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.6271517468525016
""",
)

entry(
    index = 6,
    label = "Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, w0=(575000,'J/mol'), E0=(140198,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(9.30761,'m^3/(mol*s)'), n=1.42034, w0=(699450,'J/mol'), E0=(211483,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06773005034058709, var=2.9432513028000793, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 20 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 3.6094807746605344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 3.6094807746605344""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 3.6094807746605344
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(746.282,'m^3/(mol*s)'), n=0.640431, w0=(871444,'J/mol'), E0=(216383,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0628458418453768, var=8.04913038340613, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 9 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 5.845535884075809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 5.845535884075809""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 5.845535884075809
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0758643,'m^3/(mol*s)'), n=2.01891, w0=(858500,'J/mol'), E0=(229228,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011793282512864578, var=2.024203988529797, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.8818586311989254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.8818586311989254""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.8818586311989254
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(2306.92,'m^3/(mol*s)'), n=0.487436, w0=(858500,'J/mol'), E0=(230239,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0642223628921602, var=23.30206195671698, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 9.838661855854145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 9.838661855854145""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 9.838661855854145
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(2.58922e+31,'m^3/(mol*s)'), n=-7.52934, w0=(847000,'J/mol'), E0=(355955,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(0.05668,'m^3/(mol*s)'), n=1.82997, w0=(858500,'J/mol'), E0=(243611,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001375287828578135, var=5.986718801343786, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 4.908595631730828"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 4.908595631730828""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 4.908595631730828
""",
)

entry(
    index = 13,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(3.6316e+39,'m^3/(mol*s)'), n=-9.93401, w0=(847000,'J/mol'), E0=(361528,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(25.7253,'m^3/(mol*s)'), n=1.21132, w0=(703286,'J/mol'), E0=(206078,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03045015788316864, var=1.8157940125483882, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 14 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 2.7779165415252853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 2.7779165415252853""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 2.7779165415252853
""",
)

entry(
    index = 15,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(13614.5,'m^3/(mol*s)'), n=0.655298, w0=(690500,'J/mol'), E0=(231985,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07923780514491993, var=8.025326839793111, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 5.87830553082296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 5.87830553082296""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 5.87830553082296
""",
)

entry(
    index = 16,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(9.86605e+06,'m^3/(mol*s)'), n=-0.591411, w0=(858500,'J/mol'), E0=(227557,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1322459354187164, var=7.329193340812668, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 8 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 5.759591843561456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 5.759591843561456""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 5.759591843561456
""",
)

entry(
    index = 17,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(0.143461,'m^3/(mol*s)'), n=1.81734, w0=(975000,'J/mol'), E0=(187093,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(11.9206,'m^3/(mol*s)'), n=1.10384, w0=(858500,'J/mol'), E0=(227617,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(28.9428,'m^3/(mol*s)'), n=1.05131, w0=(858500,'J/mol'), E0=(243570,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(307.977,'m^3/(mol*s)'), n=0.887668, w0=(711000,'J/mol'), E0=(207432,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.018710765986783482, var=1.9090086128911585, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 2.81689184001201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 2.81689184001201""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 2.81689184001201
""",
)

entry(
    index = 21,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0672018,'m^3/(mol*s)'), n=2.03608, w0=(657000,'J/mol'), E0=(211258,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.846002355125819, var=49.138765843648514, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 26.22888743315396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 26.22888743315396""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 26.22888743315396
""",
)

entry(
    index = 22,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(4402.23,'m^3/(mol*s)'), n=0.832427, w0=(699500,'J/mol'), E0=(224340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007734243753195459, var=0.9741359578645888, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 1.9980727377529526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.9980727377529526""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 1.9980727377529526
""",
)

entry(
    index = 23,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(645500,'J/mol'), E0=(273615,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(2.10475e+06,'m^3/(mol*s)'), n=-0.449201, w0=(858500,'J/mol'), E0=(221555,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11932877489247144, var=10.28065402539315, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
    Total Standard Deviation in ln(k): 6.727695136852385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 6.727695136852385""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R
Total Standard Deviation in ln(k): 6.727695136852385
""",
)

entry(
    index = 25,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(6.85233,'m^3/(mol*s)'), n=1.35489, w0=(711000,'J/mol'), E0=(204878,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02966106149535314, var=2.836461601920132, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 3.4508596037375416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 3.4508596037375416""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 3.4508596037375416
""",
)

entry(
    index = 26,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.84999e+06,'m^3/(mol*s)'), n=-0.353558, w0=(711000,'J/mol'), E0=(213624,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0011176031788138253, var=0.766425788910674, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 1.757868355229437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.757868355229437""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.757868355229437
""",
)

entry(
    index = 27,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(1.28077,'m^3/(mol*s)'), n=1.61803, w0=(657000,'J/mol'), E0=(211922,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.237624,'m^3/(mol*s)'), n=2.2618, w0=(699500,'J/mol'), E0=(218542,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005716926918813203, var=0.8821332733001921, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 1.8972504194064923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.8972504194064923""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.8972504194064923
""",
)

entry(
    index = 29,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Ct-R",
    kinetics = ArrheniusBM(A=(2.10658,'m^3/(mol*s)'), n=1.73542, w0=(699500,'J/mol'), E0=(212290,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Ct-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Ct-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(0.0810442,'m^3/(mol*s)'), n=1.99079, w0=(858500,'J/mol'), E0=(196672,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2434497875801829e-14, var=4.978412222288914e-60, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R_Ext-3Cd-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R_Ext-3Cd-R
    Total Standard Deviation in ln(k): 3.1242456974376454e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R_Ext-3Cd-R
Total Standard Deviation in ln(k): 3.1242456974376454e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1s->F1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_3COCdCddCtO2d->Cd_Ext-3Cd-R_Ext-3Cd-R
Total Standard Deviation in ln(k): 3.1242456974376454e-14
""",
)

entry(
    index = 31,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(863.231,'m^3/(mol*s)'), n=0.722812, w0=(711000,'J/mol'), E0=(207515,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006812385391110879, var=3.4113384386473915, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.719823940287308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.719823940287308""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.719823940287308
""",
)

entry(
    index = 32,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.71307,'m^3/(mol*s)'), n=1.56407, w0=(711000,'J/mol'), E0=(211801,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, w0=(711000,'J/mol'), E0=(215085,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.97967e+06,'m^3/(mol*s)'), n=-0.518739, w0=(711000,'J/mol'), E0=(212126,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, w0=(711000,'J/mol'), E0=(212590,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R",
    kinetics = ArrheniusBM(A=(40.7026,'m^3/(mol*s)'), n=1.65435, w0=(699500,'J/mol'), E0=(223829,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-3Ct-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(631.246,'m^3/(mol*s)'), n=0.744315, w0=(711000,'J/mol'), E0=(204988,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007791397538652573, var=13.169458742624444, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
    Total Standard Deviation in ln(k): 7.294709630031939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.294709630031939""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.294709630031939
""",
)

entry(
    index = 38,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, w0=(711000,'J/mol'), E0=(220112,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(179.755,'m^3/(mol*s)'), n=0.928737, w0=(711000,'J/mol'), E0=(199420,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0015583992925483614, var=35.83408174955999, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.004575517732093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.004575517732093""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.004575517732093
""",
)

entry(
    index = 40,
    label = "Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, w0=(711000,'J/mol'), E0=(210237,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

