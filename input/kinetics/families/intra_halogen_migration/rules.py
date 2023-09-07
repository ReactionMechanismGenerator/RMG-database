#!/usr/bin/env python
# encoding: utf-8

name = "intra_halogen_migration/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(82318.8,'s^-1'), n=2.16221, w0=(416.556,'kJ/mol'), E0=(165.549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.022281151252300645, var=66.1657303763108, Tref=1000.0, N=18, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 18 training reactions at node Root
    Total Standard Deviation in ln(k): 16.36296302820437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 16.36296302820437""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 16.36296302820437
""",
)

entry(
    index = 2,
    label = "F",
    kinetics = ArrheniusBM(A=(4.69879e+07,'s^-1'), n=1.42748, w0=(485,'kJ/mol'), E0=(198.783,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05505882546177618, var=61.63242994454046, Tref=1000.0, N=11, data_mean=0.0, correlation='F',), comment="""BM rule fitted to 11 training reactions at node F
    Total Standard Deviation in ln(k): 15.876777019841905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node F
Total Standard Deviation in ln(k): 15.876777019841905""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node F
Total Standard Deviation in ln(k): 15.876777019841905
""",
)

entry(
    index = 3,
    label = "R2F",
    kinetics = ArrheniusBM(A=(1.80066e+13,'s^-1'), n=-0.0685173, w0=(485,'kJ/mol'), E0=(172.526,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02862981863955743, var=17.29616153989066, Tref=1000.0, N=6, data_mean=0.0, correlation='R2F',), comment="""BM rule fitted to 6 training reactions at node R2F
    Total Standard Deviation in ln(k): 8.409357597252756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node R2F
Total Standard Deviation in ln(k): 8.409357597252756""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node R2F
Total Standard Deviation in ln(k): 8.409357597252756
""",
)

entry(
    index = 4,
    label = "R2F_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.38157e+14,'s^-1'), n=-0.447076, w0=(485,'kJ/mol'), E0=(188.293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08474952276158404, var=26.08378321593064, Tref=1000.0, N=4, data_mean=0.0, correlation='R2F_Ext-1R!H-R',), comment="""BM rule fitted to 4 training reactions at node R2F_Ext-1R!H-R
    Total Standard Deviation in ln(k): 10.45157867357281"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node R2F_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.45157867357281""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node R2F_Ext-1R!H-R
Total Standard Deviation in ln(k): 10.45157867357281
""",
)

entry(
    index = 5,
    label = "R2F_Ext-1R!H-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.00763e+12,'s^-1'), n=0.18834, w0=(485,'kJ/mol'), E0=(182.239,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "R2F_Ext-1R!H-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(7.9267e+15,'s^-1'), n=-0.733083, w0=(485,'kJ/mol'), E0=(190.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0717849990446407, var=47.27832310158784, Tref=1000.0, N=3, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C
    Total Standard Deviation in ln(k): 13.964769221395043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 13.964769221395043""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 13.964769221395043
""",
)

