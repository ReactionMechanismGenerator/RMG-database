#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.51258e+21,'m^3/(mol*s)'), n=-4.73433, w0=(662667,'J/mol'), E0=(260353,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24606408429282084, var=11.431364239445765, Tref=1000.0, N=6, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 7.3963210190210456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.3963210190210456""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.3963210190210456
""",
)

entry(
    index = 2,
    label = "Root_1COCSCdCdd->Cd",
    kinetics = ArrheniusBM(A=(0.0195885,'m^3/(mol*s)'), n=2.14699, w0=(658200,'J/mol'), E0=(219998,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04346154203493252, var=5.777042437712499, Tref=1000.0, N=5, correlation='Root_1COCSCdCdd->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd
    Total Standard Deviation in ln(k): 4.927676610542817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 4.927676610542817""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 4.927676610542817
""",
)

entry(
    index = 3,
    label = "Root_N-1COCSCdCdd->Cd",
    kinetics = ArrheniusBM(A=(2.73271e-32,'m^3/(mol*s)'), n=10.9581, w0=(685000,'J/mol'), E0=(68500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-1COCSCdCdd->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCSCdCdd->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_1COCSCdCdd->Cd_3COCSCdCdd->CO",
    kinetics = ArrheniusBM(A=(0.113741,'m^3/(mol*s)'), n=2.0246, w0=(700500,'J/mol'), E0=(222212,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013070562052782878, var=13.242392200388787, Tref=1000.0, N=3, correlation='Root_1COCSCdCdd->Cd_3COCSCdCdd->CO',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_3COCSCdCdd->CO
    Total Standard Deviation in ln(k): 7.328091167028413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_3COCSCdCdd->CO
Total Standard Deviation in ln(k): 7.328091167028413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_3COCSCdCdd->CO
Total Standard Deviation in ln(k): 7.328091167028413
""",
)

entry(
    index = 5,
    label = "Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO",
    kinetics = ArrheniusBM(A=(66.1612,'m^3/(mol*s)'), n=0.949831, w0=(594750,'J/mol'), E0=(226339,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010964617442947782, var=1.2507574696173305, Tref=1000.0, N=2, correlation='Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO
    Total Standard Deviation in ln(k): 2.2695902476071947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO
Total Standard Deviation in ln(k): 2.2695902476071947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO
Total Standard Deviation in ln(k): 2.2695902476071947
""",
)

entry(
    index = 6,
    label = "Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd",
    kinetics = ArrheniusBM(A=(19.0618,'m^3/(mol*s)'), n=1.0884, w0=(602000,'J/mol'), E0=(227200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_3CSCd->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd",
    kinetics = ArrheniusBM(A=(965.19,'m^3/(mol*s)'), n=0.627082, w0=(587500,'J/mol'), E0=(226772,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO_N-3CSCd->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

