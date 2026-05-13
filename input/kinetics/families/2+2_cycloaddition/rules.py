#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.11235e+09,'m^3/(mol*s)'), n=-1.20501, w0=(662.667,'kJ/mol'), E0=(238.68,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003010933537879097, var=8.886675108973241, Tref=1000.0, N=6, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 6 training reactions at node Root
    Total Standard Deviation in ln(k): 5.983786044226393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 5.983786044226393""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 5.983786044226393
""",
)

entry(
    index = 2,
    label = "Root_1COCSCdCdd->Cd",
    kinetics = ArrheniusBM(A=(52.6233,'m^3/(mol*s)'), n=1.06332, w0=(658.2,'kJ/mol'), E0=(224.83,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12982002987877939, var=5.903195576681125, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1COCSCdCdd->Cd',), comment="""BM rule fitted to 5 training reactions at node Root_1COCSCdCdd->Cd
    Total Standard Deviation in ln(k): 5.196984097535264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 5.196984097535264""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 5.196984097535264
""",
)

entry(
    index = 3,
    label = "Root_N-1COCSCdCdd->Cd",
    kinetics = Arrhenius(A=(2.319e-07,'m^3/(mol*s)'), n=3.416, Ea=(322.616,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCSCdCdd->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCSCdCdd->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCSCdCdd->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_1COCSCdCdd->Cd_3COCSCdCdd->CO",
    kinetics = ArrheniusBM(A=(55.4264,'m^3/(mol*s)'), n=1.17, w0=(700.5,'kJ/mol'), E0=(225.619,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10290757387673852, var=13.244109988914712, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCSCdCdd->Cd_3COCSCdCdd->CO',), comment="""BM rule fitted to 3 training reactions at node Root_1COCSCdCdd->Cd_3COCSCdCdd->CO
    Total Standard Deviation in ln(k): 7.554285452853174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1COCSCdCdd->Cd_3COCSCdCdd->CO
Total Standard Deviation in ln(k): 7.554285452853174""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1COCSCdCdd->Cd_3COCSCdCdd->CO
Total Standard Deviation in ln(k): 7.554285452853174
""",
)

entry(
    index = 5,
    label = "Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO",
    kinetics = ArrheniusBM(A=(66629.8,'m^3/(mol*s)'), n=0.0047097, w0=(594.75,'kJ/mol'), E0=(231.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08837421302191284, var=0.332734874802399, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO',), comment="""BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO
    Total Standard Deviation in ln(k): 1.378440616495377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO
Total Standard Deviation in ln(k): 1.378440616495377""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCSCdCdd->Cd_N-3COCSCdCdd->CO
Total Standard Deviation in ln(k): 1.378440616495377
""",
)