entry(
    index = 7,
    label = "R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.02536e+15,'s^-1'), n=-0.647135, w0=(485,'kJ/mol'), E0=(204.307,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05148276168955191, var=80.78210905804004, Tref=1000.0, N=2, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 18.14768560421227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 18.14768560421227""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 18.14768560421227
""",
)

entry(
    index = 8,
    label = "R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.35648e+12,'s^-1'), n=0.369741, w0=(485,'kJ/mol'), E0=(182.731,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.2804e+11,'s^-1'), n=0.253035, w0=(485,'kJ/mol'), E0=(209.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-1R!H-R_N-4R!H->C_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "R2F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.36622e+11,'s^-1'), n=0.48217, w0=(485,'kJ/mol'), E0=(153.633,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node R2F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "R3F",
    kinetics = ArrheniusBM(A=(0.00930803,'s^-1'), n=4.16824, w0=(485,'kJ/mol'), E0=(227.637,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3F',), comment="""BM rule fitted to 1 training reactions at node R3F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R3F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R3F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "R4F",
    kinetics = ArrheniusBM(A=(2.56499e-06,'s^-1'), n=5.16802, w0=(485,'kJ/mol'), E0=(228.119,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010618623676007603, var=1.2440368903510177, Tref=1000.0, N=3, data_mean=0.0, correlation='R4F',), comment="""BM rule fitted to 3 training reactions at node R4F
    Total Standard Deviation in ln(k): 2.2626893278675366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node R4F
Total Standard Deviation in ln(k): 2.2626893278675366""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node R4F
Total Standard Deviation in ln(k): 2.2626893278675366
""",
)

entry(
    index = 13,
    label = "R4F_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(0.00363316,'s^-1'), n=4.43046, w0=(485,'kJ/mol'), E0=(242.356,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4F_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node R4F_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4F_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4F_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "R4F_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.000550858,'s^-1'), n=4.50663, w0=(485,'kJ/mol'), E0=(242.042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4F_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node R4F_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4F_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4F_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "R5nF",
    kinetics = ArrheniusBM(A=(1.64853e+07,'s^-1'), n=1.15307, w0=(485,'kJ/mol'), E0=(198.221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nF',), comment="""BM rule fitted to 1 training reactions at node R5nF
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R5nF
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R5nF
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Cl",
    kinetics = ArrheniusBM(A=(893.664,'s^-1'), n=2.71685, w0=(327,'kJ/mol'), E0=(122.89,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3496301716658287e-15, var=152.99410132498224, Tref=1000.0, N=4, data_mean=0.0, correlation='Cl',), comment="""BM rule fitted to 4 training reactions at node Cl
    Total Standard Deviation in ln(k): 24.79672541318142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Cl
Total Standard Deviation in ln(k): 24.79672541318142""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Cl
Total Standard Deviation in ln(k): 24.79672541318142
""",
)

entry(
    index = 17,
    label = "R2Cl",
    kinetics = ArrheniusBM(A=(1.03108e+13,'s^-1'), n=-0.0707693, w0=(327,'kJ/mol'), E0=(47.2642,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2Cl',), comment="""BM rule fitted to 1 training reactions at node R2Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R2Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R2Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "R3Cl",
    kinetics = ArrheniusBM(A=(6.00221e+06,'s^-1'), n=1.90111, w0=(327,'kJ/mol'), E0=(169.648,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3Cl',), comment="""BM rule fitted to 1 training reactions at node R3Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R3Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R3Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "R4Cl",
    kinetics = ArrheniusBM(A=(2.50247e+07,'s^-1'), n=1.58353, w0=(327,'kJ/mol'), E0=(156.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4Cl',), comment="""BM rule fitted to 1 training reactions at node R4Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "R5nCl",
    kinetics = ArrheniusBM(A=(4.11837e-16,'s^-1'), n=7.45351, w0=(327,'kJ/mol'), E0=(118.459,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nCl',), comment="""BM rule fitted to 1 training reactions at node R5nCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R5nCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R5nCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Br",
    kinetics = ArrheniusBM(A=(4.41069e+09,'s^-1'), n=0.616349, w0=(285,'kJ/mol'), E0=(131.367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.198849422960356e-15, var=19.080469612873383, Tref=1000.0, N=3, data_mean=0.0, correlation='Br',), comment="""BM rule fitted to 3 training reactions at node Br
    Total Standard Deviation in ln(k): 8.756922761748767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Br
Total Standard Deviation in ln(k): 8.756922761748767""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Br
Total Standard Deviation in ln(k): 8.756922761748767
""",
)

entry(
    index = 22,
    label = "R3Br",
    kinetics = ArrheniusBM(A=(5.2885e+08,'s^-1'), n=1.30127, w0=(285,'kJ/mol'), E0=(134.618,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3Br',), comment="""BM rule fitted to 1 training reactions at node R3Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R3Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R3Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "R4Br",
    kinetics = ArrheniusBM(A=(9.62119e+10,'s^-1'), n=0.157944, w0=(285,'kJ/mol'), E0=(121.704,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R4Br',), comment="""BM rule fitted to 1 training reactions at node R4Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R4Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R4Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "R5nBr",
    kinetics = ArrheniusBM(A=(1.68639e+09,'s^-1'), n=0.389834, w0=(285,'kJ/mol'), E0=(137.78,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nBr',), comment="""BM rule fitted to 1 training reactions at node R5nBr
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node R5nBr
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node R5nBr
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

