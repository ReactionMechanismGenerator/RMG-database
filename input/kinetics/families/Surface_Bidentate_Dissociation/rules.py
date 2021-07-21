#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = SurfaceArrheniusBM(A=(2.07437e-80,'s^-1'), n=27.3342, w0=(324318,'J/mol'), E0=(28294.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5080993266790987, var=129.51285366221362, Tref=1000.0, N=82, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 82 training reactions at node Root
    Total Standard Deviation in ln(k): 26.60382406803188"""),
    rank = 11,
    shortDesc = """BM rule fitted to 82 training reactions at node Root
Total Standard Deviation in ln(k): 26.60382406803188""",
    longDesc = 
"""
BM rule fitted to 82 training reactions at node Root
Total Standard Deviation in ln(k): 26.60382406803188
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = SurfaceArrheniusBM(A=(7.18564e-73,'s^-1'), n=25.1106, w0=(332214,'J/mol'), E0=(20579.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3747139571607914, var=123.74260957549355, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 51 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 25.75465910816819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 25.75465910816819""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 25.75465910816819
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = SurfaceArrheniusBM(A=(1.29961e-97,'s^-1'), n=32.4504, w0=(311326,'J/mol'), E0=(20832.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8287949710907843, var=131.52999042498047, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 31 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 27.58657221877186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 27.58657221877186""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 27.58657221877186
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_Ext-2R!H-R",
    kinetics = SurfaceArrheniusBM(A=(5.55893e-44,'s^-1'), n=16.5591, w0=(375807,'J/mol'), E0=(37580.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9143142678145597, var=178.60913811183366, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 29.08949980947839"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 29.08949980947839""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 29.08949980947839
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_Sp-4Xo-2R!H",
    kinetics = SurfaceArrheniusBM(A=(1.32257e+22,'s^-1'), n=-2.71859, w0=(462559,'J/mol'), E0=(153917,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11133592438187004, var=26.127255828712883, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_Sp-4Xo-2R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_Sp-4Xo-2R!H
    Total Standard Deviation in ln(k): 10.526907255216901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_Sp-4Xo-2R!H
Total Standard Deviation in ln(k): 10.526907255216901""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_Sp-4Xo-2R!H
Total Standard Deviation in ln(k): 10.526907255216901
""",
)

entry(
    index = 6,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H",
    kinetics = SurfaceArrheniusBM(A=(9.92408e-85,'s^-1'), n=28.6035, w0=(301321,'J/mol'), E0=(10582.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.658780425308337, var=113.22678615795161, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H',), comment="""BM rule fitted to 38 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H
    Total Standard Deviation in ln(k): 25.49979023992207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H
Total Standard Deviation in ln(k): 25.49979023992207""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H
Total Standard Deviation in ln(k): 25.49979023992207
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_Sp-4Xo#2R!H",
    kinetics = SurfaceArrheniusBM(A=(0.0153832,'s^-1'), n=4.29114, w0=(229275,'J/mol'), E0=(315571,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07907896677732504, var=467.21732358060075, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H->C_Sp-4Xo#2R!H',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H->C_Sp-4Xo#2R!H
    Total Standard Deviation in ln(k): 43.53146150197257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H->C_Sp-4Xo#2R!H
Total Standard Deviation in ln(k): 43.53146150197257""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H->C_Sp-4Xo#2R!H
Total Standard Deviation in ln(k): 43.53146150197257
""",
)

entry(
    index = 8,
    label = "Root_N-1R!H->C_N-Sp-4Xo#2R!H",
    kinetics = SurfaceArrheniusBM(A=(1.0119e-91,'s^-1'), n=30.6708, w0=(339865,'J/mol'), E0=(-9243.46,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7438888235711683, var=44.34844854732982, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R!H->C_N-Sp-4Xo#2R!H',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H
    Total Standard Deviation in ln(k): 17.732089448099316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H
Total Standard Deviation in ln(k): 17.732089448099316""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H
Total Standard Deviation in ln(k): 17.732089448099316
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C",
    kinetics = SurfaceArrheniusBM(A=(2.9772e-88,'s^-1'), n=29.6509, w0=(353165,'J/mol'), E0=(24419.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.045329884061335, var=154.7912430649373, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C
    Total Standard Deviation in ln(k): 30.08095712150698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C
Total Standard Deviation in ln(k): 30.08095712150698""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C
Total Standard Deviation in ln(k): 30.08095712150698
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C",
    kinetics = SurfaceArrheniusBM(A=(1.22872e-86,'s^-1'), n=29.1686, w0=(267509,'J/mol'), E0=(-29746.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.244909746502856, var=123.64249151965932, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C',), comment="""BM rule fitted to 23 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C
    Total Standard Deviation in ln(k): 27.93205734286632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C
Total Standard Deviation in ln(k): 27.93205734286632""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C
Total Standard Deviation in ln(k): 27.93205734286632
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H->C_Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi",
    kinetics = SurfaceArrheniusBM(A=(1.16414e-92,'s^-1'), n=30.8804, w0=(252596,'J/mol'), E0=(-44511,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5438074951974166, var=187.2955383899766, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 36.340033326604036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi
Total Standard Deviation in ln(k): 36.340033326604036""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi
Total Standard Deviation in ln(k): 36.340033326604036
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H->C_Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi",
    kinetics = SurfaceArrheniusBM(A=(4.87445e+198,'s^-1'), n=-54.9907, w0=(205954,'J/mol'), E0=(933666,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.133000233291183, var=298.9189470332864, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 57.60764801069082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi
Total Standard Deviation in ln(k): 57.60764801069082""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi
Total Standard Deviation in ln(k): 57.60764801069082
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi",
    kinetics = SurfaceArrheniusBM(A=(4.49896e-89,'s^-1'), n=29.8821, w0=(344133,'J/mol'), E0=(-9148.81,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6702478164200514, var=50.72095578478135, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 18.47405439075857"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi
Total Standard Deviation in ln(k): 18.47405439075857""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi
Total Standard Deviation in ln(k): 18.47405439075857
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H->C_N-Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi",
    kinetics = SurfaceArrheniusBM(A=(6.96061e-100,'s^-1'), n=33.1073, w0=(319595,'J/mol'), E0=(-4081.87,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2443722257418027, var=67.04182921438466, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 17.028585941164078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi
Total Standard Deviation in ln(k): 17.028585941164078""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_N-Sp-3Xo-1BrClFINOPSSi
Total Standard Deviation in ln(k): 17.028585941164078
""",
)

entry(
    index = 15,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H",
    kinetics = SurfaceArrheniusBM(A=(1.91296e-72,'s^-1'), n=25.0084, w0=(374444,'J/mol'), E0=(-21179.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.579197551449248, var=200.6143231476045, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H
    Total Standard Deviation in ln(k): 37.387702691636036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H
Total Standard Deviation in ln(k): 37.387702691636036""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H
Total Standard Deviation in ln(k): 37.387702691636036
""",
)

entry(
    index = 16,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H",
    kinetics = SurfaceArrheniusBM(A=(1.39491e+84,'s^-1'), n=-21.0841, w0=(334545,'J/mol'), E0=(470710,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2686185908882586, var=48.82090495536609, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H
    Total Standard Deviation in ln(k): 17.19496038201663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H
Total Standard Deviation in ln(k): 17.19496038201663""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H
Total Standard Deviation in ln(k): 17.19496038201663
""",
)

entry(
    index = 17,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_Sp-4Xo=2R!H",
    kinetics = SurfaceArrheniusBM(A=(3.93878e+14,'s^-1'), n=-0.519369, w0=(307625,'J/mol'), E0=(194870,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025128848229138637, var=21.42083667008411, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_Sp-4Xo=2R!H',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_Sp-4Xo=2R!H
    Total Standard Deviation in ln(k): 9.341582950587945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_Sp-4Xo=2R!H
Total Standard Deviation in ln(k): 9.341582950587945""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_Sp-4Xo=2R!H
Total Standard Deviation in ln(k): 9.341582950587945
""",
)

entry(
    index = 18,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H",
    kinetics = SurfaceArrheniusBM(A=(8.53211e-86,'s^-1'), n=28.9129, w0=(253351,'J/mol'), E0=(25335.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.596426755980361, var=144.2566073130645, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H',), comment="""BM rule fitted to 17 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H
    Total Standard Deviation in ln(k): 28.089368460683513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H
Total Standard Deviation in ln(k): 28.089368460683513""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H
Total Standard Deviation in ln(k): 28.089368460683513
""",
)

entry(
    index = 19,
    label = "Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H",
    kinetics = SurfaceArrheniusBM(A=(1.29274e-76,'s^-1'), n=26.23, w0=(382009,'J/mol'), E0=(23637.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8785728740557036, var=34.68732044701335, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H
    Total Standard Deviation in ln(k): 14.014545720355073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H
Total Standard Deviation in ln(k): 14.014545720355073""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H
Total Standard Deviation in ln(k): 14.014545720355073
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H",
    kinetics = SurfaceArrheniusBM(A=(2.33482e-102,'s^-1'), n=33.8453, w0=(310044,'J/mol'), E0=(-21864,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.123399954750533, var=79.78340712107436, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H
    Total Standard Deviation in ln(k): 23.24178180187642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H
Total Standard Deviation in ln(k): 23.24178180187642""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H
Total Standard Deviation in ln(k): 23.24178180187642
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet211",
    kinetics = SurfaceArrheniusBM(A=(1.66572e-96,'s^-1'), n=32.1169, w0=(359303,'J/mol'), E0=(-111606,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.719710184306593, var=404.72697562530703, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet211',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet211
    Total Standard Deviation in ln(k): 54.70204520318786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet211
Total Standard Deviation in ln(k): 54.70204520318786""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet211
Total Standard Deviation in ln(k): 54.70204520318786
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet111",
    kinetics = SurfaceArrheniusBM(A=(1.36582e+14,'s^-1'), n=-0.37593, w0=(385800,'J/mol'), E0=(145230,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004466518921338301, var=12.07865131720345, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet111',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet111
    Total Standard Deviation in ln(k): 6.978549693105444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet111
Total Standard Deviation in ln(k): 6.978549693105444""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_Sp-4Xo=2R!H_facet111
Total Standard Deviation in ln(k): 6.978549693105444
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet211",
    kinetics = SurfaceArrheniusBM(A=(6.20932e+12,'s^-1'), n=0, w0=(370000,'J/mol'), E0=(37000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet211',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet211
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet211
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet211
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet111",
    kinetics = SurfaceArrheniusBM(A=(7.50481e+63,'s^-1'), n=-15.0954, w0=(329480,'J/mol'), E0=(439593,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9410051857306686, var=35.1364401218806, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet111',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet111
    Total Standard Deviation in ln(k): 14.247602005266849"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet111
Total Standard Deviation in ln(k): 14.247602005266849""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_Sp-3Xo-1C_N-Sp-4Xo=2R!H_facet111
Total Standard Deviation in ln(k): 14.247602005266849
""",
)

entry(
    index = 25,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C",
    kinetics = SurfaceArrheniusBM(A=(1.48432e-89,'s^-1'), n=30.0236, w0=(268617,'J/mol'), E0=(26861.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6577561176061524, var=180.77732243415278, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C
    Total Standard Deviation in ln(k): 31.119572635851654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C
Total Standard Deviation in ln(k): 31.119572635851654""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C
Total Standard Deviation in ln(k): 31.119572635851654
""",
)

entry(
    index = 26,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C",
    kinetics = SurfaceArrheniusBM(A=(2.00361e-80,'s^-1'), n=27.3261, w0=(231541,'J/mol'), E0=(23154.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5088133856867854, var=163.5517415778455, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C
    Total Standard Deviation in ln(k): 29.429013952599565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C
Total Standard Deviation in ln(k): 29.429013952599565""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C
Total Standard Deviation in ln(k): 29.429013952599565
""",
)

entry(
    index = 27,
    label = "Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_1BrClFINOPSSi->N",
    kinetics = SurfaceArrheniusBM(A=(6.38238e-67,'s^-1'), n=23.3724, w0=(366238,'J/mol'), E0=(26750.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3397561716421878, var=27.4284732595876, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_1BrClFINOPSSi->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.352897351578957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.352897351578957""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.352897351578957
""",
)

entry(
    index = 28,
    label = "Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_N-1BrClFINOPSSi->N",
    kinetics = SurfaceArrheniusBM(A=(1.87167e-89,'s^-1'), n=30.0249, w0=(394625,'J/mol'), E0=(-2996.37,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2505612740098409, var=60.12111642236131, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 16.173827256734366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 16.173827256734366""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_Sp-4Xo-2R!H_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 16.173827256734366
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_1BrClFINOPSSi->N",
    kinetics = SurfaceArrheniusBM(A=(2.44546e-88,'s^-1'), n=29.6933, w0=(293874,'J/mol'), E0=(26899.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23693079588159865, var=69.74638598650373, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_1BrClFINOPSSi->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 17.33770852770335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 17.33770852770335""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 17.33770852770335
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_N-1BrClFINOPSSi->N",
    kinetics = SurfaceArrheniusBM(A=(2.8699e-102,'s^-1'), n=33.8118, w0=(320825,'J/mol'), E0=(-48531.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2059042864076641, var=198.90093469082322, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 28.790575843246433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 28.790575843246433""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-Sp-4Xo#2R!H_Sp-3Xo-1BrClFINOPSSi_N-Sp-4Xo-2R!H_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 28.790575843246433
""",
)

entry(
    index = 31,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet211",
    kinetics = SurfaceArrheniusBM(A=(2.372e-111,'s^-1'), n=36.4632, w0=(264151,'J/mol'), E0=(26415.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0133218637202246, var=329.2095267524814, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet211',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet211
    Total Standard Deviation in ln(k): 41.43277555653176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet211
Total Standard Deviation in ln(k): 41.43277555653176""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet211
Total Standard Deviation in ln(k): 41.43277555653176
""",
)

entry(
    index = 32,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet111",
    kinetics = SurfaceArrheniusBM(A=(5.04042e-75,'s^-1'), n=25.7305, w0=(271595,'J/mol'), E0=(27159.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.4207122795776777, var=168.47874293732096, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet111',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet111
    Total Standard Deviation in ln(k): 29.590962182410497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet111
Total Standard Deviation in ln(k): 29.590962182410497""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_Sp-3Xo=1C_facet111
Total Standard Deviation in ln(k): 29.590962182410497
""",
)

entry(
    index = 33,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet001",
    kinetics = SurfaceArrheniusBM(A=(6.20932e+12,'s^-1'), n=0, w0=(250138,'J/mol'), E0=(25013.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet001',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet001
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet001
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet001
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet111",
    kinetics = SurfaceArrheniusBM(A=(3.31481e-81,'s^-1'), n=27.5569, w0=(228442,'J/mol'), E0=(22844.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5215596528095472, var=207.83420158526891, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet111',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet111
    Total Standard Deviation in ln(k): 32.72418909786959"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet111
Total Standard Deviation in ln(k): 32.72418909786959""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-Sp-4Xo-2R!H_N-Sp-3Xo-1C_N-Sp-4Xo=2R!H_N-Sp-3Xo=1C_facet111
Total Standard Deviation in ln(k): 32.72418909786959
""",
)

